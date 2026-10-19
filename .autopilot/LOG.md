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
