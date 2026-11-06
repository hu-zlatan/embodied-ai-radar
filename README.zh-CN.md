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
- **代码追踪**：[精选索引的全部开源仓库](https://hu-zlatan.github.io/embodied-ai-radar/code.html)集中在一页：GitHub 星标、本周新增、最后更新与检测到的许可证，可按主题和许可证筛选。
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
- ⭐ **[From Pixels to Actions - Towards Native Vision-Language-Action Policies](https://arxiv.org/abs/2611.06918)** (2026) — NEO-VLA 去掉独立视觉编码器：图像与语言在同一主干中共同演化，流匹配动作专家从多个深度读取特征。逐层探测显示，对动作关键的信号往往在最终视觉层之前达到峰值。 · [代码](https://github.com/EvolvingLMMs-Lab/NEO) · [项目页](https://weichenfan.github.io/NEO-VLA-Page/)
- ⭐ **[Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models](https://arxiv.org/abs/2611.06817)** (2026) — 开源 5 万小时带标注的第一视角视频语料及流程和权重。报告预训练时长与机器人成功率之间的对数线性规律，后训练后在 RoboTwin 2.0 Clean2Random 上达到 84.6%。 · [代码](https://github.com/DAGroup-PKU/HumanNet) · [项目页](https://dagroup-pku.github.io/open-humanscale/)
- ⭐ **[RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild](https://arxiv.org/abs/2611.02497)** (2026) — 在 124 个站点做盲测两两对比，横跨四种机器人评测 VLA 与前沿智能体。不同机器人的排名几乎不一致（Kendall W = 0.24），开箱排名也难以预测微调后的表现；G1 人形上没有策略完成任何任务。 · [代码](https://github.com/RoboColosseum/robocolosseum-client)
- ⭐ **[π\*0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759)** (2025) — RECAP 通过优势条件化，用演示、机器人自主运行数据和遥操作纠正对 VLA 做强化学习；论文报告在叠衣服、做意式咖啡等难任务上吞吐量提升一倍以上、失败率约减半。 · [项目页](https://pi.website/blog/pistar06)
- ⭐ **[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** (2024) — VLM 主干加流匹配动作专家，跨多种机器人训练，能完成叠衣服等长时程灵巧任务。 · [代码](https://github.com/Physical-Intelligence/openpi)
- ⭐ **[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** (2024) — 基于 Llama 2 与 DINOv2/SigLIP 的 7B 开源 VLA，是 VLA 研究与 LoRA 微调的事实开源基线。 · [代码](https://github.com/openvla/openvla)
- ⭐ **[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** (2023) — 提出 "VLA" 概念：把网络规模的视觉语言模型联合微调为输出动作 token，把语义知识迁移到机器人控制。 · [项目页](https://robotics-transformer2.github.io/)
- **[ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining](https://arxiv.org/abs/2606.17200)** (2026) — 用 4530 小时机器人/仿真数据加 1480 小时带伪动作的第一视角人类视频联合预训练 VLA，采用相机空间动作与按可靠性加权的损失。报告在 RoboCasa GR1 TableTop 和 RoboTwin 2.0 上达到最优。 · [代码](https://github.com/ACERobotics-VLA/ACE-Ego-0)
- **[APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies](https://arxiv.org/abs/2606.12366)** (2026) — 先把动作专家预训练为不含语言的视觉-动作先验，再通过门控融合注入语言。针对 VLA 对未见指令泛化差的问题，适用于 π 系和 GR00T 系架构。 · [代码](https://github.com/xukechun/APT) · [项目页](https://xukechun.github.io/papers/APT/)
- **[EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies](https://arxiv.org/abs/2606.20092)** (2026) — 为 VLA 加入稀疏记忆：由策略自己预测哪些关键帧之后会有用并只保存这些帧。同时提出 RoboTwin-MeM 基准；报告在 17 个仿真和 4 个真机任务上平均成功率比带记忆的 VLA 高 40%。 · [代码](https://github.com/InternRobotics/EventVLA)
- **[HuRo: Robotizing Human Videos for Scalable VLA Pretraining](https://arxiv.org/abs/2609.10706)** (2026) — 把五个来源的人类视频转换成与机器人对齐的观测和动作（约 63 万条轨迹）。报告用更多此类数据预训练 VLA，真机任务完成率从 51.5% 升到 80.3%，分布外从 34.9% 升到 72.2%。 · [代码](https://github.com/3587jjh/HuRo) · [项目页](https://3587jjh.github.io/HuRo)

**[查看全部 179 条 →](lists/vla.zh-CN.md)**

<a id="manipulation"></a>
### 操作与灵巧手

_模仿学习、扩散策略、抓取、双臂与灵巧操作。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/manipulation.html)

- ⭐ **[AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data](https://arxiv.org/abs/2611.03815)** (2026) — 从 16,151 小时手持夹爪演示中学习，全程不采机器人数据；报告十项任务平均成功率 78%，其他 VLA 最好为 27%，并开放数据集、权重和后训练方案。 · [项目页](https://a-0.airoa.io)
- ⭐ **[Generalizable Humanoid Manipulation with 3D Diffusion Policies](https://arxiv.org/abs/2410.10803)** (2024) — iDP3：上半身全身遥操作、带三维激光雷达的 25 自由度人形，加上改进的三维扩散策略，使技能不再局限于单一场景。 · [代码](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy) · [项目页](https://humanoid-manipulation.github.io/)
- ⭐ **[Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](https://arxiv.org/abs/2402.10329)** (2024) — 手持夹爪加 GoPro 可随处采集演示，训练出的策略可直接迁移到机械臂。 · [代码](https://github.com/real-stanford/universal_manipulation_interface)
- ⭐ **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** (2023) — 以去噪方式生成动作序列，比回归更能处理多模态演示，已成为模仿学习标准基线。 · [代码](https://github.com/real-stanford/diffusion_policy)
- ⭐ **[Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705)** (2023) — ALOHA + ACT：约 2 万美元的双臂遥操作平台，加上动作分块 Transformer，约 50 条演示即可学会精细任务。 · [代码](https://github.com/tonyzhaozh/act)
- **[Attention from Action, for Action: Emergent Visual Bottlenecks for Policy Learning](https://arxiv.org/abs/2608.13422)** (2026) — Seeker 仅凭动作监督学习“看哪里”，在冻结的 DINOv3 特征上给出随任务进展变化的裁剪区域。报告真机成功率从 48.3% 升到 76.7%，光照与背景变化下从 20% 升到 60%。 · [代码](https://github.com/zheyu-zhuang/seeker)
- **[DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination](https://arxiv.org/abs/2609.09119)** (2026) — 基于混合 Transformer 的灵巧视触觉 VLA：接触感知门控决定何时引入触觉，并联合想象未来的视觉与触觉潜变量。报告在富接触任务上平均成功率 71%。 · [代码](https://github.com/AureleoPKU/DeCAL) · [项目页](https://aureleopku.github.io/DeCAL)
- **[MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2610.03476)** (2026) — 双循环移动操作智能体：内循环由 VLM 规划并组合流匹配技能，外循环从部署数据中自动发现并微调技能。报告在 BEHAVIOR-1K 上比 π0.5 高 22.5 个百分点。 · [代码](https://github.com/kaiknower/MobiAgent) · [项目页](https://kaiknower.github.io/mobiagent)
- **[VLS: Steering Pretrained Robot Policies via Vision-Language Models](https://arxiv.org/abs/2602.03973)** (2026) — 在测试时适配冻结的扩散或流匹配策略：当障碍或杂物改变场景时，由 VLM 生成可微奖励来引导去噪。报告 CALVIN 提升 31%、LIBERO-PRO 提升 13%，无需重新训练。 · [代码](https://github.com/Vision-Language-Steering/code) · [项目页](https://vision-language-steering.github.io/webpage/)
- **[CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization](https://arxiv.org/abs/2610.38357)** (2026) — 面向 VQ 类技能策略的两阶段后训练：先让技能先验对齐线上成功轨迹，再冻结编码器按技能优化；报告 LIBERO 成功率从 80.1% 升至 97.5%。
- **[Correct Robots Before They Make Mistakes: Proactive Human-in-the-Loop Intervention via Preference Learning](https://arxiv.org/abs/2611.05667)** (2026) — PHIL 在 XR 中预览策略预测的动作，让操作者在出错前介入，再用被否决与修正后的动作片段做偏好训练；报告相比 HG-DAgger，扩散策略成功率从 44.0% 升至 70.3%。 · [项目页](https://intuitive-robots.github.io/PHIL-page/)
- **[GRASP: Gradient-Guided Sampling for Contact-Rich Physics-Based Motion Retargeting](https://arxiv.org/abs/2611.05754)** (2026) — 无需可微仿真器即可在接触动力学下重定向人类示教：从存档的采样轨迹中恢复梯度。报告在 1352 条双手 OakInk2 示教上成功率 92.8%，且不用任务专属接触奖励。 · [代码](https://github.com/ComputationalRobotics/GRASP_code) · [项目页](https://computationalrobotics.seas.harvard.edu/GRASP/)

**[查看全部 107 条 →](lists/manipulation.zh-CN.md)**

<a id="tactile"></a>
### 触觉与视触觉感知

_触觉传感器、触觉表征与接触丰富的控制。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/tactile.html)

- ⭐ **[DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](https://arxiv.org/abs/2005.14679)** (2020) — 低成本、紧凑的 GelSight 式指尖传感器，让视触觉传感器得以普及。 · [代码](https://github.com/facebookresearch/digit-interface)
- **[Equivariant Visual-Tactile Diffusion Policy for Contact-Rich Manipulation](https://arxiv.org/abs/2610.03333)** (2026) — VISTA：等变视触觉扩散策略，把触觉融合进球面视觉 token 并随末端姿态旋转，提升富接触模仿学习的数据效率。 · [代码](https://github.com/Kenn3o3/Vista) · [项目页](https://vista-paper.github.io/)
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

**[查看全部 51 条 →](lists/tactile.zh-CN.md)**

<a id="locomotion"></a>
### 运动控制与人形机器人

_足式运动、人形全身控制与跑酷。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/locomotion.html)

- ⭐ **[Perceptive Humanoid Motion from Simulation](https://arxiv.org/abs/2611.06908)** (2026) — HALO 在上千个程序化生成的家庭场景中合成视觉-语言-动作数据来训练人形技能，数据量随算力增长。报告零微调迁移：六个未建图真实环境的 360 次试验成功率 91%。 · [代码](https://github.com/apple-aiml-research/ml-halo) · [项目页](https://apple-aiml-research.github.io/ml-halo/)
- ⭐ **[BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](https://arxiv.org/abs/2508.08241)** (2025) — 用同一套超参数的运动跟踪方案学会侧手翻、飞踢、冲刺等敏捷技能，再用带引导的潜空间扩散模型组合这些技能以完成摇杆遥控、避障等新目标，零样本迁移到真机。 · [代码](https://github.com/HybridRobotics/whole_body_tracking)
- ⭐ **[SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control](https://arxiv.org/abs/2511.07820)** (2025) — 检验规模定律在人形控制上的效果：扩大网络、数据和算力，得到通用动作跟踪基础模型，无需手工设计奖励。
- ⭐ **[Real-World Humanoid Locomotion with Reinforcement Learning](https://arxiv.org/abs/2303.03381)** (2023) — 在仿真中训练的因果 Transformer 策略零样本驱动全尺寸人形机器人在户外行走。
- ⭐ **[Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](https://arxiv.org/abs/2109.11978)** (2021) — 数千个 GPU 并行环境几分钟就能训练出四足行走策略；legged_gym 成为标准入门框架。 · [代码](https://github.com/leggedrobotics/legged_gym)
- ⭐ **[DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](https://arxiv.org/abs/1804.02717)** (2018) — 证明强化学习能模仿包括空翻在内的大量动作片段并保持鲁棒，是后续人形动作模仿工作的基本范式。 · [代码](https://github.com/xbpeng/DeepMimic)
- **[Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation](https://arxiv.org/abs/2609.38172)** (2026) — PRISM 用视频生成把少量真实视频扩增为数百段反事实人-物交互视频，在仿真中重建并训练单一人形搬运策略，无需真机微调即可泛化到未见物体。 · [代码](https://github.com/amazon-far/PRISM) · [项目页](https://prism-real2sim2real.github.io/)
- **[HERO: Learning Humanoid End-Effector Control for Visual Whole-Body Open-Vocabulary Object Grasping](https://arxiv.org/abs/2602.16705)** (2026) — 模块化人形抓取：大视觉模型负责场景理解，仿真训练的末端跟踪策略结合 IK 与学习的正运动学模型负责执行。报告末端跟踪误差 2.44 厘米，比先前最好方法低 5.5 倍。 · [代码](https://github.com/RunpeiDong/HERO) · [项目页](https://hero-humanoid.github.io/)
- **[Learning Contact Representation for Leg Odometry](https://arxiv.org/abs/2606.05501)** (2026) — 仅用关节编码器与 IMU 自监督估计足端接触，并作为支撑置信度输入卡尔曼滤波器。报告腿式里程计误差在对比方法中最低。 · [代码](https://github.com/egirgin/leg-odometry-contact-representation)
- **[Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.05507)** (2026) — 在动作跟踪中为每个接触部位加入显式三维力指令，由高层规划器在线给出。实机可推、踢最重 20 kg 的箱子（不感知力的基线会失败），并能适应任务中途增加的负载。 · [项目页](https://forcectrl.github.io/)
- **[Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight](https://arxiv.org/abs/2611.04839)** (2026) — 用潜空间世界动作模型在执行前为人形指令序列打分，并逐步重规划；报告七项真机任务成功率 85.7%，GR00T N1.7 为 70.0%。 · [项目页](https://ju6276.github.io/Action-Grounded-Foresight/)
- **[Deep Whole-body Parkour](https://arxiv.org/abs/2601.07701)** (2026) — 将外部感知融入全身动作跟踪，让人形机器人在不平整地形上完成高动态的非行走类技能。 · [代码](https://github.com/project-instinct/InstinctLab) · [项目页](https://project-instinct.github.io/deep-whole-body-parkour)

**[查看全部 119 条 →](lists/locomotion.zh-CN.md)**

<a id="world-models"></a>
### 世界模型

_学习的动力学模型、视频世界模型、世界动作模型（WAM）与基于模型的强化学习。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/world-models.html)

- ⭐ **[Cosmos 3: Omnimodal World Models for Physical AI](https://arxiv.org/abs/2606.02800)** (2026) — 全模态世界模型家族，用一个 Mixture-of-Transformers 同时处理语言、图像、视频、音频和动作，把 VLM、视频生成、世界模拟器和世界动作模型并入同一框架。 · [代码](https://github.com/nvidia/cosmos) · [项目页](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)
- ⭐ **[DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](https://arxiv.org/abs/2602.06949)** (2026) — 在 4.4 万小时第一视角人类视频上预训练的基础世界模型，用连续潜动作代替缺失的动作标签，再用小规模机器人数据后训练。 · [代码](https://github.com/NVIDIA/DreamDojo) · [项目页](https://dreamdojo-world.github.io/)
- ⭐ **[OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398)** (2026) — 开放研究栈，把世界动作模型拆成可组合模块，并通过对照实验研究该从视频先验继承什么、世界学习与动作学习如何相互作用。 · [代码](https://github.com/OpenWAM-Official/OpenWAM) · [项目页](https://openwam-official.github.io/)
- ⭐ **[RoboJEPA: Scaling Robotic Latent World Models](https://arxiv.org/abs/2610.10515)** (2026) — 跨 12 种机器人形态训练的 JEPA 世界模型；其想象误差随算力服从幂律，因此可以预测超出拟合规模时的模型质量。 · [代码](https://github.com/facebookresearch/robo_jepa) · [项目页](https://robojepa.github.io/)
- ⭐ **[World Action Models: A Survey](https://arxiv.org/abs/2606.20781)** (2026) — 厘清 WAM 与世界模型、视频生成模型、VLA 的区别，并按生成内容（渲染、潜空间或不生成）和架构分类；结论是领域正走向少生成未来，只保留控制所需。 · [项目页](https://world-action-models.github.io/)
- ⭐ **[Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104)** (2023) — DreamerV3：一套超参数适用于 150 多个任务，包括从零开始在《我的世界》中挖到钻石。 · [代码](https://github.com/danijar/dreamerv3)
- **[$μ_0$: A Scalable 3D Interaction-Trace World Model](https://arxiv.org/abs/2606.13769)** (2026) — 不预测像素也不预测动作，而是预测物体、工具、手等关键点的 3D 轨迹，可用无动作标签的视频预训练。报告以轨迹为条件的策略可与 π0 类 VLA 相当。 · [代码](https://github.com/Yoonkyo/mu0) · [项目页](https://mu0-wm.github.io/)
- **[ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/abs/2606.19531)** (2026) — 追问世界动作模型是否真需要视频生成：ImageWAM 改用图像编辑模型去噪时的 KV 缓存来条件化流匹配动作专家；报告优于 VLA 基线，计算量为视频 WAM 的 1/6、延迟为 1/4。 · [代码](https://github.com/yuyangalin/ImageWAM) · [项目页](https://zhangwenyao1.github.io/ImageWAM/)
- **[Large Video Planner Enables Generalizable Robot Control](https://arxiv.org/abs/2512.15840)** (2026) — 以视频而非语言为主干构建机器人基础模型：在互联网规模人类视频上训练开源视频规划器，零样本生成视频计划再转为机器人动作；模型与数据集均已开源。 · [代码](https://github.com/buoyancy99/large-video-planner) · [项目页](https://www.boyuan.space/large-video-planner/)
- **[Light-WAM: Efficient World Action Models with State-Fusion Action Decoding](https://arxiv.org/abs/2606.08242)** (2026) — 轻量世界动作模型：紧凑视频主干在降采样潜空间中做未来监督，动作专家融合多层特征一次前向预测动作块；报告可训练参数仅 0.44B，推理延迟 72 毫秒。 · [代码](https://github.com/L1ziang/Light-WAM)
- **[StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement](https://arxiv.org/abs/2606.00267)** (2026) — 通过优化视频世界模型的初始噪声（以 VLM 为目标），把想象引向罕见但合理的不利结果（如任务失败），用于评估和改进策略；覆盖自动驾驶与操作。 · [代码](https://github.com/CMU-IntentLab/StressDream) · [项目页](https://stressdream.github.io/)
- **[What Makes Video World Model Latents Action-Relevant: Prediction over Reconstruction](https://arxiv.org/abs/2606.07687)** (2026) — 探测哪些视频世界模型的潜变量含有动作信息：关键在于时序视频预训练，而非像素重建质量；V-JEPA 类编码器取得最佳权衡。 · [代码](https://github.com/k1seul/corl2026-action-relevant-latents)

**[查看全部 98 条 →](lists/world-models.zh-CN.md)**

<a id="navigation"></a>
### 导航与具身智能体

_视觉语言导航、具身问答、移动操作与大模型规划。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/navigation.html)

- ⭐ **[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)** (2022) — SayCan：大模型提出步骤，学习到的价值函数评估机器人当下实际能做什么。
- **[CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation](https://arxiv.org/abs/2607.02222)** (2026) — 低层视觉语言导航动作头：在可见扇区上预测语言条件的流场并展开为连续轨迹；并提供连续时间的 Habitat 评测基准。 · [代码](https://github.com/ut-dragon-lab/CoFL)
- **[CostNav: A Navigation Benchmark for Real-World Economic-Cost Evaluation of Physical AI Agents](https://arxiv.org/abs/2511.20216)** (2026) — 以经济账评估配送机器人导航：在 Isaac Sim 中结合公开财报与伤害数据计算成本、收入与盈亏平衡。报告七种基线方法目前都无法盈利。 · [代码](https://github.com/worv-ai/CostNav)
- **[G2-Nav: Grounded and Guarded Vision-Language Costmaps for Robot Social Navigation](https://arxiv.org/abs/2607.16956)** (2026) — 社交导航：让 VLM 生成代价地图而非直接决策，并校验上游跟踪，另加高频安全检查应对延迟；真机验证。 · [代码](https://github.com/centiLinda/G2-Nav)
- **[RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical Embodied Systems](https://arxiv.org/abs/2508.01415)** (2026) — 受大脑启发的具身智能体记忆框架（时间、空间、语义、情景记忆），配合动态空间知识图谱。报告让 Qwen2.5-VL-72B 在 EmbodiedBench 上平均成功率提高 26.5 个百分点。 · [代码](https://github.com/SP4595/RoboMemory-Code)
- **[OdorSpaces: Visual-Olfactory Embodied Navigation in 3D Environments](https://arxiv.org/abs/2611.05738)** (2026) — 用 Fire Dynamics Simulator 为 Habitat-Sim 加入气味传输仿真，构成视觉加嗅觉的导航基准，任务是定位不可见的气体泄漏和早期火源，并提供多模态强化学习基线。
- **[Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware](https://arxiv.org/abs/2611.04392)** (2026) — 紧凑的 JEPA 加流匹配四旋翼策略，报告异常坦率：行为克隆 60 次任务全败，DAgger 进入瓶颈，运行时安全层将仿真森林任务成功率从 21.1% 提至 52.2%。 · [代码](https://github.com/ylee-sling/Aero-VPA) · [项目页](https://huggingface.co/ylee-sling/aero-vpa)
- **[Collaborative Planning for UAV-UGV Teams under Operational Constraints via Masked Error-bounded Neuro-Symbolic Diffusion](https://arxiv.org/abs/2610.18850)** (2026) — MEND 用掩码扩散规划无人机与地面车协同充电任务，在执行时通过逻辑动作掩码强制满足运行约束；在真实地图和实体机器人队伍上测试。
- **[Driving, Fast or Slow? Neuro-Symbolic Guidance for Motion Prediction in Multi-Modal Ground Mobility](https://arxiv.org/abs/2606.15251)** (2026) — TraCS 将由自然语言交规生成的可解释概率逻辑加到黑盒运动预测模型上；报告在 Argoverse 2 上稳定提升。Oral 论文。
- **[From Region Arrival to Instance-Level Grounding in Vision-and-Language Navigation](https://arxiv.org/abs/2607.03792)** (2026) — 指出 VLN 成功率掩盖了“最后 3 米定位缺口”：智能体停在附近却未对准目标。提出实例级指标和可接入任意主干的修正模块 REALM。
- **[WayTrace: A Map-to-Language-to-Trace Hierarchy for Embodied Urban Navigation](https://arxiv.org/abs/2611.05129)** (2026) — 视觉语言模型把网络地图导航拆成一条条原子指令，预测器在图像上画出路径，强化学习负责跟踪；轮腿机器人完成最长 1.37 公里的真实任务。 · [项目页](https://way-trace.github.io)
- **[OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation](https://arxiv.org/abs/2610.39287)** (2026) — 面向无人机的机载 VLA：同一视觉-语言表征同时支撑语义理解、空间推理与闭环航点控制。 · [代码](https://github.com/Ideal-ljl/AeroBrain) · [项目页](https://ideal-ljl.github.io/AeroBrain/)

**[查看全部 50 条 →](lists/navigation.zh-CN.md)**

<a id="perception"></a>
### 感知、SLAM 与三维建图

_视觉/激光 SLAM 与里程计、三维重建、物体位姿、深度估计与开放词汇场景地图。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/perception.html)

- ⭐ **[Segment Anything](https://arxiv.org/abs/2304.02643)** (2023) — SAM：可用点、框、掩码提示的分割模型，在 10 亿级掩码上训练；已成为机器人感知流程中获取物体掩码的常用基础组件。 · [代码](https://github.com/facebookresearch/segment-anything)
- ⭐ **[ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](https://arxiv.org/abs/2007.11898)** (2020) — 最常用的特征点 SLAM 库：支持单目、双目与 RGB-D，可融合 IMU，并支持多地图重定位。 · [代码](https://github.com/UZ-SLAMLab/ORB_SLAM3)
- **[Cyclops: LiDAR as a Camera That Dreams in Color](https://arxiv.org/abs/2608.16264)** (2026) — 把稀疏 LiDAR 强度转换为类 RGB 视频，让相机模型在黑暗中也能用。报告在不同光照下，分割与车道线检测优于 LiDAR 基线和真实相机。 · [代码](https://github.com/IMRL/Cyclops)
- **[Functional-SLAM: Interaction-Aware Mapping with Online Functional Scene Graphs](https://arxiv.org/abs/2609.07497)** (2026) — 把功能场景图（如哪个把手开哪个抽屉）作为 SLAM 的在线状态持续维护，并利用其拓扑辅助重复场景的回环检测。报告比离线方法更快且精度相当。 · [代码](https://github.com/Hbelief1998/Functional-SLAM-CoRL_2026)
- **[ReSiReg: Towards Spatially Consistent Semantics in Language-Conditioned Robotic Tasks](https://arxiv.org/abs/2606.19088)** (2026) — 通过由带语言描述的视觉原型重建每个图像块，让稠密 VLM 特征在空间上更一致，提升开放词汇检索与三维建图；并提供 25M 参数的小型稠密 VLM。 · [代码](https://github.com/SimonSchwaiger/resireg) · [项目页](https://resireg.github.io)
- **[CoReMatch: Recurrent Continuous Coordinate Refinement for Real-Time Robotic Feature Matching](https://arxiv.org/abs/2611.03932)** (2026) — 在连续坐标中循环细化对应点、不再依赖固定网格的特征匹配方法；报告精度高于 Efficient LoFTR，在嵌入式硬件上速度超过其 10 倍。
- **[Articulated 3D Scene Graphs for Open-World Mobile Manipulation](https://arxiv.org/abs/2602.16356)** (2026) — MoMa-SG 从 RGB-D 序列构建包含物体铰接方式的 3D 场景图，并发布 Arti4D-Semantic 数据集；在四足和移动操作机器人上演示。 · [代码](https://github.com/robot-learning-freiburg/MoMa-SG) · [项目页](https://momasg.cs.uni-freiburg.de)
- **[MosaicIMU: Composing Carrier Experts for Generalizable Neural Inertial Odometry](https://arxiv.org/abs/2606.09355)** (2026) — 面向多种载体的神经惯性里程计：路由器组合各载体专家，新载体通过轻量残差分支适配。报告 ATE 比学习型基线降低 40%。
- **[Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping](https://arxiv.org/abs/1910.02490)** (2019) — 开源 C++ 实时度量-语义视觉惯性 SLAM 库，模块化包含 VIO、鲁棒位姿图、快速三维网格与稠密语义重建。 · [代码](https://github.com/MIT-SPARK/Kimera)
- **[AnchorHEC: Targetless Hand-Eye Calibration of Wrist and Fixed Cameras](https://arxiv.org/abs/2611.02884)** (2026) — 无需标定板，用 RGB、正运动学和三维基础模型同时标定腕部与固定相机；仿真中平移和旋转误差比基于重建的基线分别降低 86.4% 和 71.6%，并在真机上验证。 · [代码](https://github.com/HwangGB/AnchorHEC) · [项目页](https://hwanggb.github.io/AnchorHEC/)
- **[Anchor3R: Streaming 3D Reconstruction with Transient Anchors for Long-Horizon Visual Mapping](https://arxiv.org/abs/2606.05035)** (2026) — CoRL 2026 Spotlight。以当前帧为中心的流式三维重建：在当前帧坐标系预测窗口相对位姿与局部几何，以抑制长时漂移。 · [代码](https://github.com/polar-explorer/Anchor3R)
- **[OpenVIO: A Versatile Open-Source Visual-Inertial Odometry System](https://arxiv.org/abs/2610.41671)** (2026) — MIT 许可的开源视觉惯性里程计，面向科研与实际应用。支持针孔、鱼眼相机及拼接 360° 图像，并在公开数据集上与其他开源 VIO 系统做了对比。 · [代码](https://github.com/93won/openvio)

**[查看全部 39 条 →](lists/perception.zh-CN.md)**

<a id="control"></a>
### 规划、控制与安全

_运动规划、轨迹优化、模型预测控制、安全滤波器与安全的学习型控制。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/control.html)

- ⭐ **[cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation](https://arxiv.org/abs/2310.17274)** (2023) — 面向机械臂的 GPU 并行运动生成：同时运行大量轨迹优化，在毫秒级给出无碰撞且平滑的轨迹。 · [代码](https://github.com/NVlabs/curobo)
- **[PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning](https://arxiv.org/abs/2611.05372)** (2026) — 学习式目标条件逆运动学，能保持位置控制器静止时所需的偏置；报告在 93.5% 的留出仿真任务上误差低于 1 mm 和 0.2°，并可直接在真实机械臂上训练。 · [代码](https://github.com/Tinaliu0123/PolicyIK)
- **[Scalable Deep Unfolding of Conic Optimizers](https://arxiv.org/abs/2606.13825)** (2026) — 通过无矩阵隐式微分和稳定的半正定投影梯度，让深度展开适用于大规模锥优化求解器；报告在基于 SDP 的规划上最高提速 50 倍。
- **[cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots](https://arxiv.org/abs/2603.05493)** (2026) — cuRoboV2 新增考虑力矩限制的 B 样条轨迹优化和 GPU 原生 TSDF/ESDF 感知，面向高自由度机器人。 · [代码](https://github.com/NVlabs/curobo)
- **[PyRoki: A Modular Toolkit for Robot Kinematic Optimization](https://arxiv.org/abs/2505.03728)** (2025) — PyRoki：模块化、跨平台的运动学优化工具包，可原生运行在 CPU、GPU 和 TPU 上。 · [代码](https://github.com/chungmin99/pyroki) · [项目页](https://pyroki-toolkit.github.io)
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
- **[Online World Modeling Enables Real-World Inverse Reinforcement Learning from Observation](https://arxiv.org/abs/2602.24121)** (2026) — 仅从观测（视频，无动作和奖励）做逆强化学习，借助在线世界模型在真机上实现。报告不到 40 分钟从零学会抓放，成功率 82%。 · [代码](https://github.com/UWRobotLearning/mpail2) · [项目页](https://uwrobotlearning.github.io/mpail2/)
- **[TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics](https://arxiv.org/abs/2602.19313)** (2026) — 免训练的进度奖励：不让视频语言模型输出数值，而是读取其判断“任务已完成”的 token 概率作为稠密奖励。并提出 ManiRewardBench（130 个任务、4 种机器人）。 · [代码](https://github.com/TOPReward/TOPReward)
- **[ELA: End-to-End Latent Action Policy Learning from Video Demonstrations](https://arxiv.org/abs/2611.05571)** (2026) — 联合训练潜在动作模型、潜在策略和动作解码器，用大量无动作标注的视频加少量带标注示教即可训练策略。报告在仿真和真实任务上优于已有潜在动作方法。 · [项目页](https://end2end-latent-action.github.io/)
- **[LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation](https://arxiv.org/abs/2611.04974)** (2026) — ARPG 让大模型在部署前设计强化学习流程：先定 MDP，再写仿真代码，并校验状态、动作与奖励是否一致；报告在 Isaac Sim 中成功率高于单体式大模型基线。
- **[RACE: Calibrated Cumulative Scoring for Rollout-Free Robot Policy Checkpoint Selection](https://arxiv.org/abs/2611.05838)** (2026) — 无需实机回放即可排序检查点：用保留示教得到的状态相关阈值校准动作偏差，再按累乘聚合。论文报告其排序与真实机器人部署成功率一致。 · [项目页](https://changyeon.site/race)
- **[Control-Ready Uncertainty for Trajectory Diffusion](https://arxiv.org/abs/2610.12431)** (2026) — SCOPE 通过蒸馏得分函数曲率，让扩散轨迹模型无需蒙特卡洛采样即可给出校准的不确定性管道；在人群导航和 Franka 操作上测试。 · [项目页](https://zackaxue.github.io/SCOPE-project-page/)
- **[FedGuide: Diffusion Prior Alignment and Value Baseline Guidance for Heterogeneous Federated Reinforcement Learning](https://arxiv.org/abs/2609.18964)** (2026) — 面向异构客户端的联邦强化学习：不再平均策略，而是用最优传输聚合扩散行为先验，并加入低方差的 DICE 价值基线。
- **[GSBR: Geometric Support Behavior Regularization for Online RL](https://arxiv.org/abs/2611.05295)** (2026) — 在预训练策略之上做在线强化学习，按动作到其支撑集的距离施加惩罚：集内不罚，集外平滑增长；报告 19 个基准任务的平均成功率从 33% 升至 95%。 · [代码](https://github.com/charlesxu0124/gsbr) · [项目页](https://charlesxu0124.github.io/gsbr/)
- **[SCoCaT: Success Conditioned Constrained Reinforcement Learning for Spacecraft Docking](https://arxiv.org/abs/2609.06061)** (2026) — 发现基于终止的约束强化学习在目标附近约束收紧时会学会回避目标，并用稠密成功信号的辅助价值网络解决；在航天器对接任务上验证。
- **[TARC: Time-Adaptive Robotic Control](https://arxiv.org/abs/2510.23176)** (2026) — 策略同时预测动作及其保持时长。报告在遥控车、Unitree Go1 和仿真 VLA 上以不到一半的控制频率达到高频控制的性能。 · [项目页](https://arnavsukhija.github.io/projects/tarc)

**[查看全部 62 条 →](lists/learning.zh-CN.md)**

<a id="sim"></a>
### 仿真与 Sim-to-Real

_物理仿真器、GPU 并行训练与向真实机器人迁移。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/sim.html)

- ⭐ **[When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks](https://arxiv.org/abs/2610.41857)** (2026) — 审计仿真基准：不少“策略失败”其实是物理引擎把物体弹飞。SimuGuard 为 LIBERO、RoboTwin、RoboCasa、RoboDojo 提供审计插件，把 RoboTwin 上的问题追溯到碰撞检测的一个常量；仅改动它，异常回合由 100 回合 12 次降到 0，五个容器任务成功率由 89% 升到 98%。 · [代码](https://github.com/ALEXander22568/simuguard)
- ⭐ **[MuJoCo](https://mujoco.org/)** (2012) — 快速准确的接触物理仿真，机器人学习研究的默认仿真器，由 DeepMind 开源。 · [代码](https://github.com/google-deepmind/mujoco)
- **[CoDA: Co-Evolution of Data Engines and Action Policies](https://arxiv.org/abs/2610.22362)** (2026) — 把诊断出的策略失败转成新的仿真场景和塑形训练信号，让生成器与策略共同进化；在 LIBERO-Pro 上报告位置扰动下成功率从 25% 升至 84%。 · [项目页](https://plan-lab.github.io/projects/coda/)
- **[Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot](https://arxiv.org/abs/2601.02078)** (2026) — Genie Sim 3.0：面向操作的仿真平台，用 LLM 工具依自然语言生成场景，并提供基于 LLM 与 VLM 的自动化评测基准。 · [代码](https://github.com/AgibotTech/genie_sim)
- **[Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](https://arxiv.org/abs/2607.13451)** (2026) — PGRD 以可优化的弹簧质点模型为骨架，加上学习得到的残差来仿真可变形物体，报告精度优于单用任一方法；可用于 MPC 和动作条件视频预测。 · [代码](https://github.com/shivanshpatel35/pgrd) · [项目页](https://pgrd-robot.github.io/)
- **[GaussGym: An open-source real-to-sim framework for learning locomotion from pixels](https://arxiv.org/abs/2510.15352)** (2025) — 把 3D 高斯溅射作为渲染器接入矢量化物理仿真，报告在消费级 GPU 上超过每秒 10 万步，用于从像素学习。
- **[Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation](https://arxiv.org/abs/2504.12908)** (2025) — 结合 IPC 与 ABD 的 GPU 触觉仿真；作者报告在数千并行环境下达到实时速度的 18 倍。
- **[BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark](https://arxiv.org/abs/2407.07788)** (2024) — 面向移动双臂机器人的基准，含 40 个家庭任务（从抓取到厨房清洁），均配人类采集的演示。 · [项目页](https://chernyadev.github.io/bigym/)
- **[DIFFTACTILE: A Physics-based Differentiable Tactile Simulator for Contact-rich Robotic Manipulation](https://arxiv.org/abs/2403.08716)** (2024) — 可微触觉仿真器，用 FEM 软体模型模拟弹性体，面向多种材料的接触，而非主要针对刚体。 · [代码](https://github.com/Genesis-Embodied-AI/DiffTactile)
- **[GRUtopia: Dream General Robots in a City at Scale](https://arxiv.org/abs/2407.10943)** (2024) — 面向多种机器人的交互式三维仿真社会；GRScenes 含 10 万标注场景、89 个类别，可组合成城市级环境。 · [代码](https://github.com/OpenRobotLab/GRUtopia)
- **[ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks](https://arxiv.org/abs/2412.13211)** (2024) — GPU 加速的 Home Assistant Benchmark，采用真实低层控制；作者报告速度超过此前“魔法抓取”实现的 3 倍。 · [代码](https://github.com/arth-shukla/mshab)
- **[TacEx: GelSight Tactile Simulation in Isaac Sim -- Combining Soft-Body and Visuotactile Simulators](https://arxiv.org/abs/2411.04776)** (2024) — 把 GIPC 软体接触与 Taxim、FOTS 触觉仿真器接入 Isaac Sim，模拟 GelSight Mini，并提供 Isaac Lab 强化学习环境。

**[查看全部 49 条 →](lists/sim.zh-CN.md)**

<a id="datasets"></a>
### 数据集与基准

_大规模机器人数据集、第一视角数据与评测基准。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/datasets.html)

- ⭐ **[LeRobot](https://github.com/huggingface/lerobot)** (2024) — PyTorch 机器人学习库，提供数据集、预训练策略（ACT、Diffusion、SmolVLA）与低成本机械臂驱动。
- ⭐ **[LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)** (2023) — 四个套件共 130 个语言条件任务，现已成为 VLA 论文最常用的仿真基准。 · [代码](https://github.com/Lifelong-Robot-Learning/LIBERO)
- ⭐ **[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)** (2023) — 30 多个实验室汇集 22 种机器人的 100 多万条轨迹；在其上训练的 RT-X 优于单机器人基线。 · [代码](https://github.com/google-deepmind/open_x_embodiment)
- **[RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](https://arxiv.org/abs/2609.25636)** (2026) — 揭示 VLA 的高成功率常掩盖薄弱的指令遵循：场景支持多种合法任务，必须依赖语言。九个 VLA 与 WAM 策略在基础级以外的测试中明显下降。 · [代码](https://github.com/AutoLab-SAI-SJTU/RoboFollow)
- **[BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories](https://arxiv.org/abs/2611.06911)** (2026) — 1000 道专家整理的题目、11 种图像和视频任务，检验多模态大模型能否担任自动化化学实验室的“大脑”：可供性、轨迹、仪器搭建、安全与步骤推理。
- **[Beyond Infraction Scores: Failure-Boundary Profiles for Closed-Loop Evaluation of Driving and Robot Navigation Agents](https://arxiv.org/abs/2611.06453)** (2026) — 每类场景只改变一个可测因素，并认证智能体此时该通过还是该停下；CARLA 中得分最高的学习型智能体决策准确率为 0.60，规则专家为 0.74。 · [代码](https://github.com/speedym/failure-boundary-profiles)
- **[MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics](https://arxiv.org/abs/2611.05567)** (2026) — 五组评测分别隔离空间布局、物体实例、物体类别和子任务组合上的泛化能力，并提供双臂版 BiMESA。七种基线中最好的也只有 52% 和 49%，仍有很大提升空间。 · [代码](https://github.com/pairlab/mesa-env) · [项目页](https://pairlab.github.io/MESA)
- **[CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation](https://arxiv.org/abs/2611.05080)** (2026) — 面向无频繁重置场景下 VLA 强化学习微调的仿真基准；发现直接微调会因物体和末端位姿偏移而失败，定向分配重置并处理预训练偏差可以缓解。 · [项目页](https://embodiedai-ntu.github.io/cronos/)
- **[EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World](https://arxiv.org/abs/2604.07607)** (2026) — 面向人类数据机器人学习的共享平台和数据集：1,362 小时、8 万条片段，覆盖 1,965 项任务和 2,087 名演示者，接受学界和业界贡献。
- **[PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](https://arxiv.org/abs/2611.05320)** (2026) — 编程智能体凭一条标定轨迹在仿真中重建任务，再由视频模型渲染成写实数据；报告真机 100 次成功 93 次，遥操作数据为 84 次，每小时数据约 107 美元。 · [代码](https://github.com/DAGroup-PKU/PyRUA-Lean) · [项目页](https://dagroup-pku.github.io/PyRUA-Lean/DataFarm)
- **[RoboScope Kit: Unified Interfaces for Fast and Scalable Embodied-AI Evaluation](https://arxiv.org/abs/2611.03850)** (2026) — 模型和基准各封装一次，把仿真 worker 与策略副本分成两个池调度；报告单卡评测比官方 StarVLA 评测器快 4.45 到 6.16 倍。 · [代码](https://github.com/MINT-SJTU/RoboScope-Kit) · [项目页](https://roboscope.pages.dev/)
- **[RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation](https://arxiv.org/abs/2604.19092)** (2026) — 评估视频世界模型时不只看画面是否逼真，而是把生成的操作转成动作，在物理仿真中验证能否执行。

**[查看全部 74 条 →](lists/datasets.zh-CN.md)**

<a id="hardware"></a>
### 硬件与开源机器人

_可自行搭建的低成本机械臂、灵巧手、夹爪与数据采集设备。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/hardware.html)

- ⭐ **[Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation](https://arxiv.org/abs/2611.03648)** (2026) — 把硬件、数据和学习放在一起设计：低成本轮式人形、柔顺夹爪，遥操作与免机器人的人类数据采集，统一的全身控制器，以及人类与机器人示范共用的策略学习流程。 · [项目页](https://pixel-robot.com/pixel)
- ⭐ **[LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning](https://arxiv.org/abs/2309.06440)** (2023) — 16 自由度灵巧手，用现成零件约 2000 美元即可搭建。 · [代码](https://github.com/leap-hand/LEAP_Hand_API) · [项目页](https://leaphand.com/)
- **[MABEL: An Open Anthropomorphic Mobile Bimanual Platform for Teleoperation and Learning](https://arxiv.org/abs/2611.04083)** (2026) — 开源 56 自由度移动双臂机器人，含 7 自由度手臂和 17 自由度灵巧手，零件成本约 8100 美元，支持 Apple Vision Pro 遥操作，并演示了模仿学习全流程。 · [项目页](https://robotmabel.github.io/website/)
- **[RAIPAL: A Powerful and Agile Humanoid Arm for Human Tasks](https://arxiv.org/abs/2611.04334)** (2026) — 人形手臂，其力量、速度和耐力指标取自人类上肢测量数据；报告峰值负载 20 公斤（自重的 2.25 倍），末端速度 20.6 米每秒。
- **[Shape Your Body: Value Gradients for Multi-Embodiment Robot Design](https://arxiv.org/abs/2606.00702)** (2026) — 把冻结的多机器人价值函数作为可微代理模型来优化机器人设计，无需为每台机器人重跑协同设计 RL；可处理 1100 多个设计参数。
- **[MEVITA: Open-Source Bipedal Robot Assembled from E-Commerce Components via Sheet Metal Welding](https://arxiv.org/abs/2508.17684)** (2025) — 用电商零件和钣金焊接搭建的开源双足机器人，避开 3D 打印方案在尺寸和强度上的限制。 · [代码](https://github.com/haraduka/mevita) · [项目页](https://haraduka.github.io/mevita-hardware)
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
