# 具身智能雷达 · Embodied AI Radar

**中英双语（[English](README.md) / 中文）、持续更新的具身智能与机器人学习全景图。**
人工核验的论文、代码、数据集、仿真器与硬件，配一句话要点；外加每天自动抓取并按主题标注的 arXiv 机器人新论文。

### 🌐 [打开网站 → hu-zlatan.github.io/embodied-ai-radar](https://hu-zlatan.github.io/embodied-ai-radar/?lang=zh)

![具身智能雷达网站截图](docs/screenshot.png)

**CoRL 2026（11 月 9–12 日，奥斯汀）：** [会议指南](https://hu-zlatan.github.io/embodied-ai-radar/venues/corl-2026-program.html?lang=zh)按日程与海报编号列出全部 687 篇录用论文，可筛选，附 arXiv 与代码链接，并收录 32 场研讨会。

**刚入门？** 跟着[入门路线](https://hu-zlatan.github.io/embodied-ai-radar/start.html?lang=zh)读：10 个阶段，从强化学习/模仿学习基础，到视觉运动策略、VLA、仿真、足式运动、世界模型，再到可以动手搭建的硬件，共 41 个精选条目，每条都有中英文要点。

## 特点

- **可信**：每个精选条目的 arXiv 编号都会与 arXiv 核对，所有链接每周由 CI 自动检查。
- **新鲜**：GitHub Action 每天抓取 cs.RO 新论文（以及 cs.CV / cs.LG / cs.AI / cs.CL 中的机器人相关论文）并按主题标注，自动出现在网站上。
- **好找**：快速静态网站，支持即时搜索（可直接输入中文关键词，如“人形 强化学习”“触觉”，自动匹配英文论文）与筛选（主题 · 机器人形态：机械臂、灵巧手、人形、足式、无人机… · 已录用会议（CoRL、NeurIPS、IROS 等） · 精选/每日 · 是否有代码），手机友好。已被会议接收的论文还按会议汇总成页面，例如 [CoRL 2026](https://hu-zlatan.github.io/embodied-ai-radar/venues/corl-2026.html?lang=zh)（[全部会议/期刊](https://hu-zlatan.github.io/embodied-ai-radar/venues/index.html?lang=zh)）；每种机器人形态也有独立页面和 Atom 订阅，例如 [人形](https://hu-zlatan.github.io/embodied-ai-radar/robots/humanoid.html?lang=zh) · [灵巧手](https://hu-zlatan.github.io/embodied-ai-radar/robots/hand.html?lang=zh) · [四足](https://hu-zlatan.github.io/embodied-ai-radar/robots/legged.html?lang=zh)；还可以按机构浏览，例如 [英伟达](https://hu-zlatan.github.io/embodied-ai-radar/labs/nvidia.html?lang=zh) · [清华大学](https://hu-zlatan.github.io/embodied-ai-radar/labs/tsinghua.html?lang=zh) · [上海人工智能实验室](https://hu-zlatan.github.io/embodied-ai-radar/labs/shanghai-ai-lab.html?lang=zh)（[全部机构](https://hu-zlatan.github.io/embodied-ai-radar/labs/index.html?lang=zh)）。
- **双语**：每个精选条目都有中英文一句话要点，网站支持 EN / 中文 切换。
- **好引用**：网站上每篇 arXiv 论文都可一键复制 BibTeX，[`curated.bib`](https://hu-zlatan.github.io/embodied-ai-radar/curated.bib) 打包了全部精选论文（由 arXiv 元数据生成）。每个精选条目都有独立的可分享页面，例如 [LEAP Hand](https://hu-zlatan.github.io/embodied-ai-radar/e/arxiv-2309.06440.html)。
- **不只是数量**：每篇论文显示其代码的 GitHub 星数；登上 [Hugging Face Daily Papers](https://huggingface.co/papers) 的论文还会显示社区点赞数（▲）。搜索可按二者排序，首页列出最近两周点赞最多的机器人论文。
- **可复用**：全部精选数据可下载为 [`curated.json`](https://hu-zlatan.github.io/embodied-ai-radar/curated.json) 或 [`curated.csv`](https://hu-zlatan.github.io/embodied-ai-radar/curated.csv)（可直接用 Excel 打开；CC BY 4.0），含主题、机器人类型、链接、中英文要点和 GitHub 星数，方便你做自己的工具。

| 内容 | 更新频率 |
|---|---|
| 每日 arXiv 论文（[网站](https://hu-zlatan.github.io/embodied-ai-radar/feed.html?lang=zh) · [Atom 订阅](https://hu-zlatan.github.io/embodied-ai-radar/feed.xml)；每个主题也有单独的 Atom 订阅，如 [VLA](https://hu-zlatan.github.io/embodied-ai-radar/topics/vla.xml)） | 每天自动 |
| 精选索引（见下方与网站）· 从每日论文中挑选的精选（[Atom 订阅](https://hu-zlatan.github.io/embodied-ai-radar/picks.xml)，每天几篇，中英双语） | 每周多次 |
| [每周精选](digest/) | 每周 |

## 精选索引

⭐ = 重点推荐。每个主题展示重点推荐和最新精选，点击“查看全部”打开完整列表。由 [`data/curated/`](data/curated) 自动生成——请修改 YAML，而不是这些列表。

<!-- radar:start -->

[VLA 与机器人基础模型](#vla) · [操作与灵巧手](#manipulation) · [触觉与视触觉感知](#tactile) · [运动控制与人形机器人](#locomotion) · [世界模型](#world-models) · [导航与具身智能体](#navigation) · [感知、SLAM 与三维建图](#perception) · [规划、控制与安全](#control) · [机器人学习：强化学习与模仿学习](#learning) · [仿真与 Sim-to-Real](#sim) · [数据集与基准](#datasets) · [硬件与开源机器人](#hardware)

<a id="vla"></a>
### VLA 与机器人基础模型

_视觉-语言-动作模型与通用机器人策略。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/vla.html)

- ⭐ **[A Pragmatic VLA Foundation Model](https://arxiv.org/abs/2601.18692)** (2026) — LingBot-VLA：Apache-2.0 开源的基础模型，用九种双臂构型约 2 万小时真实数据训练，并在四个平台各 100 项任务上评测；代码、基座模型和评测数据一并开放。 · [代码](https://github.com/Robbyant/lingbot-vla) · [项目页](https://technology.robbyant.com/lingbot-vla)
- ⭐ **[RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild](https://arxiv.org/abs/2611.02497)** (2026) — 在 124 个站点做盲测两两对比，横跨四种机器人评测 VLA 与前沿智能体。不同机器人的排名几乎不一致（Kendall W = 0.24），开箱排名也难以预测微调后的表现；G1 人形上没有策略完成任何任务。 · [代码](https://github.com/RoboColosseum/robocolosseum-client)
- ⭐ **[π\*0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759)** (2025) — RECAP 通过优势条件化，用演示、机器人自主运行数据和遥操作纠正对 VLA 做强化学习；论文报告在叠衣服、做意式咖啡等难任务上吞吐量提升一倍以上、失败率约减半。 · [项目页](https://pi.website/blog/pistar06)
- ⭐ **[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** (2024) — VLM 主干加流匹配动作专家，跨多种机器人训练，能完成叠衣服等长时程灵巧任务。 · [代码](https://github.com/Physical-Intelligence/openpi)
- ⭐ **[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** (2024) — 基于 Llama 2 与 DINOv2/SigLIP 的 7B 开源 VLA，是 VLA 研究与 LoRA 微调的事实开源基线。 · [代码](https://github.com/openvla/openvla)
- ⭐ **[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** (2023) — 提出 "VLA" 概念：把网络规模的视觉语言模型联合微调为输出动作 token，把语义知识迁移到机器人控制。 · [项目页](https://robotics-transformer2.github.io/)
- **[Asynchronous Robot Policies](https://arxiv.org/abs/2611.05155)** (2026) — 把低频更新语义记忆的大型 VLM 与高频出动作的轻量专家解耦，并针对陈旧和延迟训练；报告 VLM 降到标称频率十分之一时性能无明显损失。 · [项目页](https://arp.insait.ai)
- **[Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs](https://arxiv.org/abs/2611.04166)** (2026) — 展示视觉扰动可以改变推理型 VLA 的动作，而解释文本一字不变（在 Alpamayo 和 InstructVLA 上测试），因此监控必须直接检查动作通道，不能只看文本。
- **[Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation](https://arxiv.org/abs/2611.01112)** (2026) — 任务决策交给大模型，框架提供标定后的三维测量、轨迹预览和偏差即停的执行检查。作者报告在 RoboDojo 榜单排名第一，成功率 57.7%，是同模型参考框架的两倍多。 · [代码](https://github.com/lose4578/Auriga) · [项目页](https://auriga.stelledge.com/)
- **[Democratizing Robot-Use Agents: A Unified Harness with Open Models](https://arxiv.org/abs/2611.01560)** (2026) — uni-robot-agent：面向开放权重模型的机器人操作智能体（Robot-use Agent）框架，便于继续训练。作者报告现成的 Qwen3.8 模型在 RoboDojo 上得 31.39 分，高于已发表的 GPT-6 Astra-RoboProbe 的 28.97 分。 · [代码](https://github.com/Open-RUA/uni-robot-agent)
- **[HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation](https://arxiv.org/abs/2611.02660)** (2026) — 用显式文本保存任务历史、只在检测到事件时更新，为 VLA 增加工作记忆。在 10 个真实的非马尔可夫任务上测试，其中包括需要跨回合保持上下文的任务。 · [代码](https://github.com/kimspacehuni/HeLM) · [项目页](https://kimspacehuni.github.io/HeLM/)
- **[HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model](https://arxiv.org/abs/2610.40373)** (2026) — 跨时间尺度联合预测短期状态、语义里程碑与目标状态，再由动作查询从中检索相关的未来表征。

**[查看全部 141 条 →](lists/vla.zh-CN.md)**

<a id="manipulation"></a>
### 操作与灵巧手

_模仿学习、扩散策略、抓取、双臂与灵巧操作。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/manipulation.html)

- ⭐ **[AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data](https://arxiv.org/abs/2611.03815)** (2026) — 从 16,151 小时手持夹爪演示中学习，全程不采机器人数据；报告十项任务平均成功率 78%，其他 VLA 最好为 27%，并开放数据集、权重和后训练方案。 · [项目页](https://a-0.airoa.io)
- ⭐ **[Generalizable Humanoid Manipulation with 3D Diffusion Policies](https://arxiv.org/abs/2410.10803)** (2024) — iDP3：上半身全身遥操作、带三维激光雷达的 25 自由度人形，加上改进的三维扩散策略，使技能不再局限于单一场景。 · [代码](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy) · [项目页](https://humanoid-manipulation.github.io/)
- ⭐ **[Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](https://arxiv.org/abs/2402.10329)** (2024) — 手持夹爪加 GoPro 可随处采集演示，训练出的策略可直接迁移到机械臂。 · [代码](https://github.com/real-stanford/universal_manipulation_interface)
- ⭐ **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** (2023) — 以去噪方式生成动作序列，比回归更能处理多模态演示，已成为模仿学习标准基线。 · [代码](https://github.com/real-stanford/diffusion_policy)
- ⭐ **[Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705)** (2023) — ALOHA + ACT：约 2 万美元的双臂遥操作平台，加上动作分块 Transformer，约 50 条演示即可学会精细任务。 · [代码](https://github.com/tonyzhaozh/act)
- **[FEIJOA: Task-Driven Grounding and Execution for Mobile Manipulation](https://arxiv.org/abs/2611.04080)** (2026) — 语言模型智能体在测试时对带位姿的 RGB-D 扫描做指令落地，不依赖预建表示；Spot 真机 50 次试验成功 35 次，失败大多来自物理技能而非推理。 · [项目页](https://williamshen-nz.github.io/feijoa/)
- **[RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](https://arxiv.org/abs/2611.05163)** (2026) — 把人到机器人的迁移看作虚拟试穿：保留动作，把视频中的人换成目标机器人；报告在没有这些任务真机演示时，新任务成功率从 2% 升到 60%。 · [项目页](https://ryan-seungyong-lee.github.io/RoboTryOn)
- **[SLAC: Safe and Efficient Real-Robot Reinforcement Learning via Unsupervised Simulation Pre-Training](https://arxiv.org/abs/2506.04147)** (2025) — 在低保真仿真器中预训练与任务无关的潜在动作空间，让高自由度移动操作机器人的真实世界强化学习安全高效。 · [项目页](https://robo-rl.github.io/)
- **[BeyondContact: A Reinforcement Learning Framework for Airflow-Based Non-Contact Manipulation](https://arxiv.org/abs/2611.03059)** (2026) — 为 Isaac Lab 增加基于实测模型的气流扩展，并在夹爪旁加装轻型鼓风机。报告零调试真机部署：推吹混合策略 20 次成功率 80%，纯气流转向平均误差 2.6°。 · [代码](https://github.com/iit-DLSLab/BeyondContact)
- **[ForceLDM: A Force-aware Latent Dynamics Model for Contact-Rich Manipulation](https://arxiv.org/abs/2611.03294)** (2026) — 教师网络看到未来的力/力矩与光流，再把动力学特征蒸馏给只用当前观测的学生网络，使策略在部署时能预判接触。在五个真实接触丰富任务上测试。 · [代码](https://github.com/tpy001/ForceLDM-code) · [项目页](https://tpy001.github.io/ForceLDM/)
- **[Knowing Where to Look: Interactive Object Search via Spatial-Semantic Fusion](https://arxiv.org/abs/2611.00499)** (2026) — 把逐物体的 VLM 合理性评分与几何占据证据融合为统一的三维体素信念，决定下一步看哪、去哪、开哪个柜子；在双臂移动人形上优于纯几何搜索和 LLM 规划。 · [项目页](https://skymanaditya1.github.io/objsearch-website/)
- **[Pixel-UMI: Learning Environment-Aware Whole-Body Manipulation from Sensorized Human Demonstrations](https://arxiv.org/abs/2611.03647)** (2026) — 把传感化的人类示范变成全身策略：结合重建的场景几何做重定向，训练时用重定向误差遮蔽不匹配的视角，再用 DAgger 人工纠正补足接触。作者报告五个任务平均进度 87.0%。 · [项目页](https://pixel-robot.com/pixel-umi)

**[查看全部 67 条 →](lists/manipulation.zh-CN.md)**

<a id="tactile"></a>
### 触觉与视触觉感知

_触觉传感器、触觉表征与接触丰富的控制。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/tactile.html)

- ⭐ **[DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](https://arxiv.org/abs/2005.14679)** (2020) — 低成本、紧凑的 GelSight 式指尖传感器，让视触觉传感器得以普及。 · [代码](https://github.com/facebookresearch/digit-interface)
- **[ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control](https://arxiv.org/abs/2611.04424)** (2026) — 在学习型全身策略之下加入全身触觉反射，10 毫秒内直达电机；在 G1 上，与延迟 20 毫秒的相同反射相比，首次力峰值降低 34.1%。 · [项目页](https://minusmodulo.github.io/reflexarc-website/)
- **[AnyTouch: Learning Unified Static-Dynamic Representation across Multiple Visuo-tactile Sensors](https://arxiv.org/abs/2502.12191)** (2025) — 跨多种视触觉传感器学习统一的静态-动态表征，并贡献对齐的多传感器触觉数据集 TacQuad。 · [代码](https://github.com/GeWu-Lab/AnyTouch)
- **[FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning](https://arxiv.org/abs/2502.17432)** (2025) — 低成本双边遥操作把机械臂受力反馈给操作者；训练时对视觉的破坏逐渐减弱，让策略学会关注力信息。
- **[LocoTouch: Learning Dynamic Quadrupedal Transport with Tactile Sensing](https://arxiv.org/abs/2505.23175)** (2025) — 在四足机器人背部铺设高密度触觉传感器，无需固定装置即可长距离运输未固定的圆柱物体。 · [代码](https://github.com/linchangyi1/LocoTouch)
- **[PP-Tac: Paper Picking Using Tactile Feedback in Dexterous Robotic Hands](https://arxiv.org/abs/2504.16649)** (2025) — 用带高分辨率全向触觉传感器的多指手抓取纸张类薄物体，同时解决状态估计与抓取规划。
- **[Tactile Robotics: An Outlook](https://arxiv.org/abs/2508.11261)** (2025) — 对触觉机器人的综合展望，涵盖压阻、压电、电容、磁性和光学等传感方式及领域走向。
- **[ManiWAV: Learning Robot Manipulation from In-the-Wild Audio-Visual Data](https://arxiv.org/abs/2406.19464)** (2024) — “手上长耳朵”：夹爪在野外人类演示时同步录制音频与视觉；当视觉信息不足时，接触声帮助策略完成接触密集操作。 · [代码](https://github.com/real-stanford/maniwav)
- **[Octopi: Object Property Reasoning with Large Tactile-Language Models](https://arxiv.org/abs/2405.02794)** (2024) — 把触觉感知与语言结合，让具身系统对触摸获得的物理属性做常识推理；贡献 PhysiCLeAR 数据集。 · [代码](https://github.com/clear-nus/octopi)
- **[RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing](https://arxiv.org/abs/2407.01418)** (2024) — 循环图网络从视触觉历史估计物体状态与潜在物理属性，学到的动力学模型用于 MPC，完成密集装箱等任务。
- **[Tactile-Augmented Radiance Fields](https://arxiv.org/abs/2405.04534)** (2024) — TaRF 把视觉与触觉放进同一三维空间：将触摸采样配准到照片，并用条件扩散模型估计未采样位置的触觉。 · [代码](https://github.com/dou-yiming/TaRF)
- **[Evetac: An Event-based Optical Tactile Sensor for Robotic Manipulation](https://arxiv.org/abs/2312.01236)** (2023) — 用事件相机取代光学触觉传感器的 RGB 相机；触觉处理以 1000 Hz 在线运行，可感知最高 498 Hz 的振动。

**[查看全部 50 条 →](lists/tactile.zh-CN.md)**

<a id="locomotion"></a>
### 运动控制与人形机器人

_足式运动、人形全身控制与跑酷。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/locomotion.html)

- ⭐ **[BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](https://arxiv.org/abs/2508.08241)** (2025) — 用同一套超参数的运动跟踪方案学会侧手翻、飞踢、冲刺等敏捷技能，再用带引导的潜空间扩散模型组合这些技能以完成摇杆遥控、避障等新目标，零样本迁移到真机。 · [代码](https://github.com/HybridRobotics/whole_body_tracking)
- ⭐ **[SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control](https://arxiv.org/abs/2511.07820)** (2025) — 检验规模定律在人形控制上的效果：扩大网络、数据和算力，得到通用动作跟踪基础模型，无需手工设计奖励。
- ⭐ **[Real-World Humanoid Locomotion with Reinforcement Learning](https://arxiv.org/abs/2303.03381)** (2023) — 在仿真中训练的因果 Transformer 策略零样本驱动全尺寸人形机器人在户外行走。
- ⭐ **[Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](https://arxiv.org/abs/2109.11978)** (2021) — 数千个 GPU 并行环境几分钟就能训练出四足行走策略；legged_gym 成为标准入门框架。 · [代码](https://github.com/leggedrobotics/legged_gym)
- ⭐ **[DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](https://arxiv.org/abs/1804.02717)** (2018) — 证明强化学习能模仿包括空翻在内的大量动作片段并保持鲁棒，是后续人形动作模仿工作的基本范式。 · [代码](https://github.com/xbpeng/DeepMimic)
- **[HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors](https://arxiv.org/abs/2611.05113)** (2026) — 让人形底层控制器在场景中真实带着物体做动作模仿训练，再在其上训练高层策略；在宇树 G1 上可搬运不同箱子，并能从掉落中恢复。
- **[Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking](https://arxiv.org/abs/2606.03985)** (2026) — 在 20 亿帧重定向动作语料上预训练的 GPT 式因果 Transformer，跟踪高动态全身动作，并零次微调泛化到未见动作。 · [代码](https://github.com/GalaxyGeneralRobotics/Humanoid-GPT) · [项目页](https://qizekun.github.io/Humanoid-GPT/)
- **[SUGAR: A Scalable Human-Video-Driven Generalizable Humanoid Loco-Manipulation Learning Framework](https://arxiv.org/abs/2605.20373)** (2026) — 把多样的人类视频转化为可部署的人形移动操作技能，无需任务专用奖励，能应对先验中的遮挡与重定向误差。 · [代码](https://github.com/tianshuwu/SUGAR) · [项目页](https://tianshuwu.github.io/sugar-humanoid/)
- **[InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions](https://arxiv.org/abs/2502.20390)** (2025) — 单一策略从数小时不完美动捕数据学习全身人-物交互：先用个体教师策略精修数据，再扩展规模。 · [代码](https://github.com/Sirui-Xu/InterMimic)
- **[Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies](https://arxiv.org/abs/2410.11825)** (2024) — 对学习到的策略施加 Lipschitz 约束，作为获得平滑动作的通用方法，取代需手动调参的低通滤波和平滑奖励。 · [代码](https://github.com/zixuan417/smooth-humanoid-locomotion)
- **[Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation](https://arxiv.org/abs/2309.01952)** (2023) — TRILL 用 VR 采集演示，由全身控制器把任务空间指令转为关节力矩，实现数据高效的人形移动操作模仿。 · [代码](https://github.com/UT-Austin-RPL/TRILL) · [项目页](https://ut-austin-rpl.github.io/TRILL)
- **[Perpetual Humanoid Control for Real-time Simulated Avatars](https://arxiv.org/abs/2305.06456)** (2023) — 人形控制器可扩展到一万条动作片段且无需外部稳定力，并能自行从跌倒中恢复，无需重置。 · [代码](https://github.com/ZhengyiLuo/PHC) · [项目页](https://zhengyiluo.github.io/PHC/)

**[查看全部 69 条 →](lists/locomotion.zh-CN.md)**

<a id="world-models"></a>
### 世界模型

_学习的动力学模型、视频世界模型、世界动作模型（WAM）与基于模型的强化学习。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/world-models.html)

- ⭐ **[World Action Models: A Survey](https://arxiv.org/abs/2606.20781)** (2026) — 厘清 WAM 与世界模型、视频生成模型、VLA 的区别，并按生成内容（渲染、潜空间或不生成）和架构分类；结论是领域正走向少生成未来，只保留控制所需。 · [项目页](https://world-action-models.github.io/)
- ⭐ **[Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104)** (2023) — DreamerV3：一套超参数适用于 150 多个任务，包括从零开始在《我的世界》中挖到钻石。 · [代码](https://github.com/danijar/dreamerv3)
- **[DreamX: Video Diffusion Model is a Universal Latent Action Learner](https://arxiv.org/abs/2611.05377)** (2026) — 复用预训练视频扩散模型提取紧凑潜动作（每帧 1,200 压到 4 个 token），作为人、机器人和不同环境之间的共享接口，并支持零示教动作迁移。 · [代码](https://github.com/cvlab-kaist/DreamX) · [项目页](https://cvlab-kaist.github.io/DreamX/)
- **[PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](https://arxiv.org/abs/2611.04870)** (2026) — 自回归多视角世界模型，运行 10.1 FPS，100 至 200 步梯度即可适配未见平台；作者开放权重和代码，并说明细粒度局部标定仍落后于同类。 · [项目页](https://primebottech.github.io/PrimeSim-website/)
- **[OpenNWM: A Generalist Navigation World Model with Latent Action Pretraining](https://arxiv.org/abs/2611.01844)** (2026) — 先从无动作标注的视频中学习潜在动作，再在后训练阶段对齐真实运动。配套数据集 NavAnywhere 含 17.5M 条视觉观测，来自 15 个来源，覆盖地面机器人、人和无人机。 · [代码](https://github.com/OpenSpace-Lab/OpenNWM)
- **[Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](https://arxiv.org/abs/2610.39232)** (2026) — GenSight 把未来视频生成与稠密感知（深度、本体分割、二维光流）放进同一个视频扩散 Transformer，共用一个预测空间。 · [项目页](https://gensight-rbs.github.io/)
- **[Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence](https://arxiv.org/abs/2611.01677)** (2026) — 流式多视角因果世界模型：用 3D 高斯重建的渲染结果作为场景上下文来维持长时生成，面向闭环仿真、闭环训练和世界动作模型应用。 · [项目页](https://xiaomiautoworldmodel.github.io/CausalWorldModel/)
- **[pico-WAM: Evaluating Counterfactual Prediction and Planning Error in a Compact World Action Model](https://arxiv.org/abs/2611.01039)** (2026) — 世界动作模型失败时，问题出在动作提议还是轨迹评分？在 Push-T 上，把学习的评分换成仿真器代价可提升 12.2 个百分点的覆盖率，而在提议阶段换用仿真器状态未见增益。提供可复现的诊断流程。 · [代码](https://github.com/keivalya/pico-wam)
- **[Chunk-wise Model-based Policy Optimization](https://arxiv.org/abs/2610.14564)** (2026) — CoRL 2026 Spotlight。将分块世界模型用作训练期可微评估器的模型式强化学习，针对累积误差、推理延迟与 BPTT 不稳定问题。 · [代码](https://github.com/song-wx/CMPO) · [项目页](https://song-wx.github.io/cmpo.github.io/)
- **[Hierarchical World Models with Implicit Dynamics](https://arxiv.org/abs/2610.42146)** (2026) — ID-WM 将状态可达性与局部控制解耦：高层模型在状态流形上采样可行转移，低层世界模型充当逆动力学求解器，把子目标落实为精确动作。报告比单层世界模型 MPC 提升 135%，比最优策略与扩散规划器提升 38.5%。 · [项目页](https://id-wm.github.io)
- **[Targeting World Models to Compromise Robot Learning Pipelines](https://arxiv.org/abs/2606.09499)** (2026) — CoRL 2026 Spotlight。展示世界模型可成为隐蔽的数据投毒入口：即使真实训练数据看似安全，部署的策略仍可能被破坏。
- **[World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922)** (2026) — CoRL 2026 Oral。DreamZero：基于预训练视频扩散骨干的世界动作模型，联合预测视频与动作，可从异构机器人数据学习技能，无需重复示范。 · [代码](https://github.com/dreamzero0/dreamzero) · [项目页](https://dreamzero0.github.io/)

**[查看全部 59 条 →](lists/world-models.zh-CN.md)**

<a id="navigation"></a>
### 导航与具身智能体

_视觉语言导航、具身问答、移动操作与大模型规划。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/navigation.html)

- ⭐ **[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)** (2022) — SayCan：大模型提出步骤，学习到的价值函数评估机器人当下实际能做什么。
- **[WayTrace: A Map-to-Language-to-Trace Hierarchy for Embodied Urban Navigation](https://arxiv.org/abs/2611.05129)** (2026) — 视觉语言模型把网络地图导航拆成一条条原子指令，预测器在图像上画出路径，强化学习负责跟踪；轮腿机器人完成最长 1.37 公里的真实任务。 · [项目页](https://way-trace.github.io)
- **[OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation](https://arxiv.org/abs/2610.39287)** (2026) — 面向无人机的机载 VLA：同一视觉-语言表征同时支撑语义理解、空间推理与闭环航点控制。 · [代码](https://github.com/Ideal-ljl/AeroBrain) · [项目页](https://ideal-ljl.github.io/AeroBrain/)
- **[OSCAR: Obstacle Survival Curves for Adaptive Robot Navigation](https://arxiv.org/abs/2606.00990)** (2026) — CoRL 2026 Spotlight。通过建模各类障碍物通常停留多久，决定在路线受阻时等待还是改道。
- **[SidewalkBench: Benchmarking Visual Navigation on Urban Sidewalks](https://arxiv.org/abs/2606.16953)** (2026) — CoRL 2026 Spotlight。城市人行道视觉导航基准，基于 Isaac Sim，包含程序生成与真实世界环境。 · [代码](https://github.com/VAIL-UCLA/SidewalkBench) · [项目页](https://vail-ucla.github.io/SidewalkBench/)
- **[Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation](https://arxiv.org/abs/2610.34674)** (2026) — OSMA-Bench 用仅障碍物类型不同的配对场景，检验导航策略能否按障碍物危险程度调整间距与速度，并提出语义敏感度指数 SSI。结果显示 VLM 与 VLA 策略能识别哪些障碍更危险，却很少把这种判断体现在实际运动中；在 VLM 方案中加入显式参数推断步骤有所改善。 · [代码](https://github.com/OSMA-Bench/OSMA-Bench) · [项目页](https://osma-bench.github.io/)
- **[Gaussian Episodic Memory for Long-Term Spatiotemporal Reasoning](https://arxiv.org/abs/2610.33158)** (2026) — GEMS 维护一张只在场景变化处增量更新的 3DGS 地图，智能体按需渲染新视角来回答时空问题和定位物体；同时发布 GEMS-Bench（3 个真实 + 12 个合成环境，473 个问答对），报告在物体定位和时空问答上优于近期基线。 · [项目页](https://abwerby.github.io/GEMS/)
- **[One Scan is Enough: Demonstration-Free Adaptation for Language-Guided Navigation](https://arxiv.org/abs/2610.33794)** (2026) — 只需用 iPhone 扫描一次新建筑：扫描被编译成训练环境并自动合成带语言指令的导航回合，再用无评论家的闭式 Pareto 效用适配策略；报告真机成功率 85%，用人类示教后训练的基线为 49%。
- **[See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space](https://arxiv.org/abs/2610.31762)** (2026) — RepresentNav 用一个小型 Transformer 融合多个视觉基础模型各层特征，构建由导航目标自行塑造的表示空间，并在每步动作前预测下一时刻的潜在表示（JEPA 式）；报告 VLNVerse 细粒度成功率 83.8%（领先 20.05 个百分点），并在真机上验证。 · [项目页](https://wang-yinxi.github.io/representnav/)
- **[HAVANA: A Hierarchical Video-Action Model for Vision-Language Navigation](https://arxiv.org/abs/2610.24122)** (2026) — 面向视觉语言导航的双系统视频-动作模型：慢系统根据历史观测与指令生成紧凑的隐式规划，快系统结合该规划与最新观测输出局部轨迹；推理时不生成未来视频。代码与权重称将在该仓库发布。 · [代码](https://github.com/Anastasiawd/HAVANA) · [项目页](https://github.com/Anastasiawd/HAVANA)
- **[MOON: Learning When to Forget and How to Move On in Vision-and-Language Navigation](https://arxiv.org/abs/2610.33546)** (2026) — 发现 VLN 智能体偏离路线后会被历史记忆“惯性”拖住。MOON 给冻结的导航策略加上偏航判断器（判断何时清空历史）和 GRPO 训练的恢复策略，参数增加不到 1%；报告在 R2R-CE / RxR-CE 上分别提升 5.2 / 6.0 个百分点。 · [代码](https://github.com/AutoLab-SAI-SJTU/MOON)
- **[EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models](https://arxiv.org/abs/2610.25959)** (2026) — 包含 20 万余条导航规划样本的数据集，场景多样，标注从相机运动轨迹到高层语义指令；并把视频世界模型当作低成本交互环境做强化学习后训练，报告称在未见场景上有明显提升。 · [代码](https://github.com/XiaokunFeng/EmbodiedWorld-200K) · [项目页](https://xiaokunfeng.github.io/EmbodiedWorld-200K/)

**[查看全部 38 条 →](lists/navigation.zh-CN.md)**

<a id="perception"></a>
### 感知、SLAM 与三维建图

_视觉/激光 SLAM 与里程计、三维重建、物体位姿、深度估计与开放词汇场景地图。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/perception.html)

- ⭐ **[Segment Anything](https://arxiv.org/abs/2304.02643)** (2023) — SAM：可用点、框、掩码提示的分割模型，在 10 亿级掩码上训练；已成为机器人感知流程中获取物体掩码的常用基础组件。 · [代码](https://github.com/facebookresearch/segment-anything)
- ⭐ **[ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](https://arxiv.org/abs/2007.11898)** (2020) — 最常用的特征点 SLAM 库：支持单目、双目与 RGB-D，可融合 IMU，并支持多地图重定位。 · [代码](https://github.com/UZ-SLAMLab/ORB_SLAM3)
- **[Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping](https://arxiv.org/abs/1910.02490)** (2019) — 开源 C++ 实时度量-语义视觉惯性 SLAM 库，模块化包含 VIO、鲁棒位姿图、快速三维网格与稠密语义重建。 · [代码](https://github.com/MIT-SPARK/Kimera)
- **[AnchorHEC: Targetless Hand-Eye Calibration of Wrist and Fixed Cameras](https://arxiv.org/abs/2611.02884)** (2026) — 无需标定板，用 RGB、正运动学和三维基础模型同时标定腕部与固定相机；仿真中平移和旋转误差比基于重建的基线分别降低 86.4% 和 71.6%，并在真机上验证。 · [项目页](https://hwanggb.github.io/AnchorHEC/)
- **[Anchor3R: Streaming 3D Reconstruction with Transient Anchors for Long-Horizon Visual Mapping](https://arxiv.org/abs/2606.05035)** (2026) — CoRL 2026 Spotlight。以当前帧为中心的流式三维重建：在当前帧坐标系预测窗口相对位姿与局部几何，以抑制长时漂移。 · [代码](https://github.com/polar-explorer/Anchor3R)
- **[OpenVIO: A Versatile Open-Source Visual-Inertial Odometry System](https://arxiv.org/abs/2610.41671)** (2026) — MIT 许可的开源视觉惯性里程计，面向科研与实际应用。支持针孔、鱼眼相机及拼接 360° 图像，并在公开数据集上与其他开源 VIO 系统做了对比。 · [代码](https://github.com/93won/openvio)
- **[ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models](https://arxiv.org/abs/2610.27040)** (2026) — 用自动标注的机器人操作录像加多来源视觉数据构建约 150 万条可验证的定位监督，微调 Qwen3.5-9B；报告在七个公开视觉定位基准上平均 75.41 分，GPT-6 Astra 为 73.68。 · [代码](https://github.com/DAXIAORobotics/ACE-Brain-0.6) · [项目页](https://daxiaorobotics.github.io/ACE-Brain-0.6/)
- **[Which Depth Estimator for Jetson AGX Orin? A 2026 Benchmark of Monocular and Stereo Methods](https://arxiv.org/abs/2610.27199)** (2026) — 给机器人开发者的实测数据：在 Jetson AGX Orin 上用 TensorRT 运行九类单目与双目深度估计模型（Depth Anything V2/3、Depth Pro、MoGe-2、Fast-FoundationStereo 等），并评测度量精度与速度。 · [代码](https://github.com/nodarhub/orin-depth-benchmark)
- **[SpaRV: Sparse Radiance Voxels for Scalable Geometrically Consistent LiDAR-Visual Mapping and Rendering](https://arxiv.org/abs/2610.25665)** (2026) — 用激光雷达与相机数据构建稀疏体素辐射场地图，针对机器人数据视角少、位姿有误差、场景大的问题，在保证几何精度的同时控制显存占用。 · [代码](https://github.com/hku-mars/SpaRV)
- **[Vision as Proprioception: Estimating Humanoid Robot Pose from Video](https://arxiv.org/abs/2610.25288)** (2026) — HumanoidPose 仅凭视频恢复人形机器人的全身关节构型：适用于拿不到机载状态的场景，也能把网上的机器人视频变成训练数据。 · [代码](https://github.com/eth-siplab/HumanoidPose)
- **[FoundationStereo: Zero-Shot Stereo Matching](https://arxiv.org/abs/2501.09898)** (2025) — 在大规模合成数据上训练的双目深度模型，报告称在真实场景上零样本精度很强；可直接作为双目相机机器人的深度来源。 · [代码](https://github.com/NVlabs/FoundationStereo)
- **[SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719)** (2025) — 给定短名词短语或示例图像，即可在图像和视频中分割并跟踪某一概念的所有实例；数据引擎覆盖 400 万个概念标签，开放权重与 SA-Co 基准，可直接用作机器人开放词汇感知模块。 · [代码](https://github.com/facebookresearch/sam3)

**[查看全部 29 条 →](lists/perception.zh-CN.md)**

<a id="control"></a>
### 规划、控制与安全

_运动规划、轨迹优化、模型预测控制、安全滤波器与安全的学习型控制。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/control.html)

- ⭐ **[cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation](https://arxiv.org/abs/2310.17274)** (2023) — 面向机械臂的 GPU 并行运动生成：同时运行大量轨迹优化，在毫秒级给出无碰撞且平滑的轨迹。 · [代码](https://github.com/NVlabs/curobo)
- **[RAM: Reachability Across Morphologies](https://arxiv.org/abs/2606.09108)** (2026) — CoRL 2026 Spotlight。以形态为条件的隐式神经位姿可达性模型，可微、考虑自碰撞，并能泛化到未见形态。 · [代码](https://github.com/TimWalter/ram) · [项目页](https://timwalter.github.io/ram)
- **[TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation](https://arxiv.org/abs/2606.06218)** (2026) — CoRL 2026 Spotlight。面向富接触动作迁移的模块，应对仿真到现实、负载与个体差异，用于替代域随机化或系统辨识。 · [代码](https://github.com/Dongwon-Son/TAM) · [项目页](https://dongwon-son.github.io/tam-project-page/)
- **[A generalist policy for muscle-driven control across individual musculoskeletal models](https://arxiv.org/abs/2610.36535)** (2026) — MyoAcross 结合个体化肌骨模型构建、形态条件策略学习与虚拟模型增广，用一个策略驱动不同个体的肌骨模型跟踪参考动作而无需逐个微调；报告在 31 个未见个体模型上完成率 99.24%，跟踪误差比无条件 MLP 降低 22.6%，并与 120 人的地面反力和肌电数据做了对比。 · [项目页](https://woodater-thu.github.io/MyoAcross/)
- **[Keeping Contact: Task-Adaptive Friction Margins for Bimanual Non-Prehensile Manipulation](https://arxiv.org/abs/2610.36961)** (2026) — 以带符号摩擦距离度量防滑裕度，并在双臂绕支点倾转物体时按任务需求自适应调整；一系列二阶锥规划给出全局最优接触力。真机实验显示自适应裕度优于固定裕度和无裕度。 · [项目页](https://keeping-contact.github.io/)
- **[CusADi2: Latency-Optimized Batch Computation of Robot Kinematics, Jacobians, and Hessians on the GPU](https://arxiv.org/abs/2610.25476)** (2026) — 在 GPU 上以低延迟批量计算运动学、雅可比与海森矩阵，面向在线运行的采样式与梯度式轨迹优化。 · [代码](https://github.com/johnviljoen/cusadi2)
- **[PrismPlan: A Shared GPU Substrate for Motion Planning Across Paradigms](https://arxiv.org/abs/2610.23884)** (2026) — 一次性实现批量 GPU 碰撞检测与正运动学，在其上运行采样、搜索和优化三类规划器，使三种范式可以公平比较。 · [代码](https://github.com/XiaoyubotMotionTeam/PrismPlan)
- **[Sub-Millisecond Reflexes for Continuous Physical Human-Robot Interaction](https://arxiv.org/abs/2610.21913)** (2026) — 开源的 ROS 2 多模式控制器，可在亚毫秒内切换控制模式并触发安全反射而无需中断任务；在 Franka 机械臂上验证。 · [代码](https://github.com/RoboRef/franka_reflex_engine)
- **[Motions in Microseconds via Vectorized Sampling-Based Planning](https://arxiv.org/abs/2309.14545)** (2023) — VAMP：用 CPU SIMD 指令把碰撞检测向量化，使 RRT-Connect 等基于采样的规划器在微秒到毫秒级求解机械臂运动规划，无需 GPU。 · [代码](https://github.com/KavrakiLab/vamp)
- **[Motion Policy Networks](https://arxiv.org/abs/2210.12209)** (2022) — 在数百万条规划器生成的轨迹上训练的神经策略，可直接根据点云把机械臂移动到目标位置。 · [代码](https://github.com/NVlabs/motion-policy-networks)
- **[Planning with Diffusion for Flexible Behavior Synthesis](https://arxiv.org/abs/2205.09991)** (2022) — Diffuser：把规划视为对整条轨迹去噪，目标与奖励可以引导采样；扩散模型与控制结合的早期代表作。 · [代码](https://github.com/jannerm/diffuser)
- **[Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo](https://arxiv.org/abs/2212.00541)** (2022) — 推出 MuJoCo MPC（MJPC），可在 MuJoCo 中交互式地做实时预测控制，并表明简单的基于采样的规划器在接触丰富的行为上是很强的基线。 · [代码](https://github.com/google-deepmind/mujoco_mpc)

**[查看全部 28 条 →](lists/control.zh-CN.md)**

<a id="learning"></a>
### 机器人学习：强化学习与模仿学习

_面向机器人的强化学习、模仿学习与策略后训练方法，不限机器人形态。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/learning.html)

- ⭐ **[Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](https://arxiv.org/abs/2410.21845)** (2024) — HIL-SERL：结合人类纠正的真机强化学习，报告称在精密装配与动态任务上经数小时训练即可接近满分成功率。 · [代码](https://github.com/rail-berkeley/hil-serl)
- ⭐ **[Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)** (2017) — 采用截断目标的策略梯度方法，是大多数 GPU 并行仿真训练（运动控制、灵巧操作）背后的算法。
- **[Behavior Graphs: Unsupervised Graph Structures for Interpreting Robot Deployment Data](https://arxiv.org/abs/2611.00405)** (2026) — 把策略回放压缩成一张有向图，将行为模式与结果相连，帮助决定下一步采集什么数据。在三个真实任务的用户研究中，18 名参与者有 16 名更喜欢它而非回放视频。 · [项目页](https://try.behavior-graphs.com/)
- **[Beyond Validation Loss: Coverage and Reliability Dynamics in Robot Policy Pretraining](https://arxiv.org/abs/2611.01565)** (2026) — 提出跟踪闭环 pass@k（k 次尝试至少成功一次的概率）。pass@1 相同的检查点在后训练中可能表现不同，因此给出兼顾覆盖度与可靠性的离线检查点选择方法。 · [项目页](https://zhanyisun.github.io/robot-policy-learning-dynamics/)
- **[D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models](https://arxiv.org/abs/2611.03622)** (2026) — 只靠提示词的任务进度评估：先让 VLM 客观描述画面并定义绝对成功标准，再按明确评分表打分，减少对失败执行“幻觉式”的进度判断，其奖励可用于下游强化学习。 · [代码](https://github.com/memmelma/dna) · [项目页](https://weirdlabuw.github.io/dna)
- **[When Robots Outweigh Objects: How Inertia Mismatch Shapes Robot Policy Learning](https://arxiv.org/abs/2611.03501)** (2026) — 在仿真中改变机器人与物体质量：强化学习影响不大，行为克隆则在机器人比物体轻时更可靠，增加数据只能缩小而无法消除差距。采集低惯量示教可部分缓解。 · [项目页](https://younghyopark.me/inertia-mismatch/)
- **[Diffusion ReRoll: Revisable Denoising for Robotic Sequential Prediction](https://arxiv.org/abs/2607.19919)** (2026) — CoRL 2026 Spotlight。在扩散序列预测中选择性重新加噪，让时间跨度内的片段可以借助其余片段的上下文再次修正。 · [项目页](https://seonsoo-p1.github.io/DiffusionReRoll/)
- **[Flow Policy Gradients for Robot Control](https://arxiv.org/abs/2602.02481)** (2026) — CoRL 2026 Oral。让流匹配策略梯度可用于机器人控制：绕过动作似然计算，策略不再限于高斯分布。应用于足式运动、人形动作跟踪与操作。 · [代码](https://github.com/amazon-far/fpo-control) · [项目页](https://hongsukchoi.github.io/fpo-control)
- **[FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space](https://arxiv.org/abs/2607.08877)** (2026) — CoRL 2026 Spotlight。在隐空间中根据人类干预适配冻结的生成式策略，替代大规模采集或实机在线强化学习。 · [代码](https://github.com/microsoft/FlowDAgger) · [项目页](https://microsoft.github.io/FlowDAgger)
- **[RL Token: Bootstrapping Online RL with Vision-Language-Action Models](https://arxiv.org/abs/2604.23073)** (2026) — CoRL 2026 Oral。让 VLA 输出紧凑的 RL token 作为在线强化学习接口，预训练策略只需几小时真实练习即可提升精度与速度。
- **[Recursive Self-Improvement in Physical AI: Mechanisms, Evidence, and Evaluation](https://arxiv.org/abs/2610.38266)** (2026) — 综述：区分普通的学习器更新与会修改学习过程本身的“改进器”，给出从任务内适应到已验证改进增益的 L0–L3 分级，并提出从相同起点比较的评测方法。 · [项目页](https://github.com/nkd-lkz/physical-ai-rsi-survey)
- **[CuraEval: Evaluating Demonstration Curation on Mixed-Skill Robot Data](https://arxiv.org/abs/2610.38221)** (2026) — 对示范数据筛选方法做严格对照：在混合技能的 robomimic 数据上与等量随机子集和全量训练比较，发现某评分几乎等同于按轨迹长度排序；经多重比较校正后，没有任何筛选条件显著优于全量数据训练（CoRL 2026 Workshop 论文）。 · [代码](https://github.com/jiuyixu25/CuraEval)

**[查看全部 47 条 →](lists/learning.zh-CN.md)**

<a id="sim"></a>
### 仿真与 Sim-to-Real

_物理仿真器、GPU 并行训练与向真实机器人迁移。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/sim.html)

- ⭐ **[When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks](https://arxiv.org/abs/2610.41857)** (2026) — 审计仿真基准：不少“策略失败”其实是物理引擎把物体弹飞。SimuGuard 为 LIBERO、RoboTwin、RoboCasa、RoboDojo 提供审计插件，把 RoboTwin 上的问题追溯到碰撞检测的一个常量；仅改动它，异常回合由 100 回合 12 次降到 0，五个容器任务成功率由 89% 升到 98%。 · [代码](https://github.com/ALEXander22568/simuguard)
- ⭐ **[MuJoCo](https://mujoco.org/)** (2012) — 快速准确的接触物理仿真，机器人学习研究的默认仿真器，由 DeepMind 开源。 · [代码](https://github.com/google-deepmind/mujoco)
- **[Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation](https://arxiv.org/abs/2504.12908)** (2025) — 结合 IPC 与 ABD 的 GPU 触觉仿真；作者报告在数千并行环境下达到实时速度的 18 倍。
- **[BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark](https://arxiv.org/abs/2407.07788)** (2024) — 面向移动双臂机器人的基准，含 40 个家庭任务（从抓取到厨房清洁），均配人类采集的演示。 · [项目页](https://chernyadev.github.io/bigym/)
- **[DIFFTACTILE: A Physics-based Differentiable Tactile Simulator for Contact-rich Robotic Manipulation](https://arxiv.org/abs/2403.08716)** (2024) — 可微触觉仿真器，用 FEM 软体模型模拟弹性体，面向多种材料的接触，而非主要针对刚体。 · [代码](https://github.com/Genesis-Embodied-AI/DiffTactile)
- **[GRUtopia: Dream General Robots in a City at Scale](https://arxiv.org/abs/2407.10943)** (2024) — 面向多种机器人的交互式三维仿真社会；GRScenes 含 10 万标注场景、89 个类别，可组合成城市级环境。 · [代码](https://github.com/OpenRobotLab/GRUtopia)
- **[ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks](https://arxiv.org/abs/2412.13211)** (2024) — GPU 加速的 Home Assistant Benchmark，采用真实低层控制；作者报告速度超过此前“魔法抓取”实现的 3 倍。 · [代码](https://github.com/arth-shukla/mshab)
- **[TacEx: GelSight Tactile Simulation in Isaac Sim -- Combining Soft-Body and Visuotactile Simulators](https://arxiv.org/abs/2411.04776)** (2024) — 把 GIPC 软体接触与 Taxim、FOTS 触觉仿真器接入 Isaac Sim，模拟 GelSight Mini，并提供 Isaac Lab 强化学习环境。
- **[AuRA: From Atoms to Bits through Autonomous Robot Interaction](https://arxiv.org/abs/2610.34452)** (2026) — 自动完成物理数字孪生所需的机器人交互与数据准备；在 13 种柔性物体上报告每个资产的人工投入减少 88.5%。 · [代码](https://github.com/Yoonkyo/AuRA) · [项目页](https://aura-robot.github.io/)
- **[Closing the Dynamics Gap through Self-Directed Robotic Interaction](https://arxiv.org/abs/2611.02691)** (2026) — CUE（CoRL 2026 Late Breaking Results）：智能体主动选择仿真最不准的交互来辨识摩擦和恢复系数；在台球任务上报告留出位置误差比最强基线低 72%，并部署到真实球桌。 · [项目页](https://cue-dynamics.github.io/)
- **[Kamino: GPU-based Simulation of Rigid Multi-Body Physics with Kinematic Loops](https://arxiv.org/abs/2603.16536)** (2026) — CoRL 2026 Spotlight。基于 NVIDIA Warp 的 Python GPU 物理求解器，集成于 Newton，可并行仿真含真实运动学闭环的机器人，而非树形近似。
- **[MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation](https://arxiv.org/abs/2603.16861)** (2026) — CoRL 2026 Oral。挑战“仅靠仿真不够”的观点：足够大规模、多样的合成数据即可零样本迁移到真实静态与移动操作。MolmoBot-Engine 是开源的程序化数据管线。 · [代码](https://github.com/allenai/MolmoBot) · [项目页](https://allenai.github.io/MolmoBot)

**[查看全部 43 条 →](lists/sim.zh-CN.md)**

<a id="datasets"></a>
### 数据集与基准

_大规模机器人数据集、第一视角数据与评测基准。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/datasets.html)

- ⭐ **[LeRobot](https://github.com/huggingface/lerobot)** (2024) — PyTorch 机器人学习库，提供数据集、预训练策略（ACT、Diffusion、SmolVLA）与低成本机械臂驱动。
- ⭐ **[LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)** (2023) — 四个套件共 130 个语言条件任务，现已成为 VLA 论文最常用的仿真基准。 · [代码](https://github.com/Lifelong-Robot-Learning/LIBERO)
- ⭐ **[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)** (2023) — 30 多个实验室汇集 22 种机器人的 100 多万条轨迹；在其上训练的 RT-X 优于单机器人基线。 · [代码](https://github.com/google-deepmind/open_x_embodiment)
- **[CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation](https://arxiv.org/abs/2611.05080)** (2026) — 面向无频繁重置场景下 VLA 强化学习微调的仿真基准；发现直接微调会因物体和末端位姿偏移而失败，定向分配重置并处理预训练偏差可以缓解。 · [项目页](https://embodiedai-ntu.github.io/cronos/)
- **[PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](https://arxiv.org/abs/2611.05320)** (2026) — 编程智能体凭一条标定轨迹在仿真中重建任务，再由视频模型渲染成写实数据；报告真机 100 次成功 93 次，遥操作数据为 84 次，每小时数据约 107 美元。 · [代码](https://github.com/DAGroup-PKU/PyRUA-Lean) · [项目页](https://dagroup-pku.github.io/PyRUA-Lean/DataFarm)
- **[RoboScope Kit: Unified Interfaces for Fast and Scalable Embodied-AI Evaluation](https://arxiv.org/abs/2611.03850)** (2026) — 模型和基准各封装一次，把仿真 worker 与策略副本分成两个池调度；报告单卡评测比官方 StarVLA 评测器快 4.45 到 6.16 倍。 · [代码](https://github.com/MINT-SJTU/RoboScope-Kit) · [项目页](https://roboscope.pages.dev/)
- **[ClothDojo: Learned Data Generation and Benchmarking for Bimanual Garment Flattening and Folding](https://arxiv.org/abs/2611.01190)** (2026) — 仿真平台：用微调后的 VLA 生成近 8000 条成功的衣物操作轨迹，并重新渲染供 RGB 策略训练，效果优于直接用人类数据训练，但泛化到未见衣物仍是难题。 · [项目页](https://clothdojo.github.io/)
- **[DexArena: A Unified Benchmark for Long-Horizon Dexterous Manipulation](https://arxiv.org/abs/2611.02629)** (2026) — 10 个长时序和 30 个阶段级双手灵巧任务，每个阶段都有物理判定的成功条件，可衡量中间进度；提供经过验证的遥操作示范和统一接口。 · [项目页](https://sipair-elastic.github.io/DexArena-website/)
- **[Is It the Curriculum or Just the Easy Start? Benchmarking Unsupervised Environment Design on Quadrupeds](https://arxiv.org/abs/2610.40364)** (2026) — 在 MuJoCo MJX 中用统一协议在五款四足上比较 14 种课程方法：没有方法在所有机器人和地形集上都领先，而训练关卡偏简单的方法在分布内随机地形上表现靠前。 · [代码](https://github.com/Solvro/ml-wojtek-ued)
- **[OmniPiano: Diverse Dexterous Piano-Playing Challenges for Standard, Robust, Safe, and Multi-Agent RL](https://arxiv.org/abs/2611.00243)** (2026) — 把机器人弹钢琴扩展到 1 至 5 只 Shadow 手，并支持鲁棒、安全和多智能体强化学习：至少 912 种任务设置、36 个基线算法。作者报告前沿算法与大模型智能体在高难任务上仍很吃力。 · [代码](https://github.com/SAIL-Research-Lab/omnipiano) · [项目页](https://sail-research-lab.github.io/omnipiano/)
- **[RoboJev: An Open Vision-Language Judge for Robot Success Detection](https://arxiv.org/abs/2610.33718)** (2026) — 开放权重模型，根据视频帧判断操作是否成功，可用于标注数据；在未见过的实验室与机器人上报告 AUROC 0.89。 · [项目页](https://robo-jev.com)
- **[Rollout then Recycle: 3,718 Labelled Real-Robot Episodes from Benchmarking 7 Policies on 12 Tasks](https://arxiv.org/abs/2611.03168)** (2026) — 公开 ArmnetBench v0.1 在 SO-101 机械臂上的全部回合：600 条遥操作示范和 3118 条带标注的策略执行，其中 73% 是失败，可以在同一任务上比较多种策略的错误。

**[查看全部 65 条 →](lists/datasets.zh-CN.md)**

<a id="hardware"></a>
### 硬件与开源机器人

_可自行搭建的低成本机械臂、灵巧手、夹爪与数据采集设备。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/hardware.html)

- ⭐ **[Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation](https://arxiv.org/abs/2611.03648)** (2026) — 把硬件、数据和学习放在一起设计：低成本轮式人形、柔顺夹爪，遥操作与免机器人的人类数据采集，统一的全身控制器，以及人类与机器人示范共用的策略学习流程。 · [项目页](https://pixel-robot.com/pixel)
- ⭐ **[LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning](https://arxiv.org/abs/2309.06440)** (2023) — 16 自由度灵巧手，用现成零件约 2000 美元即可搭建。 · [代码](https://github.com/leap-hand/LEAP_Hand_API) · [项目页](https://leaphand.com/)
- **[MABEL: An Open Anthropomorphic Mobile Bimanual Platform for Teleoperation and Learning](https://arxiv.org/abs/2611.04083)** (2026) — 开源 56 自由度移动双臂机器人，含 7 自由度手臂和 17 自由度灵巧手，零件成本约 8100 美元，支持 Apple Vision Pro 遥操作，并演示了模仿学习全流程。 · [项目页](https://robotmabel.github.io/website/)
- **[RAIPAL: A Powerful and Agile Humanoid Arm for Human Tasks](https://arxiv.org/abs/2611.04334)** (2026) — 人形手臂，其力量、速度和耐力指标取自人类上肢测量数据；报告峰值负载 20 公斤（自重的 2.25 倍），末端速度 20.6 米每秒。
- **[MEVITA: Open-Source Bipedal Robot Assembled from E-Commerce Components via Sheet Metal Welding](https://arxiv.org/abs/2508.17684)** (2025) — 用电商零件和钣金焊接搭建的开源双足机器人，避开 3D 打印方案在尺寸和强度上的限制。 · [项目页](https://haraduka.github.io/mevita-hardware)
- **[The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics](https://arxiv.org/abs/2409.19795)** (2024) — 面向运动研究的开源 10 自由度人形；利用被动动力学的强化学习策略将运输成本在仿真中最多降低 50%，实机降低 31%。 · [代码](https://github.com/generalroboticslab/dukeHumanoidHardwareControl)
- **[KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL](https://arxiv.org/abs/2611.03138)** (2026) — 基于桌游 KLASK 的桌面级对抗多智能体强化学习平台，成本低于 2500 美元：开放 CAD 与物料清单，提供 Isaac Lab 数字孪生，以及采用学习型执行器模型的 sim-to-real 基线。 · [代码](https://github.com/IDSCETHZurich/klask_rl) · [项目页](https://idscethzurich.github.io/klask_hardware)
- **[SwapBot: Tool-Centric Robot Manipulation via Interchangeable End-Effectors and Tactile Sensing](https://arxiv.org/abs/2610.40646)** (2026) — 不追求万能夹爪，而是用固定的机器人侧接口加低成本、带触觉传感器的工具侧适配器，把日常厨具变成可自动更换的末端执行器，兼容多种机器人平台；配套遥操作采集示范，模仿学习策略完成煎豆腐、拌沙拉、翻肉等工具任务。 · [项目页](https://personalrobotics.github.io/SwapBot)
- **[UMI-Live for In-The-Wild Bimanual Robotics Data Collection](https://arxiv.org/abs/2610.39385)** (2026) — 全栈开源的双手 UMI 野外数据采集系统：手持设备集成相机、激光雷达-惯性传感、板载算力与电源，无需外部追踪或现场标定；异步 SLAM 流水线直接产出可训练数据集，并发布 40 小时数据、硬件设计与复现指南，用 π0.5 和 MolmoAct2 微调验证数据质量。 · [代码](https://github.com/AfterQuery-Research/umi-live) · [项目页](https://umi-live.github.io/)
- **[EgoThumb: A Vision-Driven Supernumerary Robotic Thumb for Autonomous Grasp and Holding Assistance](https://arxiv.org/abs/2610.37582)** (2026) — 开源的可穿戴“第六指”：紧凑的双腱驱动手指，电机移到前臂以减轻末端重量；模仿学习策略直接把掌心相机图像映射为关节位置，从视觉中推断使用者意图，无需显式手势触发，软硬件全部开源。 · [代码](https://github.com/JayeFu/ego_thumb_firmware) · [项目页](https://ego-thumb.github.io)
- **[OpenJaws: An Open Hardware UMI Framework with Stereo Localization for Generalist Manipulation](https://arxiv.org/abs/2610.36598)** (2026) — 完全开源的 UMI 式手持夹爪：3D 打印、标准 ISO 接口，用低成本双目相机获得公制尺度、低漂移的轨迹，并提出手持采集设备定位精度基准 UMI-Loc-Bench-v1；硬件、软件与数据以可商用许可证发布。 · [项目页](https://open-jaws.github.io/)
- **[DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection](https://arxiv.org/abs/2610.32969)** (2026) — 便携手持式数据采集装置，面向高自由度机器人灵巧手；采集与部署使用同一只机械手，无需从人手动作重定向，也无需搭建完整机器人系统。 · [代码](https://github.com/amazon-far/dexport) · [项目页](https://amberxie88.github.io/dexport/)

**[查看全部 40 条 →](lists/hardware.zh-CN.md)**

<!-- radar:end -->

## 相关列表与学习资源

领域内其他优秀的资源整理，以及推荐给新手的课程和文档。本雷达与它们互补：提供搜索、每日论文流和中英双语要点。

<!-- resources:start -->

**相关列表**

- [Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide) `中文` — 中文具身智能入门指南，从基础知识一路讲到各研究方向。
- [Embodied_AI_Paper_List (HCPLab-SYSU)](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) — 配合具身智能综述的论文列表，按感知、交互、智能体与 sim-to-real 组织。
- [awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) — 专注于人形机器人学习的论文列表。
- [Awesome-Robotics-Foundation-Models](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models) — 机器人基础模型相关论文，来自综述《Foundation Models in Robotics》。
- [awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) — 持续更新的视觉-语言-动作（VLA）与视觉-语言导航（VLN）论文列表。

**课程与教材**

- [Robotic Manipulation (MIT 6.4210, Russ Tedrake)](https://manipulation.csail.mit.edu/) — 免费在线教材与课程，涵盖操作中的感知、规划与控制，附 Drake 交互笔记本。
- [Underactuated Robotics (MIT, Russ Tedrake)](https://underactuated.mit.edu/) — 免费在线教材，讲解行走、飞行、游动机器人的非线性动力学、最优控制与轨迹优化。
- [CS 285 Deep Reinforcement Learning (UC Berkeley)](https://rail.eecs.berkeley.edu/deeprlcourse/) — Sergey Levine 的深度强化学习课程，讲座视频与课件公开。
- [蘑菇书 EasyRL (Datawhale)](https://github.com/datawhalechina/easy-rl) `中文` — 广受欢迎的开源中文强化学习教程（从 Q-learning 到 PPO、DDPG、TD3），附代码，可在线阅读。
- [动手学强化学习 (Hands-on RL)](https://github.com/boyu-ai/Hands-on-RL) `中文` — 以可运行的 Jupyter 笔记本组织的中文强化学习教材，在线版见 hrl.boyuai.com。

**工具文档**

- [LeRobot documentation](https://huggingface.co/docs/lerobot) — Hugging Face LeRobot 实操文档：采集数据、训练 ACT/扩散/VLA 策略并在低成本机械臂上运行。
- [Isaac Lab documentation](https://isaac-sim.github.io/IsaacLab/) — NVIDIA GPU 并行机器人学习框架的文档与教程。
- [MuJoCo documentation](https://mujoco.readthedocs.io/) — MuJoCo 物理引擎的参考与建模指南（MJX、MJCF、Python 绑定）。

**社区**

- [古月居 (GuYueHome)](https://www.guyuehome.com/) `中文` — 历史悠久的中文 ROS 与机器人社区，提供教程与论坛。

<!-- resources:end -->

## 参与贡献

发现缺少的好论文、代码库、数据集或机器人，或者发现错误？欢迎 [提交 issue](https://github.com/hu-zlatan/embodied-ai-radar/issues/new)，或提交一个在 `data/curated/<主题>.yaml` 中新增条目的 PR。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 项目如何运作

本仓库由 **AI 智能体**（Anthropic 的 Claude）按计划自动构建和维护，并由 [@hu-zlatan](https://github.com/hu-zlatan) 监督。智能体的工作章程见 [AUTOPILOT.md](AUTOPILOT.md)，笔记、决策和运行日志见 [`.autopilot/`](.autopilot)。数据绝不编造：未通过核验的条目会被修正或删除。

## 许可

代码：[MIT](LICENSE)。精选文本与数据：[CC BY 4.0](LICENSE-DATA.md)。arXiv 元数据：CC0，来自 [arXiv API](https://info.arxiv.org/help/api/index.html)。
