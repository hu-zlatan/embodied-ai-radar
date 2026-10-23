"""Community signal: which of our papers made it onto Hugging Face Daily Papers, and how many upvotes they have.

Runs in GitHub Actions (repo-stats.yml). For each of the last DAYS days it reads the public list
https://huggingface.co/api/daily_papers?date=YYYY-MM-DD and keeps only arXiv IDs that are in our daily feed or
curated data. Writes data/hf_papers.json:
  {"updated": "YYYY-MM-DD", "papers": {"<arxiv id>": {"upvotes": int, "date": "YYYY-MM-DD"}}}
"date" is the day the paper was listed on Hugging Face. Days that fail to fetch keep their previous values,
entries older than KEEP_DAYS are dropped. Upvote counts come straight from Hugging Face; nothing is estimated.
Usage: python scripts/hf_papers.py
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import time
import urllib.error
import urllib.request

from radar import ROOT, load_arxiv_feed, load_curated

OUT = ROOT / "data" / "hf_papers.json"
API = "https://huggingface.co/api/daily_papers?date={d}"
DAYS = 21
KEEP_DAYS = 60
UA = {"User-Agent": "embodied-ai-radar/1.0 (+https://github.com/hu-zlatan/embodied-ai-radar)"}


def load() -> dict[str, dict]:
    try:
        d = json.loads(OUT.read_text(encoding="utf-8")).get("papers", {})
        return {k: v for k, v in d.items() if isinstance(v, dict) and isinstance(v.get("upvotes"), int)}
    except (OSError, ValueError, AttributeError):
        return {}


def fetch_day(day: str) -> list[dict] | None:
    """The day's list, [] when Hugging Face has none, None when it could not be fetched."""
    req = urllib.request.Request(API.format(d=day), headers=UA)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.load(r)
            return data if isinstance(data, list) else []
        except urllib.error.HTTPError as e:
            if e.code in (400, 404):
                return []
            time.sleep(3 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError, ValueError):
            time.sleep(3 * (attempt + 1))
    return None


def main() -> int:
    ours = {p["id"] for p in load_arxiv_feed()}
    entries, _ = load_curated(strict=False)
    ours |= {str(e["arxiv"]) for e in entries if e.get("arxiv")}
    old = load()
    new: dict[str, dict] = {}
    today = dt.date.today()
    ok = 0
    for i in range(DAYS):
        day = (today - dt.timedelta(days=i)).isoformat()
        items = fetch_day(day)
        if items is None:
            print(f"  {day}: fetch failed, keeping previous values")
            continue
        ok += 1
        for it in items:
            p = it.get("paper") if isinstance(it, dict) else None
            if not isinstance(p, dict):
                continue
            pid, up = str(p.get("id", "")), p.get("upvotes")
            if pid in ours and isinstance(up, int) and pid not in new:
                new[pid] = {"upvotes": up, "date": day}
        time.sleep(0.5)
    cut = (today - dt.timedelta(days=KEEP_DAYS)).isoformat()
    for pid, v in old.items():
        if pid not in new and pid in ours and str(v.get("date", "")) >= cut:
            new[pid] = v
    OUT.write_text(json.dumps({"updated": today.isoformat(), "papers": new}, indent=1, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(f"{ok}/{DAYS} days fetched; {len(new)} of our papers are on Hugging Face Daily Papers")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
