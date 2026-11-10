"""Tell IndexNow search engines (Bing, Yandex, Seznam, Naver) about new site pages.

IndexNow takes a URL list and checks ownership through a key file on
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

SITE = "https://embodied-ai-radar.com/"
HOST = "embodied-ai-radar.com"
# Same files as SITE; used to read the sitemap if the canonical host is unreachable.
FALLBACK = "https://hu-zlatan.github.io/embodied-ai-radar/"
ALWAYS = [SITE, SITE + "feed.html"]
SENT = ROOT / ".autopilot" / "indexnow_sent.json"
MAX_URLS = 10000  # IndexNow limit per request


def live_urls() -> list[str]:
    for base in (SITE, FALLBACK):
        try:
            with urllib.request.urlopen(base + "sitemap.xml", timeout=60) as r:
                return re.findall(r"<loc>([^<]+)</loc>", r.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"sitemap at {base} unreadable: {e}")
    return []


def key_file_status() -> str:
    try:
        with urllib.request.urlopen(f"{SITE}{INDEXNOW_KEY}.txt", timeout=30) as r:
            body = r.read().decode("utf-8", "replace").strip()
            return f"{r.status}, {'matches key' if body == INDEXNOW_KEY else 'WRONG CONTENT'}"
    except (urllib.error.URLError, TimeoutError) as e:
        return f"unreachable ({e})"


def main() -> int:
    sent = set(json.loads(SENT.read_text())) if SENT.exists() else set()
    urls = live_urls()
    if not urls:
        print("empty sitemap")
        return 1
    urls = [u for u in urls if u.startswith(SITE)]
    new = [u for u in urls if u not in sent]
    batch = list(dict.fromkeys(ALWAYS + new))[:MAX_URLS]
    body = json.dumps({"host": HOST, "key": INDEXNOW_KEY,
                       "keyLocation": f"{SITE}{INDEXNOW_KEY}.txt", "urlList": batch}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    print(f"key file {SITE}{INDEXNOW_KEY}.txt: {key_file_status()}")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            print(f"IndexNow answered {r.status} for {len(batch)} URLs ({len(new)} new)")
    except urllib.error.HTTPError as e:
        detail = e.read()[:300]
        print(f"IndexNow refused: {e.code} {detail!r}")
        if e.code == 403 and b"SiteVerificationNotCompleted" in detail:
            # New host: IndexNow checks the key file asynchronously. Nothing is
            # marked as sent, so the next daily run submits the same URLs again.
            print("::warning::IndexNow site verification still pending for "
                  f"{HOST}; will retry on the next run")
            return 0
        return 1
    SENT.write_text(json.dumps(sorted(sent | set(batch)), indent=0) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
