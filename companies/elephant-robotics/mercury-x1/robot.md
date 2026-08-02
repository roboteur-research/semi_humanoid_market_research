# Mercury X1 — Elephant Robotics (大象机器人)

> The Mercury X1 is a 1.18 m, 19-DoF wheeled semi-humanoid for education, research and embodied-AI development: the dual-arm Mercury B1 torso (17 DoF, LCD-face head) mounted on a lidar-equipped AGV base. At a published $15,999 it is one of the cheapest complete wheeled dual-arm humanoids on the market, competing on price and open software (ROS/MoveIt/Gazebo/Mujoco, Python/C++) rather than payload (1 kg/arm). This dossier also covers the Mercury B1 torso sibling.

| Field | Value |
|---|---|
| Company | Elephant Robotics (Shenzhen) |
| HQ | Shenzhen, China |
| Status (2026) | shipping |
| First shown / launch | Announced Dec 2023; CES 2024 debut; shipping 2024– |
| Target applications | University education, embodied-AI/VLA research, imitation-learning data collection, light service demos |
| Price | X1: USD 15,999 (vendor shop, third-party confirmed [S4]); B1 torso: ~EUR 17,599 at EU reseller OpenELAB [S5] (reseller markup; vendor bundle pricing lower); A1 single arm ~GBP 3,785 [S3] |
| Availability | Global via own web shop + resellers (RobotShop, OpenELAB, OzRobotics, Robot Pi Shop); made-to-order, direct purchase (no RaaS) |

## Design & morphology
Humanoid torso on wheeled AGV base. Height 1.18 m, net weight 55 kg (vendor spec page [S2]; shop lists 62.5 kg shipping config [S3]). 19 DoF total: two 7-axis arms + head + base [S1][S2]. The torso is the Mercury B1: dual 7-DoF arms (17 DoF, 11.2 kg torso weight), head with 9-inch HD LCD touchscreen showing customizable expressions [S3][S6]. 15 L storage space in the base [S2]. No torso lift column (fixed torso height).

## Locomotion
High-performance wheeled base (differential AGV type), max 1.2 m/s, climbs 15° slopes and 2 cm obstacles [S1][S2]. Vendor-claimed.

## Upper body & manipulation
Two Mercury A1-derived 7-axis arms: 450 mm working radius each, 1 kg payload per arm, repeatability ±0.05 mm (vendor-claimed [S2][S3]). Carbon-fiber/aluminium arm construction. Standard myCobot-ecosystem end effectors (parallel grippers, suction pumps) attach at the flange; no dexterous hand standard. Media at flange: n/a (not disclosed).

## Sensing
Head: Orbbec Deeyea 3D camera, 4-mic array (5 m pickup, 180°) [S2]. Base: lidar, ultrasonic sensors, 2D vision for navigation [S1][S2]. No force/torque or tactile sensing disclosed.

## Actuation & power
In-house harmonic "Power Spring" joint modules with electromagnetic brakes [S3]. 24 V working voltage, up to 8 h runtime per charge [S2]; battery capacity kWh n/a (not disclosed). No hot-swap disclosed.

## Compute & software
Current builds: NVIDIA Jetson Orin Nano SUPER 8GB (67 TOPS) main controller + 128-CUDA-core base controller [S2]; earlier units used Jetson Xavier NX + ESP32 motor boards [S4]. ROS 1/2, MoveIt, Gazebo, Mujoco support; Python (pymycobot) and C++ (Mercury API); myBlockly visual programming; ChatGPT/LLM voice interaction [S1][S6]. Teleoperation via the myController S570 wearable exoskeleton with 1:1 joint mapping for imitation-learning data collection [S1]. CAN bus, WiFi, Bluetooth, Ethernet, USB serial; 24 V 6-in/6-out IO [S2].

## Safety & compliance
Electromagnetic joint brakes; collaborative-class speeds/payloads. No ISO 13482/10218 or CE certification claims found — n/a (not disclosed).

## Deployment evidence & traction
Sold openly through multiple international resellers since 2024 (third-party listings confirm commercial availability [S4][S5]). Unit numbers not disclosed; the company's 10,000+ myCobot install base suggests a functioning education/research channel. No industrial deployments claimed. Confidence: third-party for availability, n/a for volumes.

## Assessment (analyst view)
*Analyst opinion.* Strengths: unmatched price point (~$16k) for a complete mobile bimanual humanoid, mature open SDK, global self-serve distribution, and a cheap exoskeleton teleop accessory — a plausible default platform for embodied-AI coursework and small labs. Weaknesses: 1 kg per-arm payload, 450 mm reach and no force/tactile sensing rule out real industrial work; compute (Orin Nano) is light for onboard VLA inference. Threat to an EU entrant targeting commercial/industrial semi-humanoids is low in direct competition, but Elephant anchors low price expectations in the research segment and could crowd out higher-priced EU research platforms in universities.

## Mercury B1 (sibling, torso-only)
Mercury B1 = the X1's upper body sold standalone for desktop/bench research: dual 7-axis arms, 17 DoF, 11.2 kg, 9-inch LCD head with expressions, Orbbec 3D camera, 4-mic array, Jetson (Xavier 21 TOPS in early units, Orin Nano 40 TOPS current), same software stack and S570 teleop support [S3][S5][S6]. EU reseller price ~€17.6k [S5].

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.elephantrobotics.com/en/mercury-x1-en/ | overview, 19 DoF, base specs, software, S570 | vendor-claimed |
| 2 | https://www.elephantrobotics.com/en/mercury-x1-specifications-en/ | full spec table (height, weight, payload, compute, sensors) | vendor-claimed |
| 3 | https://shop.elephantrobotics.com/products/mercury-humanoid-robot-series | A1/B1/X1 variants, prices, Power Spring joints | vendor-claimed |
| 4 | https://www.cnx-software.com/2024/11/22/mercury-x1-wheeled-humanoid-robot-combines-nvidia-jetson-xavier-nx-ai-controller-and-esp32-motor-control-boards/ | $15,999 price, Xavier NX/ESP32 architecture | third-party |
| 5 | https://openelab.io/products/elephant-robotics-mercury-b1-dual | B1 price €17,598.90, B1 specs | third-party (reseller) |
| 6 | https://docs.elephantrobotics.com/docs/Mercury_B1_en/ | B1 architecture, head/controllers | vendor-claimed |
