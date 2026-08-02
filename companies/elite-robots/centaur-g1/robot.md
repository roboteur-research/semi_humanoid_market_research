# Centaur-G1 — Elite Robots (艾利特)

> Centaur-G1 is cobot-maker Elite Robots' first wheeled humanoid: a 1.75 m, 20-DoF dual-arm robot on a mecanum omnidirectional base, unveiled 21 May 2026 in Hangzhou together with the upgraded "Yuanqi Primo" (元启·Primo) embodied-AI platform. Its pitch is industrial precision — ±0.1 mm dual-arm repeatability and a 2,200 mm working radius — backed by a supplier with ~10,000 cobots already in the field. It matters as the clearest example of a scaled Chinese cobot incumbent converting its arm technology, channels and installed base into the semi-humanoid category.

| Field | Value |
|---|---|
| Company | Elite Robots (艾利特机器人) |
| HQ | Suzhou, China |
| Status (2026) | announced (in development; launch targeted 2026) |
| First shown / launch | Unveiled 2026-05-21, Hangzhou |
| Target applications | Industrial inspection, intelligent manufacturing, AI infrastructure (data centers), research & education, healthcare, commercial services |
| Price | n/a (not disclosed) |
| Availability | Not yet orderable; China first (estimated); Elite has global cobot distribution that could carry it abroad |

## Design & morphology
Dual-arm humanoid torso with waist and 2-DoF-class head on a boxy mobile base; footprint 960 × 660 mm; standing height 1,750 mm; operating (working) height up to 1,500 mm [S1]. 20 DoF total: 2 × 7-DoF arms (14) + waist + head [S1][S2]. Renders show a black/white industrial design with dexterous multi-finger hands on some units and gripper tooling on others [S1].

## Locomotion
Mecanum-wheel omnidirectional base; chassis positioning accuracy ±10 mm [S1]. Speed, gradeability: n/a (not disclosed).

## Upper body & manipulation
- Arms: dual 7-DoF, 5 kg payload each [S1].
- Working radius 2,200 mm (dual-arm span envelope) [S1][S2].
- Repeatability: ±0.1 mm dual-arm (vendor-claimed — high for a mobile humanoid; presumably arm-local, chassis parked) [S1][S2].
- End-effector force sensors (6-axis F/T at wrists) [S1].

## Sensing
Head RGB-D camera for scene recognition; wrist-mounted binocular cameras for precision work; base lidar; 6-axis force-torque sensing [S1].

## Actuation & power
Battery 48 V / 40 Ah (~1.9 kWh); runtime ~240 min [S1]. Actuator types: cobot-heritage joint modules (estimated; not disclosed).

## Compute & software
- "Yuanqi Primo" (元启·Primo, formerly ELITE PAI) embodied foundation model: multimodal perception, world modeling, reinforcement learning, end-to-end decision-making [S2].
- ROS 2 support; NVIDIA Isaac Sim / Isaac Lab simulation environments; software package closed-source [S1].
- Onboard compute: n/a (not disclosed).

## Safety & compliance
n/a (not disclosed) for the humanoid. Elite's cobot lines carry standard cobot certifications, and the company is likely to follow ISO 10218/TS 15066 practice (estimated).

## Deployment evidence & traction
- Unveiled 05/2026; status "in development" per third-party tracker; no announced pilots or customers yet [S1][S2].
- Company-level: ~10,000 cobots in 50+ countries provide the conversion funnel (third-party) [S3].

## Assessment (analyst view)
*Analyst opinion.* Strengths: industrial credibility — real repeatability engineering, F/T sensing, ROS 2/Isaac toolchain, existing global sales/service network, and a "one brain, multiple forms" strategy that amortizes AI investment across cobots and humanoids. The ±0.1 mm claim, if it survives independent testing, positions Centaur-G1 for precision assembly niches most VLA-first startups can't touch. Weaknesses: late to market (2026) with no deployment evidence, modest 5 kg/arm payload, and an unproven AI stack versus VLA leaders. Threat to an EU entrant: medium-high and rising — Elite already sells cobots in Europe, so Centaur-G1 has a ready-made EU channel; an EU semi-humanoid startup could face it inside the same distributor networks within 1–2 years.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.aparobot.com/robots/centaur-g1 | Full spec set (dimensions, DoF, 5kg/arm, ±0.1mm, 48V/40Ah, 240min, sensors, ROS2/Isaac, status) | third-party (manufacturer-verified listing) |
| 2 | lite.duckduckgo.com aggregate (2026-05-21 launch coverage) | Unveiling date/place, Yuanqi Primo, 2.2m radius, target sectors | third-party |
| 3 | https://www.aparobot.com/companies/elite-robots | ~10,000 cobots, 50+ countries | third-party |

*Unknown fields = n/a (not disclosed).*
