# Run log

Newest entries at the bottom. One entry per run: date and time (UTC), what shipped, what's next, any problems.

## 2026-10-19 — setup

- Repository created by the owner. Charter (`AUTOPILOT.md`) and `.autopilot/` files added during setup.
- Schedule: one agent run every 6 hours (around 00:00, 06:00, 12:00 and 18:00 Asia/Shanghai).

## 2026-10-19 — run 1 (bootstrap)

- Surveyed existing lists/trackers; positioning written in DECISIONS.md.
- Shipped v0.1: 85 curated entries in 9 topics (EN/ZH), static site generator with search, README generator, daily arXiv intake, Pages deploy, CI and verification workflows. Workflows pushed fine (no fallback needed).
- Triggered the first intake with a 7-day backfill.
- Problem: WebFetch can't open constructed URLs and the shell can't reach arXiv/GitHub, so curated data is verified by the `verify.yml` workflow instead.
- First intake attempt failed: arXiv API 429 from GitHub runners (verify hit the same). Fixes: shared `arxiv_get()` backoff, shared concurrency group, RSS-first intake (rss.arxiv.org), abs-page fallback for verify. Second intake succeeded: 453 papers (2026-10-12..19).
- Tagging v2: scored keywords (title 3 / abstract 1 / threshold 2) + relevance filter for cross-lists (dropped 2 off-topic papers, e.g. face-manipulation deepfakes). Retagged stored feed.
- Verify flagged 1 wrong arXiv ID (Berkeley Humanoid 2407.18276 → 2407.21781, confirmed by web search); all other 84 IDs and all links passed.
- Agent picks: REKI, LTM, frontier-VLM-as-policy (RoboMME), Cracking Mobile Manipulation → curated with `added: 2026-10-19`; home page shows "Newly added picks".
- Wrote `.autopilot/LAUNCH_KIT.md` (draft). Pages deploys succeed, so the Pages source is already set. Repo: 0 stars, 0 forks, no description/topics yet.

## 2026-10-19 — run 2 (~10:50–11:20 UTC)

- All workflows green at start (CI, Pages, verify). No issues or PRs. Repo: 0 stars, 0 forks; description/topics still unset (owner to-do).
- LICENSE split: plain MIT in `LICENSE` so GitHub shows "MIT"; CC BY 4.0 data terms in `LICENSE-DATA.md`.
- New topic **Perception, SLAM & 3D Mapping** with 10 anchors (ORB-SLAM3, LIO-SAM, FAST-LIO2, DROID-SLAM, MonoGS, DUSt3R, VGGT, FoundationPose, Depth Anything, ConceptGraphs) — verify.yml passed. World-models keywords now catch "world action model". Untagged feed 204 → 180 / 451.
- **Robot-type filter** (arm, hand, humanoid, legged, mobile, drone, driving, underwater) + chips; search index drops abstracts older than 21 days.
- OG/Twitter preview image, refreshed README screenshot, per-topic Atom feeds.
- Agent picks: Blind Precise Assembly (MIT), FastVLA, Embodied Skill Bench.
- Verified the new UI headless (filters, language toggle, mobile layout; no JS errors).
- Later in run 2: new topic **Planning, Control & Safety** (cuRobo, MPiNets, Diffuser, CBF tutorial, safe-learning survey, safe-control-gym; verify passed) → untagged 162/451. Shareable search URLs. Intake enrichment with arXiv comments → project links + conservative venue badges; dispatched intake (days=1) to test it.
- End of run 2: enrichment run succeeded (all 451 papers; 105 with project pages, 29 with code, 36 accepted-venue badges, mostly CoRL 2026); fixed venue edge cases ('Submiited', '(CoRL) 2026'). Venue search ('corl 2026'), project links in search results, curated venue badges, topic-page robot quick links. First digest 2026-W42 (with 'Accepted at venues'). Picks: WACL, HiRe-MoMa, MetaGenSim (CoRL 2026). Launch kit updated. Repo still 0 stars / 0 forks.

## 2026-10-19 — run 3 (~16:50–17:15 UTC)

- Start: all workflows green, no issues/PRs, 0 stars / 0 forks. Owner has set the repo description, website and topics (thanks!) — one topic is misspelled (`robot-learnin`), noted in OWNER_TODO.
- Thin-topic anchors (verify passed): ToddlerBot, BEHAVIOR Robot Suite (hardware); ReSkin, Touch and Go (tactile); Dreamer, TD-MPC2, DINO-WM (world models); Crocoddyl, acados (control).
- **Related lists & learning resources** (`data/resources.yaml`): 4 lists (incl. 中文 Embodied-AI-Guide), 3 courses, 3 tool docs, 古月居 — in both READMEs and a new site page `resources.html` (nav: Learn / 资源). verify.yml now checks these links too (passed).
- Agent picks: NestedVLA (NeurIPS 2026), HexaShell (VLM coding agent driving a bimanual robot), sub-millisecond ROS 2 reflex engine (pHRI).
- Weekly digest gains a **By robot type** section (starts with W43; W42 left as hand-edited).
- New topic **Robot Learning: RL & Imitation** (`learning`) with PPO, SAC, DAgger, RLPD, SERL, HIL-SERL; retagged feed: untagged 162 → 142, 66 papers tagged `learning`.
- All verify.yml runs this run passed (every new arXiv ID, code link and resource link checked). CI and Pages green.

## 2026-10-19 — run 4 (~22:50–23:10 UTC)

- Start: all workflows green, no issues/PRs, 0 stars / 0 forks. Owner set more topics (now incl. `wam`, `awesome-lists`, `paper-lists`); `robot-learnin` typo still there.
- Anchors for the Chinese audience (widely used open work from Chinese labs/companies): RoboTwin 2.0 (sim), CogACT + RoboBrain 2.0 (vla), DexGraspNet (manipulation), RoboMIND (datasets), Unitree RL Gym (locomotion). arXiv IDs confirmed by web search; verify.yml checks IDs and code links.
- Agent picks: VLA-Δ (ZJU, state-transition supervision), MambaAct (Mamba action expert for π0.5).
- Bilingual issue forms (suggest / fix) + contact links (site, Discussions).
- Also: MimicGen, BEHAVIOR-1K (sim) and Hi Robot (vla) anchors. All verify.yml runs passed (every new arXiv ID/title and code link checked); CI + Pages green. Curated: 140 entries. End of run 4.

## 2026-10-20 — run 5 (~04:50–05:15 UTC)

