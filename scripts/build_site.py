"""Generate the static website into _site/ from data/. Usage: python scripts/build_site.py

Pages: index (highlights + instant search), one page per topic, the daily arXiv feed,
weekly digests, plus data/index.json for client-side search, sitemap.xml and feed.xml (Atom).
Bilingual: every text exists in EN and ZH; CSS shows one based on <html class="zh">.
"""
from __future__ import annotations

import csv
import datetime as dt
import html
import io
import json
import re
import shutil
import sys
from pathlib import Path

from hf_papers import load as load_hf, merge_links
from repo_stats import apply_feed_stats, load_feed_stats, load_history, load_stats, repo_key, star_gains
from radar import (ROOT, bibtex, classify, venue_of, load_arxiv_feed, load_curated, load_curated_meta, load_embodiments,
                   load_resources, load_start, load_topics)

OUT = ROOT / "_site"
SRC = ROOT / "site_src"
DIGEST = ROOT / "digest"
SITE_URL = "https://hu-zlatan.github.io/embodied-ai-radar/"
REPO_URL = "https://github.com/hu-zlatan/embodied-ai-radar"
FEED_DAYS_ON_SITE = 60   # feed papers kept in the search index
TOPIC_FEED_MAX = 40      # recent feed papers per topic page
FEED_ABSTRACT_DAYS = 21  # abstracts (for search) kept in the index only for this many days

esc = html.escape
EMB: dict[str, dict] = {}  # embodiment id -> {en, zh}, filled in build()
STATS: dict[str, dict] = {}  # 'owner/repo' -> {stars, pushed, archived}, from data/repo_stats.json
VENUE_PAGES: set[str] = set()  # venue keys like 'CoRL 2026' that have a page venues/<slug>.html, filled in build()
VENUE_MIN = 3  # a venue+year gets its own page once it has this many papers (curated + feed)


def venue_key(v: str | None) -> str | None:
    """'CoRL 2026' from 'CoRL 2026' or 'NeurIPS 2021 Datasets and Benchmarks'; None without a year."""
    m = re.match(r"^(.+?) (20\d\d|19\d\d)\b", str(v or "").strip())
    return f"{m.group(1)} {m.group(2)}" if m else None


