"""Generate the static website into _site/ from data/. Usage: python scripts/build_site.py

Pages: index (highlights + instant search), one page per topic, the daily arXiv feed,
weekly digests, plus data/index.json for client-side search, sitemap.xml and feed.xml (Atom).
Bilingual: every text exists in EN and ZH; CSS shows one based on <html class="zh">.
"""
from __future__ import annotations

import datetime as dt
import html
import json
import re
import shutil
import sys
from pathlib import Path

from repo_stats import load_stats, repo_key
from radar import ROOT, classify, venue_of, load_arxiv_feed, load_curated, load_embodiments, load_resources, load_topics

OUT = ROOT / "_site"
SRC = ROOT / "site_src"
DIGEST = ROOT / "digest"
SITE_URL = "https://hu-zlatan.github.io/embodied-ai-radar/"
REPO_URL = "https://github.com/hu-zlatan/embodied-ai-radar"
FEED_DAYS_ON_SITE = 60   # feed papers kept in the search index
FEED_DAYS_PAGE = 7       # days shown on the feed page
TOPIC_FEED_MAX = 40      # recent feed papers per topic page
FEED_ABSTRACT_DAYS = 21  # abstracts (for search) kept in the index only for this many days

esc = html.escape
EMB: dict[str, dict] = {}  # embodiment id -> {en, zh}, filled in build()
STATS: dict[str, dict] = {}  # 'owner/repo' -> {stars, pushed, archived}, from data/repo_stats.json


def fmt_stars(n: int) -> str:
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def repo_stat(e: dict) -> dict | None:
    """GitHub stats for the entry's code repo (or website/project if that is a GitHub repo)."""
    for k in ("code", "url", "project"):
        st = STATS.get(repo_key(e.get(k)) or "")
        if st:
            return st
    return None


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


def title_html(t: str) -> str:
    # Render the few LaTeX titles we have ($π_0$, $π_{0.5}$) readably.
    t = re.sub(r"\$π_\{?([^}$]+)\}?\$", r"π\1", t)
    return esc(t).replace("π0.5", "π<sub>0.5</sub>").replace("π0", "π<sub>0</sub>")


def curated_card(e: dict, topics_by_id: dict, root: str) -> str:
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
    st = repo_stat(e)
    if st:
        linkrow += f' <span class="gh" title="GitHub stars">★ {fmt_stars(st["stars"])}</span>'
        if st.get("archived"):
            linkrow += f' <span class="badge">{bi("archived", "已归档")}</span>'
    meta = " · ".join(x for x in [esc(str(e["year"])), esc(e.get("org", ""))] if x)
    if e.get("venue"):
        meta += f' <span class="badge venue">{esc(str(e["venue"]))}</span>'
    return f"""<article class="card" id="{esc(e['id'])}">
<div class="meta"><span class="badge">{bi(en, zh)}</span> {meta} {star}</div>
<h3><a href="{esc(main)}" rel="noopener">{title_html(e['title'])}</a></h3>
<p class="take">{bi(e['takeaway_en'], e['takeaway_zh'])}</p>
<div class="links">{linkrow}</div>
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
    proj = "".join(f' · <a href="{esc(u)}" rel="noopener">{bi("Project", "项目页")}</a>' for u in p.get("project", [])[:1])
    has_code = '<span class="badge code">code</span>' if p.get("code") else ""
    v = venue_of(p.get("comment"))
    if v:
        has_code += f' <span class="badge venue">{esc(v)}</span>'
    return f"""<article class="card feed" id="arxiv-{esc(p['id'])}">
