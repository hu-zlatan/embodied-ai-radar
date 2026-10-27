"""Community signal: which of our papers made it onto Hugging Face Daily Papers, and how many upvotes they have.

Runs in GitHub Actions (repo-stats.yml). For each of the last DAYS days it reads the public list
https://huggingface.co/api/daily_papers?date=YYYY-MM-DD and keeps only arXiv IDs that are in our daily feed or
curated data. Writes data/hf_papers.json:
  {"updated": "YYYY-MM-DD", "papers": {"<arxiv id>": {"upvotes": int, "date": "YYYY-MM-DD",
                                                     "github": url?, "project": url?}}}
"date" is the day the paper was listed on Hugging Face; "github" / "project" are the links the authors (or HF users)
attached to the paper page, kept only when they are plain https URLs (github: a github.com/<owner>/<repo> URL).
The site uses them for feed papers whose arXiv comment names no code / project link; repo_stats.py checks the
GitHub links like any other feed code link (404 -> 'not public yet').
Also writes .autopilot/review_queue.json for the maintainer agent: our not-yet-curated papers with the most
upvotes, with the full abstract and links as listed on Hugging Face (input for picks; not published on the site). Days that fail to fetch keep their previous values,
entries older than KEEP_DAYS are dropped. Upvote counts come straight from Hugging Face; nothing is estimated.
Usage: python scripts/hf_papers.py
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import time
import urllib.error
import urllib.request

from radar import ROOT, load_arxiv_feed, load_curated

OUT = ROOT / "data" / "hf_papers.json"
QUEUE = ROOT / ".autopilot" / "review_queue.json"
QUEUE_MIN_UPVOTES = 5
QUEUE_MAX = 40
GH_RE = re.compile(r"^https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/?$")
API = "https://huggingface.co/api/daily_papers?date={d}"
DAYS = 21
KEEP_DAYS = 60
UA = {"User-Agent": "embodied-ai-radar/1.0 (+https://github.com/hu-zlatan/embodied-ai-radar)"}


def load() -> dict[str, dict]:
    try:
        d = json.loads(OUT.read_text(encoding="utf-8")).get("papers", {})
        out = {}
        for k, v in d.items():
            if not (isinstance(v, dict) and isinstance(v.get("upvotes"), int)):
                continue
            rec = {"upvotes": v["upvotes"], "date": str(v.get("date", ""))}
            gh, pj = clean_github(v.get("github")), clean_url(v.get("project"))
            if gh:
                rec["github"] = gh
            if pj:
                rec["project"] = pj
            out[str(k)] = rec
        return out
    except (OSError, ValueError, AttributeError):
        return {}


def clean_github(u) -> str | None:
    if not isinstance(u, str):
        return None
    u = u.strip().replace("http://", "https://", 1).removesuffix(".git").rstrip("/")
    if u.startswith("https://www.github.com/"):
        u = "https://github.com/" + u[len("https://www.github.com/"):]
    return u if GH_RE.match(u) else None


def clean_url(u) -> str | None:
    if not isinstance(u, str):
        return None
    u = u.strip()
    return u if re.match(r"^https://[^\s<>\"']+$", u) and len(u) < 300 else None


def merge_links(papers: list[dict], hf: dict[str, dict]) -> int:
    """Fill missing feed code/project links from Hugging Face. Returns how many papers gained a code link."""
    n = 0
    for p in papers:
        h = hf.get(str(p.get("id", "")))
        if not h:
            continue
        if h.get("github") and not p.get("code") and not p.get("code_pending"):
            p["code"] = [h["github"]]
            p["code_via_hf"] = True
            n += 1
        if h.get("project") and not p.get("project"):
            p["project"] = [h["project"]]
    return n


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
    raw: dict[str, dict] = {}
    keys_logged = False
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
                rec = {"upvotes": up, "date": day}
                gh, pj = clean_github(p.get("githubRepo")), clean_url(p.get("projectPage"))
                if gh:
                    rec["github"] = gh
                if pj and pj != gh:
                    rec["project"] = pj
                new[pid] = rec
                raw[pid] = p
            if not keys_logged:
                print("  HF paper fields:", sorted(p.keys()))
                keys_logged = True
        time.sleep(0.5)
    cut = (today - dt.timedelta(days=KEEP_DAYS)).isoformat()
    for pid, v in old.items():
        if pid not in new and pid in ours and str(v.get("date", "")) >= cut:
            new[pid] = v
    OUT.write_text(json.dumps({"updated": today.isoformat(), "papers": new}, indent=1, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(f"{ok}/{DAYS} days fetched; {len(new)} of our papers are on Hugging Face Daily Papers "
          f"({sum(1 for v in new.values() if v.get('github'))} with a GitHub link)")
    if ok:
        write_queue(new, raw, entries)
    return 0 if ok else 1


def write_queue(new: dict[str, dict], raw: dict[str, dict], entries: list[dict]) -> None:
    curated = {str(e["arxiv"]) for e in entries if e.get("arxiv")}
    titles = {p["id"]: p for p in load_arxiv_feed()}
    rows = []
    for pid, v in sorted(new.items(), key=lambda kv: -kv[1]["upvotes"]):
        if pid in curated or v["upvotes"] < QUEUE_MIN_UPVOTES or pid not in raw:
            continue
        p, f = raw[pid], titles.get(pid, {})
        org = p.get("organization") if isinstance(p.get("organization"), dict) else {}
        authors = [a.get("name") for a in p.get("authors") or [] if isinstance(a, dict) and a.get("name")]
        rows.append({"id": pid, "title": str(p.get("title") or f.get("title") or "")[:300],
                     "upvotes": v["upvotes"], "hf_date": v["date"], "published": f.get("published"),
                     "topics": f.get("topics", []), "authors": authors[:20],
                     "organization": org.get("fullname") or org.get("name"),
                     "github": v.get("github"), "project": v.get("project") or (f.get("project") or [None])[0],
                     "arxiv_code": f.get("code", []), "comment": f.get("comment"),
                     "abstract": str(p.get("summary") or "")[:4000],
                     "ai_summary": str(p.get("ai_summary") or "")[:600] or None})
        if len(rows) >= QUEUE_MAX:
            break
    # curated entries whose HF page lists a code repo / project page that the entry still lacks
    links = []
    for e in entries:
        v = new.get(str(e.get("arxiv") or ""))
        if not v:
            continue
        miss = {k: v[hk] for k, hk in (("code", "github"), ("project", "project")) if v.get(hk) and not e.get(k)}
        if miss:
            links.append({"id": str(e["arxiv"]), "title": str(e.get("title", ""))[:200]} | miss)
    QUEUE.write_text(json.dumps({"updated": dt.date.today().isoformat(), "papers": rows,
                                 "curated_link_updates": links}, indent=1,
                                ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"review queue: {len(rows)} uncurated papers with >= {QUEUE_MIN_UPVOTES} upvotes, "
          f"{len(links)} curated entries with new HF links")


if __name__ == "__main__":
    sys.exit(main())