- Start: CI/Pages/verify green, no issues/PRs, 0 stars / 0 forks. Problem: the first scheduled intake (02:17 UTC) never fired. Dispatched it by hand (170 new papers for 2026-10-20, enrichment fine) and added backup cron slots to intake (07:43, 15:29 UTC) and weekly digest (Mon 13:11 UTC); both jobs are idempotent.
- Anchors (IDs confirmed by web search): ViNT (navigation, CoRL 2023), VIMA (vla, ICML 2023), Dobb-E / On Bringing Robots Home (manipulation), Isaac Lab paper 2511.04831 + AI2-THOR (sim).
- Agent picks 2026-10-20: Ropedia W0 (cross-embodiment loco-manipulation world model), CondenseVLA (NeurIPS 2026), MoDex (CoRL 2026), PrismPlan (GPU motion-planning substrate).
- Tagging: new keywords for control/learning/manipulation/hardware; retag moved 17 papers, untagged 199 → 186 of 621.
- verify.yml passed for all 9 new entries (IDs, titles, code links). CI + Pages green. Repo still 0 stars / 0 forks. End of run 5.

## 2026-10-20 — run 6 (~10:50–11:05 UTC)

- Start: no issues/PRs, 0 stars / 0 forks. Scheduled workflows now fire (intake 07:43 slot ran, no new papers since arXiv's next announcement is tonight; pages schedule ran). All green.
- **GitHub stars**: new `repo-stats.yml` + `scripts/repo_stats.py` fetch stars / last push / archived for every curated GitHub repo (GITHUB_TOKEN; first run: 91 repos, all real API values). Site shows ★ counts on cards and in search, an 'archived' badge (4 repos archived), and a home-page 'Most-starred open-source code' list. Workflow push was accepted (no fallback needed).
- Anchors: GNM (navigation, ICRA 2023), Habitat 3.0 (sim, ICLR 2024), GR-3 (vla, ByteDance Seed); IDs confirmed by web search, GR-3 takeaway checked against the abstract.
- Problem caught locally: an unquoted colon in a YAML takeaway broke vla.yaml; `| tail` hid validate's exit code. Fixed before pushing; now using `set -o pipefail` for check chains.
- Thin-topic anchors: Digit 360 (tactile/hardware, 2411.02479), MuJoCo MPC predictive sampling (2212.00541) and Pinocchio (control). verify.yml passed for all 6 new entries this run; CI + Pages green. Curated: 155. Repo still 0 stars / 0 forks. End of run 6.

## 2026-10-20 — run 7 (~16:50–17:15 UTC)

- Start: all workflows green, no issues/PRs, 0 stars / 0 forks. Owner fixed the `robot-learnin` topic typo (ticked in OWNER_TODO). No new arXiv papers since run 5 (next announcement ~00:00 UTC).
- Anchors (IDs confirmed by web search; verify.yml passed incl. code links): robomimic, IQL, Behavior Transformers, DPPO (learning); ALOHA 2, Stretch (hardware).
- **BibTeX**: collapsed BibTeX + copy button on every arXiv card, `curated.bib` download; curated authors cached by intake in `data/arxiv/curated_meta.json`. Dispatched intake to fill the cache. Tested headless (copy works, no JS errors, 390px OK).
- **Search sort**: best match / newest / GitHub stars, shareable `?sort=`.
- README (EN/ZH): new 'Citable' bullet.
- Tactile anchors Taxim + Tactile Gym 2.0 (verify passed). Dispatched intake (first dispatch was cancelled by a newer pending verify in the shared concurrency group; re-dispatched after verify started): curated_meta.json now covers all 157 curated arXiv papers; curated.bib has 157 entries, unique keys. Curated: 163. CI/verify/Pages green. Repo: 0 stars / 0 forks. End of run 7.

## 2026-10-20 — run 8 (~22:50 UTC–)

- Start: all workflows green (scheduled intake 15:29 slot ran, no new papers), no issues/PRs, 0 stars / 0 forks.
- Anchors (IDs/titles confirmed by web search; verify.yml passed): Segment Anything, SAM 2, Grounding DINO, FoundationStereo (perception 10 → 16 with picks), CQL, Decision Transformer (learning), Berkeley Humanoid Lite (hardware, RSS 2025).
- Agent picks from 2026-10-20 feed (all with code): SpaRV (HKU MaRS), HumanoidPose (ETH), CusADi2, CTR (SJTU bimanual IL). Takeaways from the stored (truncated) abstracts, kept to what they state; WebFetch of arxiv.org/abs pages needs approval in unattended runs.
- **Feed split by day**: feed.html 1.27 MB → 0.35 MB; per-day permalink pages with prev/next and a summary line; tested headless at 390 px (no JS errors, no horizontal scroll).
- Push was rejected once because the repo-stats bot had pushed; `git pull --rebase` then push (always pull before push).
- Hardware anchors ORCA hand (ETH) and HOMIE (Shanghai AI Lab/CUHK, RSS 2025); checked against the arXiv HTML pages.
- verify.yml caught a 404 code link on the CTR pick (repo not public yet) → removed. A second failure came from a temporary MIT course-site outage → verify now retries network/5xx errors once and reports them as warnings; 4xx still fails. Final verify run passed for all 176 entries.
- End: CI/Pages green, curated 176, repo 0 stars / 0 forks, no issues/PRs. Nothing new for the owner. End of run 8.

## 2026-10-21 — run 9 (~04:50 UTC–)

- Start: CI/Pages/verify green, no issues/PRs, 0 stars / 0 forks. Scheduled 02:17 intake had not fired (GitHub cron delays); dispatched intake by hand → 91 papers for 2026-10-21.
- **Feed code-link check**: repo_stats.py now also checks the code repos linked from feed papers (last 30 days) and runs after every intake. First CI run: 41 feed repos, 2 not public yet (MINT-SJTU/CTR, yjang43/lp2) → shown as 'Code: not public yet' instead of a broken link; others get ★. Workflow change pushed fine.
- Agent picks 2026-10-21: SuperMimic (CoRL 2026 oral, humanoid tracking + differentiable world model), RoboCasa-Shift (VLA robustness benchmark), Jetson AGX Orin depth benchmark (perception), Robotic Video World Models survey (Princeton, with paper list). Takeaways only state what the (truncated) abstracts say.
- Navigation anchors VLFM (ICRA 2024), NaVid (RSS 2024), Uni-NaVid (RSS 2025), Nav2 / Marathon 2 (IROS 2020); tactile anchors GelSlim 3.0, DTact, 9DTact. IDs/repos confirmed by web + GitHub search. Dispatched intake after verify started → curated_meta.json now 178 entries (BibTeX for the new picks).
- verify.yml passed for all 11 new entries (picks, navigation, tactile). Curated: 187. CI/Pages green. Repo 0 stars / 0 forks, no issues/PRs. Nothing new for the owner. End of run 9.

## 2026-10-21 — run 10 (~10:50 UTC–)

- Start: CI/Pages/verify green, no issues/PRs, 0 stars / 0 forks. Scheduled 07:43 intake fired on time (no new papers; next arXiv announcement ~00:00 UTC). No picks this run (run 9 already reviewed the 10-21 feed).
- Thin-topic anchors (IDs/titles confirmed by web search): PlaNet, DreamerV2, IRIS, UniPi, TD-MPC (world models 12 → 17); TD3, GAIL, Implicit BC, AWAC (learning 12 → 16); AnyTeleop (hardware 12 → 13). Curated: 197.
- **Search venue filter**: new 'Any venue' select (CoRL, NeurIPS, IROS, ICLR, RSS… with counts, plus 'Any accepted venue'); matches the venue series of curated `venue:` and feed venue badges; shareable `?venue=CoRL`. Tested headless at 390 px (40 CoRL results, no JS errors, no horizontal scroll). READMEs mention it.
- Resources: 蘑菇书 EasyRL (Datawhale) and 动手学强化学习 (Hands-on RL) as Chinese RL courses; awesome-embodied-vla-va-vln list. Repos confirmed via GitHub search.
- Locomotion anchors: perceptive ANYmal (2201.08117, Science Robotics), OmniH2O (CoRL 2024), HOVER (ICRA 2025). Control anchors: OSQP (paper), OMPL, MoveIt 2, Drake (code; repos confirmed via GitHub search). Curated: 204.
- verify.yml passed for every push this run (#37–#40: all new IDs, titles, code and resource links). Dispatched intake after verify finished to fill BibTeX metadata for the new anchors.
- End: CI/Pages/verify green, repo 0 stars / 0 forks, no issues/PRs. Nothing new for the owner (launch kit still waiting). End of run 10.

## 2026-10-21 — run 11 (~16:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. The 07:43 intake slot fired late (13:11 UTC), no new papers (next arXiv announcement ~00:00 UTC), so no picks this run.
- **Entry permalink pages** `e/<id>.html` for all curated entries: bilingual takeaway as `<h1>` card, links, ★, BibTeX, arXiv authors, 'More in <topic>' (8 related), schema.org JSON-LD; in sitemap. Cards and search results get a 'Details / 详情' link. Why: shareable links per paper and search-engine landing pages (e.g. Chinese queries for a paper name) — the site had only list pages. Tested headless at 390 px (no JS errors, no horizontal scroll, search → details link works); internal link check: 0 broken.
- Hardware anchors (checked on arXiv HTML pages + GitHub search): AirExo (ICRA 2024), AirExo-2 (CoRL 2025), Bunny-VisionPro, TeleMoMa, Solo / Open Dynamic Robot Initiative. Hardware 13 → 18.
- **Star history**: `repo_stats.py` now writes a daily snapshot to `data/repo_stars_history.json` (first one committed by the bot 2026-10-21, ~150 repos); home page 'Rising this week' + '+N' badges appear once 7 days exist. Tested with throw-away fake history locally (not committed). Workflow change pushed fine.
- **Mobile header fix**: nav was squeezed into a 4-line column beside the brand on phones (`flex:1` made the basis 0); now one row under the brand (header 74 px at 390/320 px).
- Anchors (IDs checked on arXiv, affiliations from arXiv HTML, repos via GitHub search): UniVLA, SpatialVLA (vla, RSS 2025), NaVILA (navigation, RSS 2025), VLN-CE (ECCV 2020), HM3D (datasets, NeurIPS 2021). Curated: 214.
- Digest picks now link to their entry pages; launch kit (V2EX) mentions BibTeX, entry pages, stars.
- verify.yml passed for both anchor pushes (#41, #42). Dispatched intake after verify to fill BibTeX metadata for the new anchors.
- End: CI/verify green, 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting). End of run 11.

## 2026-10-21 — run 12 (~22:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. Scheduled 15:29 intake slot fired at 19:23 (no new papers; next arXiv announcement ~00:00 UTC).
- Tactile anchors (thinnest topic, 14 → 19): Making Sense of Vision and Touch (ICRA 2019), See Hear Feel (CoRL 2022), TVL (ICML 2024), RotateIt (CoRL 2023), TacSL (NVIDIA). IDs/venues via web search, repos via GitHub search.
- **Data export**: site now publishes `curated.json` + `curated.csv` (stable fields incl. robot types and ★, CC BY 4.0; CSV with BOM for Excel). Linked from topics page and both READMEs ('Reusable').
- Anchors: LM-Nav, SemExp, Active Neural SLAM (navigation 19 → 22), QT-Opt, DrQ-v2 (learning 16 → 18; DrQ-v2 repo is archived → badge). Curated: 224.
- Locomotion anchors: Walk These Ways (CoRL 2022), DreamWaQ (ICRA 2023), ANYmal Parkour (Science Robotics), Humanoid Parkour Learning (CoRL 2024) → 20. Dataset anchors: RoboNet, Ego-Exo4D, Objaverse, ScanNet → 21. Curated: 232.
- verify.yml: run #43 (tactile) passed; #44 was cancelled by the newer pending run (shared concurrency group), #45/#46 re-check everything.
- No feed picks this run: the next arXiv announcement is ~00:00 UTC and the next scheduled intake 02:17 UTC; run 13 should review the 10-22 feed.
- verify.yml #45 and #46 passed (all 232 entries incl. the 18 new ones). CI/Pages green. BibTeX metadata for new anchors will be filled by the next scheduled intake (02:17 UTC). Repo 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting). End of run 12.

## 2026-10-22 — run 13 (~04:50 UTC–)

- Start: CI/Pages/verify green, no issues/PRs, 0 stars / 0 forks. The scheduled 02:17 intake had again not fired by 04:50 (third day in a row) → dispatched by hand (82 papers for 10-22). Added intake cron slots 01:11, 04:53, 11:07 UTC (pushed fine).
- Agent picks 2026-10-22: HyperDrone (CoRL 2026, GPU quadrotor sim), Watch Your Step (humanoid foothold-aware perception), Post-hoc epistemic uncertainty for VLAs (code), CW-WAM (contact-wrench world action model). Takeaways only from the (truncated) abstracts.
- Anchors: control VAMP (ICRA 2024, confirmed on Kavraki Lab page), Riemannian Motion Policies, HJ reachability overview; perception DINOv2 (TMLR), CoTracker, MASt3R (ECCV 2024). Repos via GitHub search. Curated: 242.
- **picks.xml**: low-volume Atom feed of agent picks (bilingual, links to entry pages), linked from home + READMEs. Why: the daily feed is 80–170 papers/day; many readers only want the reviewed few.
- Sim anchors: Brax (NeurIPS 2021 D&B), Habitat 2.0 (NeurIPS 2021), Humanoid-Gym (RobotEra), Gazebo. Curated: 246.
- verify.yml #47, #48, #49 passed (all new picks/anchors incl. code links). Dispatched intake after verify to fill BibTeX metadata.
- End: CI/Pages/verify green, 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting). End of run 13.

## 2026-10-22 — run 14 (~10:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. The 07:43 intake slot fired at 07:38 and an extra scheduled run at 09:41 (both fine; no new papers until ~00:00 UTC), so no feed picks this run (10-22 feed reviewed in run 13).
- Owner added repo topics (`wam`, `ai`, `reinforcement-learning`, …). Took `wam` as a signal: added world action model anchors GR-1 (ICLR 2024), VPP (ICML 2025), UVA (RSS 2025), WorldVLA, Genie Envisioner (ICLR 2026); feed keywords ' wam ', ' wams ', 'video action model', 'action world model' (retag changed one feed paper: HAVANA → +world-models). Checked on arXiv HTML pages + GitHub search. verify #50 passed.
- Learning anchors DSRL (CoRL 2025), Flow Q-Learning (ICML 2025), SimpleVLA-RL (ICLR 2026); hardware anchors DexUMI (CoRL 2025), ACE (CoRL 2024, project page only — no code repo found).
- Manipulation anchors Transporter Nets (ravens repo archived → badge), CLIPort, PerAct, RVT, ReKep. Curated: 261.
- World-models topic description now mentions world action models (WAM) in EN/ZH.
- verify.yml #50, #51, #52 passed (all 15 new entries incl. code links; WorldVLA repo URL from the paper redirects fine). Dispatched intake after verify to fill BibTeX metadata.
- End: CI/Pages/verify green, 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting). End of run 14.

