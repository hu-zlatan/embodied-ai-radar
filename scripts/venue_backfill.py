"""Backfill papers accepted at this season's venues (runs in GitHub Actions; needs network).

The daily feed only reaches back to its first day (2026-10-12), so a venue page misses papers posted
before that. arXiv's API can search the comment field: this asks for each venue's comments, keeps
papers where venue_of() reads an accepted venue (same conservative rule as the badges) and that pass
is_relevant(), and stores them in data/venue_papers.json. They appear on venue pages and in search,
not on the day pages. Saved after every venue, so a rate limit keeps what was already fetched.

Usage: python scripts/venue_backfill.py [--venues "CoRL 2026,IROS 2026"]
"""
import argparse
import datetime as dt
import json
import sys
import time
import urllib.error
import urllib.request

from hf_papers import UA, clean_github, clean_url
from intake_arxiv import PAGE, enrich_topics, fetch, is_relevant, parse
from radar import VENUE_PAPERS, load_topics, load_venue_papers, venue_of

# (venue as venue_of() reports it, first submission date to search from)
VENUES = [("CoRL 2026", "202604010000"), ("Humanoids 2026", "202604010000"), ("NeurIPS 2026", "202604010000"),
          ("IROS 2026", "202601010000"), ("RSS 2026", "202601010000"), ("ICRA 2026", "202507010000")]
MAX_PER_VENUE = 1000
HF_API = "https://huggingface.co/api/papers/{id}"
HF_MAX = 1200
HF_RECHECK_DAYS = 14


def fetch_venue(venue: str, since: str) -> dict[str, dict]:
    name = venue.rsplit(" ", 1)[0]
    query = f'co:"{name}" AND submittedDate:[{since} TO 203001010000]'
    got: dict[str, dict] = {}
    for start in range(0, MAX_PER_VENUE, PAGE):
        recs = parse(fetch(query, start))
        time.sleep(4)
        for r in recs:
            if venue_of(r.get("comment")) == venue and is_relevant(r):
                got[r["id"]] = r
        print(f"  {venue}: {start + len(recs)} scanned, {len(got)} kept", flush=True)
        if len(recs) < PAGE:
            break
    return got


def hf_links(papers: dict[str, dict]) -> int:
    """Best-effort: GitHub / project links from Hugging Face paper pages, for papers whose arXiv text has none.
    Most authors put code on a project page or HF, not in the arXiv comment. Rechecked after HF_RECHECK_DAYS."""
    today = dt.date.today()
    cut = (today - dt.timedelta(days=HF_RECHECK_DAYS)).isoformat()
    todo = [p for p in papers.values() if not p.get("code") and p.get("hf_checked", "") < cut]
    todo.sort(key=lambda p: p.get("published", ""), reverse=True)
    found = errors = 0
    for p in todo[:HF_MAX]:
        req = urllib.request.Request(HF_API.format(id=p["id"]), headers=UA)
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                d = json.load(r)
        except urllib.error.HTTPError as ex:
            if ex.code == 404:  # no HF page for this paper
                p["hf_checked"] = today.isoformat()
                continue
            errors += 1
            d = None
        except (urllib.error.URLError, TimeoutError, ValueError):
            errors += 1
            d = None
        if d is None:
            if errors >= 10:
                print("warning: too many Hugging Face errors, stopping")
                break
            continue
        p["hf_checked"] = today.isoformat()
        gh, pj = clean_github(d.get("githubRepo")), clean_url(d.get("projectPage"))
        if gh:
            p["code"] = [gh]
            found += 1
        if pj and not p.get("project"):
            p["project"] = [pj]
        time.sleep(0.3)
    print(f"hugging face: {len(todo)} to check, {found} code links found, {errors} errors")
    return found


def save(papers: dict[str, dict]) -> None:
    body = sorted(papers.values(), key=lambda p: (p.get("published", ""), p["id"]), reverse=True)
    VENUE_PAPERS.write_text(json.dumps({"updated": dt.date.today().isoformat(), "source": "arXiv API (metadata CC0)",
                                        "papers": body}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--venues", default="", help="comma-separated subset, e.g. 'CoRL 2026,IROS 2026'")
    args = ap.parse_args()
    only = {v.strip() for v in args.venues.split(",") if v.strip()}
    topics = load_topics()
    papers = {p["id"]: p for p in load_venue_papers()}
    ok = 0
    for venue, since in VENUES:
        if only and venue not in only:
            continue
        try:
            got = fetch_venue(venue, since)
        except Exception as ex:  # keep what earlier venues gave; the next run retries
            print(f"warning: {venue}: {ex}")
            continue
        enrich_topics(got.values(), topics)
        for k, r in got.items():  # keep links found earlier on Hugging Face
            old = papers.get(k, {})
            for f in ("code", "project"):
                if old.get(f) and not r.get(f):
                    r[f] = old[f]
            if old.get("hf_checked"):
                r["hf_checked"] = old["hf_checked"]
        papers.update(got)
        save(papers)
        ok += 1
    try:
        hf_links(papers)
        save(papers)
    except Exception as ex:  # never lose the arXiv results over optional links
        print(f"warning: hugging face links failed: {ex}")
    print(f"done: {ok} venues fetched, {len(papers)} papers stored")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
