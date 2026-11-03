"""Find code repositories on the project pages of papers that have a project page but no code link.

Authors often put the GitHub link on their project page and not in the arXiv comment. This reads those pages,
picks the repository the page presents as the paper's code, and checks on the GitHub API that it holds real code.
Runs in GitHub Actions (repo-stats.yml), since the agent's shell cannot reach project pages. Writes
data/project_code.json:
  {"updated": "YYYY-MM-DD",
   "papers": {arxiv_id: {"github": url, "page": url, "checked": date}},
   "none": {arxiv_id: date},          # looked, nothing usable; retried after RECHECK_DAYS
   "curated": {arxiv_id: {...}}}      # same as "papers", for curated entries: the agent reviews these by hand
Precision beats recall: a missing link is harmless, a wrong one is not, so an unclear page yields nothing.
Failed fetches keep old values, and every step is best-effort.
Usage: python scripts/project_code.py [--limit N]
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import html.parser
import http.client
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

from hf_papers import load as load_hf, merge_links
from radar import ROOT, load_arxiv_feed, load_curated, load_venue_papers

OUT = ROOT / "data" / "project_code.json"
RECHECK_DAYS = 7     # authors publish code around the conference, so look again
MAX_PAGE = 1_500_000
MAX_STARS_UNNAMED = 2000  # a repo this big that is not named after the paper is a dependency, not the paper's code
MAX_AGE_UNNAMED = 730     # likewise a repo much older than the paper
NOT_CODE_LANG = {None, "HTML", "CSS", "SCSS", "Less", "TeX"}  # no language = README only
GH_LINK = re.compile(r"https?://(?:www\.)?github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
NOT_OWNERS = {"sponsors", "features", "orgs", "topics", "marketplace", "settings", "login", "users", "about", "site", "apps"}
TEMPLATES = {"keunhong/nerfies", "nerfies/nerfies.github.io", "eliahuhorwitz/academic-project-page-template",
             "jonbarron/website", "shunzh/project_website", "alshedivat/al-folio", "academicpages/academicpages.github.io",
             "twbs/bootstrap", "mrdoob/three.js", "google/model-viewer", "jekyll/jekyll", "mmistakes/minimal-mistakes",
             "ai-robotic-kitchen/ai-robotic-kitchen.github.io", "gkioxari/aims2_project_page"}
SITE_WORDS = re.compile(r"website|homepage|project-?page|\.github\.io|template|theme|awesome|paper-?list", re.I)
SITE_TEXT = re.compile(r"template|website|theme|inspired by|borrowed|adapted from|based on", re.I)
CODE_WORD = re.compile(r"\b(code|codes|github|source|repo|repository|implementation|software|open[- ]source)\b", re.I)
SOON = re.compile(r"coming soon|to be released|will be (?:released|available|made)|\bsoon\b|\bTBD\b", re.I)
UA = {"User-Agent": "Mozilla/5.0 (compatible; embodied-ai-radar; +https://hu-zlatan.github.io/embodied-ai-radar/)"}


class Links(html.parser.HTMLParser):
    """All <a> elements as {href, hint}; hint = link text + class/title/aria-label + inner image alt/icon classes."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links: list[dict] = []
        self.cur: dict | None = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        extra = " ".join(str(a.get(k) or "") for k in ("class", "title", "aria-label", "alt", "src"))
        if tag == "a":
            self.cur = {"href": a.get("href") or "", "hint": extra}
            self.links.append(self.cur)
        elif self.cur is not None:
            self.cur["hint"] += " " + extra

    def handle_endtag(self, tag):
        if tag == "a":
            self.cur = None

    def handle_data(self, data):
        if self.cur is not None:
            self.cur["hint"] += " " + data


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def repo_of(url: str) -> str | None:
    """'https://github.com/Owner/Repo/tree/main' -> 'Owner/Repo'; None for anything that is not a repository."""
    m = GH_LINK.match(url.strip())
    if not m:
        return None
    owner, repo = m.group(1), m.group(2).removesuffix(".git")
    if owner.lower() in NOT_OWNERS or repo.startswith("."):
        return None
    key = f"{owner}/{repo}"
    return None if key.lower() in TEMPLATES or SITE_WORDS.search(repo) else key


