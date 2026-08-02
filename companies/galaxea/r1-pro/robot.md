# R1 Pro (星海图 R1 Pro) — Galaxea AI

> R1 Pro is Galaxea's flagship research-grade wheeled semi-humanoid: a 1.70 m, 96 kg, 26-DoF dual-arm platform on a three-wheel steering-vector omnidirectional chassis with a 4-DoF articulated torso (lift/tilt/swivel) covering a 0-2 m vertical workspace. Sold internationally at ~$69,999 with unusually complete public documentation, SDK and VR teleoperation, it is the default Chinese "embodied-AI lab platform" for demonstration collection and VLA research. Variants R1 (baseline) and R1 Lite (smaller, $/data-collection-optimized) round out the family. Competitively it matters because it captures the research segment that seeds tomorrow's commercial deployments.

| Field | Value |
|---|---|
| Company | Galaxea AI (星海图) |
| HQ | Beijing, China |
| Status (2026) | shipping (since 2024; international resellers) |
| First shown / launch | R1 2024; R1 Pro 2025 (docs current through 2026) |
| Target applications | Embodied-AI research, teleoperation data collection, mobile manipulation development, industrial prototyping |
| Price | US$69,999 (R1 Pro, US reseller); R1 Lite lower (n/a exact) |
| Availability | China direct + international resellers (US: Robotopian, backorder ~9-15 business days shipping); purchase model |

## Design & morphology
R1 Pro: 1,700 mm standing height, 675 mm width, 96 kg including battery [S1]. 26 DoF total: 8 per arm including gripper (7-DoF arm + 1-DoF gripper), 4-DoF torso, 6-DoF chassis [S1]. Torso functions: lift/tilt/swivel with waist yaw ±175°, hip pitch -105°~+90°, two knee joints (W1 -65°~105°, W2 -160°~145°); torso motor torque 108 Nm rated / 180 Nm max [S1]. Vertical operating range 0-2,000 mm — floor pick to 2 m shelf [S1].
R1 Lite: 1,281 mm, 55 kg, 23 DoF (6 chassis + 3 torso + 7 per arm w/ gripper), vertical range 0-1.7 m, torso lift + forward/back translation [S2]. R1 (baseline): 24 DoF with A1 arms (third-party; official docs no longer list it) [S4].

## Locomotion
Three self-developed steering-wheel modules (6 DoF chassis) giving true omnidirectional motion: Ackermann, translation and spin modes, 360° unlimited rotation [S1][S2]. Top speed ~1.5 m/s (third-party listing) [S4]. Indoor use; no terrain/climb specs. E-stop on base; arms have no brakes — on power loss they drop (explicit research-grade caveat in official docs) [S1].

## Upper body & manipulation
Two Galaxea A2 arms (R1 Pro; earlier units A1): 7 DoF each, 620 mm working radius (716 mm horizontal reach from torso, 861 mm with gripper), 7.8 kg per arm, rated payload 3.5 kg @0.6 m, max 5 kg @0.6 m, end-effector speed up to 7.5 m/s, acceleration 10 m/s², repeatability ±0.5 mm [S1]. Standard EE: Galaxea G1 force-controlled parallel gripper (R1 Lite gripper: 100 N rated force, 0-100 mm stroke) [S1][S2]. Note: dual-arm combined max ~10 kg (reseller framing) — the discovery-sweep claim of "10 kg per arm" is contradicted by official docs (3.5/5 kg per arm) [S1][S4]. Flange: V-mount quick-install interface on platform (R1 Lite); aviation-plug power (24 V/12 A + 5 V/3 A) available for external devices [S1][S2].

