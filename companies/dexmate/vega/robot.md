# Vega — Dexmate

> Vega is Dexmate's general-purpose wheeled semi-humanoid: an omni-directional base carrying a 3-DoF foldable torso, two 7-DoF arms and a 3-DoF sensor head, 36+ DoF in total. Its signature trick is packaging — it folds to 0.66 m for transport yet works from floor level up to a 2.2 m reach — combined with an unusually long 10-30 h battery life and a developer-first software story (pip-installable Python SDK, URDF/USD sim assets, VR/exoskeleton teleop). At an MSRP of $89,999 and actually orderable from the Dexmate web shop (lead time quoted at ~3 weeks in 2026), it is one of the cheapest full-featured dual-arm mobile manipulators on the market and a direct benchmark for any EU research/light-industrial platform.

| Field | Value |
|---|---|
| Company | Dexmate, Inc. |
| HQ | Santa Clara, CA, USA |
| Status (2026) | shipping ("In Production Now") [S1][S2] |
| First shown / launch | March 2025 (preorders; robot developed in under 6 months) [S4][S5] |
| Target applications | AI/robotics research, logistics, manufacturing, retail, healthcare, education [S1][S6] |
| Price | $89,999 MSRP ($999 deposit at preorder); some third-party listings cite $80,000 [S4][S5][S3] |
| Availability | Direct via shop.dexmate.ai, US-centric; lead time ~3 weeks (was ~3 months at 2025 launch) [S1][S5] |

