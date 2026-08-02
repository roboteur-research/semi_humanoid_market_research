# Moz1 (小墨 "Xiaomo") — Spirit AI (千寻智能)

> Moz1 is Spirit AI's first commercial wheeled humanoid: a 26-DoF, fully force-controlled dual-arm robot on a 4-wheel mecanum omni base, unveiled June 2025 and debuted at WAIC 2025. Its differentiators are proprietary "highest power-density" integrated force-control joints with a claimed 1:1 whole-machine load-to-weight ratio, whole-body zero-latency teleoperation for data collection, and the Spirit v1 VLA. It matters competitively because it already runs on a CATL battery-pack production line — one of the most credible industrial humanoid deployments in China — and because Huawei's Hubble fund backed the company.

| Field | Value |
|---|---|
| Company | Spirit AI (千寻智能) |
| HQ | Hangzhou, China |
| Status (2026) | shipping |
| First shown / launch | Released June 2025; public debut WAIC 2025 (Shanghai, July); also shown WRC 2025 |
| Target applications | EV-battery / electronics assembly and test, logistics, office services (tidying, delivery), embodied-AI research |
| Price | ~USD 150,000 (third-party aggregator estimate; official: on request) [S7] |
| Availability | China; direct sales; developer docs public (docs.spirit-ai.com); shipping to research + industrial customers |

## Design & morphology
Humanoid torso on wheeled chassis. Per official docs drawings: overall height 1,850 mm, base footprint ~650 × 650 mm (685 mm diagonal), base height ~292 mm [S5]. Third-party sources list 160 cm / 70 kg — likely an earlier/marketing figure vs. the 1,850 mm full-extension drawing; treat height as configuration-dependent [S7]. DoF total 26: 4 (omni base) + 6 (leg-waist 腰腿 articulation) + 7 per arm ×2 + 2 (neck) [S5]. The 6-DoF leg-waist lets the torso pitch/crouch for low picks.

## Locomotion
4-wheel mecanum omnidirectional base (rollers visible in docs drawings); docs limits: cartesian speed 500 mm/s, rotation 60°/s (conservative software limits) [S5]. Indoor use.

## Upper body & manipulation
- Arms: 2 × 7 DoF, joint speed limits 210–300°/s (docs) [S5].
- Whole-machine load-to-weight ratio 1:1 (vendor-claimed; implies payload on the order of machine mass, marketing framing) [S2].
- End-effectors: standard config ships with two 2-finger grippers (二指夹爪, docs); marketing renders and press show 5-finger dexterous hands with "10+ DoF each" — hands appear to be an option [S5][S7].
- Force control: all joints are integrated force-control units, "globally highest power density" (vendor-claimed); joint impedance control, drag teaching, collision detection exposed in SDK [S2][S5].
- Repeatability: n/a (not disclosed).

## Sensing
Head: camera + lidar unit (docs FOV diagram: head sensor cones 50°/57° downward coverage) with 2-DoF neck; base: front lidar (52° cones, 4° ground clearance angle) [S5]. Chest camera visible in product photo (estimated). Joint torque sensing throughout (force-control architecture) [S2].

## Actuation & power
Proprietary integrated force-control actuators (QDD-class power-dense units; exact type not disclosed) [S2]. Lithium battery; charger 54.8 V / 10 A (≈13S pack) [S5]. Capacity/runtime: n/a (not disclosed). Custom battery technology developed with CATL claimed in one report [S6].

## Compute & software
- Spirit v1 VLA: three-stage training pyramid — pre-trained base model (10,000+ h embodied data) for generalization; imitation-learning fine-tuning (~24 h) for precision; RL post-training for robustness (>95% task success); chain-of-thought reasoning for planning [S4].
- High-precision, high-speed WBC (whole-body control); whole-body zero-latency teleoperation [S2].
- MozRobot SDK; MovaXHelper Windows HMI; "SpiritAI MovaX" tablet app (Wi-Fi hotspot); Ethernet control interface (fixed IP); 4-level user permission model; simulation support: NVIDIA Isaac and MuJoCo; π0.5 open-model adaptation documented [S5].
- Onboard compute: n/a (not disclosed).

## Safety & compliance
Three e-stops (platform rear, back panel, handheld wireless); brake engage/disengage; collision detection; impedance-controlled compliant joints [S5]. No ISO 13482/10218 or CE certification publicly claimed.

## Deployment evidence & traction
- CATL (宁德时代) Zhongzhou base: "Xiaomo" robots deployed on a battery-pack line — connector insertion for EOL/DCR end-of-line testing, ~99% insertion success, up to 3× efficiency vs prior method; promoted as world's first scaled humanoid production-line deployment (third-party reported, vendor-promoted) [S6].
- Office pilots: desk tidying, trash disposal, chair repositioning driven by Spirit v1 (vendor demo/pilot) [S2][S4].
- Trade shows: WAIC 2025 + WRC 2025 — bartending service, moonwalking while balancing held objects, garment folding/stacking (third-party observed) [S2][S6].
- Unit counts: n/a (not disclosed).

## Assessment (analyst view)
*Analyst opinion.* Strengths: genuine full-force-control joint IP (the founder built ROKAE's torque-controlled cobots), a public, unusually transparent developer documentation set (rare among Chinese humanoid startups), a marquee CATL production-line reference, and enormous capital runway (~RMB 4.5B raised, Huawei Hubble on the cap table). Weaknesses: hardware is young (June 2025), key specs (payload, runtime, compute) undisclosed, and the flagship deployment is a single (if high-profile) customer; standard end-effector is only a 2-finger gripper despite dexterous-hand marketing. Threat to an EU entrant: high in force-sensitive assembly niches — 1:1 load-to-weight force-controlled arms plus RL-hardened task success rates target exactly the precision-assembly use cases an EU industrial entrant would pitch; no European presence or certifications yet, buying EU players perhaps 1–2 years.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.spirit-ai.com/ | Company identity, mission | vendor-claimed |
| 2 | https://www.stcn.com/article/detail/2763729.html | 26 DoF, force-control power density, 1:1 ratio, WBC, teleop, WAIC demos, June 2025 release | third-party |
| 3 | DuckDuckGo aggregate (Hubble/funding articles) | Huawei Hubble stake, funding | third-party |
| 4 | https://www.spirit-ai.com/product (Spirit VLA pyramid graphic) | Spirit v1 training stages, >95% RL success, CoT | vendor-claimed |
| 5 | https://docs.spirit-ai.com/zh/moz1/mechanics.html (+get-started.html) | DoF breakdown, dimensions drawing (1850mm, 650×650 base), joint speeds/ranges, grippers, e-stops, SDK, sim support, charger 54.8V/10A | vendor-claimed (official docs) |
| 6 | DuckDuckGo aggregate (宁德时代 小墨 articles) | CATL Zhongzhou line, 99% insertion, EOL/DCR, 3x efficiency | third-party |
| 7 | https://humanoid.guide/product/moz1/ | 160cm/70kg listing, ~$150k price est., 5-finger hand claim | third-party (estimated) |

*Unknown fields = n/a (not disclosed).*