## Sensing
Head: stereo pair of two monocular RGB cameras, 120 mm baseline, 1920×1080 @30 fps, 118°H×62°V (head itself has no DoF on R1 Pro) [S1]. Wrists: 2 optional monocular depth cameras (1280×720 @30 fps, 87°H×58°V, 0.2-3 m depth) [S1]. Chassis: 5 monocular cameras (1920×1080) + 1-2 × 360° lidar (905 nm, 360°H×59°V, 0.1 m blind zone, 100BASE-TX, built-in IMU) [S1]. R1 Lite: platform binocular camera (1280×720, 126°H×116°V, 0.25-10 m) + 2 wrist depth cams [S2]. Force sensing: G1 gripper is force-controlled; IMU in lidar unit; no whole-arm F/T sensors listed.

## Actuation & power
Planetary-geared electric joint motors (high-precision, high-torque; arm joints brakeless) [S1][S2]. R1 Pro battery: 48 V Li-ion, 35 Ah / 1,680 Wh, BMS, low-noise forced-air cooling [S1]. R1 Lite: 48 V, 15 Ah / 720 Wh, optional 110-220 V AC tether for continuous bench operation [S2]. Runtime not officially stated (~4-6 h estimated from capacity/class). No hot-swap, no dock documented.

## Compute & software
R1 Pro computing unit: single SoC, 8-core 2.2 GHz CPU, 200 TOPS deep-learning compute, 32 GB LPDDR5, 1 TB SSD, 8× GMSL camera inputs, 4× GbE, M.2 WiFi with AP mode — matching NVIDIA Jetson AGX Orin 32 GB (reseller confirms AGX Orin) [S1][S4]; docs show a dual-SoC 550 TOPS variant as roadmap (commented out) [S1]. R1 Lite: Intel NUC i9-12900H [S2]. Software: Galaxea SDK + ROS-based development environment, VR/joystick teleoperation (2.4 GHz RF, 1.5 km range), full data-collection→training→deployment pipeline; Galaxea also publishes its G0 dual-system VLA work [S1][S3]. Open public documentation is a differentiator.

## Safety & compliance
Explicitly research-only: "not designed for general consumer use… does not have the necessary certifications" [S1]. E-stop button, BMS; arm brake absence is a documented hazard. No ISO/CE certifications.

## Deployment evidence & traction
Shipping since 2024 into Chinese and international research labs; US reseller listing (backorder status suggests real demand) [S4]. Galaxea reports >1,000 robots of R1 family delivered per Chinese press (third-party, unverified precise split). Used as the reference platform for Galaxea's own G0 VLA papers and various academic works (third-party). No industrial production deployments claimed for R1 Pro itself — that is the point of the product (data collection / research), with commercial operations robots to follow.

## Assessment (analyst view)
*Analyst opinion.* Strengths: best-in-class documentation and openness among Chinese vendors, sensible research-grade design (omni steering chassis, 0-2 m workspace, force-controlled grippers), aggressive price (~$70k vs $100k+ Western equivalents), strong capital. Weaknesses: modest per-arm payload (3.5/5 kg), brakeless arms and no certifications bar it from unattended commercial use; research market is small and fickle. Threat to an EU entrant: high in the research/university channel — it undercuts on price and ships today; any EU research-platform play must beat its docs/SDK experience, not just its hardware. In regulated commercial deployments its research-grade compromises leave an opening.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://docs.galaxea-ai.com/Guide/R1Pro/hardware_introduction/R1Pro_Hardware_Introduction/ (via web.archive.org snapshot 2026-04-14, site 503 at research time) | All R1 Pro official specs | vendor-claimed |
| 2 | https://docs.galaxea-ai.com/Guide/R1Lite/hardware_introduction/R1Lite_Hardware_Introduction/ (via web.archive.org snapshot 2026-02-17) | All R1 Lite official specs | vendor-claimed |
| 3 | https://galaxea.ai/ | Company/product positioning, G0 model | vendor-claimed |
| 4 | https://robotopian.com/products/galaxea-r1-pro-7dual-arm-humanoid-robot | $69,999 price, Jetson AGX Orin 32GB, 1.5 m/s, R1/R1 Lite variant positioning, 10 kg dual-arm max | third-party |
