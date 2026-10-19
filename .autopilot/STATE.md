# State

_Last updated: 2026-10-19 ~11:20 UTC, run 2._

## Status

v0.1 is live at https://hu-zlatan.github.io/embodied-ai-radar/ (Pages deploys succeed).
- Data: `data/topics.yaml` (10 topics incl. `perception` + keyword rules), `data/embodiments.yaml` (robot-type rules, computed at build time), `data/curated/<topic>.yaml` (102 entries, EN/ZH takeaways; 7 agent picks with `added:`), `data/arxiv/YYYY/MM-DD.json` (451 papers, 2026-10-12..19; 180 untagged).
- Site: search + filters (topic, robot type `?robot=`, source, has code), per-topic Atom feeds `topics/<id>.xml`, OG image `assets/og.png`. Index ~300 KB; abstracts only for last 21 days.
- License: `LICENSE` = MIT (GitHub detects it), data terms in `LICENSE-DATA.md`.
- Verification: all curated arXiv IDs + links checked by `verify.yml` (run 2: 10 perception anchors passed). Re-check the latest verify run at the start of each run.
- Scripts: `validate.py`, `verify_curated.py` (CI; API → abs-page fallback), `intake_arxiv.py` (CI; RSS first, API fallback, `--retag`), `build_site.py`, `build_readme.py` (`--check` in CI), `make_digest.py`.
- Workflows: `ci.yml`, `intake.yml` (daily 02:17 UTC), `pages.yml` (push / after intake or digest / daily 03:40 UTC), `verify.yml` (curated changes + weekly Mon), `weekly.yml` (Mon 05:23 UTC → `digest/YYYY-Www.md`). intake + verify share concurrency group `arxiv-api` (a newer pending run cancels an older pending one — re-dispatch if needed).

## Known issues

- arXiv export API returns 429 to GitHub runners often; RSS covers the daily path. API backfill is best-effort.
- RSS dates = announcement date; API dates = first-submission date. Mixed but deduped by ID.
- ~40% of feed papers get no topic (control/MPC/safety, autonomous driving, multi-robot, aerial). Shown as untagged; robot-type filter covers driving/drones.
- RSS records have no arXiv comments, so venue badges can't be parsed on the daily path.
- Search index will grow to ~1.2 MB at 60 days even without old abstracts (gzip on Pages helps). Revisit if it passes ~1 MB.

## Next steps

1. Check the latest `verify.yml`, `intake.yml` (first scheduled run 2026-10-20 02:17 UTC) and `pages.yml` results; fix anything red.
2. Each run: review the newest feed (papers with code first), promote 2–5 notable ones into curated YAML with `added: <date>` and careful EN/ZH takeaways (phrase results as "reports").
3. Monday 2026-10-26: check the first auto digest (2026-W43); add a short human-quality intro paragraph if useful.
4. Owner: set repo description/topics (OWNER_TODO). Launch kit draft is ready in `.autopilot/LAUNCH_KIT.md`; recommend posting after the first digest.
5. Consider a 'Planning, Control & Safety' topic (MPC, CBF, safe RL, motion planning) — largest untagged cluster; needs verified anchors.

## Backlog

- Venue badges (CoRL/RSS/ICRA/IROS/NeurIPS): RSS has no comments; would need an API enrichment step (429-prone) — low priority.
- Chinese community resources section (courses, 中文教程) — only well-known, verified links.
- Open Graph preview image for link sharing.
- Deep links: shareable search URLs that reflect current filters (update `?q=&topic=&robot=` as you type).
- Weekly digest: add 'robot type' breakdown and the week's agent picks first.
