# Mobile ALOHA — Stanford University

> Mobile ALOHA is Stanford's open-source, ~$32k wheeled bimanual teleoperation-and-imitation-learning platform (two Trossen ViperX 300 arms plus two leader arms on an AgileX Tracer base). It is a research rig, not a product, but its January 2024 cooking demos went viral and its hardware/software recipe became the de-facto standard for low-cost mobile manipulation data collection — the direct ancestor of Sunday Robotics' Memo, Trossen's ALOHA kits, AgileX Cobot Magic and much of Physical Intelligence's data pipeline.

| Field | Value |
|---|---|
| Company | Stanford University (IRIS Lab; Fu, Zhao, Finn) |
| HQ | Stanford, CA, USA |
| Status (2026) | research (open-source; commercial kits sold by Trossen/AgileX) |
| First shown / launch | 4 Jan 2024 (arXiv 2401.02117 + viral demo videos) |
| Target applications | mobile manipulation research: cooking, cleaning, household tasks; teleop data collection for imitation learning |
| Price | ~USD 32k self-build BOM [S2]; Trossen Mobile AI kit ~USD 23-34k [S6] |
| Availability | build-it-yourself (MIT-licensed hardware docs) or Trossen/AgileX kits, worldwide |

## Design & morphology
Low-slung AgileX Tracer differential-drive AGV base carrying a vertical frame with two 6-DoF Trossen ViperX 300 S follower arms mounted facing forward, plus two smaller leader arms (operator puppeteering) that are removed for autonomous runs [S2]. Arms cover a workspace 0.65-2.0 m above the floor and extend 1.0 m beyond the base; each arm lifts ~1.5 kg, and the system can exert 100 N pulling force at 1.5 m height (opening heavy cabinets, pulling chairs) [S2]. A 14 kg, 1.26 kWh battery sits in the base as ballast. Total DoF: 12 in arms (2×6) plus the mobile base; no torso lift (fixed frame).

## Locomotion
Differential drive (2 powered wheels), max ~1.42-1.6 m/s — deliberately human-walking speed so the tethered operator can drive it by walking [S2]. 100 kg base payload (Tracer spec) [S3]. Indoor flat-floor only.

## Upper body & manipulation
2× ViperX 300 S: 6 DoF each, 750 mm reach, Dynamixel smart-servo joints, parallel-jaw grippers with custom low-cost fingers [S2][S3]. Teleoperation is joint-space mapping from kinematically similar WidowX-scale leader arms; the operator's waist is tethered to the base so the human backdrives base motion while both hands run the arms — the signature "whole-body teleoperation" trick [S2]. No tool changer, no media at flange, repeatability not stated (hobby-class servos).

## Sensing
3× Logitech C922x RGB webcams (one on each wrist, one front/top view), 640×480 @ 50 Hz [S2]. No lidar, no depth, no force-torque or tactile sensing — policies are vision + proprioception only. Base odometry from Tracer.

## Actuation & power
Dynamixel XM-series smart servos (geared DC) in arms; hub-motor diff-drive base. 1.26 kWh battery, runtime not formally stated (multi-hour, powers arms + laptop) [S2]. No dock/hot-swap.

## Compute & software
Consumer laptop onboard: Intel i7-12800H + RTX 3070 Ti (8 GB) [S2]. ROS-based stack; all code MIT open-source: hardware repo github.com/MarkFzp/mobile-aloha, learning repo github.com/MarkFzp/act-plus-plus (ACT, Diffusion Policy, VINN implementations), public datasets and tutorial [S1]. Key result: co-training with 825 static-ALOHA episodes lifts success to 80-95% on tasks like Wipe Wine (95%), Call Elevator (95%), Use Cabinet (85%), Rinse Pan (80%) from only 20-50 mobile demos per task [S2].

## Safety & compliance
None — research prototype; no certifications, no rated safety functions (e-stop on base only). Not for unsupervised operation.

## Deployment evidence & traction
No commercial deployments (research rig), but exceptional research traction: demo videos of shrimp sautéing/serving reached tens of millions of views in Jan 2024 [S4]; dozens of labs replicated the platform; Trossen sells official kits (~$8-17k stationary, ~$23-34k mobile) [S6]; AgileX sells the Cobot Magic derivative; Google DeepMind's ALOHA 2 and ALOHA Unleashed extend the line [S5]. Direct commercial lineage: Tony Zhao co-founded Sunday Robotics (Memo, $1.15B valuation 3/2026) [S7].

## Assessment (analyst view)
*Analyst opinion.* Mobile ALOHA is not a competitor product but it defines the cost floor and the data-collection paradigm of the segment. Strengths: unbeatable price/openness, huge community, proven imitation-learning results. Weaknesses: toy-grade payload (~1.5 kg), no safety engineering, hobby servos with poor durability/repeatability — nothing here ships to a customer. Threat to an EU entrant is indirect but large: it commoditizes bimanual mobile teleop hardware, meaning differentiation must come from reliability, safety certification and fleet software, not from the basic morphology; and it continuously feeds trained talent and datasets to US/Chinese startups.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://mobile-aloha.github.io/ | project page, repos, tutorial, datasets | vendor-claimed (project) |
| 2 | https://arxiv.org/html/2401.02117v1 | all hardware specs, cost, success rates | vendor-claimed (paper) |
| 3 | https://www.roboticscenter.ai/blog/mobile-aloha-setup | BOM breakdown, Tracer/ViperX prices | third-party |
| 4 | https://www.freethink.com/robots-ai/mobile-aloha | virality, media coverage | third-party |
| 5 | https://aloha-unleashed.github.io/ | DeepMind follow-ups | vendor-claimed |
| 6 | https://www.trossenrobotics.com/aloha | commercial kit pricing | vendor-claimed |
| 7 | https://techcrunch.com/2026/03/12/humanoid-robotics-maker-sunday-reaches-1-15b-valuation-to-build-household-robots/ | Sunday Robotics lineage | third-party |
