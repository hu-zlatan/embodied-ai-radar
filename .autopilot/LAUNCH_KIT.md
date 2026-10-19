# Launch kit

Ready-to-post texts. **The owner decides whether, where and when to post** — the agent never posts. Post each one once, in the place where it fits the community's rules (self-promotion rules differ: read them first). Every text says plainly that the project is maintained by an AI agent.

Status: draft v1 (2026-10-19). Best posted after the daily feed has a few days of data and the first weekly digest exists (next Monday).

Links:
- Site: https://hu-zlatan.github.io/embodied-ai-radar/ (中文: append `?lang=zh`)
- Repo: https://github.com/hu-zlatan/embodied-ai-radar

---

## V2EX（节点：分享创造）

**标题：** 做了一个中英双语的具身智能雷达：精选论文 + 每天自动收录 arXiv 机器人新论文

正文：

最近在跟具身智能 / 机器人学习方向，发现现有的 awesome list 要么很久不更新，要么只是每日 arXiv 列表、没有筛选。于是做了个小网站：

- 精选索引：VLA、操作与灵巧手、触觉、人形与足式、世界模型、导航、仿真与 sim-to-real、数据集、开源硬件 9 个主题，每条都有中英文一句话要点，arXiv 编号和链接由 CI 自动核验
- 每日 arXiv：GitHub Actions 每天抓 cs.RO 以及 CV/LG/AI/CL 里的机器人论文，按主题自动标注，可筛选"有代码"
- 纯静态站，搜索即时，手机可用，支持 EN/中文 切换，有 Atom 订阅

一个说明：这个仓库是由 AI 智能体（Claude）按计划自动维护的，我负责方向和监督，所有数据都要通过核验，不编造。欢迎提 issue 推荐论文或指出错误。

网站：https://hu-zlatan.github.io/embodied-ai-radar/?lang=zh
GitHub：https://github.com/hu-zlatan/embodied-ai-radar

---

## 知乎（文章或回答"具身智能入门有哪些资料"类问题）

**标题：** 一个每天更新的具身智能论文地图（中英双语，开源）

具身智能这两年论文增长很快，从 RT-2、OpenVLA、π0 到各种人形机器人全身控制，单靠收藏夹很难跟上。我整理了一个开源项目「具身智能雷达」：

1. **精选索引**：按 9 个主题整理里程碑与近期重要工作（论文、代码、数据集、仿真器、硬件），每条配中英文一句话要点，标注是否开源、真机/仿真等；
2. **每日 arXiv**：每天自动收录 cs.RO 及相关方向新论文并按主题标注，可以只看有代码的；
3. **每周精选**：每周一自动生成双语周报。

入门建议的阅读顺序（都在网站对应主题页里）：Diffusion Policy / ACT → Open X-Embodiment → Octo / OpenVLA → π0；运动控制方向从 legged_gym 开始。

项目由 AI 智能体在人工监督下维护，代码 MIT、数据 CC BY 4.0，欢迎补充和纠错。

https://hu-zlatan.github.io/embodied-ai-radar/?lang=zh

---

## 小红书

**标题：** 具身智能论文太多看不过来？这个双语网站每天帮你筛 🤖

正文：
📡 具身智能雷达｜开源免费
✅ 9 大主题精选：VLA、灵巧手、触觉、人形机器人、世界模型、仿真……
✅ 每条论文都有中文一句话总结
✅ 每天自动收录 arXiv 机器人新论文，能筛"有代码"的
✅ 每周一出双语周报
适合：机器人/具身智能方向的研究生、工程师、想入门的同学
（项目由 AI 智能体维护、人工监督）
🔗 hu-zlatan.github.io/embodied-ai-radar
#具身智能 #机器人 #人工智能 #论文阅读 #研究生 #VLA

---

## Reddit — r/robotics (check the sub's self-promotion rules; a weekly "showcase" thread may be the right place)

**Title:** I made a bilingual, auto-updating map of embodied AI / robot learning papers (verified links, daily arXiv feed)

Body:

Embodied AI Radar is a free, open-source site that tries to fix two things that bug me about paper lists: they go stale, and daily arXiv dumps are unfiltered.

- A curated index across 9 topics (VLA & foundation models, manipulation, tactile, locomotion & humanoids, world models, navigation, sim-to-real, datasets, open hardware). Each entry has a one-line takeaway; CI checks every arXiv ID against arXiv and every link weekly.
- A daily feed of new cs.RO papers (plus robotics papers cross-listed from CV/LG/AI/CL), auto-tagged by topic, filterable by "has code", with an Atom feed.
- English and Chinese throughout.

Transparency: the repo is maintained by an AI agent (Claude) on a schedule, with a human owner setting direction. Feedback and suggestions very welcome — especially what's missing.

Site: https://hu-zlatan.github.io/embodied-ai-radar/ · Code (MIT): https://github.com/hu-zlatan/embodied-ai-radar

---

## Hacker News (Show HN)

**Title:** Show HN: Embodied AI Radar – a self-updating, verified map of robot-learning research

Text:

This is a static site plus a few GitHub Actions: every day it pulls new robotics papers from arXiv, tags them by topic with simple keyword rules, and rebuilds the site. A small curated index (85 entries to start) sits on top, with one-line takeaways in English and Chinese, and a CI job that checks each arXiv ID and link so the list can't silently rot.

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
