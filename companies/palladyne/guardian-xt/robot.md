# Guardian XT — Palladyne AI (Sarcos) — DISCONTINUED

> The Guardian XT was Sarcos's teleoperated dual-arm "robotic avatar": the upper half of the Guardian XO exoskeleton, platform-agnostic so it could be mounted on tracked bases, boom/scissor lifts or vehicles, lifting up to 200 lb (90 kg) combined while an operator in VR goggles and an IMU motion-capture SenSuit mirrored its arms in real time. Beta was completed in 2021, it headlined CES 2021/2022 and won Navy/USAF interest — then the whole hardware line was shelved in the November 2023 exit that turned Sarcos into software-only Palladyne AI. It remains the reference case for pre-AI-era teleop torso robots that failed commercially.

| Field | Value |
|---|---|
| Company | Sarcos Technology and Robotics → Palladyne AI |
| HQ | Salt Lake City, UT, USA |
| Status (2026) | discontinued (hardware development/production exited Nov 2023) [S1] |
| First shown / launch | Concept 2020; next-gen teleop demo July 2021; beta complete late 2021; CES 2022 demo [S2][S3] |
| Target applications | Hazardous/at-height industrial work: power-tool operation, welding/cutting, inspection; aviation MRO, energy, construction, defense logistics |
| Price | Planned RaaS subscription (never commercially released; XO exoskeleton was quoted ~$100k/yr — XT expected similar model) |
| Availability | Never generally available; pilots only |

## Design & morphology
Dual-arm humanoid torso (derived from Guardian XO upper body); dimensions <72 × <40 × <24 in (<183 × 102 × 61 cm) [S2]. Platform-agnostic mounting: tracked mobile bases, boom lifts, scissor lifts, vehicles — the mobile variant marketed as Guardian XM [S2][S3].

## Locomotion
None integral — carried by host platform (track/lift/vehicle).

## Upper body & manipulation
Two 7-DoF-class force-reflective arms; combined lift/manipulation capacity up to 200 lb (90 kg) [S2][S3]. End-effectors: 3-DoF effectors able to hold and operate hand-held power tools, welding and cutting equipment, and test/inspection gear [S2]. Human-like dexterity via 1:1 motion mapping.

## Sensing
Stereo camera head streaming to operator VR goggles ("see exactly what the robot sees"); force feedback to operator [S2][S3].

## Actuation & power
Sarcos proprietary high-power-density electric (XT was the electrified evolution of hydraulic Sarcos arms); tethered or platform-powered; details n/a.

## Compute & software
Teleoperation-first: IMU-based SenSuit motion-capture controller mirroring operator movements in real time; no meaningful autonomy layer at the time — the company's later Palladyne IQ software is, in effect, the autonomy it lacked [S2][S1].

## Safety & compliance
Operator removed from hazard (the safety proposition); no robot-safety certifications published.

## Deployment evidence & traction
- Beta development completed (announced late 2021); CES 2021/2022 live demos [S2][S3].
- US Navy / USAF development contracts via Sarcos Defense and RE2 (related HDMS dual-arm systems) [S1].
- No commercial deployments before the Nov 2023 hardware exit; program shelved with the pivot [S1].

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://en.wikipedia.org/wiki/Palladyne_AI | Hardware exit Nov 2023, corporate history | third-party |
| 2 | https://www.robotics247.com/article/sarcos_completes_beta_development_of_guardian_xt_teleoperated_robotic_avatar | Beta completion, 200lb/90kg, dimensions, 3-DoF effectors, SenSuit | third-party |
| 3 | https://www.businesswire.com/news/home/20210707005077/en/ | Teleop implementation, VR goggles, platform-agnostic mounting | vendor-claimed |
