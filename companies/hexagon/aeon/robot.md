# AEON — Hexagon Robotics

> AEON is Hexagon's industrial humanoid, launched June 2025: 1.65 m, 60 kg, 34 joints, dual arms — and a **BORDERLINE morphology for this study: wheels-on-legs**, i.e. articulated legs terminating in wheels instead of feet, rolling at up to ~9 km/h on flat floors while stepping over obstacles when needed. Backed by BMW Leipzig and Pilatus pilots and Schaeffler's commitment to 1,000+ units by 2032 (Europe's largest confirmed humanoid fleet deal), plus a metrology-grade sensing story unique in the segment, it is the most commercially advanced European industrial humanoid program.

| Field | Value |
|---|---|
| Company | Hexagon Robotics (division of Hexagon AB, Sweden) |
| HQ | Stockholm, SE (global division) |
| Status (2026) | shipping to pilot customers / early fleet ramp (announced → deployment phase) |
| First shown / launch | June 2025 (Hexagon LIVE) |
| Target applications | Machine tending (load/unload), part inspection & QC scanning, reality capture/digital twins, intralogistics |
| Price | n/a (not disclosed; one aggregator lists "$20,000 inquire" — implausibly low, treat as unreliable) [S4] |
| Availability | Pilot partners (BMW, Schaeffler, Pilatus); broader rollout with Schaeffler from end-2026 |

## Design & morphology
**BORDERLINE wheels-on-legs**: two articulated legs, each terminating in a powered wheel instead of a foot — rolls fast on even surfaces, can step/lift legs over obstacles; not a classic wheeled-base semi-humanoid, not a walking biped [S1][S2]. Height 1.65 m, weight 60 kg, **34 DoF** total, two arms with 10-fingered hands [S1][S4].

## Locomotion
Wheeled rolling on leg-mounted wheels: up to 2.5 m/s (~9 km/h) on flat factory floors — faster than any walking humanoid; stepping capability for obstacles/uneven ground [S1][S2].

## Upper body & manipulation
Dual arms, ~15 kg payload (aggregator figure) [S4]; demonstrated high-precision manipulation operating a multi-machine station — loading, unloading and inspecting parts in real production at Schaeffler [S3]. Schaeffler will supply high-precision actuators for future builds [S3].

## Sensing
22 integrated sensors: peripheral cameras, time-of-flight sensors, infrared arrays, SLAM cameras for spatial mapping, microphones; multimodal RGB/depth/lidar/force suite delivering "centimetre-accurate digital twins" — AEON doubles as a mobile reality-capture/metrology device (Hexagon's core franchise) [S1][S4].

## Actuation & power
Electric actuators (Schaeffler precision actuators entering supply chain) [S3]. Hot-swappable lithium battery packs; ~4 h per charge, swap concept for continuous operation [S4].

## Compute & software
NVIDIA Jetson AGX Orin onboard (motion planning, spatial AI, edge LLM reasoning); upcoming NVIDIA IGX Thor module for certified functional safety; trained/simulated in NVIDIA Isaac Sim + Omniverse; four-layer "physical AI" architecture with imitation learning — ~20 demonstrations suffice to train a task (vendor-claimed) [S1][S4]. Integration with Hexagon's metrology/manufacturing-intelligence software stack.

## Safety & compliance
Functional-safety path via NVIDIA IGX (safety-certified compute) announced; no completed ISO 10218/13482 certification published yet (n/a). Deployments run under plant-level risk assessments with human-adjacent operation claimed safe [S4].

## Deployment evidence & traction
- **BMW Group Plant Leipzig**: initial test deployment Dec 2025; second test phase from April 2026; full pilot phase from summer 2026 [S2][S5].
- **Schaeffler**: successful 2025 pilot (multi-machine tending + inspection); April 2026 expanded agreement — **fleet of at least 1,000 AEON humanoids across Schaeffler's global factory network by 2032**; additional applications (automated part inspection) rolling out from end-2026 [S3][S6].
- **Pilatus** (Swiss aerospace) pilot partner; aggregator-reported pilot results "40% faster QC scans, 99.9% accuracy" (vendor-derived) [S1][S4].

## Assessment (analyst view)
*Analyst opinion.* Strengths: corporate balance sheet (no funding risk), the only credible metrology/QC differentiation in the market, NVIDIA-deep stack, Schaeffler's 1,000-unit commitment plus actuator supply (vertical alignment), and BMW as reference. Weaknesses: wheels-on-legs adds legged-robot complexity/cost without full stair capability — a pure wheeled platform is simpler and cheaper for 90% of the same tasks; 4 h runtime; safety certification still prospective. Threat to a new EU entrant: very high — Hexagon owns the enterprise relationships and can bundle robots with inspection software factories already buy. An entrant should avoid QC-adjacent positioning and compete on price, openness, and true wheeled simplicity.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.therobotreport.com/bmw-piloting-hexagons-wheeled-humanoid-in-germany/ | 1.65 m/60 kg/34 DoF, wheels-on-legs, 22 sensors, imitation learning ~20 demos, launch June 2025 | third-party |
| 2 | https://www.bmwblog.com/2026/03/03/bmw-hexagon-aeon-humanoid-robot-leipzig-pilot/ | 2.5 m/s, stepping, Leipzig pilot phases | third-party |
| 3 | https://www.therobotreport.com/schaeffler-plans-to-deploy-1000-hexagon-humanoids-2032/ | Schaeffler 1,000 by 2032, pilot tasks, actuator supply | third-party |
| 4 | https://humanoid.guide/product/aeon/ | Payload 15 kg, hot-swap battery/4 h, Jetson Orin + IGX Thor, Isaac Sim, sensors, (unreliable $20k price) | third-party (aggregator) |
| 5 | https://robotics.hexagon.com/bmw-deploys-aeon-hexagon-robotics-humanoid/ | BMW deployment vendor account | vendor-claimed |
| 6 | https://roboticsandautomationnews.com/2026/04/27/hexagon-and-schaeffler-to-install-1000-aeon-humanoids-across-global-factory-network/101049/ | Fleet agreement, end-2026 inspection rollout | third-party |
