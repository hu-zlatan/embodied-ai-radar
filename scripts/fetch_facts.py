"""Facts for hand-written curated entries (dispatched by the maintainer agent; runs in GitHub Actions).

The agent's own tools usually cannot open arXiv, Hugging Face or the GitHub API. Given arXiv IDs, this writes
.autopilot/facts.json with each paper's title, authors, full abstract and comment, the repo and project page
Hugging Face lists, and the stars of every candidate repo. The file is replaced on every run and is not
published on the site.

Usage: python scripts/fetch_facts.py --ids 2406.19464,2502.17432 [--repos owner/name,owner/name]
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import time
import urllib.request
import xml.etree.ElementTree as ET

from intake_arxiv import ENRICH_BATCH, NS, clean, fetch_ids, parse
from radar import ROOT, arxiv_get
from repo_stats import fetch as repo_fetch, repo_key

OUT = ROOT / ".autopilot" / "facts.json"
ID_RE = re.compile(r"^\d{4}\.\d{4,5}$")
REPO_RE = re.compile(r"^[\w.-]+/[\w.-]+$")


def from_api(ids: list[str]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for i in range(0, len(ids), ENRICH_BATCH):
        chunk = ids[i:i + ENRICH_BATCH]
        try:
            xml = fetch_ids(chunk)
            short = {r["id"]: r for r in parse(xml)}
            for e in ET.fromstring(xml).findall("a:entry", NS):
                m = re.search(r"abs/([^v\s]+)(v\d+)?$", clean(e.findtext("a:id", default="", namespaces=NS)))
                if m and m.group(1) in short:
                    r = short[m.group(1)]
                    out[r["id"]] = {
                        "title": r["title"], "published": r["published"], "comment": r.get("comment"),
                        "code": r.get("code", []), "project": r.get("project", []),
                        "abstract": clean(e.findtext("a:summary", default="", namespaces=NS))[:4000],
                        "authors": [clean(a.findtext("a:name", default="", namespaces=NS))
                                    for a in e.findall("a:author", NS)][:20]}
        except Exception as ex:  # 429s are common from runners; the abs-page fallback covers them
            print(f"warning: API batch failed: {ex}", flush=True)
        time.sleep(4)
    return out


def from_abs_page(aid: str) -> dict | None:
    try:
        page = arxiv_get(f"https://arxiv.org/abs/{aid}", attempts=3).decode("utf-8", "replace")
    except Exception as ex:
        print(f"warning: abs page {aid}: {ex}", flush=True)
        return None
    def metas(name: str) -> list[str]:
        return [" ".join(html.unescape(v).split()) for v in re.findall(rf'<meta name="{name}" content="([^"]*)"', page)]
    title, abstract = metas("citation_title"), metas("citation_abstract")
    if not title:
        return None
    return {"title": title[0], "abstract": abstract[0][:4000] if abstract else "", "comment": None,
            "authors": metas("citation_author")[:20], "code": [], "project": []}


def from_hf(aid: str) -> dict:
    req = urllib.request.Request(f"https://huggingface.co/api/papers/{aid}", headers={"User-Agent": "embodied-ai-radar"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.load(r)
    except Exception:
        return {}
    return {"hf_github": d.get("githubRepo"), "hf_project": d.get("projectPage")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", default="")
    ap.add_argument("--repos", default="")
    args = ap.parse_args()
    ids = list(dict.fromkeys(x.strip() for x in args.ids.split(",") if ID_RE.match(x.strip())))
    papers = from_api(ids)
    for aid in ids:
        if aid not in papers:
            rec = from_abs_page(aid)
            if rec:
                papers[aid] = rec
            time.sleep(2)
        if aid in papers:
            papers[aid].update(from_hf(aid))
    repos = {x.strip() for x in args.repos.split(",") if REPO_RE.match(x.strip())}
    for p in papers.values():
        for u in p.get("code", []) + [p.get("hf_github")]:
            key = repo_key(u)
            if key:
                repos.add(key)
    token = os.environ.get("GITHUB_TOKEN")
    stats = {r: repo_fetch(r, token) for r in sorted(repos)}
    OUT.write_text(json.dumps({"updated": dt.date.today().isoformat(), "missing": [a for a in ids if a not in papers],
                               "papers": papers, "repos": stats}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(papers)}/{len(ids)} papers, {len(repos)} repos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
