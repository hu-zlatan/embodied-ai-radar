# State

_Last updated: 2026-10-22 ~05:00 UTC, run 13._

## Status

v0.1 is live at https://hu-zlatan.github.io/embodied-ai-radar/ (Pages deploys succeed).
- Data: `data/topics.yaml` (12 topics incl. `perception`, `control`, `learning` + keyword rules), `data/resources.yaml` (related lists / courses / docs / communities → README section + site `resources.html`), `data/embodiments.yaml` (robot-type rules, computed at build time), `data/curated/<topic>.yaml` (242 entries, EN/ZH takeaways; 31 agent picks with `added:`; curated `venue:` shows as a badge), `data/arxiv/YYYY/MM-DD.json` (794 papers, 2026-10-12..22).
- Intake: RSS → API backfill → **enrichment** (id_list API, 50/request) adds `comment`, project/code links from comments, `enriched: true`; `venue_of()` turns comments into venue badges (accepted only).
- Site: search + filters (topic, robot type, source, has code) with shareable URLs (`?q=&topic=&robot=&src=&code=1`), venue badges, per-topic Atom feeds `topics/<id>.xml`, OG image `assets/og.png`. Index ~300 KB; abstracts only for last 21 days.
- **GitHub stats**: `repo-stats.yml` (weekly Sun 06:37 UTC + on curated/resources changes + dispatch) runs `scripts/repo_stats.py` → `data/repo_stats.json` (stars, last push, archived; ~92 repos; failures keep old values). Site shows ★ counts on curated cards/search results, an 'archived' badge, and a home-page 'Most-starred open-source code' top-12 list. README does not show stars (would churn `build_readme --check`).
- **Feed code-link check** (run 9): `repo_stats.py` also checks code repos of feed papers from the last 30 days → `feed` section of `data/repo_stats.json` (`{stars}` or `{missing: true}`). 404 repos render as 'Code: not public yet' (no link, not counted as code, excluded from digest/filter); live ones show ★ (also in search, sortable). `repo-stats.yml` now also runs after every intake (workflow_run).
- **BibTeX** (run 7): every arXiv card (curated + feed) has a collapsed BibTeX block + copy button; `_site/curated.bib` bundles all curated papers; topics page links it. Built only from arXiv metadata: feed authors (capped 8 → 'and others'), curated authors cached in `data/arxiv/curated_meta.json` by intake (`fill_curated_meta`, only missing IDs). Feed page +21% gzipped.
- **Venue filter** (run 10): search has an 'Any venue' select (venue series from curated `venue:` + feed badges, ≥2 items, with counts; '*' = any accepted venue), `?venue=CoRL`.
- **Search sort** (run 7): best match / newest / GitHub stars, `?sort=new|stars`; sort alone lists everything.
- **Feed by day** (run 8): `feed.html` = newest day (code-first) + archive list; `feed/YYYY-MM-DD.html` per day with prev/next, summary (papers / with code / venues), in sitemap. All days kept (permalinks stay valid); each day page ~150–350 KB raw.
- **Entry pages** (run 11): `e/<id>.html` for every curated entry (id = `arxiv-<id>` or title slug, stable): takeaway card with `<h1>`, links, ★, BibTeX, arXiv authors, 'More in <topic>', schema.org JSON-LD; in sitemap. Cards, search results and the most-starred list link to them ('Details / 详情').
- **Star history** (run 11): `repo_stats.py` appends one snapshot per day (45 days) to `data/repo_stars_history.json` (curated + recent feed repos; first snapshot 2026-10-21). Home page shows 'Rising this week' (top 10 by 7-day gain) and +N badges on the most-starred list once a snapshot ≥7 days older exists (from ~2026-10-28). Nothing shows before that.
- **Data export** (run 12): `_site/curated.json` + `curated.csv` (fields: id, title, type, arxiv, year, venue, org, url, code, project, topics, tags, robot_types, highlight, added, takeaways, github_stars, page). Keep field names stable; add new fields at the end.
- **Picks feed** (run 13): `_site/picks.xml` = Atom feed of the newest 60 agent picks (curated entries with `added:`), bilingual summary, links to entry pages. Linked from home ('Newly added picks') and both READMEs.
- Issue forms: `.github/ISSUE_TEMPLATE/` (suggest an entry / report a mistake, bilingual; contact links to site + Discussions). Footer link `/issues/new` opens the chooser.
- License: `LICENSE` = MIT (GitHub detects it), data terms in `LICENSE-DATA.md`.
- Verification: all curated arXiv IDs + links checked by `verify.yml` (since run 8: HTTP 4xx fails; network errors/5xx are retried once and shown as ⚠️ warnings, not failures) (run 2: 10 perception anchors passed). Re-check the latest verify run at the start of each run.
- Scripts: `validate.py`, `verify_curated.py` (CI; API → abs-page fallback), `intake_arxiv.py` (CI; RSS first, API fallback, `--retag`), `build_site.py`, `build_readme.py` (`--check` in CI), `make_digest.py`.
- Workflows: `repo-stats.yml` (above), `ci.yml`, `intake.yml` (daily 02:17 UTC + backup slots 01:11, 04:53, 07:43, 11:07, 15:29 UTC — run 13 added three because the 02:17 slot has never fired on time), `pages.yml` (push / after intake or digest / daily 03:40 UTC), `verify.yml` (curated changes + weekly Mon), `weekly.yml` (Mon 05:23 UTC + backup 13:11 UTC → `digest/YYYY-Www.md`, skips if it exists). intake + verify share concurrency group `arxiv-api` (a newer pending run cancels an older pending one — re-dispatch if needed).

