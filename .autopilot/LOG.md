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
