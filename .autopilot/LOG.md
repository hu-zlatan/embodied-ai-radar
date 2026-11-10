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
- verify #107/#108 passed (all 5 picks incl. project links). Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: 'Rising this week' check from 10-28; picks from the 10-28 feed; W44 digest Mon 11-02. End of run 36.

## 2026-10-28 — run 37 (~04:50 UTC–)

- Start: CI/Pages/verify/repo-stats green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. No scheduled intake yet → dispatched intake.yml; 10-28 feed landed 04:50 (91 papers), repo-stats followed (8th daily star snapshot).
- 'Rising this week' now renders on the home page with real 7-day gains (lerobot +163, mujoco +127, …); +N badges on the most-starred list too. No code change needed.
- Picks (facts from CI-fetched `.autopilot/candidates.json` / HF review queue; code repos live per repo_stats feed section): TAPESTRY (CoRL 2026), GAWM, RynnWorld-Latent, Rollback → world-models; JAM, PaceVLA, OmniBrain-0, ThinkWorld → vla; DexSafe, CARD, RoboLongR → manipulation; HIDRA (NeurIPS 2026), PGPG (CoRL 2026) → learning; One Scan is Enough (NeurIPS 2026) → navigation; OpenJaws → hardware; SO-101 Bench → datasets. Two over-length takeaways caught before writing. Curated: 447.
- verify #109 and #110 passed (all 16 picks incl. code/project links); CI green. Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: picks from the 10-29 feed (+ leftovers listed in STATE backlog); W44 digest Mon 11-02 (first with 'Rising on GitHub'). End of run 37.

## 2026-10-28 — run 38 (~10:50 UTC–)

- Start: CI/Pages/verify/repo-stats/intake green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. No new feed day until Thu 10-29.
- Picks from `.autopilot/candidates.json` (10-28 leftovers): Trace-WAM → world-models; Retrieve to Act → vla; REACH (Humanoids 2026, SUSTech) + GRAFT → locomotion; RoboSTD + cuArms → manipulation; Keeping Contact (RA-L) → control. From the HF review queue: PDRVLA (92 upvotes) + FocusVLA (CoRL 2026) → vla; RoboJudge (CUHK, code) → datasets. JAM gets its code link (repo confirmed live via GitHub search). Five over-length takeaways caught by validate. Curated: 457.
- verify #111 and #112 passed (all 10 picks + JAM code link). Dispatched intake to fill BibTeX metadata.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: picks from the 10-29 feed; W44 digest Mon 11-02. End of run 38.

## 2026-10-28 — run 39 (~16:50 UTC–)

- Start: CI/Pages/repo-stats/intake green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → `main`, pulled. No new feed day until Thu 10-29; HF review queue unchanged (only off-scope items).
- Picks from `.autopilot/candidates.json` leftovers: MoGAP (motion-focused auxiliary loss for WAMs) → world-models; RepresentNav → navigation; RISE (steerable humanoid fall recovery) + Stochastic Motion Tokenization (Humanoids 2026) → locomotion. Two over-length takeaways caught by validate. Curated: 461.
- verify #113 passed (all 4 picks incl. project links). BibTeX metadata fills on the next intake (10-29).
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: picks from the 10-29 feed; W44 digest Mon 11-02. End of run 39.

## 2026-10-28 — run 40 (~22:50 UTC–)

- Start: CI/Pages/repo-stats/intake green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. No new feed day until Thu 10-29.
- Picks from `.autopilot/candidates.json` leftovers (CI-fetched abstracts; repo live per repo_stats feed): Calibrated for Which Policy? → world-models; MyoAcross → control. Curated: 463. validate + README check + site build clean.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: picks from the 10-29 feed; W44 digest Mon 11-02. End of run 40.

## 2026-10-29 — run 41 (~10:50 UTC–)

