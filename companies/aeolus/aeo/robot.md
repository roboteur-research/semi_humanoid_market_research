# Aeo — Aeolus Robotics

> Aeo is a dual-arm wheeled service humanoid sold as a subscription (RaaS) for eldercare, disinfection, delivery and security patrol — one of the few semi-humanoids with multi-year paying deployments, chiefly with large Japanese eldercare operators. Its competitive significance is not raw manipulation power (arms lift only ~3.6 kg) but building-wide autonomy: Aeo opens doors and, per the vendor, is "the only robot in the world that can get on and off elevators autonomously", plus a modular head/attachment system (UV-C wand, cameras) and task-package business model.

| Field | Value |
|---|---|
| Company | Aeolus Robotics, Inc. |
| HQ | San Francisco Bay Area, USA (R&D Taiwan / Vienna / Wroclaw) |
| Status (2026) | shipping (RaaS deployments since 2019) [S1][S2] |
| First shown / launch | Lineage from CES 2018 "Aeolus Robot"; current Aeo unveiled CES 2023 (booth #9843) [S2] |
| Target applications | Eldercare monitoring, UV-C disinfection, in-building delivery, security patrol, kiosk |
| Price | n/a (not disclosed); leasing/subscription plans only [S1] |
| Availability | RaaS in Japan, Hong Kong, Taipei; distribution via Marubun Corp. (JP); vendor claims deployment "within hours" [S1][S4] |

## Design & morphology
Rounded white humanoid torso with expressive LED-face head on a low black wheeled base (see images); two arms mounted at shoulder height. Height/weight/footprint not published — from deployment photos the robot stands roughly human-waist-to-chest height (~1.1-1.3 m, estimated). Total DoF not disclosed; two 7-DoF arms plus pan/tilt head [S2].

## Locomotion
Wheeled base (drive type not disclosed; appears diff-drive with casters, estimated). Speed not published. Navigates multi-floor buildings by operating elevators itself — pressing call/floor buttons with its arm — and opening doors; vendor claims unique autonomous elevator on/off capability [S1][S2].

## Upper body & manipulation
Two third-generation Aeolus arms, 7 DoF each, single-arm lift capacity 8 lb (~3.6 kg) [S2][S3]. Design intent is asymmetric multi-tasking: one arm carries a payload or disinfection tool while the other operates elevators/doors [S2]. End effector: simple gripper; plug-and-play attachments (e.g. UV-C disinfection wand, cleaning tools) with third-party integration via Asratec (Japan) and Malibu AI (Taiwan) [S2]. No force/torque or tactile sensing disclosed.

## Sensing
Modular sensor head with cameras (first-gen platform carried a 3D depth camera + 5 MP RGB camera; current sensor loadout undisclosed) [S3]. Vision algorithms do person posture/fall detection for eldercare safety, anomaly detection for security (open windows, misplaced objects), and object recognition for fetch/delivery [S1][S2]. Base sensor suite (lidar etc.) not itemized publicly.

## Actuation & power
Actuator technology, battery capacity and runtime: n/a (not disclosed). Continuous multi-shift service operation in care facilities implies dock charging (estimated).

## Compute & software
Onboard compute not disclosed. Cloud-connected fleet/robot-management platform with CI/CD-managed updates (per Aeolus DevOps hiring) [S5]; historical stack used ROS/MoveIt (Vienna motion-planning team recruited via moveit-users list) [S5]. Task packages delivered as services: Aeo Disinfect (UV-C), Aeo Care (monitoring, reduced night-staff burden), Aeo Delivery (medicine/supplies), Aeo Security (patrol with real-time monitoring) [S1]. Voice/HRI features on first-gen platform; LLM/VLA features: none claimed.

## Safety & compliance
No ISO 13482 or other certification claims found (notable gap given eldercare use). Operates daily around frail residents in Japanese care facilities since 2019, which implies operator-accepted risk processes rather than published certification (estimated).

## Deployment evidence & traction
- Japan (since 2019), Hong Kong, Taipei [S2].
- Eldercare operators: Medical Care Service Inc., Gakken Cocofump, HIMEDIC — described as "some of the largest eldercare providers in Japan" [S1][S2]; several (Cocofump/Gakken, Saint-Care/MSC) are also investors [S4] — strong retention signal, third-party confirmed.
- Property management: Tokyu Group, Globeship Corporation [S2].
- Distribution: Marubun Corporation (Japan) [S1].
- Unit counts: n/a (not disclosed). Media: CNET, Daily Mail, Robotics 24/7 coverage of CES 2023 [S1].

## Assessment (analyst view)
*Analyst opinion.* Aeolus's strength is commercial proof, not hardware: real multi-year RaaS revenue from marquee Japanese care operators, a door/elevator capability competitors still lack in production, and a strategic-investor customer base that locks in distribution. Weaknesses: very light payload (~3.6 kg) caps task value; opaque specs, modest funding (~$30M) and low public activity since 2023 suggest limited scaling capacity; no safety-certification story despite eldercare exposure. Threat to a new EU entrant: moderate in eldercare/facility services — Aeolus defines the incumbent service level and pricing model in Japan, but its EU footprint is engineering-only (Vienna), leaving the EU care market open. An EU entrant with a certified, higher-payload platform could leapfrog it; copying its operator-investor RaaS structure would be the smarter lesson.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://aeolusbot.com/ | Service packages (Disinfect/Care/Delivery/Security), RaaS leasing, elevator-uniqueness claim, customers, Marubun, media list | vendor-claimed |
| 2 | https://www.prnewswire.com/news-releases/aeolus-debuts-autonomous-dual-arm-humanoid-robot-at-ces-301713109.html | 3rd-gen 7-DoF arms, 8 lb single-arm lift, one-arm-task/one-arm-mobility design, CES 2023 details, deployments since 2019, customer names, partners | vendor-claimed (press release) |
| 3 | https://www.althumans.com/aeolus.html | 7-DoF/8 lb confirmation, first-gen sensor loadout (3D + 5 MP cameras), deployment countries, hours-scale deployment claim | third-party |
| 4 | https://tracxn.com/d/companies/aeolusrobotics/ + Crunchbase + GigaMedia PR (https://www.prnewswire.com/news-releases/gigamedia-announces-purchase-of-convertible-note-of-aeolus-robotics-corporation-301120933.html) | $30M funding, investor-customers (Gakken Cocofump, Saint-Care, MSC), GigaMedia note | third-party |
| 5 | Aeolus hiring posts (LinkedIn Vienna/Wroclaw; moveit-users job posting) | Vienna arm motion-planning/grasping R&D, MoveIt/ROS heritage, cloud fleet management | third-party |

*Unknowns: height, weight, DoF total, speed, battery, compute, price. Vendor discloses capabilities, not specs.*
