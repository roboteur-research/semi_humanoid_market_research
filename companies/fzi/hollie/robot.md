# HoLLiE / HoLLiE C — FZI Forschungszentrum Informatik

> HoLLiE ("House of Living Labs intelligent Escort") is FZI's bimanual wheeled service robot, built since 2011 from industrial off-the-shelf components (Clearpath Ridgeback omni base, two 6-DoF Pilz PRBT arms, Schunk SVH five-finger hands, 2-DoF actuated torso) on ROS. Its competitive significance is the HoLLiECares program: real-ward hospital trials at Klinikum Karlsruhe and Knappschaftsklinikum Saar with six implemented nursing-support use cases — one of Europe's best-documented reality checks for care semi-humanoids.

| Field | Value |
|---|---|
| Company | FZI Research Center for Information Technology |
| HQ | Karlsruhe, Germany |
| Status (2026) | research (active platform; HoLLiECares project concluded 2024; HoLLiE C current generation) |
| First shown / launch | 2011 (original HoLLiE); HoLLiE C generation documented Dec 2023 [S1][S4] |
| Target applications | Hospital nursing support, care, household/service demos (cocktails, cookie decoration), research |
| Price | n/a (not for sale) |
| Availability | Not available; FZI living-lab platform, contract-research vehicle |

## Design & morphology
Anthropomorphic upper body on a Clearpath Ridgeback omnidirectional industrial base; total weight ~135 kg; actuated torso with 2 additional joints (bending/leaning) above the base; two arms + sensor head; chest LED badge, detachable 10-inch Android tablet on chest [S2, third-party/peer-reviewed]. Height not stated (n/a). Total DoF: 2 (torso) + 2x6 (arms) + hand DoF (Schunk SVH: 9 drives per hand) — no official total published.

## Locomotion
Omnidirectional (mecanum) Clearpath Ridgeback platform, max speed 1.1 m/s — chosen deliberately as a stable, no-tip commercial base appropriate for hospital environments [S2]. Indoor, flat floors; doors and elevators identified as practical obstacles in trials [S2].

## Upper body & manipulation
Two Pilz PRBT 6-DoF manipulator modules with integrated joint controllers (industrial service-robotics arms) [S2]. Interchangeable end effectors: Schunk SVH 5-finger hands, vacuum grippers, custom hooks/forearm rest for patient guidance [S2]. Two 6-axis force/torque sensors at the shoulder joints enable haptic cooperative guidance (patient escort use case) and wheelchair pushing [S2]. Payload per arm not officially stated (Pilz PRBT module rated ~3-6 kg class, estimated). Demonstrated manipulation: medicine restocking pick-and-place (ArtiMinds RPS + YOLOv5 3D localization), deformable-object handling (transfusion bags, part-aware panoptic segmentation) [S2].

## Sensing
Two frontal laser scanners on base (navigation/safety); Microsoft Azure Kinect RGB-D camera; short-range projector for floor/desk projections; microphone (ASR for wound documentation); stereo speakers; shoulder F/T sensors; multi-color LED chest badge for state signaling [S2].

## Actuation & power
Industrial electric actuators (Ridgeback drives, Pilz PRBT integrated servo joints, Schunk SVH motorized hands); battery in Ridgeback base (24 V system, capacity not restated; runtime n/a) [S2, estimated where noted].

## Compute & software
Three networked onboard PCs: platform PC (low-level control/mobility), mid-level PC (sensor/actuator comms), high-level PC (motion planning, navigation, vision) [S2]. Software: ROS (project era) / ROS 2 (current per FZI), MoveIt-style planning, MediaPipe + YOLOv5 perception, ASR/NLU pipeline for clinical documentation, ArtiMinds RPS for manipulation programming [S1][S2]. Modular "manufacturer-independent" integration philosophy [S1].

## Safety & compliance
Research platform, no ISO 13482 certification claimed (n/a). Safety via industrial base laser scanners, speed limited to 1.1 m/s, compliant/haptic control in guidance tasks; hospital deployments required case-by-case safety, security and data-protection integration — flagged as a major practical hurdle [S2].

## Deployment evidence & traction
Field tests in two German hospitals — Städtisches Klinikum Karlsruhe and Knappschaftsklinikum Saar — in two in-hospital testing phases within HoLLiECares (BMBF-funded, ~2020-2024; trials in the 2022-2024 window; COVID-19 delayed the start) [S2][S3, third-party]. Six use cases field-evaluated (wheelchair pushing, patient escort, exercise instruction, wound documentation, medicine restocking, deformable-object handling). Honest published limitations: hardware limits in wheelchair pushing, door/elevator access, no substitute for human empathy [S2]. Earlier public demos: cocktail mixing, cookie decorating [S1]. No commercial customers (n/a).

## Assessment (analyst view)
(Analyst opinion.) Strengths: pragmatic COTS architecture (cheap to maintain, reproducible), real multi-site hospital evidence, strong German care-ecosystem network (BMBF, hospitals, Devanthro via Teleskoop). Weaknesses: dated component set (Ridgeback + PRBT arms are modest performers), no product path, low payload, no certification. Threat to a new EU entrant: none commercially — instead HoLLiECares is required reading: it maps which hospital tasks are feasible today and which integration barriers (doors, elevators, IT/data protection, empathy expectations) will hit any commercial care robot. FZI is a candidate pilot partner and evaluation site.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.fzi.de/en/research/projekt-details/hollie/ | Platform overview, modularity, ROS 2, demos, since-2011 heritage | vendor-claimed |
| 2 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1325143/full | Full hardware spec (Ridgeback 135 kg, 1.1 m/s, 2x Pilz PRBT 6-DoF, SVH hands, 3 PCs), six use cases, two hospitals, findings | third-party (peer-reviewed) |
| 3 | https://www.fzi.de/en/project/holliecares-2/ | HoLLiECares project scope, BMBF funding | vendor-claimed |
| 4 | https://arxiv.org/abs/2312.06292 | HoLLiE C generation description (Dec 2023) | vendor-claimed (preprint) |
| 5 | https://www.fzi.de/en/2025/01/23/closing-of-teleskoop-research-project-robotics-for-future-care/ | Teleskoop telepresence-care project with Devanthro, closed Jan 2025 (context) | vendor-claimed |