## Design & morphology
Wheeled omni-directional base (four visible wheels, low cabinet-style chassis) with a 3-DoF foldable torso, two arms and a 3-DoF head; 36+ DoF total [S1]. The fold mechanism compresses the robot to 0.66 m height for storage/transport; the torso extends the workspace from ground level ("0 ft") up to 2.2 m (7'2") [S1][S4]. Standing height ~171 cm and weight ~135 kg per third-party spec listings [S3]; Robotico lists 130 kg / 220 cm max [S6]. Red Dot Design Award 2025 for the industrial design [S6].

## Locomotion
Omni-directional drive, full 360-degree movement in place [S1][S7]. Speed ~4 km/h (~1.1 m/s) per third-party listings [S3]. Terrain/climbing limits not disclosed — flat indoor floors assumed (small-diameter wheels).

## Upper body & manipulation
Two 7-DoF arms; the vendor counts "13 DoFs" per arm including the end effector [S1][S3]. End-effector options include a 12-DoF five-fingered dexterous hand (visible in vendor renders; 10 fingers total across both arms) and simpler grippers; the Vega-U research grant configuration explicitly excludes the end effector, implying a modular tool interface [S3][S8]. Payload is the most contested figure: the vendor states "10+ lbs (≈4.5 kg) per arm at any pose" [S1], while the discovery notes and several third-party spec sheets state 15 kg per arm (plausibly a best-case/close-in figure, or lbs/kg confusion propagating through aggregators — treat 15 kg as unverified) [S3][S6]. 6-axis force/torque sensing at the wrists enables compliance control [S1]. Repeatability not stated.

## Sensing
Head: RGB-D and RGB cameras on a 3-DoF neck [S1][S3]. Base: LiDAR, ultrasonic sensors, IMUs [S1][S7]. Wrists: 6-axis force/torque sensors [S1]. No tactile skin claimed.

## Actuation & power
Brushless motors with harmonic gear reductions, aluminium frame (third-party) [S3]. Battery chemistry/kWh not disclosed. Runtime: "10+ hours" vendor-claimed, exceeding 30 h with arms unloaded; aggregators quote 20-25 h typical [S1][S3][S6] (discovery file's "25 h claim" sits inside this vendor range). Hot-swap/dock not disclosed.

## Compute & software
Originally shipped with Intel x86 CPU + NVIDIA Jetson AGX Orin GPU (32 GB or 64 GB options) [S3][S7]; the 2026 product page advertises "Powered by NVIDIA AGX Thor" — an in-line compute upgrade [S1]. I/O for payloads: 4x USB 3.2, Ethernet, DisplayPort, 5 V/12 V rails; WiFi 2.4/5 GHz [S1][S7]. Software: closed-source stack with a pip-installable Python API, URDF/USD models for simulation (Isaac-friendly; Dexmate is an NVIDIA Inception startup), teleoperation-ready via VR headsets and exoskeleton rigs (Dexmate also released an open-source teleoperation device), compliance control, LLM-integration touted [S1][S3][S6]. ROS compatibility is claimed by aggregators [S3] but the primary interface is Dexmate's own SDK.

## Safety & compliance
No ISO 13482/10218/TS 15066 or CE/UL certification claims found. Vendor cites compliance control with F/T sensing "for safe human interaction" [S1] — a feature, not a certification. This is a research-grade machine from a compliance standpoint (estimated).

## Deployment evidence & traction
- Orderable online since March 2025; "In Production Now", lead time ~3 weeks (vendor) [S1][S5].
- Vega units "in testing with publicly traded companies across manufacturing, logistics, and retail" (third-party, names undisclosed) [S6].
- Vega-U Research Grant Program: 6 dual-arm Vega-U platforms (valued $45,000 each) awarded to US faculty, 2025 cycle — academic seeding [S8].
- Sponsored a $200,000 challenge (WBCD) at ICRA 2025 [S6].
- Funding: ~$41M total (Dealroom/Tracxn); LG Technology Ventures / LG CNS invested (reported Feb 2026); NVIDIA-backed per press shorthand [S6][S9].
- No public unit counts or named customers; no independent field-deployment videos found beyond vendor demos (household chores, logistics demos) [S4][S5].

## Assessment (analyst view)
*Analyst opinion.* Strengths: aggressive price-performance (sub-$90k for omni base + dual 7-DoF arms + dexterous-hand option), genuinely orderable with short lead times, exceptional battery life, transport-friendly folding design, and a research-community flywheel (grants, ICRA sponsorship, sim assets) that mimics the PR2 playbook at 1/5 the price. Weaknesses: thin public deployment evidence, no safety certification story, closed-source stack, contested payload spec, and a company still small enough (single-digit LinkedIn headcount at launch) that support/service scaling is unproven. For a new EU entrant the threat is high in the research/developer segment — Vega undercuts Reachy 2 and PAL/NEURA platforms on capability-per-euro — but low in certified industrial or care deployments, where Dexmate has no EU entity, CE story or service network. Expect LG money to push Vega toward retail/logistics pilots in Asia.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://dexmate.ai/product/vega | 0-2.2 m height range, 36+ DoF, 13 DoF/arm, 3 DoF torso/head, omni base, 10+ lb/arm any pose, 10-30 h battery, sensors, AGX Thor, Python API, teleop, I/O, 3-week lead time | vendor-claimed |
| 2 | https://dexmate.ai/ | Positioning, shop, production status | vendor-claimed |
| 3 | https://humanoid.guide/product/vega/ + https://humanoidspecs.com/robots/dexmate-vega + https://www.aparobot.com/robots/vega | 171 cm / 135 kg, 7-DoF arms, 12-DoF hands, 15 kg/arm claim, 4 km/h, harmonic drives, Intel x86 + Jetson AGX Orin 32/64GB, $80k listing, ROS-compatible SDK | third-party |
| 4 | https://x.com/TheHumanoidHub/status/1896819088456110506 | March 2025 intro, <6 months development, 2'2"-7'2" height, $90K MSRP, preorders | third-party |
| 5 | https://mikekalil.com/blog/dexmate-vega/ | $89,999 price, $999 non-refundable deposit, ~3-month launch lead time, researcher/developer targeting, ~7 LinkedIn members | third-party |
| 6 | https://robotico.market/company/dexmate | Founders (Tao Chen CEO/MIT, Yuzhe Qin CTO/UCSD, Chongyang Wang COO/MIT), $41M funding, LG Technology Ventures, enterprise testing with public companies, Red Dot 2025, ICRA 2025 WBCD $200k, 25 h runtime figure, open-source teleop device | third-party |
| 7 | https://www.aparobot.com/robots/vega | Sensor suite, connectivity, 32/64 GB Orin options, closed-source + Python API, URDF/USD | third-party (manufacturer-verified listing) |
| 8 | https://www.dexmate.ai/research-grant | Vega-U variant, $45,000 value, 6 grant units, end effector excluded | vendor-claimed |
| 9 | https://app.dealroom.co/news/feed/lg-cns-invests-in-nvidia-backed-us-robotics-startup-dexmate | LG CNS investment, NVIDIA-backed | third-party |

*Conflicts noted: arm payload (vendor 10+ lb any-pose vs third-party 15 kg), price ($80k vs $89,999), runtime (10+/20/25/30 h), compute (Orin at launch vs Thor in 2026). Unknowns: battery kWh, repeatability, safety certs, unit counts.*
