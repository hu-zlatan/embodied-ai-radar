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
