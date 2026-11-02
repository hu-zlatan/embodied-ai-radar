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

from intake_arxiv import PAGE, enrich_topics, fetch, is_relevant, parse
from radar import VENUE_PAPERS, load_topics, load_venue_papers, venue_of

# (venue as venue_of() reports it, first submission date to search from)
VENUES = [("CoRL 2026", "202604010000"), ("Humanoids 2026", "202604010000"), ("NeurIPS 2026", "202604010000"),
          ("IROS 2026", "202601010000"), ("RSS 2026", "202601010000"), ("ICRA 2026", "202507010000")]
MAX_PER_VENUE = 1000


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
        papers.update(got)
        save(papers)
        ok += 1
    print(f"done: {ok} venues fetched, {len(papers)} papers stored")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
