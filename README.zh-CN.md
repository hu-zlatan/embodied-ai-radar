# 具身智能雷达 · Embodied AI Radar

**中英双语（[English](README.md) / 中文）、持续更新的具身智能与机器人学习全景图。**
人工核验的论文、代码、数据集、仿真器与硬件，配一句话要点；外加每天自动抓取并按主题标注的 arXiv 机器人新论文。

### 🌐 [打开网站 → hu-zlatan.github.io/embodied-ai-radar](https://hu-zlatan.github.io/embodied-ai-radar/?lang=zh)

![具身智能雷达网站截图](docs/screenshot.png)

## 特点

- **可信**：每个精选条目的 arXiv 编号都会与 arXiv 核对，所有链接每周由 CI 自动检查。
- **新鲜**：GitHub Action 每天抓取 cs.RO 新论文（以及 cs.CV / cs.LG / cs.AI / cs.CL 中的机器人相关论文）并按主题标注，自动出现在网站上。
- **好找**：快速静态网站，支持即时搜索与筛选（主题 · 机器人形态：机械臂、灵巧手、人形、足式、无人机… · 精选/每日 · 是否有代码），手机友好。
- **双语**：每个精选条目都有中英文一句话要点，网站支持 EN / 中文 切换。

| 内容 | 更新频率 |
|---|---|
| 每日 arXiv 论文（[网站](https://hu-zlatan.github.io/embodied-ai-radar/feed.html?lang=zh) · [Atom 订阅](https://hu-zlatan.github.io/embodied-ai-radar/feed.xml)；每个主题也有单独的 Atom 订阅，如 [VLA](https://hu-zlatan.github.io/embodied-ai-radar/topics/vla.xml)） | 每天自动 |
| 精选索引（见下方与网站） | 每周多次 |
| [每周精选](digest/) | 每周 |

## 精选索引

⭐ = 重点推荐。由 [`data/curated/`](data/curated) 自动生成——请修改 YAML，而不是这个列表。

<!-- radar:start -->

[VLA 与机器人基础模型](#vla) · [操作与灵巧手](#manipulation) · [触觉与视触觉感知](#tactile) · [运动控制与人形机器人](#locomotion) · [世界模型](#world-models) · [导航与具身智能体](#navigation) · [感知、SLAM 与三维建图](#perception) · [规划、控制与安全](#control) · [仿真与 Sim-to-Real](#sim) · [数据集与基准](#datasets) · [硬件与开源机器人](#hardware)

<a id="vla"></a>
### VLA 与机器人基础模型

_视觉-语言-动作模型与通用机器人策略。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/vla.html)

- ⭐ **[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** (2024) — VLM 主干加流匹配动作专家，跨多种机器人训练，能完成叠衣服等长时程灵巧任务。 · [代码](https://github.com/Physical-Intelligence/openpi)
- ⭐ **[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** (2024) — 基于 Llama 2 与 DINOv2/SigLIP 的 7B 开源 VLA，是 VLA 研究与 LoRA 微调的事实开源基线。 · [代码](https://github.com/openvla/openvla)
- ⭐ **[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** (2023) — 提出 "VLA" 概念：把网络规模的视觉语言模型联合微调为输出动作 token，把语义知识迁移到机器人控制。 · [项目页](https://robotics-transformer2.github.io/)
- **[FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2610.22146)** (2026) — 只保留当前任务所需的视觉 token、并让 token 预算随时间步变化，以加快 VLA 推理。 · [代码](https://github.com/jiuyixu25/FastVLA)
- **[LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models](https://arxiv.org/abs/2610.21362)** (2026) — 通过缓存相邻观测之间的紧凑潜在转移，为 π0.5 加入记忆，面向关键物体移出视野的任务。 · [代码](https://github.com/buaa-colalab/LTM-pi)
- **[REKI: Registering Knowledge in VLAs](https://arxiv.org/abs/2610.22178)** (2026) — 仅用公开数据预训练的 2.4B VLM + 流匹配 VLA；报告称只输给约两倍大的模型，并用少量寄存器 token 实现低成本记忆。 · [代码](https://github.com/kyutai-labs/reki)
- **[π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)** (2025) — 通过异构数据联合训练，让移动操作机器人在从未见过的家庭中整理厨房和卧室。 · [代码](https://github.com/Physical-Intelligence/openpi)
- **[FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747)** (2025) — 用基于 DCT 的分词器压缩动作块，使自回归 VLA 能学习高频灵巧控制。
- **[Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645)** (2025) — OpenVLA-OFT：并行解码、动作分块与连续动作让 VLA 微调更快、成功率更高。 · [代码](https://github.com/moojink/openvla-oft)
- **[GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)** (2025) — 双系统（VLM 慢思考 + 扩散快执行）人形机器人策略，用真实、人类视频与合成数据训练。 · [代码](https://github.com/NVIDIA/Isaac-GR00T)
- **[Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020)** (2025) — 基于 Gemini 2.0 的 VLA 与具身推理模型，面向灵巧、通用的机器人控制。
- **[SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://arxiv.org/abs/2506.01844)** (2025) — 约 4.5 亿参数的 VLA，用社区 LeRobot 数据训练，可在消费级 GPU 上运行。 · [代码](https://github.com/huggingface/lerobot)
- **[Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213)** (2024) — 在 Open X-Embodiment 上预训练的开源扩散头 Transformer 策略，可快速微调到新机器人和新传感器。 · [代码](https://github.com/octo-models/octo)
- **[RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](https://arxiv.org/abs/2410.07864)** (2024) — 12 亿参数扩散 Transformer，采用跨机器人统一动作空间，面向双臂操作。 · [代码](https://github.com/thu-ml/RoboticsDiffusionTransformer)
- **[PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378)** (2023) — 将连续传感器嵌入注入 5620 亿参数语言模型，用于具身推理与规划。
- **[A Generalist Agent](https://arxiv.org/abs/2205.06175)** (2022) — Gato：同一套权重的 Transformer 既能玩游戏、写图像描述，也能用真实机械臂堆积木。
- **[RT-1: Robotics Transformer for Real-World Control at Scale](https://arxiv.org/abs/2212.06817)** (2022) — 将动作离散化为 token，用 13 万条真实演示训练 Transformer，证明机器人策略会随数据多样性扩展。 · [代码](https://github.com/google-research/robotics_transformer)
- _另见:_ [Cracking Mobile Manipulation](#navigation), [Open X-Embodiment](#datasets), [Evaluating Real-World Robot Manipulation Policies in Simulation](#datasets), [Embodied Skill Bench](#datasets)

<a id="manipulation"></a>
### 操作与灵巧手

_模仿学习、扩散策略、抓取、双臂与灵巧操作。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/manipulation.html)

- ⭐ **[Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](https://arxiv.org/abs/2402.10329)** (2024) — 手持夹爪加 GoPro 可随处采集演示，训练出的策略可直接迁移到机械臂。 · [代码](https://github.com/real-stanford/universal_manipulation_interface)
- ⭐ **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** (2023) — 以去噪方式生成动作序列，比回归更能处理多模态演示，已成为模仿学习标准基线。 · [代码](https://github.com/real-stanford/diffusion_policy)
- ⭐ **[Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705)** (2023) — ALOHA + ACT：约 2 万美元的双臂遥操作平台，加上动作分块 Transformer，约 50 条演示即可学会精细任务。 · [代码](https://github.com/tonyzhaozh/act)
- **[Blind Precise Assembly: Proprioceptive Sim-to-Real Peg-in-Hole for Diverse Parts](https://arxiv.org/abs/2610.23849)** (2026) — 探究仅靠关节读数能否完成毫米级精密插装：训练不用相机、力或触觉输入的 sim-to-real 策略。
- **[Can a Frontier VLM Serve as a Robot Policy for Memory-Dependent Manipulation?](https://arxiv.org/abs/2610.17350)** (2026) — 冻结的前沿 VLM 以整段回合为上下文直接输出路径点，在 RoboMME 记忆类任务上报告 92.1% 成功率，且无需任务训练。 · [代码](https://github.com/jackbjed/embodied-astra-robomme) · [项目页](https://embodied-astra.github.io)
- **[3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations](https://arxiv.org/abs/2403.03954)** (2024) — 用紧凑点云编码作为扩散策略条件，比图像输入更省数据、对视角更鲁棒。 · [代码](https://github.com/YanjieZe/3D-Diffusion-Policy)
- **[DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation](https://arxiv.org/abs/2403.07788)** (2024) — 可穿戴动捕手套与相机采集人手动作，重定向后用于训练灵巧机器人手。
- **[Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation](https://arxiv.org/abs/2401.02117)** (2024) — 将 ALOHA 装上移动底盘；与静态 ALOHA 数据联合训练显著提升做饭、开柜等移动任务表现。 · [代码](https://github.com/MarkFzp/mobile-aloha)
- **[VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://arxiv.org/abs/2307.05973)** (2023) — 大模型编写代码组合 3D 可供性/约束地图，再由规划器生成轨迹，无需机器人训练。
- **[R3M: A Universal Visual Representation for Robot Manipulation](https://arxiv.org/abs/2203.12601)** (2022) — 在 Ego4D 人类视频上预训练视觉编码器，显著提高下游模仿学习的数据效率。
- **[Visual Dexterity: In-Hand Reorientation of Novel and Complex Object Shapes](https://arxiv.org/abs/2211.11744)** (2022) — 仅凭深度相机即可在手中翻转未见过的物体，策略在仿真中训练。
- **[Solving Rubik's Cube with a Robot Hand](https://arxiv.org/abs/1910.07113)** (2019) — 自动域随机化让仿真训练的灵巧手策略在真实硬件上操作魔方。
- **[Learning Dexterous In-Hand Manipulation](https://arxiv.org/abs/1808.00177)** (2018) — 完全在随机化仿真中用强化学习训练，Shadow 灵巧手在真实世界翻转方块，是 sim-to-real 里程碑。
- _另见:_ [3D-ViTac](#tactile), [Code as Policies](#navigation), [OK-Robot](#navigation), [Cracking Mobile Manipulation](#navigation), [FoundationPose](#perception), [cuRobo](#control), [Motion Policy Networks](#control), [LeRobot](#datasets), [LEAP Hand](#hardware)

<a id="tactile"></a>
### 触觉与视触觉感知

_触觉传感器、触觉表征与接触丰富的控制。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/tactile.html)

- ⭐ **[DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](https://arxiv.org/abs/2005.14679)** (2020) — 低成本、紧凑的 GelSight 式指尖传感器，让视触觉传感器得以普及。 · [代码](https://github.com/facebookresearch/digit-interface)
- **[3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing](https://arxiv.org/abs/2410.24091)** (2024) — 在扩散策略中融合密集触觉阵列与 3D 视觉，完成易碎、接触丰富的双臂任务。
- **[AnySkin: Plug-and-play Skin Sensing for Robotic Touch](https://arxiv.org/abs/2409.08276)** (2024) — 可更换的磁性触觉皮肤，更换皮肤后训练好的策略仍能继续使用。
- **[Binding Touch to Everything: Learning Unified Multimodal Tactile Representations](https://arxiv.org/abs/2401.18084)** (2024) — UniTouch 将触觉信号与视觉、语言、音频嵌入对齐，实现零样本触觉理解。
- **[Sparsh: Self-supervised touch representations for vision-based tactile sensing](https://arxiv.org/abs/2410.24090)** (2024) — 在大量触觉图像上自监督预训练的编码器，可跨不同视触觉传感器使用。 · [代码](https://github.com/facebookresearch/sparsh)
- **[TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors](https://arxiv.org/abs/2012.08456)** (2020) — 在仿真中渲染 DIGIT/GelSight 式触觉图像，便于大规模训练基于触觉的策略。 · [代码](https://github.com/facebookresearch/tacto)

<a id="locomotion"></a>
### 运动控制与人形机器人

_足式运动、人形全身控制与跑酷。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/locomotion.html)

- ⭐ **[Real-World Humanoid Locomotion with Reinforcement Learning](https://arxiv.org/abs/2303.03381)** (2023) — 在仿真中训练的因果 Transformer 策略零样本驱动全尺寸人形机器人在户外行走。
- ⭐ **[Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](https://arxiv.org/abs/2109.11978)** (2021) — 数千个 GPU 并行环境几分钟就能训练出四足行走策略；legged_gym 成为标准入门框架。 · [代码](https://github.com/leggedrobotics/legged_gym)
- **[ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](https://arxiv.org/abs/2502.01143)** (2025) — 从真实轨迹学习残差"增量动作"模型来修正仿真物理，实现敏捷的人形运动技能。 · [代码](https://github.com/LeCAR-Lab/ASAP)
- **[Expressive Whole-Body Control for Humanoid Robots](https://arxiv.org/abs/2402.16796)** (2024) — 上半身模仿人类动捕、下肢保持鲁棒行走，让人形机器人做出富有表现力的动作和舞蹈。
- **[HumanPlus: Humanoid Shadowing and Imitation from Humans](https://arxiv.org/abs/2406.10454)** (2024) — 人形机器人通过单个 RGB 相机实时模仿人类，再用采集的数据学习自主技能。 · [代码](https://github.com/MarkFzp/humanplus)
- **[Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](https://arxiv.org/abs/2403.04436)** (2024) — H2O：强化学习跟踪策略借助 RGB 相机，把人的全身动作实时映射到人形机器人。
- **[Extreme Parkour with Legged Robots](https://arxiv.org/abs/2309.14341)** (2023) — 端到端深度相机策略让小型四足机器人完成跳远、跳高和倒立。 · [代码](https://github.com/chengxuxin/extreme-parkour)
- **[Robot Parkour Learning](https://arxiv.org/abs/2309.05665)** (2023) — 将多个跑酷专家技能蒸馏为单一视觉策略，让低成本四足机器人攀爬、跳跃和匍匐。 · [代码](https://github.com/ZiwenZhuang/parkour)
- **[RMA: Rapid Motor Adaptation for Legged Robots](https://arxiv.org/abs/2107.04034)** (2021) — 自适应模块在线估计环境参数，使同一策略实时适应新地形和负载。
- **[Learning Quadrupedal Locomotion over Challenging Terrain](https://arxiv.org/abs/2010.11251)** (2020) — 仅依赖本体感知的师生策略，让 ANYmal 在泥地、雪地和碎石等野外地形行走。
- **[Learning Agile and Dynamic Motor Skills for Legged Robots](https://arxiv.org/abs/1901.08652)** (2019) — 学习的执行器模型缩小仿真与现实差距，使强化学习策略能让 ANYmal 奔跑并摔倒后起身。
- _另见:_ [Open-TeleVision](#hardware), [Berkeley Humanoid](#hardware)

<a id="world-models"></a>
### 世界模型

_学习的动力学模型、视频世界模型与基于模型的强化学习。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/world-models.html)

- ⭐ **[Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104)** (2023) — DreamerV3：一套超参数适用于 150 多个任务，包括从零开始在《我的世界》中挖到钻石。 · [代码](https://github.com/danijar/dreamerv3)
- **[Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575)** (2025) — 开放的视频世界基础模型及分词器与数据管线，用于生成物理 AI 训练数据。
- **[V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985)** (2025) — 自监督视频编码器经少量机器人数据后训练，通过潜空间预测实现零样本抓放规划。
- **[Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391)** (2024) — 仅从无标注的网络视频中学习可交互环境与潜在动作。
- **[Learning Interactive Real-World Simulators](https://arxiv.org/abs/2310.06114)** (2023) — UniSim：以动作为条件的视频生成模型充当仿真器，训练出的策略可迁移到真实世界。
- **[DayDreamer: World Models for Physical Robot Learning](https://arxiv.org/abs/2206.14176)** (2022) — 直接在真实机器人上训练 Dreamer——四足机器人无需仿真器，约一小时学会行走。
- **[World Models](https://arxiv.org/abs/1803.10122)** (2018) — 经典的 VAE + RNN 智能体，学习环境的压缩模型并在"梦境"中训练控制器。 · [项目页](https://worldmodels.github.io/)
- _另见:_ [Planning with Diffusion for Flexible Behavior Synthesis](#control)

<a id="navigation"></a>
### 导航与具身智能体

_视觉语言导航、具身问答、移动操作与大模型规划。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/navigation.html)

- ⭐ **[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)** (2022) — SayCan：大模型提出步骤，学习到的价值函数评估机器人当下实际能做什么。
- **[Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System](https://arxiv.org/abs/2610.19600)** (2026) — 发现 VLA 在原子技能上 80% 成功率、组合成移动操作后仅 19%，分析失败原因并据此构建智能体式系统。 · [代码](https://github.com/PKU-VaLuE-Lab/Cracking-Mobile-Manipulation)
- **[OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics](https://arxiv.org/abs/2401.12202)** (2024) — 组合现成的开放词汇模型，构建无需训练即可在真实家庭中抓取放置的系统。
- **[NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](https://arxiv.org/abs/2310.07896)** (2023) — 通过对目标做掩码，单一扩散策略同时完成目标导航与探索。
- **[Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753)** (2022) — 大模型编写调用感知与控制 API 的 Python 代码，把指令变成可响应的机器人程序。
- **[Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608)** (2022) — 将成功检测与场景描述反馈给大模型规划器，使其在失败后重新规划。
- **[Visual Language Maps for Robot Navigation](https://arxiv.org/abs/2210.05714)** (2022) — VLMaps 将视觉语言特征融合进 3D 地图，使机器人可按开放词汇空间目标导航。
- **[Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](https://arxiv.org/abs/1711.07280)** (2017) — 提出视觉语言导航任务与基于 Matterport3D 的 Room-to-Room (R2R) 基准。
- _另见:_ [ConceptGraphs](#perception), [Habitat](#datasets), [Embodied Skill Bench](#datasets)

<a id="perception"></a>
### 感知、SLAM 与三维建图

_视觉/激光 SLAM 与里程计、三维重建、物体位姿、深度估计与开放词汇场景地图。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/perception.html)

- ⭐ **[ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](https://arxiv.org/abs/2007.11898)** (2020) — 最常用的特征点 SLAM 库：支持单目、双目与 RGB-D，可融合 IMU，并支持多地图重定位。 · [代码](https://github.com/UZ-SLAMLab/ORB_SLAM3)
- **[VGGT: Visual Geometry Grounded Transformer](https://arxiv.org/abs/2503.11651)** (2025) — 单个前馈 Transformer 一次性为多视角图像预测相机参数、深度、点图与跟踪，约一秒完成。 · [代码](https://github.com/facebookresearch/vggt)
- **[Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](https://arxiv.org/abs/2401.10891)** (2024) — 在数千万张伪标注图像上训练的单目深度模型，常被机器人系统直接拿来作为深度先验。 · [代码](https://github.com/LiheYoung/Depth-Anything)
- **[ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650)** (2023) — 用视觉语言模型构建带语义标注的物体级三维场景图，大模型规划器可以用自然语言查询。 · [项目页](https://concept-graphs.github.io/)
- **[DUSt3R: Geometric 3D Vision Made Easy](https://arxiv.org/abs/2312.14132)** (2023) — 不需要已知相机内参或位姿，直接从图像对回归三维点图，开启了“三维基础模型”这一方向。 · [代码](https://github.com/naver/dust3r)
- **[FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects](https://arxiv.org/abs/2312.08344)** (2023) — 只需 CAD 模型或少量参考图像即可对未见过的物体做 6D 位姿估计与跟踪，无需逐物体训练。 · [代码](https://github.com/NVlabs/FoundationPose)
- **[Gaussian Splatting SLAM](https://arxiv.org/abs/2312.06741)** (2023) — MonoGS：直接在三维高斯地图上做 SLAM，仅用单个相机即可同时完成相机跟踪与照片级稠密建图。 · [代码](https://github.com/muskie82/MonoGS)
- **[DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](https://arxiv.org/abs/2108.10869)** (2021) — 端到端学习的视觉 SLAM：循环光流更新加上可微分的光束法平差层。 · [代码](https://github.com/princeton-vl/DROID-SLAM)
- **[FAST-LIO2: Fast Direct LiDAR-inertial Odometry](https://arxiv.org/abs/2107.06829)** (2021) — 用增量 k-d 树把原始激光点直接配准到地图，速度足以在无人机和机器人机载计算机上运行。 · [代码](https://github.com/hku-mars/FAST_LIO)
- **[LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping](https://arxiv.org/abs/2007.00258)** (2020) — 基于因子图的激光-惯性里程计，GPS 与回环可以作为额外因子直接加入。 · [代码](https://github.com/TixiaoShan/LIO-SAM)

<a id="control"></a>
### 规划、控制与安全

_运动规划、轨迹优化、模型预测控制、安全滤波器与安全的学习型控制。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/control.html)

- ⭐ **[cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation](https://arxiv.org/abs/2310.17274)** (2023) — 面向机械臂的 GPU 并行运动生成：同时运行大量轨迹优化，在毫秒级给出无碰撞且平滑的轨迹。 · [代码](https://github.com/NVlabs/curobo)
- **[Motion Policy Networks](https://arxiv.org/abs/2210.12209)** (2022) — 在数百万条规划器生成的轨迹上训练的神经策略，可直接根据点云把机械臂移动到目标位置。 · [代码](https://github.com/NVlabs/motion-policy-networks)
- **[Planning with Diffusion for Flexible Behavior Synthesis](https://arxiv.org/abs/2205.09991)** (2022) — Diffuser：把规划视为对整条轨迹去噪，目标与奖励可以引导采样；扩散模型与控制结合的早期代表作。 · [代码](https://github.com/jannerm/diffuser)
- **[Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning](https://arxiv.org/abs/2108.06266)** (2021) — 综述，连接控制理论与强化学习两种安全视角：从带保证的学习动力学到约束强化学习与安全滤波器。
- **[safe-control-gym: a Unified Benchmark Suite for Safe Learning-based Control and Reinforcement Learning in Robotics](https://arxiv.org/abs/2109.06325)** (2021) — Gym 风格基准，含倒立摆与四旋翼任务、约束与扰动，用于比较安全控制与安全强化学习方法。 · [代码](https://github.com/utiasDSL/safe-control-gym)
- **[Control Barrier Functions: Theory and Applications](https://arxiv.org/abs/1903.11199)** (2019) — 控制障碍函数教程：为任意控制器加一层“尽量少改动”的安全滤波器、保证系统安全的标准方法。

<a id="sim"></a>
### 仿真与 Sim-to-Real

_物理仿真器、GPU 并行训练与向真实机器人迁移。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/sim.html)

- ⭐ **[MuJoCo](https://mujoco.org/)** (2012) — 快速准确的接触物理仿真，机器人学习研究的默认仿真器，由 DeepMind 开源。 · [代码](https://github.com/google-deepmind/mujoco)
- **[MuJoCo Playground](https://arxiv.org/abs/2502.08844)** (2025) — 基于 MJX 的 GPU 加速运动与操作环境，几分钟即可训练并迁移到真实机器人。 · [代码](https://github.com/google-deepmind/mujoco_playground)
- **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** (2024) — 开源、Python 原生的物理平台，覆盖刚体、软体、流体，支持高速 GPU 仿真。
- **[ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI](https://arxiv.org/abs/2410.00425)** (2024) — GPU 并行仿真与渲染，内置大量操作任务，适合快速视觉强化学习与数据生成。 · [代码](https://github.com/haosulab/ManiSkill)
- **[RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)** (2024) — 120 个厨房场景、2500 多个物体与 100 个任务，并附生成演示，用于训练通用策略。 · [代码](https://github.com/robocasa/robocasa)
- **[Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments](https://arxiv.org/abs/2301.04195)** (2023) — Isaac Lab 的前身，在 Isaac Sim 之上提供模块化的机器人、传感器与任务。 · [代码](https://github.com/isaac-sim/IsaacLab)
- **[Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning](https://arxiv.org/abs/2108.10470)** (2021) — 物理仿真与策略全程在 GPU 上运行，单卡即可并行数千个环境。
- **[SAPIEN: A SimulAted Part-based Interactive ENvironment](https://arxiv.org/abs/2003.08515)** (2020) — 包含大规模铰接物体（PartNet-Mobility）的仿真器，适合开抽屉等交互任务。
- **[robosuite: A Modular Simulation Framework and Benchmark for Robot Learning](https://arxiv.org/abs/2009.12293)** (2020) — 基于 MuJoCo 的模块化操作环境，是众多模仿学习基准的底座。 · [代码](https://github.com/ARISE-Initiative/robosuite)
- **[Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://arxiv.org/abs/1703.06907)** (2017) — 在仿真中随机化纹理、光照和相机，使视觉模型无需真实数据即可在真实图像上工作。
- **[Sim-to-Real Transfer of Robotic Control with Dynamics Randomization](https://arxiv.org/abs/1710.06537)** (2017) — 训练中随机化物理参数，得到足以在真实机械臂上运行的鲁棒控制策略。
- _另见:_ [Blind Precise Assembly](#manipulation), [TACTO](#tactile), [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](#locomotion), [Habitat](#datasets)

<a id="datasets"></a>
### 数据集与基准

_大规模机器人数据集、第一视角数据与评测基准。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/datasets.html)

- ⭐ **[LeRobot](https://github.com/huggingface/lerobot)** (2024) — PyTorch 机器人学习库，提供数据集、预训练策略（ACT、Diffusion、SmolVLA）与低成本机械臂驱动。
- ⭐ **[LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)** (2023) — 四个套件共 130 个语言条件任务，现已成为 VLA 论文最常用的仿真基准。 · [代码](https://github.com/Lifelong-Robot-Learning/LIBERO)
- ⭐ **[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)** (2023) — 30 多个实验室汇集 22 种机器人的 100 多万条轨迹；在其上训练的 RT-X 优于单机器人基线。 · [代码](https://github.com/google-deepmind/open_x_embodiment)
- **[Embodied Skill Bench: Benchmarking How Well Agents with Embodied Skills Perform on Physical Tasks](https://arxiv.org/abs/2610.16238)** (2026) — 将 VLA 策略、感知模型与经验知识封装成 250 个可复用的“具身技能”，评测它们对大模型智能体完成物理任务的帮助。 · [代码](https://github.com/HanZhi306/EmbodiedSkill-Bench)
- **[AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://arxiv.org/abs/2503.06669)** (2025) — 在专门搭建的场景中采集的百万级真实机器人数据集，并基于其训练通用策略 GO-1。
- **[DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://arxiv.org/abs/2403.12945)** (2024) — 由多家机构在数百个真实场景中采集的 7.6 万条 Franka 遥操作轨迹。 · [代码](https://github.com/droid-dataset/droid)
- **[Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941)** (2024) — SimplerEnv：真实到仿真的评测环境，其得分与 RT-1/Octo 类策略的真机表现相关。 · [代码](https://github.com/simpler-env/SimplerEnv)
- **[BridgeData V2: A Dataset for Robot Learning at Scale](https://arxiv.org/abs/2308.12952)** (2023) — 在低成本 WidowX 机械臂上采集、涵盖众多厨房与任务的 6 万条轨迹，常用作预训练数据。
- **[RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot](https://arxiv.org/abs/2307.00595)** (2023) — 11 万多条接触丰富的序列，包含视觉、力、音频及配对的人类演示视频。
- **[CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](https://arxiv.org/abs/2112.03227)** (2021) — 连续执行五条语言指令，测试长时程、语言条件下的控制能力。 · [代码](https://github.com/mees/calvin)
- **[Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058)** (2021) — 3670 小时第一视角日常生活视频，广泛用于为机器人预训练视觉表征。
- **[Habitat: A Platform for Embodied AI Research](https://arxiv.org/abs/1904.01201)** (2019) — 极速的逼真 3D 仿真器与任务集，统一了具身导航研究的标准。 · [代码](https://github.com/facebookresearch/habitat-sim)
- **[Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning](https://arxiv.org/abs/1910.10897)** (2019) — 50 个 Sawyer 操作任务，用于多任务与元强化学习评测。 · [代码](https://github.com/Farama-Foundation/Metaworld)
- **[RLBench: The Robot Learning Benchmark & Learning Environment](https://arxiv.org/abs/1909.12271)** (2019) — 100 个手工设计的操作任务并附演示，是 PerAct 等 3D 策略方法的常用基准。 · [代码](https://github.com/stepjam/RLBench)
- _另见:_ [Universal Manipulation Interface](#manipulation), [Vision-and-Language Navigation](#navigation), [safe-control-gym](#control), [robosuite](#sim), [RoboCasa](#sim)

<a id="hardware"></a>
### 硬件与开源机器人

_可自行搭建的低成本机械臂、灵巧手、夹爪与数据采集设备。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/hardware.html)

- ⭐ **[LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning](https://arxiv.org/abs/2309.06440)** (2023) — 16 自由度灵巧手，用现成零件约 2000 美元即可搭建。 · [项目页](https://leaphand.com/)
- **[Berkeley Humanoid: A Research Platform for Learning-based Control](https://arxiv.org/abs/2407.21781)** (2024) — 中等尺寸、低成本的人形机器人，专为强化学习运动策略的 sim-to-real 迁移设计。
- **[Open-TeleVision: Teleoperation with Immersive Active Visual Feedback](https://arxiv.org/abs/2407.01512)** (2024) — 带主动转向立体相机的 VR 遥操作系统，用于采集人形机器人操作数据。 · [代码](https://github.com/OpenTeleVision/TeleVision)
- **[SO-ARM100 / SO-101](https://github.com/TheRobotStudio/SO-ARM100)** (2024) — 开源 3D 打印 6 自由度机械臂（主从臂），每只约 100–200 美元，是 LeRobot 的默认入门套件。
- **[GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators](https://arxiv.org/abs/2309.13037)** (2023) — 3D 打印的机械臂运动学复刻件，实现低成本、直观的关节空间遥操作。 · [代码](https://github.com/wuphilipp/gello_software)
- _另见:_ [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](#manipulation), [Mobile ALOHA](#manipulation), [Universal Manipulation Interface](#manipulation), [DexCap](#manipulation), [DIGIT](#tactile), [AnySkin](#tactile), [LeRobot](#datasets)

<!-- radar:end -->

## 参与贡献

发现缺少的好论文、代码库、数据集或机器人，或者发现错误？欢迎 [提交 issue](https://github.com/hu-zlatan/embodied-ai-radar/issues/new)，或提交一个在 `data/curated/<主题>.yaml` 中新增条目的 PR。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 项目如何运作

本仓库由 **AI 智能体**（Anthropic 的 Claude）按计划自动构建和维护，并由 [@hu-zlatan](https://github.com/hu-zlatan) 监督。智能体的工作章程见 [AUTOPILOT.md](AUTOPILOT.md)，笔记、决策和运行日志见 [`.autopilot/`](.autopilot)。数据绝不编造：未通过核验的条目会被修正或删除。

## 许可

代码：[MIT](LICENSE)。精选文本与数据：[CC BY 4.0](LICENSE-DATA.md)。arXiv 元数据：CC0，来自 [arXiv API](https://info.arxiv.org/help/api/index.html)。
