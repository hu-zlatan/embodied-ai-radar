"""Regenerate the curated lists from data/curated.

README.md and README.zh-CN.md show a short list per topic (rated entries ⭐⭐⭐/⭐⭐/⭐, then the
newest picks) between <!-- radar:start --> and <!-- radar:end -->. The complete
lists go to lists/<topic>.md and lists/<topic>.zh-CN.md, because GitHub stops
rendering a README at 512 KB and everything after the lists was buried anyway.
Usage: python scripts/build_readme.py          # rewrite in place
       python scripts/build_readme.py --check  # exit 1 if out of date (CI)
"""
from __future__ import annotations

import re
import sys

from radar import ROOT, load_curated, load_resources, load_topics

START, END = "<!-- radar:start -->", "<!-- radar:end -->"
RSTART, REND = "<!-- resources:start -->", "<!-- resources:end -->"
KIND_LABEL = {"list": ("Related lists", "相关列表"), "course": ("Courses & textbooks", "课程与教材"),
              "docs": ("Tool docs", "工具文档"), "community": ("Communities", "社区")}
SITE = "https://hu-zlatan.github.io/embodied-ai-radar/"
README_TOP = 12  # entries per topic in the README


def md_title(t: str) -> str:
    t = re.sub(r"\$([πΨ])_\{?([^}$]+)\}?\$", r"\1\2", t)
    return t.replace("[", "\\[").replace("]", "\\]").replace("*", "\\*")


def in_topic(entries: list[dict], tid: str) -> list[dict]:
    return sorted((e for e in entries if e["topics"][0] == tid),
                  key=lambda e: (-e["rating"], -int(e["year"]), e["title"]))


def entry_line(e: dict, lang: str) -> str:
    link = f"https://arxiv.org/abs/{e['arxiv']}" if e.get("arxiv") else (e.get("url") or e.get("code") or e.get("project"))
    star = "⭐" * e["rating"] + " " if e["rating"] else ""
    extra = []
    if e.get("code") and e.get("code") != link:
        extra.append(f"[{'代码' if lang == 'zh' else 'code'}]({e['code']})")
    if e.get("project"):
        extra.append(f"[{'项目页' if lang == 'zh' else 'project'}]({e['project']})")
    take = e["takeaway_zh"] if lang == "zh" else e["takeaway_en"]
    tail = f" · {' · '.join(extra)}" if extra else ""
    return f"- {star}**[{md_title(e['title'])}]({link})** ({e['year']}) — {take}{tail}"


def top_entries(items: list[dict]) -> list[dict]:
    """Rated entries first (⭐⭐⭐, ⭐⭐, ⭐), then the most recently added picks, then the newest papers."""
    rated = [e for e in items if e["rating"]]  # in_topic() already orders them by rating
    rest = sorted((e for e in items if not e["rating"]),
                  key=lambda e: (str(e.get("added") or ""), int(e["year"])), reverse=True)
    return (rated + rest)[:README_TOP]


def list_path(tid: str, lang: str) -> str:
    return f"lists/{tid}.zh-CN.md" if lang == "zh" else f"lists/{tid}.md"


def render(lang: str) -> str:
    zh = lang == "zh"
    topics = load_topics()
    entries, _ = load_curated(strict=False)
    lines = [START, ""]
    toc = " · ".join(f"[{t['zh' if zh else 'en']}](#{t['id']})" for t in topics)
    lines += [toc, ""]
    for t in topics:
        name = t["zh"] if zh else t["en"]
        items = in_topic(entries, t["id"])
        lines.append(f'<a id="{t["id"]}"></a>')
        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"_{t['desc_zh'] if zh else t['desc_en']}_ "
                     f"[{'在网站上查看与最新论文' if zh else 'Browse with the latest papers'} →]({SITE}topics/{t['id']}.html)")
        lines.append("")
        lines += [entry_line(e, lang) for e in top_entries(items)]
        if len(items) > README_TOP:
            label = f"查看全部 {len(items)} 条" if zh else f"All {len(items)} entries"
            lines += ["", f"**[{label} →]({list_path(t['id'], lang)})**"]
        lines.append("")
    lines.append(END)
    return "\n".join(lines)


