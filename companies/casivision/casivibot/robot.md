# CASIVIBOT — CasiVision (中科慧远)

> Dual-arm wheeled "embodied quality-inspection robot" from Chinese AOI-equipment leader CasiVision, launched 19 August 2025. It packages the company's multispectral inspection optics (three-camera eye), 7-DoF arms with interchangeable grippers and the proprietary HuiBrain AI into a compact mobile platform for in-line and roaming quality inspection plus light service tasks. Competitively notable as a vertical-specialist embodiment play priced aggressively (~$29k listed) rather than a general-purpose humanoid.

| Field | Value |
|---|---|
| Company | CasiVision (中科慧远) |
| HQ | China |
| Status (2026) | announced / early production ("in production" per listing) [S1] |
| First shown / launch | 19 August 2025 [S2] |
| Target applications | Industrial quality inspection (3C/panel), healthcare, hospitality, commercial service, research labs |
| Price | ~USD 29,000 (third-party listing; configuration-dependent, "inquire") [S1] |
| Availability | China; export availability n/a (not disclosed) |

## Design & morphology
Compact dual-arm torso on an enclosed wheeled AMR base with a prominent oval sensor head housing a ring-lit three-lens multispectral camera cluster (verified image); CAS branding on chest, red e-stop on base deck. Height 140 cm, weight 55 kg, 14 DoF overall [S1, third-party]. Torso is fixed on a central column; no lift stated.

## Locomotion
Wheeled platform (enclosed; drive type not disclosed), max speed ~3.5 km/h (~1 m/s) [S1]. Indoor use, IP20 [S1]. Terrain/brakes n/a.

## Upper body & manipulation
Two arms (14 DoF total suggests ~7 DoF each, matching launch reporting of 7-DoF arm design [S2]); payload ~10 kg (listing; per-arm split n/a) [S1]. End-effectors: 2-finger gripping claws, 2–3 DoF each, described at launch as "interchangeable intelligent grippers" — i.e. a tool-swap concept for inspection fixtures [S1][S2]. Repeatability n/a.

## Sensing
Head: three-camera multispectral sensing array with ring illumination — the core differentiator, derived from CasiVision's AOI optics [S2]. Listing estimates 1080p RGB + depth [S1, estimated]. Base sensors, force/tactile n/a (not disclosed).

## Actuation & power
Electric servo motors with harmonic/planetary gears (listing estimate) [S1, estimated]. Runtime ~8 h per charge [S1]. Battery capacity, hot-swap, dock n/a.

## Compute & software
Industrial CPU + embedded GPU (Jetson-class, listing estimate); Linux/ROS environment [S1, estimated]. Proprietary "HuiBrain" (慧脑) AI platform for the hand-eye-brain integrated architecture: defect detection, grasp planning, task orchestration; designed to collaborate with fixed AOI stations across the quality lifecycle [S2]. Connectivity: Wi-Fi, Ethernet, Bluetooth [S1].

## Safety & compliance
IP20; "safe operation in indoor environments" (listing) [S1]. No ISO/CE certifications found. Physical e-stop visible on base (verified image).

## Deployment evidence & traction
Launch coverage across major Chinese outlets (Tencent, Sina, Zhihu; Baidu Baike entry) [S2]. CasiVision's installed AOI base in 3C/panel factories is the obvious deployment channel, but no named CASIVIBOT customers, pilots or unit counts found.

## Assessment (analyst view)
*Analyst opinion.* Strengths: real domain moat (industrial inspection optics + defect AI honed over ~9 years), installed customer base to sell into, very low listed price, and a focused use-case where wheeled dual-arm morphology genuinely helps (roaming inspection with part handling). Weaknesses: modest platform specs (14 DoF, 3.5 km/h, IP20), no disclosed safety certification or force sensing, and specs rest heavily on an unverified third-party listing. Threat to a new EU entrant: low outside China and outside inspection; instructive, though, as the vertical-specialist pattern that can lock up the QC niche before generalist humanoids arrive.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/casivibot/ | specs (140 cm, 55 kg, 14 DoF, 10 kg, 3.5 km/h, 8 h, IP20), price ~$29k, image | third-party |
| 2 | https://lite.duckduckgo.com/lite/?q=CASIVIBOT+中科慧远 (aggregated snippets) | launch 2025-08-19, hand-eye-brain design, three-camera multispectral array, HuiBrain, AOI background | third-party |
