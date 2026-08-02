# Galbot S1 — Galbot / Galaxy General (银河通用)

> Galbot's second, heavy-industrial wheeled robot, released January 2026: a 1.79 m, 320 kg dual-arm machine on a four-wheel omnidirectional base with a tall mast, lifting up to 30 kg per arm (50 kg dual-arm claim) across a 2.3 m working-height range, running 8 h with autonomous charging. Positioned as "zero-teleoperation" fully autonomous factory labor and already working at CATL production lines — the industrial complement to Galbot's retail-focused G1.

| Field | Value |
|---|---|
| Company | Galbot / Beijing Galaxy General Robot (银河通用) |
| HQ | Beijing, China |
| Status (2026) | shipping / in production (deployed at CATL) [S1][S2] |
| First shown / launch | January 2026 [S2] |
| Target applications | Factory logistics, heavy material handling, machine tending, warehouse automation |
| Price | ~USD 55,000 listed ("inquire") [S1] — likely below actual industrial config pricing (analyst caution) |
| Availability | China; direct/enterprise sales |

## Design & morphology
Industrial aesthetic (grey/orange GALBOT livery, verified image): humanoid dual-arm torso on a tall mast over a low four-wheel AMR base. Height 1,793 mm, weight 320 kg [S1][S2]. Working-height coverage up to 2.3 m via mast/arm articulation [S2]. DoF total n/a (not disclosed).

## Locomotion
Four-wheel omnidirectional base; max speed 1.5 m/s (5.4 km/h); autonomous navigation with obstacle avoidance [S1][S2]. Autonomous dock charging [S2].

## Upper body & manipulation
Dual arms, up to 30 kg per arm / ~50 kg dual-arm combined payload — the heaviest lift claim among Chinese wheeled humanoids to date [S1][S2]. End-effectors: 2-finger industrial claws/grippers (verified image shows angled parallel grippers) [S1]. Reach/repeatability n/a.

## Sensing
Dual RGB cameras + dual 3D radars (lidar) per listing [S1]; head sensor pod with stereo cameras visible in image. Force/tactile n/a.

## Actuation & power
Actuators n/a (not disclosed). Runtime 8 h per charge with autonomous recharging [S1][S2]. Battery capacity n/a.

## Compute & software
NVIDIA Jetson AGX Orin 64 GB (275 TOPS) [S1][S2]. Software: Galbot's simulation-first stack (SynGrasp/GraspVLA foundation-model lineage) with "zero-teleoperation" fully autonomous operation claimed [S2]; fleet/enterprise software subscription model at company level.

## Safety & compliance
n/a (not disclosed). Autonomous obstacle avoidance claimed [S1].

## Deployment evidence & traction
Deployed in regular use on CATL battery-factory production lines (reported "actual use", extending Galbot's existing CATL relationship — CATL led its Series B) [S2, third-party]. Company-level: several-thousand-unit cumulative orders claimed across G1/S1 family; Mercedes-Benz China, Bosch, BYD etc. pilots (family-level, see company.md) [S2].

## Assessment (analyst view)
*Analyst opinion.* Strengths: 30 kg-per-arm payload is category-leading and directly addresses the heavy-tote/heavy-part gap that keeps most wheeled humanoids out of real logistics; backed by Galbot's ~$1.15B war chest, GraspVLA autonomy stack and CATL/automotive channel. Weaknesses: 320 kg mass complicates safety cases around people; DoF/precision specs undisclosed; $55k listed price looks like marketing anchor rather than delivered-config price. Threat to a new EU entrant: high — this is the strongest Chinese industrial wheeled-humanoid offer on paper, from the sector's best-funded player, and it will anchor payload/price expectations in EU procurement conversations.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/galbot-s1/ | specs (179 cm, 320 kg, 30 kg/arm, 5.4 km/h, 8 h, Orin 64GB, dual RGB + dual 3D radar, omni base), $55k listing, image | third-party |
| 2 | https://lite.duckduckgo.com/lite/?q=Galbot+S1+银河通用 (aggregated snippets) | Jan 2026 release, 50 kg dual-arm payload, 2.3 m height coverage, zero-teleoperation, CATL deployment | third-party |