def venue_slug(k: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", k.lower()).strip("-")


def venue_badge(v: str, root: str) -> str:
    k = venue_key(v)
    if k in VENUE_PAGES:
        return f'<a class="badge venue" href="{root}venues/{venue_slug(k)}.html">{esc(v)}</a>'
    return f'<span class="badge venue">{esc(v)}</span>'


def fmt_stars(n: int) -> str:
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def repo_stat(e: dict) -> dict | None:
    """GitHub stats for the entry's code repo (or website/project if that is a GitHub repo)."""
    for k in ("code", "url", "project"):
        st = STATS.get(repo_key(e.get(k)) or "")
        if st:
            return st
    return None


def hf_link(arxiv_id: str | None, h: dict | None) -> str:
    """' · ▲ 12 HF' link to the paper's Hugging Face page when it was listed on HF Daily Papers."""
    if not arxiv_id or not h:
        return ""
    return (f' · <a class="hf" href="https://huggingface.co/papers/{esc(str(arxiv_id))}" rel="noopener" '
            f'title="Upvotes on Hugging Face Daily Papers">▲ {int(h["upvotes"])} HF</a>')


def emb_chips(ids: list[str]) -> str:
    return "".join(f'<span class="chip emb">{bi(EMB[i]["en"], EMB[i]["zh"])}</span>' for i in ids if i in EMB)


def bi(en: str, zh: str, tag: str = "span") -> str:
    """Bilingual text: both versions rendered, CSS shows the active one."""
    return f'<{tag} lang="en">{esc(en)}</{tag}><{tag} lang="zh">{esc(zh)}</{tag}>'


def links_of(e: dict) -> list[tuple[str, str, str]]:
    out = []
    if e.get("arxiv"):
        out.append(("Paper", "论文", f"https://arxiv.org/abs/{e['arxiv']}"))
    if e.get("url"):
        out.append(("Website", "官网", e["url"]))
    if e.get("code"):
        out.append(("Code", "代码", e["code"]))
    if e.get("project"):
        out.append(("Project", "项目页", e["project"]))
    return out


TYPE_LABEL = {
    "paper": ("Paper", "论文"), "code": ("Code", "代码"), "dataset": ("Dataset", "数据集"),
    "benchmark": ("Benchmark", "基准"), "simulator": ("Simulator", "仿真器"), "hardware": ("Hardware", "硬件"),
}


def bib_block(b: str | None) -> str:
    """Collapsed BibTeX (works without JS; app.js adds the copy button behaviour)."""
    if not b:
        return ""
    return (f'<details class="bib"><summary>BibTeX</summary><pre>{esc(b)}</pre>'
            f'<button type="button" class="copy">{bi("Copy", "复制")}</button></details>')


def plain_title(t: str) -> str:
    return re.sub(r"\$π_\{?([^}$]+)\}?\$", r"π\1", t)


def title_html(t: str) -> str:
    # Render the few LaTeX titles we have ($π_0$, $π_{0.5}$) readably.
    t = re.sub(r"\$π_\{?([^}$]+)\}?\$", r"π\1", t)
    return esc(t).replace("π0.5", "π<sub>0.5</sub>").replace("π0", "π<sub>0</sub>")


SCHEMA_TYPE = {"paper": "ScholarlyArticle", "code": "SoftwareSourceCode", "dataset": "Dataset",
               "benchmark": "Dataset", "simulator": "SoftwareSourceCode", "hardware": "CreativeWork"}


def entry_page(e: dict, topics_by_id: dict, related: list[dict], authors: list[str]) -> str:
    """Body of e/<id>.html: one curated entry with its takeaway, links, BibTeX and related entries."""
    t0 = topics_by_id[e["topics"][0]]
    crumbs = (f'<p class="muted"><a href="../topics/index.html">{bi("Topics", "主题")}</a> › '
              f'<a href="../topics/{t0["id"]}.html">{bi(t0["en"], t0["zh"])}</a></p>')
    au = ""
    if authors:
        au = f'<p class="authors">{bi("Authors (from arXiv): ", "作者（来自 arXiv）：")}{esc(", ".join(authors[:8]))}{" et al." if len(authors) > 8 else ""}</p>'
    rel = ""
    if related:
        rel = (f'<h2>{bi("More in " + t0["en"], "更多" + t0["zh"] + "条目")}</h2><ul class="tlist">'
               + "".join(f'<li><a href="{esc(r["id"])}.html">{title_html(r["title"])}</a> '
                         f'<span class="muted">· {esc(str(r["year"]))}{" · " + esc(r["org"]) if r.get("org") else ""}</span></li>'
                         for r in related)
               + f'</ul><p><a class="more" href="../topics/{t0["id"]}.html">{bi("All " + t0["en"] + " entries →", "查看全部" + t0["zh"] + "条目 →")}</a></p>')
    ld = {"@context": "https://schema.org", "@type": SCHEMA_TYPE.get(e["type"], "CreativeWork"),
          "name": plain_title(e["title"]), "url": f"{SITE_URL}e/{e['id']}.html",
          "description": e["takeaway_en"], "sameAs": [u for _, _, u in links_of(e)], "dateCreated": str(e["year"]),
          "about": [topics_by_id[t]["en"] for t in e["topics"]]}
    if authors:
        ld["author"] = [{"@type": "Person", "name": a} for a in authors[:20]]
    ld_js = json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")
    return (crumbs + f'<div class="cards single">{curated_card(e, topics_by_id, "../", detail=True)}</div>' + au + rel
            + f'\n<script type="application/ld+json">{ld_js}</script>')


def curated_card(e: dict, topics_by_id: dict, root: str, detail: bool = False) -> str:
    links = links_of(e)
    main = links[0][2]
    en, zh = TYPE_LABEL[e["type"]]
    chips = "".join(
        f'<a class="chip topic" href="{root}topics/{t}.html">{bi(topics_by_id[t]["en"], topics_by_id[t]["zh"])}</a>'
        for t in e["topics"])
    tags = emb_chips(e.get("emb", [])) + "".join(f'<span class="chip">{esc(t)}</span>' for t in (e.get("tags") or []))
    star = '<span class="star" title="Highlight">★</span>' if e.get("highlight") else ""
    if e.get("added"):
        star += f' <span class="badge new">{bi("new", "新")} {esc(str(e["added"]))}</span>'
    linkrow = " · ".join(f'<a href="{esc(u)}" rel="noopener">{bi(a, b)}</a>' for a, b, u in links)
    if not detail:
        linkrow += f' · <a class="perma" href="{root}e/{esc(e["id"])}.html">{bi("Details", "详情")}</a>'
    st = repo_stat(e)
    if st:
        linkrow += f' <span class="gh" title="GitHub stars">★ {fmt_stars(st["stars"])}</span>'
        if st.get("archived"):
            linkrow += f' <span class="badge">{bi("archived", "已归档")}</span>'
    linkrow += hf_link(e.get("arxiv"), e.get("hf"))
    meta = " · ".join(x for x in [esc(str(e["year"])), esc(e.get("org", ""))] if x)
    h = "h1" if detail else "h3"
    if e.get("venue"):
        meta += " " + venue_badge(str(e["venue"]), root)
    return f"""<article class="card" id="{esc(e['id'])}">
<div class="meta"><span class="badge">{bi(en, zh)}</span> {meta} {star}</div>
<{h}><a href="{esc(main)}" rel="noopener">{title_html(e['title'])}</a></{h}>
<p class="take">{bi(e['takeaway_en'], e['takeaway_zh'])}</p>
<div class="links">{linkrow}</div>
{bib_block(e.get("bib"))}
<div class="chips">{chips}{tags}</div>
</article>"""


def feed_card(p: dict, topics_by_id: dict, root: str) -> str:
    authors = ", ".join(p.get("authors", [])[:4])
    if len(p.get("authors", [])) > 4:
        authors += " et al."
    chips = "".join(
        f'<a class="chip topic" href="{root}topics/{t}.html">{bi(topics_by_id[t]["en"], topics_by_id[t]["zh"])}</a>'
        for t in p.get("topics", []) if t in topics_by_id) + emb_chips(p.get("emb", []))
    code = "".join(f' · <a href="{esc(u)}" rel="noopener">{bi("Code", "代码")}</a>' for u in p.get("code", [])[:1])
    if not code and p.get("code_pending"):
        code = (' · <span class="muted" title="' + esc(p["code_pending"][0]) + '">'
                + bi("Code: not public yet", "代码：尚未公开") + "</span>")
    elif code and p.get("stars") is not None:
        code += f' <span class="gh" title="GitHub stars">★ {fmt_stars(p["stars"])}</span>'
    proj = "".join(f' · <a href="{esc(u)}" rel="noopener">{bi("Project", "项目页")}</a>' for u in p.get("project", [])[:1])
    has_code = '<span class="badge code">code</span>' if p.get("code") else ""
    v = venue_of(p.get("comment"))
    if v:
        has_code += " " + venue_badge(v, root)
    return f"""<article class="card feed" id="arxiv-{esc(p['id'])}">
<div class="meta"><span class="badge">arXiv {esc(p.get('primary', ''))}</span> {esc(p.get('published', ''))} {has_code}</div>
<h3><a href="https://arxiv.org/abs/{esc(p['id'])}" rel="noopener">{esc(p['title'])}</a></h3>
<p class="authors">{esc(authors)}</p>
<details><summary>{bi("Abstract", "摘要")}</summary><p>{esc(p.get('abstract', ''))}</p></details>
<div class="links"><a href="https://arxiv.org/abs/{esc(p['id'])}" rel="noopener">arXiv</a> · <a href="https://arxiv.org/pdf/{esc(p['id'])}" rel="noopener">PDF</a>{code}{proj}{hf_link(p['id'], p.get('hf'))}</div>
{bib_block(bibtex(p["id"], p["title"], p.get("authors", []), p.get("published", ""), p.get("primary", "")))}
<div class="chips">{chips}</div>
</article>"""


def page(title: str, body: str, root: str, desc: str, path: str, alt: str = "") -> str:
    nav = (f'<a href="{root}index.html">{bi("Home", "首页")}</a>'
           f'<a href="{root}feed.html">{bi("Daily arXiv", "每日 arXiv")}</a>'
           f'<a href="{root}topics/index.html">{bi("Topics", "主题")}</a>'
           f'<a href="{root}digest/index.html">{bi("Weekly", "周报")}</a>'
           f'<a href="{root}resources.html">{bi("Learn", "资源")}</a>'
           f'<a href="{REPO_URL}" rel="noopener">GitHub</a>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE_URL}{path}">
<link rel="alternate" type="application/atom+xml" title="Embodied AI Radar" href="{root}feed.xml">{alt}
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE_URL}{path}">
<meta property="og:image" content="{SITE_URL}assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E📡%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="{root}assets/style.css">
<script>try{{var l=new URLSearchParams(location.search).get('lang')||localStorage.getItem('lang')||((navigator.language||'').startsWith('zh')?'zh':'en');if(l==='zh')document.documentElement.classList.add('zh');document.documentElement.lang=l==='zh'?'zh-CN':'en'}}catch(e){{}}</script>
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{root}index.html">📡 {bi("Embodied AI Radar", "具身智能雷达")}</a>
<nav>{nav}</nav>
<button id="lang" class="lang" type="button" aria-label="Switch language"><span lang="en">中文</span><span lang="zh">EN</span></button>
</div></header>
<main class="wrap">
{body}
</main>
<footer class="wrap foot">
<p>{bi("Maintained by an AI agent (Claude, by Anthropic) under the oversight of", "由 AI 智能体（Anthropic 的 Claude）维护，人类监督者：")} <a href="https://github.com/hu-zlatan">@hu-zlatan</a>.
{bi("Code MIT · curated data CC BY 4.0 · arXiv metadata CC0.", "代码 MIT · 精选数据 CC BY 4.0 · arXiv 元数据 CC0。")}
<a href="{REPO_URL}/issues/new">{bi("Suggest a paper or report a problem", "推荐论文或反馈问题")}</a></p>
</footer>
<script src="{root}assets/app.js" defer></script>
</body>
</html>
"""


def atom(papers: list[dict], title: str, path: str, today: dt.date) -> str:
    items = "".join(f"""<entry><title>{esc(p['title'])}</title><id>https://arxiv.org/abs/{esc(p['id'])}</id>
<link href="https://arxiv.org/abs/{esc(p['id'])}"/><updated>{esc(p.get('published', today.isoformat()))}T00:00:00Z</updated>
<summary>{esc(p.get('abstract', ''))}</summary></entry>""" for p in papers)
    return f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"><title>{esc(title)}</title>
<link href="{SITE_URL}"/><link rel="self" href="{SITE_URL}{path}"/><id>{SITE_URL}{"" if path == "feed.xml" else path}</id>
<updated>{today.isoformat()}T00:00:00Z</updated><author><name>Embodied AI Radar</name></author>
{items}
</feed>
"""


def picks_atom(entries: list[dict], today: dt.date, limit: int = 60) -> str:
    """Low-volume feed: only agent picks (curated entries with `added:`), newest first, bilingual takeaway."""
    picks = sorted((e for e in entries if e.get("added")), key=lambda e: (str(e["added"]), e["id"]), reverse=True)[:limit]
    items = "".join(f"""<entry><title>{esc(e['title'])}</title><id>{SITE_URL}e/{esc(e['id'])}.html</id>
<link href="{SITE_URL}e/{esc(e['id'])}.html"/><updated>{esc(str(e['added']))}T00:00:00Z</updated>
<summary>{esc(e.get('takeaway_en', ''))}\n\n{esc(e.get('takeaway_zh', ''))}</summary></entry>""" for e in picks)
    latest = str(picks[0]["added"]) if picks else today.isoformat()
    return f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"><title>Embodied AI Radar — agent picks / 精选</title>
<link href="{SITE_URL}"/><link rel="self" href="{SITE_URL}picks.xml"/><id>{SITE_URL}picks.xml</id>
<updated>{latest}T00:00:00Z</updated><author><name>Embodied AI Radar</name></author>
{items}
</feed>
"""


def week_id(d: dt.date) -> str:
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def md_to_html(md: str) -> str:
    """Tiny Markdown subset for digests: headings, lists, links, bold, paragraphs."""
    out, in_list = [], False
    for line in md.splitlines():
        s = line.rstrip()
        def inline(t: str) -> str:
            t = esc(t)
            if len(t) > 2 and t.startswith("_") and t.endswith("_"):  # whole-line italics
                t = f"<em>{t[1:-1]}</em>"
            t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
            t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" rel="noopener">\1</a>', t)
            return t
        if s.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(s[2:])}</li>")
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        m = re.match(r"^(#{1,4}) (.*)", s)
        if m:
            n = len(m.group(1)) + 1
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
        elif s:
            out.append(f"<p>{inline(s)}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def build() -> int:
    topics = load_topics()
    tby = {t["id"]: t for t in topics}
    entries, errs = load_curated(strict=False)
    if errs:
        print(f"warning: {len(errs)} curated data problems (run validate.py); building anyway")
    feed = load_arxiv_feed()
    today = dt.datetime.now(dt.timezone.utc).date()
    embs = load_embodiments()
    EMB.clear()
    EMB.update({m["id"]: m for m in embs})
    STATS.clear()
    STATS.update(load_stats())
    hf = load_hf()
    merge_links(feed, hf)  # code/project links from Hugging Face paper pages when the arXiv comment has none
    apply_feed_stats(feed, load_feed_stats())
    for p in feed:
        if p["id"] in hf:
            p["hf"] = hf[p["id"]]
    for e in entries:
        e["emb"] = classify(" ".join([e["takeaway_en"], " ".join(e.get("tags") or [])]), embs, title=e["title"], threshold=1)
    for e in entries:
        if e.get("arxiv") and str(e["arxiv"]) in hf:
            e["hf"] = hf[str(e["arxiv"])]
    meta = load_curated_meta()
    for e in entries:
        m = meta.get(e.get("arxiv") or "")
        if m:
            e["bib"] = bibtex(e["arxiv"], e["title"], m["authors"], m.get("published", ""), m.get("primary", ""))
    for p in feed:
        p["emb"] = classify(p.get("abstract", ""), embs, title=p.get("title", ""), threshold=1)
    venues: dict[str, dict] = {}  # 'CoRL 2026' -> {"c": [curated entries], "f": [feed papers]}
    for e in entries:
        k = venue_key(e.get("venue"))
        if k:
            venues.setdefault(k, {"c": [], "f": []})["c"].append(e)
    cur_ids = {e.get("arxiv") for e in entries if e.get("arxiv")}
    for p in feed:
        k = venue_key(venue_of(p.get("comment")))
        if k and p["id"] not in cur_ids:  # agent picks are curated entries already
            venues.setdefault(k, {"c": [], "f": []})["f"].append(p)
    VENUE_PAGES.clear()
    VENUE_PAGES.update(k for k, g in venues.items() if len(g["c"]) + len(g["f"]) >= VENUE_MIN)

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "topics").mkdir(parents=True)
    (OUT / "digest").mkdir()
    (OUT / "data").mkdir()
    shutil.copytree(SRC / "assets", OUT / "assets")

    by_topic = {t["id"]: [e for e in entries if t["id"] in e["topics"]] for t in topics}
    feed_by_topic = {t["id"]: [p for p in feed if t["id"] in p.get("topics", [])] for t in topics}
    latest_date = feed[0]["published"] if feed else None
    week_cut = (today - dt.timedelta(days=7)).isoformat()
    feed_week = [p for p in feed if p.get("published", "") >= week_cut]

    # ---- search index
    site_cut = (today - dt.timedelta(days=FEED_DAYS_ON_SITE)).isoformat()
    idx = []
    for e in entries:
        idx.append({"k": "c", "id": e["id"], "t": re.sub(r"\$π_\{?([^}$]+)\}?\$", r"π\1", e["title"]), "y": e["year"], "ty": e["type"],
                    "o": e.get("org", ""), "en": e["takeaway_en"], "zh": e["takeaway_zh"],
                    "tp": e["topics"], "em": e["emb"], "tg": e.get("tags") or [], "h": 1 if e.get("highlight") else 0,
                    "l": links_of(e)[0][2], "a": e.get("arxiv"), "c": e.get("code"), "p": e.get("project"),
                    "v": str(e["venue"]) if e.get("venue") else None,
                    "s": (repo_stat(e) or {}).get("stars"), "u": (e.get("hf") or {}).get("upvotes")})
    ab_cut = (today - dt.timedelta(days=FEED_ABSTRACT_DAYS)).isoformat()
    for p in feed:
        if p.get("published", "") < site_cut:
            break
        it = {"k": "f", "id": p["id"], "t": p["title"], "d": p.get("published", ""),
              "au": ", ".join(p.get("authors", [])[:4]), "tp": p.get("topics", []), "em": p["emb"],
              "c": (p.get("code") or [None])[0], "pc": p.get("primary", ""), "v": venue_of(p.get("comment")),
              "pj": (p.get("project") or [None])[0], "s": p.get("stars") if p.get("code") else None,
              "u": (p.get("hf") or {}).get("upvotes")}
        if it["d"] >= ab_cut:  # keep the index small: older papers are searchable by title/authors only
            it["ab"] = p.get("abstract", "")[:300]
        idx.append({k: v for k, v in it.items() if v not in (None, [], "")} | {"k": "f", "id": p["id"], "t": p["title"]})
    topics_js = {t["id"]: [t["en"], t["zh"]] for t in topics}
    emb_js = {m["id"]: [m["en"], m["zh"]] for m in embs}
    (OUT / "data" / "index.json").write_text(
        json.dumps({"topics": topics_js, "emb": emb_js, "items": idx, "venues": {k: venue_slug(k) for k in sorted(VENUE_PAGES)}, "built": today.isoformat()}, ensure_ascii=False,
                   separators=(",", ":")), encoding="utf-8")

    # ---- index
    stats = (f'<div class="stats"><div><b>{len(entries)}</b>{bi("curated", "精选条目")}</div>'
             f'<div><b>{len(feed_week)}</b>{bi("new arXiv papers this week", "本周新 arXiv 论文")}</div>'
             f'<div><b>{len(topics)}</b>{bi("topics", "主题")}</div>'
             f'<div><b>{esc(latest_date or "—")}</b>{bi("latest intake", "最近收录")}</div></div>')
    topic_opts = "".join(f'<option value="{t["id"]}" data-en="{esc(t["en"])}" data-zh="{esc(t["zh"])}">{esc(t["en"])}</option>' for t in topics)
    emb_opts = "".join(f'<option value="{m["id"]}" data-en="{esc(m["en"])}" data-zh="{esc(m["zh"])}">{esc(m["en"])}</option>' for m in embs)
    venue_n: dict[str, int] = {}
    for it in idx:
        if it.get("v"):
            ser = str(it["v"]).rsplit(" ", 1)[0] if re.search(r" 20\d\d$", str(it["v"])) else str(it["v"])
            venue_n[ser] = venue_n.get(ser, 0) + 1
    venue_opts = ('<option value="*" data-en="Any accepted venue" data-zh="任意已录用会议/期刊">Any accepted venue</option>'
                  + "".join(f'<option value="{esc(v)}">{esc(v)} ({n})</option>'
                            for v, n in sorted(venue_n.items(), key=lambda x: (-x[1], x[0])) if n >= 2))
    search = f"""<section class="search" id="search">
<input id="q" type="search" placeholder="Search papers, code, datasets… / 搜索论文、代码（支持中文关键词）…" aria-label="Search" autocomplete="off">
<div class="filters">
<select id="f-topic" aria-label="Topic"><option value="" data-en="All topics" data-zh="全部主题">All topics</option>{topic_opts}</select>
<select id="f-emb" aria-label="Embodiment"><option value="" data-en="Any robot" data-zh="全部机器人形态">Any robot</option>{emb_opts}</select>
<select id="f-kind" aria-label="Source"><option value="" data-en="Curated + daily feed" data-zh="精选 + 每日论文">Curated + daily feed</option><option value="c" data-en="Curated only" data-zh="仅精选">Curated only</option><option value="f" data-en="Daily feed only" data-zh="仅每日论文">Daily feed only</option></select>
<select id="f-venue" aria-label="Venue"><option value="" data-en="Any venue" data-zh="全部会议/期刊">Any venue</option>{venue_opts}</select>
<select id="f-sort" aria-label="Sort"><option value="" data-en="Sort: best match" data-zh="排序：默认">Sort: best match</option><option value="new" data-en="Sort: newest" data-zh="排序：最新">Sort: newest</option><option value="stars" data-en="Sort: GitHub stars" data-zh="排序：GitHub 星标">Sort: GitHub stars</option><option value="hf" data-en="Sort: HF upvotes" data-zh="排序：HF 点赞">Sort: HF upvotes</option></select>
<label><input id="f-code" type="checkbox"> {bi("Has code", "有代码")}</label>
</div>
<p id="count" class="muted"></p>
<div id="results"></div>
</section>"""
    hi = [e for e in entries if e.get("highlight")]
    recent_picks = sorted((e for e in entries if e.get("added")), key=lambda e: str(e["added"]), reverse=True)[:6]
    picks_html = ""
    if recent_picks:
        picks_html = (f'<h2>{bi("Newly added picks", "最新精选")} <span class="muted">(<a href="picks.xml">{bi("Atom feed", "Atom 订阅")}</a>)</span></h2>'
                      f'<p class="muted">{bi("Notable new papers reviewed from the daily feed.", "从每日论文中审阅挑选的值得关注的新工作。")}</p>'
                      f'<div class="cards">{"".join(curated_card(e, tby, "") for e in recent_picks)}</div>')
    by_repo: dict[str, dict] = {}  # one row per repo; prefer the non-paper entry (e.g. "LeRobot" over a paper using it)
    for e in entries:
        k = repo_key(e.get("code"))
        if k and k in STATS and (k not in by_repo or (by_repo[k]["type"] == "paper" and e["type"] != "paper")):
            by_repo[k] = e
    popular = sorted(((STATS[k], e) for k, e in by_repo.items()), key=lambda x: -x[0]["stars"])[:12]
    gains, span = star_gains(load_history())

    def gain_badge(k: str) -> str:
        g = gains.get(k, 0)
        return f' <span class="badge rise" title="GitHub stars gained in the last {span} days">+{fmt_stars(g)}</span>' if g > 0 else ""

    def short(t: str) -> str:
        return title_html(t) if len(t) < 70 else title_html(t[:67]) + "…"

    popular_html = ""
    if popular:
        rows = "".join(
            f'<li><a href="{esc(e["code"])}" rel="noopener">{esc(e["code"].split("github.com/")[1].rstrip("/"))}</a>'
            f' <span class="gh">★ {fmt_stars(st["stars"])}</span>{gain_badge(repo_key(e["code"]) or "")}'
            f' <span class="muted">· <a href="e/{esc(e["id"])}.html">{short(e["title"])}</a></span></li>'
            for st, e in popular)
        popular_html = (f'<h2>{bi("Most-starred open-source code", "最受关注的开源代码")}</h2>'
                        f'<p class="muted">{bi("GitHub stars of curated entries, refreshed weekly.", "精选条目的 GitHub 星标数，每周更新。")}</p>'
                        f'<ol class="poplist">{rows}</ol>')
    # repos that gained the most GitHub stars over the last week (curated code + code of recent feed papers)
    rising_html = ""
    if gains:
        owner_of: dict[str, tuple[str, str, str]] = {}  # repo -> (repo url, title, detail link)
        for p in feed:
            for u in p.get("code") or []:
                k = repo_key(u)
                if k and k not in owner_of:
                    owner_of[k] = (u, p["title"], f'https://arxiv.org/abs/{p["id"]}')
        for k, e in by_repo.items():
            owner_of[k] = (e["code"], e["title"], f'e/{e["id"]}.html')
        top = sorted(((g, k) for k, g in gains.items() if g > 0 and k in owner_of), reverse=True)[:10]
        if top:
            rows = "".join(
                f'<li><a href="{esc(owner_of[k][0])}" rel="noopener">{esc(k)}</a> <span class="badge rise">+{fmt_stars(g)}</span>'
                f' <span class="muted">· <a href="{esc(owner_of[k][2])}">{short(owner_of[k][1])}</a></span></li>' for g, k in top)
            rising_html = (f'<h2>{bi("Rising this week", "本周升温")}</h2>'
                           f'<p class="muted">{bi(f"GitHub stars gained in the last {span} days by code from curated entries and recent arXiv papers.", f"精选条目与近期 arXiv 论文的代码在最近 {span} 天新增的 GitHub 星标。")}</p>'
                           f'<ol class="poplist">{rows}</ol>')
    # papers from the feed / curated data that the community upvoted on Hugging Face Daily Papers recently
    hf_html = ""
    hf_cut = (today - dt.timedelta(days=14)).isoformat()
    cur_by_arxiv = {str(e["arxiv"]): e for e in entries if e.get("arxiv")}
    hf_rows: dict[str, tuple[int, str, str]] = {}  # arxiv id -> (upvotes, title, our link)
    for p in feed:
        if p.get("hf") and str(p["hf"].get("date", "")) >= hf_cut:
            hf_rows[p["id"]] = (p["hf"]["upvotes"], p["title"], f'https://arxiv.org/abs/{p["id"]}')
    for a, e in cur_by_arxiv.items():
        if e.get("hf") and str(e["hf"].get("date", "")) >= hf_cut:
            hf_rows[a] = (e["hf"]["upvotes"], e["title"], f'e/{e["id"]}.html')
    hf_top = sorted(hf_rows.items(), key=lambda x: (-x[1][0], x[0]))[:8]
    if hf_top:
        rows = "".join(
            f'<li><a href="{esc(link)}">{short(t)}</a> <a class="badge rise" href="https://huggingface.co/papers/{esc(a)}" rel="noopener" title="Upvotes on Hugging Face Daily Papers">▲ {n}</a></li>'
            for a, (n, t, link) in hf_top)
        hf_html = (f'<h2>{bi("Upvoted on Hugging Face", "Hugging Face 热议")}</h2>'
                   f'<p class="muted">{bi("Robotics papers from our feed that made Hugging Face Daily Papers in the last 14 days, by community upvotes.", "最近 14 天登上 Hugging Face Daily Papers 的本站收录论文，按社区点赞数排序。")}</p>'
                   f'<ol class="poplist">{rows}</ol>')
    topic_grid = "".join(
        f'<a class="tile" href="topics/{t["id"]}.html"><h3>{bi(t["en"], t["zh"])}</h3>'
        f'<p>{bi(t["desc_en"], t["desc_zh"])}</p><span class="muted">{len(by_topic[t["id"]])} {bi("curated", "精选")} · '
        f'{len([p for p in feed_by_topic[t["id"]] if p.get("published", "") >= week_cut])} {bi("new this week", "本周新增")}</span></a>'
        for t in topics)
    fresh = "".join(feed_card(p, tby, "") for p in feed[:8])
    body = f"""<section class="hero">
<h1>{bi("The map of embodied AI & robot learning", "具身智能与机器人学习全景图")}</h1>
<p class="lead">{bi("Hand-verified papers, code, datasets, simulators and hardware with one-line takeaways in English and Chinese — plus every new robotics paper on arXiv, tagged by topic, every day.", "人工核验的论文、代码、数据集、仿真器与硬件，配中英文一句话要点；外加每天自动收录并按主题标注的 arXiv 机器人新论文。")}</p>
{stats}
<p class="start-link"><a class="more" href="start.html">{bi("New to embodied AI? Start with the reading path →", "刚入门具身智能？从入门路线开始 →")}</a></p>
</section>
{search}
<div id="home-static">
<h2>{bi("Topics", "主题")}</h2>
<div class="grid">{topic_grid}</div>
<p class="muted">{bi("By robot type:", "按机器人形态：")} {" · ".join(f'<a href="robots/{m["id"]}.html">{bi(m["en"], m["zh"])}</a>' for m in embs)}</p>
{picks_html}
{hf_html}
{rising_html}
{popular_html}
<h2>{bi("Highlights", "重点推荐")}</h2>
<div class="cards">{''.join(curated_card(e, tby, '') for e in hi)}</div>
<h2>{bi("Fresh from arXiv", "arXiv 最新")}</h2>
<div class="cards">{fresh or '<p class="muted">' + bi("The daily feed starts with the first scheduled intake.", "每日论文将在首次定时收录后出现。") + '</p>'}</div>
<p><a class="more" href="feed.html">{bi("See the full daily feed →", "查看完整每日论文 →")}</a></p>
</div>"""
    desc = "Bilingual (EN/中文), daily-updated map of embodied AI and robot learning: VLA, manipulation, tactile, humanoids, world models, sim-to-real, datasets and hardware."
    (OUT / "index.html").write_text(page("Embodied AI Radar · 具身智能雷达", body, "", desc, "",
                                         alt='\n<link rel="alternate" type="application/atom+xml" title="Agent picks · Embodied AI Radar" href="picks.xml">'), encoding="utf-8")

    # ---- topics
    tlist = "".join(f'<li><a href="{t["id"]}.html">{bi(t["en"], t["zh"])}</a> <span class="muted">({len(by_topic[t["id"]])})</span></li>' for t in topics)
    nbib = sum(1 for e in entries if e.get("bib"))
    bibnote = (f'<p><a href="../curated.bib" download>{bi(f"Download BibTeX for all {nbib} curated arXiv papers", f"下载全部 {nbib} 篇精选 arXiv 论文的 BibTeX")}</a></p>'
               if nbib else "")
    bibnote += (f'<p>{bi("Reuse the whole curated index (CC BY 4.0):", "复用全部精选数据（CC BY 4.0）：")} '
                f'<a href="../curated.json">curated.json</a> · <a href="../curated.csv" download>curated.csv</a></p>')
    bibnote += f'<p><a href="../venues/index.html">{bi("Browse papers by venue (CoRL, RSS, ICRA, NeurIPS…) →", "按会议/期刊浏览论文（CoRL、RSS、ICRA、NeurIPS…）→")}</a></p>'
    bibnote += f'<p><a href="../robots/index.html">{bi("Browse papers by robot type (humanoid, quadruped, dexterous hand…) →", "按机器人形态浏览（人形、四足、灵巧手…）→")}</a></p>'
    (OUT / "topics" / "index.html").write_text(page("Topics · Embodied AI Radar", f'<h1>{bi("Topics", "主题")}</h1><ul class="tlist">{tlist}</ul>' + bibnote, "../", desc, "topics/index.html"), encoding="utf-8")
    for t in topics:
        cur = sorted(by_topic[t["id"]], key=lambda e: (not e.get("highlight"), -int(e["year"])))
        recent = feed_by_topic[t["id"]][:TOPIC_FEED_MAX]
        in_topic = by_topic[t["id"]] + feed_by_topic[t["id"]]
        robot_links = " · ".join(
            f'<a href="../index.html?topic={t["id"]}&amp;robot={m["id"]}#search">{bi(m["en"], m["zh"])}</a> <span class="muted">({n})</span>'
            for m in embs if (n := sum(1 for x in in_topic if m["id"] in x.get("emb", []))))
        robot_row = f'<p class="muted">{bi("Search this topic by robot type:", "按机器人形态搜索本主题：")} {robot_links}</p>' if robot_links else ""
        body = f"""<h1>{bi(t["en"], t["zh"])}</h1>
<p class="lead">{bi(t["desc_en"], t["desc_zh"])}</p>
{robot_row}
<h2>{bi("Curated", "精选")} <span class="muted">({len(cur)})</span></h2>
<div class="cards">{''.join(curated_card(e, tby, '../') for e in cur)}</div>
<h2>{bi("Recent arXiv papers", "近期 arXiv 论文")} <span class="muted">({bi("auto-tagged", "自动标注")} · <a href="{t['id']}.xml">{bi("Atom feed", "Atom 订阅")}</a>)</span></h2>
<div class="cards">{''.join(feed_card(p, tby, '../') for p in recent) or '<p class="muted">—</p>'}</div>"""
        (OUT / "topics" / f"{t['id']}.html").write_text(
            page(f"{t['en']} · {t['zh']} · Embodied AI Radar", body, "../",
                 f"{t['desc_en']} Curated papers, code and datasets plus daily arXiv updates.", f"topics/{t['id']}.html",
                 alt=f'\n<link rel="alternate" type="application/atom+xml" title="{esc(t["en"])} · Embodied AI Radar" href="{t["id"]}.xml">'),
            encoding="utf-8")

    # ---- one permalink page per curated entry: e/<id>.html
    (OUT / "e").mkdir()
    for e in entries:
        t0 = e["topics"][0]
        related = sorted((r for r in by_topic[t0] if r["id"] != e["id"]),
                         key=lambda r: (not r.get("highlight"), -int(r["year"]), r["title"]))[:8]
        authors = (meta.get(e.get("arxiv") or "") or {}).get("authors") or []
        desc_e = f"{e['takeaway_en']} {e['takeaway_zh']}"
        (OUT / "e" / f"{e['id']}.html").write_text(
            page(f"{plain_title(e['title'])} · Embodied AI Radar", entry_page(e, tby, related, authors), "../",
                 desc_e, f"e/{e['id']}.html"), encoding="utf-8")

    # ---- feed: feed.html = newest day + archive; feed/<date>.html = one page per day
    all_days = sorted({p["published"] for p in feed if p.get("published")}, reverse=True)
    day_papers = {d: [p for p in feed if p.get("published") == d] for d in all_days}
    (OUT / "feed").mkdir(exist_ok=True)
    lead = f"""<p class="lead">{bi("New papers from cs.RO, plus robotics and embodied-AI papers from cs.CV / cs.LG / cs.AI / cs.CL, fetched automatically every day and tagged by keyword rules (tags can be wrong — curated entries are the verified ones).", "每天自动抓取 cs.RO 新论文，以及 cs.CV / cs.LG / cs.AI / cs.CL 中与机器人和具身智能相关的论文，并按关键词规则标注主题（自动标注可能有误，精选条目才是经过核验的）。")}</p>"""

    def day_summary(ps: list[dict]) -> str:
        n_code = sum(1 for p in ps if p.get("code"))
        n_venue = sum(1 for p in ps if venue_of(p.get("comment")))
        return (f'<p class="muted">{len(ps)} {bi("papers", "篇论文")} · {n_code} {bi("with code", "附代码")}'
                + (f' · {n_venue} {bi("accepted at a venue", "已被会议/期刊接收")}' if n_venue else "") + "</p>")

    def day_cards(ps: list[dict], root: str) -> str:
        # papers with code first, otherwise keep feed order
        ordered = [p for p in ps if p.get("code")] + [p for p in ps if not p.get("code")]
        return '<div class="cards">' + "".join(feed_card(p, tby, root) for p in ordered) + "</div>"

    def archive(root: str, current: str | None) -> str:
        items = "".join(
            f'<li>{"<b>" if d == current else ""}<a href="{root}feed/{d}.html">{esc(d)}</a>{"</b>" if d == current else ""} '
            f'<span class="muted">({len(day_papers[d])})</span></li>' for d in all_days)
        return f'<h2 id="archive">{bi("All days", "按日期浏览")}</h2><ul class="days">{items}</ul>' if items else ""

    for i, d in enumerate(all_days):
        newer = all_days[i - 1] if i > 0 else None
        older = all_days[i + 1] if i + 1 < len(all_days) else None
        pn = ('<p class="pager">'
              + (f'<a href="{older}.html">← {esc(older)}</a>' if older else "")
              + (f' <a href="{newer}.html">{esc(newer)} →</a>' if newer else "") + "</p>")
        body = f"""<h1>{bi("arXiv papers", "arXiv 论文")} · {esc(d)}</h1>
{lead}{day_summary(day_papers[d])}{pn}
{day_cards(day_papers[d], "../")}
{pn}{archive("../", d)}"""
        (OUT / "feed" / f"{d}.html").write_text(
            page(f"Embodied AI & robotics papers on arXiv, {d} · Embodied AI Radar", body, "../",
                 f"{len(day_papers[d])} new embodied AI and robotics papers on arXiv ({d}), tagged by topic; papers with code first.",
                 f"feed/{d}.html"), encoding="utf-8")

    if all_days:
        d0 = all_days[0]
        latest = (f'<h2 id="d{d0}">{bi("Latest", "最新")}: {esc(d0)}</h2>{day_summary(day_papers[d0])}'
                  f'{day_cards(day_papers[d0], "")}'
                  f'<p><a class="more" href="feed/{d0}.html">{bi("Permalink for this day →", "本日固定链接 →")}</a></p>')
    else:
        latest = '<p class="muted">' + bi("The first intake has not run yet.", "首次收录尚未运行。") + "</p>"
    body = f"""<h1>{bi("Daily arXiv feed", "每日 arXiv 论文")}</h1>
{lead}
<p><a href="index.html#search">{bi("Search and filter all of it →", "搜索与筛选 →")}</a> · <a href="#archive">{bi("Earlier days", "往日论文")}</a> · <a href="venues/index.html">{bi("By venue", "按会议/期刊")}</a> · <a href="robots/index.html">{bi("By robot type", "按机器人形态")}</a></p>
{latest}
{archive("", None)}"""
    (OUT / "feed.html").write_text(page("Daily arXiv feed · Embodied AI Radar", body, "", "New embodied AI and robotics papers from arXiv, every day, tagged by topic.", "feed.html"), encoding="utf-8")

    # ---- digests
    digests = sorted(DIGEST.glob("*.md"), reverse=True) if DIGEST.exists() else []
    dl = []
    for d in digests:
        md = d.read_text(encoding="utf-8")
        (OUT / "digest" / f"{d.stem}.html").write_text(
            page(f"Weekly digest {d.stem} · Embodied AI Radar", f'<article class="prose">{md_to_html(md)}</article>', "../",
                 f"Embodied AI Radar weekly digest {d.stem}", f"digest/{d.stem}.html"), encoding="utf-8")
        dl.append(f'<li><a href="{d.stem}.html">{esc(d.stem)}</a></li>')
    (OUT / "digest" / "index.html").write_text(
        page("Weekly digests · Embodied AI Radar",
             f'<h1>{bi("Weekly digests", "每周精选")}</h1><ul class="tlist">{"".join(dl) or "<li class=muted>—</li>"}</ul>',
             "../", "Weekly bilingual digests of embodied AI research.", "digest/index.html"), encoding="utf-8")

    # ---- related lists & learning resources
    kinds = [("list", "Related lists", "相关列表"), ("course", "Courses & textbooks", "课程与教材"),
             ("docs", "Tool docs", "工具文档"), ("community", "Communities", "社区")]
    res, _ = load_resources()
    rs = []
    for k, en, zh in kinds:
        items = [r for r in res if r["kind"] == k]
        if items:
            rs.append(f'<h2>{bi(en, zh)}</h2><ul class="tlist">' + "".join(
                f'<li><a href="{esc(r["url"])}" rel="noopener">{esc(r["name"])}</a>'
                + (' <span class="badge">中文</span>' if r["lang"] == "zh" else "")
                + f' — {bi(r["note_en"], r["note_zh"])}</li>' for r in items) + "</ul>")
    body = (f'<h1>{bi("Related lists & learning resources", "相关列表与学习资源")}</h1>'
            f'<p class="lead">{bi("Other good maps of the field, plus courses and docs we point newcomers to. Suggest more by opening an issue.", "领域内其他优秀的资源整理，以及推荐给新手的课程和文档。欢迎提 issue 补充。")}</p>'
            f'<p><a class="more" href="start.html">{bi("New here? Follow the reading path through the curated index →", "刚入门？按入门路线阅读精选条目 →")}</a></p>'
            + "".join(rs))
    (OUT / "resources.html").write_text(page("Learning resources · Embodied AI Radar", body, "",
        "Related embodied AI lists, robotics courses, tool docs and communities (EN/中文).", "resources.html"), encoding="utf-8")

    # ---- "start here" reading path
    eby = {e["id"]: e for e in entries}
    steps, _ = load_start(set(eby))
    if steps:
        n_items = sum(len(st["entries"]) for st in steps)
        sh = []
        for st in steps:
            rows = "".join(
                f'<li><a href="e/{esc(i)}.html">{title_html(eby[i]["title"])}</a> '
                f'<span class="muted">· {esc(str(eby[i]["year"]))}{" · " + esc(eby[i]["org"]) if eby[i].get("org") else ""}</span>'
                f'<br><span class="take">{bi(eby[i]["takeaway_en"], eby[i]["takeaway_zh"])}</span></li>'
                for i in st["entries"])
            sh.append(f'<h2>{bi(st["en"], st["zh"])}</h2><p class="muted">{bi(st["why_en"], st["why_zh"])}</p>'
                      f'<ol class="tlist path">{rows}</ol>')
        body = (f'<h1>{bi("Start here: a reading path", "入门路线：从这里开始读")}</h1>'
                f'<p class="lead">{bi(f"{len(steps)} steps, {n_items} papers, code bases and robots, picked from the curated index for newcomers. Each links to a page with the bilingual takeaway, code, BibTeX and related work. Skip any step you already know.", f"为新手从精选库中挑选的 {len(steps)} 个阶段、{n_items} 篇论文/代码/硬件。每一项都链接到详情页（中英文要点、代码、BibTeX 与相关工作）。已经熟悉的部分可以跳过。")}</p>'
                + "".join(sh)
                + f'<p class="muted">{bi("Courses and other lists: ", "课程与其他资源列表：")}<a href="resources.html">{bi("Learning resources", "学习资源")}</a> · '
                f'<a href="{REPO_URL}/issues/new">{bi("Suggest a change to this path", "对路线提建议")}</a></p>')
        (OUT / "start.html").write_text(page("Start here: embodied AI reading path · Embodied AI Radar", body, "",
            "A bilingual (EN/中文) reading path into embodied AI and robot learning: RL and imitation, visuomotor policies, VLA, simulation, locomotion, world models, perception and hardware.",
            "start.html"), encoding="utf-8")

    # ---- one .bib with every curated arXiv paper we have metadata for
    bibs = [e["bib"] for e in entries if e.get("bib")]
    (OUT / "curated.bib").write_text(
        "% Embodied AI Radar - curated papers (" + str(len(bibs)) + " entries), built from arXiv metadata (CC0).\n"
        f"% {SITE_URL}\n\n" + "\n\n".join(bibs) + "\n", encoding="utf-8")

    # ---- machine-readable export of the curated index (CC BY 4.0), JSON + CSV
    FIELDS = ["id", "title", "type", "arxiv", "year", "venue", "org", "url", "code", "project", "topics", "tags",
              "robot_types", "highlight", "added", "takeaway_en", "takeaway_zh", "github_stars", "page"]
    rows = []
    for e in entries:
        st = repo_stat(e) or {}
        rows.append({
            "id": e["id"], "title": e["title"], "type": e.get("type"), "arxiv": e.get("arxiv"),
            "year": e.get("year"), "venue": e.get("venue"), "org": e.get("org"), "url": e.get("url"),
            "code": e.get("code"), "project": e.get("project"), "topics": e["topics"], "tags": e.get("tags") or [],
            "robot_types": e.get("emb") or [], "highlight": bool(e.get("highlight")),
            "added": str(e["added"]) if e.get("added") else None,
            "takeaway_en": e["takeaway_en"], "takeaway_zh": e["takeaway_zh"],
            "github_stars": st.get("stars"), "page": f"{SITE_URL}e/{e['id']}.html"})
    (OUT / "curated.json").write_text(json.dumps({
        "name": "Embodied AI Radar - curated index", "source": SITE_URL,
        "license": "CC BY 4.0 (curated text and data); arXiv metadata CC0",
        "built": today.isoformat(), "count": len(rows), "fields": FIELDS, "items": rows},
        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(FIELDS)
    for r in rows:
        w.writerow(["; ".join(v) if isinstance(v, list) else ("" if v is None else v) for v in (r[f] for f in FIELDS)])
    # UTF-8 BOM so Excel opens the Chinese takeaways correctly
    (OUT / "curated.csv").write_text("\ufeff" + buf.getvalue(), encoding="utf-8")

    # ---- venue pages: venues/<slug>.html per venue+year with >= VENUE_MIN papers, venues/index.html
    (OUT / "venues").mkdir()
    vkeys = sorted(VENUE_PAGES, key=lambda k: (-int(k.rsplit(" ", 1)[1]), -(len(venues[k]["c"]) + len(venues[k]["f"])), k))
    vnote = bi("Feed papers are listed when their arXiv comment says they were accepted (e.g. 'Accepted to CoRL 2026'); papers that do not say so are missing, and the list grows as authors post camera-ready versions. Curated entries carry a hand-checked venue.",
               "日常 arXiv 论文仅在其 arXiv 备注写明已被接收（如 “Accepted to CoRL 2026”）时列入；未注明的论文不会出现，列表会随作者上传终稿而增加。精选条目的会议/期刊信息经过人工核对。")
    for k in vkeys:
        g = venues[k]
        cur = sorted(g["c"], key=lambda e: (not e.get("highlight"), e["title"]))
        fp = sorted(g["f"], key=lambda p: p.get("published", ""), reverse=True)
        fp = [p for p in fp if p.get("code")] + [p for p in fp if not p.get("code")]
        n_code = sum(1 for p in fp if p.get("code")) + sum(1 for e in cur if e.get("code"))
        parts = [f'<p class="muted"><a href="index.html">{bi("Venues", "会议/期刊")}</a> › {esc(k)}</p>',
                 f'<h1>{esc(k)} · {bi("papers", "论文")}</h1>',
                 f'<p class="lead">{bi(f"{len(cur) + len(fp)} embodied-AI and robotics papers accepted at {k}, {n_code} with code.", f"{len(cur) + len(fp)} 篇被 {k} 接收的具身智能与机器人论文，其中 {n_code} 篇附代码。")}</p>',
                 f'<p class="muted">{vnote}</p>',
                 f'<p><a href="../index.html?venue={esc(k.rsplit(" ", 1)[0])}#search">{bi("Search within this venue series →", "在该会议/期刊系列中搜索 →")}</a></p>']
        if cur:
            parts.append(f'<h2>{bi("Curated", "精选")} ({len(cur)})</h2><div class="cards">{"".join(curated_card(e, tby, "../") for e in cur)}</div>')
        if fp:
            parts.append(f'<h2>{bi("From the daily arXiv feed", "来自每日 arXiv")} ({len(fp)})</h2><div class="cards">{"".join(feed_card(p, tby, "../") for p in fp)}</div>')
        (OUT / "venues" / f"{venue_slug(k)}.html").write_text(
            page(f"{k} papers: embodied AI & robotics · Embodied AI Radar", "".join(parts), "../",
                 f"{len(cur) + len(fp)} embodied AI and robotics papers accepted at {k}, with code links, topics and BibTeX; updated daily from arXiv.",
                 f"venues/{venue_slug(k)}.html"), encoding="utf-8")
    vrows = "".join(f'<li><a href="{venue_slug(k)}.html">{esc(k)}</a> <span class="muted">({len(venues[k]["c"]) + len(venues[k]["f"])})</span></li>' for k in vkeys)
    (OUT / "venues" / "index.html").write_text(page("Papers by venue · Embodied AI Radar",
        f'<h1>{bi("Papers by venue", "按会议/期刊浏览")}</h1><p class="lead">{bi(f"Conferences and journals with at least {VENUE_MIN} papers in the radar, newest year first.", f"收录论文不少于 {VENUE_MIN} 篇的会议与期刊，按年份从新到旧排列。")}</p>'
        f'<p class="muted">{vnote}</p><ul class="tlist">{vrows or "<li class=muted>—</li>"}</ul>', "../",
        "Embodied AI and robotics papers grouped by venue: CoRL, RSS, ICRA, IROS, NeurIPS, CVPR and more.", "venues/index.html"), encoding="utf-8")

    # ---- robot-type pages: robots/<id>.html + robots/<id>.xml per embodiment, robots/index.html
    (OUT / "robots").mkdir()
    by_emb = {m["id"]: sorted((e for e in entries if m["id"] in e["emb"]),
                              key=lambda e: (not e.get("highlight"), -int(e["year"]), e["title"])) for m in embs}
    feed_by_emb = {m["id"]: [p for p in feed if m["id"] in p["emb"]] for m in embs}
    rnote = bi("Robot types are detected by keyword rules from titles, abstracts and tags, so a few papers may be misfiled.",
               "机器人形态由标题、摘要和标签中的关键词自动识别，个别论文可能归类有误。")
    for m in embs:
        cur, fp = by_emb[m["id"]], feed_by_emb[m["id"]]
        recent = fp[:TOPIC_FEED_MAX]
        n_code = sum(1 for e in cur if e.get("code"))
        tcount = " · ".join(
            f'<a href="../index.html?topic={t["id"]}&amp;robot={m["id"]}#search">{bi(t["en"], t["zh"])}</a> <span class="muted">({n})</span>'
            for t in topics if (n := sum(1 for x in cur + fp if t["id"] in (x.get("topics") or []))))
        body = (f'<p class="muted"><a href="index.html">{bi("Robot types", "机器人形态")}</a> › {bi(m["en"], m["zh"])}</p>'
                f'<h1>{bi(m["en"], m["zh"])}</h1>'
                f'<p class="lead">{bi(f"{len(cur)} curated papers, code and datasets ({n_code} with code) and {len(fp)} recent arXiv papers tagged “{m["en"]}”.", f"{len(cur)} 个精选论文、代码与数据集（{n_code} 个附代码），以及 {len(fp)} 篇近期 arXiv 论文，均与「{m["zh"]}」相关。")}</p>'
                f'<p class="muted">{rnote}</p>'
                + (f'<p class="muted">{bi("Search by topic:", "按主题搜索：")} {tcount}</p>' if tcount else "")
                + f'<h2>{bi("Curated", "精选")} <span class="muted">({len(cur)})</span></h2>'
                f'<div class="cards">{"".join(curated_card(e, tby, "../") for e in cur) or "<p class=muted>—</p>"}</div>'
                f'<h2>{bi("Recent arXiv papers", "近期 arXiv 论文")} <span class="muted">(<a href="{m["id"]}.xml">{bi("Atom feed", "Atom 订阅")}</a>)</span></h2>'
                f'<div class="cards">{"".join(feed_card(p, tby, "../") for p in recent) or "<p class=muted>—</p>"}</div>'
                + (f'<p><a href="../index.html?robot={m["id"]}&amp;src=f#search">{bi(f"All {len(fp)} feed papers in search →", f"在搜索中查看全部 {len(fp)} 篇 →")}</a></p>' if len(fp) > len(recent) else ""))
        (OUT / "robots" / f"{m['id']}.html").write_text(
            page(f"{m['en']} papers · {m['zh']} · Embodied AI Radar", body, "../",
                 f"{m['en']}: curated robot-learning papers, code and datasets plus new arXiv papers every day, with EN/中文 takeaways.",
                 f"robots/{m['id']}.html",
                 alt=f'\n<link rel="alternate" type="application/atom+xml" title="{esc(m["en"])} · Embodied AI Radar" href="{m["id"]}.xml">'),
            encoding="utf-8")
        (OUT / "robots" / f"{m['id']}.xml").write_text(
            atom(fp[:100], f"Embodied AI Radar — {m['en']}", f"robots/{m['id']}.xml", today), encoding="utf-8")
    rrows = "".join(f'<li><a href="{m["id"]}.html">{bi(m["en"], m["zh"])}</a> <span class="muted">({len(by_emb[m["id"]])} + {len(feed_by_emb[m["id"]])})</span></li>' for m in embs)
    (OUT / "robots" / "index.html").write_text(page("Papers by robot type · Embodied AI Radar",
        f'<h1>{bi("Papers by robot type", "按机器人形态浏览")}</h1><p class="lead">{bi("Humanoids, quadrupeds, dexterous hands, arms, drones and more. Counts: curated + recent arXiv papers.", "人形、四足、灵巧手、机械臂、无人机等。数字为：精选 + 近期 arXiv 论文。")}</p>'
        f'<p class="muted">{rnote}</p><ul class="tlist">{rrows}</ul>', "../",
        "Embodied AI and robot learning papers grouped by robot type: humanoid, quadruped, dexterous hand, robot arm, mobile robot, drone, autonomous driving.", "robots/index.html"), encoding="utf-8")

    # ---- 404, robots, sitemap, atom
    (OUT / "404.html").write_text(page("Not found · Embodied AI Radar", f'<h1>404</h1><p><a href="{SITE_URL}">{bi("Back to the radar", "返回首页")}</a></p>', SITE_URL, desc, "404.html"), encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n")
    urls = ["", "feed.html", "topics/index.html", "digest/index.html", "resources.html", "start.html"] + [f"topics/{t['id']}.html" for t in topics] + [f"digest/{d.stem}.html" for d in digests] + [f"feed/{d}.html" for d in all_days] + [f"e/{e['id']}.html" for e in entries] + ["venues/index.html"] + [f"venues/{venue_slug(k)}.html" for k in vkeys] + ["robots/index.html"] + [f"robots/{m['id']}.html" for m in embs]
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{SITE_URL}{u}</loc><lastmod>{today.isoformat()}</lastmod></url>\n" for u in urls)
        + "</urlset>\n", encoding="utf-8")
    (OUT / "feed.xml").write_text(atom(feed[:100], "Embodied AI Radar — daily arXiv", "feed.xml", today), encoding="utf-8")
    (OUT / "picks.xml").write_text(picks_atom(entries, today), encoding="utf-8")
    for t in topics:
        (OUT / "topics" / f"{t['id']}.xml").write_text(
            atom(feed_by_topic[t["id"]][:100], f"Embodied AI Radar — {t['en']}", f"topics/{t['id']}.xml", today), encoding="utf-8")
    n = sum(1 for _ in OUT.rglob("*.html"))
    print(f"built {n} pages into {OUT.relative_to(ROOT)}/ ({len(entries)} curated, {len(feed)} feed)")
    return 0


if __name__ == "__main__":
    sys.exit(build())
