"""One-off probe (runs in GitHub Actions): sample the embedded HTML of the CoRL accepted-papers page."""
import html
import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"}
t = urllib.request.urlopen(urllib.request.Request("https://www.corl.org/program/accepted-papers", headers=UA), timeout=40).read().decode("utf-8", "replace")
c = html.unescape(re.search(r'data-code="([^"]*)"', t).group(1))
try:
    c = c.encode().decode("unicode_escape").encode("latin-1", "replace").decode("utf-8", "replace")
except Exception:
    pass
c = c[c.index("<body"):c.index("<script")]
lines = re.sub(r"(<tr|<section|<h[123]|<div|<p|<li|</section)", r"\n\1", c).split("\n")
out, n = [], 0
for ln in lines:
    if ln.startswith('<tr class="paper"'):
        n += 1
        if n > 12 and n % 97:
            continue
    out.append(ln[:420])
open(".autopilot/corl_probe.txt", "w", encoding="utf-8").write(f"{len(lines)} lines, {n} paper rows\n" + "\n".join(out) + "\n")
