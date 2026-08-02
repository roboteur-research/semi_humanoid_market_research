# Helios (轮式双臂机器人) — Rokae (珞石)

> Helios is Rokae's 42-DoF wheeled dual-arm humanoid: two 7-DoF force-controlled arms (xMate cobot heritage with joint torque sensors), a 4-DoF torso, 2-DoF head and optional 10-DoF dexterous hands on an omnidirectional base. Marketed under a "posture-vision-force" multimodal control strategy for flexible assembly, sorting and data collection, it debuted in 2025 and showed at Automate 2026 in Chicago. It matters because it transplants genuine industrial force-control IP — not just cobot branding — into the semi-humanoid form factor.

| Field | Value |
|---|---|
| Company | Rokae Robotics (珞石) |
| HQ | Beijing, China |
| Status (2026) | announced / early availability (product page live, Automate 2026 debut; deployments undisclosed) |
| First shown / launch | 2025 (China); international debut Automate 2026, Chicago [S3] |
| Target applications | Flexible assembly, material sorting, precision industrial tasks, kitchen/commercial demos, embodied-AI data collection, education/research [S1] |
| Price | n/a (not disclosed) |
| Availability | Via Rokae direct/industrial channels; regions n/a |

## Design & morphology
Wheeled humanoid: footprint ≤680 × 640 mm; height ≤1,736 mm extended / ≤1,142 mm folded (4-DoF torso provides large vertical travel and forward pitch); weight ~190 kg [S1, vendor-claimed]. DoF budget (42 total): 2 head + 2×7 arms + 4 torso + 2×10 optional dexterous hands + 3 mobile base [S1].

## Locomotion
Omnidirectional wheeled base, max 1.5 m/s, 10 mm obstacle clearance, dual-laser SLAM navigation [S1, vendor-claimed]. Indoor industrial floors.

## Upper body & manipulation
Two 7-DoF force-controlled arms with wrist-cross force control; 650 mm reach per arm; 5 kg payload per arm (excl. end-effector); ±0.1 mm repeatability; joint torque sensors with dual encoders for high-dynamic force control [S1, vendor-claimed]. Optional 10-DoF dexterous hands; standard end-effectors configurable. Real-time human-motion imitation and teleoperation supported [S3, vendor-claimed].

## Sensing
Head: Orbbec Gemini 335L RGB-D camera on 2-DoF neck; optional 3D obstacle-avoidance kit (4 chassis cameras); dual lidar (SLAM); joint torque sensing throughout; microphone + speaker [S1, vendor-claimed].

## Actuation & power
Torque-controlled integrated joints (Rokae xMate lineage; harmonic/planetary details n/a). Battery 48 V 30 Ah (~1.44 kWh), 6 h runtime, 1.5 h charge [S1, vendor-claimed].

## Compute & software
NVIDIA Jetson AGX Orin NX 8GB (117 TOPS) or AGX Orin 64GB (275 TOPS) options; Ethernet + WiFi; ROS 2 compatible; "posture-vision-force" multimodal fusion control for autonomous navigation and manipulation without environment modification; teleop/data-collection modes [S1, vendor-claimed]. SDK openness n/a beyond ROS 2 claim.

## Safety & compliance
n/a (not disclosed) for Helios; Rokae's cobot lines carry standard industrial certifications (CE etc.) — likely path for Helios [estimated].

## Deployment evidence & traction
Product page live with full datasheet-grade specs (unusual maturity for the category); Automate 2026 Chicago exhibition [S3]. No named customers, pilots or volumes disclosed [as of 08/2026]. Application videos show assembly/sorting/kitchen demos [S1, vendor media].

## Assessment (analyst view)
*Analyst opinion.* Strengths: real force-control pedigree (shipped torque-sensing cobots), complete published specs, sensible industrial positioning, folding 1.14-1.74 m torso giving a large vertical workspace, and export channels including a US trade-show presence. Weaknesses: 5 kg/arm and 650 mm reach are modest; 190 kg mass is high; no disclosed price, safety certification, or deployments; AI/autonomy stack unproven vs VLA-native startups. Threat to an EU entrant: high in industrial semi-humanoids — Rokae is exactly the profile (credible arms + Chinese cost base + Western trade-show push) that will compress pricing in EU/US flexible-assembly niches.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.rokae.com/cn/product/show/583/轮式双臂机器人Helios.html (EN: /en/product/show/596/Wheeled-Dual-Arm-Robot-Helios.html) | Full specs: 42 DoF breakdown, dims, 190kg, 650mm/5kg arms, ±0.1mm, 1.5 m/s, 48V30Ah/6h, Orin compute, sensors | vendor-claimed |
| 2 | https://www.rokae.com/ | Company/product line context | vendor-claimed |
| 3 | https://www.originofbots.com/news/rokae-unveils-helios-wheeled-humanoid-robot-for-real-world-industrial-automation | Unveiling, Automate 2026 Chicago debut, teleop/imitation capabilities | third-party |
