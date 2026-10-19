# Embodied AI Radar · 具身智能雷达

**A bilingual (English / [中文](README.zh-CN.md)), always-fresh map of embodied AI and robot learning.**
Hand-verified papers, code, datasets, simulators and hardware with one-line takeaways — plus every new robotics paper on arXiv, fetched and tagged by topic every day.

### 🌐 [Open the website → hu-zlatan.github.io/embodied-ai-radar](https://hu-zlatan.github.io/embodied-ai-radar/)

[![Website](https://img.shields.io/badge/website-live-0f6fde)](https://hu-zlatan.github.io/embodied-ai-radar/)
[![Daily arXiv intake](https://github.com/hu-zlatan/embodied-ai-radar/actions/workflows/intake.yml/badge.svg)](https://github.com/hu-zlatan/embodied-ai-radar/actions/workflows/intake.yml)
[![Verified links](https://github.com/hu-zlatan/embodied-ai-radar/actions/workflows/verify.yml/badge.svg)](https://github.com/hu-zlatan/embodied-ai-radar/actions/workflows/verify.yml)
[![License: MIT + CC BY 4.0](https://img.shields.io/badge/license-MIT%20%2B%20CC%20BY%204.0-lightgrey)](LICENSE-DATA.md)

![Screenshot of the Embodied AI Radar website](docs/screenshot.png)

## Why this one

- **Verified.** Every curated arXiv ID is checked against arXiv and every link is checked by CI, weekly.
- **Fresh.** A GitHub Action pulls new cs.RO papers (plus robotics papers from cs.CV / cs.LG / cs.AI / cs.CL) every day and tags them by topic — they appear on the site without anyone touching the repo.
- **Searchable.** Instant search and filters (topic · robot type: arm, hand, humanoid, legged, drone… · curated vs. daily · has code) on a fast static site that works on phones.
- **Bilingual.** Every curated entry has a one-line takeaway in English and Chinese; the site has an EN / 中文 toggle.

| What | How often |
|---|---|
| Daily arXiv feed ([site](https://hu-zlatan.github.io/embodied-ai-radar/feed.html) · [Atom](https://hu-zlatan.github.io/embodied-ai-radar/feed.xml); one Atom feed per topic, e.g. [VLA](https://hu-zlatan.github.io/embodied-ai-radar/topics/vla.xml)) | every day, automatically |
| Curated index (below and on the site) | several times a week |
| [Weekly digest](digest/) | weekly |

## Topics

VLA & robot foundation models · manipulation & dexterous hands · tactile sensing · locomotion & humanoids · world models · navigation & embodied agents · perception, SLAM & 3D mapping · planning, control & safety · sim-to-real & simulators · datasets & benchmarks · hardware & open-source robots.

## Curated index

⭐ = highlight. Generated from [`data/curated/`](data/curated) — edit the YAML, not this list.

<!-- radar:start -->

[VLA & Robot Foundation Models](#vla) · [Manipulation & Dexterous Hands](#manipulation) · [Tactile & Visuotactile Sensing](#tactile) · [Locomotion & Humanoids](#locomotion) · [World Models](#world-models) · [Navigation & Embodied Agents](#navigation) · [Perception, SLAM & 3D Mapping](#perception) · [Planning, Control & Safety](#control) · [Robot Learning: RL & Imitation](#learning) · [Sim-to-Real & Simulators](#sim) · [Datasets & Benchmarks](#datasets) · [Hardware & Open-Source Robots](#hardware)

<a id="vla"></a>
### VLA & Robot Foundation Models

_Vision-language-action models and generalist robot policies._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/vla.html)

- ⭐ **[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** (2024) — A VLM backbone with a flow-matching action expert, trained across many robots, doing long dexterous tasks like laundry folding. · [code](https://github.com/Physical-Intelligence/openpi)
- ⭐ **[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** (2024) — A 7B open VLA built on Llama 2 + DINOv2/SigLIP; the de-facto open baseline for VLA research and LoRA fine-tuning. · [code](https://github.com/openvla/openvla)
- ⭐ **[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** (2023) — Coined "VLA" — co-fine-tuning a web-scale VLM to output action tokens transfers semantic knowledge to robot control. · [project](https://robotics-transformer2.github.io/)
- **[FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2610.22146)** (2026) — Speeds up VLA inference by keeping only the visual tokens the current task needs, with a token budget that changes from step to step. · [code](https://github.com/jiuyixu25/FastVLA)
- **[LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models](https://arxiv.org/abs/2610.21362)** (2026) — Gives π0.5 memory by caching compact latent transitions between observations, aimed at tasks where key objects go out of view. · [code](https://github.com/buaa-colalab/LTM-pi)
- **[NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models](https://arxiv.org/abs/2610.23271)** (2026) — Learns skills separately, then consolidates them after the fact with a nested hypernetwork that generates VLA parameters instead of merging weights. · [code](https://github.com/WanyuGroup/NeurIPS2026-NestedVLA)
- **[REKI: Registering Knowledge in VLAs](https://arxiv.org/abs/2610.22178)** (2026) — A 2.4B VLM + flow-matching VLA pretrained only on public data; reports beating all but ~2× larger models, plus cheap register-token memory. · [code](https://github.com/kyutai-labs/reki)
- **[π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)** (2025) — Co-training on heterogeneous data lets a mobile manipulator clean kitchens and bedrooms in homes it has never seen. · [code](https://github.com/Physical-Intelligence/openpi)
- **[FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747)** (2025) — Compresses action chunks with a DCT-based tokenizer so autoregressive VLAs can learn high-frequency, dexterous control.
- **[Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645)** (2025) — OpenVLA-OFT — parallel decoding, action chunking and continuous actions make VLA fine-tuning much faster and more accurate. · [code](https://github.com/moojink/openvla-oft)
- **[GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)** (2025) — A dual-system (VLM "slow" + diffusion "fast") humanoid policy trained on real, human-video and synthetic data. · [code](https://github.com/NVIDIA/Isaac-GR00T)
- **[Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020)** (2025) — Gemini 2.0-based VLA and embodied-reasoning models for dexterous, general robot control.
- **[RoboBrain 2.0 Technical Report](https://arxiv.org/abs/2507.02029)** (2025) — Open embodied VLMs (7B and 32B) trained for spatial grounding, affordances, trajectories and multi-step task planning — a "brain" that sits above low-level policies. · [code](https://github.com/FlagOpen/RoboBrain2.0)
- **[SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://arxiv.org/abs/2506.01844)** (2025) — A ~450M-parameter VLA trained on community LeRobot data that runs on consumer GPUs. · [code](https://github.com/huggingface/lerobot)
- **[CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation](https://arxiv.org/abs/2411.19650)** (2024) — Instead of emitting action tokens from the VLM, a separate diffusion action transformer is conditioned on the VLM's "cognition" feature; reports clear gains over OpenVLA in sim and on real robots. · [code](https://github.com/microsoft/CogACT)
- **[Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213)** (2024) — A small open diffusion-head Transformer pretrained on Open X-Embodiment that fine-tunes quickly to new robots and sensors. · [code](https://github.com/octo-models/octo)
- **[RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](https://arxiv.org/abs/2410.07864)** (2024) — A 1.2B diffusion Transformer with a unified action space across robots, targeted at bimanual manipulation. · [code](https://github.com/thu-ml/RoboticsDiffusionTransformer)
- **[PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378)** (2023) — Injects continuous sensor embeddings into a 562B language model for embodied reasoning and planning.
- **[A Generalist Agent](https://arxiv.org/abs/2205.06175)** (2022) — Gato — one Transformer with one set of weights plays games, captions images and stacks blocks with a real arm.
- **[RT-1: Robotics Transformer for Real-World Control at Scale](https://arxiv.org/abs/2212.06817)** (2022) — Tokenized actions plus a Transformer trained on 130k real demos showed that robot policies scale with data diversity. · [code](https://github.com/google-research/robotics_transformer)
- _See also:_ [HexaShell](#manipulation), [Cracking Mobile Manipulation](#navigation), [Open X-Embodiment](#datasets), [Evaluating Real-World Robot Manipulation Policies in Simulation](#datasets), [Embodied Skill Bench](#datasets)

<a id="manipulation"></a>
### Manipulation & Dexterous Hands

_Imitation learning, diffusion policies, grasping, bimanual and dexterous manipulation._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/manipulation.html)

- ⭐ **[Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](https://arxiv.org/abs/2402.10329)** (2024) — A handheld gripper with a GoPro collects demos anywhere; policies transfer directly to robot arms. · [code](https://github.com/real-stanford/universal_manipulation_interface)
- ⭐ **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** (2023) — Generating action sequences by denoising handles multimodal demos far better than regression; now a standard IL baseline. · [code](https://github.com/real-stanford/diffusion_policy)
- ⭐ **[Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705)** (2023) — ALOHA + ACT — a ~$20k bimanual teleop rig and an action-chunking Transformer that learns precise tasks from ~50 demos. · [code](https://github.com/tonyzhaozh/act)
- **[Beyond the End-Effector: Learning Whole-Arm Contact Manipulation from Human Demonstrations](https://arxiv.org/abs/2610.17802)** (2026) — WACL learns from human demos to push and hold with the whole arm, choosing where on the arm to make contact while keeping the gripper's constraints. · [project](https://wacl-robot.github.io)
- **[Blind Precise Assembly: Proprioceptive Sim-to-Real Peg-in-Hole for Diverse Parts](https://arxiv.org/abs/2610.23849)** (2026) — Asks whether joint readings alone suffice for millimetre-precise insertion — trains sim-to-real policies with no camera, force or tactile input.
- **[Can a Frontier VLM Serve as a Robot Policy for Memory-Dependent Manipulation?](https://arxiv.org/abs/2610.17350)** (2026) — A frozen frontier VLM, prompted with the whole episode, outputs waypoints directly and reports 92.1% on RoboMME memory tasks with no task training. · [code](https://github.com/jackbjed/embodied-astra-robomme) · [project](https://embodied-astra.github.io)
- **[HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents](https://arxiv.org/abs/2610.23479)** (2026) — A coding agent drives a bimanual robot through one command line; after each failure it reads the logs and writes or fixes small reusable tool programs. · [code](https://github.com/HexaFuture/HexaShell)
- **[3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations](https://arxiv.org/abs/2403.03954)** (2024) — Conditions a diffusion policy on a compact point-cloud encoding; more data-efficient and robust to viewpoint than images. · [code](https://github.com/YanjieZe/3D-Diffusion-Policy)
- **[DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation](https://arxiv.org/abs/2403.07788)** (2024) — A wearable mocap glove + camera rig records human hand motion that is retargeted to train dexterous robot hands.
- **[Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation](https://arxiv.org/abs/2401.02117)** (2024) — Puts ALOHA on a mobile base; co-training with static ALOHA data boosts mobile tasks like cooking and opening cabinets. · [code](https://github.com/MarkFzp/mobile-aloha)
- **[VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://arxiv.org/abs/2307.05973)** (2023) — LLMs write code that composes 3D affordance/constraint maps, which a planner turns into trajectories — no robot training.
- **[DexGraspNet: A Large-Scale Robotic Dexterous Grasp Dataset for General Objects Based on Simulation](https://arxiv.org/abs/2210.02697)** (2022) — Over a million physically validated ShadowHand grasps on thousands of objects, synthesized by optimizing a differentiable force-closure energy; a standard training set for dexterous grasp models. · [code](https://github.com/PKU-EPIC/DexGraspNet)
- **[R3M: A Universal Visual Representation for Robot Manipulation](https://arxiv.org/abs/2203.12601)** (2022) — Pretrains a visual encoder on Ego4D human videos that makes downstream imitation far more data-efficient.
- **[Visual Dexterity: In-Hand Reorientation of Novel and Complex Object Shapes](https://arxiv.org/abs/2211.11744)** (2022) — Reorients unseen objects in-hand using only a depth camera, with a policy trained in simulation.
- **[Solving Rubik's Cube with a Robot Hand](https://arxiv.org/abs/1910.07113)** (2019) — Automatic domain randomization lets a sim-trained hand policy manipulate a Rubik's cube on real hardware.
- **[Learning Dexterous In-Hand Manipulation](https://arxiv.org/abs/1808.00177)** (2018) — A Shadow Hand reorients a cube using RL trained purely in randomized simulation — a sim-to-real milestone.
- _See also:_ [3D-ViTac](#tactile), [Code as Policies](#navigation), [OK-Robot](#navigation), [Cracking Mobile Manipulation](#navigation), [Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance](#navigation), [FoundationPose](#perception), [cuRobo](#control), [Motion Policy Networks](#control), [Sub-Millisecond Reflexes for Continuous Physical Human-Robot Interaction](#control), [SERL](#learning), [Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](#learning), [RoboTwin 2.0](#sim), [LeRobot](#datasets), [LEAP Hand](#hardware), [BEHAVIOR Robot Suite](#hardware)

<a id="tactile"></a>
### Tactile & Visuotactile Sensing

_Tactile sensors, touch representations and contact-rich control._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/tactile.html)

- ⭐ **[DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](https://arxiv.org/abs/2005.14679)** (2020) — An inexpensive, compact GelSight-style fingertip sensor that made vision-based touch widely accessible. · [code](https://github.com/facebookresearch/digit-interface)
- **[3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing](https://arxiv.org/abs/2410.24091)** (2024) — Fuses dense tactile arrays with 3D vision in a diffusion policy for fragile, contact-rich bimanual tasks.
- **[AnySkin: Plug-and-play Skin Sensing for Robotic Touch](https://arxiv.org/abs/2409.08276)** (2024) — A replaceable magnetic tactile skin whose learned policies keep working after the skin is swapped.
- **[Binding Touch to Everything: Learning Unified Multimodal Tactile Representations](https://arxiv.org/abs/2401.18084)** (2024) — UniTouch aligns tactile signals with vision, language and audio embeddings, enabling zero-shot touch understanding.
- **[Sparsh: Self-supervised touch representations for vision-based tactile sensing](https://arxiv.org/abs/2410.24090)** (2024) — Self-supervised encoders pretrained on many tactile images that work across different vision-based touch sensors. · [code](https://github.com/facebookresearch/sparsh)
- **[Touch and Go: Learning from Human-Collected Vision and Touch](https://arxiv.org/abs/2211.12498)** (2022) — A dataset of paired video and GelSight touch collected by people probing objects in the wild, for cross-modal tactile learning.
- **[ReSkin: versatile, replaceable, lasting tactile skins](https://arxiv.org/abs/2111.00071)** (2021) — A thin magnetic-elastomer skin read by magnetometers; cheap to make and swap, with learned calibration that carries over to new skins. · [code](https://github.com/raunaqbhirangi/reskin_sensor)
- **[TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors](https://arxiv.org/abs/2012.08456)** (2020) — Renders DIGIT/GelSight-style tactile images in simulation so touch-based policies can be trained at scale. · [code](https://github.com/facebookresearch/tacto)

<a id="locomotion"></a>
### Locomotion & Humanoids

_Legged locomotion, humanoid whole-body control and parkour._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/locomotion.html)

- ⭐ **[Real-World Humanoid Locomotion with Reinforcement Learning](https://arxiv.org/abs/2303.03381)** (2023) — A causal Transformer policy trained in simulation walks a full-size humanoid outdoors, zero-shot.
- ⭐ **[Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](https://arxiv.org/abs/2109.11978)** (2021) — Thousands of parallel GPU environments train a quadruped walking policy in minutes; legged_gym became a standard starter. · [code](https://github.com/leggedrobotics/legged_gym)
- **[ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](https://arxiv.org/abs/2502.01143)** (2025) — Learns a residual "delta action" model from real rollouts to fix sim physics, enabling agile athletic humanoid motions. · [code](https://github.com/LeCAR-Lab/ASAP)
- **[Expressive Whole-Body Control for Humanoid Robots](https://arxiv.org/abs/2402.16796)** (2024) — Imitates upper-body human motion capture while keeping robust legs, giving humanoids expressive gestures and dance.
- **[HumanPlus: Humanoid Shadowing and Imitation from Humans](https://arxiv.org/abs/2406.10454)** (2024) — A humanoid shadows a human from one RGB camera, then learns autonomous skills from the collected data. · [code](https://github.com/MarkFzp/humanplus)
- **[Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](https://arxiv.org/abs/2403.04436)** (2024) — H2O — an RL tracking policy lets an RGB camera stream a person's whole-body motion onto a humanoid in real time.
- **[Unitree RL Gym](https://github.com/unitreerobotics/unitree_rl_gym)** (2024) — Unitree's official starting point for RL locomotion on Go2, H1 and G1 — train in Isaac Gym, check sim-to-sim in MuJoCo, then deploy to the real robot.
- **[Extreme Parkour with Legged Robots](https://arxiv.org/abs/2309.14341)** (2023) — An end-to-end depth-camera policy makes a small quadruped do long jumps, high jumps and handstands. · [code](https://github.com/chengxuxin/extreme-parkour)
- **[Robot Parkour Learning](https://arxiv.org/abs/2309.05665)** (2023) — Distills specialist parkour skills into a single vision-based policy that climbs, leaps and crawls on low-cost quadrupeds. · [code](https://github.com/ZiwenZhuang/parkour)
- **[RMA: Rapid Motor Adaptation for Legged Robots](https://arxiv.org/abs/2107.04034)** (2021) — An adaptation module infers environment parameters online, so one policy handles new terrains and payloads in real time.
- **[Learning Quadrupedal Locomotion over Challenging Terrain](https://arxiv.org/abs/2010.11251)** (2020) — A teacher-student, proprioception-only policy that walks ANYmal over mud, snow and rubble in the wild.
- **[Learning Agile and Dynamic Motor Skills for Legged Robots](https://arxiv.org/abs/1901.08652)** (2019) — A learned actuator model closes the sim-to-real gap so RL policies run and recover from falls on ANYmal.
- _See also:_ [Crocoddyl](#control), [Open-TeleVision](#hardware), [Berkeley Humanoid](#hardware), [ToddlerBot](#hardware)

<a id="world-models"></a>
### World Models

_Learned dynamics, video world models and model-based RL for embodied agents._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/world-models.html)

- ⭐ **[Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104)** (2023) — DreamerV3 — one set of hyperparameters works across 150+ tasks, including collecting diamonds in Minecraft from scratch. · [code](https://github.com/danijar/dreamerv3)
- **[Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575)** (2025) — Open video world foundation models plus tokenizers and data pipelines for generating physical-AI training data.
- **[V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985)** (2025) — A self-supervised video encoder, post-trained with a little robot data, plans zero-shot pick-and-place by latent prediction.
- **[DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](https://arxiv.org/abs/2411.04983)** (2024) — Predicts future DINOv2 patch features instead of pixels, so a world model trained on offline data can plan to new visual goals at test time. · [code](https://github.com/gaoyuezhou/dino_wm)
- **[Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391)** (2024) — Learns playable environments and latent actions from unlabeled internet videos alone.
- **[Learning Interactive Real-World Simulators](https://arxiv.org/abs/2310.06114)** (2023) — UniSim — an action-conditioned video model used as a simulator to train policies that transfer to the real world.
- **[TD-MPC2: Scalable, Robust World Models for Continuous Control](https://arxiv.org/abs/2310.16828)** (2023) — An implicit (decoder-free) world model planned with MPC; one set of hyperparameters works across many continuous-control tasks and scales to a multitask agent. · [code](https://github.com/nicklashansen/tdmpc2)
- **[DayDreamer: World Models for Physical Robot Learning](https://arxiv.org/abs/2206.14176)** (2022) — Dreamer trained directly on real robots — a quadruped learns to walk in about an hour with no simulator.
- **[Dream to Control: Learning Behaviors by Latent Imagination](https://arxiv.org/abs/1912.01603)** (2019) — The first Dreamer — learns a latent world model from pixels and trains the policy entirely on imagined rollouts.
- **[World Models](https://arxiv.org/abs/1803.10122)** (2018) — The classic VAE + RNN agent that learns a compressed model of its environment and trains a controller inside the "dream". · [project](https://worldmodels.github.io/)
- _See also:_ [Planning with Diffusion for Flexible Behavior Synthesis](#control)

<a id="navigation"></a>
### Navigation & Embodied Agents

_Vision-language navigation, embodied question answering, mobile manipulation and LLM planners._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/navigation.html)

- ⭐ **[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)** (2022) — SayCan — an LLM proposes steps and learned value functions score what the robot can actually do right now.
- **[Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System](https://arxiv.org/abs/2610.19600)** (2026) — Finds a VLA at 80% on atomic skills drops to 19% when composed into mobile manipulation, diagnoses why, and builds an agentic system around it. · [code](https://github.com/PKU-VaLuE-Lab/Cracking-Mobile-Manipulation)
- **[Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance](https://arxiv.org/abs/2610.20607)** (2026) — HiRe-MoMa fine-tunes a frozen mobile-manipulation policy in the real world by learning residual corrections, with only occasional human guidance. · [project](https://hire-moma.github.io/)
- **[OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics](https://arxiv.org/abs/2401.12202)** (2024) — Combines off-the-shelf open-vocabulary models into a pick-and-drop system that works in real homes without training.
- **[NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](https://arxiv.org/abs/2310.07896)** (2023) — One diffusion policy handles both goal-directed navigation and exploration by masking the goal.
- **[Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753)** (2022) — LLMs write Python that calls perception and control APIs, turning instructions into reactive robot programs.
- **[Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608)** (2022) — Feeding success detection and scene descriptions back to the LLM planner lets it replan after failures.
- **[Visual Language Maps for Robot Navigation](https://arxiv.org/abs/2210.05714)** (2022) — VLMaps fuses visual-language features into a 3D map so robots can navigate to open-vocabulary spatial goals.
- **[Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](https://arxiv.org/abs/1711.07280)** (2017) — Introduced the VLN task and the Room-to-Room (R2R) benchmark in Matterport3D homes.
- _See also:_ [ConceptGraphs](#perception), [Habitat](#datasets), [Embodied Skill Bench](#datasets)

<a id="perception"></a>
### Perception, SLAM & 3D Mapping

_Visual / LiDAR SLAM and odometry, 3D reconstruction, object pose, depth and open-vocabulary scene maps for robots._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/perception.html)

- ⭐ **[ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](https://arxiv.org/abs/2007.11898)** (2020) — The go-to feature-based SLAM library — monocular, stereo and RGB-D, with IMU fusion and multi-map relocalization. · [code](https://github.com/UZ-SLAMLab/ORB_SLAM3)
- **[VGGT: Visual Geometry Grounded Transformer](https://arxiv.org/abs/2503.11651)** (2025) — One feed-forward transformer predicts cameras, depth, point maps and tracks for many views at once, in about a second. · [code](https://github.com/facebookresearch/vggt)
- **[Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](https://arxiv.org/abs/2401.10891)** (2024) — Monocular depth model trained on tens of millions of pseudo-labelled images; a common off-the-shelf depth prior for robots. · [code](https://github.com/LiheYoung/Depth-Anything)
- **[ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650)** (2023) — Builds an object-level 3D scene graph labelled by vision-language models, which an LLM planner can query in natural language. · [project](https://concept-graphs.github.io/)
- **[DUSt3R: Geometric 3D Vision Made Easy](https://arxiv.org/abs/2312.14132)** (2023) — Regresses 3D point maps straight from image pairs without known camera intrinsics or poses; started the "3D foundation model" wave. · [code](https://github.com/naver/dust3r)
- **[FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects](https://arxiv.org/abs/2312.08344)** (2023) — 6D pose estimation and tracking of unseen objects from a CAD model or a few reference images, with no per-object training. · [code](https://github.com/NVlabs/FoundationPose)
- **[Gaussian Splatting SLAM](https://arxiv.org/abs/2312.06741)** (2023) — MonoGS — runs SLAM directly on a 3D Gaussian map, giving camera tracking and a photorealistic dense map from one camera. · [code](https://github.com/muskie82/MonoGS)
- **[DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](https://arxiv.org/abs/2108.10869)** (2021) — End-to-end learned visual SLAM — recurrent optical-flow updates plus a differentiable bundle-adjustment layer. · [code](https://github.com/princeton-vl/DROID-SLAM)
- **[FAST-LIO2: Fast Direct LiDAR-inertial Odometry](https://arxiv.org/abs/2107.06829)** (2021) — Registers raw LiDAR points directly to the map with an incremental k-d tree; fast enough for onboard drone and robot computers. · [code](https://github.com/hku-mars/FAST_LIO)
- **[LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping](https://arxiv.org/abs/2007.00258)** (2020) — LiDAR-inertial odometry built on a factor graph, so GPS and loop closures slot in as extra factors. · [code](https://github.com/TixiaoShan/LIO-SAM)

<a id="control"></a>
### Planning, Control & Safety

_Motion planning, trajectory optimization, MPC, safety filters and safe learning-based control._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/control.html)

- ⭐ **[cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation](https://arxiv.org/abs/2310.17274)** (2023) — GPU-parallel motion generation for arms — many trajectory optimizations run at once, giving collision-free, smooth plans in milliseconds. · [code](https://github.com/NVlabs/curobo)
- **[Sub-Millisecond Reflexes for Continuous Physical Human-Robot Interaction](https://arxiv.org/abs/2610.21913)** (2026) — An open-source ROS 2 multimode controller that switches control modes and triggers safety reflexes in under a millisecond, without stopping the task; shown on a Franka arm. · [code](https://github.com/RoboRef/franka_reflex_engine)
- **[Motion Policy Networks](https://arxiv.org/abs/2210.12209)** (2022) — A neural policy trained on millions of planner-generated trajectories that moves an arm to goals straight from point clouds. · [code](https://github.com/NVlabs/motion-policy-networks)
- **[Planning with Diffusion for Flexible Behavior Synthesis](https://arxiv.org/abs/2205.09991)** (2022) — Diffuser — treats planning as denoising whole trajectories, so goals and rewards can steer sampling; an early link between diffusion and control. · [code](https://github.com/jannerm/diffuser)
- **[Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning](https://arxiv.org/abs/2108.06266)** (2021) — Survey connecting control-theory and RL views of safety, from learned dynamics with guarantees to constrained RL and safety filters.
- **[safe-control-gym: a Unified Benchmark Suite for Safe Learning-based Control and Reinforcement Learning in Robotics](https://arxiv.org/abs/2109.06325)** (2021) — Gym-style benchmark with cart-pole and quadrotor tasks, constraints and disturbances for comparing safe control and safe RL methods. · [code](https://github.com/utiasDSL/safe-control-gym)
- **[Control Barrier Functions: Theory and Applications](https://arxiv.org/abs/1903.11199)** (2019) — Tutorial on control barrier functions — the standard way to wrap any controller in a minimal-change filter that keeps the system safe.
- **[Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control](https://arxiv.org/abs/1909.04947)** (2019) — An open-source DDP-based solver for contact-rich trajectory optimization, widely used for legged and humanoid motion generation and MPC. · [code](https://github.com/loco-3d/crocoddyl)
- **[acados: a modular open-source framework for fast embedded optimal control](https://arxiv.org/abs/1910.13753)** (2019) — Fast nonlinear MPC and estimation solvers with Python/MATLAB interfaces that generate C code for embedded targets. · [code](https://github.com/acados/acados)
- _See also:_ [TD-MPC2](#world-models)

<a id="learning"></a>
### Robot Learning: RL & Imitation

_Reinforcement learning, imitation learning and policy post-training methods for robots, on any embodiment._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/learning.html)

- ⭐ **[Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](https://arxiv.org/abs/2410.21845)** (2024) — HIL-SERL — real-world RL with human corrections, reported to reach near-perfect success on precise assembly and dynamic tasks after a few hours of training. · [code](https://github.com/rail-berkeley/hil-serl)
- ⭐ **[Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)** (2017) — The clipped policy-gradient method behind most GPU-parallel sim-to-real locomotion and dexterity training.
- **[SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning](https://arxiv.org/abs/2401.16013)** (2024) — An open-source stack for training manipulation policies with RL on a real arm — learned reward classifiers, reset-free training and an impedance controller. · [code](https://github.com/rail-berkeley/serl)
- **[Efficient Online Reinforcement Learning with Offline Data](https://arxiv.org/abs/2302.02948)** (2023) — RLPD — a few simple changes to off-policy RL (symmetric sampling of offline and online data, layer norm, ensembles) make prior data speed up online learning. · [code](https://github.com/ikostrikov/rlpd)
- **[Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://arxiv.org/abs/1801.01290)** (2018) — Off-policy RL with an entropy bonus; sample-efficient enough to become the default for learning directly on real robots.
- **[A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://arxiv.org/abs/1011.0686)** (2010) — DAgger — query the expert on the states the learner itself visits, fixing the compounding errors of plain behavior cloning.
- _See also:_ [Unitree RL Gym](#locomotion)

<a id="sim"></a>
### Sim-to-Real & Simulators

_Physics simulators, GPU-parallel training and transfer to real robots._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/sim.html)

- ⭐ **[MuJoCo](https://mujoco.org/)** (2012) — Fast, accurate contact physics; the default simulator for robot learning research, open-sourced by DeepMind. · [code](https://github.com/google-deepmind/mujoco)
- **[Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training](https://arxiv.org/abs/2610.19479)** (2026) — MetaGenSim learns which simulated data to generate, using meta-gradients from real-world performance, instead of sampling the simulator uniformly. · [project](https://meta-gensim.github.io)
- **[MuJoCo Playground](https://arxiv.org/abs/2502.08844)** (2025) — GPU-accelerated MJX environments for locomotion and manipulation that train in minutes and transfer to real robots. · [code](https://github.com/google-deepmind/mujoco_playground)
- **[RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://arxiv.org/abs/2506.18088)** (2025) — Simulation pipeline that writes and checks task code with multimodal LLMs to mass-produce bimanual demos under heavy randomization (clutter, lighting, backgrounds, instructions); also a 50-task dual-arm benchmark. · [code](https://github.com/RoboTwin-Platform/RoboTwin)
- **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** (2024) — An open-source, Python-native physics platform covering rigid bodies, soft bodies, fluids and fast GPU simulation.
- **[ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI](https://arxiv.org/abs/2410.00425)** (2024) — GPU-parallel simulation and rendering with many manipulation tasks; fast visual RL and data generation. · [code](https://github.com/haosulab/ManiSkill)
- **[RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)** (2024) — 120 kitchen scenes, 2,500+ objects and 100 tasks with generated demonstrations for training generalist policies. · [code](https://github.com/robocasa/robocasa)
- **[Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments](https://arxiv.org/abs/2301.04195)** (2023) — The framework that became Isaac Lab — modular robots, sensors and tasks on top of Isaac Sim. · [code](https://github.com/isaac-sim/IsaacLab)
- **[Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning](https://arxiv.org/abs/2108.10470)** (2021) — Keeps physics and policy on the GPU end-to-end, enabling thousands of parallel environments on one card.
- **[SAPIEN: A SimulAted Part-based Interactive ENvironment](https://arxiv.org/abs/2003.08515)** (2020) — A simulator with large-scale articulated objects (PartNet-Mobility) for interaction tasks like opening drawers.
- **[robosuite: A Modular Simulation Framework and Benchmark for Robot Learning](https://arxiv.org/abs/2009.12293)** (2020) — Modular MuJoCo-based manipulation environments behind many imitation-learning benchmarks. · [code](https://github.com/ARISE-Initiative/robosuite)
- **[Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://arxiv.org/abs/1703.06907)** (2017) — Randomizing textures, lighting and cameras in sim makes vision models work on real images with no real data.
- **[Sim-to-Real Transfer of Robotic Control with Dynamics Randomization](https://arxiv.org/abs/1710.06537)** (2017) — Randomizing physical parameters during training yields control policies robust enough to run on a real arm.
- _See also:_ [Blind Precise Assembly](#manipulation), [TACTO](#tactile), [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](#locomotion), [Habitat](#datasets)

<a id="datasets"></a>
### Datasets & Benchmarks

_Large robot datasets, egocentric data and evaluation suites._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/datasets.html)

- ⭐ **[LeRobot](https://github.com/huggingface/lerobot)** (2024) — PyTorch library with datasets, pretrained policies (ACT, Diffusion, SmolVLA) and drivers for low-cost arms.
- ⭐ **[LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)** (2023) — 130 language-conditioned tasks in four suites; now the most common simulation benchmark for VLA papers. · [code](https://github.com/Lifelong-Robot-Learning/LIBERO)
- ⭐ **[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)** (2023) — 1M+ trajectories from 22 robot types pooled by 30+ labs; RT-X models trained on it beat single-robot baselines. · [code](https://github.com/google-deepmind/open_x_embodiment)
- **[Embodied Skill Bench: Benchmarking How Well Agents with Embodied Skills Perform on Physical Tasks](https://arxiv.org/abs/2610.16238)** (2026) — Packages VLA policies, perception models and know-how as 250 reusable "embodied skills" and measures how much they help LLM agents on physical tasks. · [code](https://github.com/HanZhi306/EmbodiedSkill-Bench)
- **[AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://arxiv.org/abs/2503.06669)** (2025) — A million-scale real-robot dataset collected in purpose-built scenes, with the GO-1 generalist policy trained on it.
- **[DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://arxiv.org/abs/2403.12945)** (2024) — 76k teleoperated Franka trajectories collected in hundreds of real scenes across many institutions. · [code](https://github.com/droid-dataset/droid)
- **[Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941)** (2024) — SimplerEnv — real-to-sim environments whose scores correlate with real-robot results for RT-1/Octo-style policies. · [code](https://github.com/simpler-env/SimplerEnv)
- **[RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation](https://arxiv.org/abs/2412.13877)** (2024) — Large real-robot teleoperation dataset across several embodiments (single-arm, dual-arm, humanoid) collected under one standardized protocol, and it keeps failed demos with annotated causes. · [project](https://x-humanoid-robomind.github.io/)
- **[BridgeData V2: A Dataset for Robot Learning at Scale](https://arxiv.org/abs/2308.12952)** (2023) — 60k trajectories on a low-cost WidowX arm across many kitchens and tasks; a common pretraining source.
- **[RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot](https://arxiv.org/abs/2307.00595)** (2023) — 110k+ contact-rich sequences with vision, force, audio and paired human demonstration videos.
- **[CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](https://arxiv.org/abs/2112.03227)** (2021) — Chains of five language instructions in a row test long-horizon, language-conditioned control. · [code](https://github.com/mees/calvin)
- **[Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058)** (2021) — 3,670 hours of first-person daily-life video; widely used to pretrain visual representations for robots.
- **[Habitat: A Platform for Embodied AI Research](https://arxiv.org/abs/1904.01201)** (2019) — A very fast photorealistic 3D simulator and task suite that standardized embodied navigation research. · [code](https://github.com/facebookresearch/habitat-sim)
- **[Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning](https://arxiv.org/abs/1910.10897)** (2019) — 50 Sawyer manipulation tasks for multi-task and meta-RL evaluation. · [code](https://github.com/Farama-Foundation/Metaworld)
- **[RLBench: The Robot Learning Benchmark & Learning Environment](https://arxiv.org/abs/1909.12271)** (2019) — 100 hand-designed manipulation tasks with demos; a staple for 3D policy methods like PerAct. · [code](https://github.com/stepjam/RLBench)
- _See also:_ [Universal Manipulation Interface](#manipulation), [DexGraspNet](#manipulation), [Vision-and-Language Navigation](#navigation), [safe-control-gym](#control), [robosuite](#sim), [RoboCasa](#sim), [RoboTwin 2.0](#sim)

<a id="hardware"></a>
### Hardware & Open-Source Robots

_Low-cost arms, hands, grippers and data-collection rigs you can build._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/hardware.html)

- ⭐ **[LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning](https://arxiv.org/abs/2309.06440)** (2023) — A 16-DoF dexterous hand buildable for about $2,000 from off-the-shelf parts. · [project](https://leaphand.com/)
- **[BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities](https://arxiv.org/abs/2503.05652)** (2025) — A whole-body teleoperation interface plus a learning method for a wheeled bimanual robot doing long household tasks that need reach, balance and navigation. · [project](https://behavior-robot-suite.github.io/)
- **[ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation](https://arxiv.org/abs/2502.00893)** (2025) — A small, 3D-printed open-source humanoid with a matching simulation model, built so that ML policies and teleoperated data transfer to the real robot. · [project](https://toddlerbot.github.io/)
- **[Berkeley Humanoid: A Research Platform for Learning-based Control](https://arxiv.org/abs/2407.21781)** (2024) — A mid-size, low-cost humanoid designed for easy sim-to-real transfer of RL locomotion.
- **[Open-TeleVision: Teleoperation with Immersive Active Visual Feedback](https://arxiv.org/abs/2407.01512)** (2024) — VR teleoperation with an actively steered stereo camera, used to collect humanoid manipulation data. · [code](https://github.com/OpenTeleVision/TeleVision)
- **[SO-ARM100 / SO-101](https://github.com/TheRobotStudio/SO-ARM100)** (2024) — An open 3D-printed 6-DoF arm (leader + follower) costing roughly $100–200 per arm; the default LeRobot starter kit.
- **[GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators](https://arxiv.org/abs/2309.13037)** (2023) — 3D-printed kinematic replicas of robot arms for cheap, intuitive joint-space teleoperation. · [code](https://github.com/wuphilipp/gello_software)
- _See also:_ [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](#manipulation), [Mobile ALOHA](#manipulation), [Universal Manipulation Interface](#manipulation), [DexCap](#manipulation), [DIGIT](#tactile), [AnySkin](#tactile), [ReSkin](#tactile), [Unitree RL Gym](#locomotion), [LeRobot](#datasets)

<!-- radar:end -->

## Related lists & learning resources

Other good maps of the field, plus courses and docs we point newcomers to. This radar complements them with search, a daily feed and bilingual takeaways.

<!-- resources:start -->

**Related lists**

- [Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide) `中文` — A large Chinese-language beginner's guide to embodied AI, from fundamentals to research directions.
- [Embodied_AI_Paper_List (HCPLab-SYSU)](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) — Paper list accompanying a survey of embodied AI, organized by perception, interaction, agents and sim-to-real.
- [awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) — A focused list of humanoid robot learning papers.
- [Awesome-Robotics-Foundation-Models](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models) — Papers on foundation models in robotics, from the survey "Foundation Models in Robotics".

**Courses & textbooks**

- [Robotic Manipulation (MIT 6.4210, Russ Tedrake)](https://manipulation.csail.mit.edu/) — Free online textbook and course on perception, planning and control for manipulation, with Drake notebooks.
- [Underactuated Robotics (MIT, Russ Tedrake)](https://underactuated.mit.edu/) — Free online textbook on nonlinear dynamics, optimal control and trajectory optimization for walking, flying and swimming robots.
- [CS 285 Deep Reinforcement Learning (UC Berkeley)](https://rail.eecs.berkeley.edu/deeprlcourse/) — Sergey Levine's deep RL course; lecture videos and slides are public.

**Tool docs**

- [LeRobot documentation](https://huggingface.co/docs/lerobot) — Hands-on docs for Hugging Face LeRobot — record data, train ACT/diffusion/VLA policies and run them on low-cost arms.
- [Isaac Lab documentation](https://isaac-sim.github.io/IsaacLab/) — Docs and tutorials for NVIDIA's GPU-parallel robot learning framework.
- [MuJoCo documentation](https://mujoco.readthedocs.io/) — Reference and modeling guide for the MuJoCo physics engine (MJX, MJCF, Python bindings).

**Communities**

- [古月居 (GuYueHome)](https://www.guyuehome.com/) `中文` — A long-running Chinese ROS and robotics community with tutorials and forums.

<!-- resources:end -->

## Contribute

Found a great paper, repo, dataset or robot that's missing — or a mistake? [Open an issue](https://github.com/hu-zlatan/embodied-ai-radar/issues/new) or send a pull request that adds one entry to `data/curated/<topic>.yaml`. See [CONTRIBUTING.md](CONTRIBUTING.md).

## How this project is run

This repository is **built and maintained by an AI agent** (Claude, made by Anthropic) that works on a schedule, under the oversight of [@hu-zlatan](https://github.com/hu-zlatan). The agent's brief is [AUTOPILOT.md](AUTOPILOT.md); its notes, decisions and run log are in [`.autopilot/`](.autopilot). Data is never invented: entries that fail verification are fixed or removed.

## License

Code: [MIT](LICENSE). Curated text and data: [CC BY 4.0](LICENSE-DATA.md). arXiv metadata: CC0, from the [arXiv API](https://info.arxiv.org/help/api/index.html) — thank you to arXiv for use of its open access interoperability.