<div class="meta"><span class="badge">arXiv {esc(p.get('primary', ''))}</span> {esc(p.get('published', ''))} {has_code}</div>
<h3><a href="https://arxiv.org/abs/{esc(p['id'])}" rel="noopener">{esc(p['title'])}</a></h3>
<p class="authors">{esc(authors)}</p>
<details><summary>{bi("Abstract", "摘要")}</summary><p>{esc(p.get('abstract', ''))}</p></details>
<div class="links"><a href="https://arxiv.org/abs/{esc(p['id'])}" rel="noopener">arXiv</a> · <a href="https://arxiv.org/pdf/{esc(p['id'])}" rel="noopener">PDF</a>{code}{proj}</div>
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
    for e in entries:
        e["emb"] = classify(" ".join([e["takeaway_en"], " ".join(e.get("tags") or [])]), embs, title=e["title"], threshold=1)
    for p in feed:
        p["emb"] = classify(p.get("abstract", ""), embs, title=p.get("title", ""), threshold=1)

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
                    "s": (repo_stat(e) or {}).get("stars")})
    ab_cut = (today - dt.timedelta(days=FEED_ABSTRACT_DAYS)).isoformat()
    for p in feed:
        if p.get("published", "") < site_cut:
            break
        it = {"k": "f", "id": p["id"], "t": p["title"], "d": p.get("published", ""),
              "au": ", ".join(p.get("authors", [])[:4]), "tp": p.get("topics", []), "em": p["emb"],
              "c": (p.get("code") or [None])[0], "pc": p.get("primary", ""), "v": venue_of(p.get("comment")),
              "pj": (p.get("project") or [None])[0]}
        if it["d"] >= ab_cut:  # keep the index small: older papers are searchable by title/authors only
            it["ab"] = p.get("abstract", "")[:300]
        idx.append({k: v for k, v in it.items() if v not in (None, [], "")} | {"k": "f", "id": p["id"], "t": p["title"]})
    topics_js = {t["id"]: [t["en"], t["zh"]] for t in topics}
    emb_js = {m["id"]: [m["en"], m["zh"]] for m in embs}
    (OUT / "data" / "index.json").write_text(
        json.dumps({"topics": topics_js, "emb": emb_js, "items": idx, "built": today.isoformat()}, ensure_ascii=False,
                   separators=(",", ":")), encoding="utf-8")

    # ---- index
    stats = (f'<div class="stats"><div><b>{len(entries)}</b>{bi("curated", "精选条目")}</div>'
             f'<div><b>{len(feed_week)}</b>{bi("new arXiv papers this week", "本周新 arXiv 论文")}</div>'
             f'<div><b>{len(topics)}</b>{bi("topics", "主题")}</div>'
             f'<div><b>{esc(latest_date or "—")}</b>{bi("latest intake", "最近收录")}</div></div>')
    topic_opts = "".join(f'<option value="{t["id"]}" data-en="{esc(t["en"])}" data-zh="{esc(t["zh"])}">{esc(t["en"])}</option>' for t in topics)
    emb_opts = "".join(f'<option value="{m["id"]}" data-en="{esc(m["en"])}" data-zh="{esc(m["zh"])}">{esc(m["en"])}</option>' for m in embs)
    search = f"""<section class="search" id="search">
<input id="q" type="search" placeholder="Search papers, code, datasets… / 搜索论文、代码、数据集…" aria-label="Search" autocomplete="off">
<div class="filters">
<select id="f-topic" aria-label="Topic"><option value="" data-en="All topics" data-zh="全部主题">All topics</option>{topic_opts}</select>
<select id="f-emb" aria-label="Embodiment"><option value="" data-en="Any robot" data-zh="全部机器人形态">Any robot</option>{emb_opts}</select>
<select id="f-kind" aria-label="Source"><option value="" data-en="Curated + daily feed" data-zh="精选 + 每日论文">Curated + daily feed</option><option value="c" data-en="Curated only" data-zh="仅精选">Curated only</option><option value="f" data-en="Daily feed only" data-zh="仅每日论文">Daily feed only</option></select>
<label><input id="f-code" type="checkbox"> {bi("Has code", "有代码")}</label>
</div>
<p id="count" class="muted"></p>
<div id="results"></div>
</section>"""
    hi = [e for e in entries if e.get("highlight")]
    recent_picks = sorted((e for e in entries if e.get("added")), key=lambda e: str(e["added"]), reverse=True)[:6]
    picks_html = ""
    if recent_picks:
        picks_html = (f'<h2>{bi("Newly added picks", "最新精选")}</h2>'
                      f'<p class="muted">{bi("Notable new papers reviewed from the daily feed.", "从每日论文中审阅挑选的值得关注的新工作。")}</p>'
                      f'<div class="cards">{"".join(curated_card(e, tby, "") for e in recent_picks)}</div>')
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
</section>
{search}
<div id="home-static">
<h2>{bi("Topics", "主题")}</h2>
<div class="grid">{topic_grid}</div>
{picks_html}
<h2>{bi("Highlights", "重点推荐")}</h2>
<div class="cards">{''.join(curated_card(e, tby, '') for e in hi)}</div>
<h2>{bi("Fresh from arXiv", "arXiv 最新")}</h2>
<div class="cards">{fresh or '<p class="muted">' + bi("The daily feed starts with the first scheduled intake.", "每日论文将在首次定时收录后出现。") + '</p>'}</div>
<p><a class="more" href="feed.html">{bi("See the full daily feed →", "查看完整每日论文 →")}</a></p>
</div>"""
    desc = "Bilingual (EN/中文), daily-updated map of embodied AI and robot learning: VLA, manipulation, tactile, humanoids, world models, sim-to-real, datasets and hardware."
    (OUT / "index.html").write_text(page("Embodied AI Radar · 具身智能雷达", body, "", desc, ""), encoding="utf-8")

    # ---- topics
    tlist = "".join(f'<li><a href="{t["id"]}.html">{bi(t["en"], t["zh"])}</a> <span class="muted">({len(by_topic[t["id"]])})</span></li>' for t in topics)
    (OUT / "topics" / "index.html").write_text(page("Topics · Embodied AI Radar", f'<h1>{bi("Topics", "主题")}</h1><ul class="tlist">{tlist}</ul>', "../", desc, "topics/index.html"), encoding="utf-8")
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

    # ---- feed page
    days = sorted({p["published"] for p in feed}, reverse=True)[:FEED_DAYS_PAGE]
    sections = []
    for d in days:
        ps = [p for p in feed if p["published"] == d]
        sections.append(f'<h2 id="d{d}">{esc(d)} <span class="muted">({len(ps)})</span></h2><div class="cards">'
                        + "".join(feed_card(p, tby, "") for p in ps) + "</div>")
    body = f"""<h1>{bi("Daily arXiv feed", "每日 arXiv 论文")}</h1>