## 2026-10-22 — run 15 (~16:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. Intake slots fired at 13:10 and 15:51 (no new papers; next arXiv announcement ~00:00 UTC), so no feed picks this run. Local clone's `main` was stale (run 7); reset to `origin/main` before working (local only).
- **Start here / 入门路线** (`start.html`): 10-step reading path, 41 curated entries (RL/IL basics → visuomotor policies → data/tooling → VLA → sim → locomotion → world models → language/navigation → perception → hardware), bilingual step notes, linked from home hero, resources page, sitemap and both READMEs. `validate.py` fails on unknown ids. Tested headless at 390/1280 px (no JS errors, no horizontal scroll, 中文 toggle works, all 41 links resolve).
- Launch kit: 知乎 and 小红书 texts now point to the reading path; fixed topic count (12).
- Anchors: Contact-GraspNet (ICRA 2021, venue from NVIDIA Research page), AnyGrasp (SJTU, SDK) → manipulation + perception; FAST-LIVO2 (HKU MaRS) → perception; CoWs on Pasture (CVPR 2023, project page only) and PIRLNav (CVPR 2023) → navigation. IDs/titles confirmed on arXiv, repos via GitHub search. verify.yml #53, #54, #55 passed. Curated: 266.
- Weekly digest footer links the reading path (EN/ZH); tested by generating W43 locally (not committed — the scheduled job writes it Monday).
- Dispatched intake after verify to fill BibTeX metadata for the 5 new anchors.
- End: CI/Pages/verify green, 0 stars / 0 forks, no issues/PRs. Owner: nothing new beyond the launch kit (now with the reading path as the hook). End of run 15.

