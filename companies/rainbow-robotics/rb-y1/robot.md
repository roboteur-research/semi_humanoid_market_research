# RB-Y1 (이동형 양팔로봇 RB-Y1) — Rainbow Robotics

> The RB-Y1 is a wheeled "bimanual mobile manipulator": two 7-DoF arms and a 6-DoF articulated torso column on a fast (up to 2.5 m/s) two-wheel-drive base. Sold openly since May 2024 at $80k (research) / $120k (commercial), it became the de-facto standard non-Chinese semi-humanoid research platform (MIT, UC Berkeley, UW, Georgia Tech) and passed 100 units sold in 2025. With Samsung as controlling shareholder and a Coupang warehouse pilot underway, it is the benchmark competitor for any EU semi-humanoid entrant.

| Field | Value |
|---|---|
| Company | Rainbow Robotics (Samsung Electronics consolidated subsidiary) |
| HQ | Daejeon, South Korea |
| Status (2026) | shipping |
| First shown / launch | Unveiled March/April 2024; pre-orders 8 May 2024; deliveries from Oct 2024; Mecanum option + integrated SDK at ICRA 2025 [S1][S2][S4] |
| Target applications | AI research platform (imitation learning/VLA), logistics sorting, manufacturing tasks |
| Price | $80,000 research platform / $120,000 commercial platform, VAT excl. (2024 pre-order pricing) [S2] |
| Availability | Global (US subsidiary Schaumburg, IL); direct purchase; ~20 units/month capacity (2025) [S6] |

## Design & morphology
Single-column "leg" architecture: a 6-DoF articulated torso (knee/waist-like joints) carrying a dual-arm upper body on a wheeled base. Dimensions 600 × 690 × 1,400 mm; torso gives >50 cm of vertical travel (floor pick to shelf height). Weight 131 kg total (upper body 38 kg, "leg" 42 kg, mobile base 51 kg). 24 DoF total: 2×7 (arms) + 6 (torso) + 2×1 (grippers) + 2 (wheels). [S1][S3]

## Locomotion
Two-wheel differential drive with casters (stock); operating speed 1.5 m/s (official spec), max 2.5 m/s reported at launch — fast for the class. Optional Mecanum omnidirectional wheel kit (ICRA 2025) for 360° movement in constrained spaces. No stair/step capability claimed. [S1][S2][S4]

## Upper body & manipulation
Two 7-DoF arms, 3 kg payload each (vendor). 1-DoF parallel grippers standard; gripper, IMU and lidar modules exchangeable via the integrated SDK's module support. Optional master-arm teleoperation rig (sold as accessory) for bimanual data collection — the standard imitation-learning workflow on this platform. Whole-body control ("20-axis full-body control" with CoM management) lets the torso extend the workspace from floor level to ~2 m. No dexterous hand offered by Rainbow to date; third-party hands (e.g. from research labs) are commonly fitted. Repeatability n/a (not disclosed). [S1][S2]

## Sensing
Base lidar for navigation; optional 3D recognition (RGB-D) sensor on head plate; IMU. Detailed camera loadout is configuration-dependent and not fully disclosed. Force/torque and tactile sensing: n/a (not disclosed). [S1][S2]

## Actuation & power
Actuators derived from Rainbow's in-house cobot and AMR actuators (precision servo, not QDD; exact type not disclosed). Battery 50 V / 25 Ah = 1,270 Wh; runtime n/a (not disclosed); hot-swap not claimed. [S1]

## Compute & software
Onboard control PC; optional user PC (UPC) for AI workloads (vendor docs; details vendor-claimed). Open SDK on GitHub (rby1-sdk, C++/Python) with web manual; URDF/sim assets available, including NVIDIA Isaac Sim integration. Positioning is explicitly "robot platform for AI researchers": open APIs, modular design, imitation-learning-ready via master arm. Teleoperation was the primary mode at launch; autonomy comes from customer AI stacks (several labs run VLA models incl. NVIDIA GR00T-family models on it — GR00T demo usage is reported but not independently confirmed). [S1][S2][S4]

## Safety & compliance
No ISO 13482/10218 or CE certification claims published for the platform. E-stop and collision-avoidance via lidar; safety case currently rests on research-platform usage. [estimated — absence of claims]

## Deployment evidence & traction
- Pre-orders/units: >100 units sold during 2025, ~130+ cumulative by late 2025; ~50 units in H1 2025 (third-party Korean press). [S6]
- Research customers: MIT, UC Berkeley, University of Washington, Georgia Tech (vendor-claimed, echoed by trade press). [S4]
- Coupang: RB-Y1 pilot in a Coupang fulfillment center (sorting/moving trial) — first commercial logistics deployment. CONFIRMED by Korean press as early as 2026-01-15 (nate.com/Korean wire coverage), then covered internationally in June 2026. Talks with CJ Logistics reported. [S5][S8]
- Schaeffler/KETI MoU (Apr 2024) for mobile manipulator co-development. [S2]
- Supply chain: Korean actuator component supplier SPG ramping for Rainbow volumes (third-party). [S6]

## Assessment (analyst view)
*Analyst opinion.* Strengths: the only non-Chinese semi-humanoid with real installed base and open pricing; strong academic mindshare (the "default lab robot" outside China); Samsung ownership de-risks supply and funding; fast base and 6-DoF torso give a genuinely large workspace. Weaknesses: 3 kg/arm payload is light for industrial work; simple 1-DoF grippers; autonomy left to customers; no safety certification path published. Threat to an EU entrant: high — it owns the research/developer channel through which VLA-era applications will be built, and Samsung/Coupang pilots signal commercial scaling; an EU entrant must differentiate on payload, certification (CE/ISO 13482) and integrated autonomy rather than platform openness alone.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.rainbow-robotics.com/rby1 | dimensions, 131 kg, 24 DoF, 3 kg/arm, 1.5 m/s, 1,270 Wh, SDK | vendor-claimed |
| 2 | https://www.rainbow-robotics.com/en_pr/20240508 (+ roboticstomorrow.com syndication) | $80k/$120k pricing, pre-order/delivery dates, lidar, optional 3D sensor & master arm | vendor-claimed |
| 3 | https://www.therobotreport.com/rainbow-robotics-unveils-rb-y1-wheeled-two-armed-robot/ | 2.5 m/s max, >50 cm vertical travel, launch, Schaeffler/KETI | third-party |
| 4 | https://www.therobotreport.com/rainbow-robotics-unveils-omnidirectional-wheels-development-kit-dual-arm-robot/ | Mecanum option + SDK at ICRA 2025, MIT/Berkeley/UW/GT, Samsung 35% | third-party |
| 5 | https://www.koreaherald.com/article/10771827 (also techtimes.com/articles/318386) | Coupang fulfillment-center pilot, June 2026 | third-party |
| 6 | Korean press via DDG (레인보우로보틱스 RB-Y1 100대 판매; incl. aitimes.kr) | 100-unit milestone 2025, 130+ cumulative, 20/month capacity | third-party |
| 7 | https://www.aitimes.kr/news/articleView.html?idxno=35384 | ICRA 2025 details, CTO quote, US YouTube traction | third-party |
| 8 | nate.com news (Korean wire), 2026-01-15 | Coupang pilot confirmation (earliest report) | third-party |
