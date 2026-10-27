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


def load_embodiments() -> list[dict]:
    """Embodiment tags (arm, hand, humanoid, ...) used for the site filter. Missing file -> []."""
    path = DATA / "embodiments.yaml"
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or []


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


RESOURCE_KINDS = ("list", "course", "docs", "community")


def load_resources() -> tuple[list[dict], list[str]]:
    """Related lists / courses / docs / communities from data/resources.yaml."""
    path = DATA / "resources.yaml"
    if not path.exists():
        return [], []
    try:
        items = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    except yaml.YAMLError as ex:
        return [], [f"resources.yaml: YAML error: {ex}"]
    out, errs = [], []
    for i, r in enumerate(items):
        where = f"resources.yaml#{i + 1}"
        if not isinstance(r, dict):
            errs.append(f"{where}: not a mapping")
            continue
        miss = [k for k in ("name", "url", "kind", "lang", "note_en", "note_zh") if not r.get(k)]
        if miss:
            errs.append(f"{where}: missing {', '.join(miss)}")
            continue
        if r["kind"] not in RESOURCE_KINDS:
            errs.append(f"{where}: kind must be one of {RESOURCE_KINDS}")
            continue
        if not str(r["url"]).startswith("https://"):
            errs.append(f"{where}: url must be https")
            continue
        out.append(r)
    return out, errs


def load_start(known_ids: set[str]) -> tuple[list[dict], list[str]]:
    """'Start here' reading path from data/start.yaml. Unknown entry ids are reported and dropped."""
    path = DATA / "start.yaml"
    if not path.exists():
        return [], []
    try:
        steps = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    except yaml.YAMLError as ex:
        return [], [f"start.yaml: YAML error: {ex}"]
    out, errs = [], []
    for i, st in enumerate(steps):
        where = f"start.yaml#{i + 1}"
        if not isinstance(st, dict):
            errs.append(f"{where}: not a mapping")
            continue
        miss = [k for k in ("en", "zh", "why_en", "why_zh", "entries") if not st.get(k)]
        if miss:
            errs.append(f"{where}: missing {', '.join(miss)}")
            continue
        bad = [x for x in st["entries"] if x not in known_ids]
        errs += [f"{where}: unknown curated entry id '{x}'" for x in bad]
        ids = [x for x in st["entries"] if x in known_ids]
        if ids:
            out.append({**st, "entries": ids})
    return out, errs


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


def classify(text: str, topics: list[dict], title: str | None = None, threshold: int = 2) -> list[str]:
    """Rule-based topic tags for feed papers, from topics.yaml keywords.

    A keyword in the title scores 3, each occurrence in the rest of the text scores 1;
    a topic is tagged at score >= 2, so a single passing mention in an abstract is not enough.
    """
    def prep(x: str) -> str:
        # Split glued acronyms ("FlowVLA" -> "Flow VLA") and pad punctuation ("PACT-VLA:" -> "PACT-VLA :")
        # so short keywords such as " vla" / "vla " match at word edges.
        x = re.sub(r"(?<=[a-z]{2})(?=[A-Z]{2,}\b)", " ", x)
        x = re.sub(r"[:;,.!?()\[\]{}\"'/]", lambda m: f" {m.group(0)} ", x)
        return " " + re.sub(r"\s+", " ", x.lower()) + " "
    body = prep(text)
    head = prep(title) if title else ""
    out = []
    for tp in topics:
        score = 0
        for k in tp.get("keywords", []):
            if head and k in head:
                score += 3
            score += body.count(k)
        if score >= threshold:
            out.append(tp["id"])
    return out


def norm_title(s: str) -> str:
    """Comparable form of a title: Greek letters spelled out (Δ and \\Delta both -> delta), LaTeX and punctuation dropped."""
    import unicodedata

    def greek(ch: str) -> str:
        name = unicodedata.name(ch, "")
        if not name.startswith("GREEK"):
            return ch
        w = name.split()[-1].lower()
        return "lambda" if w == "lamda" else w  # Unicode spells it LAMDA; TeX says \lambda
    s = "".join(greek(c) for c in s).lower()
    s = re.sub(r"\\([a-z]+)", r"\1", s)  # \delta -> delta
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
                wait = max(wait, min(int(ra), 300))  # never stall a CI job on a huge Retry-After
            print(f"  arXiv HTTP {ex.code}; waiting {wait}s (attempt {attempt}/{attempts})", flush=True)
        except Exception as ex:  # timeouts, resets
            wait = delay
            print(f"  arXiv error {type(ex).__name__}; waiting {wait}s (attempt {attempt}/{attempts})", flush=True)
        if attempt < attempts:
            time.sleep(wait)
            delay = min(delay * 2, 300)
    raise RuntimeError(f"arXiv API unreachable after {attempts} attempts: {url[:120]}")


