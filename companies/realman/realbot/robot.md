# RealBot S2 & L2 — RealMan Robotics (睿尔曼)

> RealBot-S2 (folding) and RealBot-L2 (lifting) are full-size wheeled dual-arm humanoids debuted by Beijing arm/joint-module incumbent RealMan at WAIC 2026 (unveiled 2026-07-19). Built entirely from RealMan's own 50,000-hour-MTBF joint modules and sold with the GLN teleoperation network and Darwin data platform, they target data collection, home service, retail guidance and light manufacturing — a components-incumbent's reliability-first counterpoint to demo-driven humanoid startups. This dossier covers both variants.

| Field | Value |
|---|---|
| Company | RealMan Robotics (睿尔曼智能) |
| HQ | Beijing, China |
| Status (2026) | announced (WAIC 2026 debut; orderable via sales inquiry; sibling platforms already deployed) |
| First shown / launch | WAIC 2026, Shanghai, unveiled 2026-07-19 [third-party] |
| Target applications | S2: data collection & training, home service, retail, industrial manufacturing; L2: home service, retail guidance, data collection [vendor-claimed] |
| Price | n/a (not disclosed) |
| Availability | Direct/inquiry (CN + international site); ODM/OEM services offered [vendor-claimed] |

## Variant comparison (official spec pages, vendor-claimed) [S1][S2]

| Spec | RealBot-S2 (folding) | RealBot-L2 (lifting) |
|---|---|---|
| Dimensions | 614 × 552 × 1700 mm | 650 × 512 × 1700 mm |
| Weight | ≈125 kg | ≈120 kg |
| Total active DoF | 20 | 17 |
| Arms | 2× 7-DoF, 5 kg payload each, 0.69 m reach (w/o EE) | 2× 7-DoF-class, 5 kg payload each |
| Vertical working range | 0–2.1 m (leg folds to floor level) | 0–2.1 m via 300 mm lift travel |
| Torso mechanism | Folding "knee" leg (ground-level retrieval) | Lift column, 0.3 m travel, lift capacity ≥60 kg (arms + payload) |
| Chassis | Four-steer four-drive (4S4D) | Two-wheel differential |
| Speed | 0.1–1.5 m/s | 0.1–1.0 m/s |
| Compute | NVIDIA Jetson AGX Orin 64GB | Jetson AGX Orin 64GB / D-Robotics S100 |
| Head sensing | Stereo RGB ×1 + fisheye ×2 (360° surround), dual-LiDAR navigation | Stereo RGB (std), depth optional |
| Hand cameras | RGBD std / mono RGB opt | RGBD std / mono RGB opt |
| End-effector | 2-finger gripper / 5-finger hand, quick-swap | 2-finger gripper / 5-finger hand, quick-swap |
| Battery / runtime | 48V 20Ah, ≈6 h | 48V 20Ah, ≈6 h, ~1 h full charge |
| Connectivity | Wired, WiFi, 5G (optional) | Wired, WiFi |

## Design & morphology
Both are 1.70 m humanoid torsos on wheeled bases, differing in the height mechanism: the S2 uses an articulated folding leg (render shows a knee-like pillar) that crouches to floor level and folds compactly — press reports add 90° lateral movement and a 413 mm minimum turning radius [S4, third-party]; the L2 uses a conventional 300 mm lift column rated ≥60 kg (arm assembly + payload) [S1][S2]. Quick-release modules throughout for fast maintenance/upgrade, plus OTA remote O&M [S1].

## Locomotion
S2: four-steer four-drive chassis (omnidirectional, incl. sideways translation), 0.1–1.5 m/s. L2: two-wheel differential chassis, 0.1–1.0 m/s [S1][S2].

## Upper body & manipulation
Dual 7-DoF humanoid arms built on RealMan WHJ-series integrated joint modules; 5 kg per arm, 0.69 m reach (S2, without end-effector); quick-swap two-finger gripper or five-finger dexterous hand; wrist RGBD cameras standard [S1][S2]. NOTE: pre-launch press mentioned "9 kg/arm, 15 kg dual" for the L2 — the official spec page says 5 kg/arm; official figure carried in specs.json, press figure flagged as unconfirmed [conflict noted].

## Sensing
S2 head: one stereo RGB pair + two fisheye cameras for 360° surround view; dual LiDAR on chassis for navigation. L2: stereo RGB standard, depth optional. Hand RGBD standard on both. L2 markets "force compliance + dynamic obstacle avoidance, triple safety assurance" [S1][S2, vendor-claimed].

## Actuation & power
Fully self-developed integrated joint modules; vendor-claimed 50,000 h MTBF, CRL3-certified; annual module capacity >500,000 units [S3][S4]. 48V 20Ah battery (~1 kWh), ≈6 h runtime, ~1 h full charge (L2) [S1][S2].

## Compute & software
Jetson AGX Orin 64GB (S2; L2 alternatively D-Robotics S100). Software stack: GLN teleoperation network (millisecond-level cross-city teleop — Beijing operator ran a Shanghai robot making tea at WAIC; data centers Beijing + Changzhou, >10,000 h real-robot data), Darwin teleoperation/device-management/data-collection platform, "teleoperation to autonomy" roadmap; RealBOT embodied open-source platform for data collection [S3][S4][S6].

## Safety & compliance
CRL3 certification for joint modules [S3, vendor-claimed]; L2 claims force compliance and dynamic obstacle avoidance. No ISO 13482/10218 or CE declarations published for the full robots.

## Deployment evidence & traction
- WAIC 2026 live demos: opening refrigerator doors, tea preparation via cross-city GLN teleop [S3][S4, third-party].
- RealMan wheeled-robot platforms in back-kitchen use at a restaurant in Yining, Xinjiang (noodle pulling, skewering, grilling, chopping) and 24/7 inspection robots with CASI Vision (<5 s cycles) — company-level traction, predating S2/L2 [S3, third-party].
- No named S2/L2 customers yet (announced 07/2026).

## Assessment (analyst view)
*Analyst opinion.* Strengths: vertical integration down to the joint module, a quantified reliability story (50,000 h MTBF) rare in this category, dual chassis options covering narrow-aisle (S2 4S4D) and low-cost (L2 diff-drive) use cases, and a teleop-to-autonomy data business that monetizes robots before autonomy matures. Weaknesses: modest 5 kg/arm payload, no published safety certification for the full robots, no named humanoid customers, and a brand primarily known to integrators rather than end users. Threat to an EU entrant: moderate-to-high on price and components (RealMan can undercut as supplier and vendor simultaneously), though FCC 2026 import restrictions block the US channel and EU service markets still demand certifications RealMan has not shown.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.realman-robotics.com/en/products/realbot-l2.html | L2 full spec table | vendor-claimed |
| 2 | https://www.realman-robotics.com/en/products/realbot-s2.html | S2 full spec table | vendor-claimed |
| 3 | https://finance.biggo.com/news/7e7a7253-d158-4f4f-99ab-5b180295e1dc | MTBF/CRL3, GLN, Xinjiang + CASI deployments, module capacity | third-party |
| 4 | https://baike.baidu.com/en/item/RealBot-S2/3543499 | Unveiling 2026-07-19, 413 mm turning radius, 90° lateral, folding legs | third-party |
| 5 | https://robottoday.com/industry-briefing/real-work-robots-make-impact-at-waic-2026-with-50-000-hours-of-operation/8979 | WAIC dates, demos | third-party |
| 6 | DuckDuckGo-indexed CN sources | RealBOT open-source platform, funding context | third-party |
