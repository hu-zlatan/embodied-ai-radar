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
