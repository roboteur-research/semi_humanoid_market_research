# Punyo — Toyota Research Institute

> Punyo is TRI's soft bimanual upper-body research robot: two off-the-shelf rigid arms and a chest entirely covered in air-filled tactile "bubbles", built to manipulate large, heavy, unwieldy objects with its whole body (hugging, bracing, shouldering) rather than fingertips. Not a product — a research thesis that contact-rich softness plus learned policies beats rigid precision for human-environment tasks, and a likely feature-preview for future commercial semi-humanoids.

| Field | Value |
|---|---|
| Company | Toyota Research Institute |
| HQ | Los Altos, CA, USA |
| Status (2026) | research (active platform; Punyo-1 2021 → Punyo relaunch Feb 2024) |
| First shown / launch | Punyo-1 paper Nov 2021 (RoboSoft 2022); "Meet Punyo" platform reveal Feb 2024 |
| Target applications | whole-body manipulation research: carrying large/heavy household objects, physical human interaction, eldercare-motivated tasks |
| Price | n/a (internal research; Soft-Bubble gripper design open-sourced) |
| Availability | not for sale |

## Design & morphology
Humanoid upper body (torso + two arms + sensor head) on a stationary mount; the design philosophy is "outfit off-the-shelf hard arms and components with soft tactile-sensing modules" [S2][S3]. Each arm is sheathed in 13 individually pressurizable air bladders ("bubbles") adding ~5 cm of compliance; the chest carries a compliant force/geometry-sensing surface for bracing objects against the body [S3][S4]. No mobile base in current publications (upper-body rig).

## Locomotion
None (stationary research torso). n/a.

## Upper body & manipulation
Two 7-DoF-class commercial arms (Kinova Gen3-class; TRI describes them generically as off-the-shelf) [S3][S4]. End-effectors are "paws": single high-friction latex bubbles with an internal camera watching a printed dot pattern to estimate contact forces/slip — no fingers at all [S4]. Manipulation strategy is whole-body: jamming objects between arms and chest, hugging water jugs, laundry baskets, boxes far beyond fingertip payload. Effective carried-object class: bulky items in the 5-20 kg range (estimated from demos; TRI does not publish payload figures).

## Sensing
Tactile everywhere: 26 arm bubbles with per-bubble pressure sensing and localization of contact, camera-based paw bubbles (dense force/geometry), chest force/geometry sensor; plus conventional head RGB-D for vision [S3][S4]. This sensing density is the platform's raison d'être.

## Actuation & power
Commercial electric arms (harmonic-drive class); pneumatic pressurization system for bubble stiffness control; mains-powered lab rig. n/a battery.

## Compute & software
Off-board/lab compute; learning stack draws on TRI's manipulation portfolio: teleoperated demonstration collection, Diffusion Policy imitation learning, plan-guided RL for whole-body manipulation, and integration with the Large Behavior Model program (hundreds of skills in one model); Drake simulation toolbox underpins model-based work [S1][S3][S5]. Nothing productized.

## Safety & compliance
No certifications (research). Soft compliant surfaces are themselves a safety mechanism for physical human interaction — one of the project's stated motivations [S2][S3].

## Deployment evidence & traction
None commercial — lab platform with public demos (videos: carrying jugs, hugging boxes, human-robot object handovers) and peer-reviewed output (Punyo-1, RoboSoft 2022; whole-body RL papers 2023-24) [S3][S5]. Soft-Bubble gripper hardware open-sourced and replicated by other labs (e.g. BYU's Baloo torso cites it) [S6].

## Assessment (analyst view)
*Analyst opinion.* Punyo attacks the biggest functional gap of current wheeled semi-humanoids: real-world payloads (crates, laundry, appliances) exceed what parallel grippers hold, and humans solve this with body contact. Strengths: unmatched tactile coverage, backing of TRI's top-tier learning stack, corporate patience. Weaknesses: stationary, no product path, pneumatics add maintenance complexity. Threat to an EU entrant is indirect: if whole-body soft manipulation matures, Toyota can inject it into partner platforms (e.g. Boston Dynamics) quickly; EU entrants should track the open publications and consider compliant torso surfaces early — it is cheap differentiation validated by a $1B lab.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.tri.global/ | TRI research context, LBM program | vendor-claimed |
| 2 | https://punyo.tech/ | platform positioning, bubble gripper, images | vendor-claimed |
| 3 | https://medium.com/toyotaresearch/meet-punyo-tris-soft-robot-for-whole-body-manipulation-research-949c934ac3d8 | Feb 2024 reveal, design philosophy, demos | vendor-claimed |
| 4 | https://www.therobotreport.com/punyo-soft-robot-from-tri-designed-for-whole-body-manipulation/ | 13 bubbles/arm, 5cm compliance, paw cameras, chest sensor | third-party |
| 5 | https://arxiv.org/abs/2111.09354 | Punyo-1 paper (hardware, large-object manipulation, pHRI) | vendor-claimed (peer-reviewed) |
| 6 | https://arxiv.org/pdf/2409.08420 | third-party replication/citation (BYU Baloo) | third-party |
