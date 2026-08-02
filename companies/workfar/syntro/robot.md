# Syntro (V17) — WorkFar

> Syntro is a teleoperation-first wheeled humanoid from bootstrapped US manufacturer WorkFar: 45 DoF including two 12-DoF four-finger hands, 20 kg payload, swappable 1.2 kWh batteries, on a 3-wheel omni base — listed from $9,999.99 (base) to $59,999.99 (full AI/fleet tier), with the popular quoted price $29,999. On paper it undercuts the whole market; in practice there is no independent deployment evidence and orders carry 6-12-month ETAs, so treat it as an ambitious pre-order product from a real plastics manufacturer, not a proven platform.

| Field | Value |
|---|---|
| Company | WorkFar Inc. (manufactured at Advantage Plastics, Louisville, KY) |
| HQ | Dover, DE (registered) / Louisville, KY (manufacturing) |
| Status (2026) | announced / build-to-order ("in production" claimed; 6-12 month ETAs; no verified deployments) [S1][S2] |
| First shown / launch | August 2024 (PR debut); V17 iteration announced ~2025-26 [S3][S4] |
| Target applications | Manufacturing, logistics/material handling, medical, hospitality; hazardous environments via telepresence |
| Price | $9,999.99 (Base) / mid Telepresence tier / $59,999.99 (Intelligent); $29,999 commonly cited [S1][S2] |
| Availability | US web store pre-order; Base 6-month ETA, Telepresence/Intelligent 12-month; robot+remote-operator monthly lease, no down payment [S1][S3] |

## Design & morphology
Humanoid head/torso/arms on a skirted wheeled pedestal base (official renders show a cone-shaped lower body over three omni wheels). Height 170 cm, 108 kg. DoF budget (vendor): head 2, arms 8 (4/arm), wrists 6 (3/wrist), hands 24 (12/hand), waist 2, wheels 3 = 45 total [S1].

## Locomotion
3-wheel omnidirectional base; max speed ~3 km/h (0.83 m/s) [S2]. Indoor floors.

## Upper body & manipulation
Two arms (4+3 = 7 DoF each incl. wrist per vendor breakdown); total payload 20 kg [S1][S2]. Hands: 4-finger dexterous hands, 12 DoF each [S1]. Teleop grasping assisted by AI targeting with VR eye tracking; haptic-glove force feedback to operator [S3]. Reach/repeatability n/a (not disclosed).

## Sensing
2D lidar, cameras (computer vision), microphones [S2]. Detail (models, counts) n/a.

## Actuation & power
Maxon motors with harmonic drives (notable quality claim at this price); metals + engineered polymers (in-house injection molding) [S2]. Swappable 1.2 kWh battery packs; 6-10 h runtime, 6-10 h charge [S1][S2].

## Compute & software
Intel multicore CPU (GPU undisclosed); Linux + ROS 2; 5G LTE + Wi-Fi 6 [S2]. Three software tiers: Base (perception/motion/safety), Telepresence (live VR teleop with headset, gloves, suit), Intelligent (AI autonomy, fleet management, IoT) [S1]. Autonomy claims are unverified; the working mode today is human teleoperation.

## Safety & compliance
"Human-safe operation" claimed; no standards or certifications cited [S2].

## Deployment evidence & traction
- No independently verified deployments, customers or pilots found (all claims from company PR).
- humanoid.guide lists it "in production, not verified" [S2].
- Continuous iteration is documented (V17 with overhauled wheeled lower body; store refresh Jan 2026) — evidence of ongoing engineering, not of field traction [S4].

## Assessment (analyst view)
*Analyst opinion.* Strengths: vertical integration with a 40-year plastics/metal manufacturer could make the sub-$30k price real; Maxon/harmonic component claims and swappable batteries are sensible; the robot+operator monthly lease is a clean labor-replacement pitch. Weaknesses: anonymous leadership, paid-PR-only visibility, 6-12-month ETAs, no third-party sightings, and a DoF/price combination that strains credibility. Threat to a new EU entrant: minimal today — but if a bootstrapped manufacturer proves a $30k teleop humanoid, it would pressure everyone's pricing; worth a monitoring file, not a battle plan.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.workfar.com/product/syntro/ | Price tiers, DoF breakdown, packages, ETAs, Advantage Plastics | vendor-claimed |
| 2 | https://humanoid.guide/product/syntro/ | 170cm/108kg/45DoF/20kg/3km/h/1.2kWh/6-10h/Maxon+harmonic/Intel/ROS2/$29,999 | third-party (aggregator, unverified) |
| 3 | https://www.prnewswire.com/news-releases/workfar-robotics-unleashes-sentient-humanoid-robots-syntro-into-the-workforce-302218378.html | Debut, VR eye tracking, haptic gloves, lease model | vendor-claimed (paid PR) |
| 4 | https://www.workfar.com/blog/ + https://www.prnewswire.com/news-releases/workfar-robotics-mass-produces-humanoid-robots-without-venture-capital-302317854.html | V17 lower-body overhaul, no-VC mass production claim | vendor-claimed |
