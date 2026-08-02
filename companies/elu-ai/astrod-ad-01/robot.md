# AstroD. AD-01 (AstroDroid) — Elu.AI / INFIFORCE (原力无限)

> Wheeled dual-arm humanoid unveiled 24 September 2025 at Alibaba's APSARA Conference: a 170 cm torso with 11-DoF dexterous force-feedback hands on an articulated linkage over an AMR base, driven by the company's Hyper-VLA model with ~200 ms end-to-end response via cloud-edge computing. Competitively, another Hangzhou model-first entrant pushing VLA latency as the differentiator in the ~$100k industrial/retail wheeled-humanoid bracket.

| Field | Value |
|---|---|
| Company | Elu.AI / INFIFORCE (原力无限), ELU.AI Technology Group |
| HQ | Hangzhou, China |
| Status (2026) | prototype (advanced prototype; pilots "planned for 2025") [S1] |
| First shown / launch | 24 September 2025, APSARA (云栖) Conference, Hangzhou [S2] |
| Target applications | Manufacturing, logistics, retail, research & education |
| Price | ~USD 100,000 (third-party listing; "inquire") [S1] |
| Availability | China; lab/demo stage, no ordering channel found |

## Design & morphology
Humanoid torso (head with LED accents, chest display) on an articulated pitch linkage over a low wheeled AMR base with visible drive wheels and sensor strip (verified image — same "torso on folding link over AMR" pattern as X-Humanoid Tian Yi). Height 170 cm, weight ~120 kg [S1]. DoF: ~40–43 total incl. two 11-DoF hands [S2]. The pitch linkage provides working-height variation (floor pick to elevated reach); no separate lift column.

## Locomotion
Wheeled base; drive type not disclosed. Max speed 7.2 km/h (2 m/s) wheeled — listing also gives an odd "2 km/h walking" figure, likely an auto-generated artifact [S1, treat cautiously]. Terrain/brakes n/a.

## Upper body & manipulation
Dual arms (per-arm DoF n/a) ending in black 11-DoF dexterous five-finger hands with force-torque feedback in the fingers ("10 fingers with force-torque feedback") [S1][S2]. Grip/payload ~3 kg (listing "grip strength") [S1]. Reach, repeatability, tool changer n/a.

## Sensing
Head sensor suite not itemised; hands carry force-torque feedback [S1]. IP42 ingress protection [S1]. Base lidar/camera details n/a (sensor strip visible in image; estimated).

## Actuation & power
Harmonic Drive reducers with brushless DC motors [S1]. Runtime ~2 h per charge [S1]. Battery capacity, hot-swap n/a.

## Compute & software
NVIDIA Jetson AGX Orin 64 GB onboard [S1]. Software: Hyper-VLA multimodal vision-language-action model targeting ~200 ms end-to-end (glass-to-action) response; cloud-edge collaborative computing for continuous model updates; ROS-compatible modular architecture [S1][S2]. Fits the group's "One Brain, Multiple Bodies, Multiple Scenarios" platform strategy [S2].

## Safety & compliance
IP42 stated; no certifications or functional-safety features disclosed [S1].

## Deployment evidence & traction
APSARA Conference demo (Sept 2025) is the only public showing found; pilot programs in manufacturing/logistics/retail "planned" but none named. No customers or unit counts. [S1][S2]

## Assessment (analyst view)
*Analyst opinion.* Strengths: credible latency-focused VLA story, force-feedback 11-DoF hands, Alibaba-ecosystem visibility, standard Orin compute making integration plausible. Weaknesses: 2 h runtime and 3 kg grip are weak for the claimed industrial use-cases; heavy (120 kg) for its class; company opaque (no funding, team, or customers disclosed); several listing figures look auto-generated. Threat to a new EU entrant: low at present — one of many Chinese prototypes; revisit if Hyper-VLA pilots materialise or funding lands.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/astrod/ | specs (170 cm, 120 kg, 11-DoF hands, Orin AGX 64GB, harmonic + BLDC, IP42, 2 h), ~$100k, image | third-party |
| 2 | https://lite.duckduckgo.com/lite/?q=Elu.AI+INFIFORCE+AstroD (aggregated snippets) | APSARA debut 2025-09-24, 40-43 DoF, Hyper-VLA ~200 ms, cloud-edge, One Brain strategy | third-party |