## Known issues

- arXiv export API returns 429 to GitHub runners often; RSS covers the daily path. API backfill is best-effort.
- RSS dates = announcement date; API dates = first-submission date. Mixed but deduped by ID.
- ~31% of feed papers get no topic (control/MPC/safety, autonomous driving, multi-robot, aerial). Shown as untagged; robot-type filter covers driving/drones.
- Search index will grow to ~1.2 MB at 60 days even without old abstracts (gzip on Pages helps). Revisit if it passes ~1 MB.

## Next steps

0. New curated entries get BibTeX metadata on the next intake run. A push touching curated data queues verify.yml in the `arxiv-api` group and cancels a *pending* intake — dispatch intake only after verify has started/finished.
1. Scheduled runs: the 02:17 intake slot has not fired on time on any day (10-20, 10-21, 10-22 — nothing by 04:50); other slots land hours late (07:43 → ~13:11, 15:29 → ~19:23). Run 13 added slots 01:11, 04:53, 11:07. Check on 10-23 whether any early slot fired (list runs with event=schedule). If the feed still only lands around noon UTC, consider an OWNER_TODO note (nothing the owner can really fix; GitHub cron is best-effort).
2. Run 14+: review the newest feed (papers with code first), promote 2–5 notable ones with `added: <date>` and careful EN/ZH takeaways (≤220 chars EN; phrase results as "reports"). 10-22 feed reviewed in run 13.
3. Monday 2026-10-26: check the first auto digest (2026-W43); add a short human-quality intro paragraph if useful.
3b. From ~2026-10-28: check 'Rising this week' renders with real data (needs 7 days of `data/repo_stars_history.json`); consider adding it to the weekly digest (`make_digest.py`).
4. Owner: launch kit ready in `.autopilot/LAUNCH_KIT.md` (recommend posting after the first auto digest).

## Backlog

- More resources in `data/resources.yaml` as users suggest them (only well-known, verified links; Chinese courses/tutorials especially).
- Thin topics still: learning (18), hardware (18), sim (19). Run 13: control 17 → 20 (VAMP, RMP, HJ reachability), perception 17 → 20 (DINOv2, CoTracker, MASt3R). Run 12: tactile 14 → 19, navigation → 22, locomotion → 20, datasets → 21. Run 11 added hardware (13 → 18), VLA, navigation, dataset anchors. Run 10 added world-models (→17), learning, locomotion anchors. Run 9 added navigation (VLFM, NaVid, Uni-NaVid, Nav2) and tactile (GelSlim 3.0, DTact, 9DTact) anchors.
- Feed split by day done in run 8. If the site gets large (many months of day pages), consider dropping abstracts from day pages older than ~90 days rather than deleting pages.
- Untagged feed (~31%): mostly aerial/marine/space, autonomous driving, formal control. Consider an `aerial-field` topic only if users ask; robot-type filter covers drones/driving/underwater.
- Site nav wraps to two lines on phones (6 links) — fine now, revisit if more links are added.
- Done in run 3: resources section/page, digest robot-type counts, `learning` topic.
- Done in run 4: 6 anchors from Chinese labs/companies (RoboTwin 2.0, CogACT, RoboBrain 2.0, DexGraspNet, RoboMIND, Unitree RL Gym), picks VLA-Δ + MambaAct, MimicGen, BEHAVIOR-1K, Hi Robot, issue forms. verify.yml passed for all.
- Done in run 5: anchors ViNT, VIMA, Dobb-E, Isaac Lab paper (2511.04831), AI2-THOR; picks Ropedia W0, CondenseVLA, MoDex, PrismPlan; tagging keywords (impedance control, behavior trees, rearrangement, lifelong learning, soft/continuum robots).
- Done in run 6: GitHub stars (repo-stats workflow, ★ on site, most-starred list); anchors GNM, Habitat 3.0, GR-3, Digit 360 (tactile), MuJoCo MPC + Pinocchio (control). verify.yml passed for all.
- Archived repos found by stats: digit-interface, tacto, sparsh (facebookresearch), robotics_transformer (RT-1). Shown with an 'archived' badge; consider noting maintained forks if users ask.
- Done in run 7: anchors robomimic, IQL, BeT, DPPO, ALOHA 2, Stretch, Taxim, Tactile Gym 2.0; BibTeX + curated.bib; search sort.
- Done in run 10: anchors PlaNet, DreamerV2, IRIS, UniPi, TD-MPC, TD3, GAIL, IBC, AWAC, AnyTeleop, perceptive ANYmal, OmniH2O, HOVER; venue filter; resources EasyRL, Hands-on RL, awesome-embodied-vla-va-vln.
- Done in run 9: feed code-link check (404 → 'not public yet', ★ for feed repos); picks SuperMimic, RoboCasa-Shift, Orin depth benchmark, video world models survey; navigation + tactile anchors.
- Done in run 8: anchors SAM, SAM 2, Grounding DINO, FoundationStereo (perception), CQL, Decision Transformer (learning), Berkeley Humanoid Lite (hardware); picks SpaRV, HumanoidPose, CusADi2, CTR; feed split by day.
- Idea: stars in README (would need the stats workflow to regenerate README too).
- Candidate anchors still missing: GraspNet-1Billion (no arXiv; CVPR page), GelSight 2017 sensor paper (MDPI Sensors, no arXiv).
- Pick CTR (2610.26507): add its code link once github.com/MINT-SJTU/CTR is public.