def page_names(page: str) -> tuple[list[str], str]:
    """Slugs that name the project in the page URL, and the github.io owner ('' when not on github.io)."""
    u = urllib.parse.urlparse(page)
    parts = [p for p in u.path.split("/") if p and not p.endswith((".html", ".htm"))]
    names = parts[-1:]
    owner = ""
    host = u.netloc.lower()
    if host.endswith(".github.io"):
        owner = host.removesuffix(".github.io")
        names.append(owner)
    elif host.count(".") >= 1 and host.split(".")[0] not in ("www", "sites", "research"):
        names.append(host.split(".")[0])
    return names, owner


def named_after(repo: str, title: str, page: str) -> bool:
    """Is the repository named after this paper (its short title, or the project page's slug)?"""
    name = repo.split("/")[1]
    n = norm(name)
    if len(n) < 3:
        return False
    head = title.split(":")[0]
    if len(head.split()) <= 3 and len(norm(head)) >= 3 and (norm(head) in n or (len(n) >= 4 and n in norm(head))):
        return True
    for s in page_names(page)[0]:
        s = norm(s)
        if len(s) >= 4 and (s == n or s in n or (len(n) >= 4 and n in s)):
            return True
    words = {w.lower() for w in re.split(r"[-_.\s]|(?<=[a-z])(?=[A-Z])", name) if len(w) >= 3}
    title_words = {w.lower() for w in re.findall(r"[A-Za-z0-9]+", title)}
    return len(words) >= 2 and words <= title_words


def candidates(html_text: str) -> list[dict]:
    """Repositories on the page: {repo, strong}. strong = an actual link that says it is code."""
    p = Links()
    try:
        p.feed(html_text)
    except (AssertionError, ValueError):
        pass
    found: dict[str, dict] = {}
    for a in p.links:
        repo = repo_of(a["href"])
        if not repo:
            continue
        hint = " ".join(a["hint"].split())
        if SITE_TEXT.search(hint):
            continue
        c = found.setdefault(repo, {"repo": repo, "strong": False, "soon": False})
        c["strong"] = c["strong"] or bool(CODE_WORD.search(hint.replace("-", " ")) or "github" in hint.lower())
        c["soon"] = c["soon"] or bool(SOON.search(hint))
    for m in GH_LINK.finditer(html_text):  # links in scripts or plain text: weak, must be named after the paper
        repo = repo_of(m.group(0))
        if repo:
            found.setdefault(repo, {"repo": repo, "strong": False, "soon": False})
    return [c for c in found.values() if not c["soon"]]


def choose(cands: list[dict], title: str, page: str) -> tuple[str, bool] | None:
    """The repository the page presents as this paper's code, with whether it is named after the paper; None if unclear."""
    named = [c for c in cands if named_after(c["repo"], title, page)]
    if named:
        return sorted(named, key=lambda c: not c["strong"])[0]["repo"], True
    strong = [c for c in cands if c["strong"]]
    if len(strong) == 1:
        return strong[0]["repo"], False
    owner = page_names(page)[1]
    if len(cands) == 1 and owner and cands[0]["repo"].split("/")[0].lower() == owner:
        return cands[0]["repo"], False
    return None


def repo_ok(d: dict, named: bool, published: str) -> str | None:
    """None when GitHub's record looks like real code for this paper, otherwise the reason it does not."""
    if d.get("archived") and not named:
        return "archived"
    if d.get("language") in NOT_CODE_LANG:
        return f"language {d.get('language')}"
    if d.get("private") or d.get("disabled"):
        return "not public"
    if int(d.get("size") or 0) < 20:
        return "nearly empty"
    if not named:
        if d.get("fork"):
            return "fork"
        if int(d.get("stargazers_count") or 0) > MAX_STARS_UNNAMED:
            return "large repo not named after the paper"
        try:
            made, pub = dt.date.fromisoformat(d["created_at"][:10]), dt.date.fromisoformat(published[:10])
            if (pub - made).days > MAX_AGE_UNNAMED:
                return "older than the paper"
        except (KeyError, TypeError, ValueError):
            return "no dates"
    return None


