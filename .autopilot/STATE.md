# State

_Last updated: 2026-10-19 ~11:10 UTC, end of run 2._

## Status

v0.1 is live at https://hu-zlatan.github.io/embodied-ai-radar/ (Pages deploys succeed).
- Data: `data/topics.yaml` (11 topics incl. `perception`, `control` + keyword rules), `data/embodiments.yaml` (robot-type rules, computed at build time), `data/curated/<topic>.yaml` (111 entries, EN/ZH takeaways; 10 agent picks with `added:`; curated `venue:` shows as a badge), `data/arxiv/YYYY/MM-DD.json` (451 papers, 2026-10-12..19; 162 untagged).
- Intake: RSS → API backfill → **enrichment** (id_list API, 50/request) adds `comment`, project/code links from comments, `enriched: true`; `venue_of()` turns comments into venue badges (accepted only).
- Site: search + filters (topic, robot type, source, has code) with shareable URLs (`?q=&topic=&robot=&src=&code=1`), venue badges, per-topic Atom feeds `topics/<id>.xml`, OG image `assets/og.png`. Index ~300 KB; abstracts only for last 21 days.
- License: `LICENSE` = MIT (GitHub detects it), data terms in `LICENSE-DATA.md`.
- Verification: all curated arXiv IDs + links checked by `verify.yml` (run 2: 10 perception anchors passed). Re-check the latest verify run at the start of each run.
- Scripts: `validate.py`, `verify_curated.py` (CI; API → abs-page fallback), `intake_arxiv.py` (CI; RSS first, API fallback, `--retag`), `build_site.py`, `build_readme.py` (`--check` in CI), `make_digest.py`.
- Workflows: `ci.yml`, `intake.yml` (daily 02:17 UTC), `pages.yml` (push / after intake or digest / daily 03:40 UTC), `verify.yml` (curated changes + weekly Mon), `weekly.yml` (Mon 05:23 UTC → `digest/YYYY-Www.md`). intake + verify share concurrency group `arxiv-api` (a newer pending run cancels an older pending one — re-dispatch if needed).

## Known issues

- arXiv export API returns 429 to GitHub runners often; RSS covers the daily path. API backfill is best-effort.
- RSS dates = announcement date; API dates = first-submission date. Mixed but deduped by ID.
- ~40% of feed papers get no topic (control/MPC/safety, autonomous driving, multi-robot, aerial). Shown as untagged; robot-type filter covers driving/drones.
- Search index will grow to ~1.2 MB at 60 days even without old abstracts (gzip on Pages helps). Revisit if it passes ~1 MB.

## Next steps

1. Check the latest `verify.yml`, `intake.yml` (first scheduled run 2026-10-20 02:17 UTC) and `pages.yml` results; fix anything red.
2. Each run: review the newest feed (papers with code first), promote 2–5 notable ones into curated YAML with `added: <date>` and careful EN/ZH takeaways (phrase results as "reports").
3. Monday 2026-10-26: check the first auto digest (2026-W43); add a short human-quality intro paragraph if useful.
4. Owner: set repo description/topics (OWNER_TODO). Launch kit draft is ready in `.autopilot/LAUNCH_KIT.md`; recommend posting after the first digest.
5. Enrichment worked on first try (451/451; project links 0→105, code 7→29, 36 venue badges). Watch tomorrow's scheduled intake log for 429s in the enrichment step.
6. Digests: `digest/2026-W42.md` written by hand-run (launch week). Next auto digest Mon 2026-10-26 includes an 'Accepted at venues' section.

## Backlog

- Chinese community resources section (courses, 中文教程) — only well-known, verified links.
- Open Graph preview image for link sharing.
- Weekly digest: robot-type breakdown.
- Chinese community resources section (only well-known, verified links).
- More curated anchors for thin topics (hardware: 3 feed hits/week; tactile).
