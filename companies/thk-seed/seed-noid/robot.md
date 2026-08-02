# SEED-Noid / SEED-R7 series (シードノイド) — THK / SEED Solutions

> SEED-Noid is THK's life-size upper-body humanoid, sold since June 2021 as part of the modular SEED-R7 platform series — Noid (dual-arm torso) + Lifter (vertical unit) + Mover (omnidirectional cart) — built entirely on THK's daisy-chained "smart actuators". It is a development platform for service-robot builders rather than an end application robot, with World Robot Summit platform heritage and open ROS packages, and it showcases the component giant THK's play for the wheeled-humanoid supply chain.

| Field | Value |
|---|---|
| Company | THK Co., Ltd. (SEED Solutions business) |
| HQ | Tokyo, Japan |
| Status (2026) | shipping (platform sales, orders since 2021-06-01) |
| First shown / launch | SEED-Noid platform era ~2016-2018 (WRS ecosystem); SEED-R7 series commercial order start 1 June 2021 |
| Target applications | Platform for service-robot development: reception, convenience-store/backroom tasks, research (teleop + autonomous) |
| Price | n/a (not disclosed; quotation-based, units sold individually) |
| Availability | Japan, B2B direct from THK; units purchasable separately (Noid / Lifter / Mover) |

## Design & morphology
Modular three-unit architecture [S1][S2]:
- **SEED-Noid** — life-size upper-body humanoid (等身大上体ヒューマノイド): two 7-DoF arms with grippers, 2-DoF waist, head/neck; upper-body DoF ~20 (academic description: "dual-arm robot with 20 DoF on the lifter") [S3].
- **SEED-Lifter** — vertical elevation unit (2-DoF lifter mechanism) letting the torso work from floor to shelf height; full stack height ~141-170cm via prismatic travel (third-party) [S4].
- **SEED-Mover** — omnidirectional wheeled cart (4 omni wheels) [S4].
Full-stack weight ~80kg (third-party, R7F configuration) [S4].

## Locomotion
SEED-Mover omnidirectional base, 4 omni wheels; speed n/a (not disclosed). Navigation supported via ROS navigation stack in official packages [S5].

## Upper body & manipulation
Two 7-DoF arms with parallel grippers; grasp/release exposed as ROS services with force-percentage argument [S5]. Payload n/a (not disclosed; convenience-store item scale — hundreds of grams to low kg, estimated). Waist 2 DoF widens the workspace between lifter and arms [S2][S3].

## Sensing
Third-party description of R7F configuration: two 3D cameras (head + chest), two laser range sensors (0.06-4m, 120°), six ultrasonic sensors (0.02-3m) on the base [S4] (medium confidence). Chest touchscreen/tablet interface option [S4].

## Actuation & power
THK SEED smart actuators throughout — compact integrated servo units with simplified daisy-chain wiring, low power consumption; unitized mechatronics is the series' core selling point [S1][S2]. Power: 2× 12V/22Ah lead batteries in mobile configuration (third-party) [S4].

## Compute & software
Linux mini-PC controller onboard; ROS (Kinetic/Melodic/Noetic) with official open packages `seed_r7_ros_pkg` (MoveIt manipulation, navigation, smart-actuator SDK `seed_smartactuator_sdk`) [S5]. Teleoperated and autonomous operation both supported [S1].

## Safety & compliance
n/a (not disclosed). Platform product; safety engineering left to the integrating customer.

## Deployment evidence & traction
- Order intake open since 2021-06-01; units sold individually to service-robot developers [S1].
- NTT Communications adopted SEED-Noid-Mover in its ExTorch Open Innovation Program (05/2021) [S6].
- WRS-era platform heritage: SEED-Noid served as a common research platform (convenience-store robotics challenges, ~2018) and appears in multiple academic papers [S3] (third-party).
- No public unit counts or commercial end deployments (n/a).

## Assessment (analyst view)
*Analyst opinion.* SEED-R7's importance is architectural and industrial, not commercial: THK productized the exact modular decomposition (torso / lift / omni base) that today's semi-humanoids use, and it functions as a live demo of THK's smart-actuator catalogue — the real business is selling components into everyone else's humanoids. As a robot, it is dated (lead batteries, ROS 1, gripper-only hands) and traction looks thin. Threat to an EU entrant: negligible as a competing product; significant as evidence that Japan's premier motion-component supplier wants to be in every humanoid BOM — a potential supplier, not a rival.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://prtimes.jp/main/html/rd/p/000000010.000069594.html | series launch 2021-06-01, unit lineup, smart actuators, teleop/autonomous | vendor-claimed |
| 2 | https://www.automation-news.jp/2021/06/56672/ | series composition, unitized mechatronics positioning | third-party |
| 3 | https://www.researchgate.net/figure/Overview-of-SEED-Noid_fig1_365005554 | 2-DoF lifter + 20-DoF dual-arm upper body (academic) | third-party |
| 4 | https://mahamohsin310.medium.com/seed-noid-r7f-an-anthropomorphic-robot-c84ff2865c60 | R7F config: 141-170cm, ~80kg, sensors, batteries, omni wheels | third-party (medium confidence) |
| 5 | https://github.com/seed-solutions/seed_r7_ros_pkg | ROS packages, MoveIt/nav, gripper services | vendor-claimed |
| 6 | https://www.thk.com/jp/ja/news/products/article-17052021-1.html | NTT Com ExTorch adoption | vendor-claimed |