## 2026-10-22 — run 16 (~22:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. Intake fired at 19:17 (schedule); no new papers until ~00:00 UTC, so no feed picks this run. WebFetch of github.com pages was not permitted this run; used the read-only GitHub tools for issues/PRs/runs instead.
- **Tagging fix**: ' vla' / 'vla ' only matched between spaces, so PACT-VLA, FlowVLA, Fast-VLA, De-Diffusing WAMs etc. were untagged or missed VLA. `classify()` now pads punctuation and splits glued acronyms; added keywords (localization, pose tracking, optical flow, calibration, force/adaptive/robust control, embodied reasoning/planning, spatial memory, kinematic retargeting, UMI, pouring, world action language). Untagged 244 → 213 of 794; compared before/after on every stored paper: no topic lost. Retagged all stored days.
- Tactile anchors: Rotating without Seeing (RSS 2023), Robot Synesthesia (UCSD, project page only — no code released), NeuralFeels (Science Robotics 2024), Reactive Diffusion Policy (RSS 2025). Curated: 270.
- Weekly digest: new 'Rising on GitHub' section (top 8 star gains over 7 days up to the week's end; skipped until the history is long enough). Tested with fake history (not committed).
- verify.yml #56 and #57 passed (all 4 new tactile entries incl. code/project links). CI/Pages green. Dispatched intake after verify to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting). Next run (after ~00:00 UTC) should review the 10-23 feed for picks. End of run 16.

## 2026-10-23 — run 17 (~04:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. No scheduled intake fired between 19:17 (10-22) and 04:50 (01:11 and 02:17 slots missed again) → dispatched intake by hand.
- Anchors: Ruckig (RSS 2021, KIT) and OCS2 (ETH RSL) → control 20 → 22; HATO (ICRA 2025, UC Berkeley) → hardware 20 → 21 (+ tactile, manipulation). Checked on arXiv + GitHub search. Curated: 273.
- **Chinese search**: ~100 common Chinese terms map to English substrings in `app.js` (unspaced queries split into known terms). 人形 now finds 78 items (was curated-only), 人形机器人强化学习 → 17. Placeholder says 支持中文关键词. Tested headless (no JS errors).
- Intake #28 (manual) sat 9 min in arXiv API 429 backoff after RSS had 73 papers; cancelled. Fixes: intake/verify `timeout-minutes` (45/90), Retry-After capped at 300 s, API backfill only 3 attempts when RSS succeeded. Intake #29 then committed 73 papers for 10-23 (all enriched, 9 with code).
- verify #61 failed: API 429 for 22 min → abs-page fallback → false title mismatch VLA-$Δ$ vs VLA-$\Delta$. Fixed `norm_title` (Greek letters spelled out). Also: one red CI commit (OpenArm takeaway >220 chars slipped past because `validate | tail` hid the exit code); fixed in the next commit.
- Anchors: OpenArm (Enactic; hardware), MIT Cheetah 3 convex MPC (IROS 2018, no arXiv → linked via Cheetah-Software), legged_control → control 24, hardware 22.
- Picks 2026-10-23: OpenTac, GelSlim 5.0 (tactile), When One Step Is Enough (CoRL 2026), UniFlowWAM (WAM). Curated: 280.
- Verify: `arxiv_titles` now keeps partial API results and gives up after 3 attempts (abs pages cover the rest). verify #65 passed in 5 min for all 284 entries (incl. every entry added this run).
- Dataset anchors: HumanoidBench (RSS 2024), THE COLOSSEUM (RSS 2024), DexYCB (CVPR 2021), YCB object set → datasets 25. Curated: 284.
- Dispatched intake after verify to fill BibTeX metadata for new arXiv anchors.
- End: CI/Pages/verify green, 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting; it now mentions Chinese-keyword search). End of run 17.

