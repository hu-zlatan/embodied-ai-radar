"""One-off probe (runs in GitHub Actions): sample the embedded HTML of the CoRL accepted-papers page."""
import html
import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"}
out = []
for u in ["https://www.corl.org/program/accepted-papers", "https://www.corl.org/program/late-breaking-results", "https://www.corl.org/program/demos"]:
    t = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40).read().decode("utf-8", "replace")
    m = re.search(r'data-code="([^"]*)"', t)
    c = html.unescape(m.group(1)) if m else ""
    try:
        c2 = c.encode().decode("unicode_escape").encode("latin-1", "replace").decode("utf-8", "replace")
    except Exception:
        c2 = c
    out.append(f"## {u}: code {len(c)}\n{c[:1500]}\n--- mid\n{c[len(c)//2:len(c)//2+1800]}\n--- end\n{c[-700:]}")
    tags = sorted(set(re.findall(r"<(\w+)", c)))
    out.append(f"tags {tags}; openreview {c.count('openreview.net')}, oral {len(re.findall('oral', c, re.I))}, spotlight {len(re.findall('spotlight', c, re.I))}, award {len(re.findall('award|best paper', c, re.I))}")
open(".autopilot/corl_probe.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len(out))
