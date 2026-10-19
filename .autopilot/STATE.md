# State

_Last updated: 2026-10-19 ~07:40 UTC, end of run 1 (bootstrap)._

## Status

v0.1 is live at https://hu-zlatan.github.io/embodied-ai-radar/ (Pages deploys succeed).
- Data: `data/topics.yaml` (9 topics + keyword rules), `data/curated/<topic>.yaml` (89 entries, EN/ZH takeaways; 4 are agent picks from the feed with `added:`), `data/arxiv/YYYY/MM-DD.json` (451 papers from the first intake, 2026-10-12..19).
- Verification: all 85 seed arXiv IDs + all links checked by `verify.yml`; one wrong ID (Berkeley Humanoid) fixed. Re-check the latest verify run at the start of next run.
- Scripts: `validate.py`, `verify_curated.py` (CI; API → abs-page fallback), `intake_arxiv.py` (CI; RSS first, API fallback, `--retag`), `build_site.py`, `build_readme.py` (`--check` in CI), `make_digest.py`.
- Workflows: `ci.yml`, `intake.yml` (daily 02:17 UTC), `pages.yml` (push / after intake or digest / daily 03:40 UTC), `verify.yml` (curated changes + weekly Mon), `weekly.yml` (Mon 05:23 UTC → `digest/YYYY-Www.md`). intake + verify share concurrency group `arxiv-api` (a newer pending run cancels an older pending one — re-dispatch if needed).

## Known issues

- arXiv export API returns 429 to GitHub runners often; RSS covers the daily path. API backfill is best-effort.
- RSS dates = announcement date; API dates = first-submission date. Mixed but deduped by ID.
- ~45% of feed papers get no topic (SLAM/odometry, aerial, control, multi-robot). Shown as untagged.
- Search index (`_site/data/index.json`) is ~300 KB for one week; will grow to ~2–3 MB at 60 days → shrink or split before then.

## Next steps

1. Check the latest `verify.yml`, `intake.yml` (first scheduled run 2026-10-20 02:17 UTC) and `pages.yml` results; fix anything red.
2. Each run: review the newest feed (papers with code first), promote 2–5 notable ones into curated YAML with `added: <date>` and careful EN/ZH takeaways (phrase results as "reports").
3. Monday 2026-10-26: check the first auto digest (2026-W43); add a short human-quality intro paragraph if useful.
4. Owner: set repo description/topics (OWNER_TODO). Launch kit draft is ready in `.autopilot/LAUNCH_KIT.md`; recommend posting after the first digest.
5. Index size: split the feed index by month or drop abstracts from `index.json`.

## Backlog

- New topic "Perception, SLAM & Mapping" (large untagged share) — needs a few curated anchors (e.g. ORB-SLAM3, LIO-SAM) verified by CI.
- Embodiment filter (arm / humanoid / quadruped / hand / drone) via tags + keyword rules.
- Venue badges (CoRL/RSS/ICRA/IROS/NeurIPS) parsed from arXiv comments.
- Per-topic Atom feeds.
- Chinese community resources section (courses, 中文教程) — only well-known, verified links.
- Open Graph preview image for link sharing.
