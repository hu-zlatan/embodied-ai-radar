"""Fetch GitHub stars / last push / archived flag for every GitHub repo linked from curated data.

Runs in GitHub Actions (repo-stats.yml) with GITHUB_TOKEN; writes data/repo_stats.json:
  {"updated": "YYYY-MM-DD", "repos": {"owner/repo": {"stars": int, "pushed": "YYYY-MM-DD", "archived": bool}},
   "feed": {"owner/repo": {"stars": int} | {"missing": true}}}
"repos" covers curated entries and resources. "feed" covers code links that authors put in the arXiv comments
of papers from the last FEED_DAYS days: such repos often 404 until the code is released, so the site shows
them as "code not public yet" instead of a broken link. Repos that fail to fetch (network, rate limit)
keep their previous values, so a flaky API never blanks the site.
Usage: python scripts/repo_stats.py
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

from radar import ROOT, load_arxiv_feed, load_curated, load_resources

OUT = ROOT / "data" / "repo_stats.json"
FEED_DAYS = 30
GH = re.compile(r"^https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:\.git)?/?(?:[#?].*)?$")


def repo_key(url: str | None) -> str | None:
    """'https://github.com/Owner/Repo' -> 'owner/repo' (lowercase); None for non-repo links."""
    m = GH.match(url or "")
    return f"{m.group(1)}/{m.group(2)}".lower() if m else None


def _load(section: str) -> dict:
    try:
        return json.loads(OUT.read_text(encoding="utf-8")).get(section, {})
    except (OSError, ValueError):
        return {}


def load_stats() -> dict:
    return _load("repos")


def load_feed_stats() -> dict:
    return _load("feed")


def apply_feed_stats(papers: list[dict], stats: dict) -> None:
    """Move feed code links whose repo is known to 404 into 'code_pending'; attach 'stars' when known."""
    for p in papers:
        live, pending = [], []
        for u in p.get("code") or []:
            st = stats.get(repo_key(u) or "")
            (pending if st and st.get("missing") else live).append(u)
            if st and "stars" in st and "stars" not in p:
                p["stars"] = st["stars"]
        if pending:
            p["code"] = live
            p["code_pending"] = pending


def wanted() -> set[str]:
    entries, _ = load_curated(strict=False)
    urls = [e.get(k) for e in entries for k in ("code", "url", "project")]
    resources, _ = load_resources()
    urls += [r.get("url") for r in resources]
    return {k for k in map(repo_key, urls) if k}


def feed_wanted(curated: set[str]) -> set[str]:
    cut = (dt.date.today() - dt.timedelta(days=FEED_DAYS)).isoformat()
    urls = [u for p in load_arxiv_feed() if p.get("published", "") >= cut for u in p.get("code") or []]
    return {k for k in map(repo_key, urls) if k} - curated


MISSING = {"missing": True}


def fetch(key: str, token: str | None) -> dict | None:
    """Repo stats, MISSING on HTTP 404, None when the API could not be reached."""
    req = urllib.request.Request(f"https://api.github.com/repos/{key}",
                                 headers={"Accept": "application/vnd.github+json", "User-Agent": "embodied-ai-radar"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                d = json.load(r)
            return {"stars": int(d["stargazers_count"]), "pushed": (d.get("pushed_at") or "")[:10],
                    "archived": bool(d.get("archived"))}
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"  {key}: 404 (not public, moved or deleted)")
                return MISSING
            time.sleep(2 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError, ValueError, KeyError):
            time.sleep(2 * (attempt + 1))
    print(f"  {key}: fetch failed, keeping previous value")
    return None


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN")
    old, old_feed = load_stats(), load_feed_stats()
    keys = sorted(wanted())
    new, ok = {}, 0
    for k in keys:
        got = fetch(k, token)
        if got and got is not MISSING:
            new[k] = got
            ok += 1
        elif k in old:  # curated 404s are caught by verify.yml; keep the last good value meanwhile
            new[k] = old[k]
    fkeys = sorted(feed_wanted(set(keys)))
    feed, fok = {}, 0
    for k in fkeys:
        got = fetch(k, token)
        if got:
            feed[k] = {"missing": True} if got is MISSING else {"stars": got["stars"]}
            fok += 1
        elif k in old_feed:
            feed[k] = old_feed[k]
    OUT.write_text(json.dumps({"updated": dt.date.today().isoformat(), "repos": new, "feed": feed},
                              indent=1, sort_keys=True) + "\n", encoding="utf-8")
    n_missing = sum(1 for v in feed.values() if v.get("missing"))
    print(f"{ok}/{len(keys)} curated repos fetched; feed: {fok}/{len(fkeys)} fetched, {n_missing} not found")
    return 0 if ok or not keys else 1


if __name__ == "__main__":
    sys.exit(main())
