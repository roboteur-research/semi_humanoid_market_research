# R1-D (宇树 R1-D 双臂机器人) — Unitree Robotics

> R1-D is Unitree's first non-biped robot: a dual-arm humanoid upper body (head, 1-DoF waist, two 5- or 7-DoF arms) sold either on a fixed bench base or on a wheeled mobile base with a telescoping column (0.68→1.6 m). Launched May 2026 from RMB 26,900 / US$4,290, it applies Unitree's vertical integration and 60% gross margins to the wheeled semi-humanoid category, instantly resetting the entry price for manipulation research, education and light service tasks by an order of magnitude. Payloads are light (2-4 kg/arm) and runtime short (~1.5 h) — this is a data-collection/development machine, not an industrial workhorse — but it puts a credible dual-arm platform within reach of every lab and school.

| Field | Value |
|---|---|
| Company | Unitree Robotics (宇树科技) |
| HQ | Hangzhou, China |
| Status (2026) | shipping (webshop/global distributors) |
| First shown / launch | May 2026 [S2] |
| Target applications | Research & data collection, education, industrial/service manipulation development, interaction demos |
| Price | From RMB 26,900 / US$4,290 (R1-A5 fixed base); higher SKUs n/a exact [S1][S2] |
| Availability | Global (Unitree webshop + distributor network); purchase; charger included |

## Design & morphology
Four SKUs combining arm DoF and base [S1]:
- R1-A5: 5-DoF arms, fixed base — 15 DoF total, 700×357×190 mm, ~11 kg
- R1-A7: 7-DoF arms, fixed base — 19 DoF, 835×357×190 mm, ~13 kg
- R1-A5-D: 5-DoF arms + wheeled base — 18 DoF, ~30 kg
- R1-A7-D: 7-DoF arms + wheeled base — 22 DoF, ~32 kg
Mobile versions: 683×520×440 mm collapsed → 1,600×520×440 mm extended (telescoping column lift). Waist: 1 DoF yaw (±150° fixed / ±35° mobile); head: 2 DoF (±115° yaw, ±36° pitch); chassis: 3 DoF [S1]. Arm lengths 420 mm (A5) / 555 mm (A7).

## Locomotion
Wheeled base on -D SKUs (3-DoF chassis; drive layout not detailed — omni-capable per marketing footage; vendor-claimed). Speed/terrain specs n/a. Fixed-base SKUs are stationary bench units.

## Upper body & manipulation
Arms: 5 or 7 DoF each, 2-4 kg max payload per arm, shoulder joint torque up to 60 Nm [S1]. Standard gripper with ±0.1 mm accuracy claim; optional Unitree Dex5 dexterous hand ecosystem compatibility (vendor materials; confirm per SKU). Wrist camera optional [S1]. Flange media n/a.

## Sensing
Head binocular camera: 1280×720 @30 Hz RGB, 146° horizontal FOV; optional wrist camera; 4-microphone array, dual 3 W speakers [S1]. No lidar listed for the base (navigation is not the focus); IMU implied. Force/torque sensing not listed.

## Actuation & power
Unitree in-house joint motors (R1-biped lineage: low-cost QDD-style actuators; vendor-claimed). Battery: ~1.5 h runtime [S1]; capacity n/a; charger included; no hot-swap documented.

## Compute & software
Body: 8-core CPU; head unit: 8-core CPU + 10 TOPS NPU acceleration [S1]. Connectivity: WiFi 6, Bluetooth 5.2 [S1]. OTA updates + secondary development support (Unitree SDK; the G1/R1 ecosystem is ROS2-friendly with open SDKs — vendor-claimed) [S1]. No VLA/autonomy stack bundled; intended as a development platform (teleop/data-collection accessories from the R1 ecosystem apply).

## Safety & compliance
n/a (not disclosed). Consumer-electronics-style distribution (webshop) without ISO 13482/10218 claims; light masses (11-32 kg) reduce risk vs full-size platforms.

## Deployment evidence & traction
Launch-quarter product: no named customers yet (announced ~May 2026). Distribution and traction can be inferred from Unitree's track record: >5,500 humanoids shipped 2025, #1 global unit share (32.4%), massive research install base [S3]. Chinese press framed R1-D as "further lowering the entry threshold for high-performance humanoid robots" [S2]. Expect rapid uptake in university labs and education — estimated.

## Assessment (analyst view)
*Analyst opinion.* Strengths: unbeatable price (from $4,290), Unitree's actuator vertical integration and quality-at-volume reputation, global channel, modular SKU ladder (fixed→wheeled, 5→7 DoF). Weaknesses: light payload (2-4 kg), ~1.5 h battery, minimal onboard AI compute (10 TOPS), no safety certification, no autonomy stack — it is a component/platform, not a solution. Threat to an EU entrant: severe at the low end — it annihilates any business model premised on selling entry research hardware at €30-80k; EU players must differentiate on payload, certified safety, integration and application software. Strategically, R1-D signals Unitree will fill every embodiment niche; a heavier wheeled industrial SKU from Unitree would be the real disruption to watch.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.unitree.com/mobile/R1-D/ | All SKUs, DoF, dimensions, weights, payload, torque, sensors, compute, $4,290 | vendor-claimed |
| 2 | https://finance.sina.cn/stock/jdts/2026-05-01/detail-inhwkimm6728813.d.html | May 2026 launch, RMB 26,900, 15-31 DoF range, market framing | third-party |
| 3 | https://lite.duckduckgo.com/lite/?q=Unitree+IPO+STAR+2026 (IPO coverage) | Company traction context (5,500 units, margins, IPO) | third-party |
