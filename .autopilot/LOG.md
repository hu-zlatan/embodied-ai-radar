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
