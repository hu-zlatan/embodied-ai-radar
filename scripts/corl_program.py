"""CoRL 2026 program from the official accepted-papers page (runs in GitHub Actions; needs network).

The page embeds its whole program: 687 accepted papers with OpenReview links, oral and spotlight
sessions, poster numbers, rooms and times. This stores those facts in data/program/corl-2026.json
and finds each paper's arXiv version by exact title, so the site can link code and abstracts.
A paper is only linked to arXiv when the titles match; the rest keep their OpenReview link.

Usage: python scripts/corl_program.py [--parse-only] [--minutes 45]
"""
import argparse
import datetime as dt
import difflib
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request

from intake_arxiv import API, enrich_topics, parse
from radar import PROGRAM_DIR, VENUE_PAPERS, arxiv_get, load_arxiv_feed, load_curated, load_program, load_topics, load_venue_papers, norm_title
from venue_backfill import hf_links, save

URL = "https://www.corl.org/program/accepted-papers"
OUT = PROGRAM_DIR / "corl-2026.json"
RECHECK_DAYS = 3  # authors post preprints around the conference (Nov 9-12), so look again more often
BROWSER = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"}
MIN_PAPERS = 600  # below this the page changed shape: keep the stored program
AWARDS_URLS = ("https://www.corl.org/program/awards", "https://2026.corl.org/program/awards")
AWARDS_OUT = PROGRAM_DIR / "corl-2026-awards.txt"  # plain-text snapshot for the agent to read; not used by the site
TITLE_RATIO = 0.95  # arXiv titles differ in small ways from the submitted one (hyphens, a changed word)


def embedded_html(page: str) -> str:
    """The list sits in a Google Sites custom embed: an HTML-escaped data-code attribute."""
    m = re.search(r'data-code="([^"]*)"', page)
    code = html.unescape(m.group(1)) if m else page
    if "\\u003c" in code or '\\"' in code:  # JS-escaped inside the attribute
        code = code.encode("utf-8").decode("unicode_escape").encode("latin-1", "replace").decode("utf-8", "replace")
    return code


