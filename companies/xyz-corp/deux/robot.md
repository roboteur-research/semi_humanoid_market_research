# DEUX (듀스, "Deuce") — XYZ Inc.

> DEUX is a height-adjustable (90-155 cm) dual-arm semi-humanoid on a 360° swerve-drive base, aimed at retail store operations — restocking, shelf arrangement, tidying and packing. Unveiled 27 July 2026 with a live packing demo at the LoungeX store in Seoul, it pairs 1:1 with the Glove X data-collection glove and Brain X behavior models. At $39,900 (mobile) with 7-DoF three-finger hands, it is one of the cheapest mobile dual-arm platforms announced anywhere — a direct signal of where Korean retail-robot pricing is heading.

| Field | Value |
|---|---|
| Company | XYZ Inc. (엑스와이지) |
| HQ | Seoul (Seongsu), South Korea |
| Status (2026) | announced (pre-order; live store demos) |
| First shown / launch | 27 July 2026, LoungeX Seongsu store demo [S1] |
| Target applications | retail restocking/arrangement, inventory checks, store tidying, packing; later offices/hospitals/homes |
| Price | Mobile DEUX $39,900; fixed DEUX $29,900; Glove X $3,900/unit; pre-order incl. Brain X + one task-modeling cycle; NVIDIA Thor compute sold separately [S2] |
| Availability | Pre-order (Korea first); ships n/a (not disclosed) |

## Design & morphology
Footprint W 530 × D 652 mm; height 900 mm (min) to 1,550 mm (max) via 1-DoF lift column. Weight 60 kg total (base 35 kg + robot 25 kg). Official joint budget: 30 DoF = 2×7-DoF arms + 2×7-DoF dexterous hands + 1-DoF lift + 3-DoF swerve mobile base (marketing materials and press also cite "32 DoF"). [S1][S2]

## Locomotion
Four swerve-drive modules (per press; spec table lists the base as a 3-DoF unit) giving true 360° omnidirectional movement. Max speed n/a (not disclosed). Indoor floors only. [S1][S2]

## Upper body & manipulation
Two 7-DoF arms; range of motion (reach) 501 mm; max payload 5.5 kg single-arm / 11 kg dual-arm. Proprietary 3-finger dexterous hands with 7 DoF each; impedance-control-based compliance for safe operation around people (press). 1,000 Hz CAN-FD control bus. The 1:1 kinematic mapping between Glove X and the hand means demonstration data needs no retargeting correction. [S1][S2]

## Sensing
Robot sensor suite not fully disclosed. The paired Glove X capture device records three streams: (1) high-res dual camera with 220° ultra-wide lens (MIPI CSI-2), (2) 7-joint magnetic-encoder tracking at 1,000 Hz (0.5° tolerance) fused with Meta Quest dual-hand 3D tracking, (3) 3-channel independent fingertip pressure sensors at 83.3 Hz. Robot hand tactile: pressure data transfers "directly into DEUX's 3-finger hand" (vendor). [S2]

## Actuation & power
Battery 24 V / 60 Ah = 1,440 Wh; runtime n/a (not disclosed). Actuator type n/a (not disclosed); 1 kHz CAN-FD control loop implies integrated smart servos. Standalone system — operates without external PC or cables. [S2]

## Compute & software
ROS 2 support, Python, "DEUX Controller" software provided. On-device 1 kHz data processing; NVIDIA Thor compute module optional/sold separately (implies base config uses lighter compute). AI stack: Brain X behavior models + agentic AI, continuously trained on store data collected via Glove X and deployed robots; one task-modeling cycle bundled with pre-orders. [S2]

## Safety & compliance
Impedance-control compliance highlighted for human-shared spaces (press). No ISO 13482/CE claims published. [S1]

## Deployment evidence & traction
- 27 July 2026: public real-environment demo at LoungeX Seongsu (XYZ's robot-café brand) — arranging products, tidying, boxing coffee and donuts; framed as "behavioral verification and physical AI system testing". [S1]
- Leverages XYZ's existing paid fleet history (BARISBREW/STORAGY, 720k+ cumulative orders) rather than a customer install base for DEUX itself — no external DEUX customers announced yet. [S3]

## Assessment (analyst view)
*Analyst opinion.* Strengths: aggressive pricing (~$40k with two 7-DoF hands), coherent data strategy (Glove X 1:1 capture, no retargeting; own stores as testbeds), compact 60 kg platform with 90-155 cm height range suited to low shelves and counters. Weaknesses: 501 mm reach is short; specs silent on battery life, robot-side cameras, and safety certification; company is small and Korea-centric; "announced" maturity. Threat to an EU entrant: medium — limited near-term EU presence, but its price point and retail focus will shape customer expectations for convenience/grocery use cases; an EU entrant targeting retail should benchmark DEUX's $/DoF and data pipeline.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://en.sedaily.com/technology/2026/07/27/xyz-unveils-dual-arm-semi-humanoid-robot-deuce-for-store | unveiling, LoungeX demo, 32 DoF, 3-finger hands, swerve x4, impedance control, CEO quote | third-party |
| 2 | https://xyzcorp.imweb.me/DEUX | full spec table (dimensions, 30 DoF, 1,440 Wh, 501 mm, 5.5/11 kg, CAN-FD, ROS 2, pricing), Glove X details | vendor-claimed |
| 3 | Korean press via DDG (엑스와이지 시리즈B 13 0억) | Series B, company history/revenue | third-party |