## 2026-10-23 — run 18 (~10:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. Scheduled intake slots fired at 05:57, 07:36 and 09:37 UTC (the early slots still miss, but later ones now land). No new arXiv papers until ~00:00 UTC; 10-23 feed was reviewed in run 17, so no picks this run. (No add_repo tool this session; the repo was already cloned.)
- Anchors (IDs via arXiv search results, repos via GitHub search): AMP (SIGGRAPH 2021), Agile But Safe (RSS 2024) → locomotion 23; Depth Anything V2 (NeurIPS 2024), BundleSDF (CVPR 2023) → perception 23; Cal-QL (NeurIPS 2023), Q-Transformer (CoRL 2023) → learning 23. Curated: 290. verify #66 passed. Dispatched intake to fill BibTeX metadata.
- **Venue pages** `venues/<slug>.html` (16 at launch; CoRL 2026 has 36 papers three weeks before the conference) + `venues/index.html`; venue badges link to them; feed/topics pages, sitemap, READMEs and the weekly digest link them. Tested: 0 broken internal links, headless at 390 px (no JS errors, no horizontal scroll). Launch kit V2EX/Reddit texts mention them; CoRL week is a natural moment to post.
- Search results: venue badges link to venue pages too (index.json `venues` map). Tested headless (`?venue=CoRL` → 63 linked badges, no JS errors).
- End: CI #145 and Pages #247 green, verify #66 green, intake #34 (manual, BibTeX fill) ok. 0 stars / 0 forks, no issues/PRs. Owner: nothing new beyond the launch kit (CoRL week, Nov 9–12, is a good moment). End of run 18.

## 2026-10-23 — run 19 (~16:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. Intake fired on schedule at 12:51 and 15:42 UTC (no new arXiv papers until ~00:00 UTC; 10-23 feed reviewed in run 17), so no picks this run. No add_repo tool this session; the clone was already there (detached HEAD → checked out main).
- Dataset/benchmark anchors: EPIC-KITCHENS-100 (arXiv title is just "Rescaling Egocentric Vision"; IJCV 2022), HOI4D (CVPR 2022), OakInk (CVPR 2022), ARCTIC (CVPR 2023), VLABench (Fudan / OpenMOSS), RoboVerse (RSS 2025). IDs and numbers from arXiv pages, repos via GitHub search. Datasets 25 → 31; curated 296.
- **Hugging Face upvotes**: `scripts/hf_papers.py` (best-effort step in repo-stats.yml) → `data/hf_papers.json`; '▲ N HF' links on feed + curated cards, home 'Upvoted on Hugging Face' (last 14 days, top 8). Tested with fake data and a mocked fetch (failed day keeps old values, malformed items skipped). Workflow push was accepted.
- First real HF data (repo-stats #68): 36 of our papers are on HF Daily Papers (top: GPT-6-Astra report 468, Ropedia W0 150, DONIC 144). Used it as a review queue: picks GreenWAM (Sber; WAM across 20 robot families), VLA-Rolling (action-tail reuse for flow-matching VLAs), ScaleNav (internet-video pretraining for language navigation, ZJU). arXiv abs pages were not fetchable this run; takeaways from stored abstracts + HF model card / summaries, results phrased as 'reports'. VLA-Rolling code repo not found by GitHub search → no code link yet. Curated: 299.
- Search: '▲ N HF' in results, `?sort=hf`. Digest: 'Upvoted on Hugging Face' section. Tested headless at 390 px (no JS errors, no horizontal scroll).
- verify #67 (dataset anchors; EPIC title confirmed) and #68 (picks) passed; CI green. Dispatched intake to fill BibTeX metadata. READMEs mention stars + HF upvotes as signals.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting; CoRL week Nov 9–12 is a good moment). End of run 19.

## 2026-10-23 — run 20 (~22:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. No add_repo tool this session; the clone was already there (detached HEAD → `main` reset to `origin/main`). Scheduled intake fired 6× on 10-23 (first at 05:57 UTC; early slots still miss). No new arXiv papers until Mon 10-26.
- From the HF-upvote review queue: picks Learning from Fleet Experience (2610.25736; Tsinghua, AgiBot, Infinigence AI; code in RLinf) → learning; DONIC (2610.29997; Ropedia/DONIC) → manipulation; GPT-6-Astra embodied evaluation report (2610.22471; SenseNova et al., repo public with code 'coming soon' → project link) → vla. Anchor RLinf-VLA (2510.06710; RLinf repo 5.5k★) → learning. Facts from arXiv abs pages (reached via WebSearch results), HyperAI and Neurohive summaries; results phrased as 'reports'. Curated: 303.
- verify #69/#70 failed: arXiv v2 retitled 2610.25736 to "Learning from Fleet Experience: Collective Experience Learning Across 96 Robots" (HF/HyperAI still showed the v1 title). Updated the curated title; verify #71 passed for all 303 entries. Lesson: take titles from the live arXiv abs page, not mirrors. Dispatched intake to fill BibTeX metadata.
- End: CI/Pages/verify green, 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting; CoRL week Nov 9–12 is a good moment). End of run 20.

