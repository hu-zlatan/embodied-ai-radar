"""Tell IndexNow search engines (Bing, Yandex, Seznam, Naver) about new site pages.

A project site lives under a path, so crawlers never see its robots.txt or sitemap
on their own. IndexNow takes a URL list and checks ownership through a key file on
the site. Only URLs not sent before go out, plus ALWAYS (pages that change daily).
Google does not use IndexNow; see OWNER_TODO.md.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_site import INDEXNOW_KEY  # noqa: E402

SITE = "https://hu-zlatan.github.io/embodied-ai-radar/"
ALWAYS = [SITE, SITE + "feed.html"]
SENT = ROOT / ".autopilot" / "indexnow_sent.json"
MAX_URLS = 10000  # IndexNow limit per request


def live_urls() -> list[str]:
    with urllib.request.urlopen(SITE + "sitemap.xml", timeout=60) as r:
        return re.findall(r"<loc>([^<]+)</loc>", r.read().decode("utf-8"))


def main() -> int:
    sent = set(json.loads(SENT.read_text())) if SENT.exists() else set()
    urls = live_urls()
    if not urls:
        print("empty sitemap")
        return 1
    new = [u for u in urls if u not in sent]
    batch = list(dict.fromkeys(ALWAYS + new))[:MAX_URLS]
    body = json.dumps({"host": "hu-zlatan.github.io", "key": INDEXNOW_KEY,
                       "keyLocation": f"{SITE}{INDEXNOW_KEY}.txt", "urlList": batch}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            print(f"IndexNow answered {r.status} for {len(batch)} URLs ({len(new)} new)")
    except urllib.error.HTTPError as e:
        print(f"IndexNow refused: {e.code} {e.read()[:200]!r}")
        return 1
    SENT.write_text(json.dumps(sorted(sent | set(batch)), indent=0) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
