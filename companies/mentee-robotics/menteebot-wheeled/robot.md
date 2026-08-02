# MenteeBot V3.0 ("wheeled variant" — unverified) — Mentee Robotics / Mentee by Mobileye

> **Verification result: no wheeled MenteeBot could be confirmed.** The discovery note "modular lower body: biped OR wheels" is not supported by Mentee's site, press coverage of V3.0, or third-party spec databases — all describe MenteeBot exclusively as a **bipedal** humanoid; the modular biped/wheeled claim almost certainly belongs to UK startup Humanoid's HMND-01 (covered under companies/humanoid-uk/), which appeared alongside MenteeBot in the same round-up articles. This dossier therefore records the actual product — the bipedal MenteeBot V3.0 (Feb 2025) — because its $900M Mobileye acquisition makes it a first-order strategic competitor to wheeled semi-humanoids in warehouse logistics.

| Field | Value |
|---|---|
| Company | Mentee Robotics (Mentee by Mobileye since Feb 2026) |
| HQ | Herzliya, Israel |
| Status (2026) | prototype — customer proof-of-concept deployments during 2026; series production targeted 2028 |
| First shown / launch | V1 April 2024; V2 mid-2024; **V3.0 announced 2025-02-17** |
| Target applications | Warehouse/logistics (box handling, sorting, transport); long-term household |
| Price | n/a (not disclosed) |
| Availability | Not yet purchasable; POC engagements 2026, commercialization 2028 (Mobileye guidance) |

## Design & morphology
Bipedal full humanoid: **175 cm, ~70 kg (with battery), ~40 DoF** [S2][S3]. Enhanced torso mobility vs V2 [S4]. No wheeled/modular lower-body option found (checked official site, Robot Report, Interesting Engineering, aparobot, humanoid.guide) — wheeled-variant claim marked **unverified/likely erroneous**.

## Locomotion
Bipedal walking up to **1.5 m/s**; running shown in earlier versions; dynamic balance while carrying load [S2][S3].

## Upper body & manipulation
- **Lift capacity up to 25 kg** (55 lb) [S2] (vendor-claimed).
- Redesigned hands in V3.0: firmer hold, impact resistance, **~30 N pinch force per finger** [S3][S4] (vendor-claimed).
- Arm DoF breakdown n/a; total ~40 DoF including hands [S3].

## Sensing
Camera-centric, lidar-free philosophy (Mobileye heritage): head sensors plus **back camera and fisheye side cameras for 360° vision**; depth estimation from vision; tactile sensors in hands [S2][S3]. Production version planned camera-only [S3].

## Actuation & power
Custom-built actuators claimed **~3× more power/power density** than predecessor/competitors, enhanced precision [S2] (vendor-claimed). **Hot-swappable battery, 3+ h (up to ~300 min) continuous operation** [S2][S3]. Battery kWh n/a.

## Compute & software
**Dual NVIDIA Jetson AGX Orin** onboard [S2]. AI stack: Sim2Real RL locomotion, NeRF-based 3-D semantic mapping, LLM-based task decomposition ("mentoring" — learning from verbal instruction and demonstration), proprietary foundation-model training methodology [S2][S3]. No public SDK.

## Safety & compliance
n/a (not disclosed).

## Deployment evidence & traction
- Uncut 18-minute video (2025) of **two V3 MenteeBots autonomously sorting/moving 32 boxes** in a shared warehouse space without collision [S6] (vendor video, third-party covered).
- **Mobileye acquisition $900M** (announced CES 2026, closed 2026-02-03) with stated first on-site customer POCs in 2026 and series production 2028 [S1][S5]. No paying customers/unit counts disclosed yet.

## Assessment (analyst view)
*Analyst opinion.* Strengths: elite AI founding team, camera-only cost-down philosophy, now Mobileye's automotive-grade productization muscle and balance sheet — the most credible Israeli humanoid play by far. Weaknesses: bipedal complexity pushes commercialization to 2028, no field deployments yet, and lift/runtime claims are vendor-only. For a new EU wheeled semi-humanoid entrant the threat is medium-term but serious: Mentee targets identical warehouse workflows, and Mobileye's scale manufacturing could erode the cost advantage that justifies wheeled bases. Near term (2026-27) it competes for pilots and talent, not orders.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://www.mobileye.com/news/mobileye-to-acquire-mentee-robotics-to-accelerate-physical-ai-leadership/ | $900M deal, POC 2026, production 2028 | vendor-claimed |
| S2 | https://interestingengineering.com/innovation/israel-humanoid-robot-with-360-vision | V3.0 specs: 175 cm, 25 kg, 1.5 m/s, 3h hot-swap battery, 2× AGX Orin, 360° cameras, 3× actuators | third-party |
| S3 | https://www.aparobot.com/robots/menteebot | 70 kg, 40 DoF, 30N pinch, tactile, camera-only plan, no wheeled variant listed | third-party |
| S4 | https://mikekalil.com/blog/hmnd01-menteev3-engineais2/ | V3 torso mobility, pinch force; source of probable HMND-01 wheeled/biped confusion | third-party |
| S5 | https://www.robotics247.com/article/ces-2026-mobileye-set-to-acquire-humanoid-robot-startup-mentee-robotics-for-900m | Acquisition completion 2026-02-03 | third-party |
| S6 | https://interestingengineering.com/ai-robotics/humanoid-robot-pair-32-boxes | Two-robot warehouse box-sorting demo | third-party |