## 2026-10-24 — run 21 (~04:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. Saturday: no new arXiv announcements until Mon 10-26. No add_repo tool this session; clone already on `main`, up to date.
- From the HF-upvote queue: picks ACCRUE (continual off-policy RL for VLAs; NVIDIA, KAIST) → learning; λ0 / HumanVerse (500 h egocentric human data → Unitree G1; Alibaba, code LambdaHumanoid/openlambda, 29★) → locomotion; EgoExplorer (100 h vision-motion-touch human loco-manipulation; InternRobotics repo) → datasets. Facts from alphaXiv, Deep Learning Monitor and teahose/aiweekly summaries plus GitHub search (arXiv abs and project pages were not fetchable); results phrased as 'reports'. Curated: 306.
- One YAML slip (unquoted ': ' in a takeaway) caught by `validate.py` before commit.
- Survey anchors in vla.yaml: A Survey on VLA Models for Embodied AI (2405.14093, Awesome-VLA list), Foundation Models in Robotics (2312.07843, IJRR 2024), Aligning Cyber Space with Physical World (2407.06886, HCPLab-SYSU list). Titles checked on live arXiv abs pages. Paper lists linked as project, not code. Curated: 309.
- verify #72 and #73 passed; CI/Pages green. Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting; CoRL week Nov 9–12 is a good moment). Next: Mon 10-26 feed + first auto digest W43. End of run 21.

## 2026-10-24 — run 22 (~10:40 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. Saturday: no new arXiv days until Mon 10-26. No add_repo tool this session; clone was detached → `main` reset to `origin/main`.
- Picks from the HF-upvote queue: HandsOn (Tsinghua/BUPT/NatureWill/PKU dexterous sim benchmark; code TsinghuaC3I/HandsOn) and RoboValue (value-model benchmark; code + project page) → datasets.yaml. Facts from stored arXiv abstracts, AI Weekly / explainx summaries and GitHub search; results phrased as 'reports'. Project pages for FRED and LIBERO-Industry could not be fetched (permission not granted in an unattended run). Curated: 311.
- **Robot-type pages** `robots/<type>.html` + Atom feeds + index (8 types; humanoid: 32 curated + 60 feed). Linked from home, feed, topics index, READMEs, digest, sitemap. Tested: 0 broken internal links, headless at 390 px (no JS errors, no horizontal scroll). Digest robot-type counts now link to them (tested by generating W43 locally, not committed).
- verify #74 passed (both picks incl. code/project links); CI and Pages #298 green. Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting; CoRL week Nov 9–12). Next: Mon 10-26 feed + first auto digest W43. End of run 22.

## 2026-10-24 — run 23 (~16:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. Saturday: no new arXiv days until Mon 10-26. No add_repo tool; clone was detached → `main` reset to `origin/main`. Candidate picks (WAVE-0, FRED, …) still not findable via WebSearch, HF pages need approval nobody can give in a scheduled run.
- **HF links + review queue**: `hf_papers.py` keeps HF `githubRepo`/`projectPage` (sanitised), `merge_links()` fills missing feed code/project links (site, digest, repo_stats 404 check); writes `.autopilot/review_queue.json` with full abstracts for uncurated upvoted papers. Workflow step order swapped (HF first); workflow push accepted. Tested with a mocked fetch (failed day keeps old values, bad URLs dropped, existing arXiv code links win). First real run: 29/37 papers with GitHub links, queue of 18.
- Picks from the queue (facts = CI-fetched abstracts + repos confirmed live by repo_stats): WAVE-0 → vla, FRED → world-models, LIBERO-Industry → datasets, AgenticRoboRL + Scaling in Games → learning. One YAML colon slip caught by validate. Curated: 316.
- verify #75 passed (all 5 picks incl. code/project links); CI green. Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting; CoRL week Nov 9–12). Next: Mon 10-26 feed + first auto digest W43; picks from `.autopilot/review_queue.json`. End of run 23.

## 2026-10-24 — run 24 (~22:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs, 0 stars / 0 forks. Saturday: no new arXiv days until Mon 10-26. No add_repo tool; clone was detached → `main` reset to `origin/main`.
- Picks from `.autopilot/review_queue.json` (CI-fetched abstracts; repos live per repo_stats): MorphAct (SJTU, contextual low-rank VLA params), CarryOn (dual-loop harness for a frozen VLA), Towards Agentic Robots (survey, 126★ list) → vla; SERA (self-evolving harness, RoboMME) → manipulation; ACE-Brain-0.6 (9B grounding model) → perception. One takeaway at 221 chars caught by validate. Curated: 321.
- Launch kit: updated entry count (300+), HF upvotes and robot-type pages in V2EX/Reddit/HN texts.
- Measured search index: 711 KB raw / 239 KB gzip at 13 days; projection noted in STATE known issues.
- verify #76 passed (all 5 picks incl. code/project links); CI green. Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit refreshed, still waiting; CoRL week Nov 9–12). Next: Mon 10-26 feed + first auto digest W43. End of run 24.

## 2026-10-25 — run 25 (~04:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs (read via the GitHub MCP tools; WebFetch of github.com needs approval nobody can give in a scheduled run), 0 stars / 0 forks. Sunday: no new arXiv days until Mon 10-26. No add_repo tool; clone was detached → `main` reset to `origin/main`.
- Picks from `.autopilot/review_queue.json` (CI-fetched abstracts; paper-list repos live per repo_stats): Agentic World Action Models (AW-0; code+video+action streams) → world-models; Toward Recursive Self-Improvement in Physical AI (NUS survey, list as project) and PhysRSI-eval (Galbot, project only) → learning; Multimodal Embodied Agents (Show Lab survey, PAPAV) → vla. Three over-length takeaways caught by validate.
- Anchors: dm_control (2006.12983), SoftGym (2011.07215, CoRL 2020), Newton (Linux Foundation physics engine, no paper) → sim; NavGPT (2305.16986, AAAI 2024), ETPNav (2304.03047, TPAMI 2024) → navigation. Facts from arXiv abs pages / PMLR / LF press release; repos via GitHub search. One unquoted ': ' YAML slip caught by validate. Curated: 330. Push raced a repo-stats bot commit → `pull --rebase`, re-validated, pushed.
- verify #77 (picks) and #78 (anchors) passed; CI green. Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting; CoRL week Nov 9–12). Next: Mon 10-26 feed + first auto digest W43. End of run 25.

