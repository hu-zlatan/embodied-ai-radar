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
import xml.etree.ElementTree as ET

from radar import ARXIV_DIR, arxiv_get, classify, load_arxiv_feed, load_topics

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
    return arxiv_get(f"{API}?{params}")


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


RSS = "https://rss.arxiv.org/rss/cs.RO+cs.CV+cs.LG+cs.AI+cs.CL"
TITLE_KW = re.compile(r"\b(robot\w*|embodied|humanoid\w*|manipulat\w*|locomotion|vision-language-action|vla|vlas|"
                      r"sim-to-real|sim2real|tactile|visuotactile|quadruped\w*|dexterous|grasp\w*)\b", re.I)


ROBOT_CTX = re.compile(r"\b(robot\w*|embodied|humanoid\w*|vision-language-action|vla|quadruped\w*|legged|"
                       r"gripper|end-effector|sim-to-real|sim2real|teleoperat\w*)\b", re.I)


def is_relevant(rec: dict) -> bool:
    """cs.RO papers always count; cross-listed papers need a robotics title keyword AND robot context
    in the abstract (filters e.g. 'face manipulation' deepfake papers)."""
    if "cs.RO" in rec.get("categories", []):
        return True
    return bool(TITLE_KW.search(rec.get("title", "")) and ROBOT_CTX.search(rec.get("title", "") + " " + rec.get("abstract", "")))


def fetch_rss() -> list[dict]:
    """Today's arXiv announcements (new + cross-lists) from rss.arxiv.org. Empty on weekends/holidays."""
    import email.utils
    xml = arxiv_get(RSS, attempts=4)
    root = ET.fromstring(xml)
    out = []
    for it in root.iter("item"):
        link = clean(it.findtext("link"))
        m = re.search(r"abs/(\d{4}\.\d{4,5})", link)
        if not m:
            continue
        desc = it.findtext("description") or ""
        kind = re.search(r"Announce Type:\s*([\w-]+)", desc)
        if kind and kind.group(1) not in ("new", "cross"):
            continue  # skip replacements
        abstract = clean(desc.split("Abstract:", 1)[1] if "Abstract:" in desc else desc)
        title = clean(it.findtext("title"))
        cats = [clean(c.text) for c in it.findall("category") if c.text]
        creators = [clean(c.text) for c in it if c.tag.endswith("creator") and c.text]
        authors = [a.strip() for a in ",".join(creators).split(",") if a.strip()]
        try:
            date = email.utils.parsedate_to_datetime(clean(it.findtext("pubDate"))).date().isoformat()
        except (TypeError, ValueError):
            date = dt.datetime.now(dt.timezone.utc).date().isoformat()
        code = sorted({u.rstrip(".") for u in GITHUB_RE.findall(abstract)})
        project = sorted({u.rstrip(".") for u in URL_RE.findall(abstract) if "github.io" in u or "sites.google.com" in u})
        rec = {
            "id": m.group(1), "title": title,
            "authors": authors[:8] + ([f"+{len(authors) - 8}"] if len(authors) > 8 else []),
            "abstract": abstract if len(abstract) <= ABSTRACT_MAX else abstract[:ABSTRACT_MAX].rsplit(" ", 1)[0] + " …",
            "published": date, "primary": "cs.RO" if "cs.RO" in cats else (cats[0] if cats else ""), "categories": cats,
        }
        if code:
            rec["code"] = code[:3]
        if project:
            rec["project"] = project[:2]
        if is_relevant(rec):
            out.append(rec)
    return out


def retag() -> int:
    topics = load_topics()
    for path in sorted(ARXIV_DIR.glob("*/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        before = len(data.get("papers", []))
        data["papers"] = [p for p in data.get("papers", []) if is_relevant(p)]
        if len(data["papers"]) != before:
            print(f"{path.name}: dropped {before - len(data['papers'])} off-topic cross-lists")
        for p in data["papers"]:
            p["topics"] = classify(p.get("abstract", ""), topics, title=p.get("title", ""))
        path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("retagged")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=3, help="API look-back window in days")
    ap.add_argument("--no-api", action="store_true", help="only use the RSS feed")
    ap.add_argument("--retag", action="store_true", help="re-run topic tagging on all stored papers and exit")
    args = ap.parse_args()
    if args.retag:
        return retag()
    cutoff = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.days)).strftime("%Y-%m-%d")
    topics = load_topics()
    known = {p["id"] for p in load_arxiv_feed()}
    new: dict[str, dict] = {}
    ok_sources = 0

    def add(r: dict) -> None:
        if r["id"] not in known and r["id"] not in new:
            r["topics"] = classify(r["abstract"], topics, title=r["title"])
            new[r["id"]] = r

    # 1) RSS: today's announcements; a different host from the API and rarely rate-limited.
    try:
        recs = fetch_rss()
        ok_sources += 1
        print(f"rss: {len(recs)} relevant items")
        for r in recs:
            add(r)
    except Exception as ex:
        print(f"warning: RSS failed: {ex}")
    # 2) API: fills gaps (missed days, backfills). Rate-limited on shared CI IPs, so failures are tolerated.
    if not args.no_api:
        try:
            for q in QUERIES:
                print(f"api query: {q[:70]}…")
                for start in range(0, MAX_PER_QUERY, PAGE):
                    recs = parse(fetch(q, start))
                    time.sleep(3)
                    if not recs:
                        break
                    for r in recs:
                        if r["published"] >= cutoff and is_relevant(r):
                            add(r)
                    if recs[-1]["published"] < cutoff:
                        break
            ok_sources += 1
        except Exception as ex:
            print(f"warning: API failed: {ex}")
    if ok_sources == 0:
        print("error: no arXiv source reachable")
        return 1
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
        path.write_text(json.dumps({"date": date, "source": "arXiv RSS/API (metadata CC0)", "papers": merged},
                                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"{path.relative_to(ARXIV_DIR.parent.parent)}: +{len(merged) - len(existing)} (total {len(merged)})")
    print(f"done: {len(new)} new papers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