def render_list(t: dict, lang: str, topics: list[dict], entries: list[dict]) -> str:
    """One complete topic list, readable on GitHub without the site."""
    zh = lang == "zh"
    items = in_topic(entries, t["id"])
    also = [e for e in entries if t["id"] in e["topics"][1:]]
    readme = "README.zh-CN.md" if zh else "README.md"
    fname = (lambda tid: f"{tid}.zh-CN.md") if zh else (lambda tid: f"{tid}.md")
    other = f"{t['id']}.md" if zh else f"{t['id']}.zh-CN.md"
    lines = [f"# {t['zh' if zh else 'en']}", "",
             f"_{t['desc_zh'] if zh else t['desc_en']}_", "",
             (f"共 {len(items)} 条。⭐⭐⭐ 必读（每个主题仅一篇）· ⭐⭐ 强烈推荐 · ⭐ 推荐。由 [`data/curated/{t['id']}.yaml`](../data/curated/{t['id']}.yaml) 生成，请勿直接编辑。"
              if zh else
              f"{len(items)} entries. ⭐⭐⭐ must-read (one per topic) · ⭐⭐ highly recommended · ⭐ recommended. Generated from [`data/curated/{t['id']}.yaml`](../data/curated/{t['id']}.yaml); edit the YAML, not this file."),
             "",
             (f"[返回 README](../{readme}) · [在网站上查看]({SITE}topics/{t['id']}.html) · [English]({other})"
              if zh else
              f"[Back to the README](../{readme}) · [Browse on the website]({SITE}topics/{t['id']}.html) · [中文]({other})"),
             ""]
    lines.append(" · ".join(f"**{x['zh' if zh else 'en']}**" if x["id"] == t["id"]
                            else f"[{x['zh' if zh else 'en']}]({fname(x['id'])})" for x in topics))
    lines.append("")
    lines += [entry_line(e, lang) for e in items]
    if also:
        lines += ["", f"**{'另见' if zh else 'See also'}**", ""]
        lines.append(", ".join(f"[{md_title(e['title']).split(':')[0]}]({fname(e['topics'][0])})" for e in also))
    lines.append("")
    return "\n".join(lines)


def render_resources(lang: str) -> str:
    res, _ = load_resources()
    zh = lang == "zh"
    lines = [RSTART, ""]
    for kind, (en_label, zh_label) in KIND_LABEL.items():
        items = [r for r in res if r["kind"] == kind]
        if not items:
            continue
        lines += [f"**{zh_label if zh else en_label}**", ""]
        for r in items:
            tag = " `中文`" if r["lang"] == "zh" else ""
            lines.append(f"- [{md_title(r['name'])}]({r['url']}){tag} — {r['note_zh'] if zh else r['note_en']}")
        lines.append("")
    lines.append(REND)
    return "\n".join(lines)


def splice(text: str, start: str, end: str, body: str) -> str | None:
    if start not in text or end not in text:
        return None
    return text.split(start)[0] + body + text.split(end, 1)[1]


def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for fname, lang in (("README.md", "en"), ("README.zh-CN.md", "zh")):
        path = ROOT / fname
        text = path.read_text(encoding="utf-8")
        new = splice(text, START, END, render(lang))
        new = new and splice(new, RSTART, REND, render_resources(lang))
        if new is None:
            print(f"{fname}: markers missing")
            return 1
        if new != text:
            stale.append(fname)
            if not check:
                path.write_text(new, encoding="utf-8")
    topics = load_topics()
    entries, _ = load_curated(strict=False)
    for t in topics:
        for lang in ("en", "zh"):
            path = ROOT / list_path(t["id"], lang)
            new = render_list(t, lang, topics, entries)
            if not path.exists() or path.read_text(encoding="utf-8") != new:
                stale.append(list_path(t["id"], lang))
                if not check:
                    path.parent.mkdir(exist_ok=True)
                    path.write_text(new, encoding="utf-8")
    if check and stale:
        print("out of date (run python scripts/build_readme.py):", ", ".join(stale))
        return 1
    print("README lists", "checked" if check else "written", "-", ", ".join(stale) or "no changes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
