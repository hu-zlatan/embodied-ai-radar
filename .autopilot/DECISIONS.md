# Decisions

Why the project is the way it is. Newest at the bottom. Format: date — decision — why — alternatives considered.

2026-10-19 — **Positioning: a verified, searchable, bilingual radar, not another static list.** — Surveyed existing projects (via web search): big static Markdown lists (TianxingChen/Embodied-AI-Guide, HCPLab-SYSU/Embodied_AI_Paper_List, wadeKeith/Awesome-Embodied-AI, GlimmerLab/Awesome-Embodied-AI-Robot), narrow topic lists (sim2real, continual learning, RL-in-VLA), and daily arXiv dumps (e.g. luohongk/Embodied-AI-Daily). Gaps: lists go stale and are hard to filter; daily dumps have no curation; almost nothing is bilingual at the entry level or searchable by "has code / real robot / topic". We combine (1) a small, hand-verified curated index with EN+中文 one-line takeaways, (2) an automatic daily arXiv feed with rule-based topic tags and code-link detection, (3) a static site with instant search and filters, (4) weekly digests. — Alternatives: a pure awesome-list (crowded), a pure daily feed (no trust signal).

2026-10-19 — **Stack: YAML data + stdlib Python generator + vanilla-JS static site; PyYAML is the only dependency.** — Fast pages, no build toolchain to rot, easy contributions (edit one YAML file). The site loads one JSON index and filters client-side; it is plain HTML so it works without JS for topic pages. — Alternatives: Hugo/Jekyll/Next.js (heavier, more moving parts).

2026-10-19 — **Verification lives in CI.** — The agent's shell cannot reach arXiv or GitHub web pages, so a `verify` workflow checks every curated arXiv ID against the arXiv API (title must match) and every URL for a non-error status. Entries that fail are fixed or removed, never guessed.

2026-10-19 — **arXiv metadata is stored (CC0), abstracts trimmed.** — arXiv metadata, including abstracts, is released under CC0; we keep a trimmed abstract for search and always link the source. Daily files live in `data/arxiv/YYYY/MM-DD.json`.

2026-10-19 — **Daily intake reads arXiv RSS first; the export API is only a best-effort backfill.** — The API rate-limits GitHub's shared runner IPs (HTTP 429 on the first two runs); rss.arxiv.org gives the day's new + cross-listed papers with abstracts in one request. — Alternatives: OAI-PMH (same host as the API), third-party mirrors (licensing/trust unclear).

2026-10-19 — **Topic tagging = scored keyword rules, not an ML model.** — Transparent, editable in `topics.yaml`, zero cost, reproducible in CI. Title hit 3, abstract occurrence 1, threshold 2. Cross-listed (non-cs.RO) papers must have a robotics title keyword plus robot context. Curated entries remain the trusted layer.

2026-10-19 — **Agent picks are added to curated YAML with an `added:` date** — makes "what's new" and weekly digest picks automatic; results from new papers are phrased as "reports …" since they are unreviewed claims.

2026-10-19 — **Robot type ("embodiment") is a computed filter, not stored data.** — Keyword rules in `data/embodiments.yaml` run at build time over title+abstract (feed) or title+takeaway+tags (curated); one explicit mention is enough (threshold 1, unlike topics at 2) because naming the robot is a strong signal. Editing the rules re-tags everything on the next build, no data migration. — Alternatives: store per-paper tags in the JSON (needs retag passes), manual tags (doesn't scale).

2026-10-19 — **License files split** — GitHub showed "Other" for a combined MIT + CC BY file; a plain MIT `LICENSE` plus `LICENSE-DATA.md` reads clearly in the sidebar and keeps the same terms.

2026-10-19 — **New topic `learning` (Robot Learning: RL & Imitation).** — Many untagged feed papers were method papers on RL / IL / policy post-training that fit no existing topic (they are not about a specific task like manipulation). A cross-cutting methods topic tags them (untagged 162 → 142 of 451) and gives a home to anchors like PPO, SAC, DAgger, RLPD, SERL, HIL-SERL. Papers may carry it alongside a task topic. — Alternatives: stretch `vla` or `manipulation` keywords (would mis-tag), leave untagged.

2026-10-19 — **`data/resources.yaml` for related lists, courses, docs, communities.** — Newcomers (especially Chinese readers) ask "where do I start"; pointing to other good lists is honest and useful, and positions this radar as complementary. Links are checked by verify.yml like curated data.

2026-10-20 — **BibTeX from arXiv metadata only.** — Researchers copy citations constantly; every arXiv card gets a collapsed BibTeX block (`@misc` with eprint/archivePrefix/primaryClass) plus a copy button, and `curated.bib` bundles all curated papers. Built only from arXiv metadata (CC0): feed records already carry authors (capped at 8 → "and others"); curated authors are cached in `data/arxiv/curated_meta.json` by the intake workflow (only missing IDs are fetched). No venue fields are guessed. Cost: feed page +21% gzipped. — Alternatives: linking to arXiv's export page (endpoint not verifiable from here), Semantic Scholar/DBLP BibTeX (another API, rate limits).

2026-10-21 — **A permalink page per curated entry (`e/<id>.html`).** — The site only had list pages, so a single paper could not be linked or found by search engines (e.g. Chinese queries for a paper name). One small static page per entry (bilingual takeaway, links, BibTeX, related entries, JSON-LD) costs ~11 KB each and no JS. Feed papers do not get pages (hundreds per day, no curated text); they keep day pages. — Alternatives: anchors on topic pages only (already existed, poor for sharing/SEO).

2026-10-21 — **Star history kept in the repo, one snapshot per day, 45 days.** — 'Which repos are rising' is a frequent reason people visit trackers; GitHub does not expose star history cheaply, so we record our own snapshots in the existing stats workflow (one JSON line per day keeps diffs small, ~5 KB/day). Only real snapshots are used; the section stays hidden until 7 days exist.

2026-10-21 — **Curated index exported as `curated.json` + `curated.csv` on the site.** — People who build their own reading lists, dashboards or lab wikis want the data, not HTML; the internal `data/index.json` is a compact search format that may change. The export has stable, documented fields (incl. computed robot types and GitHub stars), CC BY 4.0, and the CSV carries a UTF-8 BOM so Excel shows the Chinese takeaways. Feed papers are not exported (arXiv itself is the better source). — Alternatives: point users at the YAML in the repo (no stars/robot types, needs a YAML parser).

2026-10-22 — **Separate Atom feed for agent picks (`picks.xml`).** — The all-papers feed and per-topic feeds are high-volume; a reader who trusts the curation wants a few items a day with the bilingual takeaway. Built from curated entries with `added:` (newest 60), entry IDs are the stable entry-page URLs so readers never see duplicates. — Alternatives: email newsletter (needs a service and personal data), only the weekly digest (too slow for some).
