"""Online verification of curated data (runs in GitHub Actions; needs network).

1. Every curated arXiv ID must exist and its arXiv title must match the curated title.
2. Every curated URL (url, code, project) must answer with HTTP < 400.

Writes a Markdown report to $GITHUB_STEP_SUMMARY (if set) and to stdout. Exit 1 on failures.
Usage: python scripts/verify_curated.py [--no-links]
"""
from __future__ import annotations

import argparse
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from radar import load_curated, norm_title

NS = {"a": "http://www.w3.org/2005/Atom"}
UA = {"User-Agent": "embodied-ai-radar-verify/1.0 (+https://github.com/hu-zlatan/embodied-ai-radar)"}


def arxiv_titles(ids: list[str]) -> dict[str, str]:
    out = {}
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"id_list": ",".join(chunk), "max_results": len(chunk)})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                    root = ET.fromstring(r.read())
                break
            except Exception as ex:
                print(f"arXiv fetch failed ({ex}), retrying")
                time.sleep(10 * (attempt + 1))
        else:
            raise RuntimeError("arXiv API unreachable")
        for e in root.findall("a:entry", NS):
            eid = (e.findtext("a:id", default="", namespaces=NS) or "").rsplit("/abs/", 1)[-1]
            eid = eid.split("v")[0] if "v" in eid else eid
            title = " ".join((e.findtext("a:title", default="", namespaces=NS) or "").split())
            if eid and title and title != "Error":
                out[eid] = title
        time.sleep(3)
    return out


def check_url(url: str) -> str | None:
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=30) as r:
                if r.status < 400:
                    return None
        except urllib.error.HTTPError as ex:
            if method == "GET":
                return f"HTTP {ex.code}"
        except Exception as ex:
            if method == "GET":
                return type(ex).__name__
    return "unreachable"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-links", action="store_true")
    args = ap.parse_args()
    entries, errs = load_curated()
    lines = ["## Curated data verification", ""]
    failures = list(errs)
    ids = [e["arxiv"] for e in entries if e.get("arxiv")]
    titles = arxiv_titles(ids)
    for e in entries:
        a = e.get("arxiv")
        if not a:
            continue
        got = titles.get(a)
        if not got:
            failures.append(f"arXiv {a} not found (curated: {e['title']!r})")
        elif norm_title(got) != norm_title(e["title"]):
            failures.append(f"arXiv {a} title mismatch: curated {e['title']!r} vs arXiv {got!r}")
    if not args.no_links:
        urls = sorted({e[k] for e in entries for k in ("url", "code", "project") if e.get(k)})
        for u in urls:
            problem = check_url(u)
            if problem:
                failures.append(f"link {u}: {problem}")
            time.sleep(0.3)
    lines.append(f"Checked {len(ids)} arXiv IDs and {len(entries)} entries.")
    lines.append("")
    lines += [f"- ❌ {f}" for f in failures] or ["- ✅ all good"]
    report = "\n".join(lines)
    print(report)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write(report + "\n")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