<p class="lead">{bi("New papers from cs.RO, plus robotics and embodied-AI papers from cs.CV / cs.LG / cs.AI / cs.CL, fetched automatically every day and tagged by keyword rules (tags can be wrong — curated entries are the verified ones).", "每天自动抓取 cs.RO 新论文，以及 cs.CV / cs.LG / cs.AI / cs.CL 中与机器人和具身智能相关的论文，并按关键词规则标注主题（自动标注可能有误，精选条目才是经过核验的）。")}</p>
<p><a href="index.html#search">{bi("Search and filter all of it →", "搜索与筛选 →")}</a></p>
{''.join(sections) or '<p class="muted">' + bi("The first intake has not run yet.", "首次收录尚未运行。") + '</p>'}"""
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
            + "".join(rs))
    (OUT / "resources.html").write_text(page("Learning resources · Embodied AI Radar", body, "",
        "Related embodied AI lists, robotics courses, tool docs and communities (EN/中文).", "resources.html"), encoding="utf-8")

    # ---- 404, robots, sitemap, atom
    (OUT / "404.html").write_text(page("Not found · Embodied AI Radar", f'<h1>404</h1><p><a href="{SITE_URL}">{bi("Back to the radar", "返回首页")}</a></p>', SITE_URL, desc, "404.html"), encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n")
    urls = ["", "feed.html", "topics/index.html", "digest/index.html", "resources.html"] + [f"topics/{t['id']}.html" for t in topics] + [f"digest/{d.stem}.html" for d in digests]
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{SITE_URL}{u}</loc><lastmod>{today.isoformat()}</lastmod></url>\n" for u in urls)
        + "</urlset>\n", encoding="utf-8")
    (OUT / "feed.xml").write_text(atom(feed[:100], "Embodied AI Radar — daily arXiv", "feed.xml", today), encoding="utf-8")
    for t in topics:
        (OUT / "topics" / f"{t['id']}.xml").write_text(
            atom(feed_by_topic[t["id"]][:100], f"Embodied AI Radar — {t['en']}", f"topics/{t['id']}.xml", today), encoding="utf-8")
    n = sum(1 for _ in OUT.rglob("*.html"))
    print(f"built {n} pages into {OUT.relative_to(ROOT)}/ ({len(entries)} curated, {len(feed)} feed)")
    return 0


if __name__ == "__main__":
    sys.exit(build())
