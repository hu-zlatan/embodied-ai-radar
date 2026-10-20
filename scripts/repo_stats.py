"""Fetch GitHub stars / last push / archived flag for every GitHub repo linked from curated data.

Runs in GitHub Actions (repo-stats.yml) with GITHUB_TOKEN; writes data/repo_stats.json:
  {"updated": "YYYY-MM-DD", "repos": {"owner/repo": {"stars": int, "pushed": "YYYY-MM-DD", "archived": bool}}}
Repos that fail to fetch keep their previous values, so a flaky API never blanks the site.
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

from radar import ROOT, load_curated, load_resources

OUT = ROOT / "data" / "repo_stats.json"
GH = re.compile(r"^https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:\.git)?/?(?:[#?].*)?$")


def repo_key(url: str | None) -> str | None:
    """'https://github.com/Owner/Repo' -> 'owner/repo' (lowercase); None for non-repo links."""
    m = GH.match(url or "")
    return f"{m.group(1)}/{m.group(2)}".lower() if m else None


def load_stats() -> dict:
    try:
        return json.loads(OUT.read_text(encoding="utf-8")).get("repos", {})
    except (OSError, ValueError):
        return {}


def wanted() -> set[str]:
    entries, _ = load_curated(strict=False)
    urls = [e.get(k) for e in entries for k in ("code", "url", "project")]
    resources, _ = load_resources()
    urls += [r.get("url") for r in resources]
    return {k for k in map(repo_key, urls) if k}


def fetch(key: str, token: str | None) -> dict | None:
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
                print(f"  {key}: 404 (moved or deleted)")
                return None
            time.sleep(2 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError, ValueError, KeyError):
            time.sleep(2 * (attempt + 1))
    print(f"  {key}: fetch failed, keeping previous value")
    return None


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN")
    old = load_stats()
    keys = sorted(wanted())
    new, ok = {}, 0
    for k in keys:
        got = fetch(k, token)
        if got:
            new[k] = got
            ok += 1
        elif k in old:
            new[k] = old[k]
    OUT.write_text(json.dumps({"updated": dt.date.today().isoformat(), "repos": new}, indent=1, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(f"{ok}/{len(keys)} repos fetched; {len(new)} in {OUT.name}")
    return 0 if ok or not keys else 1


if __name__ == "__main__":
    sys.exit(main())
