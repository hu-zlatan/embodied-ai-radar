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
- **[Ψ0: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)** (2026) — 面向人形移动操作的开放基础模型，主张因运动学差异，不宜直接混合人类与人形数据共同训练。
- **[Asynchronous Robot Policies](https://arxiv.org/abs/2611.05155)** (2026) — 把低频更新语义记忆的大型 VLM 与高频出动作的轻量专家解耦，并针对陈旧和延迟训练；报告 VLM 降到标称频率十分之一时性能无明显损失。 · [项目页](https://arp.insait.ai)
- **[Bayesian Active Learning for Intent Disambiguation in Interactive Robot Planning](https://arxiv.org/abs/2609.34270)** (2026) — 把澄清提问视为信号时序逻辑规约上的贝叶斯主动学习，机器人提问更少，并向形式化规划器交付可验证的任务。
- **[Do Agentic Policies Need to Look at Every Step? Geometric Abstraction for Reasoning and Action](https://arxiv.org/abs/2611.05058)** (2026) — 把常规空间推理从图像转到文本：语言模型直接读取局部刷新的三维符号场景，仅在需要时看图；报告多步任务完成度提高，图像查询大幅减少。 · [项目页](https://geometric-abstraction.github.io)
- **[Efficient Long-Horizon Vision-Language-Action Models via Static-Dynamic Disentanglement](https://arxiv.org/abs/2602.03983)** (2026) — DySta 把视觉输入分成静态和动态 token，静态部分只保留一份并复用 KV 缓存，从而延长 VLA 上下文并加快推理。
- **[Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs](https://arxiv.org/abs/2611.04391)** (2026) — H2RB 用非配对的人类与机器人示教微调预训练 VLA：按几何对齐观测，并共享动作潜变量；报告真机任务的物体迁移得分从 8.0 升至 51.8。 · [项目页](https://junhyeong-park.me/h2rb/)

**[查看全部 158 条 →](lists/vla.zh-CN.md)**

<a id="manipulation"></a>
### 操作与灵巧手

_模仿学习、扩散策略、抓取、双臂与灵巧操作。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/manipulation.html)

- ⭐ **[AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data](https://arxiv.org/abs/2611.03815)** (2026) — 从 16,151 小时手持夹爪演示中学习，全程不采机器人数据；报告十项任务平均成功率 78%，其他 VLA 最好为 27%，并开放数据集、权重和后训练方案。 · [项目页](https://a-0.airoa.io)
- ⭐ **[Generalizable Humanoid Manipulation with 3D Diffusion Policies](https://arxiv.org/abs/2410.10803)** (2024) — iDP3：上半身全身遥操作、带三维激光雷达的 25 自由度人形，加上改进的三维扩散策略，使技能不再局限于单一场景。 · [代码](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy) · [项目页](https://humanoid-manipulation.github.io/)
- ⭐ **[Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](https://arxiv.org/abs/2402.10329)** (2024) — 手持夹爪加 GoPro 可随处采集演示，训练出的策略可直接迁移到机械臂。 · [代码](https://github.com/real-stanford/universal_manipulation_interface)
- ⭐ **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** (2023) — 以去噪方式生成动作序列，比回归更能处理多模态演示，已成为模仿学习标准基线。 · [代码](https://github.com/real-stanford/diffusion_policy)
- ⭐ **[Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705)** (2023) — ALOHA + ACT：约 2 万美元的双臂遥操作平台，加上动作分块 Transformer，约 50 条演示即可学会精细任务。 · [代码](https://github.com/tonyzhaozh/act)
- **[A Tutorial on Shape Servoing of Deformable Objects-Part II: Advanced Concepts](https://arxiv.org/abs/2611.03825)** (2026) — 基于数据与雅可比的形状控制教程第二部分：哪些形变可达、特征选择如何影响行为，以及控制回路失效的三种方式。 · [代码](https://github.com/nachocz/tutorial_on_shape_servoing_of_deformable_objects) · [项目页](https://nachocz.github.io/tutorial_on_shape_servoing_of_deformable_objects/)
- **[Combining Constrained Sampling and Reinforcement Learning for Manipulation](https://arxiv.org/abs/2602.08557)** (2026) — 用感知接触的约束状态采样器重置回合，覆盖多样接触模式，帮助 RL 探索接触丰富任务；可训练通用的手内和全身操作策略。 · [项目页](https://www.user.tu-berlin.de/mtoussai/26-CSRL/)
- **[DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation](https://arxiv.org/abs/2611.05119)** (2026) — 把灵巧操作目标定义为手与物体的联合构型，从合成构型对学习统一的转移基元，无需人类动作；报告仿真未见物体成功率 69.4%，200 次真机转移成功率 61.5%。 · [项目页](https://dex-hot.github.io/)
- **[Enabling Robust Cloth Manipulation via Inference-Time Simulator-in-the-Loop Refinement](https://arxiv.org/abs/2606.24552)** (2026) — 仅凭单张 RGB 在线修正布料动作：先由 real-to-sim 模块估计布料状态，再用仿真器并行推演和先验引导的 MPPI 修正策略轨迹。 · [项目页](https://silr-cloth.github.io/)
- **[FEIJOA: Task-Driven Grounding and Execution for Mobile Manipulation](https://arxiv.org/abs/2611.04080)** (2026) — 语言模型智能体在测试时对带位姿的 RGB-D 扫描做指令落地，不依赖预建表示；Spot 真机 50 次试验成功 35 次，失败大多来自物理技能而非推理。 · [项目页](https://williamshen-nz.github.io/feijoa/)
- **[KPGrasp: Scalable Keypoint Flow Matching for Dexterous Grasp Generation](https://arxiv.org/abs/2606.09314)** (2026) — 以 3D 手部关键点表示灵巧抓取，用普通 Transformer 流模型生成，无需接触损失或后处理优化；报告 Dexonomy 成功率 76.3%，每次抓取 0.032 秒。 · [项目页](https://yuansen-huang.github.io/KPGrasp-page/)
- **[Noise-Invariant Spatial Encoding for 3D Manipulation Policies under Depth Corruption](https://arxiv.org/abs/2610.24674)** (2026) — NISE 针对 3D 策略在真实深度噪声下的急剧失效，把位置不确定性带入注意力计算；在透明和反光物体上用普通 RGB-D 相机测试。

**[查看全部 79 条 →](lists/manipulation.zh-CN.md)**

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
- **[Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight](https://arxiv.org/abs/2611.04839)** (2026) — 用潜空间世界动作模型在执行前为人形指令序列打分，并逐步重规划；报告七项真机任务成功率 85.7%，GR00T N1.7 为 70.0%。 · [项目页](https://ju6276.github.io/Action-Grounded-Foresight/)
- **[Deep Whole-body Parkour](https://arxiv.org/abs/2601.07701)** (2026) — 将外部感知融入全身动作跟踪，让人形机器人在不平整地形上完成高动态的非行走类技能。 · [代码](https://github.com/project-instinct/InstinctLab) · [项目页](https://project-instinct.github.io/deep-whole-body-parkour)
- **[HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors](https://arxiv.org/abs/2611.05113)** (2026) — 让人形底层控制器在场景中真实带着物体做动作模仿训练，再在其上训练高层策略；在宇树 G1 上可搬运不同箱子，并能从掉落中恢复。
- **[Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids](https://arxiv.org/abs/2601.07718)** (2026) — 端到端感知框架，将深度输入映射到控制，实现人形机器人在多样非结构化地形上徒步。 · [项目页](https://project-instinct.github.io/hiking-in-the-wild)
- **[HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos](https://arxiv.org/abs/2602.02473)** (2026) — 把人类视频转化为可泛化的真实人形交互技能，无需按任务设计。
- **[Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking](https://arxiv.org/abs/2606.03985)** (2026) — 在 20 亿帧重定向动作语料上预训练的 GPT 式因果 Transformer，跟踪高动态全身动作，并零次微调泛化到未见动作。 · [代码](https://github.com/GalaxyGeneralRobotics/Humanoid-GPT) · [项目页](https://qizekun.github.io/Humanoid-GPT/)
- **[Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL](https://arxiv.org/abs/2608.12063)** (2026) — 在仿真中用采样 MPC 自动生成专家数据，再以稀疏奖励训练离策略 RL，免去奖励塑形；已部署到带臂 Spot 和 G1 人形机器人。

**[查看全部 110 条 →](lists/locomotion.zh-CN.md)**

<a id="world-models"></a>
### 世界模型

_学习的动力学模型、视频世界模型、世界动作模型（WAM）与基于模型的强化学习。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/world-models.html)

- ⭐ **[Cosmos 3: Omnimodal World Models for Physical AI](https://arxiv.org/abs/2606.02800)** (2026) — 全模态世界模型家族，用一个 Mixture-of-Transformers 同时处理语言、图像、视频、音频和动作，把 VLM、视频生成、世界模拟器和世界动作模型并入同一框架。 · [代码](https://github.com/nvidia/cosmos) · [项目页](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)
- ⭐ **[DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](https://arxiv.org/abs/2602.06949)** (2026) — 在 4.4 万小时第一视角人类视频上预训练的基础世界模型，用连续潜动作代替缺失的动作标签，再用小规模机器人数据后训练。 · [项目页](https://dreamdojo-world.github.io/)
- ⭐ **[OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398)** (2026) — 开放研究栈，把世界动作模型拆成可组合模块，并通过对照实验研究该从视频先验继承什么、世界学习与动作学习如何相互作用。 · [代码](https://github.com/OpenWAM-Official/OpenWAM) · [项目页](https://openwam-official.github.io/)
- ⭐ **[RoboJEPA: Scaling Robotic Latent World Models](https://arxiv.org/abs/2610.10515)** (2026) — 跨 12 种机器人形态训练的 JEPA 世界模型；其想象误差随算力服从幂律，因此可以预测超出拟合规模时的模型质量。 · [代码](https://github.com/facebookresearch/robo_jepa) · [项目页](https://robojepa.github.io/)
- ⭐ **[World Action Models: A Survey](https://arxiv.org/abs/2606.20781)** (2026) — 厘清 WAM 与世界模型、视频生成模型、VLA 的区别，并按生成内容（渲染、潜空间或不生成）和架构分类；结论是领域正走向少生成未来，只保留控制所需。 · [项目页](https://world-action-models.github.io/)
- ⭐ **[Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104)** (2023) — DreamerV3：一套超参数适用于 150 多个任务，包括从零开始在《我的世界》中挖到钻石。 · [代码](https://github.com/danijar/dreamerv3)
- **[ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment](https://arxiv.org/abs/2603.23376)** (2026) — 14B 动作可控视频模型，基于 300 万条操作片段训练，用 DPO 式后训练抑制穿模等非物理现象，并提出 EZSbench 基准。 · [代码](https://github.com/amap-cvlab/ABot-PhysWorld)
- **[Being-H0.7: A Latent World-Action Model from Egocentric Videos](https://arxiv.org/abs/2605.00078)** (2026) — 潜空间世界动作模型，在 VLA 式策略中加入面向未来的潜查询，并用利用未来信息的分支训练，全程不生成未来帧。
- **[Causal World Modeling for Robot Control](https://arxiv.org/abs/2601.21998)** (2026) — LingBot-VA：同时学习帧预测和策略的自回归扩散框架，具有视频动作共享潜空间、闭环推演和异步推理。 · [代码](https://github.com/Robbyant/lingbot-va) · [项目页](https://technology.robbyant.com/lingbot-va)
- **[Do World Action Models Generalize Better than VLAs? A Robustness Study](https://arxiv.org/abs/2603.22078)** (2026) — 在扰动下对比世界动作模型与 VLA 的鲁棒性研究，用于检验显式未来预测能带来更好泛化这一说法。 · [项目页](https://robot-robustness.github.io/RoboTwin2.0-Plus/)
- **[DreamX: Video Diffusion Model is a Universal Latent Action Learner](https://arxiv.org/abs/2611.05377)** (2026) — 复用预训练视频扩散模型提取紧凑潜动作（每帧 1,200 压到 4 个 token），作为人、机器人和不同环境之间的共享接口，并支持零示教动作迁移。 · [代码](https://github.com/cvlab-kaist/DreamX) · [项目页](https://cvlab-kaist.github.io/DreamX/)
- **[Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666)** (2026) — 追问世界动作模型在测试时是否需要想象未来：训练时保留视频联合训练，推理时跳过视频生成，以对照实验区分两者的作用。 · [代码](https://github.com/yuantianyuan01/FastWAM) · [项目页](https://yuantianyuan01.github.io/FastWAM/)

**[查看全部 88 条 →](lists/world-models.zh-CN.md)**

<a id="navigation"></a>
### 导航与具身智能体

_视觉语言导航、具身问答、移动操作与大模型规划。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/navigation.html)

- ⭐ **[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)** (2022) — SayCan：大模型提出步骤，学习到的价值函数评估机器人当下实际能做什么。
- **[Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware](https://arxiv.org/abs/2611.04392)** (2026) — 紧凑的 JEPA 加流匹配四旋翼策略，报告异常坦率：行为克隆 60 次任务全败，DAgger 进入瓶颈，运行时安全层将仿真森林任务成功率从 21.1% 提至 52.2%。 · [代码](https://github.com/ylee-sling/Aero-VPA) · [项目页](https://huggingface.co/ylee-sling/aero-vpa)
- **[Collaborative Planning for UAV-UGV Teams under Operational Constraints via Masked Error-bounded Neuro-Symbolic Diffusion](https://arxiv.org/abs/2610.18850)** (2026) — MEND 用掩码扩散规划无人机与地面车协同充电任务，在执行时通过逻辑动作掩码强制满足运行约束；在真实地图和实体机器人队伍上测试。
- **[Driving, Fast or Slow? Neuro-Symbolic Guidance for Motion Prediction in Multi-Modal Ground Mobility](https://arxiv.org/abs/2606.15251)** (2026) — TraCS 将由自然语言交规生成的可解释概率逻辑加到黑盒运动预测模型上；报告在 Argoverse 2 上稳定提升。Oral 论文。
- **[From Region Arrival to Instance-Level Grounding in Vision-and-Language Navigation](https://arxiv.org/abs/2607.03792)** (2026) — 指出 VLN 成功率掩盖了“最后 3 米定位缺口”：智能体停在附近却未对准目标。提出实例级指标和可接入任意主干的修正模块 REALM。
- **[WayTrace: A Map-to-Language-to-Trace Hierarchy for Embodied Urban Navigation](https://arxiv.org/abs/2611.05129)** (2026) — 视觉语言模型把网络地图导航拆成一条条原子指令，预测器在图像上画出路径，强化学习负责跟踪；轮腿机器人完成最长 1.37 公里的真实任务。 · [项目页](https://way-trace.github.io)
- **[OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation](https://arxiv.org/abs/2610.39287)** (2026) — 面向无人机的机载 VLA：同一视觉-语言表征同时支撑语义理解、空间推理与闭环航点控制。 · [代码](https://github.com/Ideal-ljl/AeroBrain) · [项目页](https://ideal-ljl.github.io/AeroBrain/)
- **[OSCAR: Obstacle Survival Curves for Adaptive Robot Navigation](https://arxiv.org/abs/2606.00990)** (2026) — CoRL 2026 Spotlight。通过建模各类障碍物通常停留多久，决定在路线受阻时等待还是改道。
- **[SidewalkBench: Benchmarking Visual Navigation on Urban Sidewalks](https://arxiv.org/abs/2606.16953)** (2026) — CoRL 2026 Spotlight。城市人行道视觉导航基准，基于 Isaac Sim，包含程序生成与真实世界环境。 · [代码](https://github.com/VAIL-UCLA/SidewalkBench) · [项目页](https://vail-ucla.github.io/SidewalkBench/)
- **[Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation](https://arxiv.org/abs/2610.34674)** (2026) — OSMA-Bench 用仅障碍物类型不同的配对场景，检验导航策略能否按障碍物危险程度调整间距与速度，并提出语义敏感度指数 SSI。结果显示 VLM 与 VLA 策略能识别哪些障碍更危险，却很少把这种判断体现在实际运动中；在 VLM 方案中加入显式参数推断步骤有所改善。 · [代码](https://github.com/OSMA-Bench/OSMA-Bench) · [项目页](https://osma-bench.github.io/)
- **[Gaussian Episodic Memory for Long-Term Spatiotemporal Reasoning](https://arxiv.org/abs/2610.33158)** (2026) — GEMS 维护一张只在场景变化处增量更新的 3DGS 地图，智能体按需渲染新视角来回答时空问题和定位物体；同时发布 GEMS-Bench（3 个真实 + 12 个合成环境，473 个问答对），报告在物体定位和时空问答上优于近期基线。 · [项目页](https://abwerby.github.io/GEMS/)
- **[One Scan is Enough: Demonstration-Free Adaptation for Language-Guided Navigation](https://arxiv.org/abs/2610.33794)** (2026) — 只需用 iPhone 扫描一次新建筑：扫描被编译成训练环境并自动合成带语言指令的导航回合，再用无评论家的闭式 Pareto 效用适配策略；报告真机成功率 85%，用人类示教后训练的基线为 49%。

**[查看全部 42 条 →](lists/navigation.zh-CN.md)**

<a id="perception"></a>
### 感知、SLAM 与三维建图

_视觉/激光 SLAM 与里程计、三维重建、物体位姿、深度估计与开放词汇场景地图。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/perception.html)

- ⭐ **[Segment Anything](https://arxiv.org/abs/2304.02643)** (2023) — SAM：可用点、框、掩码提示的分割模型，在 10 亿级掩码上训练；已成为机器人感知流程中获取物体掩码的常用基础组件。 · [代码](https://github.com/facebookresearch/segment-anything)
- ⭐ **[ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](https://arxiv.org/abs/2007.11898)** (2020) — 最常用的特征点 SLAM 库：支持单目、双目与 RGB-D，可融合 IMU，并支持多地图重定位。 · [代码](https://github.com/UZ-SLAMLab/ORB_SLAM3)
- **[Articulated 3D Scene Graphs for Open-World Mobile Manipulation](https://arxiv.org/abs/2602.16356)** (2026) — MoMa-SG 从 RGB-D 序列构建包含物体铰接方式的 3D 场景图，并发布 Arti4D-Semantic 数据集；在四足和移动操作机器人上演示。 · [项目页](https://momasg.cs.uni-freiburg.de)
- **[MosaicIMU: Composing Carrier Experts for Generalizable Neural Inertial Odometry](https://arxiv.org/abs/2606.09355)** (2026) — 面向多种载体的神经惯性里程计：路由器组合各载体专家，新载体通过轻量残差分支适配。报告 ATE 比学习型基线降低 40%。
- **[Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping](https://arxiv.org/abs/1910.02490)** (2019) — 开源 C++ 实时度量-语义视觉惯性 SLAM 库，模块化包含 VIO、鲁棒位姿图、快速三维网格与稠密语义重建。 · [代码](https://github.com/MIT-SPARK/Kimera)
- **[AnchorHEC: Targetless Hand-Eye Calibration of Wrist and Fixed Cameras](https://arxiv.org/abs/2611.02884)** (2026) — 无需标定板，用 RGB、正运动学和三维基础模型同时标定腕部与固定相机；仿真中平移和旋转误差比基于重建的基线分别降低 86.4% 和 71.6%，并在真机上验证。 · [项目页](https://hwanggb.github.io/AnchorHEC/)
- **[Anchor3R: Streaming 3D Reconstruction with Transient Anchors for Long-Horizon Visual Mapping](https://arxiv.org/abs/2606.05035)** (2026) — CoRL 2026 Spotlight。以当前帧为中心的流式三维重建：在当前帧坐标系预测窗口相对位姿与局部几何，以抑制长时漂移。 · [代码](https://github.com/polar-explorer/Anchor3R)
- **[OpenVIO: A Versatile Open-Source Visual-Inertial Odometry System](https://arxiv.org/abs/2610.41671)** (2026) — MIT 许可的开源视觉惯性里程计，面向科研与实际应用。支持针孔、鱼眼相机及拼接 360° 图像，并在公开数据集上与其他开源 VIO 系统做了对比。 · [代码](https://github.com/93won/openvio)
- **[ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models](https://arxiv.org/abs/2610.27040)** (2026) — 用自动标注的机器人操作录像加多来源视觉数据构建约 150 万条可验证的定位监督，微调 Qwen3.5-9B；报告在七个公开视觉定位基准上平均 75.41 分，GPT-6 Astra 为 73.68。 · [代码](https://github.com/DAXIAORobotics/ACE-Brain-0.6) · [项目页](https://daxiaorobotics.github.io/ACE-Brain-0.6/)
- **[Which Depth Estimator for Jetson AGX Orin? A 2026 Benchmark of Monocular and Stereo Methods](https://arxiv.org/abs/2610.27199)** (2026) — 给机器人开发者的实测数据：在 Jetson AGX Orin 上用 TensorRT 运行九类单目与双目深度估计模型（Depth Anything V2/3、Depth Pro、MoGe-2、Fast-FoundationStereo 等），并评测度量精度与速度。 · [代码](https://github.com/nodarhub/orin-depth-benchmark)
- **[SpaRV: Sparse Radiance Voxels for Scalable Geometrically Consistent LiDAR-Visual Mapping and Rendering](https://arxiv.org/abs/2610.25665)** (2026) — 用激光雷达与相机数据构建稀疏体素辐射场地图，针对机器人数据视角少、位姿有误差、场景大的问题，在保证几何精度的同时控制显存占用。 · [代码](https://github.com/hku-mars/SpaRV)
- **[Vision as Proprioception: Estimating Humanoid Robot Pose from Video](https://arxiv.org/abs/2610.25288)** (2026) — HumanoidPose 仅凭视频恢复人形机器人的全身关节构型：适用于拿不到机载状态的场景，也能把网上的机器人视频变成训练数据。 · [代码](https://github.com/eth-siplab/HumanoidPose)

**[查看全部 31 条 →](lists/perception.zh-CN.md)**

<a id="control"></a>
### 规划、控制与安全

_运动规划、轨迹优化、模型预测控制、安全滤波器与安全的学习型控制。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/control.html)

- ⭐ **[cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation](https://arxiv.org/abs/2310.17274)** (2023) — 面向机械臂的 GPU 并行运动生成：同时运行大量轨迹优化，在毫秒级给出无碰撞且平滑的轨迹。 · [代码](https://github.com/NVlabs/curobo)
- **[PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning](https://arxiv.org/abs/2611.05372)** (2026) — 学习式目标条件逆运动学，能保持位置控制器静止时所需的偏置；报告在 93.5% 的留出仿真任务上误差低于 1 mm 和 0.2°，并可直接在真实机械臂上训练。 · [代码](https://github.com/Tinaliu0123/PolicyIK)
- **[Scalable Deep Unfolding of Conic Optimizers](https://arxiv.org/abs/2606.13825)** (2026) — 通过无矩阵隐式微分和稳定的半正定投影梯度，让深度展开适用于大规模锥优化求解器；报告在基于 SDP 的规划上最高提速 50 倍。
- **[cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots](https://arxiv.org/abs/2603.05493)** (2026) — cuRoboV2 新增考虑力矩限制的 B 样条轨迹优化和 GPU 原生 TSDF/ESDF 感知，面向高自由度机器人。 · [代码](https://github.com/NVlabs/curobo)
- **[PyRoki: A Modular Toolkit for Robot Kinematic Optimization](https://arxiv.org/abs/2505.03728)** (2025) — PyRoki：模块化、跨平台的运动学优化工具包，可原生运行在 CPU、GPU 和 TPU 上。 · [项目页](https://pyroki-toolkit.github.io)
- **[RAM: Reachability Across Morphologies](https://arxiv.org/abs/2606.09108)** (2026) — CoRL 2026 Spotlight。以形态为条件的隐式神经位姿可达性模型，可微、考虑自碰撞，并能泛化到未见形态。 · [代码](https://github.com/TimWalter/ram) · [项目页](https://timwalter.github.io/ram)
- **[TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation](https://arxiv.org/abs/2606.06218)** (2026) — CoRL 2026 Spotlight。面向富接触动作迁移的模块，应对仿真到现实、负载与个体差异，用于替代域随机化或系统辨识。 · [代码](https://github.com/Dongwon-Son/TAM) · [项目页](https://dongwon-son.github.io/tam-project-page/)
- **[A generalist policy for muscle-driven control across individual musculoskeletal models](https://arxiv.org/abs/2610.36535)** (2026) — MyoAcross 结合个体化肌骨模型构建、形态条件策略学习与虚拟模型增广，用一个策略驱动不同个体的肌骨模型跟踪参考动作而无需逐个微调；报告在 31 个未见个体模型上完成率 99.24%，跟踪误差比无条件 MLP 降低 22.6%，并与 120 人的地面反力和肌电数据做了对比。 · [项目页](https://woodater-thu.github.io/MyoAcross/)
- **[Keeping Contact: Task-Adaptive Friction Margins for Bimanual Non-Prehensile Manipulation](https://arxiv.org/abs/2610.36961)** (2026) — 以带符号摩擦距离度量防滑裕度，并在双臂绕支点倾转物体时按任务需求自适应调整；一系列二阶锥规划给出全局最优接触力。真机实验显示自适应裕度优于固定裕度和无裕度。 · [项目页](https://keeping-contact.github.io/)
- **[CusADi2: Latency-Optimized Batch Computation of Robot Kinematics, Jacobians, and Hessians on the GPU](https://arxiv.org/abs/2610.25476)** (2026) — 在 GPU 上以低延迟批量计算运动学、雅可比与海森矩阵，面向在线运行的采样式与梯度式轨迹优化。 · [代码](https://github.com/johnviljoen/cusadi2)
- **[PrismPlan: A Shared GPU Substrate for Motion Planning Across Paradigms](https://arxiv.org/abs/2610.23884)** (2026) — 一次性实现批量 GPU 碰撞检测与正运动学，在其上运行采样、搜索和优化三类规划器，使三种范式可以公平比较。 · [代码](https://github.com/XiaoyubotMotionTeam/PrismPlan)
- **[Sub-Millisecond Reflexes for Continuous Physical Human-Robot Interaction](https://arxiv.org/abs/2610.21913)** (2026) — 开源的 ROS 2 多模式控制器，可在亚毫秒内切换控制模式并触发安全反射而无需中断任务；在 Franka 机械臂上验证。 · [代码](https://github.com/RoboRef/franka_reflex_engine)

**[查看全部 32 条 →](lists/control.zh-CN.md)**

<a id="learning"></a>
### 机器人学习：强化学习与模仿学习

_面向机器人的强化学习、模仿学习与策略后训练方法，不限机器人形态。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/learning.html)

- ⭐ **[Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](https://arxiv.org/abs/2410.21845)** (2024) — HIL-SERL：结合人类纠正的真机强化学习，报告称在精密装配与动态任务上经数小时训练即可接近满分成功率。 · [代码](https://github.com/rail-berkeley/hil-serl)
- ⭐ **[Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)** (2017) — 采用截断目标的策略梯度方法，是大多数 GPU 并行仿真训练（运动控制、灵巧操作）背后的算法。
- **[Control-Ready Uncertainty for Trajectory Diffusion](https://arxiv.org/abs/2610.12431)** (2026) — SCOPE 通过蒸馏得分函数曲率，让扩散轨迹模型无需蒙特卡洛采样即可给出校准的不确定性管道；在人群导航和 Franka 操作上测试。 · [项目页](https://zackaxue.github.io/SCOPE-project-page/)
- **[FedGuide: Diffusion Prior Alignment and Value Baseline Guidance for Heterogeneous Federated Reinforcement Learning](https://arxiv.org/abs/2609.18964)** (2026) — 面向异构客户端的联邦强化学习：不再平均策略，而是用最优传输聚合扩散行为先验，并加入低方差的 DICE 价值基线。
- **[GSBR: Geometric Support Behavior Regularization for Online RL](https://arxiv.org/abs/2611.05295)** (2026) — 在预训练策略之上做在线强化学习，按动作到其支撑集的距离施加惩罚：集内不罚，集外平滑增长；报告 19 个基准任务的平均成功率从 33% 升至 95%。 · [项目页](https://charlesxu0124.github.io/gsbr/)
- **[SCoCaT: Success Conditioned Constrained Reinforcement Learning for Spacecraft Docking](https://arxiv.org/abs/2609.06061)** (2026) — 发现基于终止的约束强化学习在目标附近约束收紧时会学会回避目标，并用稠密成功信号的辅助价值网络解决；在航天器对接任务上验证。
- **[TARC: Time-Adaptive Robotic Control](https://arxiv.org/abs/2510.23176)** (2026) — 策略同时预测动作及其保持时长。报告在遥控车、Unitree Go1 和仿真 VLA 上以不到一半的控制频率达到高频控制的性能。 · [项目页](https://arnavsukhija.github.io/projects/tarc)
- **[Towards Embodiment Scaling Laws in Robot Locomotion](https://arxiv.org/abs/2505.05753)** (2025) — 在约 1000 个生成的机器人形态上检验“形态缩放定律”：用更多形态训练能否提升对未见形态的泛化？ · [项目页](https://embodiment-scaling-laws.github.io/)
- **[Behavior Graphs: Unsupervised Graph Structures for Interpreting Robot Deployment Data](https://arxiv.org/abs/2611.00405)** (2026) — 把策略回放压缩成一张有向图，将行为模式与结果相连，帮助决定下一步采集什么数据。在三个真实任务的用户研究中，18 名参与者有 16 名更喜欢它而非回放视频。 · [项目页](https://try.behavior-graphs.com/)
- **[Beyond Validation Loss: Coverage and Reliability Dynamics in Robot Policy Pretraining](https://arxiv.org/abs/2611.01565)** (2026) — 提出跟踪闭环 pass@k（k 次尝试至少成功一次的概率）。pass@1 相同的检查点在后训练中可能表现不同，因此给出兼顾覆盖度与可靠性的离线检查点选择方法。 · [项目页](https://zhanyisun.github.io/robot-policy-learning-dynamics/)
- **[D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models](https://arxiv.org/abs/2611.03622)** (2026) — 只靠提示词的任务进度评估：先让 VLM 客观描述画面并定义绝对成功标准，再按明确评分表打分，减少对失败执行“幻觉式”的进度判断，其奖励可用于下游强化学习。 · [代码](https://github.com/memmelma/dna) · [项目页](https://weirdlabuw.github.io/dna)
- **[When Robots Outweigh Objects: How Inertia Mismatch Shapes Robot Policy Learning](https://arxiv.org/abs/2611.03501)** (2026) — 在仿真中改变机器人与物体质量：强化学习影响不大，行为克隆则在机器人比物体轻时更可靠，增加数据只能缩小而无法消除差距。采集低惯量示教可部分缓解。 · [项目页](https://younghyopark.me/inertia-mismatch/)

**[查看全部 53 条 →](lists/learning.zh-CN.md)**

<a id="sim"></a>
### 仿真与 Sim-to-Real

_物理仿真器、GPU 并行训练与向真实机器人迁移。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/sim.html)

- ⭐ **[When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks](https://arxiv.org/abs/2610.41857)** (2026) — 审计仿真基准：不少“策略失败”其实是物理引擎把物体弹飞。SimuGuard 为 LIBERO、RoboTwin、RoboCasa、RoboDojo 提供审计插件，把 RoboTwin 上的问题追溯到碰撞检测的一个常量；仅改动它，异常回合由 100 回合 12 次降到 0，五个容器任务成功率由 89% 升到 98%。 · [代码](https://github.com/ALEXander22568/simuguard)
- ⭐ **[MuJoCo](https://mujoco.org/)** (2012) — 快速准确的接触物理仿真，机器人学习研究的默认仿真器，由 DeepMind 开源。 · [代码](https://github.com/google-deepmind/mujoco)
- **[Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot](https://arxiv.org/abs/2601.02078)** (2026) — Genie Sim 3.0：面向操作的仿真平台，用 LLM 工具依自然语言生成场景，并提供基于 LLM 与 VLM 的自动化评测基准。 · [代码](https://github.com/AgibotTech/genie_sim)
- **[Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](https://arxiv.org/abs/2607.13451)** (2026) — PGRD 以可优化的弹簧质点模型为骨架，加上学习得到的残差来仿真可变形物体，报告精度优于单用任一方法；可用于 MPC 和动作条件视频预测。 · [项目页](https://pgrd-robot.github.io/)
- **[GaussGym: An open-source real-to-sim framework for learning locomotion from pixels](https://arxiv.org/abs/2510.15352)** (2025) — 把 3D 高斯溅射作为渲染器接入矢量化物理仿真，报告在消费级 GPU 上超过每秒 10 万步，用于从像素学习。
- **[Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation](https://arxiv.org/abs/2504.12908)** (2025) — 结合 IPC 与 ABD 的 GPU 触觉仿真；作者报告在数千并行环境下达到实时速度的 18 倍。
- **[BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark](https://arxiv.org/abs/2407.07788)** (2024) — 面向移动双臂机器人的基准，含 40 个家庭任务（从抓取到厨房清洁），均配人类采集的演示。 · [项目页](https://chernyadev.github.io/bigym/)
- **[DIFFTACTILE: A Physics-based Differentiable Tactile Simulator for Contact-rich Robotic Manipulation](https://arxiv.org/abs/2403.08716)** (2024) — 可微触觉仿真器，用 FEM 软体模型模拟弹性体，面向多种材料的接触，而非主要针对刚体。 · [代码](https://github.com/Genesis-Embodied-AI/DiffTactile)
- **[GRUtopia: Dream General Robots in a City at Scale](https://arxiv.org/abs/2407.10943)** (2024) — 面向多种机器人的交互式三维仿真社会；GRScenes 含 10 万标注场景、89 个类别，可组合成城市级环境。 · [代码](https://github.com/OpenRobotLab/GRUtopia)
- **[ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks](https://arxiv.org/abs/2412.13211)** (2024) — GPU 加速的 Home Assistant Benchmark，采用真实低层控制；作者报告速度超过此前“魔法抓取”实现的 3 倍。 · [代码](https://github.com/arth-shukla/mshab)
- **[TacEx: GelSight Tactile Simulation in Isaac Sim -- Combining Soft-Body and Visuotactile Simulators](https://arxiv.org/abs/2411.04776)** (2024) — 把 GIPC 软体接触与 Taxim、FOTS 触觉仿真器接入 Isaac Sim，模拟 GelSight Mini，并提供 Isaac Lab 强化学习环境。
- **[AuRA: From Atoms to Bits through Autonomous Robot Interaction](https://arxiv.org/abs/2610.34452)** (2026) — 自动完成物理数字孪生所需的机器人交互与数据准备；在 13 种柔性物体上报告每个资产的人工投入减少 88.5%。 · [代码](https://github.com/Yoonkyo/AuRA) · [项目页](https://aura-robot.github.io/)

**[查看全部 46 条 →](lists/sim.zh-CN.md)**

<a id="datasets"></a>
### 数据集与基准

_大规模机器人数据集、第一视角数据与评测基准。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/datasets.html)

- ⭐ **[LeRobot](https://github.com/huggingface/lerobot)** (2024) — PyTorch 机器人学习库，提供数据集、预训练策略（ACT、Diffusion、SmolVLA）与低成本机械臂驱动。
- ⭐ **[LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)** (2023) — 四个套件共 130 个语言条件任务，现已成为 VLA 论文最常用的仿真基准。 · [代码](https://github.com/Lifelong-Robot-Learning/LIBERO)
- ⭐ **[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)** (2023) — 30 多个实验室汇集 22 种机器人的 100 多万条轨迹；在其上训练的 RT-X 优于单机器人基线。 · [代码](https://github.com/google-deepmind/open_x_embodiment)
- **[CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation](https://arxiv.org/abs/2611.05080)** (2026) — 面向无频繁重置场景下 VLA 强化学习微调的仿真基准；发现直接微调会因物体和末端位姿偏移而失败，定向分配重置并处理预训练偏差可以缓解。 · [项目页](https://embodiedai-ntu.github.io/cronos/)
- **[EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World](https://arxiv.org/abs/2604.07607)** (2026) — 面向人类数据机器人学习的共享平台和数据集：1,362 小时、8 万条片段，覆盖 1,965 项任务和 2,087 名演示者，接受学界和业界贡献。
- **[PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](https://arxiv.org/abs/2611.05320)** (2026) — 编程智能体凭一条标定轨迹在仿真中重建任务，再由视频模型渲染成写实数据；报告真机 100 次成功 93 次，遥操作数据为 84 次，每小时数据约 107 美元。 · [代码](https://github.com/DAGroup-PKU/PyRUA-Lean) · [项目页](https://dagroup-pku.github.io/PyRUA-Lean/DataFarm)
- **[RoboScope Kit: Unified Interfaces for Fast and Scalable Embodied-AI Evaluation](https://arxiv.org/abs/2611.03850)** (2026) — 模型和基准各封装一次，把仿真 worker 与策略副本分成两个池调度；报告单卡评测比官方 StarVLA 评测器快 4.45 到 6.16 倍。 · [代码](https://github.com/MINT-SJTU/RoboScope-Kit) · [项目页](https://roboscope.pages.dev/)
- **[RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation](https://arxiv.org/abs/2604.19092)** (2026) — 评估视频世界模型时不只看画面是否逼真，而是把生成的操作转成动作，在物理仿真中验证能否执行。
- **[TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System](https://arxiv.org/abs/2511.02832)** (2025) — 基于 VR 头显的便携式免动捕人形遥操作与数据采集系统，目标是让全身示教数据能够规模化采集。 · [代码](https://github.com/amazon-far/TWIST2) · [项目页](https://twist-data.github.io)
- **[ClothDojo: Learned Data Generation and Benchmarking for Bimanual Garment Flattening and Folding](https://arxiv.org/abs/2611.01190)** (2026) — 仿真平台：用微调后的 VLA 生成近 8000 条成功的衣物操作轨迹，并重新渲染供 RGB 策略训练，效果优于直接用人类数据训练，但泛化到未见衣物仍是难题。 · [项目页](https://clothdojo.github.io/)
- **[DexArena: A Unified Benchmark for Long-Horizon Dexterous Manipulation](https://arxiv.org/abs/2611.02629)** (2026) — 10 个长时序和 30 个阶段级双手灵巧任务，每个阶段都有物理判定的成功条件，可衡量中间进度；提供经过验证的遥操作示范和统一接口。 · [项目页](https://sipair-elastic.github.io/DexArena-website/)
- **[Is It the Curriculum or Just the Easy Start? Benchmarking Unsupervised Environment Design on Quadrupeds](https://arxiv.org/abs/2610.40364)** (2026) — 在 MuJoCo MJX 中用统一协议在五款四足上比较 14 种课程方法：没有方法在所有机器人和地形集上都领先，而训练关卡偏简单的方法在分布内随机地形上表现靠前。 · [代码](https://github.com/Solvro/ml-wojtek-ued)

**[查看全部 68 条 →](lists/datasets.zh-CN.md)**

<a id="hardware"></a>
### 硬件与开源机器人

_可自行搭建的低成本机械臂、灵巧手、夹爪与数据采集设备。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/hardware.html)

- ⭐ **[Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation](https://arxiv.org/abs/2611.03648)** (2026) — 把硬件、数据和学习放在一起设计：低成本轮式人形、柔顺夹爪，遥操作与免机器人的人类数据采集，统一的全身控制器，以及人类与机器人示范共用的策略学习流程。 · [项目页](https://pixel-robot.com/pixel)
- ⭐ **[LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning](https://arxiv.org/abs/2309.06440)** (2023) — 16 自由度灵巧手，用现成零件约 2000 美元即可搭建。 · [代码](https://github.com/leap-hand/LEAP_Hand_API) · [项目页](https://leaphand.com/)
- **[MABEL: An Open Anthropomorphic Mobile Bimanual Platform for Teleoperation and Learning](https://arxiv.org/abs/2611.04083)** (2026) — 开源 56 自由度移动双臂机器人，含 7 自由度手臂和 17 自由度灵巧手，零件成本约 8100 美元，支持 Apple Vision Pro 遥操作，并演示了模仿学习全流程。 · [项目页](https://robotmabel.github.io/website/)
- **[RAIPAL: A Powerful and Agile Humanoid Arm for Human Tasks](https://arxiv.org/abs/2611.04334)** (2026) — 人形手臂，其力量、速度和耐力指标取自人类上肢测量数据；报告峰值负载 20 公斤（自重的 2.25 倍），末端速度 20.6 米每秒。
- **[Shape Your Body: Value Gradients for Multi-Embodiment Robot Design](https://arxiv.org/abs/2606.00702)** (2026) — 把冻结的多机器人价值函数作为可微代理模型来优化机器人设计，无需为每台机器人重跑协同设计 RL；可处理 1100 多个设计参数。
- **[MEVITA: Open-Source Bipedal Robot Assembled from E-Commerce Components via Sheet Metal Welding](https://arxiv.org/abs/2508.17684)** (2025) — 用电商零件和钣金焊接搭建的开源双足机器人，避开 3D 打印方案在尺寸和强度上的限制。 · [项目页](https://haraduka.github.io/mevita-hardware)
- **[The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics](https://arxiv.org/abs/2409.19795)** (2024) — 面向运动研究的开源 10 自由度人形；利用被动动力学的强化学习策略将运输成本在仿真中最多降低 50%，实机降低 31%。 · [代码](https://github.com/generalroboticslab/dukeHumanoidHardwareControl)
- **[KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL](https://arxiv.org/abs/2611.03138)** (2026) — 基于桌游 KLASK 的桌面级对抗多智能体强化学习平台，成本低于 2500 美元：开放 CAD 与物料清单，提供 Isaac Lab 数字孪生，以及采用学习型执行器模型的 sim-to-real 基线。 · [代码](https://github.com/IDSCETHZurich/klask_rl) · [项目页](https://idscethzurich.github.io/klask_hardware)
- **[SwapBot: Tool-Centric Robot Manipulation via Interchangeable End-Effectors and Tactile Sensing](https://arxiv.org/abs/2610.40646)** (2026) — 不追求万能夹爪，而是用固定的机器人侧接口加低成本、带触觉传感器的工具侧适配器，把日常厨具变成可自动更换的末端执行器，兼容多种机器人平台；配套遥操作采集示范，模仿学习策略完成煎豆腐、拌沙拉、翻肉等工具任务。 · [项目页](https://personalrobotics.github.io/SwapBot)
- **[UMI-Live for In-The-Wild Bimanual Robotics Data Collection](https://arxiv.org/abs/2610.39385)** (2026) — 全栈开源的双手 UMI 野外数据采集系统：手持设备集成相机、激光雷达-惯性传感、板载算力与电源，无需外部追踪或现场标定；异步 SLAM 流水线直接产出可训练数据集，并发布 40 小时数据、硬件设计与复现指南，用 π0.5 和 MolmoAct2 微调验证数据质量。 · [代码](https://github.com/AfterQuery-Research/umi-live) · [项目页](https://umi-live.github.io/)
- **[EgoThumb: A Vision-Driven Supernumerary Robotic Thumb for Autonomous Grasp and Holding Assistance](https://arxiv.org/abs/2610.37582)** (2026) — 开源的可穿戴“第六指”：紧凑的双腱驱动手指，电机移到前臂以减轻末端重量；模仿学习策略直接把掌心相机图像映射为关节位置，从视觉中推断使用者意图，无需显式手势触发，软硬件全部开源。 · [代码](https://github.com/JayeFu/ego_thumb_firmware) · [项目页](https://ego-thumb.github.io)
- **[OpenJaws: An Open Hardware UMI Framework with Stereo Localization for Generalist Manipulation](https://arxiv.org/abs/2610.36598)** (2026) — 完全开源的 UMI 式手持夹爪：3D 打印、标准 ISO 接口，用低成本双目相机获得公制尺度、低漂移的轨迹，并提出手持采集设备定位精度基准 UMI-Loc-Bench-v1；硬件、软件与数据以可商用许可证发布。 · [项目页](https://open-jaws.github.io/)

**[查看全部 41 条 →](lists/hardware.zh-CN.md)**

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