VENUE_RE = re.compile(
    r"\b(CoRL|RSS|ICRA|IROS|NeurIPS|ICLR|ICML|CVPR|ICCV|ECCV|RA-?L|T-RO|TRO|Humanoids|AAAI|IJCAI|"
    r"Science Robotics|IJRR|WAFR|HRI|CASE|L4DC|ISRR|3DV|WACV)\b\)?(?:\s*['’]?\s*(20\d\d|\d\d)\b)?")
NOT_ACCEPTED_RE = re.compile(r"submi\w*|under review|in submission|preprint version of a submission|workshop", re.I)


def venue_of(comment: str | None) -> str | None:
    """'ICRA 2026' from arXiv comments like 'Accepted to ICRA 2026, 8 pages'. None for submissions,
    workshops or no venue. Conservative on purpose: a missing badge is better than a wrong one."""
    if not comment or NOT_ACCEPTED_RE.search(comment):
        return None
    m = VENUE_RE.search(comment)
    if not m:
        return None
    name = {"RAL": "RA-L", "TRO": "T-RO"}.get(m.group(1), m.group(1))
    year = m.group(2)
    if not year:  # e.g. "International Conference on ... (IROS), 2026": use the comment's only year, if unique
        years = set(re.findall(r"\b(20[2-3]\d)\b", comment))
        year = years.pop() if len(years) == 1 else None
    if year and len(year) == 2:
        year = "20" + year
    return f"{name} {year}" if year else name


CURATED_META = ARXIV_DIR / "curated_meta.json"  # authors + first-version date of curated arXiv papers (CI-filled)


def load_curated_meta() -> dict[str, dict]:
    """{arxiv_id: {"authors": [...], "published": "YYYY-MM-DD", "primary": "cs.RO"}}. Missing or malformed → {}."""
    try:
        data = json.loads(CURATED_META.read_text(encoding="utf-8"))
        return {k: v for k, v in data.get("papers", {}).items() if isinstance(v, dict) and v.get("authors")}
    except (OSError, json.JSONDecodeError, AttributeError):
        return {}


def _bib_escape(s: str) -> str:
    return re.sub(r"(?<!\\)([&%#])", r"\\\1", s)


def bibtex(arxiv_id: str, title: str, authors: list[str], published: str, primary: str = "") -> str | None:
    """A BibTeX @misc entry built only from arXiv metadata. None if there are no authors.

    Feed records cap authors at 8 and add a "+N" marker; that becomes "and others".
    """
    names = [a for a in authors if a and not a.startswith("+")]
    if not names or not published[:4].isdigit():
        return None
    import unicodedata
    last = unicodedata.normalize("NFKD", names[0].split()[-1]).encode("ascii", "ignore").decode().lower()
    last = re.sub(r"[^a-z]", "", last) or "anon"
    words = [w for w in re.findall(r"[A-Za-z]+", title) if w.lower() not in {"a", "an", "the", "on", "of", "for", "to", "and", "in", "with"}]
    key = f"{last}{published[:4]}{(words[0].lower() if words else '')}"
    author = " and ".join(_bib_escape(n) for n in names) + (" and others" if len(names) < len(authors) else "")
    lines = [f"@misc{{{key},", f"  title = {{{{{_bib_escape(' '.join(title.split()))}}}}},", f"  author = {{{author}}},",
             f"  year = {{{published[:4]}}},", f"  eprint = {{{arxiv_id}}},", "  archivePrefix = {arXiv},"]
    if primary:
        lines.append(f"  primaryClass = {{{primary}}},")
    lines += [f"  url = {{https://arxiv.org/abs/{arxiv_id}}},", "}"]
    return "\n".join(lines)
