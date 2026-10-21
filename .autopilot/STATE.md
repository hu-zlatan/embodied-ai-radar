# State

_Last updated: 2026-10-21 ~05:20 UTC, run 9._

## Status

v0.1 is live at https://hu-zlatan.github.io/embodied-ai-radar/ (Pages deploys succeed).
- Data: `data/topics.yaml` (12 topics incl. `perception`, `control`, `learning` + keyword rules), `data/resources.yaml` (related lists / courses / docs / communities → README section + site `resources.html`), `data/embodiments.yaml` (robot-type rules, computed at build time), `data/curated/<topic>.yaml` (176 entries, EN/ZH takeaways; 17 agent picks with `added:`; curated `venue:` shows as a badge), `data/arxiv/YYYY/MM-DD.json` (621 papers, 2026-10-12..20; 186 untagged).
- Intake: RSS → API backfill → **enrichment** (id_list API, 50/request) adds `comment`, project/code links from comments, `enriched: true`; `venue_of()` turns comments into venue badges (accepted only).
- Site: search + filters (topic, robot type, source, has code) with shareable URLs (`?q=&topic=&robot=&src=&code=1`), venue badges, per-topic Atom feeds `topics/<id>.xml`, OG image `assets/og.png`. Index ~300 KB; abstracts only for last 21 days.
- **GitHub stats**: `repo-stats.yml` (weekly Sun 06:37 UTC + on curated/resources changes + dispatch) runs `scripts/repo_stats.py` → `data/repo_stats.json` (stars, last push, archived; ~92 repos; failures keep old values). Site shows ★ counts on curated cards/search results, an 'archived' badge, and a home-page 'Most-starred open-source code' top-12 list. README does not show stars (would churn `build_readme --check`).
- **Feed code-link check** (run 9): `repo_stats.py` also checks code repos of feed papers from the last 30 days → `feed` section of `data/repo_stats.json` (`{stars}` or `{missing: true}`). 404 repos render as 'Code: not public yet' (no link, not counted as code, excluded from digest/filter); live ones show ★ (also in search, sortable). `repo-stats.yml` now also runs after every intake (workflow_run).
- **BibTeX** (run 7): every arXiv card (curated + feed) has a collapsed BibTeX block + copy button; `_site/curated.bib` bundles all curated papers; topics page links it. Built only from arXiv metadata: feed authors (capped 8 → 'and others'), curated authors cached in `data/arxiv/curated_meta.json` by intake (`fill_curated_meta`, only missing IDs). Feed page +21% gzipped.
- **Search sort** (run 7): best match / newest / GitHub stars, `?sort=new|stars`; sort alone lists everything.
- **Feed by day** (run 8): `feed.html` = newest day (code-first) + archive list; `feed/YYYY-MM-DD.html` per day with prev/next, summary (papers / with code / venues), in sitemap. All days kept (permalinks stay valid); each day page ~150–350 KB raw.
- Issue forms: `.github/ISSUE_TEMPLATE/` (suggest an entry / report a mistake, bilingual; contact links to site + Discussions). Footer link `/issues/new` opens the chooser.
- License: `LICENSE` = MIT (GitHub detects it), data terms in `LICENSE-DATA.md`.
- Verification: all curated arXiv IDs + links checked by `verify.yml` (since run 8: HTTP 4xx fails; network errors/5xx are retried once and shown as ⚠️ warnings, not failures) (run 2: 10 perception anchors passed). Re-check the latest verify run at the start of each run.
- Scripts: `validate.py`, `verify_curated.py` (CI; API → abs-page fallback), `intake_arxiv.py` (CI; RSS first, API fallback, `--retag`), `build_site.py`, `build_readme.py` (`--check` in CI), `make_digest.py`.
- Workflows: `repo-stats.yml` (above), `ci.yml`, `intake.yml` (daily 02:17 UTC + backup slots 07:43 and 15:29 UTC, since GitHub dropped the first scheduled run), `pages.yml` (push / after intake or digest / daily 03:40 UTC), `verify.yml` (curated changes + weekly Mon), `weekly.yml` (Mon 05:23 UTC + backup 13:11 UTC → `digest/YYYY-Www.md`, skips if it exists). intake + verify share concurrency group `arxiv-api` (a newer pending run cancels an older pending one — re-dispatch if needed).

## Known issues

