# 触觉与视触觉感知

_触觉传感器、触觉表征与接触丰富的控制。_

共 52 条，⭐ 为重点推荐。由 [`data/curated/tactile.yaml`](../data/curated/tactile.yaml) 生成，请勿直接编辑。

[返回 README](../README.zh-CN.md) · [在网站上查看](https://hu-zlatan.github.io/embodied-ai-radar/topics/tactile.html) · [English](tactile.md)

[VLA 与机器人基础模型](vla.zh-CN.md) · [操作与灵巧手](manipulation.zh-CN.md) · **触觉与视触觉感知** · [运动控制与人形机器人](locomotion.zh-CN.md) · [世界模型](world-models.zh-CN.md) · [导航与具身智能体](navigation.zh-CN.md) · [感知、SLAM 与三维建图](perception.zh-CN.md) · [规划、控制与安全](control.zh-CN.md) · [机器人学习：强化学习与模仿学习](learning.zh-CN.md) · [仿真与 Sim-to-Real](sim.zh-CN.md) · [数据集与基准](datasets.zh-CN.md) · [硬件与开源机器人](hardware.zh-CN.md)

- ⭐ **[DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](https://arxiv.org/abs/2005.14679)** (2020) — 低成本、紧凑的 GelSight 式指尖传感器，让视触觉传感器得以普及。 · [代码](https://github.com/facebookresearch/digit-interface)
- **[$TF^2$-Steering: Action Refinement with Tactile Forecasts and Feedback via Velocity-Field Steering](https://arxiv.org/abs/2611.01483)** (2026) — 保留视觉流匹配策略，用触觉预测与实时反馈学习对其速度场的残差引导，让触觉能修正动作。报告在六个仿真和六个真实任务上优于基线。 · [项目页](https://yiming-cc.github.io/tf2-steering/)
- **[ACTS: Learning Visuo-Tactile World Models from Human Physical Interaction](https://arxiv.org/abs/2610.24285)** (2026) — 只用人手持 GelSight 传感器的交互数据（4.9 小时 React 数据集）训练视触觉世界模型。报告在机器人回放中接触动态比视觉外观更容易迁移，部分任务的相机视角预测甚至不如直接复制帧。 · [项目页](https://acts-anon.github.io/)
- **[DeTac: Dual-branch Decoupling of Texture and Force Signals in Vision-Based Tactile Sensors](https://arxiv.org/abs/2610.16463)** (2026) — CoRL 2026 Spotlight。双分支生成框架，可从单帧带标记点的触觉图像同时分离出干净的明暗图与标记图，避免串行掩码修复。
- **[Equivariant Visual-Tactile Diffusion Policy for Contact-Rich Manipulation](https://arxiv.org/abs/2610.03333)** (2026) — VISTA：等变视触觉扩散策略，把触觉融合进球面视觉 token 并随末端姿态旋转，提升富接触模仿学习的数据效率。 · [代码](https://github.com/Kenn3o3/Vista) · [项目页](https://vista-paper.github.io/)
- **[Evaluating Tactile Foundation Models for End-to-End Imitation Learning in Contact-Rich Manipulation](https://arxiv.org/abs/2611.00957)** (2026) — 把多种预训练触觉基础模型接入 Diffusion Policy，在统一设置下比较，并考察编码器微调与任务专用中训练策略，含 5000 多次真实机器人回合。 · [代码](https://github.com/isri-aist/TacLatentIL) · [项目页](https://mmurooka.github.io/tfm4il-project-page/)
- **[FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning](https://arxiv.org/abs/2606.12406)** (2026) — CoRL 2026 Oral。NEXT 无需力传感器即可估计外部关节力矩，用 10 分钟自由运动数据训练 1 分钟，为低成本机械臂带来力反馈遥操作与更好的策略学习。 · [代码](https://github.com/philiphan0109/factr2_next) · [项目页](https://jasonjzliu.com/factr2)
- **[FingerEye: Learning Dexterous Manipulation with Continuous Vision-Tactile Sensing](https://arxiv.org/abs/2604.20689)** (2026) — CoRL 2026 Spotlight。指尖传感将双目 RGB 相机与柔顺接触面结合，从接触前接近到接触后控制全程提供反馈。 · [代码](https://github.com/ariszxxu/FingerEye) · [项目页](https://nus-lins-lab.github.io/FingerEyeWeb/)
- **[GelSlim 5.0: Unifying Vision and Touch with a Single Fingertip Camera](https://arxiv.org/abs/2610.31334)** (2026) — 指尖传感器只用一个摄像头，通过切换照明交替获取“透过膜的视觉图像”和触觉图像，视觉与触觉共享同一视角、无需相机外参标定；再用 Transformer（VisTacFusion）融合两者。
- **[OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing](https://arxiv.org/abs/2610.31661)** (2026) — 开源电阻式触觉皮肤：结构化覆层把切向力转成空间压力差异，相邻触点即可解码剪切与法向力；附带可定制皮肤的设计工具，硬件和软件均开源。 · [代码](https://github.com/opentac/opentac) · [项目页](https://opentac.github.io)
- **[PACE: Temporal-Role Tactile Conditioning for Chunk-Based Insertion Policies](https://arxiv.org/abs/2610.16308)** (2026) — CoRL 2026 Oral。不再用单一融合路径，而是把同一触觉流拆成三种时序角色：持续接触状态、突发接触事件与未来接触后果，用于分块式插接策略。 · [项目页](https://pace-insertion.github.io/)
- **[PanoTac: A Dense Three-Axis Tactile Sensor for Robust Touch-Centric Manipulation](https://arxiv.org/abs/2611.03520)** (2026) — 每个成本低于 50 美元的柔顺指尖，以 60 Hz 输出 12×32 的法向与剪切稠密响应。在舀取、倾倒和试管任务上，视触觉策略平均比纯视觉基线高 46.7 个百分点。 · [项目页](https://panotac.github.io)
- **[ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control](https://arxiv.org/abs/2611.04424)** (2026) — 在学习型全身策略之下加入全身触觉反射，10 毫秒内直达电机；在 G1 上，与延迟 20 毫秒的相同反射相比，首次力峰值降低 34.1%。 · [项目页](https://minusmodulo.github.io/reflexarc-website/)
- **[TacMind: Benchmarking and Modeling Tactile Interaction States for Robotic Manipulation](https://arxiv.org/abs/2611.00455)** (2026) — 128 个仿真触觉任务，分精确、识别、动态三类，含 12 种扰动；并提出动作条件的触觉世界模型，把触觉当作随时间演化的状态，用预测的触觉信息修正动作。 · [代码](https://github.com/Tacmind-Bench/TacMind) · [项目页](https://tacmind-bench.github.io/)
- **[Tactile Curiosity Drives Robot Interaction](https://arxiv.org/abs/2609.40134)** (2026) — TacEx 让好奇心聚焦触觉：按感知模态分解模型不确定性，使探索去寻找接触而非空中乱动。采集的数据可离线训练抓放策略，也可用于 VLA 后训练。 · [项目页](https://go.klem.nz/tacex)
- **[Tactile-Based Robotic Manipulation: From Mechanics-Driven to Data-Driven Perspectives](https://arxiv.org/abs/2610.30438)** (2026) — 综述（Annual Review of Control, Robotics, and Autonomous Systems 录用稿）：从接触力学建模到数据驱动学习，梳理触觉操作的发展，涵盖传感基础、状态表征、模仿学习、强化学习、VLA 与预测模型。
- **[TactileStep: Sole Tactile Learning for Regulating Foot-Terrain Interaction in Humanoid Locomotion](https://arxiv.org/abs/2609.28959)** (2026) — CoRL 2026 Spotlight。把足底压力感知引入人形运动控制，目标是比“能完成但落地粗暴”的跑酷策略更柔和的足地接触。
- **[VecTile: A Low-Cost Flexible Tactile Array for 3-DoF Force Sensing](https://arxiv.org/abs/2610.31472)** (2026) — 6 毫米厚的柔性触觉阵列：压阻层上的硅胶凸点把切向力转成可区分的压力分布，实现每个触点的三轴力测量；4x4 阵列成本不到 35 美元。报告称其提升了扩散策略插插头任务的表现。 · [项目页](https://jiannnh.github.io/VecTile/)
- **[Visible Touch: Rendering Contact for Visuomotor Policies](https://arxiv.org/abs/2609.14156)** (2026) — CoRL 2026 Spotlight。通过渲染接触信息把触觉带入基于图像的视觉运动策略，针对现有方法需要专用触觉硬件、独立触觉编码器或非图像主干，难以与预训练 2D 视觉表征策略兼容的问题。 · [代码](https://github.com/qaz1678249/visibletouch) · [项目页](https://visibletouch.github.io/)
- **[AnyTouch: Learning Unified Static-Dynamic Representation across Multiple Visuo-tactile Sensors](https://arxiv.org/abs/2502.12191)** (2025) — 跨多种视触觉传感器学习统一的静态-动态表征，并贡献对齐的多传感器触觉数据集 TacQuad。 · [代码](https://github.com/GeWu-Lab/AnyTouch)
- **[FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning](https://arxiv.org/abs/2502.17432)** (2025) — 低成本双边遥操作把机械臂受力反馈给操作者；训练时对视觉的破坏逐渐减弱，让策略学会关注力信息。
- **[LocoTouch: Learning Dynamic Quadrupedal Transport with Tactile Sensing](https://arxiv.org/abs/2505.23175)** (2025) — 在四足机器人背部铺设高密度触觉传感器，无需固定装置即可长距离运输未固定的圆柱物体。 · [代码](https://github.com/linchangyi1/LocoTouch)
- **[PP-Tac: Paper Picking Using Tactile Feedback in Dexterous Robotic Hands](https://arxiv.org/abs/2504.16649)** (2025) — 用带高分辨率全向触觉传感器的多指手抓取纸张类薄物体，同时解决状态估计与抓取规划。
- **[Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](https://arxiv.org/abs/2503.02881)** (2025) — 慢速扩散策略在隐空间规划动作块，快速策略根据触觉/力反馈高频调整；论文报告在三个接触丰富任务上比纯视觉模仿学习基线总分高 35% 以上。 · [代码](https://github.com/xiaoxiaoxh/reactive_diffusion_policy) · [项目页](https://reactive-diffusion-policy.github.io/)
- **[Tactile Robotics: An Outlook](https://arxiv.org/abs/2508.11261)** (2025) — 对触觉机器人的综合展望，涵盖压阻、压电、电容、磁性和光学等传感方式及领域走向。
- **[3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing](https://arxiv.org/abs/2410.24091)** (2024) — 在扩散策略中融合密集触觉阵列与 3D 视觉，完成易碎、接触丰富的双臂任务。
- **[A Touch, Vision, and Language Dataset for Multimodal Alignment](https://arxiv.org/abs/2402.13232)** (2024) — TVL 数据集将触觉与视觉观测配上语言描述，并训练触觉-视觉-语言编码器以及能描述物体触感的模型。 · [代码](https://github.com/Max-Fu/tvl)
- **[AnySkin: Plug-and-play Skin Sensing for Robotic Touch](https://arxiv.org/abs/2409.08276)** (2024) — 可更换的磁性触觉皮肤，更换皮肤后训练好的策略仍能继续使用。
- **[Binding Touch to Everything: Learning Unified Multimodal Tactile Representations](https://arxiv.org/abs/2401.18084)** (2024) — UniTouch 将触觉信号与视觉、语言、音频嵌入对齐，实现零样本触觉理解。
- **[Digitizing Touch with an Artificial Multimodal Fingertip](https://arxiv.org/abs/2411.02479)** (2024) — Digit 360：开放设计的指尖形触觉传感器，可感知力、细微纹理、振动和温度，并用板载神经网络加速器做类似反射弧的本地处理。 · [代码](https://github.com/facebookresearch/digit360)
- **[ManiWAV: Learning Robot Manipulation from In-the-Wild Audio-Visual Data](https://arxiv.org/abs/2406.19464)** (2024) — “手上长耳朵”：夹爪在野外人类演示时同步录制音频与视觉；当视觉信息不足时，接触声帮助策略完成接触密集操作。 · [代码](https://github.com/real-stanford/maniwav)
- **[Octopi: Object Property Reasoning with Large Tactile-Language Models](https://arxiv.org/abs/2405.02794)** (2024) — 把触觉感知与语言结合，让具身系统对触摸获得的物理属性做常识推理；贡献 PhysiCLeAR 数据集。 · [代码](https://github.com/clear-nus/octopi)
- **[RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing](https://arxiv.org/abs/2407.01418)** (2024) — 循环图网络从视触觉历史估计物体状态与潜在物理属性，学到的动力学模型用于 MPC，完成密集装箱等任务。
- **[Sparsh: Self-supervised touch representations for vision-based tactile sensing](https://arxiv.org/abs/2410.24090)** (2024) — 在大量触觉图像上自监督预训练的编码器，可跨不同视触觉传感器使用。 · [代码](https://github.com/facebookresearch/sparsh)
- **[TacSL: A Library for Visuotactile Sensor Simulation and Learning](https://arxiv.org/abs/2408.06506)** (2024) — 在 Isaac Gym 中用 GPU 模拟 GelSight 式触觉图像与接触力，并提供用于视触觉策略仿真到真实迁移的学习工具。
- **[Tactile-Augmented Radiance Fields](https://arxiv.org/abs/2405.04534)** (2024) — TaRF 把视觉与触觉放进同一三维空间：将触摸采样配准到照片，并用条件扩散模型估计未采样位置的触觉。 · [代码](https://github.com/dou-yiming/TaRF)
- **[9DTact: A Compact Vision-Based Tactile Sensor for Accurate 3D Shape Reconstruction and Generalizable 6D Force Estimation](https://arxiv.org/abs/2308.14277)** (2023) — DTact 的后续：紧凑的开源视觉触觉传感器，可重建三维接触形状，并用可泛化到新物体的模型估计六维力/力矩。 · [代码](https://github.com/linchangyi1/9DTact)
- **[Evetac: An Event-based Optical Tactile Sensor for Robotic Manipulation](https://arxiv.org/abs/2312.01236)** (2023) — 用事件相机取代光学触觉传感器的 RGB 相机；触觉处理以 1000 Hz 在线运行，可感知最高 498 Hz 的振动。
- **[General In-Hand Object Rotation with Vision and Touch](https://arxiv.org/abs/2309.09979)** (2023) — RotateIt 先在仿真中利用特权物体信息训练，再蒸馏为仅用视觉、触觉和本体感觉的策略，在真实灵巧手上旋转多种物体。
- **[MimicTouch: Leveraging Multi-modal Human Tactile Demonstrations for Contact-rich Manipulation](https://arxiv.org/abs/2310.16917)** (2023) — 从人手直接演示学习触觉策略，弥补遥操作中“人靠视觉控制、策略却要用触觉”的落差。
- **[Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation](https://arxiv.org/abs/2312.13469)** (2023) — NeuralFeels 将多指手的视觉与触觉在线融合为神经场，在操作过程中同时重建物体形状并跟踪其位姿。 · [代码](https://github.com/facebookresearch/neuralfeels)
- **[Robot Synesthesia: In-Hand Manipulation with Visuotactile Sensing](https://arxiv.org/abs/2312.01853)** (2023) — 将触觉读数转换为与相机点云、手部模型处于同一三维坐标系的点，用统一的视触觉点云输入驱动手内物体旋转。 · [代码](https://github.com/YingYuan0414/in-hand-rotation) · [项目页](https://yingyuan0414.github.io/visuotactile/)
- **[Rotating without Seeing: Towards In-hand Dexterity through Touch](https://arxiv.org/abs/2303.10880)** (2023) — 在灵巧手上铺设廉价的二值（有/无接触）触觉传感器，在仿真中用强化学习训练策略，迁移到真机后无需视觉即可在手中旋转未见过的物体。 · [代码](https://github.com/YingYuan0414/in-hand-rotation) · [项目页](https://touchdexterity.github.io)
- **[DTact: A Vision-Based Tactile Sensor that Measures High-Resolution 3D Geometry Directly from Darkness](https://arxiv.org/abs/2209.13916)** (2022) — 低成本视觉触觉传感器：根据凝胶受压时每个像素变暗的程度直接读出接触深度，无需光度立体即可获得高分辨率三维形状。
- **[See, Hear, and Feel: Smart Sensory Fusion for Robotic Manipulation](https://arxiv.org/abs/2212.03858)** (2022) — 在模仿学习策略中用自注意力融合相机、接触麦克风和 GelSight 触觉，在密集装箱与倾倒任务上做了研究。 · [代码](https://github.com/JunzheJosephZhu/see_hear_feel)
- **[Tactile Gym 2.0: Sim-to-real Deep Reinforcement Learning for Comparing Low-cost High-Resolution Robot Touch](https://arxiv.org/abs/2207.10763)** (2022) — 开源触觉强化学习环境，支持三种低成本光学触觉传感器（TacTip、DIGIT、DigiTac）的仿真到真机迁移，便于在相同任务上比较。 · [代码](https://github.com/dexterousrobot/tactile_gym)
- **[Touch and Go: Learning from Human-Collected Vision and Touch](https://arxiv.org/abs/2211.12498)** (2022) — 由人手持 GelSight 在真实场景中触碰物体采集的视觉-触觉配对数据集，用于跨模态触觉学习。
- **[GelSlim 3.0: High-Resolution Measurement of Shape, Force and Slip in a Compact Tactile-Sensing Finger](https://arxiv.org/abs/2103.12269)** (2021) — 纤薄的 GelSight 类触觉手指，可高分辨率测量接触形状、力与滑移，便于装在机器人夹爪上。
- **[ReSkin: versatile, replaceable, lasting tactile skins](https://arxiv.org/abs/2111.00071)** (2021) — 由磁力计读取的薄磁性弹性体皮肤，制作和更换成本低，学习得到的标定可迁移到新皮肤上。 · [代码](https://github.com/raunaqbhirangi/reskin_sensor)
- **[Taxim: An Example-based Simulation Model for GelSight Tactile Sensors](https://arxiv.org/abs/2109.04027)** (2021) — 用标定样本（光学查找表 + 线弹性形变）而不是基于物理的渲染来模拟 GelSight 图像，可快速生成触觉数据。 · [代码](https://github.com/Robo-Touch/Taxim)
- **[TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors](https://arxiv.org/abs/2012.08456)** (2020) — 在仿真中渲染 DIGIT/GelSight 式触觉图像，便于大规模训练基于触觉的策略。 · [代码](https://github.com/facebookresearch/tacto)
- **[Making Sense of Vision and Touch: Self-Supervised Learning of Multimodal Representations for Contact-Rich Tasks](https://arxiv.org/abs/1810.10191)** (2018) — 用自监督目标学习视觉 + 力/力矩的紧凑联合表征，再在其上用强化学习在真实机器人上训练插孔策略。 · [代码](https://github.com/stanford-iprl-lab/multimodal_representation)

**另见**

[Never Too Late for Force](vla.zh-CN.md), [FORCA](manipulation.zh-CN.md), [ContactBench 1.0](manipulation.zh-CN.md), [CARD](manipulation.zh-CN.md), [ForceLDM](manipulation.zh-CN.md), [DeCAL](manipulation.zh-CN.md), [Physical Canvas](world-models.zh-CN.md), [DIFFTACTILE](sim.zh-CN.md), [Taccel](sim.zh-CN.md), [TacEx](sim.zh-CN.md), [EgoExplorer](datasets.zh-CN.md), [ORCA](hardware.zh-CN.md), [Learning Visuotactile Skills with Two Multifingered Hands](hardware.zh-CN.md), [DOGlove](hardware.zh-CN.md), [SwapBot](hardware.zh-CN.md)
