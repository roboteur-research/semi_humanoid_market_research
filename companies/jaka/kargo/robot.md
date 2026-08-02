# JAKA Kargo — JAKA Robotics (节卡机器人)

> Logistics-specialised wheeled dual-arm robot released at CIIF 2025 (23 Sep 2025) on JAKA's EVO embodied platform: two 7-axis cobot-lineage arms and a sensor head travel on a 0–800 mm lift column inside a gantry frame over an omnidirectional AMR base with an integrated cargo deck — purpose-built for sorting, tote handling and machine loading without conveyor/track infrastructure. Competitively, it converts JAKA's certified cobot precision and 10,000-unit factory channel into a self-carrying mobile manipulation product distinct from the more general K1W.

| Field | Value |
|---|---|
| Company | JAKA Robotics (节卡机器人) |
| HQ | Shanghai, China |
| Status (2026) | shipping / in production [S1] |
| First shown / launch | 23 September 2025, 25th China International Industrial Expo (CIIF), Shanghai [S2] |
| Target applications | Intelligent sorting, material transport, picking/placing, machine loading in warehouses, factories, logistics centers |
| Price | ~USD 65,000 (third-party listing) [S1] |
| Availability | China; direct/integrator sales via JAKA cobot channel (DE/JP subsidiaries exist at company level) |

## Design & morphology
Distinctive gantry architecture (verified image): white/black vertical frame with an overhead camera bar; the dual-arm torso + stereo-camera head rides the column with 0–800 mm vertical travel; the low omnidirectional base doubles as a cargo deck for carrying totes/parts between stations. Height 156.5 cm (to ~175 cm with lift), weight 180 kg, 21 DoF total [S1][S2].

## Locomotion
Omnidirectional wheeled base with autonomous navigation ("glide in any direction", no track infrastructure required); max speed 4 km/h (1.1 m/s) [S1][S2]. IP20 — indoor only [S1].

## Upper body & manipulation
Two 7-axis arms (JAKA cobot joint lineage), 5 kg payload each; coordinated dual-arm and arm-base synchronised motion with a 1 ms communication/control cycle (EtherCAT heritage) [S1][S2]. End-effectors: application-specific grippers from JAKA's cobot tooling ecosystem (cobot flanges visible in image). Waist/torso lift 0–800 mm covers floor-to-shelf picking [S1]. Repeatability n/a for Kargo (JAKA K-family claims ±0.05–0.1 mm).

## Sensing
Multimodal sensing: overhead gantry camera, stereo/depth head cameras (visible in image), plus navigation sensors on base; details not itemised [S1][S2]. Force sensing n/a for Kargo (K1W sibling has 6-axis F/T in arms; likely shared, estimated).

## Actuation & power
JAKA integrated modular cobot joints (harmonic-drive class; lineage, estimated). Runtime ~4 h per charge [S1]. Battery capacity, hot-swap n/a.

## Compute & software
Intel Core i5 12th-gen with 128 GB SSD (listing) [S1]. Software: built on JAKA EVO, the "AI + industrial intelligent robot OS" launched at CIIF 2025; autonomous navigation and task orchestration for sorting/loading workflows [S2]. SDK/ROS n/a.

## Safety & compliance
IP20; safety features not itemised — JAKA's cobot lines carry CE/ISO cobot certifications, Kargo-specific certification not stated (estimated). 

## Deployment evidence & traction
Launched at CIIF 2025; "in production" per listing [S1]. No named Kargo customers yet; company-level: 300+ embodied-family units delivered in 2024, Fortune-500 factory pilot for sibling K1W, >10,000 cobots installed [see company.md]. 

## Assessment (analyst view)
*Analyst opinion.* Strengths: the pragmatic gantry + cargo-deck layout (carry-and-manipulate) targets the highest-ROI wheeled-humanoid use-case — tote logistics — with cobot-grade arms, 1 ms control and an existing integrator channel; ~$65k undercuts most dual-arm mobile manipulators. Weaknesses: 4 h runtime, IP20, 5 kg arms cap application range; humanoid.guide is the only spec source for several figures. Threat to a new EU entrant: moderate-to-high in intralogistics — JAKA has a German subsidiary and could bring Kargo to EU factories through its cobot accounts faster than most Chinese humanoid startups.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/jaka-kargo/ | specs (156.5 cm, 180 kg, 21 DoF, 7-axis 5 kg arms, 0–800 mm lift, 4 km/h, 4 h, i5/128GB, IP20), $65k, image | third-party |
| 2 | https://lite.duckduckgo.com/lite/?q=JAKA+Kargo (aggregated snippets) | CIIF launch 2025-09-23, JAKA EVO platform, coordinated arm-base motion, applications | third-party |