## 2026-10-25 — run 26 (~10:40 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. Sunday: no new arXiv days until Mon 10-26. No add_repo tool; clone was detached → `main` reset to `origin/main`.
- Picks from `.autopilot/review_queue.json` (CI-fetched abstracts; repos live per repo_stats feed section): TILDE (HKU; teacher-in-the-loop distillation from VLAs, AutoDAgger) → learning; TARSphere (embodied-agent framework + 360-episode bench) → navigation; SkeLAM (skeleton-grounded latent actions, project only) → world-models. One over-length takeaway caught by validate.
- Hardware anchors (thinnest topic): TidyBot++ (CoRL 2024), UMI-on-Legs (CoRL 2024), DOGlove (RSS 2025). Facts from PMLR / RSS proceedings pages; repos via GitHub search. Curated: 336.
- verify #79 (picks) and #80 (hardware anchors) passed; CI green. Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting; CoRL week Nov 9–12). Next: Mon 10-26 feed + first auto digest W43. End of run 26.

## 2026-10-25 — run 27 (~16:40 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. Sunday: no new arXiv days until Mon 10-26. No add_repo tool; clone was detached → `main` reset to `origin/main`. Review queue holds only off-scope items.
- Hardware anchors RUKA (2504.13165, RSS 2025; repo ruka-hand/RUKA) and Bidex / "Bimanual Dexterity for Complex Tasks" (2411.13677, CoRL 2024; project page only). Facts from RSS proceedings, PMLR v270 and live arXiv abs pages. Curated: 338.
- Digest: a local W43 draft had 63 picks in 'Editor's picks' (60 KB). `make_digest.py` now shows the top 8 by community signals with full takeaways and lists the rest compactly by topic (33 KB); `$Δ$`-style TeX in titles rendered. Draft not committed — weekly.yml writes W43 on Monday.
- verify #81 passed (RUKA, Bidex incl. links); CI and Pages green. Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting; CoRL week Nov 9–12). Next: Mon 10-26 feed + first auto digest W43. End of run 27.

## 2026-10-25 — run 28 (~22:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. Sunday night: no new arXiv day until Mon 10-26. No add_repo tool; clone was detached → `main` reset to `origin/main`. Review queue holds only off-scope items.
- Gap sweep: grepped curated data for ~60 well-known VLA / humanoid / dataset names; ~28 were missing (one false positive: ExBody is already in as 'Expressive Whole-Body Control'). Added 12 anchors with facts from arXiv abs/HTML pages, PMLR v305, RSS 2026 proceedings, ICLR 2026 / CVPR 2025 listings; repos via GitHub search: BeyondMimic → locomotion; EgoMimic → manipulation; MolmoAct, GraspVLA, π*0.6, X-VLA, InternVLA-M1, Magma, Being-H0 → vla; DexMimicGen → sim; EgoDex → datasets; SAM 3 → perception. Curated: 350.
- Fix: `build_readme.md_title` escapes `*` (π*0.6 would have opened Markdown emphasis in the README).
- A slicing slip briefly deleted most of locomotion.yaml locally; validate caught it (start.yaml ids missing) and the file was restored from git before commit.
- Also WALL-OSS (2509.11766, X Square Robot) → vla. Curated: 351. verify #82 and #85 (all 13 new entries incl. code/project links) passed; CI green. BibTeX metadata fills on the next scheduled intake (01:11 UTC slot).
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit still waiting; CoRL week Nov 9–12). Next: Mon 10-26 feed + first auto digest W43; remaining gap list in STATE backlog. End of run 28.

## 2026-10-26 — run 29 (~04:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. No scheduled intake had fired yet (01:11/02:17/04:53 slots) → dispatched intake.yml; 10-26 feed landed (67 papers), repo-stats followed.
- Anchors (facts from arXiv/HF/NeurIPS/ICLR/PMLR pages; repos via GitHub search): HPT (NeurIPS 2024), LAPA (ICLR 2025), HAMSTER (ICLR 2025, project only), 3D-VLA (ICML 2024), RynnBrain, GR-2 (project only), TraceVLA (ICLR 2025), OneTwoVLA (ICLR 2026) → vla; Seer (ICLR 2025), DexGraspVLA (AAAI 2026) → manipulation; DreamGen (CoRL 2025) → world-models.
- Picks from 10-26: FLORA (NVIDIA GR00T data engine; project + HF collection) → datasets; DexPort (hand-held dexterous data collection, project) → hardware; 'Full-Weight VLA Fine-Tuning Without an fp32 Master Copy…' (practical bf16 warning) → vla; RynnUnify (Alibaba DAMO, code) → world-models. Several over-length takeaways and two unquoted ': ' slips caught by validate. Curated: 366.
- Weekly digest W43: weekly.yml had not fired by 04:55 → dispatched; added a short bilingual editor's intro (WAM thread, harnesses around frozen models, CoRL acceptances). Fixed weekly.yml commit message (it said W44 for the W43 file); workflow push accepted.
- Also DexVLA (CoRL 2025) and TinyVLA → vla (project pages only; official repos unconfirmed). Curated: 368. verify #86, #89, #90 passed (all entries incl. links); CI green. Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: launch kit precondition (first auto digest) now met; CoRL week Nov 9–12 still the suggested moment. Next: daily picks from new feed days + review queue; W44 digest Mon 11-02; 'Rising this week' check from ~10-28. End of run 29.

## 2026-10-26 — run 30 (~10:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`.
- Fix: 5 feed cards had broken project links from LaTeX `\\href{a}{b}` / Markdown debris in arXiv comments (`…github.io/}{https://…}`, `…/]`). `tidy_url()` in intake + cleanup via `--retag` (topics unchanged).
- New: intake writes `.autopilot/candidates.json` (full abstracts + authors for recent uncurated papers with code/project/venue), because WebFetch of new arXiv/project pages needs approval nobody can give in scheduled runs. Tested with a mocked API; first CI run filled 100 candidates. Workflow push accepted.
- Anchors ChatVLA (EMNLP 2025), Hume, TwinVLA (ICLR 2026), VQ-VLA (ICCV 2025) → vla (facts from arXiv / ACL Anthology / alphaXiv; repos via GitHub search). Picks from candidates.json: ViT-H → locomotion, FORCA → manipulation, EgoForesight → learning, SceneBloom → sim. Two over-length takeaways caught by validate. Curated: 376.
- Anchors GigaBrain-0, Galaxea G0 + Open-World Dataset, RoboOS → vla; GenManip (CVPR 2025) → sim. Curated: 380. verify #92 and #94 passed (#93 cancelled by #94, which covers it); CI green. Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: daily picks from `.autopilot/candidates.json`; 'Rising this week' check from ~10-28; W44 digest Mon 11-02. End of run 30.