- Start: CI/Pages/repo-stats/intake green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`.
- No 10-29 feed day: both intake runs logged `rss: 0 relevant items` and 0 new API papers, so arXiv seems to have posted no announcement; later backup slots will catch it if it appears.
- CI hygiene: actions/checkout v4 → v5, setup-python v5 → v6 in all 6 workflows (every run warned about Node 20 being forced to Node 24).
- Picks from `.autopilot/candidates.json` leftovers (CI-fetched abstracts): SpatialDex → manipulation; Sensorimotor Alignment (S²) + PAL → vla; FLEX (CoRL 2026, MIT CLEAR Lab) → learning; SMR → locomotion; GEMS + GEMS-Bench → navigation. Four over-length takeaways caught by validate. Curated: 469.
- verify #115 passed (all 6 picks incl. project links); CI and Pages green on the new action versions. BibTeX metadata fills on the next intake.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: 10-29 feed if it appears in a later slot, else Fri 10-30; W44 digest Mon 11-02. End of run 41.

## 2026-10-29 — run 42 (~16:50 UTC–)

- Start: CI/Pages/repo-stats/intake green, no issues/PRs (GitHub MCP), 0 stars / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. Intake at 14:38 UTC still had `rss: 0 relevant items`.
- Intake diagnostics: `fetch_rss()` now prints total items / no-id / replacements / off-topic and the channel date. Dispatched run: `items=0`, channel date Thu 29 Oct 2026 → arXiv published an empty feed today; nothing to fix in the parser.
- Picks from `.autopilot/candidates.json`: EgoThumb (IROS 2026; open-source supernumerary thumb) → hardware; PhysTrace (training-free physics-consistency eval for video models, code live) → world-models. Two over-length takeaways caught by validate. Curated: 471.
- End: 0 stars / 0 forks, no issues/PRs. Owner: nothing new (launch kit ready; CoRL week Nov 9–12 suggested). Next: Fri 10-30 feed picks; W44 digest Mon 11-02. End of run 42.

## 2026-11-01 — run 43 (~10:45 UTC–)

- Start: CI/Pages/repo-stats/intake green, no issues/PRs (GitHub MCP), **1 star** / 0 forks (first star). No add_repo tool; clone was detached → `main` reset to `origin/main`. Feed day 10-30 landed (46 candidates); 10-29 stayed empty on arXiv's side.
- Picks (facts from CI-fetched abstracts in `.autopilot/candidates.json` and `.autopilot/review_queue.json`): UMI-Live, SwapBot, DexSuite, Gym-Anything for Robotics, METATRON, SONIC-K1, LaWAM (CoRL 2026), QbD-VLA, EgoContact, WorldFlow, π0.5-on-BEHAVIOR paired evaluation, HuGe, OSMA-Bench; Sensorimotor Alignment gets its code link (repo now live, 8★). Two over-length takeaways caught by validate. Curated: 484.
- One push was rejected because the stats bot pushed in between → `git pull --rebase`, re-checked, pushed (no force).
- Launch kit entry counts refreshed (300+ → 480+).
- verify #117 passed (first 8 picks); #119 (all 13 + code link) was queued at end of run — check it first next run. End: 1 star / 0 forks, no issues/PRs. Owner: nothing new. End of run 43.

## 2026-11-01 — run 44 (~16:50 UTC–)

- Start: CI/Pages/repo-stats/intake green, verify #119 passed (all run-43 picks), no issues/PRs (GitHub MCP), 1 star / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. Sunday: no new feed day until Mon 11-02.
- Picks from `.autopilot/candidates.json` 10-30 leftovers (CI-fetched abstracts; RoboSeed and CuraEval repos live per repo_stats feed): ScheduleGen → manipulation, ELEVATE → locomotion, RoboSeed → vla, CuraEval → learning. Two over-length takeaways caught by validate. Curated: 488. verify #120 started; intake dispatched to fill BibTeX metadata.
- End: 1 star / 0 forks, no issues/PRs. Owner: nothing new. Next: Mon 11-02 feed + W44 digest intro; CoRL week sweep. End of run 44.

## 2026-11-01 — run 45 (~22:50 UTC–)

- Start: CI/Pages/repo-stats/intake green, no issues/PRs (GitHub MCP), 1 star / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. Sunday night: no new feed day.
- Gap-fill anchors (facts from arXiv abs / papers.cool / official README; repos confirmed via GitHub search): MolmoAct2 (Ai2, Apache-2.0 repo), UnifoLM-VLA-0 (Unitree G1 humanoid VLA), GigaBrain-0.5M* (world-model-conditioned RL post-training). Curated: 491.
- End: 1 star / 0 forks. Owner: nothing new. Next: Mon 11-02 feed + W44 digest intro. End of run 45.

## 2026-11-02 — run 46 (~04:50 UTC–)

- Start: CI/Pages/repo-stats/intake green, no issues/PRs (GitHub MCP), 1 star / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. Monday feed and W44 digest not landed yet (both ~05:30–06:00 UTC).
- Internal link check over 598 pages: 0 broken; no horizontal overflow at 390 px; no JS errors.
- Venue backfill shipped and ran (2 dispatches, both green): 1,030 accepted papers; CoRL 2026 page 37 → 174. Audit of comments found one 'rejected by RSS 2026 AND CoRL 2026', an ICRA late-breaking poster and a challenge solution → `venue_of()` tightened.
- Venue pages: filter box and Oral/Spotlight badges (tested in Chromium at phone width, both languages).
- Curated 491 → 496: Wall-OSS-0.5, EagleVLA, LIFT, AgentCanvas, FiberTune.
- W44 digest dispatched (landed ~05:20 UTC) and got its bilingual intro. End: 1 star / 0 forks. Owner: CoRL week is the moment for the launch kit, if wanted. Monday's feed had not landed at end of run; next run picks it up. End of run 46.
- verify #124 passed (Wall-OSS-0.5); #125 (the 4 CoRL picks) was still running at end of run: check it first next run.

## 2026-11-02 — run 47 (~10:50 UTC–)

- Start: CI/Pages/intake green, verify #125 passed, no issues/PRs, 1 star / 0 forks. No add_repo tool again; local `main` was stale, reset to `origin/main` (no local work lost).
- Curated 496 → 515 (19 picks, see STATE backlog). Oral/Spotlight badges now also on curated cards; before, the venue filter hid curated orals such as DISCO. Tested in Chromium at 390 px, both languages.
- Launch kit: CoRL 2026 post added, entry counts refreshed.
- **Incident:** main failed to build for a few minutes. Three pushes in one shell command: `... | tail` hid a failing exit code, so commits faf6c85 and 66d1dc1 went out half-applied with a duplicate entry (SuperMimic was already curated) and an integer YAML tag (`360`) that crashes build_site though validate passed. Fixed in f677e11. Lessons: `set -o pipefail` in every push command; validate.py now rejects non-string tags. Commit message of faf6c85 overstates its content (no history rewrites, so it stays).
- `repo_stats.py` crashed on one dropped connection (RemoteDisconnected, run 211, not related to the data); `fetch()` now catches it like other network errors, so old values are kept.
- verify #126 passed (first 11 picks); #128 (the other 8) was in progress at end of run: check it first next run. End: 1 star / 0 forks. End of run 47.

## 2026-11-02 — run 48 (~17:02 UTC–)

- Start: CI/Pages green, verify #129 passed, no issues/PRs, 1 star / 0 forks. No add_repo tool; clone was detached → `main` reset to `origin/main`. Repo fetched directly.
- Found that the official CoRL accepted list holds the full program (687 papers, 21 orals, 72 spotlights, poster numbers, rooms). Two CI probes showed how it is embedded; `corl_program.py` + `corl-program.yml` read it and match arXiv by title. Program guide page shipped (tested at 390 px on a sample of the data).
- 9 picks (curated 524). Three over-length takeaways caught by validate.
- Program run 1 failed on a wrong `load_curated()` unpack and runs 2-3 were cancelled while pending (a newer run in the `arxiv-api` group replaces a pending one). Fixed, tested the whole flow with mocks, run 4 green: 554 of 687 papers linked to arXiv in 48 min.
- 17 CoRL orals curated (541 total). CoRL page 556 papers. Launch kit CoRL post rewritten around the guide; OWNER_TODO link updated.
- End: 1 star / 0 forks, no issues/PRs. Owner: CoRL week is the moment for the launch kit, if wanted. verify run for the orals was in progress at end of run: check it first next run. End of run 48.

## 2026-11-02 — run 49 (~22:50 UTC–)

- Start: CI/Pages/intake green, verify #133 passed (the orals), no issues/PRs, 1 star / 0 forks. No add_repo tool; detached shallow clone → `main` reset to `origin/main`. Tue feed not out yet.
- Program guide: personal schedule (save, share link, text, .ics, 'My list' filter). Tested in Chromium at 390 px, both languages, reload and shared link; no JS errors. One bug found in testing (text export glued EN+ZH session names) and fixed before pushing.
- Curated 541 → 573: 32 CoRL Spotlights. Local link check over 684 pages: no broken internal links. Launch kit CoRL post mentions the schedule.
- End: 1 star / 0 forks. Owner: CoRL week is the moment for the launch kit, if wanted. Verify run for the spotlights was in progress at end of run: check it first next run. End of run 49.

## 2026-11-03 — run 50 (~04:50 UTC–)

- Start: CI/Pages/intake green, verify #134 passed (the spotlights), no issues/PRs, 1 star / 0 forks. No add_repo tool; detached clone → `main` reset to `origin/main`. Tue feed not out yet.
- Found the CoRL guide's 'Has code' filter was thin: 57 of 554 arXiv-linked papers, while 275 more had a project page. Shipped `project_code.py` (reads those pages in CI, checks repos on the GitHub API). First run: 284 papers, 64 curated, 3 min. CoRL guide 57 → 178 with code.
- Audit by hand: all 34 links not named after the paper and the 106 named by loose match. One wrong link (DriveCritic → author's older LiRaFusion) and one blog repo rejected; age limit tightened. 60 of 64 curated code links applied (survey and 'coming soon' repos left out).
- Curated 573 → 583 (10 picks from the 10-26..11-02 feeds, see STATE backlog). Note: a pipe into `head` under pipefail gave exit 141 after a good push; confirmed on origin.
- End: 1 star / 0 forks, CI and Pages green. Owner: CoRL week is the moment for the launch kit, if wanted. Verify #135 and #136 (picks + 60 code links) were in progress at end of run: check them first next run. End of run 50.

## 2026-11-03 — run 51 (~10:50 UTC–)

- Start: CI/Pages/intake green, verify #135 and #136 passed, no issues/PRs, 1 star / 0 forks. No add_repo tool; detached shallow clone → `main` reset to `origin/main` (the 'forced update' from fetch was the shallow clone, not a rewrite).
- Found the Tue announcement scattered: RSS gave items=0 at 07:50 UTC, so the API filed 139 papers under submission dates (10-31, 11-01, 11-02) and the newest day page showed 17 of 156. Fixed intake (API finds in normal runs use today's date) and moved the 139 to 11-03. The 10-31 and 11-01 day pages existed for about 3 hours and are gone.
- Curated 583 → 604: 21 picks (the commit message says 22; 21 is correct). 10 over-length takeaways caught by validate. Code links only for repos live in `repo_stats.json`.
- Local link check over 716 pages: no broken internal links.
- End: 1 star / 0 forks. Owner: CoRL week is the moment for the launch kit, if wanted. Verify run for the picks was in progress at end of run: check it first next run. End of run 51.

## 2026-11-03 — run 52 (~16:50 UTC–)

- Start: CI/Pages/intake green, no issues/PRs. **Verify #137 (run 51's picks) had failed**: DiffContact title changed on arXiv, OpenNWM project page 404, robocolosseum.ai 401. Live site was unaffected (verify does not gate deploys), but three facts were wrong or unconfirmed for ~6 hours.
- Fixed: DiffContact title updated to arXiv's; OpenNWM's dead project link replaced by its repo, now live; RoboColosseum project link removed from the curated entry because it answers 401 to CI and the reason could not be checked (it is the link the paper gives; restore when public).
- CoRL guide: 'Most-starred code' top 10 with session or poster number (no overflow at 390 px, no JS errors). HF list dropped: only 3 CoRL papers had upvotes.
- Curated 604 → 612: 8 picks from the 11-03 feed. Project links come from the papers and could not be opened from here, so the verify run on this push decides.
- Verify #138 (the three fixes) passed. #139 (the picks) was cancelled while pending, as a newer run in the `arxiv-api` group replaced it, so the push had no check; re-dispatched as #140, passed, all 8 project and code links good. **Watch for this:** a 'cancelled' verify means the push was not checked.
- End: see the summary to the owner. Not fixed: verify still has no retry when cancelled. End of run 52.

## 2026-11-03 — run 53 (~22:50 UTC–)

- Start: CI/Pages/intake/repo-stats/verify green, no issues/PRs (GitHub MCP), 1 star / 0 forks (search API). No add_repo tool; clone was detached → `main` reset to `origin/main`. No new feed until Wed 11-04.
- QA: internal links 0 broken across 724 pages; 9 main pages clean at phone width (no overflow, no JS errors).
- Gap sweep against an external VLA list: 13 missing anchors added with facts read from arXiv/HF/official pages; 5 picks from candidates.json; 4 code links. Curated: 630.
- CI: `scripts/check_links.py` step added so internal link breaks fail the build.
- verify #141 passed (all new IDs, titles and links). CI green with the link check.
- End: 1 star / 0 forks, no issues/PRs. Owner: post the CoRL program text by Sun 11-08 if wanted. Next: Wed 11-04 feed; more gap sweeps; W45 digest intro Mon 11-09. End of run 53.

## 2026-11-04 — run 54 (~04:50 UTC–)

- Start: all workflows green, no issues/PRs, 1 star / 0 forks. No add_repo tool again; `main` reset to `origin/main` (shallow-clone 'forced update').
- Intake dispatched at 04:50 UTC: no 11-04 papers yet (RSS empty after the announcement, a known pattern; candidates.json shrank only because old papers aged out). Later intake slots should bring them.
- New `facts.yml` + `scripts/fetch_facts.py`: WebFetch refused arXiv and HF URLs, so CI now gets abstracts, HF links and repo stars for chosen IDs. First run: 32 of 32 papers.
- Gap sweep of two external lists: 31 anchors (see STATE backlog). DreamZero was already curated without an ID match; caught by validate and dropped. Curated 630 → 661.
- Local: validate 0 errors, 774 pages built, 0 broken internal links.
- Verify #142 took 33 min (arXiv API 503/429, abs-page fallback). All 31 new anchors passed. It failed on one older entry: arXiv retitled 2610.37652, now updated. `vis-www.cs.umass.edu/3dvla` gave a network warning only. Re-check verify for the retitle push next run. W45 intro due Mon 11-09; CoRL program text by Sun 11-08 if the owner wants it. End of run 54.

## 2026-11-04 — run 55 (~10:50 UTC–)

- Start: all workflows green incl. verify #143 (retitle), no issues/PRs, 1 star / 0 forks. No add_repo tool; `main` reset to `origin/main`.
- 11-04 feed arrived (77 papers). 15 picks, 6 code links (repo READMEs read; PrimeSim repo is a placeholder so not linked). Curated 676.
- README 267 KB → 65 KB; full lists in `lists/`. It would have reached GitHub's 512 KB limit in about two weeks at the recent pace, and Related lists / Contribute were buried.
- Found: a search for the project returns nothing, and robots.txt at a subpath is useless to crawlers. Added IndexNow (first call 403 while the key was new; second call accepted) and a Search Console owner task.
- Queued facts for 37 world-model and VLA anchors from external lists.
- Verify #144 (15 picks, 6 code links) passed. 37 anchors from the world-model sweep added with facts from the workflow; curated 713; local checks clean (828 pages, 0 broken links). Verify on that push is the next check.
- Verify #145 and #146 passed (37 anchors, all IDs, titles and links). IndexNow run 2 accepted 827 URLs. Curated 713.
- Owner: Search Console task (OWNER_TODO). Next: Thu 11-05 feed; W45 digest intro Mon 11-09; CoRL program text by Sun 11-08 if wanted; next sweep: rest of the world-model list. End of run 55.

## 2026-11-04 — run 56 (~16:50 UTC–)

- Start: all workflows green incl. verify #146, no issues/PRs, 1 star / 0 forks. No add_repo tool; `main` reset to `origin/main`. No new feed day since run 55.
- CoRL program page: 'The conference in numbers' (82% on arXiv, 26% with code found, title themes as bars, each a filter). Browser test at 1100 and 390 px: no overflow, no JS errors, `?theme=humanoid` shows 65 of 687. Filter count now counts papers, not cards; deep-link hash no longer dropped.
- 9 picks and 1 code link from the 11-04 candidates; repo READMEs read. Curated 722. Local: validate 0 errors, 838 pages, 0 broken links.
- Launch kit CoRL post has the numbers. Owner: post by Sun 11-08 if wanted; Search Console task open. Check verify on this push next run. Next: Thu 11-05 feed; W45 intro Mon 11-09. End of run 56.

## 2026-11-04 — run 57 (~22:50 UTC–)

- Start: all workflows green incl. verify #147, no issues/PRs, 1 star / 0 forks. No add_repo tool; `main` reset to `origin/main`. No new feed day yet.
- Search index had passed the ~1 MB trigger (1.76 MB raw). Abstracts now 14 days, 240 chars: 1.57 MB raw / 511 KB gzip before new entries. Titles are now the largest part; next step if needed is to split the index by month.
- CoRL guide: 23 orals/spotlights on arXiv lacked a takeaway; all added from fetched abstracts. Guide now states coverage (102 at that point). 11 orals/spotlights have no arXiv match, so no takeaway.
- Humanoid gap sweep against two external lists: 53 anchors from fetched facts (GMT, TWIST, TWIST2, HugWBC, AMO, BFM-Zero, GMR, OmniRetarget, KungfuBot, BeamDojo, ExBody2, HoST, ...). The list's labels were unreliable (2508.16943 is LHM-Humanoid, not HumanoidVerse), so titles come only from fetch_facts. Code links only where the workflow confirmed the repo. Curated 798. `$Ψ_0$` now renders in titles.
- Local: validate 0 errors, 914 pages, 0 broken links. Verify #148 still running and #149 queued at the end of this run, so the 76 new entries are not CI-checked yet (see STATE next steps). Launch kit numbers updated. Owner: CoRL post by Sun 11-08 if wanted; Search Console task open. End of run 57.

## 2026-11-05 — run 58 (~04:50 UTC–)

- Start: no issues/PRs, 1 star / 0 forks. No add_repo tool; `main` reset to `origin/main`. Verify #149 failed on one link only: LeVERB's project page 404 after its org moved. All 76 new entries otherwise passed.
- LeVERB link pointed to the new org's Pages URL, derived from the repo found by repo search; not opened by us, verify decides.
- Intake dispatched 04:50 UTC: no 11-05 papers yet (known RSS pattern); scheduled slots should bring them.
- CoRL guide: Now/Next bar and per-session 'Your time' line for viewers outside Austin. Browser test with mocked clock and time zones (Shanghai 390 px, Chicago 1100 px, before/during/after): no overflow, no JS errors.
- 4 picks from leftover 11-04 candidates (SR-DP, CoReMatch, FineCraft, ARPG). Curated 802. Local: validate 0 errors, 918 pages, 0 broken links.
- Web fetches refused in this run (unanswered permission prompt): vergilshawn sweep skipped, not routed around.
- CI #327 failed on the LeVERB commit: I skipped `build_readme.py`, so lists/vla were stale for about 4 minutes; #328 on the next commit is green. Run `build_readme.py` after any curated edit.
- End: 1 star / 0 forks. Verify #150 still running and #151 pending at the end of this run, so the LeVERB URL and 4 picks are not CI-checked yet; the live site could not be opened from here. End of run 58.

## 2026-11-05 — run 59 (~10:50 UTC–)

- Start: no issues/PRs, 1 star / 0 forks. No add_repo tool; clone was detached and shallow, `main` reset to `origin/main`. Workflows green except verify #150/#151.
- Verify failures fixed: HexaShell title changed on arXiv; kyry.me/sonic-k1 404 → https://huggingface.co/Kyry10/sonic-k1 (found by search); FLoRe project page 404, line removed (no replacement found). LeVERB link passed, so the moved URL stands.
- 11 picks from the 11-05 feed: NEO-VLA, Open-HumanScale, HALO (highlights), Ctrl-F, Cosmos interactive simulation, MESA, BEAKER, RACE, ELA, GRASP, OdorSpaces. Curated 813.
- Overlap sweep started: 10 external lists fetched from the shell, 62 uncurated IDs appear in ≥2 independent lists; `facts.yml` dispatched for them.
- Overlap sweep: added 46 of the 62 anchors from `facts.yml` (surveys, 3D and consistency diffusion policies, RoboVLMs, RDT2, ABot-M0, Qwen-VLA, VITRA, spatial VLMs, ManiSkill2, UnrealZoo, NavDP, Humanoid-VLA, RHINO, NIL). Skipped humanoid team papers with thin signal, Compositional Foundation Models, Imagination Policy, DNAct, multi-agent and very recent items. New anchors carry no `added:`, so they stay out of picks feed and digest. Labs: X Square Robot, Xiaomi, Robbyant. Curated 859.
- Verify #152 passed (11 picks, SONIC-K1 HF link, HexaShell title). LeVERB link passed.
- Verify #153 passed (all 46 anchors, links and titles); CI and Pages green on the last commit. Launch kit counts updated to 850+. No new owner task; CoRL post still fits until Sun 11-08, Search Console still open. Commit 7f86f2b carries author name hu-zlatan by a slip in my git command; authored by the agent. End of run 59.

## 2026-11-05 — run 60 (~16:50 UTC–)

- Start: no issues/PRs, 1 star / 0 forks. No add_repo tool; `main` reset to `origin/main` (local only). Workflows green.
- New: `code.html` code tracker (457 repos, stars, weekly gain, last push, license; filters, sort, shareable URL). Nav link 'Code', home link, sitemap, READMEs, launch kit line, entry-page license line, `code_license` column. Browser test at iPhone width with mock license data: filters, sort, URL, zh labels fine, no overflow, no JS errors.
- `repo_stats.py` stores the license; the push started the stats workflow, so real data arrives on its own.
- Hand review of `project_code.json` `curated`: 59 code links added, many on anchors from runs 53-59. READMEs read from the shell to catch 'coming soon'. Left out CANVAS, a VLA survey, TARC.
- Picks: PHIL, CSO (NeurIPS 2026), object-centric motion priors (AAAI 2026 oral) to manipulation; Astra on RoboMME to vla; ReactWorld to world-models. Curated 864.
- Real license data landed: 458 repos, 304 permissive, 8 copyleft, 65 custom, 81 none. Site rebuilt locally with it: 989 pages, 0 broken links.
- End: verify #154 still running and #155 pending at the end of this run, so the 5 picks and 59 code links are not CI-checked yet; next run checks them (STATE next steps). Live site not opened from here. No new owner task; CoRL post still fits until Sun 11-08, Search Console still open. End of run 60.
- Stars at end of run: 2, forks 0 (first new star since launch).

## 2026-11-05 — run 61 (~22:50 UTC–)

- Start: no issues/PRs, 2 stars / 0 forks. No add_repo tool; repo was already cloned. Workflows green except verify #155.
- Verify #155: all 59 code links of run 60 passed but airoa-org/AIRoA-0 (404). `code:` removed; project page stays. Could not read a-0.airoa.io: web fetches timed out on an unanswered permission prompt, not routed around. Two warnings only (Qwen RobotWorld blog, 3DVLA page: network errors).
- 6 picks: PyRUA-REAL, CoDA, failure-boundary profiles, latent property adaptation, Jev-AD, LeWM action geometry. Project links added to uni-robot-agent and Say the Same (from HF, verify decides). PrimeSim README still says 'code coming soon', so no code link. Curated 870.
- New: 'Similar entries' on entry pages (TF-IDF over title, tags, takeaway) replaces the same-topic list. Spot check on RT-1, AIRoA-0, failure-boundary: results make sense. Local: validate 0 errors, 995 pages, 0 broken links.
- Search index reviewed (known issue): capped and lazy, left as is.
- A search for the project name still finds nothing from this site; Search Console remains the owner's task.
- End: 2 stars / 0 forks. CI and Pages green on 68d99dd. Verify #157 still pending at the end of this run, so the 6 picks and 2 project links are not CI-checked yet; next run checks them. Live site not opened from here. No new owner task; CoRL post still fits until Sun 11-08, Search Console still open. End of run 61.

## 2026-11-06 — run 62 (~04:50 UTC–)

- Start: no issues/PRs, 2 stars / 0 forks. Repo already cloned (detached HEAD); switched to `main` and pulled. No add_repo tool needed.
- Verify #157 failed on one link: HoST project page (taohuang13.github.io/humanoid-standingup.github.io) is 404 although the repo README still links it; line removed (code + arXiv stay). Verify #158 then flagged two arXiv title changes: Open-HumanScale is now Open-HumanWAM, and RoboTryOn lost its prefix. Titles updated.
- CoRL week prep: listed CoRL 2026 program papers on arXiv with live code but no takeaway (39). Ran `facts.yml` for 33, read READMEs from the shell, and added 31 entries with `venue: CoRL 2026` (Large Video Planner, PRISM, ImageWAM, WLA, TOPReward, Light-WAM, EventVLA, VLS, μ0, HuRo, ACE-Ego-0, Functional-SLAM, APT, DeCAL, CostNav, StressDream, PAINT, HERO, MPAIL2, MobiAgent, RoboMemory, Cyclops, ReSiReg, RoboFollow, Seeker, VISTA, PoLAR, leg-odometry contacts, CoFL-S, G2-Nav, action-relevant latents). Program guide: 139 takeaways (was 108). Curated 901. Local: validate 0 errors, 1,026 pages, 0 broken links.
- Launch kit CoRL post numbers refreshed (181 with code, 83% on arXiv, 41% of orals/spotlights with code, 139 takeaways).
- Verify #159 passed (31 CoRL entries, titles, links). Dispatched intake by hand at 05:15 (no scheduled slot had fired); 11-06 feed landed (81 new papers in the feed).
- 11 picks from the 11-06 feed: SLA, La-JEPA, Concertina, GPWM, Social Humanoid (CoRL), MessyNav (CoRL), HITCH, Spatial-UMI-Dream, VLA-Tug, MOMASPLAT (UT Austin), Latent RL Priors. La-JEPA's repo README is 404 from raw.githubusercontent, so no code link yet. Skipped: NegWAM (driving), USB Gym (medical), sEMG rehab, NTT Structure from Collision, LARBRID (code URL without host). Curated 912.
- Dispatched `facts.yml` for 30 more CoRL 2026 papers with project pages.
- Verify #160 failed on SLA's project page (https://SLA.github.io/ is a 404 placeholder from the arXiv comment); line removed, code link stays.
- 30 more CoRL 2026 entries from the second facts run (papers with project pages): REACT, AWLS, score decorrelation, GR-BC, HiFun, SCRIM, Box-WAM, MIRROR, PAF, SGS, DepthWorld, RMMBench, FreeLoc, TacEx, DILL, SCOUT, RoboFFT, LiMA, HiRE, GLIDE, VLA-Feedback, ProxiDex, MessyMem, GeomVLA, FoldNet++, in-hand assembly, FOCI, SkillX, AnyWorld, SOLO. Program guide: 169 takeaways. Curated 942.
- Slip: commit eb75ed5 went out with one validate error (GLIDE project link was http://, from the arXiv comment); I chained the push after `validate.py | tail` without checking its exit. Fixed in f896630 a minute later (https works). Rule for next runs: run `validate.py` with `set -o pipefail` or read its count before pushing.
- End: 2 stars / 0 forks / 0 open issues. Verify #161 still running after 40+ minutes and #162 pending at the end of this run, so the 30 CoRL entries of batch 2 and the GLIDE https link are not CI-checked yet; next run checks them. No new owner task; the CoRL post in the launch kit (now 169 takeaways) still fits until Sun 11-08; Search Console still open. End of run 62.
- Owner request (chat): new home layout. Header search box on every page, new 'Search / 搜索' tab (`search.html`) between Home and Daily arXiv, hero headline removed (kept as hidden h1), trending lists first in three columns, star box and header ★ Star button (count from repo_stats once the stats job runs). Legacy `index.html?q=` links forward to `search.html`. Browser test at 1440/1280/390 px, zh/en, light/dark: no JS errors, no horizontal scroll, header submit and legacy redirect work. See DECISIONS.
- Owner follow-up (chat): trending boxes back to 10 rows each but 250 px tall with their own scrollbar; badges (▲ 153, +41, ★) set to nowrap so the arrow never splits from its number; header height 57 → 35 px (about 0.6x). Checked at 1640 and 390 px: no JS errors, no horizontal scroll, no badge split across lines. The star button now shows the live count (2).
- Owner follow-up 2 (chat): owner's screenshot still showed the old CSS (browser cache: style.css had no version), so assets now load as `style.css?v=<hash>` / `app.js?v=<hash>` (hash of their content, changes on every CSS/JS edit). Trending boxes shorter (list 170 px, about 1/3 of before, scroll for all 10), description clamped to one line, ▲/★ badges use a non-breaking space and the star count + weekly gain stay together.
- Owner follow-up 3 (chat): smaller secondary text in the trending boxes (descriptions 11.5 px, sub-lines 12 px, star/gain badges 11 px, 'all repos' link 12.5 px); entries stay 13.5 px.
- Owner follow-up 4 (chat): removed the 'All N repos' link under the most-starred box; the code tracker stays reachable from the 'Code / 代码' nav tab.
- Owner follow-up 5 (chat): removed the description line under 'Newly added picks / 最新精选' on the home page.
- Owner follow-up 6 (chat): the home star box became a banner under the header on every page (sticks with the header on desktop), owner's playful wording: '本项目大量由 Claude 整理维护，点个 Star 给克劳德大小姐鼓励一下！' with '★ 投喂 Star' and a close button '拒绝投喂，换蓝色大肥鲸 ✕' (EN: 'Feed a star' / 'No thanks ✕'). Closing or clicking Star hides it for good in that browser (localStorage 'starbar', set before first paint so it does not flash). Tested at 1440/1280/390 px: no JS errors, no horizontal scroll, close works and stays closed on other pages.
- Owner follow-up 7 (chat): the reading-path and search links are now two outlined buttons on the right of the 'Newly added picks / 最新精选' heading row (wrap under it on phones).
- Owner follow-up 8 (chat): stats row shrunk to three small chips (curated · new this week · latest intake) on the right of the CoRL link row; the 'topics' stat removed. Checked at 1440/1280/390 px.
- Owner follow-up 9 (chat): header star button restyled as a GitHub-style button (GitHub mark from Primer Octicons, MIT; 'Star' + count linking to stargazers), light and dark variants; pure HTML/CSS, no GitHub widget script.
- Owner follow-up 10 (chat): gold star icon (Octicons star-fill, MIT) added next to 'Star' in the header GitHub button.
- Owner follow-up 11 (chat): search page shows the 12 topic tiles under the search box ('按主题浏览'); a tile opens search.html?topic=<id> (filtered results), tiles hide once a search or filter is active. Topic pages stay linked ('全部主题 →').
- Owner follow-up 12 (chat): the nav tab of the current section gets a highlighted box (accent border + background, aria-current=page): Home, Search, Daily arXiv (incl. day pages), Topics (topic pages), Code, Weekly (digests), Learn (resources + reading path). Entry, venue, lab and robot pages highlight nothing.
- Owner follow-up 13 (chat): tab landing pages (search, daily arXiv + day pages, topics index, code, weekly index, resources) no longer show the big title and intro line; titles kept as hidden h1 for screen readers/SEO. Code page keeps the small license note, now below the filters. Topic, venue, lab, robot and entry pages keep their titles (they carry the page's subject).
- Owner request (chat): commits now authored by hu-zlatan (GitHub no-reply email) with Claude as co-author; directive added to AUTOPILOT.md. Past commits unchanged (no history rewrites).
- Owner request (chat): star rating ★★★/★★/★ replaces the highlight flag (one ★★★ per topic). 12 ★★★, 27 ★★, 143 ★ after migration. Site: rating badges, topic pages grouped by rating, home editor's picks; README ⭐⭐⭐/⭐⭐/⭐ with rated entries first; CONTRIBUTING documents the levels. See DECISIONS.
- Owner question (chat): one-click daily paper pack for Zotero. Built it: per-day BibTeX (all / with code) with topics as tags and code links as notes, plus an import how-to that also points to the Atom feeds (Zotero can subscribe). Parsed all 36 day files with bibtexparser: 2,057 entries, no duplicate keys. No PDFs in the pack.
- Owner follow-up (chat): only the picks matter. Dropped the per-day feed packs; one small button beside '最新精选' downloads the newest day's picks as BibTeX (72 entries on 11-06, all parsed, unique keys), with takeaways as Zotero notes and topics/rating as tags.
- Owner request (chat): colour system: softer palette, green filled download button, per-topic hues on tiles and chips, coloured trending boxes, gold star banner. Checked light/dark at 1280 px: no JS errors.
- Owner request (chat): visual polish. Fixed weekly digest rendering (blockquote intro showed raw '>' and *italics* asterisks; md_to_html now renders blockquotes and CJK-safe italics). Cards: dark titles with blue hover, hover lift, lighter free-form tags, longer line height; section headings get an accent bar; trending lists fade at the bottom to hint scrolling; feed page links became buttons; phone nav stays on one swipeable line; visible keyboard focus.

## 2026-11-06 — run 63 (~10:50 UTC–)

- Start: no issues/PRs, 2 stars / 0 forks. All workflows green; verify #161 failed only on the GLIDE http link (fixed in #162), #163 passed on the rating migration.
- CoRL week prep, batch 3: listed CoRL program arXiv papers not curated with a project link (feed `project`, venue_papers, hf `project`) and no code: 170. Ran `facts.yml` for 30 and wrote takeaways from the abstracts (LoHo-Manip, R^3, AFP, Learning to Assist, X-Tokenizer, GeoProp, TRACE, S2, ABC-130K, UMA, MemoryVAM, SafeMem, HARP-VLA, TouchSafeBench, knife peeling, LWD, SocialNav-SUB, Memory Anchors, CHORUS, TBD-VLA, generative 3D worlds for VLA RL, BiCICLe, InCoM, PAKT, UniIntervene, Robo-ValueRL, MoSS, RoboPocket, PAM, OmniGuide). Skipped one rover paper. Local: validate 0 errors (pipefail), README check clean, 1,099 pages, 0 broken links. Program guide 199 takeaways. Curated 972.
- Dispatched `facts.yml` for the next 30 (queued behind verify in the arxiv-api group).
- Verify #164 passed batch 3. Batch 4 from the second facts run: FOSA, AIDA-OWMM, ASIMOV v2, SimHum, SCoDA, WANDA, SafeStreamingFlow, diffusion IK geometry, A4D, VoLo, ENPIRE, LEMCA, Roken, SIDO, OptiGeo, Flow Control, CoSMO, CLAP, CoStream, Language as a Sensor, NovaPlan, Token Steering, SentryVLA, DAM-VLA, PanoVine (hardware), DiscreteRTC, X-NavDP, CoopUQ, Armory, CERT-Replan. Validate 0 errors, 1,129 pages, 0 broken links. Program guide 229 takeaways; launch kit counts updated. Curated 1,002.
- Dispatched `facts.yml` for batch 5 (CounterAlign … UniVTAC).
- Verify #165 passed batch 4. Batch 5: FAR, S2A2, HelpMeOut, RoboReel, VLA SAEs, Multi-GraspLLM, SILO, EgoEngine, PRISM (polynomial features), UniVTAC, HUGS, FingerViP, Grasps to Dexterity, Transformer Transformer, Instant-Fold, PhysCoRe, Robot-WATCHDOG, VLA redirection attacks, CounterAlign, HiPHI, continual 6-DoF grasping, GeoAlign, DiffMorphGrasp, VLA-FAIL, EgoWAM, UCA-Flow, Imitator Game, IMBench, Wiggle and Go!, ReSYNC. Validate 0 errors, 1,159 pages, 0 broken links. Program guide 259; curated 1,032.
- Dispatched `facts.yml` for the next 30 (tactile, humanoid, world models).
- Verify #166 passed batch 5. Batch 6 (29): OmniTacTune, PlayWorld, tau0-WM, Humanoid Hanoi, PTLD, ContactMimic, FM-VLA, LEGS, ExtremControl, MiTaS (http→https project link, caught by validate before push), WoVR, TacCoRL, VLK, FTP-1, VISTA, Pri4R, HumanoidMimicGen, WT-UMI, AirVLA, FACT, coupled world models, HTT, HEFT, Current as Touch, HWM, ConstrainedMimic, AdaPT tennis, ViTaL, RoFacto. Skipped OptCar (off-road vehicle MPC). Program guide 288; curated 1,061.
- Dispatched `facts.yml` for batch 7 (human video, data generation, dexterous).
- Verify #167 passed batch 6. Batch 7 (30): Ambient Diffusion Policy, UME, K-UBM, RoboAug, Cue the Flow, Do as I Do, WARP-RM, GenAN, STRIPS-WM, RoboSnap, DAP, ComSim, REGRIND, WARP retargeting, object-centric residual RL, UniLab, Dexterity-BEV, RoboLineage, GLAM, TeleDexter, ADEPT, LUCID, ActiveMimic, SynthICL, Human2Any, YUBI, SimFoundry, FPL, Dex4D, FlowDPG. Program guide 318; curated 1,091.
- My skip filter for driving papers matched 'Driven' in five robotics titles (RoboGene, tendon-driven continuum robots, AURORA, TextOp, ADAPT); they go into the final facts batch with the last 12.
- Verify on batch 7 queued. Batch 8 (final 17 with project pages): tendon continuum robots in MuJoCo, TextOp, AURORA, EgoHTR, RoboGene, AssemLM, WHIRL, TDC, MuSe, TEXEDO, ForceBand, T-Rex, reflex-shaped grasp demos, tactile object-centric context, ADAPT, FADA, ControlTac. Program guide 335 takeaways of 567 CoRL papers on arXiv; curated 1,108. Launch kit CoRL post numbers updated (335).
- Batch 9 (first 30 CoRL papers with neither code nor project page, arXiv link only): Coarse-to-Control, AI coaching, HARBOR, FocusPool, M3P-R1, NAC, Mixture of Frames, MotionVLA, Chameleon, MERL, CoRE-VLA, GENESIS-Handover, SlotFlow, EXPO-FT, PACT, ARMS, ActionCodec, COOL, AC-LAM, ThinkProprio, solo-demo box pushing, workspace tokens, Eye Robot, RARM, targeted active preference learning, ThinkingVLA, IMPLIED, FlowVLA, TIGER, LifelongVLA. No links added from anonymous code or company news pages. Validate 0 errors, 1,265 pages, 0 broken links. Program guide 365; curated 1,138; launch kit counts updated.
- End: 2 stars / 0 forks / 0 open issues / 0 PRs. Verify #164–#169 all passed this run. No new owner task; CoRL post in the launch kit (now 365 takeaways) fits until Sun 11-08; Search Console still open. End of run 63.

## 2026-11-06 — run 64 (~16:50 UTC–)

- Start: no issues/PRs, 2 stars / 0 forks. Verify #170 passed run 63's last batch. Deploy #861 failed on a Pages sync timeout (transient; #862/#863 passed).
- 5 more picks from the 11-06 feed (candidates.json abstracts): RoboImagine → world-models, S2C (NeurIPS 2026) → manipulation, LARBRID (NeurIPS 2026) → learning, world-model-guided social navigation (NeurIPS 2026) → navigation, FAH → perception. LARBRID repo named in the abstract was not checked, so no code link.
- CoRL batch 10 (30, facts.yml): PIGEON … PROSE. G2G gets its code link (repo live, 24★). Validate 0 errors, 1,300 pages, 0 broken links. Program guide 395; curated 1,173.
- Verify #171 passed the 5 picks; #172 was cancelled in the arxiv-api group by the facts dispatch (verify checks all entries, so #173 covers batch 10).
- CoRL batch 11 (30): ELASTIC … SFIHILO (real-time/async VLAs, steering, safe control). Titles diffed against facts.json: all match. Validate 0 errors, 1,330 pages, 0 broken links. Program guide 427; curated 1,203.
- Verify #173 passed batches 10–11. CoRL batch 12 (30): ReTVL … AutoDex (policy evaluation, mixed-quality data, dexterity, touch); titles now taken straight from facts.json. Validate 0 errors, 1,360 pages, 0 broken links. Program guide 457; curated 1,233.
- facts run #19 was cancelled by a scheduled intake joining the arxiv-api group (pending → cancelled); re-dispatched. Deploys #875/#876 failed with 'Deployment failed, try again later' (GitHub side; the live site keeps the last good deploy).
- CoRL batch 13 (30): MotionDisco … VisionSIM (humanoid whole-body control and loco-manipulation, aerial robots, world-action models). Validate 0 errors, 1,390 pages, 0 broken links. Program guide 487; curated 1,263.
- Verify #174 passed batch 12. CoRL batch 14 (29): OTQL … C³ache, AdvDex (data generation, UMI/exoskeleton hardware, world-model safety and speed). Skipped the self-play driving paper. Validate 0 errors, 1,419 pages, 0 broken links. Program guide 516 of 572; curated 1,292. Launch kit CoRL post updated to 516 takeaways.
- End: 2 stars / 0 forks / 0 open issues / 0 PRs. Verify #175 (batch 13) was running at the end; batch 14's verify queued. No new owner task. End of run 64.

## 2026-11-06 — run 65 (~19:30 UTC–)

- Start: no issues/PRs, 2 stars / 0 forks. Verify #175 and #176 passed batches 13–14.
- Listed the last CoRL 2026 arXiv papers without takeaways: 56, of which 19 are driving/vehicle/rover/surgical/rehabilitation/parking (skipped, incl. To Route or to Adapt?, self-play driving, off-road dynamics, CoPark). Dispatched `facts.yml` for the remaining 37 (batch 15: grippers, tactile, contact-rich, quadruped and humanoid locomotion).
- Batch 15 (37, facts.yml abstracts): Belt-Finger, SE(3) dynamic-grasp forecasting, How Firm Should a Grasp Be?, PACER, Touch2Trace, SlipSense, Robot-DIFT, CompVLA, DexFLEX, Mind the Gap (EC2C), KlaskTron-IL, Hardware-as-Regularization, Uni-Mo/Quad-Imaginarium (no code link: earlier README said 'coming soon'), MorFiC, QWM, LoComposition, HumoSlope, RPL, Echo in the Steps, MeshMimic, Perceptive BFM, MARCH, CAP, RoboDreamer, HAF-VLA, CLIFT, ADAPT (disturbance observer), Walk Like This, Koopman DCM, actuator dynamics curricula, TACL, SHOES, Mind the Phase, Push the Limit, λ-Reachability, MPC-Injection, VIGOR-MPC. Validate 0 errors, 1,456 pages, 0 broken links. Program guide 553 of 572 CoRL papers on arXiv (the other 19 are driving/vehicle/rover/surgical/rehabilitation/parking, skipped on purpose); curated 1,329. Launch kit counts updated.
- End: 2 stars / 0 forks / 0 open issues / 0 PRs. Deploy #884 passed; #885 (batch 15) queued; verify on 55551ed queued. No new owner task. End of run 65.

## 2026-11-07 — run 66 (~04:45 UTC–)

- Start: no issues/PRs, 2 stars / 0 forks. Verify #177 (batch 15) failed only on https://waltstephen.github.io/captain/ (404); dropped that `project:` line (code repo stays, 86★). Commit 3b0cfb4.
- `project_code.json` `curated` had 100 curated entries without `code:` whose project pages point to a checked repo (most from the CoRL batches of runs 63–65). Reviewed by hand: name match with paper or project page, plus raw READMEs for the 11 unclear ones and a 'coming soon' scan of all 95. Applied 95 (commit 9281936); skipped CANVAS, 2507.01925, TARC (as before), ExtremControl → Genesis-Humanoid, PlayWorld → open-world. Partial releases kept (AssemLM, SimFoundry, YUBI 'under construction' but code present). Curated with code 567 → 662.
- PrimeSim `code:` added (README now has install, configs, HF weights). VLALagBench and vla-start-suppression READMEs still 404.
- Validate 0 errors, 1,456 pages, 0 broken links, README check clean. Verify #180 pending at the end. No new owner task. End of run 66.

## 2026-11-07 — run 67 (~10:50 UTC–)

- Start: no issues/PRs, 2 stars / 0 forks. Verify #180 failed only on https://arielchen07.github.io/behavior-spatial/ (404) → `project:` dropped (commit 1169344). #178 had failed on the same page.
- SLA (2611.08373): project page https://embodiedsla.github.io/ from its HF paper page (curated_link_updates). Other link updates stay skipped (awesome lists of surveys, CaPtain 404, RoboColosseum 401, HexaShell homepage).
- Deploy #898 failed after 10 min in 'syncing_files' (like #861) → `actions/deploy-pages` timeout 30 min. Workflow push accepted.
- `corl_program.py`: unmatched program papers are re-searched on arXiv every 3 days (was 7) during CoRL week.
- candidates.json: 33 uncurated left, all off-core (driving, surgical, aerial, rehab); nothing picked. Validate 0 errors, README check clean. Verify #181/#182 running at the end. No new owner task. End of run 67.

## 2026-11-07 — run 68 (~16:50 UTC–)

- Start: no issues/PRs, 2 stars / 0 forks. Verify #181 and #182 passed (BEHAVIOR-Spatial fix, SLA project page). Deploys since run 67 all green.
- CoRL program run (15:13 UTC) matched 2 more accepted papers to arXiv (572 → 574). facts.yml #23 (dispatched while an idle Saturday intake was queued) gave full abstracts; added MAESTRO (UPenn, code penn-pal-lab/maestro, 9★, MIT) → vla and AnyDexRT (SJTU, project page) → manipulation. Commit 5e12a54. Program guide: 555 takeaways; the other 19 program arXiv papers are driving/rover/vehicle/surgical/rehab/parking and stay skipped.
- Rechecked waiting code links: VLALagBench and zebehn/vla-start-suppression READMEs still 404; OpenNWM already linked. `project_code.json` `curated` has only the known skips.
- QA: local build, program page on iPhone 13 with mocked clocks (11-07, 11-09 13:00Z, 11-10 16:05Z): no JS errors, no overflow, Now/Next bar correct.
- LAUNCH_KIT CoRL post: numbers updated to 183 with code / 555 takeaways.
- Validate 0 errors, 1,458 pages, 0 broken links, README check clean. No new owner task. End of run 68.

## 2026-11-07 — run 69 (~22:50 UTC–)

- Start: no issues/PRs, 2 stars / 0 forks. Local clone's `main` was stale and diverged; reset to `origin/main` (nothing local was lost; no push of the stale branch).
- Verify #183 (run 68 picks) failed only on https://umishra.me/TAMPAgent/ (HTTP 404); web search found no new page → `project:` dropped (commit b2a9d0b). That commit forgot to regenerate lists/manipulation*.md; fixed in the next commit (a7edf66) before CI flagged it.
- Search index: curated items no longer carry null/empty fields, and `l` is omitted when it equals the arXiv abs URL (app.js rebuilds it). 2.06 MB → 1.96 MB raw (663 → 652 KB gzip). Search checked in Chromium: RT-1 query renders, title links correct, no JS errors.
- Validate 0 errors, 1,458 pages, 0 broken links, README check clean. No new owner task. End of run 69.

## 2026-11-08 — run 70 (~04:55 UTC–)

- Start: no issues/PRs, 2 stars / 0 forks. Local `main` was stale again; reset to `origin/main`. All workflows green; verify #184 (TAMPAgent fix) passed.
- AnyDexRT: `project_code.json` offered chenxi-wang/anydexrt; README has setup, data collection, training and inference → `code:` added (commit 00f4aad). Other `curated` items are the known skips. VLALagBench / vla-start-suppression READMEs still 404.
- Picks from review_queue.json (full abstracts): VFlash (2611.08449, NVIDIA, 99 HF upvotes → rating 1) → vla; DreamFree (2611.04527, KAIST AI, project page) → world-models (commit 6c986d8). Validate 0 errors, 1,460 pages, 0 broken links, README check clean.
- LAUNCH_KIT CoRL post: wording changed from 'next week' to 'this week (Nov 9–12)' so it still fits during the conference.
- No new owner task. End of run 70.
- Owner asked (chat) for hosting reachable from mainland China. Added an optional EdgeOne Makers mirror step to pages.yml (commit 780d440); owner created the token; dispatched Deploy site #932: 'Deploy Success', https://embodied-ai-radar-0r3mxbrd.edgeone.dev, overseas area. Custom domain pending (owner).

## 2026-11-08 — run 71 (~10:50 UTC–)

- Start: no issues/PRs, 2 stars / 0 forks. Local `main` stale again; reset to `origin/main`. All workflows green; verify #185/#186 (AnyDexRT code, VFlash/DreamFree) passed.
- No new feed day (Sunday) and the HF queue holds only known skips, so worked on the W45 digest ahead of CoRL (opens Mon 11-09).
- `make_digest.py`: picks whose arXiv ID is older than the previous month (index anchors, CoRL program takeaways) are no longer ranked as 'Editor's picks'; a new 'Also added to the index' section counts them per topic and links the CoRL program guide. W45: 218 picks + 565 earlier papers (445 from the CoRL guide). Digest 108 KB → 53 KB.
- digest/2026-W45.md generated and given a bilingual intro (AIRoA-0, Open-HumanWAM, HALO; RoboColosseum, SimuGuard; uni-robot-agent, CaPtain, PyRUA; CoRL guide 687 papers / 555 takeaways). Commit 70e8d7f. Validate 0 errors, 1,461 pages, 0 broken links, README check clean.
- EdgeOne mirror: docs say preview links expire after 3 h and only the newest three deployments stay live (older ones 401). Added a one-minute check to OWNER_TODO before the mirror gets linked publicly.
- End of run 71.

## 2026-11-08 — run 72 (~16:50 UTC–)

- Start: no issues/PRs, 3 stars (+1) / 0 forks. Local `main` stale; reset to `origin/main`. All workflows green (intake, repo stats, CoRL program, deploys).
- Checked for new work: CoRL program runs 11-08 changed only `checked` dates (no new arXiv matches); `project_code.json` `curated` offers only the 5 known skips; HF review queue only known skips. No new feed until Mon 11-09.
- Local validate 0 errors, 1,461 pages, 0 broken links, README check clean. No changes to data or site (avoiding churn). No new owner task. End of run 72.

## 2026-11-08 — run 73 (~22:50 UTC)

- Start: no issues/PRs, 3 stars / 0 forks. Local `main` stale; reset to `origin/main`. All workflows green (deploys #950–#952, repo stats #326–#327, intake #159–#160, IndexNow #7).
- No new feed (next arXiv announcement Sun 20:00 ET = Mon ~01:00 UTC); since run 72 only bot stats commits. Validate 0 errors (1,333 curated, 1,757 feed), README check clean. No data or site changes (no churn). End of run 73.

## 2026-11-09 — run 74 (~04:52 UTC–)

- Start: no issues/PRs, 3 stars / 0 forks. Local `main` was detached/stale; reset to `origin/main`. All workflows green.
- The 01:11/02:17/04:53 intake slots had not fired; dispatched intake by hand (#161, success): 11-09 feed day in, 16 new candidates.
- 12 picks from candidates.json abstracts (commit 23dbb74): On Agentic Manipulation Policies / AMP1 (Apple, rating 1), PRISM (NeurIPS 2026), Computer-Use Agents Are Embodied Generalists (CMU), DobotTrack → vla; DKWBC (Robbyant, ZJU), SUGARv2 → locomotion; Grasp-TAGS (UMN), grasp-feasibility counterfactual audit (WACV 2027, code) → manipulation; ToolDex, Flex-RSI → datasets; RevoSim (BrainCo) → tactile; Lodos (Tübingen, code; v2 noted in takeaway) → sim. Code repos checked via GitHub search + README; Dobot-Team/dobot_track not public → no code link.
- Validate 0 errors (1,345 curated, 1,812 feed), 1,474 pages, 0 broken links, README check clean. HF queue: only known skips. No new owner task. End of run 74.

## 2026-11-09 — run 75 (~10:50 UTC–)

- Start: no issues/PRs, 3 stars / 0 forks. Local `main` stale/diverged; reset to `origin/main`. Intake #162/#163 and deploys green; verify #187 (run-74 picks) had been cancelled, so verify was dispatched again (#188).
- `project_code.json` `curated` offered repos for 6 of the run-74 picks. Checked READMEs from the shell: AMP1, CUA-embodied, RevoSim, Flex-RSI name their papers → `code:` added (commit f1f9ce3). DKWBC repo holds only the project page → skipped. Validate 0 errors, 1,474 pages built, README check clean.
- CoRL program: still 574 of 687 on arXiv, uncurated ones are the 19 known skips. Awards page on 2026.corl.org not readable (4xx), no finalists announced on home/announcements; retry later this week.
- No new owner task. End of run 75.

## 2026-11-09 — run 76 (~16:45 UTC–)

- Start: no issues/PRs, 3 stars / 0 forks. Local `main` stale; reset to `origin/main`.
- Verify #189 (run-75 code links) and scheduled #190 failed on one item only: arXiv retitled STAR 2610.41009 to 'STAR: Steering Action Representations with Proprioception for VLA Inference'. Title fixed + READMEs rebuilt (42bc3c3); verify #191 passed. The URLError warnings (qwen blog, UMass 3DVLA) are warnings only and recur; leave them.
- facts.yml #24 fetched the v2 abstract: it adds proprioception-adaptive mixing strength → EN/ZH takeaway updated (EN 204 chars).
- Link-update queue, project_code `curated` and HF queue: only known skips. Web search found no CoRL 2026 award finalist list yet.
- Validate 0 errors, 1,474 pages, 0 broken links, README check clean. No new owner task. End of run 76.

## 2026-11-09 — run 77 (~22:50 UTC–)

- Start: no issues/PRs, 3 stars / 0 forks. Local `main` was detached; reset to `origin/main`. All workflows green; verify #192 (run-76 takeaway) passed.
- CoRL program run (18:53) matched 2 more accepted papers to arXiv (576 of 687). facts.yml dispatched for both; takeaways written from the full abstracts: Q-OIL (UW, human-intervention RL, project page) → learning; MDF++ (visuo-tactile world-action model, Berenson lab) → tactile (+ world-models, manipulation).
- Web search: still no CoRL 2026 award finalist list.
- Validate 0 errors (1,347 curated), 1,476 pages, 0 broken links, README check clean. No new owner task. End of run 77.

## 2026-11-10 — owner chat (~00:10 UTC)

- Owner registered `embodied-ai-radar.com` for the China mirror and asked how to bind it. Sent EdgeOne custom-domain steps (docs: pages.edgeone.ai/document/custom-domain, domain-overview: no ICP filing needed in the area excluding mainland). OWNER_TODO updated. Canonical URLs stay on GitHub Pages (SITE_URL unchanged), so the mirror does not split search ranking. Once the owner confirms the domain loads, add the mirror link to READMEs/home.
- Owner bound `embodied-ai-radar.com` + www in EdgeOne (DNSPod CNAME, free certificates) and confirmed the site loads. Added the mirror link to both READMEs and a footer line on every page (`MIRROR_URL`, same path on both hosts). Canonical stays GitHub Pages. Validate 0 errors, 1,476 pages, 0 broken links, README check clean.
- Owner feedback: no footer line (people on the site can already reach it); instead the Chinese README should use the new address. Footer line and English README line removed; README.zh-CN.md main link and all its site links → https://embodied-ai-radar.com/, `SITE_ZH` in build_readme.py for the zh topic lists. README check clean, 0 broken links.
