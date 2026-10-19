# State

_Last updated: 2026-10-19, run 1 (bootstrap)._

## Status

v0.1 shipped to `main`:
- Data: `data/topics.yaml` (9 topics + keyword rules), `data/curated/<topic>.yaml` (85 entries, EN/ZH takeaways), `data/arxiv/YYYY/MM-DD.json` (daily feed, written by CI).
- Scripts (Python 3.12 + PyYAML only): `validate.py` (offline schema), `verify_curated.py` (online: arXiv titles + links, CI only), `intake_arxiv.py` (CI only), `build_site.py` (→ `_site/`), `build_readme.py` (README lists between markers; `--check` in CI).
- Workflows: `ci.yml`, `intake.yml` (daily 02:17 UTC), `pages.yml` (on push, after intake, daily 03:40 UTC), `verify.yml` (on curated changes + weekly).
- Site: index with stats + instant search/filters, topic pages, feed page, digest pages, Atom feed, sitemap. EN/中文 toggle via CSS (`html.zh`).

## Watch

- Pages deploy only works after the owner sets Settings → Pages → Source = GitHub Actions (OWNER_TODO).
- Check `verify.yml` result for the 85 seed entries: fix or remove any arXiv title mismatches / dead links — never guess.
- Check the first intake run output (counts, tagging quality).

## Next steps

1. Fix whatever `verify.yml` flags.
2. First weekly digest `digest/2026-W43.md` once the feed has a week of data (generator script: `scripts/make_digest.py` that drafts from feed + curated highlights; agent writes the picks).
3. Agent review of feed papers: pick notable new papers each run and promote them into curated YAML with takeaways (verify via CI).
4. Re-take `docs/screenshot.png` once the feed has data.
5. Launch kit (`.autopilot/LAUNCH_KIT.md`) once the site is live and verified.

## Backlog

- Per-paper "has code" detection also via Papers with Code / HF papers links (in Actions).
- Topic-tagging quality: measure precision on a sample; add negative keywords.
- Feed archive pages by month (site currently indexes last 60 days for search).
- Filter by embodiment (arm / humanoid / quadruped / hand) using tags.
- Chinese-language community resources section (courses, 中文教程).
- Venue tags (CoRL/RSS/ICRA/IROS) from arXiv comments.
