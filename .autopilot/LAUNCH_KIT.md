# Launch kit

Ready-to-post texts. **The owner decides whether, where and when to post** — the agent never posts. Post each one once, in the place where it fits the community's rules (self-promotion rules differ: read them first). Every text says plainly that the project is maintained by an AI agent.

Status: draft v1 (2026-10-19), V2EX text updated 2026-10-21 (BibTeX, entry pages, GitHub stars); 知乎/小红书 updated 2026-10-22 with the reading path (start.html). 2026-10-23: V2EX/Reddit mention per-conference pages; CoRL 2026 (Nov 9–12, Austin) is a natural moment to post. Best posted after the daily feed has a few days of data and the first weekly digest exists (next Monday).

Links:
- Site: https://hu-zlatan.github.io/embodied-ai-radar/ (中文: append `?lang=zh`)
- Repo: https://github.com/hu-zlatan/embodied-ai-radar

---

## V2EX（节点：分享创造）

**标题：** 做了一个中英双语的具身智能雷达：精选论文 + 每天自动收录 arXiv 机器人新论文

正文：

最近在跟具身智能 / 机器人学习方向，发现现有的 awesome list 要么很久不更新，要么只是每日 arXiv 列表、没有筛选。于是做了个小网站：

- 精选索引：VLA、操作与灵巧手、触觉、人形与足式、世界模型、导航、感知与 SLAM、规划控制与安全、强化学习与模仿学习、仿真与 sim-to-real、数据集、开源硬件 12 个主题，每条都有中英文一句话要点，arXiv 编号和链接由 CI 自动核验
- 每日 arXiv：GitHub Actions 每天抓 cs.RO 以及 CV/LG/AI/CL 里的机器人论文，按主题和机器人形态（机械臂/灵巧手/人形/四足/无人机…）自动标注，可筛选"有代码"，并从作者备注中识别已接收的会议，并按会议汇总成页面（如 CoRL 2026：https://hu-zlatan.github.io/embodied-ai-radar/venues/corl-2026.html?lang=zh）
- 纯静态站，搜索即时（可直接用中文关键词搜英文论文，如“人形 强化学习”“触觉”），手机可用，支持 EN/中文 切换，有 Atom 订阅
- 每篇论文一键复制 BibTeX；每个精选条目有独立可分享页面（如 LEAP Hand：https://hu-zlatan.github.io/embodied-ai-radar/e/arxiv-2309.06440.html ）；显示各开源代码的 GitHub 星标

一个说明：这个仓库是由 AI 智能体（Claude）按计划自动维护的，我负责方向和监督，所有数据都要通过核验，不编造。欢迎提 issue 推荐论文或指出错误。

网站：https://hu-zlatan.github.io/embodied-ai-radar/?lang=zh
GitHub：https://github.com/hu-zlatan/embodied-ai-radar

---

## 知乎（文章或回答"具身智能入门有哪些资料"类问题）

**标题：** 一个每天更新的具身智能论文地图（中英双语，开源）

具身智能这两年论文增长很快，从 RT-2、OpenVLA、π0 到各种人形机器人全身控制，单靠收藏夹很难跟上。我整理了一个开源项目「具身智能雷达」：

1. **精选索引**：按 12 个主题整理里程碑与近期重要工作（论文、代码、数据集、仿真器、硬件），每条配中英文一句话要点，标注是否开源、真机/仿真等；
2. **每日 arXiv**：每天自动收录 cs.RO 及相关方向新论文并按主题标注，可以只看有代码的；
3. **每周精选**：每周一自动生成双语周报。

入门建议看网站上的「入门路线」页：10 个阶段、41 个精选条目，从 PPO/SAC、DAgger 等基础，到 Diffusion Policy / ACT、Open X-Embodiment / LeRobot、RT-2 → OpenVLA → π0、MuJoCo / Isaac Lab、足式与人形运动控制、世界模型，最后是 SO-101、GELLO、LEAP Hand 这类可以自己动手搭的硬件。每条都有中英文要点和代码链接：https://hu-zlatan.github.io/embodied-ai-radar/start.html?lang=zh

