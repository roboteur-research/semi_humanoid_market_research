# ROBIN — Roboligent

> ROBIN is a mobile dual-arm robot from Austin's Roboligent that mounts two compliant, force-controlled Optimo-class arms on a wheeled AMR base, trained by imitation learning, for machine tending, material handling and healthcare/teleoperation tasks. Its competitive significance is the compliant direct-drive arm IP (safe contact-rich manipulation) and the Tesollo DG-5F dexterous-hand partnership — a technically credible but commercially early US semi-humanoid.

| Field | Value |
|---|---|
| Company | Roboligent Inc. |
| HQ | Austin / Round Rock, TX, USA |
| Status (2026) | announced/early production (humanoid.guide lists "in production", unverified; no named customers) [S2] |
| First shown / launch | ~2024-2025; RobotWorld 2025 demo with Tesollo DG-5F [S3] |
| Target applications | Machine tending, material handling, logistics in smart factories; physical therapy/healthcare; teleoperation |
| Price | $85,000 (aggregator-listed, unverified) [S2] |
| Availability | Direct engagement; no public ordering |

## Design & morphology
Dual-arm humanoid torso on wheeled mobile base; ~150 cm tall, ~80 kg, 14 DoF total (implies 2×6-DoF arms + torso/head or 2×7 arms; breakdown not published) [S2, third-party]. Human-safe "soft robot" styling [S1].

## Locomotion
Wheeled AMR base (type not detailed); max speed ~4.5 km/h (1.25 m/s) [S2]. Indoor factory/clinic floors.

## Upper body & manipulation
Two compliant Optimo-derived arms with force-control actuators (patented compliant manipulator technology — direct-drive/backdrivable class per company's rehab-arm lineage); combined payload ~10 kg [S1][S2]. End-effectors: standard grippers; demonstrated with Tesollo DG-5F 5-finger dexterous hand for delicate manipulation (RobotWorld 2025) [S3]. Reach/repeatability n/a (not disclosed).

## Sensing
"Responsive sensors" for human-robot interaction (force/torque sensing implied by compliant control); vision for AI navigation and object recognition; camera details n/a [S1][S2].

## Actuation & power
Compliant force-controlled actuators (company's core IP; direct-drive/quasi-direct-drive class, estimated). Runtime ~8 h per charge; battery capacity n/a; IP20 [S2].

## Compute & software
Compute n/a (not disclosed). Software: AI-based imitation learning (task teaching by human demonstration), autonomous navigation, object recognition, integrated fleet management system, teleoperation support [S1]. No public SDK/ROS statement.

## Safety & compliance
Compliant control + responsive sensors marketed for safe human collaboration [S2]; no ISO 10218/TS 15066/13482 certification claims found. Healthcare rehab use (Optimo) runs under research/clinical-trial frameworks (AFWERX STTR with UT Austin) [S4].

## Deployment evidence & traction
- AFWERX STTR Phase I + $1.8M Phase II for Optimo-based robotic rehabilitation trials (military use cases, UT Austin) — funds the arm technology, not ROBIN itself [S4, third-party].
- RobotWorld 2025 (Korea) live demo with Tesollo DG-5F [S3, vendor-claimed].
- No named ROBIN customers, unit counts or factory pilots found; humanoid.guide's "in production" status is unverified.

## Assessment (analyst view)
*Analyst opinion.* Strengths: genuine compliant-actuation IP with a defensible niche (rehab + contact-rich tending), DoD non-dilutive funding, and a serious dexterous-hand partner (Tesollo). Weaknesses: tiny team, dated web presence, no disclosed factory deployments, modest spec sheet (10 kg combined, 14 DoF) and no certification story; the dual healthcare/industrial focus risks diluting both. Threat to a new EU entrant: low — but its compliant-arm approach validates the safe-manipulation angle an EU entrant could also claim, and it could become an acquisition target for its actuation IP.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.roboligent.com/robin | Form factor, compliant arms, imitation learning, fleet mgmt | vendor-claimed |
| 2 | https://humanoid.guide/product/robin/ | 150cm/80kg/14 DoF/10kg/4.5km/h/8h/IP20/$85k | third-party (aggregator, unverified) |
| 3 | https://www.roboligent.com/post/roboligent-and-tesollo-showcase-dual-arm-humanoid-robot-with-delicate-manipulation-capabilities-at-r | Tesollo DG-5F demo, RobotWorld 2025 | vendor-claimed |
| 4 | https://www.einpresswire.com/article/699216551/roboligent-awarded-afwerx-funding-for-innovative-robotic-rehabilitation-trials + https://www.sbir.gov/awards/210640 | AFWERX STTR I/II, $1.8M, UT Austin | third-party |
