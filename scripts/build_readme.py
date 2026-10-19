"""Regenerate the curated lists inside README.md and README.zh-CN.md from data/curated.

The lists live between <!-- radar:start --> and <!-- radar:end -->.
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


def md_title(t: str) -> str:
    t = re.sub(r"\$π_\{?([^}$]+)\}?\$", r"π\1", t)
    return t.replace("[", "\\[").replace("]", "\\]")


def render(lang: str) -> str:
    topics = load_topics()
    entries, _ = load_curated(strict=False)
    lines = [START, ""]
    toc = " · ".join(f"[{t['zh' if lang == 'zh' else 'en']}](#{t['id']})" for t in topics)
    lines += [toc, ""]
    for t in topics:
        name = t["zh"] if lang == "zh" else t["en"]
        items = sorted((e for e in entries if e["topics"][0] == t["id"]),
                       key=lambda e: (not e.get("highlight"), -int(e["year"]), e["title"]))
        also = [e for e in entries if t["id"] in e["topics"][1:]]
        lines.append(f'<a id="{t["id"]}"></a>')
        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"_{t['desc_zh'] if lang == 'zh' else t['desc_en']}_ "
                     f"[{'在网站上查看与最新论文' if lang == 'zh' else 'Browse with the latest papers'} →]({SITE}topics/{t['id']}.html)")
        lines.append("")
        for e in items:
            link = f"https://arxiv.org/abs/{e['arxiv']}" if e.get("arxiv") else (e.get("url") or e.get("code") or e.get("project"))
            star = "⭐ " if e.get("highlight") else ""
            extra = []
            if e.get("code") and e.get("code") != link:
                extra.append(f"[{'代码' if lang == 'zh' else 'code'}]({e['code']})")
            if e.get("project"):
                extra.append(f"[{'项目页' if lang == 'zh' else 'project'}]({e['project']})")
            take = e["takeaway_zh"] if lang == "zh" else e["takeaway_en"]
            tail = f" · {' · '.join(extra)}" if extra else ""
            lines.append(f"- {star}**[{md_title(e['title'])}]({link})** ({e['year']}) — {take}{tail}")
        if also:
            label = "另见" if lang == "zh" else "See also"
            lines.append(f"- _{label}:_ " + ", ".join(
                f"[{md_title(e['title']).split(':')[0]}](#{e['topics'][0]})" for e in also))
        lines.append("")
    lines.append(END)
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
    if check and stale:
        print("out of date (run python scripts/build_readme.py):", ", ".join(stale))
        return 1
    print("README lists", "checked" if check else "written", "-", ", ".join(stale) or "no changes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
