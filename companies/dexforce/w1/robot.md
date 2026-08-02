# W1 / W1 Pro (跨维W1) — DexForce

> The DexForce W1 Pro is a 1.63 m, ~100-110 kg wheeled dual-arm humanoid (34 DoF differential / 40 DoF omnidirectional configuration) built around a pure-vision, synthetic-data-trained "Sim2Real VLA" stack. With 10 kg per-arm payload, ≥300 TOPS onboard compute, 1000 Hz whole-body control at 0.1 N force precision, sub-millimeter assembly claims and 8 h runtime, it targets parts assembly, inspection and logistics in industrial pilots (partners incl. Huawei, BYD, Foxconn per vendor). It matters as the flagship of the simulation-first route to industrial semi-humanoids — no teleop data farm required (per vendor claims).

| Field | Value |
|---|---|
| Company | DexForce (跨维智能) |
| HQ | Shenzhen, China |
| Status (2026) | shipping/pilots (announced 2025; industrial pilots; enterprise procurement) |
| First shown / launch | W1 2024/early 2025; W1 Pro (2nd gen) 2025 |
| Target applications | Precision parts assembly, factory inspection/QA, warehouse logistics, commercial service (coffee-making demos), culture & tourism |
| Price | n/a (enterprise procurement, not disclosed) |
| Availability | China; direct enterprise sales; no export channel documented |

## Design & morphology
Height 1,636 mm, footprint 682 × 550 mm, weight ~100 kg with battery (humanoid.press lists 110 kg — sources differ) [S1][S2]. Two chassis configurations: omnidirectional (40 DoF total) or differential drive (34 DoF) [S1][S2]. Dual 7-DoF anthropomorphic arms; torso/lift details not published. Full-body morphology is a classic wheeled humanoid (head + torso + two arms on wheeled base).

## Locomotion
Wheeled base, omni or diff-drive per configuration [S2]. Speed n/a (not disclosed). Indoor navigation via laser-SLAM + VSLAM hybrid localization [S2].

## Upper body & manipulation
Dual 7-DoF arms, 10 kg single-arm payload [S2][S4]. End-effectors configurable: five-finger dexterous hand or two-finger gripper [S1][S2]. Claims: sub-millimeter precision assembly, 1000 Hz real-time whole-body control, 0.1 N force-control precision, automatic hand-eye calibration [S1][S2]. Optional 6-axis wrist force sensor [S2]. Repeatability: ±1 mm positioning claimed for the vision system [S1]. Tool changer/flange media n/a.

## Sensing
Pure-vision philosophy: binocular stereo (DexSense-derived dual-camera AI, ±1 mm positioning accuracy) + wrist-mounted cameras; lidar used for SLAM navigation alongside VSLAM [S1][S2]. Tactile sensing not claimed. LLM-integrated conversational interface for voice interaction [S2].

## Actuation & power
Electric actuators (type not detailed) [S3]. Runtime: up to 8 h (480 min); power consumption reportedly cut by two-thirds vs first-gen W1 [S2][S3]. Battery capacity, hot-swap, dock: n/a (not disclosed).

## Compute & software
≥300 TOPS proprietary onboard compute platform [S2][S4]. Distributed PC/EtherCAT industrial-network control architecture, 1000 Hz [S1]. Software: closed-source DexForce stack, ROS-compatible; DexVerse™ engine generates synthetic training data; skills deployed via Sim2Real VLA models trained (per vendor) entirely on synthetic data; EmbodiChain platform open-sourced for developers; Wi-Fi, OTA updates, teleoperation supported [S1][S3]. This "no real-world data collection" claim is the core differentiator — treat as vendor-claimed until independently benchmarked.

## Safety & compliance
No certifications or safety-feature list published (n/a, not disclosed). Industrial deployment contexts imply e-stop/speed limiting but nothing documented.

## Deployment evidence & traction
- Vendor-listed partners/customers: Huawei, BYD, Foxconn, Panasonic, Toyota, plus SOE groups in aerospace, chemicals, shipbuilding [S1] (vendor-claimed; independent confirmation not found).
- Demos: autonomous coffee making, precision assembly across commercial service, manufacturing and culture-tourism scenarios [S1] (vendor-claimed).
- Press framing as "first large-scale commercial implementation in China's general embodied AI field" [S1] — promotional, unverified.
- No unit counts or named production-line deployments verified by third parties (third-party gap).

## Assessment (analyst view)
*Analyst opinion.* Strengths: differentiated simulation-first data strategy with a real industrial-vision revenue base behind it, high per-arm payload (10 kg) for the class, 8 h runtime, strong compute, and blue-chip partner names. Weaknesses: nearly all performance and customer claims are vendor-sourced; closed stack; no pricing, safety certification or export presence; the 34-vs-40 DoF and 100-vs-110 kg inconsistencies suggest fast-moving, loosely documented hardware revisions. Threat to an EU entrant: medium today (China-only sales), but the Sim2Real approach travels across borders more easily than teleop-data operations — if DexForce lands a European integrator, its cost structure could undercut EU players on skill-deployment economics.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.dexforce.com/ | W1 Pro capabilities, DexVerse, partners, 1000 Hz/0.1 N, EE options | vendor-claimed |
| 2 | https://humanoid.press/database/humanoid-press-database-dexforce-w1-pro/ | 163 cm/110 kg, 34/40 DoF, 10 kg arm, ≥300 TOPS, 8 h, sensors, SLAM | third-party |
| 3 | https://www.aparobot.com/robots/dexforce-w1-pro | 1636x682x550 mm, 100 kg, OTA/Wi-Fi/teleop, use cases (manufacturer-verified listing) | third-party |
| 4 | https://mikekalil.com/blog/china-humanoid-summer-2025/ | Independent mention: 34 joints, 10 kg lift, ~8 h battery | third-party |
