# AGIRobots Worker — AGIRobots

> AGIRobots Worker (formally unveiled 2026-03-02, primary coverage: robotstart.info) is a wheeled semi-humanoid factory worker from Nagoya startup AGIRobots: ~70kg, dual 4kg-payload arms, swerve-drive omnidirectional base, rising/lowering torso, QDD actuation, teleop-driven imitation learning. It is the first purely-domestic Japanese startup answer to China's wheeled humanoid workers, marketed explicitly under the セミヒューマノイド label with a "data collection factory" Physical-AI business model; factory PoCs are slated for FY2026.

| Field | Value |
|---|---|
| Company | AGIRobots Inc. |
| HQ | Nagoya, Japan |
| Status (2026) | announced (basic development complete; PoC partners being recruited) |
| First shown / launch | Officially unveiled 2026-03-02; live demo at Robot Technology Japan 2026 (booth D29) |
| Target applications | Manufacturing & logistics warehouses: picking from low positions, high placement, inter-process transport — without factory layout changes |
| Price | n/a (not disclosed) |
| Availability | Japan; FY2026 factory PoCs; production/sales infrastructure in preparation |

## Design & morphology
Wheeled semi-humanoid, body weight ~70kg [S1]. Upper body with vertical elevation (rising/lowering) mechanism to span low picks to high placements [S1][S2]. Height/DoF counts n/a (not disclosed).

## Locomotion
Swerve-type wheel modules (steered wheels) giving smooth omnidirectional/parallel movement on flat factory floors — chosen over legs for speed and stability on Japanese factory/warehouse flooring [S1][S2].

## Upper body & manipulation
Dual arms, 4kg payload per arm; higher-capacity models planned [S1]. Arms designed for easy detachment with future user-side unit swapping [S1]. End-effectors modular: standard parallel-link gripper with integrated camera, upgrade path to a five-finger hand [S1].

## Sensing
Face: dual wide-angle cameras (teleop, environment recognition, task monitoring) + display for status/communication + speaker (future voice dialogue) [S1]. Base: 3D LiDAR front and rear for SLAM navigation and obstacle avoidance [S1][S2].

## Actuation & power
QDD (quasi-direct-drive) motors; currently third-party QDD units, with fully in-house QDD actuator production targeted from FY2026 (also to be sold for hands/mechanisms) — high responsiveness, controllability, maintainability claimed [S1][S2]. Battery/runtime n/a.

## Compute & software
"Physical AI" architecture: teleoperation-based imitation learning transfers skilled workers' techniques; robots in the field feed a "data collection factory" for continuous model improvement [S1][S2]. Companion apps planned: AGIRobots Studio Go (smartphone teleop) and AGIRobots Studio VR [S1]. Autonomy stack: LiDAR/camera SLAM [S2]. SDK/ROS support n/a.

## Safety & compliance
n/a (not disclosed; pre-PoC stage).

## Deployment evidence & traction
None yet: basic development complete, factory PoC verification planned within FY2026, implementation/joint-verification partners being recruited [S1][S2]. Exhibition: Robot Technology Japan 2026 live demo [S1]. Third-party coverage: robotstart.info, Innovatopia, LogiToday [S2][S3].

## Assessment (analyst view)
*Analyst opinion.* AGIRobots Worker is a faithful Japanese clone of the Chinese wheeled-worker formula (QDD + swerve base + lift torso + teleop imitation learning) wrapped in a "pure domestic" flag that will resonate with Japanese factory buyers wary of Chinese robots — and its data-collection-factory framing mirrors AgiBot/Galbot playbooks. Execution risk is maximal: a 2024-incorporated blog-born startup with undisclosed funding, 4kg arms, and no deployments, entering against imported Chinese hardware that is years ahead on cost curve. Threat to an EU entrant is negligible today, but it is the bellwether for domestically-branded semi-humanoid competition in Japan, and its QDD-actuator side business could outlive the robot.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://prtimes.jp/main/html/rd/p/000000005.000152095.html | full unveiling release: 70kg, 4kg/arm, swerve drive, sensors, QDD, apps, PoC/exhibit plans | vendor-claimed |
| 2 | https://robotstart.info/article/2026/03/02/381662.html | unveiling coverage, SLAM, in-house QDD FY2026, partner recruitment | third-party |
| 3 | https://innovatopia.jp/robot/robot-news/106664/ | "Worker" name, data-collection-factory concept coverage | third-party |
