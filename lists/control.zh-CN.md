# 规划、控制与安全

_运动规划、轨迹优化、模型预测控制、安全滤波器与安全的学习型控制。_

共 46 条。⭐⭐⭐ 必读（每个主题仅一篇）· ⭐⭐ 强烈推荐 · ⭐ 推荐。由 [`data/curated/control.yaml`](../data/curated/control.yaml) 生成，请勿直接编辑。

[返回 README](../README.zh-CN.md) · [在网站上查看](https://hu-zlatan.github.io/embodied-ai-radar/topics/control.html) · [English](control.md)

[VLA 与机器人基础模型](vla.zh-CN.md) · [操作与灵巧手](manipulation.zh-CN.md) · [触觉与视触觉感知](tactile.zh-CN.md) · [运动控制与人形机器人](locomotion.zh-CN.md) · [世界模型](world-models.zh-CN.md) · [导航与具身智能体](navigation.zh-CN.md) · [感知、SLAM 与三维建图](perception.zh-CN.md) · **规划、控制与安全** · [机器人学习：强化学习与模仿学习](learning.zh-CN.md) · [仿真与 Sim-to-Real](sim.zh-CN.md) · [数据集与基准](datasets.zh-CN.md) · [硬件与开源机器人](hardware.zh-CN.md)

- ⭐⭐⭐ **[cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation](https://arxiv.org/abs/2310.17274)** (2023) — 面向机械臂的 GPU 并行运动生成：同时运行大量轨迹优化，在毫秒级给出无碰撞且平滑的轨迹。 · [代码](https://github.com/NVlabs/curobo)
- ⭐ **[cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots](https://arxiv.org/abs/2603.05493)** (2026) — cuRoboV2 新增考虑力矩限制的 B 样条轨迹优化和 GPU 原生 TSDF/ESDF 感知，面向高自由度机器人。 · [代码](https://github.com/NVlabs/curobo)
- ⭐ **[PyRoki: A Modular Toolkit for Robot Kinematic Optimization](https://arxiv.org/abs/2505.03728)** (2025) — PyRoki：模块化、跨平台的运动学优化工具包，可原生运行在 CPU、GPU 和 TPU 上。 · [代码](https://github.com/chungmin99/pyroki) · [项目页](https://pyroki-toolkit.github.io)
- ⭐ **[Planning with Diffusion for Flexible Behavior Synthesis](https://arxiv.org/abs/2205.09991)** (2022) — Diffuser：把规划视为对整条轨迹去噪，目标与奖励可以引导采样；扩散模型与控制结合的早期代表作。 · [代码](https://github.com/jannerm/diffuser)
- ⭐ **[Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo](https://arxiv.org/abs/2212.00541)** (2022) — 推出 MuJoCo MPC（MJPC），可在 MuJoCo 中交互式地做实时预测控制，并表明简单的基于采样的规划器在接触丰富的行为上是很强的基线。 · [代码](https://github.com/google-deepmind/mujoco_mpc)
- ⭐ **[legged_control](https://github.com/qiayuanl/legged_control)** (2022) — 基于 OCS2 与 ros-control 的开源四足控制栈：非线性 MPC + 全身控制 + 状态估计，并支持 sim2real；基于模型的足式控制常用的起点。
- ⭐ **[Jerk-limited Real-time Trajectory Generation with Arbitrary Target States](https://arxiv.org/abs/2105.04830)** (2021) — Ruckig：开源 C++/Python 库，可实时生成到任意目标位置、速度和加速度的时间最优、限加加速度（jerk）轨迹；常被直接用于真实控制器上的机械臂平滑运动。 · [代码](https://github.com/pantor/ruckig)
- ⭐ **[OCS2: Optimal Control for Switched Systems](https://github.com/leggedrobotics/ocs2)** (2021) — 面向切换系统的非线性 MPC C++ 工具箱（SLQ、DDP、SQP），附足式机器人与移动操作臂示例；许多开源足式 MPC + 全身控制方案都基于它。
- ⭐ **[OSQP: An Operator Splitting Solver for Quadratic Programs](https://arxiv.org/abs/1711.08013)** (2020) — 基于 ADMM 的快速、鲁棒二次规划求解器，支持热启动与嵌入式 C 代码生成，广泛用于 MPC 与全身控制器。 · [代码](https://github.com/osqp/osqp)
- ⭐ **[Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control](https://arxiv.org/abs/1909.04947)** (2019) — 基于 DDP 的开源接触丰富轨迹优化求解器，广泛用于足式与人形机器人的运动生成和 MPC。 · [代码](https://github.com/loco-3d/crocoddyl)
- ⭐ **[MoveIt 2](https://moveit.ai/)** (2019) — ROS 2 的机械臂操作框架：提供运动规划、逆运动学、碰撞检测与实时伺服控制。 · [代码](https://github.com/moveit/moveit2)
- ⭐ **[Pinocchio](https://github.com/stack-of-tasks/pinocchio)** (2019) — 高性能 C++/Python 刚体动力学库，提供解析导数；是运动学、最优控制（如 Crocoddyl）以及足式/人形机器人控制栈的常用底座。
- ⭐ **[acados: a modular open-source framework for fast embedded optimal control](https://arxiv.org/abs/1910.13753)** (2019) — 高速非线性 MPC 与状态估计求解器，提供 Python/MATLAB 接口并可为嵌入式平台生成 C 代码。 · [代码](https://github.com/acados/acados)
- ⭐ **[Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](https://github.com/mit-biomimetics/Cheetah-Software)** (2018) — 四足机器人的凸 MPC：用简化刚体动力学把足端地面反作用力规划变成可实时求解的小规模 QP；众多开源四足控制器背后的经典基于模型的基线。
- ⭐ **[Drake](https://drake.mit.edu/)** (2014) — 面向机器人的基于模型的工具箱：带接触的多体动力学仿真、数学规划与轨迹优化；MIT 操作与欠驱动课程即使用它。 · [代码](https://github.com/RobotLocomotion/drake)
- ⭐ **[OMPL: The Open Motion Planning Library](https://ompl.kavrakilab.org/)** (2012) — 采样式运动规划器的标准库（RRT、RRT-Connect、PRM、RRT* 等众多算法），也是 MoveIt 默认的规划后端。 · [代码](https://github.com/ompl/ompl)
- **[A generalist policy for muscle-driven control across individual musculoskeletal models](https://arxiv.org/abs/2610.36535)** (2026) — MyoAcross 结合个体化肌骨模型构建、形态条件策略学习与虚拟模型增广，用一个策略驱动不同个体的肌骨模型跟踪参考动作而无需逐个微调；报告在 31 个未见个体模型上完成率 99.24%，跟踪误差比无条件 MLP 降低 22.6%，并与 120 人的地面反力和肌电数据做了对比。 · [项目页](https://woodater-thu.github.io/MyoAcross/)
- **[BarrierFormer: Transformer-Guided Predictive Barrier Enforcement for Safe Robot Control](https://arxiv.org/abs/2609.23896)** (2026) — 因果 Transformer 预测未来推演（代替动力学模型）并给名义控制器输出残差修正；障碍评估器沿推演检查 CBF 约束违例，从而像 MPC 一样前瞻安全，却无需在线求解优化。
- **[CusADi2: Latency-Optimized Batch Computation of Robot Kinematics, Jacobians, and Hessians on the GPU](https://arxiv.org/abs/2610.25476)** (2026) — 在 GPU 上以低延迟批量计算运动学、雅可比与海森矩阵，面向在线运行的采样式与梯度式轨迹优化。 · [代码](https://github.com/johnviljoen/cusadi2)
- **[Exploring the Intrinsic Geometry of Diffusion Models with Constrained Inverse Kinematics](https://arxiv.org/abs/2606.26408)** (2026) — 以解流形可精确知道的约束逆运动学为试验场，检验扩散模型学到的几何结构。在 UR5 和 Franka 上，从得分函数估计的内在维度与解析自由度一致。 · [项目页](https://papers.starslab.ca/diffusion-ik-geometry/)
- **[Gradient-Free Neural Hamilton-Jacobi Reachability for Scalable Safety-Critical Control](https://arxiv.org/abs/2609.14087)** (2026) — 无需 PDE 梯度的离散时间神经 HJ 可达性：利用最优安全干预的 bang-bang 结构和免梯度的价值探测构造教师动作，把对抗式策略学习变成监督学习；分窗口的时间课程稳定训练。
- **[Keeping Contact: Task-Adaptive Friction Margins for Bimanual Non-Prehensile Manipulation](https://arxiv.org/abs/2610.36961)** (2026) — 以带符号摩擦距离度量防滑裕度，并在双臂绕支点倾转物体时按任务需求自适应调整；一系列二阶锥规划给出全局最优接触力。真机实验显示自适应裕度优于固定裕度和无裕度。 · [项目页](https://keeping-contact.github.io/)
- **[LEMCA: LLM-Guided Synthesis of Efficient Mode-Switching Control Architectures](https://arxiv.org/abs/2609.21319)** (2026) — 用 LLM 驱动的进化搜索，把多模式切换控制器写成可解释程序并迭代优化，使简单阶段使用低开销模式。报告找到的设计超越单一结构控制器的帕累托前沿。 · [项目页](https://lemca-robotics.github.io/)
- **[Learning Unions of Convex Sets via Invertible Latent Decomposition for Path Planning](https://arxiv.org/abs/2606.12027)** (2026) — 联合学习可逆映射及其潜空间中的凸多面体并集，使基于凸集的规划可用于高自由度空间，解码回原空间的路径仍可行。在 2D 至 14 自由度场景测试，细化后未观察到误报。
- **[M$^3$P-R1: Reinforcement Learning for Large Language Model Guided Multi-Modal Motion Planning via MIP Code Generation](https://arxiv.org/abs/2609.18669)** (2026) — 用求解器结果作为奖励对 LLM 做强化学习微调，让它为多模态运动规划（如先走再抓）编写可执行的混合整数规划代码，而不是直接给出答案。
- **[On the Limits of Sampling-Based Reachability: Geometry, Dynamics, and Sample Complexity](https://arxiv.org/abs/2607.18606)** (2026) — 理论工作：给出采样可达集在 Hausdorff 距离意义下准确的条件，并证明所需样本数随状态维度和时间跨度都呈指数增长，且给出相应下界。
- **[Optimal Control with Learned Critics under Unmodeled State Dependencies](https://arxiv.org/abs/2610.05359)** (2026) — 在 iLQR 模型预测控制中加入残差动力学网络和学习得到的动作价值评估器，并实现 GPU 批量 iLQR 并行求解数千个问题，用于接触难以建模时的基于模型强化学习。
- **[PAKT: Physically-Aligned Kinesthetic Teaching for Reinforcement Learning](https://arxiv.org/abs/2609.25630)** (2026) — 面向真实世界强化学习的示教框架：人手拖动示教时轨迹始终满足策略可执行的运动学限制，并配套阻抗控制栈。报告工业插装任务节拍时间比 HIL-SERL 缩短 23–48%。 · [项目页](https://pakt-website.github.io/pakt-website)
- **[PRISM: Polynomial Representations for Interaction-Structured Motor Control](https://arxiv.org/abs/2607.23473)** (2026) — 把策略 MLP 的第一层替换为可学习的乘性（双线性）特征，即插即用于强化学习与模仿学习。报告人形机器人存活率从 51.0% 提升到 92.5%，在摩擦、负载变化下依然有效。 · [项目页](https://lsh3163.github.io/prism/)
- **[PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning](https://arxiv.org/abs/2611.05372)** (2026) — 学习式目标条件逆运动学，能保持位置控制器静止时所需的偏置；报告在 93.5% 的留出仿真任务上误差低于 1 mm 和 0.2°，并可直接在真实机械臂上训练。 · [代码](https://github.com/Tinaliu0123/PolicyIK)
- **[PrismPlan: A Shared GPU Substrate for Motion Planning Across Paradigms](https://arxiv.org/abs/2610.23884)** (2026) — 一次性实现批量 GPU 碰撞检测与正运动学，在其上运行采样、搜索和优化三类规划器，使三种范式可以公平比较。 · [代码](https://github.com/XiaoyubotMotionTeam/PrismPlan)
- **[RAM: Reachability Across Morphologies](https://arxiv.org/abs/2606.09108)** (2026) — CoRL 2026 Spotlight。以形态为条件的隐式神经位姿可达性模型，可微、考虑自碰撞，并能泛化到未见形态。 · [代码](https://github.com/TimWalter/ram) · [项目页](https://timwalter.github.io/ram)
- **[Safe Streaming Flow Planning by Aligning Sampling Dynamics with Execution Dynamics](https://arxiv.org/abs/2610.03132)** (2026) — 流匹配规划器让采样过程与系统执行动力学对齐，只需对实际执行的一步施加高阶控制障碍函数约束。在导航、竞速和运动任务上降低规划延迟并提升安全性。 · [项目页](https://jang-seunghwan.github.io/SafeStreamingFlowPlanning/)
- **[Scalable Deep Unfolding of Conic Optimizers](https://arxiv.org/abs/2606.13825)** (2026) — 通过无矩阵隐式微分和稳定的半正定投影梯度，让深度展开适用于大规模锥优化求解器；报告在基于 SDP 的规划上最高提速 50 倍。
- **[Sub-Millisecond Reflexes for Continuous Physical Human-Robot Interaction](https://arxiv.org/abs/2610.21913)** (2026) — 开源的 ROS 2 多模式控制器，可在亚毫秒内切换控制模式并触发安全反射而无需中断任务；在 Franka 机械臂上验证。 · [代码](https://github.com/RoboRef/franka_reflex_engine)
- **[TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation](https://arxiv.org/abs/2606.06218)** (2026) — CoRL 2026 Spotlight。面向富接触动作迁移的模块，应对仿真到现实、负载与个体差异，用于替代域随机化或系统辨识。 · [代码](https://github.com/Dongwon-Son/TAM) · [项目页](https://dongwon-son.github.io/tam-project-page/)
- **[TDC: Sim-to-Real Transferable Directional Compliance for Contact-Rich Manipulation](https://arxiv.org/abs/2602.14174)** (2026) — 把力调节拆成两部分：方向分量（任务坐标系与控制模式，由基于 VLA 的策略在仿真数据上学习）和幅值分量（在导纳控制器中人工设定）。只用仿真数据，在四个真机任务上验证。 · [项目页](https://yifei-y.github.io/project-pages/TDC/)
- **[VertexCBF: Improving Neural Control Barrier Functions via Vertex-Restricted Control Search](https://arxiv.org/abs/2609.12831)** (2026) — 通过近似 HJ 价值函数学习神经控制障碍函数；在控制仿射动力学和多面体输入集下最优解位于顶点，于是用 GPU 并行顶点树搜索生成监督点。在 15 个系统和行人避让真机实验中验证。
- **[When Should a Robot Replan? Regret-Guided Update Scheduling in Time-Varying MDPs](https://arxiv.org/abs/2606.16972)** (2026) — 在动力学漂移、重估与重规划次数有限时，用动态遗憾界推导出何时更新的在线规则。在模拟的打滑漫游车和 Crazyflie 四旋翼上验证。
- **[Motions in Microseconds via Vectorized Sampling-Based Planning](https://arxiv.org/abs/2309.14545)** (2023) — VAMP：用 CPU SIMD 指令把碰撞检测向量化，使 RRT-Connect 等基于采样的规划器在微秒到毫秒级求解机械臂运动规划，无需 GPU。 · [代码](https://github.com/KavrakiLab/vamp)
- **[Motion Policy Networks](https://arxiv.org/abs/2210.12209)** (2022) — 在数百万条规划器生成的轨迹上训练的神经策略，可直接根据点云把机械臂移动到目标位置。 · [代码](https://github.com/NVlabs/motion-policy-networks)
- **[Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning](https://arxiv.org/abs/2108.06266)** (2021) — 综述，连接控制理论与强化学习两种安全视角：从带保证的学习动力学到约束强化学习与安全滤波器。
- **[safe-control-gym: a Unified Benchmark Suite for Safe Learning-based Control and Reinforcement Learning in Robotics](https://arxiv.org/abs/2109.06325)** (2021) — Gym 风格基准，含倒立摆与四旋翼任务、约束与扰动，用于比较安全控制与安全强化学习方法。 · [代码](https://github.com/utiasDSL/safe-control-gym)
- **[Control Barrier Functions: Theory and Applications](https://arxiv.org/abs/1903.11199)** (2019) — 控制障碍函数教程：为任意控制器加一层“尽量少改动”的安全滤波器、保证系统安全的标准方法。
- **[Riemannian Motion Policies](https://arxiv.org/abs/1801.02854)** (2018) — RMP：把每种行为（到达、避障、关节限位）表示为加速度策略加黎曼度量，再按几何方式组合；是后来 RMPflow 与几何织物（geometric fabrics）控制器的基础。
- **[Hamilton-Jacobi Reachability: A Brief Overview and Recent Advances](https://arxiv.org/abs/1709.07523)** (2017) — Hamilton-Jacobi 可达性分析简明教程：计算在最坏扰动下仍能保持系统安全的状态集合，以及将其扩展到更高维系统的方法。

**另见**

[cuArms](manipulation.zh-CN.md), [Robustness without Wrinkles](manipulation.zh-CN.md), [Learning Force-Reactive Humanoid Loco-Manipulation](locomotion.zh-CN.md), [DiffContact](locomotion.zh-CN.md), [SWAP](locomotion.zh-CN.md), [SMR](locomotion.zh-CN.md), [METATRON](locomotion.zh-CN.md), [Energy-Based Policy Orchestration](locomotion.zh-CN.md), [DeepMimic](locomotion.zh-CN.md), [ASE](locomotion.zh-CN.md), [Perpetual Humanoid Control for Real-time Simulated Avatars](locomotion.zh-CN.md), [InterMimic](locomotion.zh-CN.md), [SONIC](locomotion.zh-CN.md), [Humanoid-GPT](locomotion.zh-CN.md), [ResSafe](locomotion.zh-CN.md), [SoftMimic](locomotion.zh-CN.md), [GentleHumanoid](locomotion.zh-CN.md), [CHIP](locomotion.zh-CN.md), [Ctrl-F](locomotion.zh-CN.md), [TD-MPC2](world-models.zh-CN.md), [SCoCaT](learning.zh-CN.md), [Control-Ready Uncertainty for Trajectory Diffusion](learning.zh-CN.md)
