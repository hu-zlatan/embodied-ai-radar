# Decisions

Why the project is the way it is. Newest at the bottom. Format: date — decision — why — alternatives considered.

2026-10-19 — **Positioning: a verified, searchable, bilingual radar, not another static list.** — Surveyed existing projects (via web search): big static Markdown lists (TianxingChen/Embodied-AI-Guide, HCPLab-SYSU/Embodied_AI_Paper_List, wadeKeith/Awesome-Embodied-AI, GlimmerLab/Awesome-Embodied-AI-Robot), narrow topic lists (sim2real, continual learning, RL-in-VLA), and daily arXiv dumps (e.g. luohongk/Embodied-AI-Daily). Gaps: lists go stale and are hard to filter; daily dumps have no curation; almost nothing is bilingual at the entry level or searchable by "has code / real robot / topic". We combine (1) a small, hand-verified curated index with EN+中文 one-line takeaways, (2) an automatic daily arXiv feed with rule-based topic tags and code-link detection, (3) a static site with instant search and filters, (4) weekly digests. — Alternatives: a pure awesome-list (crowded), a pure daily feed (no trust signal).

2026-10-19 — **Stack: YAML data + stdlib Python generator + vanilla-JS static site; PyYAML is the only dependency.** — Fast pages, no build toolchain to rot, easy contributions (edit one YAML file). The site loads one JSON index and filters client-side; it is plain HTML so it works without JS for topic pages. — Alternatives: Hugo/Jekyll/Next.js (heavier, more moving parts).

2026-10-19 — **Verification lives in CI.** — The agent's shell cannot reach arXiv or GitHub web pages, so a `verify` workflow checks every curated arXiv ID against the arXiv API (title must match) and every URL for a non-error status. Entries that fail are fixed or removed, never guessed.

2026-10-19 — **arXiv metadata is stored (CC0), abstracts trimmed.** — arXiv metadata, including abstracts, is released under CC0; we keep a trimmed abstract for search and always link the source. Daily files live in `data/arxiv/YYYY/MM-DD.json`.
