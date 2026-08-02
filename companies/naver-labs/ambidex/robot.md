# AMBIDEX (앰비덱스) — NAVER LABS

> Research-stage dual-arm upper-body robot whose signature is **cable-driven (tendon) actuation**: each 7-DoF arm weighs ~2.6 kg — lighter than a human arm — yet handles ~3 kg and moves at up to 5 m/s while remaining intrinsically safe around people. Developed with KOREATECH since 2017, taught tasks via bilateral haptic teleoperation, and demonstrated on 5G "brainless-robot" cloud control (CES 2019). Matters competitively as the benchmark for lightweight safe manipulation and imitation teaching, not as a product — it has one in-house job (cleaning delivery robots in NAVER's 1784 HQ) and no commercial offering.

| Field | Value |
|---|---|
| Company | NAVER LABS |
| HQ | Seongnam (Bundang), South Korea |
| Status (2026) | research |
| First shown / launch | 2017 (R&D reveal with KOREATECH); CES 2019 5G demo; hardware/software upgrade 2021 |
| Target applications | Research: everyday manipulation (dish washing, peeling, furniture assembly), HRI; in-house robot-fleet cleaning at 1784 |
| Price | n/a (not for sale) |
| Availability | Not available; internal research platform |

## Design & morphology
Upper-body torso with two arms + sensor head, mounted on a **fixed pedestal/stand** (research configurations on lab frames/tripods; no self-mobility). Human 1:1 scale arms [S2]; standing setup ~1860 mm tall per third-party listing [S4] (third-party). Total DoF n/a (7 per arm + head; hand DoF varies by end-effector build — later builds show multi-finger hands).

## Locomotion
None — pedestal robot. (In 1784 deployment it works at a fixed station cleaning Rookie robots [S5].)

## Upper body & manipulation
- **7 DoF per arm**, kinematics mimicking the human arm [S1][S2].
- **Arm mass ~2.6 kg** — less than an average human arm — because motors sit in the torso/shoulder and pull tendons (cables), minimizing moving inertia [S2][S4] (third-party; discovery note of 2.3 kg not corroborated — 2.6 kg is the consistently reported figure).
- **Payload ~3 kg per arm**; **tip speed up to 5 m/s** claimed safe around humans [S2][S4] (vendor-claimed/third-party).
- End-effectors: interchangeable research hands — from simple grippers to articulated multi-finger hands (seen in 2020-21 demos); no standardized product hand.
- Demonstrated tasks: pouring, dish washing, vegetable peeling/dicing, furniture assembly, table tennis, catching balls; learned via **bilateral haptic teleoperation** (operator feels contact forces) and then replayed/generalized with reinforcement/imitation learning [S1][S3].

## Sensing
Head-mounted stereo/vision camera module; cable-tension-based force/position sensing in arms enables whole-arm compliance and force estimation; haptic-device interface streams force both ways [S1][S3]. Detailed sensor BOM n/a.

## Actuation & power
Proprietary **cable-driven mechanism** co-developed with KOREATECH — motors + reducers relocated proximally, cables act as tendons; provides mechanical compliance, back-drivability and low reflected inertia (the safety argument) [S1][S2]. Tethered lab power; battery n/a.

## Compute & software
Two operating modes shown: onboard control, and **"brainless" cloud control over 5G** — world-first 5G robot-control demo with Qualcomm/KT at CES 2019, with control loops closed via NAVER's ARC cloud [S1][S5]. Learning stack: haptic demonstration capture, interconnected reinforcement-learning simulator (2018), task-learning environment (2020) [S1]. No public SDK.

## Safety & compliance
No certifications (research). Safety case is mechanical: sub-human-arm inertia + compliance + force sensing for safe physical HRI [S1][S2].

## Deployment evidence & traction
- **1784 building (NAVER HQ)**: AMBIDEX employed cleaning/disinfecting the ~100-strong Rookie delivery-robot fleet — its only "real job" (third-party, Korea Times) [S5].
- IROS 2018 Fan Robotic Challenge winner; CES 2019 5G demo; no sales, no external installs [S1].

## Assessment (analyst view)
*Analyst opinion.* AMBIDEX is the strongest public proof that tendon-driven lightweight arms can combine speed, payload and intrinsic safety — a direct design benchmark for any EU entrant betting on heavier conventional arms plus software safety. Weaknesses: a decade-in research platform with no productization, no SDK, and NAVER's strategy pointing to cloud/ecosystem plays rather than hardware sales. Threat to an EU entrant: low as a competitor, moderate as an ecosystem gatekeeper — if building-scale ARC-like infrastructure becomes the deployment norm in Korea, hardware vendors may need to integrate with NAVER's stack rather than compete with it.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://www.naverlabs.com/en/ambidex | Cable mechanism, KOREATECH, timeline (2017-21), haptic task learning, IROS 2018, 5G demo | vendor-claimed |
| S2 | https://www.roboticgizmos.com/ambidex-7dof/ | 7 DoF/arm, 2.6 kg arm, 5 m/s, human 1:1 scale, safety claims | third-party |
| S3 | https://www.inceptivemind.com/ambidex-cable-driven-robot-learns-wash-dishes-peel-vegetables/16439/ | Dish-washing/peeling learning demos, bilateral haptic teleop | third-party |
| S4 | https://www.aparobot.com/robots/ambidex | 3 kg/arm payload, 1860 mm standing height, sensor summary | third-party |
| S5 | https://www.koreatimes.co.kr/business/companies/20230707/navers-1784-building-showcases-human-robot-interaction | 1784 role (cleaning Rookies), ARC/5G context | third-party |
