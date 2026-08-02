# Cobot Magic — AgileX Robotics (松灵)

> Cobot Magic is AgileX's productized Mobile ALOHA: four arms (two leader for human teleop, two follower for execution) with wrist + top cameras on the Tracer differential AGV base, shipping since 2024 as a turnkey imitation-learning/data-collection platform that runs the complete open-source Mobile ALOHA code. As the commercial descendant of the Stanford system built on AgileX's own chassis, it is the reference low-cost mobile bimanual research rig worldwide.

| Field | Value |
|---|---|
| Company | AgileX Robotics (松灵机器人) |
| HQ | Shenzhen/Dongguan, China |
| Status (2026) | shipping (research market, global distributors) |
| First shown / launch | 2024 [S3] |
| Target applications | Embodied-AI research: imitation-learning data collection (ALOHA/ACT/π0-class), mobile manipulation experiments, education |
| Price | ~$48k class via distributors (₹3,999,999 India listing); config-dependent; base PiPER arm $1,999 [third-party] |
| Availability | Global via distributor network (Generation Robots EU, robosavvy UK, MG Super Labs IN, etc.) |

## Design & morphology
Tracer differential AGV base (685 × 570 × 155 mm, 28-30 kg GVW, 100 kg load capacity) carrying a pedestal with four robot arms: 2 leader (teleop input) + 2 follower (execution), each 6 DoF [S2, distributor datasheet]. Newer configs offer PiPER-based arm options [S1]. No head/torso anthropomorphism — pure functional bimanual rig.

## Locomotion
Two-wheel differential drive (Tracer); AgileX remote controller included; AC 220 V independent charger, 4 h charge [S2]. Speed n/a in datasheet (Tracer base ~1.6 m/s class [estimated]).

## Upper body & manipulation
Follower arms: 6 DoF, 509 mm reach, 1 mm repeatability, 1.5 kg rated / 3 kg peak load each (customized arms; PiPER variants similar class) [S2]. Grippers standard (gripper ROS package provided). Leader-follower teleoperation is the core interaction: human puppeteers leader arms, data recorded for ACT/imitation training [S2][S3].

## Sensing
Orbbec DABAI depth cameras (depth 0.3-3 m, 640×400@30FPS; RGB 1080p) — 2 wrist + 1 top camera config [S2][S4]; CH110 9-axis IMU; lidar package supported; 4G router (Huawei B535) for connectivity [S2].

## Actuation & power
Arm actuation: integrated servo joints (details n/a). Base battery in Tracer chassis (capacity n/a, 4 h charge) [S2].

## Compute & software
NVIDIA Jetson Orin Nano 8GB dev kit for data acquisition; industrial PC options in higher configs [S2][S4]. OS: Ubuntu 18.04 + ROS Melodic (datasheet config; newer ROS 2 support via AgileX repos); tools: Gazebo, MoveIt, rviz, rqt; SLAM: amcl, gmapping, RF2O; full open-source demo + secondary development docs; runs complete Mobile ALOHA open-source code [S2][S3, vendor-claimed].

## Safety & compliance
Research platform; chassis certificate included; no ISO/CE robot-level certification published (n/a).

## Deployment evidence & traction
Sold globally through established distributors (Generation Robots EU datasheet, robosavvy UK, Indian resellers); ROS Discourse community presence; AgileX bases underpinned the original Stanford Mobile ALOHA — the strongest possible research-lineage credential [S2][S3][S5]. Unit counts n/a.

## Assessment (analyst view)
*Analyst opinion.* Strengths: authentic Mobile-ALOHA lineage, global distribution and support, open software, and modular AgileX chassis ecosystem; the leader-follower 4-arm design is the proven lowest-friction way to collect bimanual demonstration data. Weaknesses: 1.5 kg-class arms and AGV base make it strictly a research tool; Ubuntu 18.04/ROS Melodic-era software in the base datasheet shows product-maintenance lag; humanoid-form competitors (Galaxea R1, ARX LIFT2) offer more workspace per yuan. Threat to an EU entrant: none commercially, but it owns the mindshare of the entry-level research segment an EU player might otherwise seed its ecosystem with.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://global.agilex.ai/products/cobot-magic | Product listing, PiPER options | vendor-claimed |
| 2 | https://static.generation-robots.com/media/cobot-magic-spe.pdf | Full spec sheet: Tracer base dims, arm specs (6 DoF/509mm/1.5-3kg/1mm), Orbbec DABAI, Orin Nano, ROS stack, packing list | third-party (distributor datasheet) |
| 3 | https://discourse.openrobotics.org/t/cobot-magic-mobile-aloha-system-works-on-agilex-robotics-platform/36515 | Runs Mobile ALOHA code; higher config/lower cost claim | third-party |
| 4 | Search snippets (4 arms, 2 wrist + 1 top camera, ~$48k India listing) | Configuration and price class | third-party |
| 5 | _work/discovery_china.md entry 29 | Stanford Mobile ALOHA base supplier lineage | third-party (compiled) |