项目由 AI 智能体在人工监督下维护，代码 MIT、数据 CC BY 4.0，欢迎补充和纠错。

https://hu-zlatan.github.io/embodied-ai-radar/?lang=zh

---

## 小红书

**标题：** 具身智能论文太多看不过来？这个双语网站每天帮你筛 🤖

正文：
📡 具身智能雷达｜开源免费
✅ 12 大主题精选：VLA、灵巧手、触觉、人形机器人、世界模型、SLAM、仿真……
✅ 每条论文都有中文一句话总结
✅ 每天自动收录 arXiv 机器人新论文，能筛"有代码"的
✅ 每周一出双语周报
✅ 新手「入门路线」：10 个阶段、41 篇必读，从强化学习基础到 VLA、人形机器人和可自己搭的硬件
适合：机器人/具身智能方向的研究生、工程师、想入门的同学
（项目由 AI 智能体维护、人工监督）
🔗 hu-zlatan.github.io/embodied-ai-radar
#具身智能 #机器人 #人工智能 #论文阅读 #研究生 #VLA

---

## Reddit — r/robotics (check the sub's self-promotion rules; a weekly "showcase" thread may be the right place)

**Title:** I made a bilingual, auto-updating map of embodied AI / robot learning papers (verified links, daily arXiv feed)

Body:

Embodied AI Radar is a free, open-source site that tries to fix two things that bug me about paper lists: they go stale, and daily arXiv dumps are unfiltered.

- A curated index across 12 topics (VLA & foundation models, manipulation, tactile, locomotion & humanoids, world models, navigation, perception & SLAM, planning/control & safety, RL & imitation learning, sim-to-real, datasets, open hardware). Each entry has a one-line takeaway; CI checks every arXiv ID against arXiv and every link weekly.
- A daily feed of new cs.RO papers (plus robotics papers cross-listed from CV/LG/AI/CL), auto-tagged by topic and robot type (arm, hand, humanoid, legged, drone…), with venue badges parsed from author comments and a page per conference (e.g. CoRL 2026: https://hu-zlatan.github.io/embodied-ai-radar/venues/corl-2026.html), filterable by "has code", with Atom feeds per topic.
- English and Chinese throughout.

Transparency: the repo is maintained by an AI agent (Claude) on a schedule, with a human owner setting direction. Feedback and suggestions very welcome — especially what's missing.

Site: https://hu-zlatan.github.io/embodied-ai-radar/ · Code (MIT): https://github.com/hu-zlatan/embodied-ai-radar

---

## Hacker News (Show HN)

**Title:** Show HN: Embodied AI Radar – a self-updating, verified map of robot-learning research

Text:

This is a static site plus a few GitHub Actions: every day it pulls new robotics papers from arXiv, tags them by topic with simple keyword rules, and rebuilds the site. A small curated index (100+ entries to start) sits on top, with one-line takeaways in English and Chinese, and a CI job that checks each arXiv ID and link so the list can't silently rot.

An unusual part: the repository is maintained by an AI agent (Claude) that runs on a schedule, reads its own state/log files in the repo, and pushes small increments; a human owner steers it through a charter file. The charter, run log and decisions are all public in the repo.

Stack: YAML data, a few hundred lines of Python (PyYAML is the only dependency), vanilla JS search over one JSON index, no tracking.

https://hu-zlatan.github.io/embodied-ai-radar/

---

## X / Twitter

📡 Embodied AI Radar — a bilingual (EN/中文), self-updating map of robot learning:
• curated VLA, manipulation, tactile, humanoid, world-model, sim2real papers w/ one-line takeaways
• every new arXiv robotics paper, daily, tagged by topic
• verified links, open source, maintained by an AI agent
https://hu-zlatan.github.io/embodied-ai-radar/
