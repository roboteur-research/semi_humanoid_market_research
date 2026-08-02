# R2D3 — Open Droids

> Dual-arm wheeled mobile manipulator ("composite lifting robot") aimed at household chores, food service and housekeeping, unveiled at CES 2025 at a ~$55-60k price with a fully open-source ROS 2 stack. Competitively it matters as one of the cheapest Western-branded dual-arm platforms — though it is largely integrated from Chinese RealMan arms and a Woosh AGV base.

| Field | Value |
|---|---|
| Company | Open Droids |
| HQ | Wichita, KS / San Francisco, CA, USA |
| Status (2026) | shipping (waitlist/short-run; ~1 month lead time claimed) [S2][S5] |
| First shown / launch | CES 2025 (Jan 2025); announced as R1D1 successor late 2024 |
| Target applications | Laundry folding, dishwashing, food service, housekeeping, rehab-center assistance, light industrial |
| Price | $55,000 (Robotic Gizmos, 1-month lead) to ~$60,000 (company estimate at CES) [S2][S3] |
| Availability | Waitlist via opendroids.com; direct purchase, US-focused |

## Design & morphology
Dual-arm torso on a wheeled AMR base with a vertical lift mechanism. Per the company's own ROS 2 repo, the build is: two RealMan RM75-B 7-DoF arms (RM65-B 6-DoF as alternative config), WHJ30-80 expansion joint modules providing head rotation and torso lift, on a Woosh AGV chassis [S4]. Height/weight/footprint not disclosed. Total DoF ≈ 16-17 core (2×7 arms + lift + head) plus end-effectors (estimated).

## Locomotion
Woosh AMR base (differential drive, estimated); speed not disclosed for R2D3 (sibling R1D1: 0.67 m/s [S1]). Indoor flat-floor use; self-charging via dock (vendor-claimed, carried over from R1D1).

## Upper body & manipulation
Two 7-DoF RealMan RM75-B arms (5 kg rated payload each per RealMan's standard spec — estimated, not stated by Open Droids). End-effectors: EG2-4C2 2-finger gripper claws standard; optional RealMan RM56DFX-2R/-2L dexterous hands [S4]. Company also sells its own DH116 dexterous hand (30 kg hook load, 508-dot tactile sensing, EtherCAT) which is positioned for humanoid/prosthetic use [S2]. Reach/repeatability n/a (not disclosed).

## Sensing
3× Intel RealSense D435 depth cameras + 2 RGB cameras [S3][S5]; Fun M240 microphone array for voice input [S4]. Base sensor suite (lidar etc.) not itemized; sibling R1D3 advertises lidar navigation [S2].

## Actuation & power
Arm actuation = RealMan integrated joint modules (harmonic/planetary class, estimated). Battery capacity and runtime n/a (not disclosed); automated dock self-charging claimed [S2].

## Compute & software
NVIDIA Jetson AGX Orin onboard [S3][S5]. Open-source ROS 2 stack (Foxy/Humble/Jazzy) under Apache 2.0: MoveIt 2 motion planning, camera and AGV control interfaces, released on GitHub (v1.2.0, Jan 2025) [S4]. Teleoperation/data-collection supported via the company's motion-capture glove product. AI capabilities described only loosely ("real-time AI"); no VLA foundation model disclosed. Marketing cites Google DeepMind and NVIDIA partnerships (unverified depth) [S2].

## Safety & compliance
n/a (not disclosed). Repo includes safety guidelines only; no ISO/UL/CE certifications claimed.

## Deployment evidence & traction
- Pilot programs in rehabilitation centers assisting with repetitive tasks (vendor-claimed at CES) [S3].
- Pre-order discussions with Baskin-Robbins and Subway franchises, plus university research labs (for R1D1, Aug 2024) [S1, vendor-claimed].
- CES 2025 Unveiled demo (laundry folding, dish washing, can opening) received wide press coverage [S3][S5].
- No named paying customers or unit counts disclosed.

## Assessment (analyst view)
*Analyst opinion.* Strengths: aggressive pricing (~$55-60k dual-arm, $18.5k single-arm), genuine open-source ROS 2 release (rare in this class), and strong media presence. Weaknesses: it is essentially a systems integration of RealMan arms + Woosh base + RealSense — hardware anyone can replicate; no disclosed specs (payload, runtime, safety), no verified deployments, and a crypto-flavored investor base that signals hype risk. Threat to a new EU entrant: low-to-moderate — it pressures price expectations and open-source positioning in the research/dev segment, but poses little threat in certified industrial or eldercare deployments in Europe.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.therobotreport.com/open-droids-develops-both-single-dual-arm-mobile-manipulators/ | R1D1 specs, company background, target customers | third-party |
| 2 | https://www.opendroids.com/ (+ /droids/r2d3, /dh116-robot-hand) | Product positioning, DH116 specs, investors, partnerships | vendor-claimed |
| 3 | https://tech.yahoo.com/general/articles/ces-unveiled-2025-opendroids-r2d3-042543404.html | CES 2025 demo, ~$60k price, rehab pilots | third-party |
| 4 | https://github.com/Open-Droids-robot/R2D3_ros2 | RM75-B arms, Woosh base, sensors, grippers, ROS 2/Apache 2.0 stack | third-party (primary code) |
| 5 | https://www.roboticgizmos.com/opendroids-r2d3/ | $55k price, 1-month lead, Jetson AGX Orin, camera count | third-party |