def plain(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<br\s*/?>", " · ", s).replace("&middot;", "·"))).strip()


def strip_tags(s: str) -> str:
    return plain(re.sub(r"<(?!br)[^>]+>", " ", s))


def parse_program(code: str) -> dict:
    sub = re.search(r'<p class="sub">(.*?)</p>', code, re.S)
    days, sessions, papers = [], [], {}
    for day in re.split(r'(?=<section class="day")', code)[1:]:
        d_id = re.search(r'id="day-(\w+)"', day).group(1)
        days.append({"id": d_id, "label": strip_tags(re.search(r"<h2>(.*?)</h2>", day, re.S).group(1))})
        for sec in re.split(r'(?=<section class="session)', day)[1:]:
            head = re.search(r'<h3[^>]*class="(\w+)"[^>]*><span class="tag">(.*?)</span>(.*?)</h3>', sec, re.S)
            if not head:
                continue
            kind, tag, name = head.group(1), strip_tags(head.group(2)), strip_tags(head.group(3))
            meta = re.search(r'<p class="meta">(.*?)</p>', sec, re.S)
            if kind == "poster":
                sid = "P" + re.search(r"(\d+)", name).group(1)
            else:
                sid = tag.split()[-1]
            sessions.append({"id": sid, "kind": kind, "name": name, "day": d_id, "where": plain(meta.group(1)) if meta else ""})
            rows = (re.findall(r'<tr class="paper"><td class="num">(\d+)</td><td><a href="[^"]*[?&]id=([\w-]+)"[^>]*>(.*?)</a>', sec, re.S)
                    if kind == "poster" else
                    [("", i, t) for i, t in re.findall(r'<li class="paper"><a href="[^"]*[?&]id=([\w-]+)"[^>]*>(.*?)</a>', sec, re.S)])
            for num, or_id, title in rows:
                p = papers.setdefault(or_id, {"or": or_id, "title": strip_tags(title), "sessions": []})
                if kind == "poster":
                    p["poster"], p["poster_no"] = sid, int(num)
                elif sid not in p["sessions"]:
                    p["sessions"].append(sid)
    return {"sub": plain(strip_tags(sub.group(1))) if sub else "", "days": days, "sessions": sessions,
            "papers": list(papers.values())}


def query_title(title: str, words: int | None = None) -> list[dict]:
    clean_t = re.sub(r"[^A-Za-z0-9 ]+", " ", title)
    if words:  # every long word instead of the exact phrase: finds a retitled or reworded paper
        toks = sorted({w.lower() for w in clean_t.split() if len(w) > 3}, key=len, reverse=True)[:words]
        q = " AND ".join(f"ti:{w}" for w in toks)
    else:
        q = 'ti:"' + " ".join(clean_t.split()) + '"'
    url = API + "?" + urllib.parse.urlencode({"search_query": q, "start": 0, "max_results": 10})
    return parse(arxiv_get(url, attempts=3))


def best_match(title: str, recs: list[dict]) -> dict | None:
    want = norm_title(title)
    for r in recs:
        if norm_title(r["title"]) == want:
            return r
    scored = [(difflib.SequenceMatcher(None, want, norm_title(r["title"])).ratio(), r) for r in recs]
    scored = [x for x in scored if x[0] >= TITLE_RATIO]
    return max(scored, key=lambda x: x[0])[1] if scored else None


def awards_snapshot() -> None:
    """Save the official awards page as plain text (best effort), so award finalists can be checked
    against the source before any honor is added to curated entries. Never fails the run."""
    for url in AWARDS_URLS:
        try:
            page = urllib.request.urlopen(urllib.request.Request(url, headers=BROWSER), timeout=60).read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001 - network or HTTP error: try the next address
            print(f"awards: {url}: {e}")
            continue
        parts = [page] + [html.unescape(m) for m in re.findall(r'data-code="([^"]*)"', page)]
        text = "\n".join(strip_tags(re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", x)) for x in parts)
        text = re.sub(r"\s*(Best |Finalist|Winner|Honorable)", r"\n\1", text)[:40000]
        if not re.search(r"(?i)best (student )?paper|finalist", text):
            print(f"awards: {url}: no award text ({len(text)} chars)")
            continue
        AWARDS_OUT.write_text(f"source: {url}\nfetched: {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC\n\n{text}\n", encoding="utf-8")
        print(f"awards: saved {len(text)} chars from {url}")
        return


def write(prog: dict) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(prog, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parse-only", action="store_true")
    ap.add_argument("--minutes", type=float, default=45)
    args = ap.parse_args()
    today = dt.date.today()
    awards_snapshot()
    t = urllib.request.urlopen(urllib.request.Request(URL, headers=BROWSER), timeout=60).read().decode("utf-8", "replace")
    fresh = parse_program(embedded_html(t))
    n_rows = len(fresh["papers"])
    print(f"parsed: {n_rows} papers, {len(fresh['sessions'])} sessions")
    if n_rows < MIN_PAPERS:
        print(f"warning: only {n_rows} papers parsed; keeping the stored program")
        return 1
    old = {p["or"]: p for p in (load_program("corl-2026") or {}).get("papers", [])}
    for p in fresh["papers"]:  # keep earlier matches
        for f in ("arxiv", "phrase_checked", "checked"):
            if f in old.get(p["or"], {}):
                p[f] = old[p["or"]][f]
    fresh.update({"updated": today.isoformat(), "source": URL, "venue": "CoRL 2026"})
    write(fresh)
    if args.parse_only:
        return 0

    feed = load_arxiv_feed()
    venue_recs = {p["id"]: p for p in load_venue_papers()}
    known = {norm_title(p["title"]): p["id"] for p in feed + list(venue_recs.values())}
    known.update({norm_title(e["title"]): str(e["arxiv"]) for e in load_curated()[0] if e.get("arxiv")})
    local = 0
    for p in fresh["papers"]:
        k = known.get(norm_title(p["title"]))
        if k and not p.get("arxiv"):
            p["arxiv"] = k
            local += 1
    print(f"matched locally: {local}")
    write(fresh)

    topics = load_topics()
    cut = (today - dt.timedelta(days=RECHECK_DAYS)).isoformat()
    stop = time.time() + args.minutes * 60
    errors = found = asked = 0
    new: dict[str, dict] = {}
    for words in (None, 6):  # exact phrase first, then long words for what is still missing
        for p in fresh["papers"]:
            done = "checked" if words else "phrase_checked"
            if p.get("arxiv") or p.get(done, "") >= cut:
                continue
            if time.time() > stop or errors >= 8:
                break
            try:
                recs = query_title(p["title"], words)
                errors = 0
            except Exception as ex:
                errors += 1
                print(f"warning: arXiv query failed ({errors}): {ex}", flush=True)
                time.sleep(20)
                continue
            asked += 1
            r = best_match(p["title"], recs)
            if r:
                p["arxiv"] = r["id"]
                found += 1
                if r["id"] not in venue_recs and r["id"] not in {x["id"] for x in feed}:
                    new[r["id"]] = r
            else:
                p[done] = today.isoformat()
            time.sleep(3.1)
            if asked % 25 == 0:
                write(fresh)
                print(f"  {asked} asked, {found} found", flush=True)
    enrich_topics(new.values(), topics)
    venue_recs.update(new)
    write(fresh)
    if new:
        save(venue_recs)
        try:
            hf_links(venue_recs)
            save(venue_recs)
        except Exception as ex:
            print(f"warning: hugging face links failed: {ex}")
    linked = sum(1 for p in fresh["papers"] if p.get("arxiv"))
    print(f"done: {linked}/{n_rows} linked to arXiv, {asked} queries, {found} new matches, {len(new)} new records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
