# 具身智能雷达 · Embodied AI Radar

**中英双语（[English](README.md) / 中文）、持续更新的具身智能与机器人学习全景图。**
人工核验的论文、代码、数据集、仿真器与硬件，配一句话要点；外加每天自动抓取并按主题标注的 arXiv 机器人新论文。

### 🌐 [打开网站 → hu-zlatan.github.io/embodied-ai-radar](https://hu-zlatan.github.io/embodied-ai-radar/?lang=zh)

![具身智能雷达网站截图](docs/screenshot.png)

**刚入门？** 跟着[入门路线](https://hu-zlatan.github.io/embodied-ai-radar/start.html?lang=zh)读：10 个阶段，从强化学习/模仿学习基础，到视觉运动策略、VLA、仿真、足式运动、世界模型，再到可以动手搭建的硬件，共 41 个精选条目，每条都有中英文要点。

## 特点

- **可信**：每个精选条目的 arXiv 编号都会与 arXiv 核对，所有链接每周由 CI 自动检查。
- **新鲜**：GitHub Action 每天抓取 cs.RO 新论文（以及 cs.CV / cs.LG / cs.AI / cs.CL 中的机器人相关论文）并按主题标注，自动出现在网站上。
- **好找**：快速静态网站，支持即时搜索（可直接输入中文关键词，如“人形 强化学习”“触觉”，自动匹配英文论文）与筛选（主题 · 机器人形态：机械臂、灵巧手、人形、足式、无人机… · 已录用会议（CoRL、NeurIPS、IROS 等） · 精选/每日 · 是否有代码），手机友好。已被会议接收的论文还按会议汇总成页面，例如 [CoRL 2026](https://hu-zlatan.github.io/embodied-ai-radar/venues/corl-2026.html?lang=zh)（[全部会议/期刊](https://hu-zlatan.github.io/embodied-ai-radar/venues/index.html?lang=zh)）；每种机器人形态也有独立页面和 Atom 订阅，例如 [人形](https://hu-zlatan.github.io/embodied-ai-radar/robots/humanoid.html?lang=zh) · [灵巧手](https://hu-zlatan.github.io/embodied-ai-radar/robots/hand.html?lang=zh) · [四足](https://hu-zlatan.github.io/embodied-ai-radar/robots/legged.html?lang=zh)。
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

⭐ = 重点推荐。由 [`data/curated/`](data/curated) 自动生成——请修改 YAML，而不是这个列表。

<!-- radar:start -->

[VLA 与机器人基础模型](#vla) · [操作与灵巧手](#manipulation) · [触觉与视触觉感知](#tactile) · [运动控制与人形机器人](#locomotion) · [世界模型](#world-models) · [导航与具身智能体](#navigation) · [感知、SLAM 与三维建图](#perception) · [规划、控制与安全](#control) · [机器人学习：强化学习与模仿学习](#learning) · [仿真与 Sim-to-Real](#sim) · [数据集与基准](#datasets) · [硬件与开源机器人](#hardware)

<a id="vla"></a>
### VLA 与机器人基础模型

_视觉-语言-动作模型与通用机器人策略。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/vla.html)

- ⭐ **[π\*0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759)** (2025) — RECAP 通过优势条件化，用演示、机器人自主运行数据和遥操作纠正对 VLA 做强化学习；论文报告在叠衣服、做意式咖啡等难任务上吞吐量提升一倍以上、失败率约减半。 · [项目页](https://pi.website/blog/pistar06)
- ⭐ **[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** (2024) — VLM 主干加流匹配动作专家，跨多种机器人训练，能完成叠衣服等长时程灵巧任务。 · [代码](https://github.com/Physical-Intelligence/openpi)
- ⭐ **[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** (2024) — 基于 Llama 2 与 DINOv2/SigLIP 的 7B 开源 VLA，是 VLA 研究与 LoRA 微调的事实开源基线。 · [代码](https://github.com/openvla/openvla)
- ⭐ **[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** (2023) — 提出 "VLA" 概念：把网络规模的视觉语言模型联合微调为输出动作 token，把语义知识迁移到机器人控制。 · [项目页](https://robotics-transformer2.github.io/)
- **[CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance](https://arxiv.org/abs/2610.21453)** (2026) — 给冻结的 VLA 套上双环框架：规划环保存用户偏好与场景记忆以做个性化任务分解，执行环拦截危险接触并调用可复用的恢复技能；报告安全违规率从 52.6% 降到 6.1%，失败恢复成功率从 13% 提升到 80%。 · [代码](https://github.com/JIA-Lab-research/CarryOn) · [项目页](https://vincent2311.github.io/Projects/CarryOn/)
- **[CondenseVLA: Learnable History Condensation for Efficient Multi-Frame VLA](https://arxiv.org/abs/2610.25927)** (2026) — 不靠简单加长历史帧窗口，而是学习把过去的帧压缩成少量 token，保留短暂接触、遮挡等转瞬即逝的线索。 · [代码](https://github.com/FeiyangHong/CondenseVLA)
- **[FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies](https://arxiv.org/abs/2610.31427)** (2026) — 让前沿大模型监督冻结的 π0.5 策略的执行框架：随着经验积累逐步减少审查频率，并把监督集中在出错后的恢复上；报告在四个仿真任务上审查 token 平均减少约 57%，成功率也更高。 · [代码](https://github.com/FastHarness/fast-harness)
- **[FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2610.22146)** (2026) — 只保留当前任务所需的视觉 token、并让 token 预算随时间步变化，以加快 VLA 推理。 · [代码](https://github.com/jiuyixu25/FastVLA)
- **[From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks](https://arxiv.org/abs/2610.30051)** (2026) — 让六个前沿通用大模型通过工具调用（指定末端位姿与夹爪开合）直接控制 LIBERO-10 机械臂，无任何机器人专门训练；报告的最高成功率为 44%。提高推理强度通常有帮助，但推理成本更高。 · [代码](https://github.com/IRVLUTD/LLM_LIBERO) · [项目页](https://irvlutd.github.io/LLM-LIBERO/)
- **[Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates](https://arxiv.org/abs/2610.31859)** (2026) — 实用警示：VLA 权重以 bf16 微调且不保留 fp32 主副本时，小于权重 1/512 的 AdamW 更新会被舍入抹掉；报告 12 个开源 VLA 代码库中 9 个的默认或文档配方如此训练，LIBERO 实验中至少 79% 的更新被抹除。
- **[Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471)** (2026) — 用冻结的前沿大模型加上下文“知识包”直接控制机器人，覆盖 12 个仿真基准和 8 台真机；报告在 12 个基准中的 9 个超过此前最好结果，但真机表现较弱——结论是具备了具身“能力”，尚未达到具身“智能”。 · [项目页](https://github.com/OpenSenseNova/SenseNova-RoboRSI)
- **[LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models](https://arxiv.org/abs/2610.21362)** (2026) — 通过缓存相邻观测之间的紧凑潜在转移，为 π0.5 加入记忆，面向关键物体移出视野的任务。 · [代码](https://github.com/buaa-colalab/LTM-pi)
- **[MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models](https://arxiv.org/abs/2610.22951)** (2026) — 保留 π0.5 预训练的视觉语言编码器，把在去噪循环中被反复调用的 Transformer 动作专家换成紧凑的 Mamba 专家，以降低推理开销。 · [代码](https://github.com/giakhuyendihoc/MambaAct)
- **[MorphAct: Robot Policies Morphing with the Worlds They Act In](https://arxiv.org/abs/2610.20019)** (2026) — 不再让 VLA 在所有交互情境下共用固定参数，而是按当前情境为视觉语言模块和动作模块生成耦合的低秩参数更新；报告在 LIBERO/Meta-World 上最高提升 16.3%，真机上相对 π0.5 最高提升 14%。 · [代码](https://github.com/MINT-SJTU/MorphAct) · [项目页](https://mint-sjtu.github.io/MorphAct.io/)
- **[Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use](https://arxiv.org/abs/2610.30108)** (2026) — 用"感知、预判、规划、执行、验证"五种能力统一看待电脑操作智能体和机器人智能体的综述；统计 64 个基准后发现只有 5 个评测预判、3 个评测验证。附配套论文列表。 · [项目页](https://github.com/showlab/Awesome-Multimodal-Embodied-Agent)
- **[NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models](https://arxiv.org/abs/2610.23271)** (2026) — 先独立学习各项技能，再用嵌套超网络“生成”VLA 参数来事后整合技能，而不是直接合并权重。 · [代码](https://github.com/WanyuGroup/NeurIPS2026-NestedVLA)
- **[Post-hoc Epistemic Uncertainty for Vision-Language-Action Policies](https://arxiv.org/abs/2610.29730)** (2026) — 在训练完成后为单个 VLA 策略加上轻量的核方差头（基于训练示教嵌入的高斯过程方差）来估计认知不确定性，无需训练和运行策略集成，让机器人知道何时该求助或补充示教。 · [代码](https://github.com/post-hoc-vla-uncertainty/post-hoc-vla-uncertainty)
- **[REKI: Registering Knowledge in VLAs](https://arxiv.org/abs/2610.22178)** (2026) — 仅用公开数据预训练的 2.4B VLM + 流匹配 VLA；报告称只输给约两倍大的模型，并用少量寄存器 token 实现低成本记忆。 · [代码](https://github.com/kyutai-labs/reki)
- **[RynnBrain: Open Embodied Foundation Models](https://arxiv.org/abs/2602.14979)** (2026) — 开源时空具身基础模型（2B、8B 与 30B-A3B MoE），覆盖第一视角理解、时空定位、物理落地推理与规划，并提供导航、规划、VLA、CoP 等后训练版本。 · [代码](https://github.com/alibaba-damo-academy/RynnBrain) · [项目页](https://alibaba-damo-academy.github.io/RynnBrain.github.io)
- **[Towards Agentic Robots: Model, Data, Environment, and Harness](https://arxiv.org/abs/2610.20442)** (2026) — 关于"智能体化机器人"的综述：基础模型智能体负责规划、采集与筛选数据、构建环境与测试并自主纠错；把相关研究归为模型、数据、环境、执行框架四大领域下的 17 个类别，附配套论文列表。 · [项目页](https://github.com/chonghanqin/Awesome-Agentic-Robots)
- **[VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](https://arxiv.org/abs/2610.21306)** (2026) — 认为 VLA 容易过拟合“观测→动作”的对应关系，因此显式监督动作应引起的物理状态变化，而不是在语言或像素空间里预测未来状态。 · [代码](https://github.com/ZJU-OmniAI/VLA-Delta)
- **[VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse](https://arxiv.org/abs/2610.25043)** (2026) — 流匹配 VLA 每次只执行动作块的前几步，剩余部分通常丢弃；本文把这段"动作尾巴"作为下一块的起点，并用小型置信度模型决定还需去噪多少步；论文报告在 π0.5、SmolVLA 等模型上降低推理开销。
- **[WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction](https://arxiv.org/abs/2610.18568)** (2026) — 在预训练 VLA 上加一个 2.57 亿参数的潜空间世界模型，用预测的未来表征去条件化动作专家，无需像素生成或大规模视频预训练；报告 LIBERO 成功率 98.7%，真机任务上明显优于 π0.5。 · [代码](https://github.com/AutoLab-SAI-SJTU/WAVE-0) · [项目页](https://hmwang2002.github.io/release/wave0/)
- **[When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies](https://arxiv.org/abs/2610.30735)** (2026) — 在六个基于流匹配的 VLA 上实验，报告单步 Euler 生成动作在规模足够时与多步采样效果基本相当——在为提速引入专门的单步生成目标之前值得先看（CoRL 2026）。
- **[π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)** (2025) — 通过异构数据联合训练，让移动操作机器人在从未见过的家庭中整理厨房和卧室。 · [代码](https://github.com/Physical-Intelligence/openpi)
- **[Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos](https://arxiv.org/abs/2507.15597)** (2025) — 灵巧手 VLA：先在动捕、VR 与普通视频中的人手动作上预训练（"物理指令微调"），使用部件级动作 token，再做三维空间对齐，并针对真实机器人灵巧手后训练。 · [代码](https://github.com/BeingBeyond/Being-H0) · [项目页](https://beingbeyond.github.io/Being-H0)
- **[ChatVLA: Unified Multimodal Understanding and Robot Control with Vision-Language-Action Model](https://arxiv.org/abs/2502.14420)** (2025) — 让 VLA 保留“对话”能力：通过分阶段对齐训练和混合专家结构缓解遗忘与任务干扰；论文报告在保持 VQA/MMMU 等多模态理解成绩的同时，在 25 个真实操作任务上优于 OpenVLA。 · [代码](https://github.com/tutujingyugang1/ChatVLA_public) · [项目页](https://chatvla.github.io)
- **[DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control](https://arxiv.org/abs/2502.05855)** (2025) — 将 2B 的 Qwen2-VL 与约 1B 参数、按机器人分头输出的可插拔扩散动作专家结合，分三阶段训练（跨本体预训练、本体对齐、任务适配）；报告无需任务专门微调即可叠衬衫，LIBERO 平均 97.3。 · [项目页](https://dex-vla.github.io/)
- **[FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747)** (2025) — 用基于 DCT 的分词器压缩动作块，使自回归 VLA 能学习高频灵巧控制。
- **[Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645)** (2025) — OpenVLA-OFT：并行解码、动作分块与连续动作让 VLA 微调更快、成功率更高。 · [代码](https://github.com/moojink/openvla-oft)
- **[GR-3 Technical Report](https://arxiv.org/abs/2507.15493)** (2025) — 字节跳动 Seed 的通用 VLA——机器人数据模仿学习并与网络视觉-语言数据联合训练，再用 VR 采集的人类轨迹快速适配；在 ByteMini 双臂移动机器人上展示长时程与衣物操作任务。
- **[GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)** (2025) — 双系统（VLM 慢思考 + 扩散快执行）人形机器人策略，用真实、人类视频与合成数据训练。 · [代码](https://github.com/NVIDIA/Isaac-GR00T)
- **[Galaxea Open-World Dataset and G0 Dual-System VLA Model](https://arxiv.org/abs/2509.00576)** (2025) — 在单一移动双臂机器人（R1 Lite）上采集约 500 小时、10 万条轨迹、覆盖 50 个真实场景，并提出 G0：VLM 规划器 + 流匹配 VLA 执行器的双系统模型；论文报告单本体预训练对少样本迁移最关键。 · [代码](https://github.com/OpenGalaxea/GalaxeaVLA)
- **[Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020)** (2025) — 基于 Gemini 2.0 的 VLA 与具身推理模型，面向灵巧、通用的机器人控制。
- **[GigaBrain-0: A World Model-Powered Vision-Language-Action Model](https://arxiv.org/abs/2510.19430)** (2025) — VLA 训练大量依赖世界模型生成的数据（真实视频重渲染、新视角、仿真转真实、人类视频转机器人）；论文报告在灵巧与移动操作任务上优于 π0，并提供可在 Jetson Orin 上运行的 4.02 亿参数小模型。 · [代码](https://github.com/open-gigaai/giga-brain-0) · [项目页](https://gigabrain0.github.io)
- **[GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data](https://arxiv.org/abs/2505.03233)** (2025) — 几乎只用十亿帧级的照片级仿真抓取数据集 SynGrasp-1B（并联合网络语义数据）预训练抓取 VLA；论文报告可零样本从仿真迁移到真实开放词汇抓取，并支持少样本适配。 · [代码](https://github.com/PKU-EPIC/GraspVLA)
- **[HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation](https://arxiv.org/abs/2502.05485)** (2025) — 分层 VLA：微调后的 VLM 在图像上画出末端执行器的粗略二维路径，再由底层三维策略跟随执行；因此 VLM 可以用仿真、视频等低成本的非本域数据训练。 · [项目页](https://hamster-robo.github.io/)
- **[Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2502.19417)** (2025) — 高层 VLM 理解开放式指令与执行中的纠正，并将其转化为简短语言指令交给底层 π0 策略执行。
- **[Hume: Introducing System-2 Thinking in Visual-Language-Action Model](https://arxiv.org/abs/2505.21432)** (2025) — 双系统 VLA：价值查询头对多组候选动作块打分并择优（System 2，约 4 Hz），轻量级级联去噪策略再将其细化为流畅动作（System 1，约 90 Hz）；论文报告在 LIBERO、SIMPLER 和真机上均优于 π0。 · [项目页](https://hume-vla.github.io)
- **[Igniting VLMs toward the Embodied Space](https://arxiv.org/abs/2509.11766)** (2025) — WALL-OSS：开源具身基础模型，在同一可微模型中串联指令推理、子目标分解与细粒度动作生成（"统一跨层级思维链"）；训练代码与模型权重已开源。 · [代码](https://github.com/X-Square-Robot/wall-x)
- **[InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy](https://arxiv.org/abs/2510.13778)** (2025) — 先在 230 万条空间推理样本上做空间定位预训练（"在哪里做"），再用空间提示做动作后训练（"怎么做"）；论文报告在 SimplerEnv Google Robot 上比无空间引导的同一模型高 14.6%。 · [代码](https://github.com/InternRobotics/InternVLA-M1)
- **[Magma: A Foundation Model for Multimodal AI Agents](https://arxiv.org/abs/2502.13130)** (2025) — 同一个模型同时做界面操作与机器人操作：在图像、视频和机器人数据上预训练，用 Set-of-Mark 标注可操作对象、用 Trace-of-Mark 标注运动轨迹；模型与代码公开。 · [代码](https://github.com/microsoft/Magma) · [项目页](https://microsoft.github.io/Magma)
- **[MolmoAct: Action Reasoning Models that can Reason in Space](https://arxiv.org/abs/2508.07917)** (2025) — 开源 7B VLA，先输出深度感知 token，再生成可编辑的二维轨迹，最后输出动作；论文报告 SimplerEnv 零样本 70.5%、LIBERO 86.6%，并开放权重、代码和数据。 · [代码](https://github.com/allenai/molmoact) · [项目页](https://allenai.org/blog/molmoact)
- **[OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning](https://arxiv.org/abs/2505.11917)** (2025) — 单一模型自主决定何时“想”、何时“做”：在子任务完成、出错或人类插话等关键时刻进行推理，其余时间依据最新推理结果生成动作；并与合成的推理型视觉-语言数据共同训练。 · [代码](https://github.com/Fanqi-Lin/OneTwoVLA) · [项目页](https://one-two-vla.github.io)
- **[RoboBrain 2.0 Technical Report](https://arxiv.org/abs/2507.02029)** (2025) — 开源具身视觉语言模型（7B 与 32B），面向空间定位、可供性、轨迹预测与多步任务规划，作为底层策略之上的“大脑”。 · [代码](https://github.com/FlagOpen/RoboBrain2.0)
- **[RoboOS: A Hierarchical Embodied Framework for Cross-Embodiment and Multi-Agent Collaboration](https://arxiv.org/abs/2505.03673)** (2025) — 开源的“大脑–小脑”分层系统：RoboBrain 多模态大模型负责跨异构机器人的任务规划与分配，各机器人上的技能库负责执行，共享的空间/时间/本体记忆保持多机协同。 · [代码](https://github.com/FlagOpen/RoboOS)
- **[SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://arxiv.org/abs/2506.01844)** (2025) — 约 4.5 亿参数的 VLA，用社区 LeRobot 数据训练，可在消费级 GPU 上运行。 · [代码](https://github.com/huggingface/lerobot)
- **[SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model](https://arxiv.org/abs/2501.15830)** (2025) — 为视觉 token 加入 3D 位置编码，并用自适应动作网格表示动作，在 110 万条真机轨迹上预训练；迁移到新机器人时只需重新划分动作网格。 · [代码](https://github.com/SpatialVLA/SpatialVLA)
- **[TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models](https://arxiv.org/abs/2511.05275)** (2025) — 不做双臂预训练，而是把两份预训练单臂 VLA 组合成协同的双臂 VLA；论文报告在真实与仿真双臂任务上优于同规模 RDT-1B，并缩小了与依赖大量双臂数据的 π0 的差距。 · [代码](https://github.com/jellyho/TwinVLA) · [项目页](https://jellyho.github.io/TwinVLA/)
- **[UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](https://arxiv.org/abs/2505.06111)** (2025) — 在 DINO 特征空间中、借助语言指令过滤，从视频里学习“任务相关”的隐动作，使策略可跨机器人与人类视频预训练；报告以少得多的预训练算力超过 OpenVLA。 · [代码](https://github.com/OpenDriveLab/UniVLA)
- **[VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers](https://arxiv.org/abs/2507.01016)** (2025) — 用卷积残差 VQ-VAE 动作分词器（以百倍规模的真实+合成数据训练）替换 OpenVLA 的逐维离散分箱；论文报告 LIBERO-90 和真实 Franka 任务成功率提升，推理速度约快 2.8 倍。 · [代码](https://github.com/xiaoxiao0406/VQ-VLA)
- **[X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model](https://arxiv.org/abs/2510.10274)** (2025) — 为每个数据来源配一组可学习的软提示嵌入，使一个基于标准 Transformer 的流匹配策略（0.9B）能跨本体联合训练；在 6 个仿真基准和 3 台真实机器人上评测。 · [代码](https://github.com/2toinf/X-VLA) · [项目页](https://thu-air-dream.github.io/X-VLA/)
- **[3D-VLA: A 3D Vision-Language-Action Generative World Model](https://arxiv.org/abs/2403.09631)** (2024) — 具备三维感知的大语言模型，引入场景、物体与动作交互 token，并与扩散模型对齐，可在规划动作前“想象”目标图像和点云；训练数据为作者整理的约 200 万条三维-语言-动作样本。 · [代码](https://github.com/UMass-Embodied-AGI/3D-VLA) · [项目页](https://vis-www.cs.umass.edu/3dvla)
- **[A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093)** (2024) — 较早的 VLA 综述：把相关工作分为组件研究（视觉、语言、世界模型等）、底层控制策略与高层任务规划器，并汇总数据集、仿真器与基准；附配套论文列表。 · [项目页](https://github.com/yueen-ma/Awesome-VLA)
- **[Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI](https://arxiv.org/abs/2407.06886)** (2024) — 覆盖面很广的具身智能综述：机器人本体、仿真器、具身感知、交互、具身智能体与 sim-to-real，并讨论多模态大模型与世界模型的作用；配套中山大学 HCPLab 维护的常用论文列表。 · [项目页](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List)
- **[CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation](https://arxiv.org/abs/2411.19650)** (2024) — 不再让 VLM 直接输出动作 token，而是用独立的扩散动作 Transformer 以 VLM 的“认知”特征为条件生成动作；报告在仿真和真机上明显优于 OpenVLA。 · [代码](https://github.com/microsoft/CogACT)
- **[GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation](https://arxiv.org/abs/2410.06158)** (2024) — 先在 3800 万段视频上预训练未来帧生成，再在机器人数据上微调，同时预测视频帧与动作轨迹；报告在 100 多个真机桌面任务上平均成功率 97.7%，在未见场景中成功率约为 GR-1 的两倍。 · [项目页](https://gr2-manipulation.github.io)
- **[Latent Action Pretraining from Videos](https://arxiv.org/abs/2410.11758)** (2024) — LAPA 无需动作标注即可预训练 VLA：先从视频相邻帧间学习离散隐动作，再训练模型由图像和指令预测隐动作，最后用少量机器人数据映射到真实动作；报告在真机任务上优于 OpenVLA。 · [代码](https://github.com/LatentActionPretraining/LAPA) · [项目页](https://latentactionpretraining.github.io/)
- **[Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213)** (2024) — 在 Open X-Embodiment 上预训练的开源扩散头 Transformer 策略，可快速微调到新机器人和新传感器。 · [代码](https://github.com/octo-models/octo)
- **[RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](https://arxiv.org/abs/2410.07864)** (2024) — 12 亿参数扩散 Transformer，采用跨机器人统一动作空间，面向双臂操作。 · [代码](https://github.com/thu-ml/RoboticsDiffusionTransformer)
- **[Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers](https://arxiv.org/abs/2409.20537)** (2024) — HPT：为每种机器人设计“输入头”，把本体感知与视觉映射成短 token 序列，送入共享的 Transformer 主干；在 52 个数据集（真机、仿真、人类视频）上预训练，报告在未见任务上微调提升 20% 以上。 · [代码](https://github.com/liruiw/HPT) · [项目页](https://liruiw.github.io/hpt/)
- **[TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2409.12514)** (2024) — 由小型多模态模型（至多 1.4B）加 LoRA 微调与扩散策略头构成的紧凑 VLA，无需大规模机器人预训练；报告真机成功率高于 OpenVLA，推理速度约快 20 倍。 · [项目页](https://tiny-vla.github.io/)
- **[TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://arxiv.org/abs/2412.10345)** (2024) — 把机器人近期的运动轨迹画在输入图像上（“视觉轨迹提示”），并在 15 万条轨迹上微调 OpenVLA；报告在 SimplerEnv 上提升约 10%、真实 WidowX 任务上提升 3.5 倍，另有基于 Phi-3-Vision 的 4B 精简版。 · [代码](https://github.com/umd-huang-lab/tracevla) · [项目页](https://tracevla.github.io/)
- **[Foundation Models in Robotics: Applications, Challenges, and the Future](https://arxiv.org/abs/2312.07843)** (2023) — 综述预训练基础模型如何用于机器人的感知、决策与控制，以及主要瓶颈：机器人数据稀缺、安全性与不确定性量化、实时执行。 · [项目页](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models)
- **[PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378)** (2023) — 将连续传感器嵌入注入 5620 亿参数语言模型，用于具身推理与规划。
- **[A Generalist Agent](https://arxiv.org/abs/2205.06175)** (2022) — Gato：同一套权重的 Transformer 既能玩游戏、写图像描述，也能用真实机械臂堆积木。
- **[RT-1: Robotics Transformer for Real-World Control at Scale](https://arxiv.org/abs/2212.06817)** (2022) — 将动作离散化为 token，用 13 万条真实演示训练 Transformer，证明机器人策略会随数据多样性扩展。 · [代码](https://github.com/google-research/robotics_transformer)
- **[VIMA: General Robot Manipulation with Multimodal Prompts](https://arxiv.org/abs/2210.03094)** (2022) — 把多种桌面任务统一成图文交错的提示，交给一个 Transformer 策略执行，并配套 VIMA-Bench 用于系统性泛化评测。 · [代码](https://github.com/vimalabs/VIMA)
- _另见:_ [HexaShell](#manipulation), [CLIPort](#manipulation), [Perceiver-Actor](#manipulation), [ReKep](#manipulation), [From VLM Planners to Robotic Agents](#manipulation), [DexGraspVLA](#manipulation), [WorldVLA](#world-models), [UniFlowWAM](#world-models), [GreenWAM](#world-models), [RynnUnify](#world-models), [Cracking Mobile Manipulation](#navigation), [Uni-NaVid](#navigation), [NaVILA](#navigation), [LM-Nav](#navigation), [DINOv2](#perception), [ACE-Brain-0.6](#perception), [SimpleVLA-RL](#learning), [RLinf-VLA](#learning), [ACCRUE](#learning), [AgenticRoboRL](#learning), [TILDE](#learning), [EgoForesight](#learning), [Open X-Embodiment](#datasets), [Evaluating Real-World Robot Manipulation Policies in Simulation](#datasets), [Embodied Skill Bench](#datasets), [RoboCasa-Shift](#datasets), [VLABench](#datasets)

<a id="manipulation"></a>
### 操作与灵巧手

_模仿学习、扩散策略、抓取、双臂与灵巧操作。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/manipulation.html)

- ⭐ **[Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](https://arxiv.org/abs/2402.10329)** (2024) — 手持夹爪加 GoPro 可随处采集演示，训练出的策略可直接迁移到机械臂。 · [代码](https://github.com/real-stanford/universal_manipulation_interface)
- ⭐ **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** (2023) — 以去噪方式生成动作序列，比回归更能处理多模态演示，已成为模仿学习标准基线。 · [代码](https://github.com/real-stanford/diffusion_policy)
- ⭐ **[Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705)** (2023) — ALOHA + ACT：约 2 万美元的双臂遥操作平台，加上动作分块 Transformer，约 50 条演示即可学会精细任务。 · [代码](https://github.com/tonyzhaozh/act)
- **[Beyond the End-Effector: Learning Whole-Arm Contact Manipulation from Human Demonstrations](https://arxiv.org/abs/2610.17802)** (2026) — WACL 从人类示范中学习用整条手臂推、抵物体，自主选择手臂上的接触位置，同时满足末端执行器的约束。 · [项目页](https://wacl-robot.github.io)
- **[Blind Precise Assembly: Proprioceptive Sim-to-Real Peg-in-Hole for Diverse Parts](https://arxiv.org/abs/2610.23849)** (2026) — 探究仅靠关节读数能否完成毫米级精密插装：训练不用相机、力或触觉输入的 sim-to-real 策略。
- **[COWBOY: A Scalable Sim-to-Real Framework for Learning Contextual Whole-Body Manipulation](https://arxiv.org/abs/2610.28948)** (2026) — 在仿真中学习移动灵巧抓取：全身控制器负责底盘-手臂协同到达与主动视觉，局部强化学习专家负责物体交互，二者蒸馏成一个基于点云的视觉策略；报告可零样本迁移到真实世界的数百个物体与场景。 · [项目页](https://cowboy-manip.com)
- **[Can a Frontier VLM Serve as a Robot Policy for Memory-Dependent Manipulation?](https://arxiv.org/abs/2610.17350)** (2026) — 冻结的前沿 VLM 以整段回合为上下文直接输出路径点，在 RoboMME 记忆类任务上报告 92.1% 成功率，且无需任务训练。 · [代码](https://github.com/jackbjed/embodied-astra-robomme) · [项目页](https://embodied-astra.github.io)
- **[ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2610.24512)** (2026) — 围绕八种日常接触技能设计的 36 个接触密集型任务，40 多个物体可用消费级 3D 打印机复现，且每个都有对应仿真模型。报告称所测的视触觉策略并未明显优于纯视觉策略。 · [项目页](https://jingyi-xiang.github.io/contactbench)
- **[DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations](https://arxiv.org/abs/2610.29997)** (2026) — 用一个双手跟踪策略（PPO 结合对自身成功执行的行为克隆）复现重定向后的人手-物体交互动作，并发布 BiHOI 数据集（1575 段双手序列、229 个物体）。论文报告在未见轨迹上成功率 86.8%、新物体上 57.3%。 · [代码](https://github.com/Ropedia/DONIC)
- **[FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation](https://arxiv.org/abs/2610.31841)** (2026) — 同时读取腕部力/力矩与图像的编程智能体：编写接触探测与力反馈控制程序，并在每次执行后依据力记录诊断失败、修改代码；无需示教或训练。在 5 个真实任务上优于仅视觉版本。 · [项目页](https://tanoom.github.io/forca/)
- **[From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation](https://arxiv.org/abs/2610.29560)** (2026) — SERA 把高层 VLM 规划器做成带可编辑执行框架的智能体，为固定的底层 VLA 记录任务进度与执行反馈，并利用环境回放自动改进框架；报告在 RoboMME 上总体成功率 51.4%，未自我演化时为 44.4%。 · [代码](https://github.com/StevenKKXS/SERA) · [项目页](https://stevenkkxs.github.io/sera-webpage/)
- **[HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents](https://arxiv.org/abs/2610.23479)** (2026) — 编程智能体通过一条命令行驱动双臂机器人；每次失败后读取日志，编写或修复可复用的小工具程序。 · [代码](https://github.com/HexaFuture/HexaShell)
- **[Learn the Task, Not the Schedule: Reducing Spurious Cross-Arm Coupling in Bimanual Imitation Learning](https://arxiv.org/abs/2610.26507)** (2026) — CTR 在训练时对双臂示教中两只手臂的动作时序重新组合，同时保留任务必需的约束，避免策略把另一只手臂的进度当作捷径线索。
- **[MoDex: Towards Universal Multi-Object Dexterous Grasping](https://arxiv.org/abs/2610.23888)** (2026) — 让灵巧手一次抓取多个物体：学习对参考轨迹的单步残差修正，并根据物体的空间布局调整抓取策略。 · [代码](https://github.com/Aurora-Xiong/MoDex)
- **[DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping](https://arxiv.org/abs/2502.20900)** (2025) — 由预训练 VLM 做高层规划、扩散控制器驱动灵巧手抓取，底层输入为基础模型提取的域不变特征；报告在数千个未见过的杂乱场景中抓取成功率超过 90%。 · [代码](https://github.com/Psi-Robot/DexGraspVLA) · [项目页](https://dexgraspvla.github.io)
- **[3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations](https://arxiv.org/abs/2403.03954)** (2024) — 用紧凑点云编码作为扩散策略条件，比图像输入更省数据、对视角更鲁棒。 · [代码](https://github.com/YanjieZe/3D-Diffusion-Policy)
- **[DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation](https://arxiv.org/abs/2403.07788)** (2024) — 可穿戴动捕手套与相机采集人手动作，重定向后用于训练灵巧机器人手。
- **[EgoMimic: Scaling Imitation Learning via Egocentric Video](https://arxiv.org/abs/2410.24221)** (2024) — 把佩戴 Project Aria 眼镜采集、带三维手部跟踪的第一视角人类视频当作机器人数据，与机器人数据共同训练同一个策略；论文报告多 1 小时人手数据比多 1 小时机器人数据更有用。 · [代码](https://github.com/SimarKareer/EgoMimic) · [项目页](https://egomimic.github.io/)
- **[Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation](https://arxiv.org/abs/2401.02117)** (2024) — 将 ALOHA 装上移动底盘；与静态 ALOHA 数据联合训练显著提升做饭、开柜等移动任务表现。 · [代码](https://github.com/MarkFzp/mobile-aloha)
- **[Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation](https://arxiv.org/abs/2412.15109)** (2024) — Seer 先预测未来视觉状态，再由逆动力学模型据此输出动作，端到端训练并在 DROID 上预训练；报告 CALVIN ABC-D 平均任务长度 4.28，在 LIBERO-LONG 和真机任务上也有提升。 · [代码](https://github.com/OpenRobotLab/Seer) · [项目页](https://nimolty.github.io/Seer/)
- **[ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](https://arxiv.org/abs/2409.01652)** (2024) — ReKep：由视觉语言模型把操作任务写成定义在三维关键点上的 Python 代价函数（关系关键点约束），再由分层优化器实时求解；零样本，无需针对任务训练。 · [代码](https://github.com/huangwl18/ReKep)
- **[On Bringing Robots Home](https://arxiv.org/abs/2311.16098)** (2023) — Dobb-E 用低成本的手持夹取“棒”采集家庭示范数据并预训练，在新家庭任务上只需几分钟数据即可适配。 · [代码](https://github.com/notmahi/dobb-e)
- **[RVT: Robotic View Transformer for 3D Object Manipulation](https://arxiv.org/abs/2306.14896)** (2023) — RVT：把点云重新渲染为若干虚拟视角，再用多视角 Transformer 预测关键帧位姿；论文报告在 RLBench 上训练与推理都比基于体素的 PerAct 快得多。代码库同时包含 RVT-2。 · [代码](https://github.com/NVlabs/RVT)
- **[VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://arxiv.org/abs/2307.05973)** (2023) — 大模型编写代码组合 3D 可供性/约束地图，再由规划器生成轨迹，无需机器人训练。
- **[AnyGrasp: Robust and Efficient Grasp Perception in Spatial and Temporal Domains](https://arxiv.org/abs/2212.08333)** (2022) — AnyGrasp：基于真实传感器数据与解析标注训练、考虑物体质心的稠密 7 自由度平行夹爪抓取检测，并能跨帧跟踪抓取以应对运动物体；以 SDK 形式发布。 · [代码](https://github.com/graspnet/anygrasp_sdk)
- **[DexGraspNet: A Large-Scale Robotic Dexterous Grasp Dataset for General Objects Based on Simulation](https://arxiv.org/abs/2210.02697)** (2022) — 通过优化可微的力封闭能量合成、并经物理仿真验证的百万级 ShadowHand 抓取，覆盖数千个物体，是灵巧抓取模型的常用训练集。 · [代码](https://github.com/PKU-EPIC/DexGraspNet)
- **[Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation](https://arxiv.org/abs/2209.05451)** (2022) — PerAct：在体素化的 RGB-D 观测上运行 Perceiver Transformer，把下一关键帧夹爪位姿当作体素分类来预测；一个语言条件策略即可覆盖众多 RLBench 与真机任务。 · [代码](https://github.com/peract/peract)
- **[R3M: A Universal Visual Representation for Robot Manipulation](https://arxiv.org/abs/2203.12601)** (2022) — 在 Ego4D 人类视频上预训练视觉编码器，显著提高下游模仿学习的数据效率。
- **[Visual Dexterity: In-Hand Reorientation of Novel and Complex Object Shapes](https://arxiv.org/abs/2211.11744)** (2022) — 仅凭深度相机即可在手中翻转未见过的物体，策略在仿真中训练。
- **[CLIPort: What and Where Pathways for Robotic Manipulation](https://arxiv.org/abs/2109.12098)** (2021) — CLIPort：把 CLIP 提供的语义"是什么"通路与 Transporter 的空间"在哪里"通路结合，实现语言条件的桌面操作；是较早把网络视觉语言模型接入机器人动作的工作。 · [代码](https://github.com/cliport/cliport)
- **[Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes](https://arxiv.org/abs/2103.14127)** (2021) — Contact-GraspNet：从单帧深度图为整个杂乱场景预测 6 自由度平行夹爪抓取；把观测到的点当作抓取接触点，使每个点只需学习 4 个自由度。 · [代码](https://github.com/NVlabs/contact_graspnet)
- **[Transporter Networks: Rearranging the Visual World for Robotic Manipulation](https://arxiv.org/abs/2010.14406)** (2020) — Transporter 网络：把抓取-放置建模为以抓取点为中心的深度特征的空间匹配，在重排类任务上样本效率很高，并随论文发布 Ravens 基准。 · [代码](https://github.com/google-research/ravens)
- **[Solving Rubik's Cube with a Robot Hand](https://arxiv.org/abs/1910.07113)** (2019) — 自动域随机化让仿真训练的灵巧手策略在真实硬件上操作魔方。
- **[Learning Dexterous In-Hand Manipulation](https://arxiv.org/abs/1808.00177)** (2018) — 完全在随机化仿真中用强化学习训练，Shadow 灵巧手在真实世界翻转方块，是 sim-to-real 里程碑。
- _另见:_ [Has GPT-6-Astra Achieved Embodied Intelligence?](#vla), [CarryOn](#vla), [GraspVLA](#vla), [Being-H0](#vla), [HAMSTER](#vla), [From Reasoning to Action](#vla), [FastHarness](#vla), [3D-ViTac](#tactile), [Making Sense of Vision and Touch](#tactile), [See, Hear, and Feel](#tactile), [General In-Hand Object Rotation with Vision and Touch](#tactile), [Rotating without Seeing](#tactile), [Robot Synesthesia](#tactile), [Neural feels with neural fields](#tactile), [Reactive Diffusion Policy](#tactile), [Tactile-Based Robotic Manipulation](#tactile), [$λ_0$](#locomotion), [Solving a Giant Rubik's Cube with a Quadruped Robot](#locomotion), [CW-WAM](#world-models), [Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](#world-models), [Video Prediction Policy](#world-models), [Unified Video Action Model](#world-models), [Genie Envisioner](#world-models), [Agentic World Action Models](#world-models), [Code as Policies](#navigation), [OK-Robot](#navigation), [Cracking Mobile Manipulation](#navigation), [Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance](#navigation), [FoundationPose](#perception), [BundleSDF](#perception), [ACE-Brain-0.6](#perception), [cuRobo](#control), [Motion Policy Networks](#control), [Sub-Millisecond Reflexes for Continuous Physical Human-Robot Interaction](#control), [MoveIt 2](#control), [Motions in Microseconds via Vectorized Sampling-Based Planning](#control), [Jerk-limited Real-time Trajectory Generation with Arbitrary Target States](#control), [SERL](#learning), [Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](#learning), [What Matters in Learning from Offline Human Demonstrations for Robot Manipulation](#learning), [Diffusion Policy Policy Optimization](#learning), [QT-Opt](#learning), [Steering Your Diffusion Policy with Latent Space Reinforcement Learning](#learning), [Q-Transformer](#learning), [Learning from Fleet Experience](#learning), [ACCRUE](#learning), [RoboTwin 2.0](#sim), [MimicGen](#sim), [Habitat 2.0](#sim), [SoftGym](#sim), [DexMimicGen](#sim), [GenManip](#sim), [LeRobot](#datasets), [THE COLOSSEUM](#datasets), [DexYCB](#datasets), [Benchmarking in Manipulation Research](#datasets), [HOI4D](#datasets), [OakInk](#datasets), [ARCTIC](#datasets), [VLABench](#datasets), [EgoExplorer](#datasets), [HandsOn](#datasets), [RoboValue](#datasets), [LIBERO-Industry](#datasets), [EgoDex](#datasets), [BiDex-100](#datasets), [AstroBench](#datasets), [LEAP Hand](#hardware), [BEHAVIOR Robot Suite](#hardware), [ALOHA 2](#hardware), [ORCA](#hardware), [AnyTeleop](#hardware), [AirExo](#hardware), [AirExo-2](#hardware), [Bunny-VisionPro](#hardware), [TeleMoMa](#hardware), [DexUMI](#hardware), [Learning Visuotactile Skills with Two Multifingered Hands](#hardware), [OpenArm](#hardware), [TidyBot++](#hardware), [UMI-on-Legs](#hardware), [DOGlove](#hardware), [RUKA](#hardware), [Bimanual Dexterity for Complex Tasks](#hardware), [DexPort](#hardware), [PHD-Hand](#hardware)

<a id="tactile"></a>
### 触觉与视触觉感知

_触觉传感器、触觉表征与接触丰富的控制。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/tactile.html)

- ⭐ **[DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](https://arxiv.org/abs/2005.14679)** (2020) — 低成本、紧凑的 GelSight 式指尖传感器，让视触觉传感器得以普及。 · [代码](https://github.com/facebookresearch/digit-interface)
- **[GelSlim 5.0: Unifying Vision and Touch with a Single Fingertip Camera](https://arxiv.org/abs/2610.31334)** (2026) — 指尖传感器只用一个摄像头，通过切换照明交替获取“透过膜的视觉图像”和触觉图像，视觉与触觉共享同一视角、无需相机外参标定；再用 Transformer（VisTacFusion）融合两者。
- **[OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing](https://arxiv.org/abs/2610.31661)** (2026) — 开源电阻式触觉皮肤：结构化覆层把切向力转成空间压力差异，相邻触点即可解码剪切与法向力；附带可定制皮肤的设计工具，硬件和软件均开源。 · [项目页](https://opentac.github.io)
- **[Tactile-Based Robotic Manipulation: From Mechanics-Driven to Data-Driven Perspectives](https://arxiv.org/abs/2610.30438)** (2026) — 综述（Annual Review of Control, Robotics, and Autonomous Systems 录用稿）：从接触力学建模到数据驱动学习，梳理触觉操作的发展，涵盖传感基础、状态表征、模仿学习、强化学习、VLA 与预测模型。
- **[VecTile: A Low-Cost Flexible Tactile Array for 3-DoF Force Sensing](https://arxiv.org/abs/2610.31472)** (2026) — 6 毫米厚的柔性触觉阵列：压阻层上的硅胶凸点把切向力转成可区分的压力分布，实现每个触点的三轴力测量；4x4 阵列成本不到 35 美元。报告称其提升了扩散策略插插头任务的表现。 · [项目页](https://jiannnh.github.io/VecTile/)
- **[Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](https://arxiv.org/abs/2503.02881)** (2025) — 慢速扩散策略在隐空间规划动作块，快速策略根据触觉/力反馈高频调整；论文报告在三个接触丰富任务上比纯视觉模仿学习基线总分高 35% 以上。 · [代码](https://github.com/xiaoxiaoxh/reactive_diffusion_policy) · [项目页](https://reactive-diffusion-policy.github.io/)
- **[3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing](https://arxiv.org/abs/2410.24091)** (2024) — 在扩散策略中融合密集触觉阵列与 3D 视觉，完成易碎、接触丰富的双臂任务。
- **[A Touch, Vision, and Language Dataset for Multimodal Alignment](https://arxiv.org/abs/2402.13232)** (2024) — TVL 数据集将触觉与视觉观测配上语言描述，并训练触觉-视觉-语言编码器以及能描述物体触感的模型。 · [代码](https://github.com/Max-Fu/tvl)
- **[AnySkin: Plug-and-play Skin Sensing for Robotic Touch](https://arxiv.org/abs/2409.08276)** (2024) — 可更换的磁性触觉皮肤，更换皮肤后训练好的策略仍能继续使用。
- **[Binding Touch to Everything: Learning Unified Multimodal Tactile Representations](https://arxiv.org/abs/2401.18084)** (2024) — UniTouch 将触觉信号与视觉、语言、音频嵌入对齐，实现零样本触觉理解。
- **[Digitizing Touch with an Artificial Multimodal Fingertip](https://arxiv.org/abs/2411.02479)** (2024) — Digit 360：开放设计的指尖形触觉传感器，可感知力、细微纹理、振动和温度，并用板载神经网络加速器做类似反射弧的本地处理。 · [代码](https://github.com/facebookresearch/digit360)
- **[Sparsh: Self-supervised touch representations for vision-based tactile sensing](https://arxiv.org/abs/2410.24090)** (2024) — 在大量触觉图像上自监督预训练的编码器，可跨不同视触觉传感器使用。 · [代码](https://github.com/facebookresearch/sparsh)
- **[TacSL: A Library for Visuotactile Sensor Simulation and Learning](https://arxiv.org/abs/2408.06506)** (2024) — 在 Isaac Gym 中用 GPU 模拟 GelSight 式触觉图像与接触力，并提供用于视触觉策略仿真到真实迁移的学习工具。
- **[9DTact: A Compact Vision-Based Tactile Sensor for Accurate 3D Shape Reconstruction and Generalizable 6D Force Estimation](https://arxiv.org/abs/2308.14277)** (2023) — DTact 的后续：紧凑的开源视觉触觉传感器，可重建三维接触形状，并用可泛化到新物体的模型估计六维力/力矩。 · [代码](https://github.com/linchangyi1/9DTact)
- **[General In-Hand Object Rotation with Vision and Touch](https://arxiv.org/abs/2309.09979)** (2023) — RotateIt 先在仿真中利用特权物体信息训练，再蒸馏为仅用视觉、触觉和本体感觉的策略，在真实灵巧手上旋转多种物体。
- **[Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation](https://arxiv.org/abs/2312.13469)** (2023) — NeuralFeels 将多指手的视觉与触觉在线融合为神经场，在操作过程中同时重建物体形状并跟踪其位姿。 · [代码](https://github.com/facebookresearch/neuralfeels)
- **[Robot Synesthesia: In-Hand Manipulation with Visuotactile Sensing](https://arxiv.org/abs/2312.01853)** (2023) — 将触觉读数转换为与相机点云、手部模型处于同一三维坐标系的点，用统一的视触觉点云输入驱动手内物体旋转。 · [项目页](https://yingyuan0414.github.io/visuotactile/)
- **[Rotating without Seeing: Towards In-hand Dexterity through Touch](https://arxiv.org/abs/2303.10880)** (2023) — 在灵巧手上铺设廉价的二值（有/无接触）触觉传感器，在仿真中用强化学习训练策略，迁移到真机后无需视觉即可在手中旋转未见过的物体。 · [项目页](https://touchdexterity.github.io)
- **[DTact: A Vision-Based Tactile Sensor that Measures High-Resolution 3D Geometry Directly from Darkness](https://arxiv.org/abs/2209.13916)** (2022) — 低成本视觉触觉传感器：根据凝胶受压时每个像素变暗的程度直接读出接触深度，无需光度立体即可获得高分辨率三维形状。
- **[See, Hear, and Feel: Smart Sensory Fusion for Robotic Manipulation](https://arxiv.org/abs/2212.03858)** (2022) — 在模仿学习策略中用自注意力融合相机、接触麦克风和 GelSight 触觉，在密集装箱与倾倒任务上做了研究。 · [代码](https://github.com/JunzheJosephZhu/see_hear_feel)
- **[Tactile Gym 2.0: Sim-to-real Deep Reinforcement Learning for Comparing Low-cost High-Resolution Robot Touch](https://arxiv.org/abs/2207.10763)** (2022) — 开源触觉强化学习环境，支持三种低成本光学触觉传感器（TacTip、DIGIT、DigiTac）的仿真到真机迁移，便于在相同任务上比较。 · [代码](https://github.com/dexterousrobot/tactile_gym)
- **[Touch and Go: Learning from Human-Collected Vision and Touch](https://arxiv.org/abs/2211.12498)** (2022) — 由人手持 GelSight 在真实场景中触碰物体采集的视觉-触觉配对数据集，用于跨模态触觉学习。
- **[GelSlim 3.0: High-Resolution Measurement of Shape, Force and Slip in a Compact Tactile-Sensing Finger](https://arxiv.org/abs/2103.12269)** (2021) — 纤薄的 GelSight 类触觉手指，可高分辨率测量接触形状、力与滑移，便于装在机器人夹爪上。
- **[ReSkin: versatile, replaceable, lasting tactile skins](https://arxiv.org/abs/2111.00071)** (2021) — 由磁力计读取的薄磁性弹性体皮肤，制作和更换成本低，学习得到的标定可迁移到新皮肤上。 · [代码](https://github.com/raunaqbhirangi/reskin_sensor)
- **[Taxim: An Example-based Simulation Model for GelSight Tactile Sensors](https://arxiv.org/abs/2109.04027)** (2021) — 用标定样本（光学查找表 + 线弹性形变）而不是基于物理的渲染来模拟 GelSight 图像，可快速生成触觉数据。 · [代码](https://github.com/Robo-Touch/Taxim)
- **[TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors](https://arxiv.org/abs/2012.08456)** (2020) — 在仿真中渲染 DIGIT/GelSight 式触觉图像，便于大规模训练基于触觉的策略。 · [代码](https://github.com/facebookresearch/tacto)
- **[Making Sense of Vision and Touch: Self-Supervised Learning of Multimodal Representations for Contact-Rich Tasks](https://arxiv.org/abs/1810.10191)** (2018) — 用自监督目标学习视觉 + 力/力矩的紧凑联合表征，再在其上用强化学习在真实机器人上训练插孔策略。 · [代码](https://github.com/stanford-iprl-lab/multimodal_representation)
- _另见:_ [FORCA](#manipulation), [ContactBench 1.0](#manipulation), [Physical Canvas](#world-models), [EgoExplorer](#datasets), [ORCA](#hardware), [Learning Visuotactile Skills with Two Multifingered Hands](#hardware), [DOGlove](#hardware)

<a id="locomotion"></a>
### 运动控制与人形机器人

_足式运动、人形全身控制与跑酷。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/locomotion.html)

- ⭐ **[BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](https://arxiv.org/abs/2508.08241)** (2025) — 用同一套超参数的运动跟踪方案学会侧手翻、飞踢、冲刺等敏捷技能，再用带引导的潜空间扩散模型组合这些技能以完成摇杆遥控、避障等新目标，零样本迁移到真机。 · [代码](https://github.com/HybridRobotics/whole_body_tracking)
- ⭐ **[Real-World Humanoid Locomotion with Reinforcement Learning](https://arxiv.org/abs/2303.03381)** (2023) — 在仿真中训练的因果 Transformer 策略零样本驱动全尺寸人形机器人在户外行走。
- ⭐ **[Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](https://arxiv.org/abs/2109.11978)** (2021) — 数千个 GPU 并行环境几分钟就能训练出四足行走策略；legged_gym 成为标准入门框架。 · [代码](https://github.com/leggedrobotics/legged_gym)
- **[$λ_0$: Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.18950)** (2026) — 构建 500 小时的第一视角人类数据集 HumanVerse（含同步的身体与手部动作），对齐到 Unitree G1 后用于人形基础模型 λ0 的中期训练；论文报告 SIMPLE 上成功率 90%、真实移动操作任务 62.5%，人类数据越多下游表现越好。 · [代码](https://github.com/LambdaHumanoid/openlambda) · [项目页](https://lambdahumanoid.github.io/)
- **[Solving a Giant Rubik's Cube with a Quadruped Robot](https://arxiv.org/abs/2610.24610)** (2026) — 四足机器人只用脚完成巨型魔方：机载 RGB-D 估计魔方位姿与颜色状态，规划器把解法转成技能序列，强化学习训练的全身技能负责翻转魔方、一脚固定一脚推动转层。报告完成三次完全自主求解。 · [项目页](https://leggedrobotics.github.io/rubik-skills/)
- **[SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](https://arxiv.org/abs/2610.28480)** (2026) — SuperMimic 不再蒸馏逐动作专家或用大算力硬训单一 RL 策略，而是把人形机器人动作跟踪策略与一个从仿真日志拟合的、共享动力学的可微世界模型联合训练（CoRL 2026 口头报告）。 · [项目页](https://supermimic.github.io)
- **[ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback](https://arxiv.org/abs/2610.32966)** (2026) — 跳过人体重建与重定向：扩散模型直接把单目人类视频生成为人形机器人参考动作，并以运动跟踪结果做 DPO 后训练；自回归版本可在 Unitree G1 上实现低于 400 ms 延迟的实时视频遥操作。 · [项目页](https://awfuact.github.io/vit-h/)
- **[Watch Your Step: Anticipated Perception for Humanoid Locomotion](https://arxiv.org/abs/2610.29612)** (2026) — 不再把整张高程图输入人形机器人运动策略，而是先用轻量的落脚点预测模型去掉与接下来几步无关的地形信息，以加快训练并提升对新地形的泛化。 · [项目页](https://leggedrobotics.github.io/watch-your-step)
- **[ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](https://arxiv.org/abs/2502.01143)** (2025) — 从真实轨迹学习残差"增量动作"模型来修正仿真物理，实现敏捷的人形运动技能。 · [代码](https://github.com/LeCAR-Lab/ASAP)
- **[Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion](https://arxiv.org/abs/2401.17583)** (2024) — ABS 将敏捷的强化学习运动策略与学习的可达-规避价值网络及恢复策略结合，接近障碍时由恢复策略接管，让四足机器人高速奔跑而不碰撞。 · [代码](https://github.com/LeCAR-Lab/ABS)
- **[Expressive Whole-Body Control for Humanoid Robots](https://arxiv.org/abs/2402.16796)** (2024) — 上半身模仿人类动捕、下肢保持鲁棒行走，让人形机器人做出富有表现力的动作和舞蹈。
- **[HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots](https://arxiv.org/abs/2410.21229)** (2024) — 蒸馏出单一策略，支持多种人形控制模式（根部速度、关节角、关键点跟踪），不必为每种模式各训练一个控制器。
- **[HumanPlus: Humanoid Shadowing and Imitation from Humans](https://arxiv.org/abs/2406.10454)** (2024) — 人形机器人通过单个 RGB 相机实时模仿人类，再用采集的数据学习自主技能。 · [代码](https://github.com/MarkFzp/humanplus)
- **[Humanoid Parkour Learning](https://arxiv.org/abs/2406.10759)** (2024) — 无需动作参考，为 Unitree H1 学习基于视觉的全身跑酷策略，涵盖跳上平台、跨越沟壑等技能，并迁移到真实机器人。
- **[Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](https://arxiv.org/abs/2403.04436)** (2024) — H2O：强化学习跟踪策略借助 RGB 相机，把人的全身动作实时映射到人形机器人。
- **[OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](https://arxiv.org/abs/2406.08858)** (2024) — 一个强化学习全身控制器：人形机器人可跟随 VR 头显、语音指令或 RGB 相机的输入，也可执行学习得到的自主策略。
- **[Unitree RL Gym](https://github.com/unitreerobotics/unitree_rl_gym)** (2024) — 宇树官方的强化学习运动控制入门仓库，支持 Go2、H1、G1：在 Isaac Gym 中训练，在 MuJoCo 中做 sim2sim 验证，再部署到真机。
- **[ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots](https://arxiv.org/abs/2306.14874)** (2023) — 分层的全学习系统：导航策略结合学习到的障碍物重建来调度预训练技能（行走、跳跃、攀爬、下蹲）；报告实机速度可达 2 米/秒。发表于 Science Robotics。
- **[DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning](https://arxiv.org/abs/2301.10602)** (2023) — 盲视四足策略：借助上下文辅助估计器从本体感觉历史中隐式推断地形特性，无需相机即可稳健地走楼梯和崎岖地面。
- **[Extreme Parkour with Legged Robots](https://arxiv.org/abs/2309.14341)** (2023) — 端到端深度相机策略让小型四足机器人完成跳远、跳高和倒立。 · [代码](https://github.com/chengxuxin/extreme-parkour)
- **[Robot Parkour Learning](https://arxiv.org/abs/2309.05665)** (2023) — 将多个跑酷专家技能蒸馏为单一视觉策略，让低成本四足机器人攀爬、跳跃和匍匐。 · [代码](https://github.com/ZiwenZhuang/parkour)
- **[Learning robust perceptive locomotion for quadrupedal robots in the wild](https://arxiv.org/abs/2201.08117)** (2022) — ANYmal 通过学习的信念编码器融合本体感知与带噪声的高程图感知，在高山徒步路线等复杂地形上完成行走。
- **[Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior](https://arxiv.org/abs/2212.03238)** (2022) — 训练一个把步态参数（频率、抬脚高度、姿态等）作为指令开放的四足策略，部署时可由人调节行为以适应新任务；附带面向 Unitree Go1 的开源仿真到真实工具链。 · [代码](https://github.com/Improbable-AI/walk-these-ways)
- **[AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control](https://arxiv.org/abs/2104.02180)** (2021) — 用在无结构动捕片段上训练的判别器作为"风格奖励"，强化学习无需逐段指定参考动作即可学到自然的动作；后来被广泛用作足式机器人的步态先验。
- **[RMA: Rapid Motor Adaptation for Legged Robots](https://arxiv.org/abs/2107.04034)** (2021) — 自适应模块在线估计环境参数，使同一策略实时适应新地形和负载。
- **[Learning Quadrupedal Locomotion over Challenging Terrain](https://arxiv.org/abs/2010.11251)** (2020) — 仅依赖本体感知的师生策略，让 ANYmal 在泥地、雪地和碎石等野外地形行走。
- **[Learning Agile and Dynamic Motor Skills for Legged Robots](https://arxiv.org/abs/1901.08652)** (2019) — 学习的执行器模型缩小仿真与现实差距，使强化学习策略能让 ANYmal 奔跑并摔倒后起身。
- _另见:_ [DreamGen](#world-models), [NaVILA](#navigation), [Vision as Proprioception](#perception), [Crocoddyl](#control), [OCS2](#control), [Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](#control), [legged_control](#control), [Humanoid-Gym](#sim), [HumanoidBench](#datasets), [EgoExplorer](#datasets), [Open-TeleVision](#hardware), [Berkeley Humanoid](#hardware), [Demonstrating Berkeley Humanoid Lite](#hardware), [ToddlerBot](#hardware), [HOMIE](#hardware), [An Open Torque-Controlled Modular Robot Architecture for Legged Locomotion Research](#hardware), [UMI-on-Legs](#hardware)

<a id="world-models"></a>
### 世界模型

_学习的动力学模型、视频世界模型、世界动作模型（WAM）与基于模型的强化学习。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/world-models.html)

- ⭐ **[Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104)** (2023) — DreamerV3：一套超参数适用于 150 多个任务，包括从零开始在《我的世界》中挖到钻石。 · [代码](https://github.com/danijar/dreamerv3)
- **[Agentic World Action Models](https://arxiv.org/abs/2610.30136)** (2026) — AW-0 在同一个混合 Transformer 中联合生成代码、未来视频和机器人动作三路输出：代码既组织多步预测与控制，又沉淀为可复用技能库；报告在 RoboTwin 2.0 和真机双臂任务上优于 VLA 与 WAM 基线。 · [项目页](https://agentic-wam.github.io/)
- **[CW-WAM: A Structured Contact-Wrench World Action Model for Force-Sensitive Manipulation](https://arxiv.org/abs/2610.30117)** (2026) — 一个同时预测未来视频、运动与接触力旋量的世界动作模型，借鉴力位混合控制思路，输出时间对齐的运动-力旋量片段作为控制参考，面向仅靠视觉无法感知接触与负载的力敏感操作任务。 · [项目页](https://cw-wam-project.github.io/)
- **[GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774)** (2026) — 同一个世界模型兼作策略，用共享的关节坐标动作空间覆盖 20 类机器人；论文报告其在 WorldArena、RoboTwin 2.0、LIBERO-plus 上表现突出，并蒸馏出可实时运行的单步人形机器人策略。 · [项目页](https://greenvla.github.io/GreenWAM)
- **[Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning](https://arxiv.org/abs/2610.28613)** (2026) — 动作条件的视触觉世界模型：在统一的视频空间中同时预测多视角 RGB 与触觉图像，并经一致性后训练保证与真实任务状态吻合；可用于闭环策略评估和 GRPO 策略更新。 · [项目页](https://zebinx.github.io/PhysCanvas_HomePage/)
- **[Robotic Video World Models: A Survey of Applications, Research Challenges, Future Directions](https://arxiv.org/abs/2601.07823)** (2026) — 机器人视频世界模型综述：它们在哪些场景可替代或补充物理仿真器（如可变形物体）、主要应用与开放挑战，并附持续更新的论文列表。 · [代码](https://github.com/irom-princeton/awesome-robotics-video-world-model-papers)
- **[Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855)** (2026) — 同时覆盖移动与操作的第一人称世界模型，在约 1 万小时人类视频和约 3 千小时机器人数据上训练，用统一的运动学表示描述不同本体的动作。 · [代码](https://github.com/Ropedia/ropedia-w0)
- **[RynnUnify: Towards Unified Embodied Brain](https://arxiv.org/abs/2610.32965)** (2026) — 16B 统一具身模型，交替进行视频预测与语言推理，兼顾具身理解与长程视觉规划，并扩展出用于机器人控制的世界-动作版本；另提出 Rynn-VP、Rynn-GEU 评测，报告在 20 个 RoboCasa365 组合任务上成功率 51.5%。 · [代码](https://github.com/alibaba-damo-academy/RynnUnify) · [项目页](https://alibaba-damo-academy.github.io/RynnUnify.github.io/)
- **[Self-Distilling Future Video Representations for World Action Models](https://arxiv.org/abs/2610.30320)** (2026) — FRED 通过自蒸馏并引入历史观测，让世界动作模型在单步去噪中预测出更好的未来视频表征；报告在长时程、域外环境以及只有人类视频示范的任务上提升明显。 · [代码](https://github.com/suhyeok-jang/FRED) · [项目页](https://huiwon-jang.github.io/FRED/)
- **[Skeleton-Grounded Latent Action Model for Robot World Models](https://arxiv.org/abs/2610.31474)** (2026) — SkeLAM 把潜在动作拆成由机器人骨架监督的运动学部分和保留其余视觉动态的残差部分，使世界模型生成更贴合机器人控制指令；报告在 DROID 上末端轨迹误差比 DreamDojo 低 19.5%，预测成功率与真机评测一致。 · [项目页](https://aopolin-lv.github.io/SkeLAM/)
- **[UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry](https://arxiv.org/abs/2610.30991)** (2026) — 世界动作模型：把场景级三维流（跟踪的三维点）纳入策略内部，而不是作为独立模块或额外输出头，让 4D 几何、视觉语义与动作一起建模。 · [项目页](https://kksham111.github.io/UniFlowWAM_ProjectPage/)
- **[Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575)** (2025) — 开放的视频世界基础模型及分词器与数据管线，用于生成物理 AI 训练数据。
- **[DreamGen: Unlocking Generalization in Robot Learning through Video World Models](https://arxiv.org/abs/2505.12705)** (2025) — 把视频世界模型微调到目标机器人上“做梦”生成新示范，再用隐动作或逆动力学模型补上动作标签用于训练策略；人形机器人仅凭单一场景的遥操作数据学会 20 多种新行为。 · [代码](https://github.com/NVIDIA/GR00T-Dreams) · [项目页](https://research.nvidia.com/labs/gear/dreamgen)
- **[Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation](https://arxiv.org/abs/2508.05635)** (2025) — 智元 Genie Envisioner：一个平台集成视频扩散世界模型 GE-Base、流匹配动作解码器 GE-Act、动作条件神经仿真器 GE-Sim，以及世界模型评测基准 EWMBench。 · [代码](https://github.com/AgibotTech/Genie-Envisioner-V1)
- **[Unified Video Action Model](https://arxiv.org/abs/2503.00200)** (2025) — UVA：视频与动作共享一个潜表示，配两个轻量扩散头解码；通过掩码训练，同一模型既能当策略，也能做视频生成和正/逆动力学，且策略推理仍然较快。 · [代码](https://github.com/ShuangLI59/unified_video_action)
- **[V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985)** (2025) — 自监督视频编码器经少量机器人数据后训练，通过潜空间预测实现零样本抓放规划。
- **[Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations](https://arxiv.org/abs/2412.14803)** (2025) — VPP：在机器人与人类操作视频上微调 Stable Video Diffusion，只做一次前向提取"预测性"视觉特征再交给扩散策略；论文报告 CALVIN ABC→D 平均完成长度 4.33，并有 Franka 与灵巧手真机实验。 · [代码](https://github.com/roboterax/video-prediction-policy)
- **[WorldVLA: Towards Autoregressive Action World Model](https://arxiv.org/abs/2506.21539)** (2025) — 单个自回归模型同时充当 VLA 策略与预测未来图像的世界模型，二者在 LIBERO 上相互促进；论文还发现自回归生成动作块会累积误差，用屏蔽先前动作的注意力掩码可以缓解。 · [代码](https://github.com/alibaba-damo-academy/WorldVLA)
- **[DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](https://arxiv.org/abs/2411.04983)** (2024) — 预测未来的 DINOv2 图像块特征而非像素，使基于离线数据训练的世界模型能在测试时规划到新的视觉目标。 · [代码](https://github.com/gaoyuezhou/dino_wm)
- **[Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391)** (2024) — 仅从无标注的网络视频中学习可交互环境与潜在动作。
- **[Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](https://arxiv.org/abs/2312.13139)** (2024) — GR-1：GPT 式模型同时预测动作与未来画面；先在 Ego4D 上做视频预测预训练、再用机器人数据微调，论文报告 CALVIN 未见场景成功率从 53.3% 提升到 85.4%。 · [代码](https://github.com/bytedance/GR-1)
- **[Learning Interactive Real-World Simulators](https://arxiv.org/abs/2310.06114)** (2023) — UniSim：以动作为条件的视频生成模型充当仿真器，训练出的策略可迁移到真实世界。
- **[Learning Universal Policies via Text-Guided Video Generation](https://arxiv.org/abs/2302.00111)** (2023) — UniPi：把决策问题转化为文本条件的视频生成，再用逆动力学模型从生成的画面中恢复动作。
- **[TD-MPC2: Scalable, Robust World Models for Continuous Control](https://arxiv.org/abs/2310.16828)** (2023) — 无解码器的隐式世界模型配合 MPC 规划；同一组超参数适用于大量连续控制任务，并可扩展为多任务智能体。 · [代码](https://github.com/nicklashansen/tdmpc2)
- **[Transformers are Sample-Efficient World Models](https://arxiv.org/abs/2209.00588)** (2023) — IRIS：离散自编码器把画面变成 token，Transformer 预测后续 token；智能体只用约 2 小时的 Atari 游戏经验便在想象中学会策略。 · [代码](https://github.com/eloialonso/iris)
- **[DayDreamer: World Models for Physical Robot Learning](https://arxiv.org/abs/2206.14176)** (2022) — 直接在真实机器人上训练 Dreamer——四足机器人无需仿真器，约一小时学会行走。
- **[Temporal Difference Learning for Model Predictive Control](https://arxiv.org/abs/2203.04955)** (2022) — TD-MPC：用面向任务的潜空间模型做短视距规划，由学习到的价值函数估计长期回报；是 TD-MPC2 的前身。 · [代码](https://github.com/nicklashansen/tdmpc)
- **[Mastering Atari with Discrete World Models](https://arxiv.org/abs/2010.02193)** (2021) — DreamerV2：把 Dreamer 的潜变量改为离散类别分布，仅在世界模型的想象中学习 Atari 策略，达到人类水平。 · [代码](https://github.com/danijar/dreamerv2)
- **[Dream to Control: Learning Behaviors by Latent Imagination](https://arxiv.org/abs/1912.01603)** (2019) — 第一代 Dreamer：从像素学习潜空间世界模型，并完全在想象的轨迹上训练策略。
- **[Learning Latent Dynamics for Planning from Pixels](https://arxiv.org/abs/1811.04551)** (2019) — PlaNet：从图像中学习潜空间动力学模型（即后来 Dreamer 沿用的 RSSM），并用 CEM 直接在潜空间中规划动作。 · [代码](https://github.com/google-research/planet)
- **[World Models](https://arxiv.org/abs/1803.10122)** (2018) — 经典的 VAE + RNN 智能体，学习环境的压缩模型并在"梦境"中训练控制器。 · [项目页](https://worldmodels.github.io/)
- _另见:_ [WAVE-0](#vla), [3D-VLA](#vla), [GR-2](#vla), [Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation](#manipulation), [SuperMimic](#locomotion), [EmbodiedWorld-200K](#navigation), [Planning with Diffusion for Flexible Behavior Synthesis](#control)

<a id="navigation"></a>
### 导航与具身智能体

_视觉语言导航、具身问答、移动操作与大模型规划。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/navigation.html)

- ⭐ **[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)** (2022) — SayCan：大模型提出步骤，学习到的价值函数评估机器人当下实际能做什么。
- **[Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System](https://arxiv.org/abs/2610.19600)** (2026) — 发现 VLA 在原子技能上 80% 成功率、组合成移动操作后仅 19%，分析失败原因并据此构建智能体式系统。 · [代码](https://github.com/PKU-VaLuE-Lab/Cracking-Mobile-Manipulation)
- **[EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models](https://arxiv.org/abs/2610.25959)** (2026) — 包含 20 万余条导航规划样本的数据集，场景多样，标注从相机运动轨迹到高层语义指令；并把视频世界模型当作低成本交互环境做强化学习后训练，报告称在未见场景上有明显提升。 · [项目页](https://xiaokunfeng.github.io/EmbodiedWorld-200K/)
- **[Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance](https://arxiv.org/abs/2610.20607)** (2026) — HiRe-MoMa 在真实环境中通过学习残差修正来微调冻结的移动操作策略，只需偶尔的人类引导。 · [项目页](https://hire-moma.github.io/)
- **[ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation](https://arxiv.org/abs/2610.25690)** (2026) — 先在互联网第一视角视频上预训练，学习"朝描述的目标走近时画面如何变化"，再用仿真数据对齐到动作；论文报告在自建 HabitatGS-LN 基准上成功率 94.9%，并在真实四足机器人上部署。 · [项目页](https://zju3dv.github.io/ScaleNav/)
- **[TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments](https://arxiv.org/abs/2610.30043)** (2026) — 带具身 NPC、受限对话和事件驱动任务状态机的物理仿真框架，并提供让冻结多模态大模型调用多级技能的执行框架；基于 30 个室内场景构建 360 回合基准，评测 8 个模型，报告通用模型可胜过具身专用模型，任务变更和人机协作仍是难点。 · [代码](https://github.com/xuyicheng-zju/TARSphere) · [项目页](https://xuyicheng-zju.github.io/TARSphere/)
- **[NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://arxiv.org/abs/2412.04453)** (2024) — VLA 先用语言输出中层导航指令，再由强化学习运动策略执行，让腿式机器人按自然语言指令导航；并提供 Isaac Lab 上的 VLN 基准。 · [代码](https://github.com/AnjieCheng/NaVILA) · [项目页](https://navila-bot.github.io/)
- **[NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation](https://arxiv.org/abs/2402.15852)** (2024) — 基于视频的视觉语言模型：只看单目 RGB 历史帧和语言指令，直接输出下一步导航动作，不依赖地图、里程计或深度。 · [代码](https://github.com/jzhzhang/NaVid-VLN-CE)
- **[OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics](https://arxiv.org/abs/2401.12202)** (2024) — 组合现成的开放词汇模型，构建无需训练即可在真实家庭中抓取放置的系统。
- **[Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks](https://arxiv.org/abs/2412.06224)** (2024) — 把 NaVid 扩展为单一视频 VLA 模型，统一处理多种导航任务（指令导航、目标搜索、具身问答、跟随人）。 · [代码](https://github.com/jzhzhang/NaVid-VLN-CE)
- **[ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments](https://arxiv.org/abs/2304.03047)** (2023) — 面向连续环境视觉语言导航：根据预测的路点在线构建拓扑地图，用跨模态 Transformer 在图上规划，再由避障控制器执行；报告在 R2R-CE、RxR-CE 上分别比此前最好方法提升 10% 和 20% 以上。 · [代码](https://github.com/MarSaKi/ETPNav)
- **[NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models](https://arxiv.org/abs/2305.16986)** (2023) — 纯大语言模型的视觉语言导航智能体：GPT 读取视觉观测的文字描述、历史轨迹和可走方向，逐步显式推理下一步去哪；在 R2R 上零样本运行，但仍落后于专门训练的模型。 · [代码](https://github.com/GengzeZhou/NavGPT)
- **[NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](https://arxiv.org/abs/2310.07896)** (2023) — 通过对目标做掩码，单一扩散策略同时完成目标导航与探索。
- **[PIRLNav: Pretraining with Imitation and RL Finetuning for ObjectNav](https://arxiv.org/abs/2301.07302)** (2023) — PIRLNav：先在人类 ObjectNav 演示上做行为克隆，再用强化学习微调同一策略；论文报告在 Habitat ObjectNav 上成功率 65.0%，比此前最佳高 5 个百分点。 · [代码](https://github.com/Ram81/pirlnav)
- **[VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](https://arxiv.org/abs/2312.03275)** (2023) — 零样本目标物体导航：用视觉-语言模型对探索前沿与目标的相关度打分来决定往哪走，无需针对任务训练；在 Habitat 和 Spot 机器人上验证。 · [代码](https://github.com/rai-opensource/vlfm)
- **[ViNT: A Foundation Model for Visual Navigation](https://arxiv.org/abs/2306.14846)** (2023) — 在多种机器人的导航数据上训练的 Transformer 导航策略，经少量微调即可适配新的目标形式和新机器人。 · [代码](https://github.com/robodhruv/visualnav-transformer)
- **[CoWs on Pasture: Baselines and Benchmarks for Language-Driven Zero-Shot Object Navigation](https://arxiv.org/abs/2203.10421)** (2022) — CoWs on Pasture：CLIP on Wheels 把开放词汇定位（CLIP 等模型，无需微调）与经典探索结合，实现零样本目标物体导航；配套的 Pasture 基准加入了少见物体、按属性描述的物体和被遮挡物体。 · [项目页](https://cow.cs.columbia.edu/)
- **[Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753)** (2022) — 大模型编写调用感知与控制 API 的 Python 代码，把指令变成可响应的机器人程序。
- **[GNM: A General Navigation Model to Drive Any Robot](https://arxiv.org/abs/2210.03370)** (2022) — ViNT 的前作：在多种不同机器人汇集的数据上训练一个目标条件导航策略，可迁移到包括训练中未见过的新机器人。 · [代码](https://github.com/robodhruv/visualnav-transformer)
- **[Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608)** (2022) — 将成功检测与场景描述反馈给大模型规划器，使其在失败后重新规划。
- **[LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action](https://arxiv.org/abs/2207.04429)** (2022) — 将大语言模型（从指令中解析地标）、CLIP（在图像中找到地标）与视觉导航模型串联，无需带语言标注的机器人数据即可在真实机器人上按路线指令导航。 · [代码](https://github.com/blazejosinski/lm_nav)
- **[Visual Language Maps for Robot Navigation](https://arxiv.org/abs/2210.05714)** (2022) — VLMaps 将视觉语言特征融合进 3D 地图，使机器人可按开放词汇空间目标导航。
- **[Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments](https://arxiv.org/abs/2004.02857)** (2020) — VLN-CE 把 Room-to-Room 指令从固定导航图搬到 Habitat 连续环境中、使用底层动作执行，是更贴近真实的 VLN 标准设定。 · [代码](https://github.com/jacobkrantz/VLN-CE)
- **[Learning to Explore using Active Neural SLAM](https://arxiv.org/abs/2004.05155)** (2020) — 将探索拆为可学习的神经 SLAM 模块、选择长期目标的全局策略和到达目标的局部策略，比端到端强化学习样本效率高得多。 · [代码](https://github.com/devendrachaplot/Neural-SLAM)
- **[Object Goal Navigation using Goal-Oriented Semantic Exploration](https://arxiv.org/abs/2007.00643)** (2020) — SemExp 构建情景语义地图，并学习在地图上选择长期目标的策略；这一模块化方案成为 Habitat 中 ObjectNav 的常用基线。 · [代码](https://github.com/devendrachaplot/Object-Goal-Navigation)
- **[The Marathon 2: A Navigation System](https://arxiv.org/abs/2003.00368)** (2020) — ROS 2 标准导航栈 Nav2 的论文：用行为树编排规划器、控制器和恢复行为，并在真实机器人上长距离“马拉松”测试验证。 · [代码](https://github.com/ros-navigation/navigation2)
- **[Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](https://arxiv.org/abs/1711.07280)** (2017) — 提出视觉语言导航任务与基于 Matterport3D 的 Room-to-Room (R2R) 基准。
- _另见:_ [Has GPT-6-Astra Achieved Embodied Intelligence?](#vla), [Aligning Cyber Space with Physical World](#vla), [RynnBrain](#vla), [Agile But Safe](#locomotion), [ConceptGraphs](#perception), [Habitat 3.0](#sim), [Habitat 2.0](#sim), [SceneBloom](#sim), [MARE](#sim), [Habitat](#datasets), [Embodied Skill Bench](#datasets), [Habitat-Matterport 3D Dataset (HM3D)](#datasets), [The Design of Stretch](#hardware)

<a id="perception"></a>
### 感知、SLAM 与三维建图

_视觉/激光 SLAM 与里程计、三维重建、物体位姿、深度估计与开放词汇场景地图。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/perception.html)

- ⭐ **[Segment Anything](https://arxiv.org/abs/2304.02643)** (2023) — SAM：可用点、框、掩码提示的分割模型，在 10 亿级掩码上训练；已成为机器人感知流程中获取物体掩码的常用基础组件。 · [代码](https://github.com/facebookresearch/segment-anything)
- ⭐ **[ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](https://arxiv.org/abs/2007.11898)** (2020) — 最常用的特征点 SLAM 库：支持单目、双目与 RGB-D，可融合 IMU，并支持多地图重定位。 · [代码](https://github.com/UZ-SLAMLab/ORB_SLAM3)
- **[ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models](https://arxiv.org/abs/2610.27040)** (2026) — 用自动标注的机器人操作录像加多来源视觉数据构建约 150 万条可验证的定位监督，微调 Qwen3.5-9B；报告在七个公开视觉定位基准上平均 75.41 分，GPT-6 Astra 为 73.68。 · [代码](https://github.com/DAXIAORobotics/ACE-Brain-0.6) · [项目页](https://daxiaorobotics.github.io/ACE-Brain-0.6/)
- **[SpaRV: Sparse Radiance Voxels for Scalable Geometrically Consistent LiDAR-Visual Mapping and Rendering](https://arxiv.org/abs/2610.25665)** (2026) — 用激光雷达与相机数据构建稀疏体素辐射场地图，针对机器人数据视角少、位姿有误差、场景大的问题，在保证几何精度的同时控制显存占用。 · [代码](https://github.com/hku-mars/SpaRV)
- **[Vision as Proprioception: Estimating Humanoid Robot Pose from Video](https://arxiv.org/abs/2610.25288)** (2026) — HumanoidPose 仅凭视频恢复人形机器人的全身关节构型：适用于拿不到机载状态的场景，也能把网上的机器人视频变成训练数据。 · [代码](https://github.com/eth-siplab/HumanoidPose)
- **[Which Depth Estimator for Jetson AGX Orin? A 2026 Benchmark of Monocular and Stereo Methods](https://arxiv.org/abs/2610.27199)** (2026) — 给机器人开发者的实测数据：在 Jetson AGX Orin 上用 TensorRT 运行九类单目与双目深度估计模型（Depth Anything V2/3、Depth Pro、MoGe-2、Fast-FoundationStereo 等），并评测度量精度与速度。 · [代码](https://github.com/nodarhub/orin-depth-benchmark)
- **[FoundationStereo: Zero-Shot Stereo Matching](https://arxiv.org/abs/2501.09898)** (2025) — 在大规模合成数据上训练的双目深度模型，报告称在真实场景上零样本精度很强；可直接作为双目相机机器人的深度来源。 · [代码](https://github.com/NVlabs/FoundationStereo)
- **[SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719)** (2025) — 给定短名词短语或示例图像，即可在图像和视频中分割并跟踪某一概念的所有实例；数据引擎覆盖 400 万个概念标签，开放权重与 SA-Co 基准，可直接用作机器人开放词汇感知模块。 · [代码](https://github.com/facebookresearch/sam3)
- **[VGGT: Visual Geometry Grounded Transformer](https://arxiv.org/abs/2503.11651)** (2025) — 单个前馈 Transformer 一次性为多视角图像预测相机参数、深度、点图与跟踪，约一秒完成。 · [代码](https://github.com/facebookresearch/vggt)
- **[Depth Anything V2](https://arxiv.org/abs/2406.09414)** (2024) — 先只用深度精确的合成图像训练大教师模型，再给大量真实图像打伪标签来训练小模型；单目深度比 V1 更锐利、更鲁棒。 · [代码](https://github.com/DepthAnything/Depth-Anything-V2)
- **[Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](https://arxiv.org/abs/2401.10891)** (2024) — 在数千万张伪标注图像上训练的单目深度模型，常被机器人系统直接拿来作为深度先验。 · [代码](https://github.com/LiheYoung/Depth-Anything)
- **[FAST-LIVO2: Fast, Direct LiDAR-Inertial-Visual Odometry](https://arxiv.org/abs/2408.14035)** (2024) — FAST-LIVO2：在同一滤波器中融合激光雷达、相机与 IMU，两种传感器都采用直接法（无需提取特征）更新，并共用一张体素地图，图像块挂载在激光点上。 · [代码](https://github.com/hku-mars/FAST-LIVO2)
- **[Grounding Image Matching in 3D with MASt3R](https://arxiv.org/abs/2406.09756)** (2024) — 在 DUSt3R 基础上加入稠密局部特征头，同一网络既输出三维点图又给出视角间精确的像素匹配，适用于免标定的三维重建与定位。 · [代码](https://github.com/naver/mast3r)
- **[SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714)** (2024) — 用流式记忆把 SAM 扩展到视频：一次提示得到的掩码可在后续帧中持续跟踪，适合在操作过程中跟随目标物体。 · [代码](https://github.com/facebookresearch/sam2)
- **[BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects](https://arxiv.org/abs/2303.14158)** (2023) — 在 RGB-D 视频中跟踪从未见过物体的六自由度位姿，同时在线构建其神经三维模型，无需 CAD 模型；适用于操作新物体。 · [代码](https://github.com/NVlabs/BundleSDF)
- **[CoTracker: It is Better to Track Together](https://arxiv.org/abs/2307.07635)** (2023) — 联合跟踪视频中大量点（而非逐点独立跟踪）的 Transformer，遮挡下依然稳健；常用于从人类或机器人视频中提取运动轨迹来学习策略。 · [代码](https://github.com/facebookresearch/co-tracker)
- **[ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650)** (2023) — 用视觉语言模型构建带语义标注的物体级三维场景图，大模型规划器可以用自然语言查询。 · [项目页](https://concept-graphs.github.io/)
- **[DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193)** (2023) — 自监督学习的图像特征，冻结即可用于深度估计、分割和检索；是 VLA（如 OpenVLA）和潜空间世界模型常用的视觉骨干。 · [代码](https://github.com/facebookresearch/dinov2)
- **[DUSt3R: Geometric 3D Vision Made Easy](https://arxiv.org/abs/2312.14132)** (2023) — 不需要已知相机内参或位姿，直接从图像对回归三维点图，开启了“三维基础模型”这一方向。 · [代码](https://github.com/naver/dust3r)
- **[FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects](https://arxiv.org/abs/2312.08344)** (2023) — 只需 CAD 模型或少量参考图像即可对未见过的物体做 6D 位姿估计与跟踪，无需逐物体训练。 · [代码](https://github.com/NVlabs/FoundationPose)
- **[Gaussian Splatting SLAM](https://arxiv.org/abs/2312.06741)** (2023) — MonoGS：直接在三维高斯地图上做 SLAM，仅用单个相机即可同时完成相机跟踪与照片级稠密建图。 · [代码](https://github.com/muskie82/MonoGS)
- **[Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection](https://arxiv.org/abs/2303.05499)** (2023) — 开放集目标检测器，可根据任意文本提示找到物体；常与 SAM 组合（Grounded-SAM），把语言指令变成物体掩码。 · [代码](https://github.com/IDEA-Research/GroundingDINO)
- **[DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](https://arxiv.org/abs/2108.10869)** (2021) — 端到端学习的视觉 SLAM：循环光流更新加上可微分的光束法平差层。 · [代码](https://github.com/princeton-vl/DROID-SLAM)
- **[FAST-LIO2: Fast Direct LiDAR-inertial Odometry](https://arxiv.org/abs/2107.06829)** (2021) — 用增量 k-d 树把原始激光点直接配准到地图，速度足以在无人机和机器人机载计算机上运行。 · [代码](https://github.com/hku-mars/FAST_LIO)
- **[LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping](https://arxiv.org/abs/2007.00258)** (2020) — 基于因子图的激光-惯性里程计，GPS 与回环可以作为额外因子直接加入。 · [代码](https://github.com/TixiaoShan/LIO-SAM)
- _另见:_ [Aligning Cyber Space with Physical World](#vla), [RynnBrain](#vla), [Contact-GraspNet](#manipulation), [AnyGrasp](#manipulation), [Neural feels with neural fields](#tactile), [GelSlim 5.0](#tactile), [Watch Your Step](#locomotion), [Solving a Giant Rubik's Cube with a Quadruped Robot](#locomotion), [RynnUnify](#world-models), [Object Goal Navigation using Goal-Oriented Semantic Exploration](#navigation), [Learning to Explore using Active Neural SLAM](#navigation), [MARE](#sim), [ScanNet](#datasets), [DexYCB](#datasets), [Rescaling Egocentric Vision](#datasets), [HOI4D](#datasets), [ARCTIC](#datasets)

<a id="control"></a>
### 规划、控制与安全

_运动规划、轨迹优化、模型预测控制、安全滤波器与安全的学习型控制。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/control.html)

- ⭐ **[cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation](https://arxiv.org/abs/2310.17274)** (2023) — 面向机械臂的 GPU 并行运动生成：同时运行大量轨迹优化，在毫秒级给出无碰撞且平滑的轨迹。 · [代码](https://github.com/NVlabs/curobo)
- **[CusADi2: Latency-Optimized Batch Computation of Robot Kinematics, Jacobians, and Hessians on the GPU](https://arxiv.org/abs/2610.25476)** (2026) — 在 GPU 上以低延迟批量计算运动学、雅可比与海森矩阵，面向在线运行的采样式与梯度式轨迹优化。 · [代码](https://github.com/johnviljoen/cusadi2)
- **[PrismPlan: A Shared GPU Substrate for Motion Planning Across Paradigms](https://arxiv.org/abs/2610.23884)** (2026) — 一次性实现批量 GPU 碰撞检测与正运动学，在其上运行采样、搜索和优化三类规划器，使三种范式可以公平比较。 · [代码](https://github.com/XiaoyubotMotionTeam/PrismPlan)
- **[Sub-Millisecond Reflexes for Continuous Physical Human-Robot Interaction](https://arxiv.org/abs/2610.21913)** (2026) — 开源的 ROS 2 多模式控制器，可在亚毫秒内切换控制模式并触发安全反射而无需中断任务；在 Franka 机械臂上验证。 · [代码](https://github.com/RoboRef/franka_reflex_engine)
- **[Motions in Microseconds via Vectorized Sampling-Based Planning](https://arxiv.org/abs/2309.14545)** (2023) — VAMP：用 CPU SIMD 指令把碰撞检测向量化，使 RRT-Connect 等基于采样的规划器在微秒到毫秒级求解机械臂运动规划，无需 GPU。 · [代码](https://github.com/KavrakiLab/vamp)
- **[Motion Policy Networks](https://arxiv.org/abs/2210.12209)** (2022) — 在数百万条规划器生成的轨迹上训练的神经策略，可直接根据点云把机械臂移动到目标位置。 · [代码](https://github.com/NVlabs/motion-policy-networks)
- **[Planning with Diffusion for Flexible Behavior Synthesis](https://arxiv.org/abs/2205.09991)** (2022) — Diffuser：把规划视为对整条轨迹去噪，目标与奖励可以引导采样；扩散模型与控制结合的早期代表作。 · [代码](https://github.com/jannerm/diffuser)
- **[Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo](https://arxiv.org/abs/2212.00541)** (2022) — 推出 MuJoCo MPC（MJPC），可在 MuJoCo 中交互式地做实时预测控制，并表明简单的基于采样的规划器在接触丰富的行为上是很强的基线。 · [代码](https://github.com/google-deepmind/mujoco_mpc)
- **[legged_control](https://github.com/qiayuanl/legged_control)** (2022) — 基于 OCS2 与 ros-control 的开源四足控制栈：非线性 MPC + 全身控制 + 状态估计，并支持 sim2real；基于模型的足式控制常用的起点。
- **[Jerk-limited Real-time Trajectory Generation with Arbitrary Target States](https://arxiv.org/abs/2105.04830)** (2021) — Ruckig：开源 C++/Python 库，可实时生成到任意目标位置、速度和加速度的时间最优、限加加速度（jerk）轨迹；常被直接用于真实控制器上的机械臂平滑运动。 · [代码](https://github.com/pantor/ruckig)
- **[OCS2: Optimal Control for Switched Systems](https://github.com/leggedrobotics/ocs2)** (2021) — 面向切换系统的非线性 MPC C++ 工具箱（SLQ、DDP、SQP），附足式机器人与移动操作臂示例；许多开源足式 MPC + 全身控制方案都基于它。
- **[Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning](https://arxiv.org/abs/2108.06266)** (2021) — 综述，连接控制理论与强化学习两种安全视角：从带保证的学习动力学到约束强化学习与安全滤波器。
- **[safe-control-gym: a Unified Benchmark Suite for Safe Learning-based Control and Reinforcement Learning in Robotics](https://arxiv.org/abs/2109.06325)** (2021) — Gym 风格基准，含倒立摆与四旋翼任务、约束与扰动，用于比较安全控制与安全强化学习方法。 · [代码](https://github.com/utiasDSL/safe-control-gym)
- **[OSQP: An Operator Splitting Solver for Quadratic Programs](https://arxiv.org/abs/1711.08013)** (2020) — 基于 ADMM 的快速、鲁棒二次规划求解器，支持热启动与嵌入式 C 代码生成，广泛用于 MPC 与全身控制器。 · [代码](https://github.com/osqp/osqp)
- **[Control Barrier Functions: Theory and Applications](https://arxiv.org/abs/1903.11199)** (2019) — 控制障碍函数教程：为任意控制器加一层“尽量少改动”的安全滤波器、保证系统安全的标准方法。
- **[Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control](https://arxiv.org/abs/1909.04947)** (2019) — 基于 DDP 的开源接触丰富轨迹优化求解器，广泛用于足式与人形机器人的运动生成和 MPC。 · [代码](https://github.com/loco-3d/crocoddyl)
- **[MoveIt 2](https://moveit.ai/)** (2019) — ROS 2 的机械臂操作框架：提供运动规划、逆运动学、碰撞检测与实时伺服控制。 · [代码](https://github.com/moveit/moveit2)
- **[Pinocchio](https://github.com/stack-of-tasks/pinocchio)** (2019) — 高性能 C++/Python 刚体动力学库，提供解析导数；是运动学、最优控制（如 Crocoddyl）以及足式/人形机器人控制栈的常用底座。
- **[acados: a modular open-source framework for fast embedded optimal control](https://arxiv.org/abs/1910.13753)** (2019) — 高速非线性 MPC 与状态估计求解器，提供 Python/MATLAB 接口并可为嵌入式平台生成 C 代码。 · [代码](https://github.com/acados/acados)
- **[Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](https://github.com/mit-biomimetics/Cheetah-Software)** (2018) — 四足机器人的凸 MPC：用简化刚体动力学把足端地面反作用力规划变成可实时求解的小规模 QP；众多开源四足控制器背后的经典基于模型的基线。
- **[Riemannian Motion Policies](https://arxiv.org/abs/1801.02854)** (2018) — RMP：把每种行为（到达、避障、关节限位）表示为加速度策略加黎曼度量，再按几何方式组合；是后来 RMPflow 与几何织物（geometric fabrics）控制器的基础。
- **[Hamilton-Jacobi Reachability: A Brief Overview and Recent Advances](https://arxiv.org/abs/1709.07523)** (2017) — Hamilton-Jacobi 可达性分析简明教程：计算在最坏扰动下仍能保持系统安全的状态集合，以及将其扩展到更高维系统的方法。
- **[Drake](https://drake.mit.edu/)** (2014) — 面向机器人的基于模型的工具箱：带接触的多体动力学仿真、数学规划与轨迹优化；MIT 操作与欠驱动课程即使用它。 · [代码](https://github.com/RobotLocomotion/drake)
- **[OMPL: The Open Motion Planning Library](https://ompl.kavrakilab.org/)** (2012) — 采样式运动规划器的标准库（RRT、RRT-Connect、PRM、RRT* 等众多算法），也是 MoveIt 默认的规划后端。 · [代码](https://github.com/ompl/ompl)
- _另见:_ [TD-MPC2](#world-models)

<a id="learning"></a>
### 机器人学习：强化学习与模仿学习

_面向机器人的强化学习、模仿学习与策略后训练方法，不限机器人形态。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/learning.html)

- ⭐ **[Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](https://arxiv.org/abs/2410.21845)** (2024) — HIL-SERL：结合人类纠正的真机强化学习，报告称在精密装配与动态任务上经数小时训练即可接近满分成功率。 · [代码](https://github.com/rail-berkeley/hil-serl)
- ⭐ **[Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)** (2017) — 采用截断目标的策略梯度方法，是大多数 GPU 并行仿真训练（运动控制、灵巧操作）背后的算法。
- **[ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models](https://arxiv.org/abs/2610.18596)** (2026) — 面向 VLA 的持续离策略强化学习：轻量 actor/critic 在任务间延续，用少量保留的旧任务轨迹做蒸馏以防遗忘。论文报告新的接触式装配任务所需真机训练时间减少 31–68.5%，旧任务几乎不遗忘。 · [项目页](https://accrue-rl.github.io)
- **[AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](https://arxiv.org/abs/2610.28589)** (2026) — 像训练编程智能体一样对 9B 开源机器人规划器做后训练（SFT + 多轮强化学习），适配调用 VLA 技能和生成控制代码两类执行框架；报告在 LIBERO-PRO 上无外部记忆成功率从 18.1% 提升到 71.0%。 · [项目页](https://xinxinliu-ai.github.io/AgenticRoboRL/)
- **[EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions](https://arxiv.org/abs/2610.31845)** (2026) — 将机器人示教与动作标签噪声较大的第一视角视频联合训练 VLA：按数据源可靠性分配监督权重，并从干净的未来画面蒸馏表征；报告在最多 3 万小时预训练数据范围内扩展斜率高于基线。 · [项目页](https://lin-shan.com/EgoForesight)
- **[Learning from Fleet Experience: Collective Experience Learning Across 96 Robots](https://arxiv.org/abs/2610.25736)** (2026) — 部署中的机器人共享执行经验：用失败片段在机群经验库中检索相似的成功片段来微调策略，无需新增示教或人工纠正。论文报告五个真机任务成功率 93–99%，96 台机器人把手机装盒任务从 79% 提升到 98%。 · [代码](https://github.com/RLinf/RLinf)
- **[Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds](https://arxiv.org/abs/2610.28698)** (2026) — 针对游戏中的具身智能体做持续预训练的对照研究：120 组配置覆盖 0.8B–27B 模型、50–1600 小时数据和多世界混合；报告数据多样性有助于迁移到相近世界，对差异大的世界帮助有限。 · [代码](https://github.com/THUSI-Lab/GameScaling) · [项目页](https://gamescaling.github.io)
- **[TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models](https://arxiv.org/abs/2610.25376)** (2026) — 把预训练具身基础模型（教师）蒸馏到未做动作预训练的策略：在学生访问的状态上做在线监督，并由奖励模型监控进度、自动触发教师接管采集纠错轨迹（AutoDAgger，无需人工看护）；报告在 3 个真机任务上比行为克隆最高提升 4.1 倍。 · [代码](https://github.com/hku-sail/TILDE) · [项目页](https://hku-sail.github.io/TILDE/)
- **[Toward Recursive Self-Improvement in Physical AI](https://arxiv.org/abs/2610.29677)** (2026) — 把"递归自我改进"放到机器人学习语境下的综述：从提升技能到改进产生技能的过程，并总结增益能持续累积的条件；指出现有真机研究尚未单独验证"递归"本身带来的收益。附论文列表。 · [项目页](https://github.com/Physical2RSI/Awesome-Physical2RSI)
- **[Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy](https://arxiv.org/abs/2610.26848)** (2026) — PhysRSI-eval 在固定交互预算下用 18 个操作任务、五个维度（含从失败中改进）评测 VLM 智能体；报告公开基准平均分相近的模型改进速度差别很大，且早期物理反馈可用于预测后续进展。 · [项目页](https://physrsi-eval.github.io/)
- **[Flow Q-Learning](https://arxiv.org/abs/2502.02538)** (2025) — FQL：先用行为克隆训练流匹配策略，再训练一个最大化 Q 值、同时向流策略蒸馏的单步策略；避免对多步流采样反向传播，在 73 个 OGBench / D4RL 离线及离线转在线任务上表现突出。 · [代码](https://github.com/seohongpark/fql) · [项目页](https://seohong.me/projects/fql/)
- **[RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models](https://arxiv.org/abs/2510.06710)** (2025) — 面向 VLA 的开源强化学习训练框架（PPO/GRPO，支持 GPU 并行仿真器）；论文报告经 RL 后在 130 个 LIBERO 任务上成功率 98.11%、25 个 ManiSkill 任务上 97.66%，是 VLA+RL 研究常用的底座。 · [代码](https://github.com/RLinf/RLinf)
- **[SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning](https://arxiv.org/abs/2509.09674)** (2025) — 在 OpenVLA-OFT 上用 GRPO 与仅"成功/失败"二值奖励做在线强化学习，并加入若干促进探索的改动；论文报告 LIBERO 成功率 99.1%、RoboTwin 1.0 为 70.4%（SFT 基线 39.8%）。 · [代码](https://github.com/PRIME-RL/SimpleVLA-RL)
- **[Steering Your Diffusion Policy with Latent Space Reinforcement Learning](https://arxiv.org/abs/2506.15799)** (2025) — DSRL：不改扩散策略的权重，而是对其输入的初始噪声做强化学习来"引导"输出动作；只需前向推理、可用于 π0，论文报告真机任务在不到 50 次在线交互内成功率从 20% 升至 90%。 · [代码](https://github.com/ajwagen/dsrl) · [项目页](https://diffusion-steering.github.io)
- **[Diffusion Policy Policy Optimization](https://arxiv.org/abs/2409.00588)** (2024) — DPPO：把去噪步骤视为 MDP 的一部分，用 PPO 微调预训练扩散策略；报告称比其他强化学习微调方法更稳定，并实现了仿真到真机迁移。 · [代码](https://github.com/irom-princeton/dppo)
- **[SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning](https://arxiv.org/abs/2401.16013)** (2024) — 在真实机械臂上用强化学习训练操作策略的开源软件栈：学习式奖励分类器、免重置训练与阻抗控制器。 · [代码](https://github.com/rail-berkeley/serl)
- **[Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning](https://arxiv.org/abs/2303.05479)** (2023) — 约束保守的离线 Q 值不低于参考策略的价值，从而避免离线预训练策略开始在线微调时常见的性能先降后升。 · [代码](https://github.com/nakamotoo/Cal-QL)
- **[Efficient Online Reinforcement Learning with Offline Data](https://arxiv.org/abs/2302.02948)** (2023) — RLPD：对离策略强化学习做几处简单改动（离线/在线数据对称采样、层归一化、集成），让已有数据加速在线学习。 · [代码](https://github.com/ikostrikov/rlpd)
- **[Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions](https://arxiv.org/abs/2309.10150)** (2023) — 将每个动作维度离散化，用 Transformer 自回归地逐维预测 Q 值，并加入保守正则；在混合演示与自主采集数据的大规模真实机器人数据集上离线训练。
- **[Behavior Transformers: Cloning $k$ modes with one stone](https://arxiv.org/abs/2206.11251)** (2022) — BeT：把动作聚成 k 个类别再加连续偏移，让 Transformer 能模仿多模态示教，而不是把不同模式平均掉。 · [代码](https://github.com/notmahi/bet)
- **[Decision Transformer: Reinforcement Learning via Sequence Modeling](https://arxiv.org/abs/2106.01345)** (2021) — 把强化学习改写成序列建模：GPT 式模型以期望回报为条件预测动作；是 Transformer 与控制结合的早期代表。 · [代码](https://github.com/kzl/decision-transformer)
- **[Implicit Behavioral Cloning](https://arxiv.org/abs/2109.00137)** (2021) — 用基于能量的模型（而非直接回归）表示策略，更好地处理多模态、不连续的示范数据。
- **[Mastering Visual Continuous Control: Improved Data-Augmented Reinforcement Learning](https://arxiv.org/abs/2107.09645)** (2021) — DrQ-v2：带图像增强的简单无模型 actor-critic，单 GPU 即可从像素学习连续控制（包括 DeepMind Control Suite 的人形任务），是常用的视觉强化学习基线。 · [代码](https://github.com/facebookresearch/drqv2)
- **[Offline Reinforcement Learning with Implicit Q-Learning](https://arxiv.org/abs/2110.06169)** (2021) — IQL：用期望分位数回归学习价值函数、从不查询数据集外的动作，再用优势加权回归提取策略；是机器人离线到在线强化学习的常用基础。 · [代码](https://github.com/ikostrikov/implicit_q_learning)
- **[What Matters in Learning from Offline Human Demonstrations for Robot Manipulation](https://arxiv.org/abs/2108.03298)** (2021) — robomimic：在人类采集的操作示教数据上系统比较模仿学习与离线强化学习（示教质量、观测选择、带历史的行为克隆），并开源框架与数据集。 · [代码](https://github.com/ARISE-Initiative/robomimic)
- **[AWAC: Accelerating Online Reinforcement Learning with Offline Datasets](https://arxiv.org/abs/2006.09359)** (2020) — 优势加权的 Actor-Critic：先用已有示范数据预训练，再在线持续提升，并在真实灵巧手任务上验证。
- **[Conservative Q-Learning for Offline Reinforcement Learning](https://arxiv.org/abs/2006.04779)** (2020) — CQL：压低数据集外动作的 Q 值，使学到的价值成为下界；是从固定机器人日志中学习的标准离线强化学习基线。 · [代码](https://github.com/aviralkumar2907/CQL)
- **[Addressing Function Approximation Error in Actor-Critic Methods](https://arxiv.org/abs/1802.09477)** (2018) — TD3：通过双 Critic、延迟策略更新和目标策略平滑解决 DDPG 的价值高估问题，至今仍是连续控制的常用基线。 · [代码](https://github.com/sfujim/TD3)
- **[QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation](https://arxiv.org/abs/1806.10293)** (2018) — 使用交叉熵方法优化动作的离策略 Q 学习，在机器人集群采集的数十万次真实抓取上训练；报告对未见物体的抓取成功率为 96%。
- **[Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://arxiv.org/abs/1801.01290)** (2018) — 带熵奖励的离策略强化学习；样本效率较高，成为真机上直接学习的常用默认算法。
- **[Generative Adversarial Imitation Learning](https://arxiv.org/abs/1606.03476)** (2016) — GAIL：训练策略使判别器无法区分其状态-动作分布与专家数据，无需显式恢复奖励函数。
- **[A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://arxiv.org/abs/1011.0686)** (2010) — DAgger：在学习者自己访问到的状态上向专家查询标注，解决单纯行为克隆的误差累积问题。
- _另见:_ [UniVLA](#vla), [When One Step Is Enough](#vla), [MorphAct](#vla), [π\*0.6](#vla), [Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers](#vla), [Latent Action Pretraining from Videos](#vla), [Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates](#vla), [Learn the Task, Not the Schedule](#manipulation), [DONIC](#manipulation), [EgoMimic](#manipulation), [COWBOY](#manipulation), [Tactile Gym 2.0](#tactile), [Making Sense of Vision and Touch](#tactile), [Reactive Diffusion Policy](#tactile), [Unitree RL Gym](#locomotion), [SuperMimic](#locomotion), [AMP](#locomotion), [DreamGen](#world-models), [PIRLNav](#navigation), [Brax](#sim), [dm_control](#sim), [RoboNet](#datasets), [RoboValue](#datasets), [FLORA](#datasets), [AirExo-2](#hardware)

<a id="sim"></a>
### 仿真与 Sim-to-Real

_物理仿真器、GPU 并行训练与向真实机器人迁移。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/sim.html)

- ⭐ **[MuJoCo](https://mujoco.org/)** (2012) — 快速准确的接触物理仿真，机器人学习研究的默认仿真器，由 DeepMind 开源。 · [代码](https://github.com/google-deepmind/mujoco)
- **[Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training](https://arxiv.org/abs/2610.19479)** (2026) — MetaGenSim 利用来自真实世界表现的元梯度，学习应该生成哪些仿真数据，而不是对仿真器做均匀采样。 · [项目页](https://meta-gensim.github.io)
- **[HyperDrone: Simulation-to-Reality Transfer at Millions of Frames per Second](https://arxiv.org/abs/2610.28950)** (2026) — 以 GPU 批量渲染为核心的四旋翼仿真器；报告比现有批量四旋翼仿真器快 20 倍以上，新的光线追踪引擎（支持 OptiX、Vulkan、Metal、WebGPU）可渲染 RGB、深度、分割、法向和光流（CoRL 2026）。
- **[MARE: An Open-Source Lunar Rover Simulator with Shadow Ground Truth for Perception and Autonomy](https://arxiv.org/abs/2610.28465)** (2026) — 基于 Unreal Engine 5 与 ROS 2 的开源月球车仿真：可生成带陨石坑的地形，两台月球车配备双目、激光雷达、事件相机与 SPAD 相机，提供极区低太阳角下像素级的阴影真值，并附 GNC 导航控制栈。 · [代码](https://github.com/raulcastar/MARE-Lunar-Simulator)
- **[SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning](https://arxiv.org/abs/2610.32978)** (2026) — 先用扩散先验在功能分区内采样家具布局，再“编译”为无碰撞、可直接仿真的 3D 场景；论文报告在其场景中训练的物体导航策略，在留出的真实扫描场景上优于用等量真实扫描训练的策略。 · [代码](https://github.com/Tinaliu0123/scenebloom)
- **[GenManip: LLM-driven Simulation for Generalizable Instruction-Following Manipulation](https://arxiv.org/abs/2506.10966)** (2025) — 基于 Isaac Sim 的平台：LLM 依据任务导向场景图，从约 1 万个物体中生成任务与布局；其 200 个场景的基准发现，结合基础模型的模块化系统比端到端策略泛化更好。 · [代码](https://github.com/InternRobotics/GenManip)
- **[Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning](https://arxiv.org/abs/2511.04831)** (2025) — Isaac Lab（Orbit 的后继）的正式论文：GPU 并行的物理、渲染与传感器仿真，内置机器人与任务，面向强化学习和模仿学习。 · [代码](https://github.com/isaac-sim/IsaacLab)
- **[MuJoCo Playground](https://arxiv.org/abs/2502.08844)** (2025) — 基于 MJX 的 GPU 加速运动与操作环境，几分钟即可训练并迁移到真实机器人。 · [代码](https://github.com/google-deepmind/mujoco_playground)
- **[Newton](https://github.com/newton-physics/newton)** (2025) — 基于 NVIDIA Warp 和 OpenUSD 的开源 GPU 物理引擎，支持多种求解器，面向接触丰富的机器人学习；由 Disney Research、Google DeepMind 和 NVIDIA 联合开发，由 Linux 基金会托管。
- **[RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://arxiv.org/abs/2506.18088)** (2025) — 用多模态大模型自动生成并校验任务代码，在强域随机化（杂物、光照、背景、指令）下批量产出双臂演示数据的仿真管线，同时提供 50 个双臂任务的基准。 · [代码](https://github.com/RoboTwin-Platform/RoboTwin)
- **[DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](https://arxiv.org/abs/2410.24185)** (2024) — 把 MimicGen 扩展到双灵巧手人形机器人，从 60 条人类演示生成 2.1 万条双臂仿真演示，并给出在真实分拣罐子任务上验证的 real-to-sim-to-real 流程。 · [代码](https://github.com/NVlabs/dexmimicgen) · [项目页](https://dexmimicgen.github.io/)
- **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** (2024) — 开源、Python 原生的物理平台，覆盖刚体、软体、流体，支持高速 GPU 仿真。
- **[Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](https://arxiv.org/abs/2404.05695)** (2024) — 基于 Isaac Gym 的人形机器人运动强化学习框架，先在 MuJoCo 中做 sim2sim 验证，再零样本部署到真实人形机器人，是人形 RL 的常用起点。 · [代码](https://github.com/roboterax/humanoid-gym)
- **[ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI](https://arxiv.org/abs/2410.00425)** (2024) — GPU 并行仿真与渲染，内置大量操作任务，适合快速视觉强化学习与数据生成。 · [代码](https://github.com/haosulab/ManiSkill)
- **[RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)** (2024) — 120 个厨房场景、2500 多个物体与 100 个任务，并附生成演示，用于训练通用策略。 · [代码](https://github.com/robocasa/robocasa)
- **[Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots](https://arxiv.org/abs/2310.13724)** (2023) — 为 Habitat 加入仿真人形化身和真人在环交互接口，可在与人协作的任务（如社交导航、社交重排）上训练和评测机器人。 · [代码](https://github.com/facebookresearch/habitat-lab)
- **[MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](https://arxiv.org/abs/2310.17596)** (2023) — 把少量人类演示切分为以物体为中心的片段，并在新场景中变换重放，从而扩增为数千条演示；被广泛用于扩充模仿学习数据。 · [代码](https://github.com/NVlabs/mimicgen)
- **[Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments](https://arxiv.org/abs/2301.04195)** (2023) — Isaac Lab 的前身，在 Isaac Sim 之上提供模块化的机器人、传感器与任务。 · [代码](https://github.com/isaac-sim/IsaacLab)
- **[BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation](https://arxiv.org/abs/2403.09227)** (2022) — 依据人们希望机器人做什么的调查挑选出 1000 项家务活动，用逻辑语言定义，并在具备真实物理与渲染的 OmniGibson 中仿真。 · [代码](https://github.com/StanfordVL/BEHAVIOR-1K)
- **[Brax: A Differentiable Physics Engine for Large Scale Rigid Body Simulation](https://arxiv.org/abs/2106.13281)** (2021) — 基于 JAX 的物理引擎，在 GPU/TPU 上与强化学习训练循环一起并行运行数千个环境，把运动控制训练从数小时缩短到数分钟。 · [代码](https://github.com/google/brax)
- **[Habitat 2.0: Training Home Assistants to Rearrange their Habitat](https://arxiv.org/abs/2106.14405)** (2021) — 为 Habitat 加入快速刚体物理与可交互公寓数据集 ReplicaCAD，并提出面向移动操作机器人的家居物品重排基准。
- **[Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning](https://arxiv.org/abs/2108.10470)** (2021) — 物理仿真与策略全程在 GPU 上运行，单卡即可并行数千个环境。
- **[SAPIEN: A SimulAted Part-based Interactive ENvironment](https://arxiv.org/abs/2003.08515)** (2020) — 包含大规模铰接物体（PartNet-Mobility）的仿真器，适合开抽屉等交互任务。
- **[SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation](https://arxiv.org/abs/2011.07215)** (2020) — 开源、Gym 接口的可变形物体操作基准（布料、绳子、液体等）；实验表明高维且部分可观测的状态让这类任务对常规强化学习方法很困难。 · [代码](https://github.com/Xingyu-Lin/softgym) · [项目页](https://sites.google.com/view/softgym)
- **[dm_control: Software and Tasks for Continuous Control](https://arxiv.org/abs/2006.12983)** (2020) — DeepMind 基于 MuJoCo 的 Python 工具栈：底层绑定、用于程序化建模与编写任务的 PyMJCF 和 Composer、作为标准基准的 Control Suite，以及运动控制和机械臂拼积木操作任务。 · [代码](https://github.com/google-deepmind/dm_control)
- **[robosuite: A Modular Simulation Framework and Benchmark for Robot Learning](https://arxiv.org/abs/2009.12293)** (2020) — 基于 MuJoCo 的模块化操作环境，是众多模仿学习基准的底座。 · [代码](https://github.com/ARISE-Initiative/robosuite)
- **[AI2-THOR: An Interactive 3D Environment for Visual AI](https://arxiv.org/abs/1712.05474)** (2017) — 具有可交互物体的逼真室内场景，智能体可开关、拾取和改变物体，是 ALFRED 等众多具身智能基准的基础。 · [代码](https://github.com/allenai/ai2thor)
- **[Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://arxiv.org/abs/1703.06907)** (2017) — 在仿真中随机化纹理、光照和相机，使视觉模型无需真实数据即可在真实图像上工作。
- **[Sim-to-Real Transfer of Robotic Control with Dynamics Randomization](https://arxiv.org/abs/1710.06537)** (2017) — 训练中随机化物理参数，得到足以在真实机械臂上运行的鲁棒控制策略。
- **[Gazebo](https://gazebosim.org/)** (2004) — ROS 生态中历史悠久的开源机器人仿真器，提供传感器、插件与 ROS 2 集成；通常用于测试完整的机器人软件栈，而非训练策略。 · [代码](https://github.com/gazebosim/gz-sim)
- _另见:_ [Aligning Cyber Space with Physical World](#vla), [GraspVLA](#vla), [Blind Precise Assembly](#manipulation), [TACTO](#tactile), [Taxim](#tactile), [Tactile Gym 2.0](#tactile), [TacSL](#tactile), [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](#locomotion), [Genie Envisioner](#world-models), [Drake](#control), [Habitat](#datasets), [RoboCasa-Shift](#datasets), [Habitat-Matterport 3D Dataset (HM3D)](#datasets), [Objaverse](#datasets), [HumanoidBench](#datasets), [RoboVerse](#datasets), [HandsOn](#datasets), [AstroBench](#datasets)

<a id="datasets"></a>
### 数据集与基准

_大规模机器人数据集、第一视角数据与评测基准。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/datasets.html)

- ⭐ **[LeRobot](https://github.com/huggingface/lerobot)** (2024) — PyTorch 机器人学习库，提供数据集、预训练策略（ACT、Diffusion、SmolVLA）与低成本机械臂驱动。
- ⭐ **[LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)** (2023) — 四个套件共 130 个语言条件任务，现已成为 VLA 论文最常用的仿真基准。 · [代码](https://github.com/Lifelong-Robot-Learning/LIBERO)
- ⭐ **[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)** (2023) — 30 多个实验室汇集 22 种机器人的 100 多万条轨迹；在其上训练的 RT-X 优于单机器人基线。 · [代码](https://github.com/google-deepmind/open_x_embodiment)
- **[AstroBench: Benchmarking Free-Floating Capture and Space Robotic Manipulation](https://arxiv.org/abs/2610.31064)** (2026) — 太空机器人操作基准：用固定基座机械臂抓取舱内漂浮、旋转的物体，另含样本存储与在轨维护任务。报告称所测的冻结通用策略在 200 个静止目标中只抓住 2 个。 · [代码](https://github.com/AstroUpLab/AstroBench) · [项目页](https://astroup.com/astrobench/)
- **[BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks](https://arxiv.org/abs/2610.25459)** (2026) — 双灵巧手仿真基准：106 个任务按泛化、指令遵循、少示教、长时程、记忆五个维度组织，每个任务配有域外变体；提供 8,080 条遥操作示教，并在统一协议下评测了七个 VLA 模型。 · [项目页](https://BiDex-100.github.io/BiDex-100/)
- **[EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ](https://arxiv.org/abs/2610.18872)** (2026) — 用可穿戴设备采集的 100 小时人类移动操作数据，侧重职业场景，对齐第一视角视频、全身与手指动作、触觉和步骤级文字描述；其补全全身动作的方法报告身体关键点误差比最强基线低 71.9%。 · [代码](https://github.com/InternRobotics/EgoExplorer) · [项目页](https://internrobotics.github.io/egoexplorer.github.io/)
- **[Embodied Skill Bench: Benchmarking How Well Agents with Embodied Skills Perform on Physical Tasks](https://arxiv.org/abs/2610.16238)** (2026) — 将 VLA 策略、感知模型与经验知识封装成 250 个可复用的“具身技能”，评测它们对大模型智能体完成物理任务的帮助。 · [代码](https://github.com/HanZhi306/EmbodiedSkill-Bench)
- **[FLORA: An Open Model Suite for Scaling Robotics Data Engines](https://arxiv.org/abs/2610.31779)** (2026) — GR00T 训练所用的开放数据引擎：一组模型为人类与机器人视频生成带时间戳的动作描述、稠密过程奖励和整段结果奖励；报告在 WGO-Bench、RoboReward 与 Robometer 上达到最优。 · [项目页](https://research.nvidia.com/labs/gear/flora)
- **[HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation](https://arxiv.org/abs/2610.26765)** (2026) — 基于 Isaac Sim 的灵巧操作基准：5 种机械臂、6 种灵巧手、约 200 个资产、1.8 万条人类演示、66 个任务；报告最好的训练策略（一种世界动作模型）在 Core-50 上仅 29.1%，精密装配和柔性物体任务接近 0%。 · [代码](https://github.com/TsinghuaC3I/HandsOn)
- **[LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints](https://arxiv.org/abs/2610.16782)** (2026) — 基于 LIBERO 的 216 个工业约束任务：传送带上料、下料与转运，可调节物体形状、带速、交互时间窗与公差；报告 VLA 和世界动作模型在多重约束叠加时性能逐步下降。 · [代码](https://github.com/IAIE-PhysicalAI/LIBERO-Industry) · [项目页](https://iaie-physicalai.github.io/LIBERO-Industry/)
- **[RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861)** (2026) — 基于 RoboCasa365 的 VLA 鲁棒性诊断基准：成对比较只差一个分布偏移因素的干净/扰动执行，并定位长时序任务中失败从哪个阶段开始，而不只看总成功率；在 GR00T N1.5 上评测。 · [代码](https://github.com/HaochengWang23/RoboCasa-Shift)
- **[RoboValue: A Fine-Grained Sim-and-Real Benchmark for Unified Evaluation of Robotic Value Models](https://arxiv.org/abs/2610.26663)** (2026) — 在 15 个仿真和 20 个真实任务上评测机器人价值（进度）模型，覆盖任务状态、进度监测、失败与恢复、一致性四个维度；报告称前向进度得分高的模型在依赖历史和恢复判断上仍然薄弱。 · [代码](https://github.com/RoboValue-Benchmark/RoboValue) · [项目页](https://robovalue-benchmark.github.io/)
- **[AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://arxiv.org/abs/2503.06669)** (2025) — 在专门搭建的场景中采集的百万级真实机器人数据集，并基于其训练通用策略 GO-1。
- **[EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video](https://arxiv.org/abs/2505.11709)** (2025) — 用 Apple Vision Pro 采集的 829 小时第一视角视频，配有每个手部关节的三维姿态，覆盖从系鞋带到叠衣服的 194 种桌面任务，并提供手部轨迹预测基准。 · [代码](https://github.com/apple-aiml-research/ml-egodex)
- **[RoboVerse: Towards a Unified Platform, Dataset and Benchmark for Scalable and Generalizable Robot Learning](https://arxiv.org/abs/2504.18904)** (2025) — MetaSim 用统一接口封装多种仿真器（Isaac Sim/Gym、MuJoCo、Genesis、SAPIEN、PyBullet 等）；提供由公开基准迁移而来的大规模合成数据集，以及按泛化层级划分的统一模仿学习/强化学习基准。 · [代码](https://github.com/RoboVerseOrg/RoboVerse) · [项目页](https://roboverseorg.github.io/)
- **[DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://arxiv.org/abs/2403.12945)** (2024) — 由多家机构在数百个真实场景中采集的 7.6 万条 Franka 遥操作轨迹。 · [代码](https://github.com/droid-dataset/droid)
- **[Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941)** (2024) — SimplerEnv：真实到仿真的评测环境，其得分与 RT-1/Octo 类策略的真机表现相关。 · [代码](https://github.com/simpler-env/SimplerEnv)
- **[HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation](https://arxiv.org/abs/2403.10506)** (2024) — 27 个仿真任务（12 个运动、15 个全身操作），机器人为带两只灵巧手的 Unitree H1；报告 DreamerV3、TD-MPC2、SAC、PPO 在大多数任务上未达标，长时程全身协调任务尤甚。 · [代码](https://github.com/carlosferrazza/humanoid-bench) · [项目页](https://humanoid-bench.github.io)
- **[RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation](https://arxiv.org/abs/2412.13877)** (2024) — 在统一规范下采集的大规模真机遥操作数据集，覆盖单臂、双臂与人形等多种本体，并保留了标注失败原因的失败演示。 · [项目页](https://x-humanoid-robomind.github.io/)
- **[THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](https://arxiv.org/abs/2402.08191)** (2024) — 20 个 RLBench 任务 × 14 种扰动因素（颜色、纹理、光照、干扰物、相机位姿、摩擦、质量……）；报告主流策略成功率下降 30–50%，多种扰动叠加时下降 75% 以上。 · [代码](https://github.com/robot-colosseum/robot-colosseum) · [项目页](https://robot-colosseum.github.io)
- **[VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://arxiv.org/abs/2412.18194)** (2024) — 100 类任务、2000 多个物体，任务需要常识、世界知识与多步推理，而不只是照指令执行；在同一套件中评测 VLA、具身智能体与 VLM。 · [代码](https://github.com/OpenMOSS/VLABench) · [项目页](https://vlabench.github.io/)
- **[BridgeData V2: A Dataset for Robot Learning at Scale](https://arxiv.org/abs/2308.12952)** (2023) — 在低成本 WidowX 机械臂上采集、涵盖众多厨房与任务的 6 万条轨迹，常用作预训练数据。
- **[Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives](https://arxiv.org/abs/2311.18259)** (2023) — 人们进行技能活动（烹饪、运动、维修等）时同步采集的第一人称与第三人称视频，附丰富标注，是从人类视频学习操作技能的重要数据来源。
- **[RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot](https://arxiv.org/abs/2307.00595)** (2023) — 11 万多条接触丰富的序列，包含视觉、力、音频及配对的人类演示视频。
- **[ARCTIC: A Dataset for Dexterous Bimanual Hand-Object Manipulation](https://arxiv.org/abs/2204.13662)** (2022) — 210 万帧双手操作铰接物体（剪刀、笔记本电脑等）的视频，借助动作捕捉提供精确的手与物体三维网格；双手-物体重建的常用基准。 · [代码](https://github.com/zc-alexfan/arctic)
- **[HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction](https://arxiv.org/abs/2203.01577)** (2022) — 240 万帧第一视角 RGB-D（4000 多段序列、16 类 800 个物体实例、610 个房间），记录人操作刚体与铰接物体，带分割、手部与物体位姿标注。 · [代码](https://github.com/leolyliu/HOI4D-Instructions)
- **[OakInk: A Large-scale Knowledge Repository for Understanding Hand-Object Interaction](https://arxiv.org/abs/2203.15709)** (2022) — 为约 1800 个日常物体标注可供性，并在其中 100 个物体上记录 5 万次带意图的手-物交互；常用于灵巧抓取生成。后续 OakInk2 扩展到双手任务。 · [代码](https://github.com/oakink/OakInk)
- **[Objaverse: A Universe of Annotated 3D Objects](https://arxiv.org/abs/2212.08051)** (2022) — 80 万+ 带标注的 3D 物体模型，常用于为仿真器填充多样物体，用于抓取、重排和程序化场景生成（Objaverse-XL 扩展到 1000 万+）。
- **[CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](https://arxiv.org/abs/2112.03227)** (2021) — 连续执行五条语言指令，测试长时程、语言条件下的控制能力。 · [代码](https://github.com/mees/calvin)
- **[DexYCB: A Benchmark for Capturing Hand Grasping of Objects](https://arxiv.org/abs/2104.04631)** (2021) — 约 58.2 万帧 RGB-D（1000 段序列、10 人、20 个 YCB 物体、8 台相机）的人手抓取数据，带手部与物体位姿标注；评测检测、物体 6D 位姿、三维手部姿态及人到机器人的物体交接。 · [代码](https://github.com/NVlabs/dex-ycb-toolkit)
- **[Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058)** (2021) — 3670 小时第一视角日常生活视频，广泛用于为机器人预训练视觉表征。
- **[Habitat-Matterport 3D Dataset (HM3D): 1000 Large-scale 3D Environments for Embodied AI](https://arxiv.org/abs/2109.08238)** (2021) — 1000 个真实室内空间的 3D 扫描，供 Habitat 使用；ObjectNav 等众多具身导航基准的主要场景集。 · [代码](https://github.com/facebookresearch/habitat-matterport3d-dataset)
- **[Rescaling Egocentric Vision](https://arxiv.org/abs/2006.13256)** (2020) — EPIC-KITCHENS-100：来自 45 个厨房环境、100 小时（2000 万帧、约 9 万个动作片段）的非脚本第一视角视频，动作标注密集，并设有动作预测等挑战任务。 · [代码](https://github.com/epic-kitchens/epic-kitchens-100-annotations)
- **[Habitat: A Platform for Embodied AI Research](https://arxiv.org/abs/1904.01201)** (2019) — 极速的逼真 3D 仿真器与任务集，统一了具身导航研究的标准。 · [代码](https://github.com/facebookresearch/habitat-sim)
- **[Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning](https://arxiv.org/abs/1910.10897)** (2019) — 50 个 Sawyer 操作任务，用于多任务与元强化学习评测。 · [代码](https://github.com/Farama-Foundation/Metaworld)
- **[RLBench: The Robot Learning Benchmark & Learning Environment](https://arxiv.org/abs/1909.12271)** (2019) — 100 个手工设计的操作任务并附演示，是 PerAct 等 3D 策略方法的常用基准。 · [代码](https://github.com/stepjam/RLBench)
- **[RoboNet: Large-Scale Multi-Robot Learning](https://arxiv.org/abs/1910.11215)** (2019) — 早期的共享机器人交互视频数据集，涵盖七种机器人平台，用于预训练可迁移到新机器人的视觉动力学模型，是 Open X-Embodiment 的先驱。 · [代码](https://github.com/SudeepDasari/RoboNet)
- **[ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes](https://arxiv.org/abs/1702.04405)** (2017) — 1500+ 个室内场景的 RGB-D 扫描，含三维重建、相机位姿与语义标注；具身感知所依赖的三维场景理解标准基准。 · [代码](https://github.com/ScanNet/ScanNet)
- **[Benchmarking in Manipulation Research: The YCB Object and Model Set and Benchmarking Protocols](https://arxiv.org/abs/1502.03143)** (2015) — YCB 物体集：73 个日常物体，附扫描数据、带纹理网格与仿真模型，以及基准测试规程；被抓取与位姿估计研究广泛使用。
- _另见:_ [Galaxea Open-World Dataset and G0 Dual-System VLA Model](#vla), [Universal Manipulation Interface](#manipulation), [DexGraspNet](#manipulation), [DONIC](#manipulation), [ContactBench 1.0](#manipulation), [A Touch, Vision, and Language Dataset for Multimodal Alignment](#tactile), [$λ_0$](#locomotion), [Vision-and-Language Navigation](#navigation), [Beyond the Nav-Graph](#navigation), [TARSphere](#navigation), [EmbodiedWorld-200K](#navigation), [safe-control-gym](#control), [What Matters in Learning from Offline Human Demonstrations for Robot Manipulation](#learning), [Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy](#learning), [robosuite](#sim), [RoboCasa](#sim), [RoboTwin 2.0](#sim), [MimicGen](#sim), [BEHAVIOR-1K](#sim), [DexMimicGen](#sim), [GenManip](#sim), [DexPort](#hardware)

<a id="hardware"></a>
### 硬件与开源机器人

_可自行搭建的低成本机械臂、灵巧手、夹爪与数据采集设备。_ [在网站上查看与最新论文 →](https://hu-zlatan.github.io/embodied-ai-radar/topics/hardware.html)

- ⭐ **[LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning](https://arxiv.org/abs/2309.06440)** (2023) — 16 自由度灵巧手，用现成零件约 2000 美元即可搭建。 · [项目页](https://leaphand.com/)
- **[DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection](https://arxiv.org/abs/2610.32969)** (2026) — 便携手持式数据采集装置，面向高自由度机器人灵巧手；采集与部署使用同一只机械手，无需从人手动作重定向，也无需搭建完整机器人系统。 · [项目页](https://amberxie88.github.io/dexport/)
- **[PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits](https://arxiv.org/abs/2610.29030)** (2026) — 完全连杆驱动的人形灵巧手，每根手指 3 个主动自由度；用柔性铰链和弹簧钢驱动杆取代大量微型零件，可用入门级 3D 打印机制造，尺寸接近真人手。
- **[AirExo-2: Scaling up Generalizable Robotic Imitation Learning with Low-Cost Exoskeletons](https://arxiv.org/abs/2503.03081)** (2025) — 将外骨骼示教转换为“伪机器人”示教；论文报告仅用这些数据（无任何机器人数据）训练的 RISE-2 策略，效果与用遥操作机器人数据训练的策略相当。 · [代码](https://github.com/AirExo/AirExo-2)
- **[BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities](https://arxiv.org/abs/2503.05652)** (2025) — 面向轮式双臂机器人的全身遥操作接口与学习方法，用于需要伸展、平衡与导航的长程家务任务。 · [项目页](https://behavior-robot-suite.github.io/)
- **[DOGlove: Dexterous Manipulation with a Low-Cost Open-Source Haptic Force Feedback Glove](https://arxiv.org/abs/2502.07730)** (2025) — 开源遥操作手套，几小时即可组装、成本低于 600 美元：21 自由度手部动捕、5 自由度绳驱力反馈和指尖振动触觉；报告在无视觉输入时力/触觉反馈对接触密集任务至关重要，采集数据可训练模仿学习策略。 · [代码](https://github.com/TEA-Lab/DOGlove) · [项目页](https://do-glove.github.io/)
- **[Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot](https://arxiv.org/abs/2504.17249)** (2025) — 开源人形机器人，采用 3D 打印的模块化减速器，在美国可用不到 5000 美元搭建；硬件设计、嵌入式代码与训练框架均已开源。 · [代码](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite) · [项目页](https://lite.berkeley-humanoid.org)
- **[DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation](https://arxiv.org/abs/2505.21864)** (2025) — DexUMI：按目标机器人手的指尖工作空间设计的可穿戴手部外骨骼，再用视频修补把画面中的人手换成机器人手；论文报告在 Inspire 与 XHand 上平均成功率 86%，采集效率约为遥操作的 3.2 倍。 · [代码](https://github.com/real-stanford/DexUMI) · [项目页](https://dex-umi.github.io/)
- **[HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit](https://arxiv.org/abs/2502.13013)** (2025) — 开源的人形机器人全身遥操作系统：手臂外骨骼加动作捕捉手套，脚踏板驱动强化学习行走控制器；整套座舱硬件约 500 美元。 · [项目页](https://homietele.github.io/)
- **[ORCA: An Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning](https://arxiv.org/abs/2504.04259)** (2025) — 可 3D 打印的 17 自由度腱驱动灵巧手，指尖带触觉传感，材料成本低于 2000 瑞士法郎；设计文件与代码开源，论文报告了可长时间连续运行用于遥操作与学习。 · [项目页](https://www.orcahand.com)
- **[OpenArm](https://github.com/enactic/openarm)** (2025) — 完全开源的 7 自由度人形机械臂，面向接触丰富的研究：CAD、电路、固件、ROS 2/MoveIt 2 以及 MuJoCo/Genesis 模型全部公开，支持主从力反馈遥操作与重力补偿（软件 Apache-2.0，硬件 CERN-OHL-S）。 · [项目页](https://openarm.dev)
- **[RUKA: Rethinking the Design of Humanoid Hands with Learning](https://arxiv.org/abs/2504.13165)** (2025) — 人手大小的腱驱动灵巧手（5 指、15 个欠驱动自由度），由 3D 打印件和现成零件制成；关节到电机的控制映射用 MANUS 数据手套的动捕数据学习得到，而非手工建模。 · [代码](https://github.com/ruka-hand/RUKA) · [项目页](https://ruka-hand.github.io/)
- **[ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation](https://arxiv.org/abs/2502.00893)** (2025) — 3D 打印的小型开源人形机器人，配套仿真模型，便于机器学习策略与遥操作数据迁移到真机。 · [项目页](https://toddlerbot.github.io/)
- **[ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation](https://arxiv.org/abs/2408.11805)** (2024) — ACE：3D 打印的双臂外骨骼获取手腕位姿、朝向手部的摄像头估计手指姿态（约 600 美元）；同一套设备可遥操作机械臂+灵巧手、人形机器人以及四足搭载的机械臂。 · [项目页](https://ace-teleop.github.io/)
- **[ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation](https://arxiv.org/abs/2405.02292)** (2024) — ALOHA 双臂平台的升级版（更强夹爪、重力补偿、更稳固的框架），开源硬件设计并提供 MuJoCo 仿真模型。 · [项目页](https://aloha-2.github.io/)
- **[Berkeley Humanoid: A Research Platform for Learning-based Control](https://arxiv.org/abs/2407.21781)** (2024) — 中等尺寸、低成本的人形机器人，专为强化学习运动策略的 sim-to-real 迁移设计。
- **[Bimanual Dexterity for Complex Tasks](https://arxiv.org/abs/2411.13677)** (2024) — Bidex：便携、低延迟的双臂灵巧手遥操作系统（动捕手套 + 示教臂），可控制 50+ 自由度的机器人；论文报告其采集的数据质量和速度均优于 Vision Pro 与 SteamVR 遥操作。 · [项目页](https://bidex-teleop.github.io/)
- **[Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning](https://arxiv.org/abs/2407.03162)** (2024) — 用 Apple Vision Pro 实时遥操作双灵巧手，带实时重定向、碰撞与奇异点规避，并为操作者提供低成本振动触觉反馈。 · [代码](https://github.com/Dingry/BunnyVisionPro)
- **[Learning Visuotactile Skills with Two Multifingered Hands](https://arxiv.org/abs/2404.16823)** (2024) — HATO：用两台 UR5e 机械臂和改装的假肢手（指尖带触觉传感器）搭建双臂系统，用 VR 遥操作采集数据，并训练视觉-触觉策略完成倒酒、交接等任务。 · [代码](https://github.com/ToruOwO/hato) · [项目页](https://toruowo.github.io/hato/)
- **[Open-TeleVision: Teleoperation with Immersive Active Visual Feedback](https://arxiv.org/abs/2407.01512)** (2024) — 带主动转向立体相机的 VR 遥操作系统，用于采集人形机器人操作数据。 · [代码](https://github.com/OpenTeleVision/TeleVision)
- **[SO-ARM100 / SO-101](https://github.com/TheRobotStudio/SO-ARM100)** (2024) — 开源 3D 打印 6 自由度机械臂（主从臂），每只约 100–200 美元，是 LeRobot 的默认入门套件。
- **[TeleMoMa: A Modular and Versatile Teleoperation System for Mobile Manipulation](https://arxiv.org/abs/2403.07869)** (2024) — 模块化遥操作接口，可组合 RGB-D 人体追踪、VR 手柄、键盘与摇杆，控制 Tiago++、HSR、Fetch 等移动操作机器人做全身动作，仿真和真机都支持。 · [代码](https://github.com/UT-Austin-RobIn/telemoma) · [项目页](https://robin-lab.cs.utexas.edu/telemoma-web/)
- **[TidyBot++: An Open-Source Holonomic Mobile Manipulator for Robot Learning](https://arxiv.org/abs/2412.10447)** (2024) — 低成本开源移动底盘，采用主动脚轮实现全向（完整约束）运动，可搭载任意机械臂，并配有手机遥操作界面，方便为模仿学习采集移动操作示教数据。 · [代码](https://github.com/jimmyyhwu/tidybot2)
- **[UMI-on-Legs: Making Manipulation Policies Mobile with Manipulation-Centric Whole-body Controllers](https://arxiv.org/abs/2407.10353)** (2024) — 用手持 UMI 夹爪采集无需机器人的示教来训练操作策略，再由仿真训练的全身控制器在四足机器人上跟踪其输出的末端轨迹；报告所有任务成功率超过 70%，并能零样本复用原为固定机械臂训练的策略。 · [代码](https://github.com/real-stanford/umi-on-legs)
- **[AirExo: Low-Cost Exoskeletons for Learning Whole-Arm Manipulation in the Wild](https://arxiv.org/abs/2309.14975)** (2023) — 便携式双臂外骨骼（论文称零件成本约 600 美元），可做关节级遥操作并低成本采集野外示教；报告称少量遥操作数据加野外数据即可达到甚至超过长时间纯遥操作训练的效果。 · [代码](https://github.com/AirExo/collector)
- **[AnyTeleop: A General Vision-Based Dexterous Robot Arm-Hand Teleoperation System](https://arxiv.org/abs/2307.04577)** (2023) — 仅用相机即可遥操作"机械臂 + 灵巧手"：跟踪操作者手部并重定向到多种不同的机器人手，可用于仿真或真机。
- **[GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators](https://arxiv.org/abs/2309.13037)** (2023) — 3D 打印的机械臂运动学复刻件，实现低成本、直观的关节空间遥操作。 · [代码](https://github.com/wuphilipp/gello_software)
- **[The Design of Stretch: A Compact, Lightweight Mobile Manipulator for Indoor Human Environments](https://arxiv.org/abs/2109.10892)** (2021) — Hello Robot 的 Stretch 设计：在升降柱上装伸缩臂的轻巧移动操作机器人，面向家庭环境，被大量家庭机器人研究采用。
- **[An Open Torque-Controlled Modular Robot Architecture for Legged Locomotion Research](https://arxiv.org/abs/1910.00093)** (2019) — 开源四足机器人 Solo 及其模块化力矩控制关节，采用现成件和 3D 打印件，便于各实验室复现动态腿式机器人。 · [代码](https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware)
- _另见:_ [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](#manipulation), [Mobile ALOHA](#manipulation), [Universal Manipulation Interface](#manipulation), [DexCap](#manipulation), [DIGIT](#tactile), [AnySkin](#tactile), [ReSkin](#tactile), [Digitizing Touch with an Artificial Multimodal Fingertip](#tactile), [GelSlim 3.0](#tactile), [DTact](#tactile), [9DTact](#tactile), [OpenTac](#tactile), [VecTile](#tactile), [Unitree RL Gym](#locomotion), [LeRobot](#datasets)

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