def get_page(url: str) -> str | None:
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=15) as r:
            if "html" not in (r.headers.get("Content-Type") or "html"):
                return None
            return r.read(MAX_PAGE).decode("utf-8", "replace")
    except (OSError, http.client.HTTPException, ValueError):
        return None


def get_repo(repo: str, token: str | None) -> dict | None:
    """GitHub's record of the repo; {} on 404; None when the API could not be reached."""
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers={"Accept": "application/vnd.github+json", "User-Agent": "embodied-ai-radar"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (404, 451):
                return {}
            time.sleep(2 * (attempt + 1))
        except (OSError, http.client.HTTPException, ValueError):
            time.sleep(2 * (attempt + 1))
    return None


def load() -> dict:
    try:
        d = json.loads(OUT.read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def merge(papers: list[dict], found: dict | None = None) -> int:
    """Fill missing code links of feed/venue papers from project pages. Returns how many gained one."""
    found = load().get("papers", {}) if found is None else found
    n = 0
    for p in papers:
        h = found.get(str(p.get("id", "")))
        if isinstance(h, dict) and isinstance(h.get("github"), str) and h["github"].startswith("https://github.com/") \
                and not p.get("code") and not p.get("code_pending"):
            p["code"] = [h["github"]]
            p["code_via_page"] = True
            n += 1
    return n


def todo(old: dict, today: dt.date) -> list[dict]:
    """Papers and curated entries with a project page, no code, and no recent look."""
    feed = load_arxiv_feed()
    ids = {p["id"] for p in feed}
    papers = feed + [p for p in load_venue_papers() if p["id"] not in ids]
    merge_links(papers, load_hf())
    cut = (today - dt.timedelta(days=RECHECK_DAYS)).isoformat()
    none = old.get("none", {})
    out = []
    for p in papers:
        pages = p.get("project") or []
        if pages and not p.get("code") and not p.get("code_pending") and none.get(p["id"], "") < cut and p["id"] not in old.get("papers", {}):
            out.append({"id": p["id"], "title": p["title"], "page": pages[0], "published": p.get("published", ""), "curated": False})
    entries, _ = load_curated(strict=False)
    for e in entries:
        aid = str(e.get("arxiv") or "")
        if aid and e.get("project") and not e.get("code") and none.get(aid, "") < cut and aid not in old.get("curated", {}):
            out.append({"id": aid, "title": e["title"], "page": e["project"], "published": f"{e.get('year', today.year)}-12-31", "curated": True})
    return out


def look(item: dict) -> tuple[dict, tuple[str, bool] | None, bool]:
    text = get_page(item["page"])
    if text is None:
        return item, None, False
    return item, choose(candidates(text), item["title"], item["page"]), True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=1000)
    args = ap.parse_args()
    token = os.environ.get("GITHUB_TOKEN")
    today = dt.date.today()
    old = load()
    found, cur, none = dict(old.get("papers", {})), dict(old.get("curated", {})), dict(old.get("none", {}))
    items = todo(old, today)[:args.limit]
    print(f"{len(items)} project pages to read")
    hits = unreachable = 0
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(look, items))
    for item, pick, reached in results:
        if not reached:
            unreachable += 1
            none[item["id"]] = today.isoformat()
            continue
        if not pick:
            none[item["id"]] = today.isoformat()
            continue
        repo, named = pick
        d = get_repo(repo, token)
        if d is None:
            continue  # API trouble: try again next run
        why = "not found" if not d else repo_ok(d, named, item["published"])
        if why:
            print(f"  skip {item['id']} {repo}: {why}")
            none[item["id"]] = today.isoformat()
            continue
        rec = {"github": d.get("html_url") or f"https://github.com/{repo}", "page": item["page"], "checked": today.isoformat()}
        (cur if item["curated"] else found)[item["id"]] = rec
        none.pop(item["id"], None)
        hits += 1
        print(f"  ok   {item['id']} {rec['github']}  <- {item['page']}  ({'named' if named else 'link'}) {item['title'][:60]}")
    OUT.write_text(json.dumps({"updated": today.isoformat(), "papers": found, "none": none, "curated": cur}, indent=0, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{hits} repos found on {len(items)} pages ({unreachable} unreachable); {len(found)} papers, {len(cur)} curated in total")
    return 0


if __name__ == "__main__":
    sys.exit(main())
