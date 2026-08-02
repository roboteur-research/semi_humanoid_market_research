# JAKA K1W (节卡 K1W) — JAKA Robotics

> K1W is JAKA's wheeled semi-humanoid: dual force-controlled arms from its cobot lineage on an omnidirectional base with a lifting/pitching waist, aimed at precision industrial mobile manipulation (sorting, machine tending, inspection). Competitively it matters because it brings certified-cobot-grade repeatability (±0.05mm claimed) and an existing Fortune-500 factory channel into the wheeled-humanoid category — an industrial-credibility play rather than an AI-demo play.

| Field | Value |
|---|---|
| Company | JAKA Robotics (节卡机器人) |
| HQ | Shanghai, China |
| Status (2026) | shipping (small batches / factory pilots) [S1][S2] |
| First shown / launch | Embodied family launched from 2024; K1W publicized 2025 (WRC 2025, CIIF 2025) [S2][S3] |
| Target applications | Intelligent sorting, handling/transfer, machine loading & unloading, inspection in industrial scenarios [S1] |
| Price | n/a (not disclosed) |
| Availability | China, direct/integrator sales; described by JAKA as "out-of-the-box" deployable [S1] |

## Design & morphology
Wheeled torso-on-base semi-humanoid: omnidirectional mobile chassis, torso with lifting AND pitching waist, dual arms, sensor head. 21 DoF total (vendor-claimed; hands/end-effectors not included in count) — JAKA markets the omni base + lifting/pitching waist as giving "full-domain coverage" of the workspace [S1]. Height/weight not disclosed. The platform is an integrated base-arm-perception system rather than an AMR + arms assembly [S1].

## Locomotion
Omnidirectional wheeled base (type of omni drive not specified). Speed, gradeability, brakes: n/a (not disclosed). 360° lidar environmental monitoring plus collision detection for operation among people [S1].

## Upper body & manipulation
Dual arms with embedded six-axis (6D) force/torque sensing for force-controlled contact tasks [S1]. Repeatability ±0.05mm (vendor-claimed) — cobot-class, and tighter than the ±0.1mm of JAKA's own K1 biped [S1][S4]. Per-arm DoF not stated for K1W (K1 uses 7-axis arms; 7 per arm is a reasonable estimate). Payload per arm not disclosed (K1: 3-5 kg/arm, likely similar — estimated). End-effector: application-specific grippers; JAKA's cobot tool ecosystem applies. 1 ms communication cycle for high-speed servo response (vendor-claimed, consistent with JAKA's EtherCAT cobot controllers) [S1][S4].

## Sensing
3 AI vision sensors ("3颗AI视觉") distributed on head/torso for scene understanding and dynamic visual grasping [S1]; 6-axis F/T sensing embedded in both arms; base: 360° lidar + collision detection [S1]. Tactile: n/a (not disclosed).

## Actuation & power
JAKA integrated modular joints (harmonic-drive cobot joints per JAKA's core technology stack; vendor lineage, estimated). Battery capacity/runtime/hot-swap: n/a (not disclosed).

## Compute & software
Onboard compute not disclosed. Software: JAKA embodied stack with 3D synthetic-data training + reinforcement learning; marketed as out-of-box usable [S1]. From CIIF 2025, JAKA promotes the JAKA EVO "AI + industrial robot OS" across the product family [S5]. Vision partnerships (Albert pure-vision, Orbbec) exist at family level [S2]. SDK/ROS support: n/a (not disclosed).

## Safety & compliance
360° lidar monitoring + collision detection; force-limited arms from certified cobot lineage (JAKA cobots hold CE/ISO cobot certifications; K1W-specific certification not stated) [S1]. Confidence: estimated for K1W itself.

## Deployment evidence & traction
- Deployed and performing "flexible operations" in the factory of an unnamed Fortune-500 enterprise, in sorting/handling/loading/inspection scenarios (vendor-claimed, repeated in third-party press) [S1][S3].
- Family-level: 300+ embodied-intelligence units delivered in 2024 (K1/K1L/K1W/Lumi combined; not K1W-specific) [S2].
- Shown working at WRC 2025 (Beijing) and CIIF 2025 (Shanghai) [S2][S3].

## Assessment (analyst view)
*Analyst opinion.* Strengths: genuine industrial precision claims (±0.05mm, 6D force control, 1 ms control loop) backed by a 10,000-unit cobot install base, existing factory customers and integrator channel — the most credible "it actually works in a plant" story among China's Tier-2 wheeled humanoids. Weaknesses: thin public spec sheet (no payload, battery, compute numbers), no disclosed pricing, and corporate financing uncertainty after the withdrawn STAR IPO. For a new EU entrant the threat is moderate-to-high in precision manufacturing niches (3C, semiconductor-adjacent, automotive tending) where JAKA can bundle K1W with its cobot fleet and European subsidiary (Germany) presence; it is less of a threat in service/logistics scenarios where its precision advantage matters little.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://zhuanlan.zhihu.com/p/1977457053535581066 (JAKA embodied family article, mirrored in JAKA marketing) | K1W: 21 DoF, ±0.05mm, 3 AI vision, dual-arm 6D force, 1ms, omni base + lifting/pitching waist, 360° lidar, 3D synthetic + RL training, Fortune-500 factory deployment | vendor-claimed |
| 2 | https://sh.chinadaily.com.cn/a/202508/06/WS68932e4fa310ebef36290bc4.html | Family lineup, 300+ units delivered 2024, WRC 2025 presence, Albert/Orbbec partnerships | third-party |
| 3 | https://m.tech.china.com/hea/articles/20250924/202509241738556.html | CIIF 2025 showing, industrial positioning | third-party |
| 4 | https://news.qq.com/rain/a/20240929A07NWJ00 | K1 sibling specs for lineage comparison (29 joints, ±0.1mm, 3-5kg/arm, EtherCAT) | third-party (vendor-sourced) |
| 5 | https://www.leaderobot.com/news/6413 | JAKA EVO OS launch | third-party (vendor-sourced) |

*Specs carry confidence tags inline; unknown fields marked n/a (not disclosed).*
