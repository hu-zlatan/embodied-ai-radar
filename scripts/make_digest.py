"""Draft a bilingual weekly digest: digest/YYYY-Www.md.

Sections: editor's picks (curated entries whose `added` date falls in the week),
papers upvoted on Hugging Face Daily Papers,
repos rising on GitHub (star gains over the 7 days up to the week's end, once the history is long enough),
numbers per topic and per robot type, and new papers with code by topic (from the daily feed).
Usage: python scripts/make_digest.py [--week 2026-W43] [--force]
Without --week, uses the most recent complete ISO week (Mon–Sun).
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys

from hf_papers import load as load_hf
from radar import ROOT, classify, load_arxiv_feed, load_curated, load_embodiments, load_topics, venue_of
from repo_stats import apply_feed_stats, load_feed_stats, load_history, repo_key, star_gains

PER_TOPIC = 6
RISING = 8


def week_bounds(week: str) -> tuple[dt.date, dt.date]:
    y, w = week.split("-W")
    start = dt.date.fromisocalendar(int(y), int(w), 1)
    return start, start + dt.timedelta(days=6)


def clean_title(t: str) -> str:
    return re.sub(r"\$π_\{?([^}$]+)\}?\$", r"π\1", t).replace("[", "(").replace("]", ")")


def rising_section(entries: list[dict], end: dt.date) -> list[str]:
    """Repos (curated code + feed paper code) that gained the most GitHub stars in the 7 days up to `end`."""
    hist = {d: v for d, v in load_history().items() if d <= end.isoformat()}
    gains, span = star_gains(hist)
    if not gains:
        return []
    owner: dict[str, tuple[str, str, str]] = {}  # repo -> (repo url, title, link)
    for p in load_arxiv_feed():
        for u in p.get("code") or []:
            k = repo_key(u)
            if k and k not in owner:
                owner[k] = (u, p["title"], f"https://arxiv.org/abs/{p['id']}")
    for e in entries:
        k = repo_key(e.get("code"))
        if k:
            owner[k] = (e["code"], e["title"], f"https://hu-zlatan.github.io/embodied-ai-radar/e/{e['id']}.html")
    top = sorted(((g, k) for k, g in gains.items() if g > 0 and k in owner), reverse=True)[:RISING]
    if not top:
        return []
    L = ["", "## Rising on GitHub · GitHub 升温榜", "",
         f"_Stars gained in the {span} days to {max(hist)}. 截至 {max(hist)} 的 {span} 天内新增星标。_", ""]
    for g, k in top:
        url, title, link = owner[k]
        name = url.split("github.com/")[-1].rstrip("/")
        L.append(f"- [{name}]({url}) **+{g}** · [{clean_title(title)}]({link})")
    return L


def hf_section(entries: list[dict], start: dt.date, end: dt.date) -> list[str]:
    """Our papers listed on Hugging Face Daily Papers during the week, by upvotes."""
    hf = {k: v for k, v in load_hf().items() if start.isoformat() <= str(v.get("date", "")) <= end.isoformat()}
    if not hf:
        return []
    titles = {p["id"]: p["title"] for p in load_arxiv_feed()} | {str(e["arxiv"]): e["title"] for e in entries if e.get("arxiv")}
    top = sorted(((v["upvotes"], k) for k, v in hf.items() if k in titles), key=lambda x: (-x[0], x[1]))[:RISING]
    if not top:
        return []
    L = ["", "## Upvoted on Hugging Face · Hugging Face 热议", "",
         "_Papers from our feed listed on Hugging Face Daily Papers this week, by upvotes. 本周登上 Hugging Face Daily Papers 的收录论文，按点赞数排序。_", ""]
    for n, k in top:
        L.append(f"- [{clean_title(titles[k])}](https://arxiv.org/abs/{k}) · [▲ {n}](https://huggingface.co/papers/{k})")
    return L


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--week")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    if args.week:
        week = args.week
    else:
        last = dt.date.today() - dt.timedelta(days=dt.date.today().isoweekday())
        y, w, _ = last.isocalendar()
        week = f"{y}-W{w:02d}"
    start, end = week_bounds(week)
    out = ROOT / "digest" / f"{week}.md"
    if out.exists() and not args.force:
        print(f"{out.name} exists; use --force to overwrite")
        return 0
    topics = load_topics()
    entries, _ = load_curated(strict=False)
    feed = [p for p in load_arxiv_feed() if start.isoformat() <= p.get("published", "") <= end.isoformat()]
    apply_feed_stats(feed, load_feed_stats())  # drop code links known to 404
    picks = [e for e in entries if e.get("added") and start.isoformat() <= str(e["added"]) <= end.isoformat()]

    L = [f"# Embodied AI Radar · Weekly {week} · 具身智能雷达周报", "",
         f"{start.isoformat()} → {end.isoformat()} · {len(feed)} new arXiv papers · {len([p for p in feed if p.get('code')])} with code",
         f"本周共收录 {len(feed)} 篇 arXiv 新论文，其中 {len([p for p in feed if p.get('code')])} 篇附代码。", ""]
    L += ["## Editor's picks · 本周精选", ""]
    if picks:
        for e in picks:
            link = f"https://arxiv.org/abs/{e['arxiv']}" if e.get("arxiv") else (e.get("url") or e.get("code"))
            L.append(f"- **[{clean_title(e['title'])}]({link})** — {e['takeaway_en']} / {e['takeaway_zh']}"
                     f" · [details · 详情](https://hu-zlatan.github.io/embodied-ai-radar/e/{e['id']}.html)")
    else:
        L.append("- _No new curated picks this week. 本周暂无新增精选。_")
    accepted = sorted(((venue_of(p.get("comment")), p) for p in feed if venue_of(p.get("comment"))),
                      key=lambda vp: (vp[0], vp[1]["id"]))
    if accepted:
        L += ["", "## Accepted at venues · 已被会议/期刊接收", "",
              "_From the authors' arXiv comments. 根据作者在 arXiv 上的备注。"
              " [All papers per conference · 按会议汇总](https://hu-zlatan.github.io/embodied-ai-radar/venues/index.html)_", ""]
        for v, p in accepted:
            extra = "".join(f" · [{k}]({p[k][0]})" for k in ("code", "project") if p.get(k))
            L.append(f"- **{v}** · [{clean_title(p['title'])}](https://arxiv.org/abs/{p['id']}){extra}")
    L += hf_section(entries, start, end)
    L += rising_section(entries, end)
    L += ["", "## By topic · 分主题统计", ""]
    for t in topics:
        n = len([p for p in feed if t["id"] in p.get("topics", [])])
        L.append(f"- {t['en']} · {t['zh']}: **{n}**")
    embs = load_embodiments()
    if embs:
        L += ["", "## By robot type · 分机器人类型统计", "",
              "_Keyword-matched on title and abstract; a paper can count for several types. 按标题与摘要关键词匹配，一篇论文可计入多个类型。_", ""]
        for m in embs:
            n = sum(1 for p in feed if m["id"] in classify(p.get("abstract", ""), embs, title=p.get("title", ""), threshold=1))
            L.append(f"- {m['en']} · {m['zh']}: **{n}**")
    L += ["", "## New papers with code · 本周附代码的新论文", ""]
    for t in topics:
        ps = [p for p in feed if t["id"] in p.get("topics", []) and p.get("code")][:PER_TOPIC]
        if not ps:
            continue
        L += [f"### {t['en']} · {t['zh']}", ""]
        for p in ps:
            L.append(f"- [{clean_title(p['title'])}](https://arxiv.org/abs/{p['id']}) · [code]({p['code'][0]})"
                     + (f" · [project]({p['project'][0]})" if p.get("project") else ""))
        L.append("")
    L += ["---", "",
          "Auto-tagged by keyword rules; picks are reviewed by the maintainer agent. "
          "[Website](https://hu-zlatan.github.io/embodied-ai-radar/) · [GitHub](https://github.com/hu-zlatan/embodied-ai-radar)"
          " · New to the field? [Reading path](https://hu-zlatan.github.io/embodied-ai-radar/start.html)",
          "",
          "主题为关键词规则自动标注；精选由维护智能体审阅。刚入门？看[入门路线](https://hu-zlatan.github.io/embodied-ai-radar/start.html?lang=zh)。"]
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({len(feed)} papers, {len(picks)} picks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
