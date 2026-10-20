# State

_Last updated: 2026-10-20 ~05:10 UTC, run 5._

## Status

v0.1 is live at https://hu-zlatan.github.io/embodied-ai-radar/ (Pages deploys succeed).
- Data: `data/topics.yaml` (12 topics incl. `perception`, `control`, `learning` + keyword rules), `data/resources.yaml` (related lists / courses / docs / communities → README section + site `resources.html`), `data/embodiments.yaml` (robot-type rules, computed at build time), `data/curated/<topic>.yaml` (149 entries, EN/ZH takeaways; 17 agent picks with `added:`; curated `venue:` shows as a badge), `data/arxiv/YYYY/MM-DD.json` (621 papers, 2026-10-12..20; 186 untagged).
- Intake: RSS → API backfill → **enrichment** (id_list API, 50/request) adds `comment`, project/code links from comments, `enriched: true`; `venue_of()` turns comments into venue badges (accepted only).
- Site: search + filters (topic, robot type, source, has code) with shareable URLs (`?q=&topic=&robot=&src=&code=1`), venue badges, per-topic Atom feeds `topics/<id>.xml`, OG image `assets/og.png`. Index ~300 KB; abstracts only for last 21 days.
- Issue forms: `.github/ISSUE_TEMPLATE/` (suggest an entry / report a mistake, bilingual; contact links to site + Discussions). Footer link `/issues/new` opens the chooser.
- License: `LICENSE` = MIT (GitHub detects it), data terms in `LICENSE-DATA.md`.
- Verification: all curated arXiv IDs + links checked by `verify.yml` (run 2: 10 perception anchors passed). Re-check the latest verify run at the start of each run.
- Scripts: `validate.py`, `verify_curated.py` (CI; API → abs-page fallback), `intake_arxiv.py` (CI; RSS first, API fallback, `--retag`), `build_site.py`, `build_readme.py` (`--check` in CI), `make_digest.py`.
- Workflows: `ci.yml`, `intake.yml` (daily 02:17 UTC + backup slots 07:43 and 15:29 UTC, since GitHub dropped the first scheduled run), `pages.yml` (push / after intake or digest / daily 03:40 UTC), `verify.yml` (curated changes + weekly Mon), `weekly.yml` (Mon 05:23 UTC + backup 13:11 UTC → `digest/YYYY-Www.md`, skips if it exists). intake + verify share concurrency group `arxiv-api` (a newer pending run cancels an older pending one — re-dispatch if needed).

## Known issues

- arXiv export API returns 429 to GitHub runners often; RSS covers the daily path. API backfill is best-effort.
- RSS dates = announcement date; API dates = first-submission date. Mixed but deduped by ID.
- ~31% of feed papers get no topic (control/MPC/safety, autonomous driving, multi-robot, aerial). Shown as untagged; robot-type filter covers driving/drones.
- Search index will grow to ~1.2 MB at 60 days even without old abstracts (gzip on Pages helps). Revisit if it passes ~1 MB.

## Next steps

1. Check that scheduled runs now fire (intake 02:17 / 07:43 / 15:29 UTC, pages 03:40). If none fire again, note it in OWNER_TODO (repo may need a recent commit/activity; scheduled workflows run on the default branch only). verify.yml passed for all 9 run-5 entries; re-check the latest run each time.
2. Each run: review the newest feed (papers with code first), promote 2–5 notable ones into curated YAML with `added: <date>` and careful EN/ZH takeaways (phrase results as "reports").
3. Monday 2026-10-26: check the first auto digest (2026-W43); add a short human-quality intro paragraph if useful.
4. Owner: topic typo `robot-learnin`; launch kit ready in `.autopilot/LAUNCH_KIT.md` (recommend posting after the first auto digest).
5. Enrichment step: 2026-10-20 dispatched intake finished in <1 min with 170 new papers (code links + venues present), no 429 trouble.

## Backlog

- More resources in `data/resources.yaml` as users suggest them (only well-known, verified links; Chinese courses/tutorials especially).
- Thin topics still: hardware (7), control (9), tactile (8). Add anchors when solid ones come up.
- Untagged feed (~31%): mostly aerial/marine/space, autonomous driving, formal control. Consider an `aerial-field` topic only if users ask; robot-type filter covers drones/driving/underwater.
- Site nav wraps to two lines on phones (6 links) — fine now, revisit if more links are added.
- Done in run 3: resources section/page, digest robot-type counts, `learning` topic.
- Done in run 4: 6 anchors from Chinese labs/companies (RoboTwin 2.0, CogACT, RoboBrain 2.0, DexGraspNet, RoboMIND, Unitree RL Gym), picks VLA-Δ + MambaAct, MimicGen, BEHAVIOR-1K, Hi Robot, issue forms. verify.yml passed for all.
- Done in run 5: anchors ViNT, VIMA, Dobb-E, Isaac Lab paper (2511.04831), AI2-THOR; picks Ropedia W0, CondenseVLA, MoDex, PrismPlan; tagging keywords (impedance control, behavior trees, rearrangement, lifelong learning, soft/continuum robots).
- Candidate anchors still missing (verify IDs first): GR-3 (arXiv ID not confirmed yet), GraspNet-1Billion (no arXiv; CVPR page), GNM (general navigation model), Habitat 3.0.
