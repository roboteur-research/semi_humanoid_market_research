# X1 / X1-PRO (仙工 X1 PRO) — SEER Robotics
*(incl. C1-D universal humanoid chassis — the chassis-supplier angle)*

> X1-PRO is SEER's wheeled humanoid for logistics and industrial handling: 40 DoF, dual 7-DoF arms (6 kg each, 16 kg dual-arm short-term), a 45°-bending waist plus 700 mm height adjustment, an omnidirectional chassis with a cargo buffer tray, and SEER's SRC-5000 "embodied brain" controller. It matters twice over: as a robot it is a credible tote-and-shelf logistics worker (IEEE RAS product-innovation award 2026, WAIC 2026 double-venue demos), and as a platform strategy it is the reference design for SEER's real business — selling the C1-D universal humanoid chassis and SRC embodied controllers to OTHER humanoid makers, industrializing the wheeled-humanoid supply base.

| Field | Value |
|---|---|
| Company | SEER Robotics (仙工智能) |
| HQ | Shanghai, China |
| Status (2026) | shipping (early): wheeled humanoid delivered to customer sites for trials since 2024/25; X1-PRO in logistics pilots [S5][S6] |
| First shown / launch | Wheeled humanoid on SRC-5000 demoed CIIF Sept 2024; X1 working demos WRC Aug 2025; X1-PRO upgrade at CeMAT ASIA Oct 2025; headline showing (with C1-D) at WAIC July 2026 [S1][S4][S5] |
| Target applications | Intralogistics: tote/bin handling, sorting, machine tending in 3C, semiconductor, automotive, warehousing; service demos (beverage handout) [S1][S2] |
| Price | n/a (not disclosed) |
| Availability | China (direct + integrator ecosystem); C1-D chassis and SRC-5000 sold to third-party humanoid builders [S2][S3] |

## Design & morphology
Wheeled semi-humanoid: omnidirectional chassis, torso with bending waist (45° forward bend for low picks) and 700 mm vertical height adjustment, dual 7-DoF arms, sensorized head; 40 DoF total (vendor-claimed) [S1]. A cargo buffer tray/platform on the chassis lets the robot carry what it picks — a deliberate logistics-workflow feature [S1]. Height/weight: n/a (not disclosed).

**C1-D universal humanoid chassis (sold separately):** 650×650 mm footprint (~15% smaller than typical humanoid chassis), 820 mm turning diameter, 150 kg payload, passes 800 mm industrial aisles; low center of gravity (power/drives mounted low) to suppress pitch during acceleration, e-braking and dual-arm exertion; millisecond-response electromagnetic dual-brake system [S2][S3].

## Locomotion
Omnidirectional wheeled drive (X1-PRO and C1-D). Speed/gradeability: n/a (not disclosed). C1-D stability engineering (CG placement, dual brakes) is the differentiator claim [S3].

## Upper body & manipulation
Dual 7-DoF arms; 6 kg standard payload per arm, 16 kg dual-arm short-duration maximum [S1]. 45° waist bend + 700 mm lift give a floor-to-high-shelf workspace. End-effectors: application grippers (tote-edge grippers visible in WAIC photos); dexterous-hand options n/a. Repeatability: n/a (not disclosed).

## Sensing
Head with sensor visor (cameras; exact suite n/a); hand-eye-foot coordinated visual servoing enabled by the SRC-5000 whole-body controller [S6]. Base sensing inherited from SEER's AMR stack (lidar-based SLAM navigation — estimated from controller lineage). Force/tactile: n/a (not disclosed).

## Actuation & power
Actuator types, battery, runtime: n/a (not disclosed). C1-D: electromagnetic dual brakes, industrial-grade 150 kg-payload drivetrain [S3].

## Compute & software
SRC-5000 integrated "embodied AI controller": heterogeneous AI chips + coprocessors, claimed world-first integrated whole-body control ("brain + cerebellum" in one box), breaking the hand-eye-foot coordination bottleneck [S6]. (WAIC 2026 materials pair the C1-D chassis itself with the SRC-4000 brain — two controller tiers in the ecosystem [S5].) Software: VLA-model-based perception-language-action stack with LLM task interaction; SEER claims few-sample, short-training generalization per new scenario; M4 fleet-management for unified scheduling; Roboshop/Robocare dev-and-ops toolchain; 500,000+ h of real-world data feeding training [S1][S5]. Open-platform SDK is core to the business model.

## Safety & compliance
C1-D: millisecond electromagnetic dual-brake, stability-by-design claims [S3]. Certifications: n/a (not disclosed; SEER's AMR controller line is widely certified — estimated carry-over).

## Deployment evidence & traction
- Wheeled humanoid units delivered to customer sites for trial use since the SRC-5000 launch (vendor-claimed via industry press) [S6].
- X1 shown doing real tote work at WRC 2025 ("真干活" — actually works — framing) [S4]; X1-PRO demos at CeMAT ASIA 2025 and WAIC 2026 (tote transfer, beverage handout to visitors) [S1][S5].
- 2026 IEEE Robotics & Automation Product Innovation Award for X1-PRO (vendor-claimed) [S5].
- Platform traction is the stronger evidence: 50,000+ SRC controllers installed and 2,100+ customers give the humanoid line an instant channel [S5][S7].

## Assessment (analyst view)
*Analyst opinion.* Strengths: the only Tier-2 player whose humanoid rides on a proven, mass-deployed industrial control stack; concrete logistics-relevant numbers (6/16 kg, 45° bend, 700 mm lift, buffer tray); and a two-sided model — if X1-PRO fails commercially, the C1-D chassis + SRC-5000 brain still monetize everyone else's wheeled humanoids. HKEX listing (June 2026) removes near-term funding risk. Weaknesses: many core specs undisclosed (battery, speed, repeatability, safety certs), and the robot itself is younger than rivals' with little named-customer evidence. Threat to a new EU entrant: high at the component/platform level — an EU semi-humanoid builder may face C1-D-based clones quickly, or conversely could buy the chassis layer; SEER's Germany/Japan subsidiaries mean the channel already reaches Europe.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.leaderobot.com/news/6602 | X1-PRO specs: 40 DoF, 7-DoF arms, 6 kg/arm, 16 kg dual short-term, 45° waist, 700 mm adjustment, omni chassis + buffer platform, LLM/few-sample claims (CeMAT ASIA 2025) | third-party (vendor-sourced) |
| 2 | https://seer-robotics.ai/zh/media/338 | WAIC 2026 dual-venue exhibit, IEEE 2026 award, tote/beverage demos, C1-D positioning | vendor-claimed |
| 3 | https://seer-robotics.ai/zh/blog/wheeled-humanoid-robot-chassis | C1-D: 650×650 mm, 820 mm turning, 150 kg payload, dual e-brakes, low-CG, 800 mm aisles, target industries | vendor-claimed |
| 4 | https://zhuanlan.zhihu.com/p/1942249129624469575 | X1 working demos at WRC 2025 | vendor-claimed (marketing) |
| 5 | https://www.163.com/dy/article/L2ER1KRE0556C9TT.html | WAIC 2026 recap: VLA stack, SRC-4000 on chassis, M4, 50k brains, 500k h data | third-party (vendor-sourced) |
| 6 | https://m.chinaagv.com/news/detail/202409/31400.html | SRC-5000 launch CIIF 2024, whole-body control claim, customer-site trial deliveries | third-party (vendor-sourced) |
| 7 | https://cn.seer-group.com/about-us | 2,100+ customers, 70+ countries, subsidiaries | vendor-claimed |

*Unknown fields marked n/a (not disclosed).*
