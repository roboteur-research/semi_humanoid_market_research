# Astribot S1 — Astribot / Stardust Intelligence (星尘智能)

> The S1 is a cable-driven wheeled semi-humanoid optimized for dynamic manipulation: dual 7-DoF arms with claimed ≥10 m/s end-effector speed and 100 m/s² acceleration — the fastest published arm dynamics in the category — on a 3-DoF omni base with a flexing torso column. Sold since late 2024 into research, media, retail and eldercare pilots, it is the benchmark competitor for human-speed manipulation and whole-body imitation learning.

| Field | Value |
|---|---|
| Company | Astribot (Stardust Intelligence, 星尘智能) |
| HQ | Shenzhen, China |
| Status (2026) | shipping |
| First shown / launch | Viral demo video 2024-04; physical debut WRC 2024-08-21; commercial sales from 08/2024; batch production from ~06/2025 [S2][S4] |
| Target applications | Research/data collection, home-services R&D, eldercare, retail demos, media/entertainment; WRC 2026 medication sorting [S2][S4] |
| Price | Research edition ~¥500k (~$69k) [third-party]; B2B quote-based; sibling T1 from ¥89,900 (05/2026) [S2] |
| Availability | China direct; international research sales case-by-case; purchase (no RaaS advertised) [estimated] |

## Design & morphology
Human-scale: 1.70 m tall, ~80-90 kg (80 kg with battery per aparobot; ~90 kg production per robozaps) [S1][S2, third-party]. 23 DoF total: 2×7-DoF arms + 4-DoF torso (flexing "knee/spine" column for floor-to-high reach) + 2-DoF head + 3-DoF omni base [S2][S4, third-party]. Width across arms ~1,940 mm [S1]. A bench/pedestal (non-mobile) configuration is also sold for lab use [S1, third-party].

## Locomotion
3-DoF omnidirectional wheeled base (mobile config); speed n/a (not disclosed); indoor use [S2][S4]. The torso column flexes to reach floor level rather than the base kneeling [S4, third-party].

## Upper body & manipulation
Dual 7-DoF cable-driven arms — motors relocated to the torso, so moving arm mass is low. Vendor claims: end-effector speed ≥10 m/s, acceleration up to 100 m/s², payload 10 kg per arm, repeatability ±0.03 mm (some third-party tables cite 5 kg/arm and ±0.1 mm — conflict noted) [S1][S2][S5, vendor-claimed/third-party]. Standard end effector: parallel-jaw grippers; dexterous-hand integration shown in later demos; media at flange n/a (not disclosed) [S2]. Demonstrated skills: sub-second dynamic tasks, wine decanting, cucumber peeling, ironing, cup stacking, calligraphy, medication sorting [S2][S4, vendor video].

## Sensing
Head-mounted stereo/RGB-D camera pod (visible in photos); force sensors in joints/cables for compliant control; multimodal sensor fusion claimed; exact sensor BOM n/a (not disclosed) [S1][S5, third-party].

## Actuation & power
Signature cable/rope-driven (绳驱) transmission + electric motors; low-inertia arms with back-drivable compliance [S3, third-party]. Battery: 4-6 h active use, up to 10 h standby; ~1.5 h recharge on docking station [S2, third-party]. No hot-swap claimed.

## Compute & software
Onboard AI compute for real-time whole-body control and sensor fusion (specific SoC n/a) [S1]. Software: whole-body imitation learning from human demonstrations; VR teleoperation for data collection; zero-code visual programming interface; simulation-platform support; Astribot Suite (teleop + learning stack, paper 07/2025); LLM integration for task-level commands in demos. Closed source; SDK for B2B customers [S1][S2][S4, vendor-claimed/third-party].

## Safety & compliance
No published certifications [flag]. High-speed arm dynamics (10 m/s) are a safety liability around humans; demos are staged or teleoperated with separation. Compliant cable drive and force sensing are the claimed mitigations [estimated/vendor-claimed].

## Deployment evidence & traction
- Commercial sales since 08/2024; batch production from mid-2025; volume deliveries "thousands of units" reported from late 2025 [S2, third-party — treat volume claim with caution].
- Reported customers: JD.com, CCTV (broadcast use), elder-care institutions, retail across six Chinese cities; reported thousand-unit Thundersoft order [S2, third-party, unverified].
- WRC 2024 debut demos; WRC 2026 medication-sorting demo [S4, third-party].
- Funding validation: Ant Group-backed; 2026 cumulative >RMB 1B raised at >RMB 10B valuation [S2, third-party].

## Assessment (analyst view)
*Analyst opinion.* Astribot's differentiation is real and hard to copy: cable-drive arm dynamics an order of magnitude faster than competitors, with imitation-learning software tuned to exploit it — compelling for tasks where cycle time is the ROI lever. Weaknesses: thin verified deployment evidence relative to AgiBot/Galbot, conflicting spec disclosures, no certification story for high-speed arms near people, and a funding base ~10x smaller than the leaders. Threat to an EU entrant: moderate today, high in research/education (T1 at ¥89,900 will flood labs) and in any application where manipulation speed is decisive; low near-term threat in certified EU industrial settings.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://www.aparobot.com/robots/astribot-s1 | 1700mm/80kg, 7-DoF arms, 10 kg/arm, 10 m/s, ±0.03mm, VR teleop, zero-code, bench config | third-party |
| S2 | https://blog.robozaps.com/b/astribot-s1-review | 23 DoF breakdown, 100 m/s², battery 4-6h/10h standby, pricing, T1, customers, funding | third-party |
| S3 | DuckDuckGo-indexed CN sources | Rope-drive (绳驱) actuation, founding | third-party |
| S4 | _work/discovery_china.md entry 4 + _work/market_context.md §7 | 23 DoF/4-DoF torso, WRC 2024 debut, batch production 06/2025, WRC 2026 medication sorting | third-party (compiled) |
| S5 | DuckDuckGo spec search (aiwiki etc.) | Conflicting 5 kg/±0.1mm variants; ~$99k expected retail | third-party |
