"""Daily arXiv intake (runs in GitHub Actions; needs network).

Fetches recent cs.RO papers plus robotics/embodied papers from cs.CV, cs.LG, cs.AI and cs.CL,
tags them by topic with keyword rules, detects code / project links, and merges them into
data/arxiv/YYYY/MM-DD.json (one file per UTC publication date). Existing records are kept.

Usage: python scripts/intake_arxiv.py [--days 3]
arXiv metadata is CC0. Please respect arXiv's API terms: one request every 3 seconds.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from radar import ARXIV_DIR, classify, load_arxiv_feed, load_topics

API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
QUERIES = [
    "cat:cs.RO",
    "(cat:cs.CV OR cat:cs.LG OR cat:cs.AI OR cat:cs.CL) AND (ti:robot OR ti:robotic OR ti:robots"
    " OR ti:embodied OR ti:humanoid OR ti:manipulation OR ti:locomotion OR ti:\"vision-language-action\""
    " OR ti:VLA OR ti:\"sim-to-real\" OR ti:tactile OR ti:quadruped OR ti:dexterous)",
]
PAGE = 200
MAX_PER_QUERY = 1000
GITHUB_RE = re.compile(r"https?://github\.com/[\w.-]+/[\w.-]+", re.I)
URL_RE = re.compile(r"https?://[^\s,;()<>\"']+", re.I)
ABSTRACT_MAX = 600


def fetch(query: str, start: int) -> bytes:
    params = urllib.parse.urlencode({
        "search_query": query, "start": start, "max_results": PAGE,
        "sortBy": "submittedDate", "sortOrder": "descending",
    })
    req = urllib.request.Request(f"{API}?{params}", headers={
        "User-Agent": "embodied-ai-radar/1.0 (+https://github.com/hu-zlatan/embodied-ai-radar)"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as ex:  # network hiccups: back off and retry
            print(f"  fetch failed ({ex}); retry {attempt + 1}")
            time.sleep(10 * (attempt + 1))
    raise RuntimeError("arXiv API unreachable")


def clean(s: str | None) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def parse(xml: bytes) -> list[dict]:
    root = ET.fromstring(xml)
    out = []
    for e in root.findall("a:entry", NS):
        raw_id = clean(e.findtext("a:id", default="", namespaces=NS))
        m = re.search(r"abs/([^v\s]+)(v\d+)?$", raw_id)
        if not m:
            continue
        aid = m.group(1)
        abstract = clean(e.findtext("a:summary", default="", namespaces=NS))
        comment = clean(e.findtext("arxiv:comment", default="", namespaces=NS))
        authors = [clean(a.findtext("a:name", default="", namespaces=NS)) for a in e.findall("a:author", NS)]
        cats = [c.get("term") for c in e.findall("a:category", NS) if c.get("term")]
        prim = e.find("arxiv:primary_category", NS)
        text_links = abstract + " " + comment
        code = sorted({u.rstrip(".") for u in GITHUB_RE.findall(text_links)})
        project = sorted({u.rstrip(".") for u in URL_RE.findall(text_links)
                          if "github.io" in u or "sites.google.com" in u})
        rec = {
            "id": aid,
            "title": clean(e.findtext("a:title", default="", namespaces=NS)),
            "authors": authors[:8] + ([f"+{len(authors) - 8}"] if len(authors) > 8 else []),
            "abstract": abstract if len(abstract) <= ABSTRACT_MAX else abstract[:ABSTRACT_MAX].rsplit(" ", 1)[0] + " …",
            "published": clean(e.findtext("a:published", default="", namespaces=NS))[:10],
            "primary": prim.get("term") if prim is not None else (cats[0] if cats else ""),
            "categories": cats,
        }
        if comment:
            rec["comment"] = comment[:200]
        if code:
            rec["code"] = code[:3]
        if project:
            rec["project"] = project[:2]
        out.append(rec)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=3, help="look back this many days")
    args = ap.parse_args()
    cutoff = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.days)).strftime("%Y-%m-%d")
    topics = load_topics()
    known = {p["id"] for p in load_arxiv_feed()}
    new: dict[str, dict] = {}
    for q in QUERIES:
        print(f"query: {q[:70]}…")
        for start in range(0, MAX_PER_QUERY, PAGE):
            recs = parse(fetch(q, start))
            time.sleep(3)
            if not recs:
                break
            for r in recs:
                if r["published"] >= cutoff and r["id"] not in known:
                    r["topics"] = classify(r["title"] + " " + r["abstract"], topics)
                    new.setdefault(r["id"], r)
            if recs[-1]["published"] < cutoff:
                break
    by_date: dict[str, list[dict]] = {}
    for r in new.values():
        by_date.setdefault(r["published"], []).append(r)
    for date, recs in sorted(by_date.items()):
        path = ARXIV_DIR / date[:4] / f"{date[5:]}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        existing = []
        if path.exists():
            try:
                existing = json.loads(path.read_text(encoding="utf-8")).get("papers", [])
            except json.JSONDecodeError:
                print(f"warning: {path} was malformed; rewriting")
        ids = {p.get("id") for p in existing}
        merged = existing + [r for r in recs if r["id"] not in ids]
        merged.sort(key=lambda p: p["id"], reverse=True)
        path.write_text(json.dumps({"date": date, "source": "arXiv API (metadata CC0)", "papers": merged},
                                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"{path.relative_to(ARXIV_DIR.parent.parent)}: +{len(merged) - len(existing)} (total {len(merged)})")
    print(f"done: {len(new)} new papers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