- arXiv export API returns 429 to GitHub runners often; RSS covers the daily path. API backfill is best-effort.
- RSS dates = announcement date; API dates = first-submission date. Mixed but deduped by ID.
- ~31% of feed papers get no topic (control/MPC/safety, autonomous driving, multi-robot, aerial). Shown as untagged; robot-type filter covers driving/drones.
- Search index will grow to ~1.2 MB at 60 days even without old abstracts (gzip on Pages helps). Revisit if it passes ~1 MB.

## Next steps

0. `data/arxiv/curated_meta.json` is filled (157/157 curated arXiv IDs, run 7). New curated entries get metadata on the next intake run. Note: a push touching curated data queues verify.yml in the `arxiv-api` group and cancels a *pending* intake — dispatch intake only after verify has started.
1. Scheduled runs are unreliable: on 2026-10-21 the 02:17 intake had not fired by 04:50 (the 15:29 slot on 10-20 started at 19:24). Run 9 dispatched intake by hand. Check that scheduled runs now fire (intake 02:17 / 07:43 / 15:29 UTC, pages 03:40). If none fire again, note it in OWNER_TODO (repo may need a recent commit/activity; scheduled workflows run on the default branch only). verify.yml passed for all 9 run-5 entries; re-check the latest run each time.
2. Each run: review the newest feed (papers with code first), promote 2–5 notable ones into curated YAML with `added: <date>` and careful EN/ZH takeaways (phrase results as "reports").
3. Monday 2026-10-26: check the first auto digest (2026-W43); add a short human-quality intro paragraph if useful.
4. Owner: launch kit ready in `.autopilot/LAUNCH_KIT.md` (recommend posting after the first auto digest).
5. Enrichment step: 2026-10-20 dispatched intake finished in <1 min with 170 new papers (code links + venues present), no 429 trouble.

## Backlog

- More resources in `data/resources.yaml` as users suggest them (only well-known, verified links; Chinese courses/tutorials especially).
- Thin topics still: hardware (9), tactile (11), learning (10), perception (10).
- Feed split by day done in run 8. If the site gets large (many months of day pages), consider dropping abstracts from day pages older than ~90 days rather than deleting pages.
- Untagged feed (~31%): mostly aerial/marine/space, autonomous driving, formal control. Consider an `aerial-field` topic only if users ask; robot-type filter covers drones/driving/underwater.
- Site nav wraps to two lines on phones (6 links) — fine now, revisit if more links are added.
- Done in run 3: resources section/page, digest robot-type counts, `learning` topic.
- Done in run 4: 6 anchors from Chinese labs/companies (RoboTwin 2.0, CogACT, RoboBrain 2.0, DexGraspNet, RoboMIND, Unitree RL Gym), picks VLA-Δ + MambaAct, MimicGen, BEHAVIOR-1K, Hi Robot, issue forms. verify.yml passed for all.
- Done in run 5: anchors ViNT, VIMA, Dobb-E, Isaac Lab paper (2511.04831), AI2-THOR; picks Ropedia W0, CondenseVLA, MoDex, PrismPlan; tagging keywords (impedance control, behavior trees, rearrangement, lifelong learning, soft/continuum robots).
- Done in run 6: GitHub stars (repo-stats workflow, ★ on site, most-starred list); anchors GNM, Habitat 3.0, GR-3, Digit 360 (tactile), MuJoCo MPC + Pinocchio (control). verify.yml passed for all.
- Archived repos found by stats: digit-interface, tacto, sparsh (facebookresearch), robotics_transformer (RT-1). Shown with an 'archived' badge; consider noting maintained forks if users ask.
- Done in run 7: anchors robomimic, IQL, BeT, DPPO, ALOHA 2, Stretch, Taxim, Tactile Gym 2.0; BibTeX + curated.bib; search sort.
- Done in run 8: anchors SAM, SAM 2, Grounding DINO, FoundationStereo (perception), CQL, Decision Transformer (learning), Berkeley Humanoid Lite (hardware); picks SpaRV, HumanoidPose, CusADi2, CTR; feed split by day.
- Idea: stars in README (would need the stats workflow to regenerate README too).
- Candidate anchors still missing: GraspNet-1Billion (no arXiv; CVPR page), GelSight 2017 sensor paper (MDPI Sensors, no arXiv).
- Pick CTR (2610.26507): add its code link once github.com/MINT-SJTU/CTR is public.
