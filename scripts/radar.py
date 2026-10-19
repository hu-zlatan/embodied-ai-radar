"""Shared helpers: loading and validating the radar's data files.

Only dependency outside the standard library: PyYAML.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CURATED = DATA / "curated"
ARXIV_DIR = DATA / "arxiv"

ENTRY_TYPES = {"paper", "code", "dataset", "benchmark", "simulator", "hardware"}
ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}$")
URL_RE = re.compile(r"^https://[^\s]+$")
REQUIRED = ("title", "type", "year", "takeaway_en", "takeaway_zh")
ALLOWED = set(REQUIRED) | {
    "arxiv", "url", "code", "project", "org", "venue", "tags", "topics", "highlight", "added",
}


def load_topics() -> list[dict]:
    with open(DATA / "topics.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def slug(text: str) -> str:
    s = re.sub(r"\$[^$]*\$", lambda m: re.sub(r"[^a-z0-9]", "", m.group(0).lower()), text.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60] or "entry"


def entry_id(e: dict) -> str:
    if e.get("arxiv"):
        return "arxiv-" + e["arxiv"]
    return slug(e["title"])


def validate_entry(e: dict, where: str, topic_ids: set[str]) -> list[str]:
    errs = []
    if not isinstance(e, dict):
        return [f"{where}: entry is not a mapping"]
    for k in REQUIRED:
        if not e.get(k):
            errs.append(f"{where}: missing '{k}'")
    for k in e:
        if k not in ALLOWED:
            errs.append(f"{where}: unknown field '{k}'")
    if e.get("type") and e["type"] not in ENTRY_TYPES:
        errs.append(f"{where}: bad type '{e['type']}'")
    if e.get("arxiv") and not ARXIV_RE.match(str(e["arxiv"])):
        errs.append(f"{where}: bad arxiv id '{e['arxiv']}' (quote it, e.g. \"2406.09246\")")
    for k in ("url", "code", "project"):
        if e.get(k) and not URL_RE.match(str(e[k])):
            errs.append(f"{where}: '{k}' must be an https URL")
    if not (e.get("arxiv") or e.get("url") or e.get("code") or e.get("project")):
        errs.append(f"{where}: needs at least one link (arxiv, url, code or project)")
    if e.get("year") and not (1990 <= int(e["year"]) <= 2100):
        errs.append(f"{where}: implausible year")
    for t in e.get("topics", []) or []:
        if t not in topic_ids:
            errs.append(f"{where}: unknown topic '{t}'")
    for k in ("takeaway_en", "takeaway_zh"):
        if e.get(k) and len(str(e[k])) > 220:
            errs.append(f"{where}: {k} longer than 220 chars")
    return errs


def load_curated(strict: bool = True) -> tuple[list[dict], list[str]]:
    """Return (entries, errors). Each entry gets `id` and `topics` (primary first)."""
    topics = load_topics()
    topic_ids = {t["id"] for t in topics}
    entries, errs, seen = [], [], {}
    for t in topics:
        path = CURATED / f"{t['id']}.yaml"
        if not path.exists():
            continue
        try:
            items = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        except yaml.YAMLError as ex:
            errs.append(f"{path.name}: YAML error: {ex}")
            continue
        for i, e in enumerate(items):
            where = f"{path.name}#{i + 1}"
            problems = validate_entry(e, where, topic_ids)
            if problems:
                errs.extend(problems)
                if strict or not isinstance(e, dict):
                    continue
            e = dict(e)
            e["arxiv"] = str(e["arxiv"]) if e.get("arxiv") else None
            e["id"] = entry_id(e)
            extra = [x for x in (e.get("topics") or []) if x != t["id"]]
            e["topics"] = [t["id"]] + extra
            if e["id"] in seen:
                errs.append(f"{where}: duplicate of {seen[e['id']]} ({e['id']})")
                continue
            seen[e["id"]] = where
            entries.append(e)
    return entries, errs


def load_arxiv_feed() -> list[dict]:
    """All daily intake records, newest first. Malformed files are skipped, never fatal."""
    out = []
    for path in sorted(ARXIV_DIR.glob("*/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            for p in data.get("papers", []):
                if isinstance(p, dict) and p.get("id") and p.get("title"):
                    out.append(p)
        except (json.JSONDecodeError, OSError, AttributeError):
            print(f"warning: skipping malformed {path}")
    out.sort(key=lambda p: (p.get("published", ""), p["id"]), reverse=True)
    return out


def classify(text: str, topics: list[dict]) -> list[str]:
    """Rule-based topic tags for feed papers, from topics.yaml keywords."""
    t = " " + re.sub(r"\s+", " ", text.lower()) + " "
    return [tp["id"] for tp in topics if any(k in t for k in tp.get("keywords", []))]


def norm_title(s: str) -> str:
    s = s.lower().replace("π", "pi")
    s = re.sub(r"[\\${}_^]", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


ARXIV_UA = {"User-Agent": "embodied-ai-radar/1.0 (+https://github.com/hu-zlatan/embodied-ai-radar)"}


def arxiv_get(url: str, attempts: int = 6) -> bytes:
    """GET from the arXiv API with polite exponential backoff (honours Retry-After on 429/503)."""
    import time
    import urllib.error
    import urllib.request

    delay = 15
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=ARXIV_UA), timeout=90) as r:
                return r.read()
        except urllib.error.HTTPError as ex:
            wait = delay
            ra = ex.headers.get("Retry-After") if ex.headers else None
            if ra and ra.isdigit():
                wait = max(wait, int(ra))
            print(f"  arXiv HTTP {ex.code}; waiting {wait}s (attempt {attempt}/{attempts})", flush=True)
        except Exception as ex:  # timeouts, resets
            wait = delay
            print(f"  arXiv error {type(ex).__name__}; waiting {wait}s (attempt {attempt}/{attempts})", flush=True)
        if attempt < attempts:
            time.sleep(wait)
            delay = min(delay * 2, 300)
    raise RuntimeError(f"arXiv API unreachable after {attempts} attempts: {url[:120]}")
