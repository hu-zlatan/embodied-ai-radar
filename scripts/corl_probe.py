"""One-off probe (runs in GitHub Actions): how is the CoRL 2026 accepted-papers list embedded?
Writes .autopilot/corl_probe.txt with page size, iframe/embed URLs and short samples."""
import html
import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"}
URLS = ["https://www.corl.org/program/accepted-papers", "https://www.corl.org/program/late-breaking-results", "https://www.corl.org/program/demos"]


def get(u: str) -> str:
    with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40) as r:
        return r.read().decode("utf-8", "replace")


out = []
for u in URLS:
    try:
        t = get(u)
    except Exception as ex:
        out.append(f"## {u}: FAILED {ex}")
        continue
    out.append(f"## {u}: {len(t)} chars")
    for pat in (r'<iframe[^>]{0,600}', r'data-url="[^"]{0,300}', r'https://docs\.google\.com/[^"\'\\ ]{0,200}', r'https://[^"\'\\ ]*(?:openreview|arxiv|airtable|notion|github\.io|pdf)[^"\'\\ ]{0,120}'):
        found = sorted(set(re.findall(pat, t)))
        out.append(f"-- {pat}: {len(found)}")
        out += [x[:500] for x in found[:15]]
    i = t.find("data-code")
    out.append(f"-- data-code at {i}; count {t.count('data-code')}")
    text = re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[\s\S]*?</\1>", " ", t))
    text = re.sub(r"\s+", " ", html.unescape(text))
    out.append(f"-- visible text {len(text)} chars: {text[:1500]}")
open(".autopilot/corl_probe.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out)[:4000])
