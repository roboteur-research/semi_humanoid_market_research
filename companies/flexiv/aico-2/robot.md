# AICO 2 (爱可) — Flexiv (非夕科技)

> AICO 2 is Flexiv's mobile dual-arm platform: two 7-DoF Rizon-heritage adaptive force-controlled arms on a differential-drive base with laser SLAM, aimed at embodied-intelligence development and force-sensitive industrial tasks. Its differentiators are cobot-grade numbers rarely seen on mobile humanoids — ±0.05 mm repeatability and 0.03–0.1 N force-sensing accuracy — plus configurable payload (2×4 kg or 2×10 kg). The stationary MICO sibling (shown at ICRA 2026, Vienna) shares the same 2×7-DoF force-control architecture in a 53–79 kg torso. Together they represent the force-control specialist path into semi-humanoids.

| Field | Value |
|---|---|
| Company | Flexiv |
| HQ | Shanghai, China (+ Santa Clara, CA) |
| Status (2026) | announced (in development / early commercial; sold as development platform) |
| First shown / launch | AICO 1 earlier; AICO 2 listed 2025-26; MICO demoed ICRA 2026 (Vienna, 1-5 June 2026) |
| Target applications | Embodied-AI R&D, precision/force-sensitive industrial automation (assembly, polishing, tending), lab automation |
| Price | n/a (not disclosed) |
| Availability | Direct from Flexiv (CN/US/EU offices); one tracker lists AICO-2 "commercially available", Flexiv materials frame it as a development platform — early-commercial |

## Design & morphology
Dual-arm torso with sensor head on a compact wheeled AMR base with handle frame. Two configurations [S1]:
- AICO 2-4: 2×7-DoF arms, 2×4 kg payload, 780 mm reach, 281 kg total weight, 6 h battery.
- AICO 2-10: 2×7-DoF arms, 2×10 kg payload, 845 mm reach, 395 kg total weight, 4 h battery.
Height: n/a (not disclosed). No torso lift disclosed.

## Locomotion
Dual-wheel differential drive base; laser-SLAM navigation [S1]. Speed: n/a (not disclosed).

## Upper body & manipulation
- Arms: Rizon-series adaptive arms, 7 DoF each, full joint torque sensing [S1].
- Force sensing accuracy 0.1 N / 0.03 N (config-dependent); pose repeatability ±0.05 mm [S1].
- End-effectors: Flexiv Grav gripper or third-party tooling (flange-mounted; media at flange not detailed).

## Sensing
Laser SLAM lidar on base; head sensor unit (cameras; not itemized); joint torque sensors in every axis (force-control architecture) [S1].

## Actuation & power
Proprietary torque-controlled joints (harmonic + torque sensor class, per Rizon heritage — estimated). Battery: 6 h (2-4 config) / 4 h (2-10 config) [S1]; capacity kWh n/a.

## Compute & software
Flexiv RDK (Robot Development Kit) with 1 kHz real-time control loop (documented for MICO, same stack family) [S1]; Elements GUI software for task programming; AI force-adaptive skills. ROS support via RDK bindings (vendor SDK). Onboard compute: n/a (not disclosed).

## Safety & compliance
Force-controlled compliant arms with collision detection (vendor-claimed); certifications for AICO 2 not published. Flexiv Rizon arms have established cobot safety practice (ISO 10218/TS 15066 context, estimated).

## MICO (stationary sibling — covered here)
Compact stationary dual-arm system, modular architecture on the "Enlight" platform: 2×7 DoF, 2×5 kg payload, 752 mm reach, 0.1 N force accuracy, ±0.05 mm repeatability, RDK 1 kHz control, 0–45 °C; configs Armor (55 kg), Core (53 kg), Plus (79 kg), Ultra; ~150 cm tall; max speed 0.83 m/s (trolley-mounted); whole-body touch sensitivity claimed; demoed at ICRA 2026 Vienna, in development / not yet commercially available [S1][S2].

## Deployment evidence & traction
- No named AICO 2 customer deployments found; positioned as embodied-intelligence development platform [S1].
- MICO: ICRA 2026 live demos (third-party reported) [S2].
- Company-level: Rizon arms deployed at industrial customers and massage chains; funding $222M gives staying power [S3].

## Assessment (analyst view)
*Analyst opinion.* Strengths: best-in-class force control on a mobile dual-arm (0.03 N sensing, ±0.05 mm), mature arm supply chain, bi-national footprint with a Munich office — a rare Chinese-rooted player that can serve EU customers with local support. Weaknesses: heavy (281–395 kg), no dexterous hands or telescoping torso, no VLA-scale autonomy story versus AgiBot/Spirit-class rivals, and unclear commercial status. Threat to an EU entrant: medium — Flexiv will contest the same high-precision, contact-rich industrial niches an EU player would target, and can bid in Europe today; but its platforms skew toward development kits, leaving turnkey-application ground open.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.flexiv.com/product/robot-system | AICO 2-4/2-10 and MICO full specs | vendor-claimed |
| 2 | lite.duckduckgo.com aggregate (ICRA 2026 articles) | MICO ICRA 2026 Vienna, Enlight, dev status; AICO-2 availability claim | third-party |
| 3 | https://www.therobotreport.com/flexiv-raises-more-than-100m-for-adaptive-robots/ | Funding | third-party |

*Unknown fields = n/a (not disclosed).*
