#!/usr/bin/env python3
"""Check internal links in the built site: every relative href/src in _site/*.html
must point to a file, and a #fragment to an id on that page. Exit 1 on broken links."""
import collections
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "_site"
EXTERNAL = re.compile(r"(https?:|mailto:|data:|javascript:|//)")


def main() -> int:
    ids: dict[Path, set[str]] = {}

    def page_ids(p: Path) -> set[str]:
        if p not in ids:
            ids[p] = set(re.findall(r'\bid="([^"]+)"', p.read_text(errors="ignore")))
        return ids[p]

    broken: collections.Counter = collections.Counter()
    seen_on: dict[str, str] = {}
    pages = list(ROOT.rglob("*.html"))
    for page in pages:
        for ref in re.findall(r'(?:href|src)="([^"]+)"', page.read_text(errors="ignore")):
            ref = html.unescape(ref)
            if EXTERNAL.match(ref):
                continue
            path, _, frag = ref.split("?")[0].partition("#")
            if not path:
                target = page
            elif path.startswith("/"):
                target = ROOT / path.lstrip("/")
            else:
                target = (page.parent / path).resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.exists() or (frag and target.suffix == ".html" and frag not in page_ids(target)):
                broken[ref] += 1
                seen_on[ref] = str(page.relative_to(ROOT))
    for ref, n in broken.most_common(50):
        print(f"BROKEN {ref} ({n}x, e.g. on {seen_on[ref]})")
    print(f"{len(pages)} pages checked, {len(broken)} broken internal links")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