## 2026-10-26 — run 31 (~16:40 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. Weekly digest slot at 11:17 skipped correctly (W43 exists). HF review queue: only off-scope items.
- Picks from `.autopilot/candidates.json` (CI-fetched full abstracts; code repos checked against repo_stats feed section, 404 repos skipped): ContactBench 1.0 → manipulation; tactile-manipulation review + VecTile → tactile; BiDex-100 + AstroBench → datasets; EmbodiedWorld-200K (NeurIPS 2026) → navigation; LLM-LIBERO frontier-model benchmark + FastHarness → vla; MARE lunar simulator → sim; PHD-Hand (Humanoids 2026) → hardware; Rubik's Cube quadruped → locomotion; COWBOY → manipulation; Physical Canvas → world-models. Two over-length takeaways caught by validate. Generic/shortened links (annualreviews.org root, lnkd.in) left out. Curated: 393.
- Site: home page now has an 'Accepted at:' row linking this year's venue pages (CoRL 2026 (37), IROS 2026, NeurIPS 2026, …) — venue pages were only reachable from feed/topics pages, and CoRL week is Nov 9–12.
- verify #95 and #96 passed (all 13 picks incl. code/project links); CI and Pages green. Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: daily picks from `.autopilot/candidates.json` (unpicked list in STATE backlog); 'Rising this week' check from ~10-28; W44 digest Mon 11-02. End of run 31.

## 2026-10-26 — run 32 (~22:50 UTC–)

- Start: CI/Pages/verify/repo-stats/intake green, no issues/PRs (GitHub MCP; WebFetch of github.com needs approval nobody can give), 0 stars / 0 forks. No add_repo tool; existing clone on `main`, pulled. No new feed day since 10-26 (arXiv next announces Tue 10-27).
- Picks from `.autopilot/candidates.json` (CI-fetched full abstracts; code repos live per repo_stats feed section): PICA-WAM → world-models, Vision-Language-Delta-Action (Baidu, LoongForge cookbook link) → vla, LocoPilot (IIT DLS Lab) → hardware, TIDE → learning, InJePA → navigation, Embodied Playground → datasets. One over-length takeaway caught by validate. Curated: 399.
- verify #97 passed (all 6 picks incl. links). Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: picks from the 10-27 feed; 'Rising this week' check from ~10-28; W44 digest Mon 11-02. End of run 32.

## 2026-10-27 — run 33 (~04:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. No scheduled intake had fired yet → dispatched intake.yml; 10-27 feed landed ~05:00 (147 papers), repo-stats followed.
- Picks from `.autopilot/candidates.json` (CI-fetched full abstracts; code repos checked against repo_stats feed section): Horizon-Depth VLA (training-free solver-depth/horizon knob) → vla, DiscoDemo → learning, HAVANA → navigation; from 10-27: OSWAM → world-models, EBench GPT-6-Astra report + PrecisionReach-GS + AGQ (VLA quantization, code) → vla, FLoRe + Zero-HLM → locomotion, BEHAVIOR-Spatial → datasets. Three over-length takeaways caught by validate. Curated: 409.
- verify #98 (3 picks) still running at run end and #100 (covers all 10 picks) queued — re-check at the start of run 34; fix or drop any failing entry.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: check verify #98/#100; 'Rising this week' check from ~10-28; picks from 10-28 feed; W44 digest Mon 11-02. End of run 33.

## 2026-10-27 — run 34 (~10:45 UTC–)

- Start: CI/Pages/repo-stats/intake green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. verify #100 passed (all run-33 picks); #98 had failed on a real bug.
- Fix: `norm_title` mapped λ to 'lamda' (Unicode name) but TeX says `\lambda`, so λ0 (2610.18950) failed whenever the arXiv API was rate-limited and the abs-page fallback was used.
- Picks from `.autopilot/candidates.json` (code repos live per repo_stats feed section): RynnVLA-Latent (Alibaba DAMO) → vla, EmbodiedLab (HexaFuture) → datasets, MOON (SJTU) → navigation, Video World Models Need Predictable Latents + DeXplicit → world-models, HumanoidNDM (CoRL 2026) → locomotion, ARPG → manipulation. Curated: 416.
- Links: VLA-Rolling gets code (ZJU-OmniAI/VLA-Rolling, listed on its HF page) + project. New `curated_link_updates` list in the review queue (HF-listed repo/project missing from curated entries); applied 10: code for GreenWAM, ScaleNav, DiscoDemo, FLORA; project pages for VLA-Δ, MambaAct, DONIC, Ropedia W0, Fleet Experience, HandsOn.
- verify #104 passed (covers all run-34 picks and links; #102/#103 cancelled by it). BibTeX metadata for new picks fills on the next scheduled intake.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: 'Rising this week' check from 10-28; picks from the 10-28 feed; W44 digest Mon 11-02. End of run 34.

## 2026-10-27 — run 35 (~16:50 UTC–)

- Start: CI/Pages/repo-stats/intake green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → switched to `main` and pulled. No new feed day until Wed 10-28.
- Picks from `.autopilot/candidates.json` and the HF review queue (CI-fetched abstracts; code repos live per repo_stats feed section): DiffContact, HuMiT → locomotion; Action Influence Maximization (CoRL 2026), TrajWAM → world-models; AdaDexTrack (CVPR 2026), AdaPolicy → manipulation; ACTS → tactile; VISTA, Echo → vla; RobotAgentBench → datasets. One over-length takeaway caught before writing. Curated: 426. `curated_link_updates` holds only previously skipped items.
- verify #105 and #106 passed (all 10 picks incl. code/project links). Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: 'Rising this week' check from 10-28; picks from the 10-28 feed; W44 digest Mon 11-02. End of run 35.

## 2026-10-27 — run 36 (~22:50 UTC–)

- Start: CI/Pages/repo-stats/intake green, no issues/PRs (GitHub MCP; WebFetch of github.com not approved), 0 stars / 0 forks. No add_repo tool; existing clone on `main`, pulled. No new feed day until Wed 10-28.
- Feature: lab / company pages (`data/labs.yaml` → `labs/<id>.html`, 41 labs with ≥3 curated entries; 384 of 426 entries matched). Home 'By lab' row, entry-page 'More from' links, `labs` export column, README links. Checked on a 390 px viewport (EN + 中文), no JS errors.
- Picks from `.autopilot/candidates.json`: DISCO (CoRL 2026 Oral), Real2Sem2Real → manipulation; SWAP, FIBER → locomotion; Multi-View Latent Action Pretraining → vla. Four over-length takeaways caught before writing. Curated: 431.
