# MOVO — Kinova

> MOVO (2016-17) was Kinova's dual-arm mobile manipulator for research: a holonomic four-wheel base sized for ADA-compliant buildings, a prismatic torso lift, and up to two JACO²/Gen2 arms under a Kinect-equipped pan-tilt head, all on ROS/MoveIt. Sold to a university beta community, it was quietly discontinued (support formally ended, repo archived July 2023). It is the Canadian entry in the PR2-successor generation and shows an arm vendor's platform play failing on market size.

| Field | Value |
|---|---|
| Company | Kinova |
| HQ | Boisbriand, QC, Canada |
| Status (2026) | discontinued (support ended; GitHub repo archived 2023-07-14) |
| First shown / launch | 2016 (beta community program; built with Stanley Innovation) |
| Target applications | mobile manipulation research, assistive/HRI research |
| Price | n/a (not disclosed; est. USD ~100k-class fully configured) |
| Availability | discontinued; units remain at UWaterloo, Georgia Tech, UW-Madison and other labs |

## Design & morphology
Holonomic wheeled base, footprint 20 × 30 in (508 × 762 mm), explicitly sized to pass ADA doorways [S2][S3]. Prismatic torso lift adjusts overall height from 43 to 62 in (1.09-1.57 m) [S3]. Modular upper body: 0, 1 or 2 Kinova JACO² (Gen2) arms in 6- or 7-DoF versions plus 2-DoF pan-tilt head — total configuration ranges 8 to 27 DoF [S3][S4].

## Locomotion
Four Swedish (mecanum-type) wheels → true holonomic omnidirectional drive [S4]. Indoor flat floors; speed not published (walking-pace class, estimated).

## Upper body & manipulation
2× JACO²/Gen2 carbon-fiber arms: 6 or 7 DoF each, ~900 mm reach, ~2.2 kg mid-range payload (Gen2 spec, estimated from arm datasheet); Kinova KG-2/KG-3 2- and 3-finger underactuated grippers [S2][S3]. Arms are the same assistive-grade, low-force units Kinova sold separately — intrinsically human-safe but low-payload. No tool changer or flange media.

## Sensing
Head: Microsoft Kinect One (v2) RGB-D + microphone array on pan-tilt unit [S3][S4]. Base: front and rear 2D laser scanners for SLAM/navigation [S3]. Arm joint torque sensing (Gen2 actuators); no tactile fingertips stock.

## Actuation & power
Kinova Gen2 rotary actuators (brushless + harmonic-type reduction) in arms; electric torso lift; battery-electric base (capacity/runtime not published — n/a).

## Compute & software
Onboard PCs running ROS (Indigo/Kinetic era), full MoveIt and Gazebo integration, open API; all packages public in the archived kinova-movo repo [S2]. No fleet management, no autonomy products — a developer platform.

## Safety & compliance
No certifications; research platform. Intrinsically low-force arms, e-stop; nothing formal (n/a, not disclosed).

## Deployment evidence & traction
Sold/placed through a "beta community" of universities from ~2016: University of Waterloo RoboHub, Georgia Tech CORE Robotics Lab, UW-Madison, plus European groups (e.g. dual-arm BCI-controlled assistive-task research) [S1][S4][S5]. Estimated total fleet: dozens at most (estimated; never disclosed). No commercial deployments. Support formally ended; repo archived 14 July 2023 [S2].

## Assessment (analyst view)
*Analyst opinion.* MOVO's morphology — omni base + torso lift + two compliant arms + RGB-D head — is exactly what today's commercial semi-humanoids ship, so Kinova was directionally right and roughly eight years early. Weaknesses: assistive-grade arms (~2 kg payload), no autonomy stack, research-only economics, and a vendor whose core business (arms) did not depend on the platform succeeding. For an EU entrant, MOVO's failure argues that a hardware-only research platform has no durable market; the modern opportunity requires an AI/autonomy layer and industrial-grade payloads. Kinova itself is now a potential arm supplier, not a platform threat.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://uwaterloo.ca/robohub/profiles/movo | UWaterloo deployment, photo | third-party |
| 2 | https://github.com/Kinovarobotics/kinova-movo | architecture, ROS stack, support ended, archived | vendor-claimed |
| 3 | https://www.slideshare.net/MariePierFaucher/why-movo-insights-into-the-new-beta-community | footprint, height range, DoF range, ADA sizing, beta program | vendor-claimed |
| 4 | https://www.sciencedirect.com/science/article/abs/pii/S0967066120302392 | Swedish wheels/holonomic, prismatic torso, dual JACO² | third-party (peer-reviewed) |
| 5 | https://core-robotics.gatech.edu/robot-movo | Georgia Tech deployment | third-party |
