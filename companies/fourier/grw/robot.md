# GRW (轮式双臂机器人 GRW) — Fourier Intelligence

> GRW is Fourier's first wheeled dual-arm robot, unveiled at WAIC Shanghai in July 2026. It is a heavy-payload semi-humanoid — 16 kg stable payload, 29 DoF, 585 mm shoulder width, height-adjustable 1,160-1,650 mm, ~160 kg — with three quick-swap end-effector families (gripper, suction, dexterous hand) and 4 h hot-swappable batteries. Positioned for warehouse intake/transfer and eldercare lifting assistance, it extends a leading Chinese biped maker (GR-1/2/3 heritage) into the wheeled category and shares the FOCUS fleet-control stack with Fourier's bipeds. Competitive significance: payload-first wheeled design from a care-robotics brand, aimed at the two niches (logistics + eldercare) with the clearest near-term demand.

| Field | Value |
|---|---|
| Company | Fourier Intelligence (傅利叶) |
| HQ | Shanghai, China |
| Status (2026) | announced (WAIC Jul 2026; commercial availability not yet confirmed) |
| First shown / launch | WAIC 2026, Shanghai (coverage 10-18 Jul 2026) [S1][S2] |
| Target applications | Warehouse/logistics intake and transfer, manufacturing material handling, eldercare mobility/lifting assistance |
| Price | n/a (not disclosed) |
| Availability | n/a; China first (no export info) |

## Design & morphology
Wheeled dual-arm torso robot on a compact base: footprint 720 × 618 mm, height adjustable 1,160-1,650 mm via lift mechanism, weight ~160 kg [S1]. 29 DoF excluding end-effectors [S1]. Deliberately narrow 585 mm shoulder width for movement through tight aisles and doorways ("narrow-shoulder, long-arm configuration") [S1][S2]. ~2 m operational radius/work envelope [S1].

## Locomotion
Wheeled chassis; ZOL coverage describes a parallel mechanism with independent drive and steering per wheel (omnidirectional-capable) [S3]. Speed, climbing and terrain limits n/a (not disclosed). Anti-tipping protection and automatic shutdown on tilt are built in [S2].

## Upper body & manipulation
Dual arms, 16 kg stable maximum payload (能扛起16公斤) — among the highest payloads in the wheeled semi-humanoid class [S1][S2]. Per-arm DoF not separately published (29 DoF whole-body). Quick-change end-effector system with three families: parallel gripper, suction cup, and dexterous hand [S1][S2]. Flange media (power/data/pneumatics for the suction option) not documented. Repeatability n/a.

## Sensing
Not itemized in launch coverage; compliant joint control implies joint torque sensing [S3]. Cameras/lidar configuration n/a (not disclosed) — a gap to close when the datasheet appears.

## Actuation & power
Fourier self-developed FSA-family joint actuators presumed (company-wide platform; not explicitly confirmed for GRW — estimated). Battery: hot-swappable, 4 h per charge, supporting all-day cycles via swap [S1][S2]. Safety braking: mechanical locking on power loss [S2].

## Compute & software
Onboard compute n/a (not disclosed). Software: integration with Fourier FOCUS fleet/robot control system — multi-robot deployment, automatic task allocation, path planning, collision avoidance [S1][S2]. AI/VLA claims are notably absent from launch messaging; positioning is pragmatic automation rather than "embodied AGI".

## Safety & compliance
Vendor-claimed safety features: power-loss mechanical locking, anti-tipping protection, automatic shutdown on tilt or collision, compliant joint control for close human collaboration [S2][S3]. No ISO 13482/10218 or CE certifications claimed yet (n/a). Eldercare positioning will force certification work — watch this.

## Deployment evidence & traction
Launch-stage only: WAIC 2026 booth demos (material retrieval, transfer, eldercare assistance scenarios) [S1][S2]. No named customers, pilots or unit counts yet (announced ~1 month before this research). Fourier's GR-3 eldercare channels (hospitals, care facilities) are the obvious first deployment path — estimated.

## Assessment (analyst view)
*Analyst opinion.* Strengths: class-leading 16 kg payload with a genuinely narrow 585 mm body, swappable end-effectors, hot-swap power, and a parent company with real actuator IP, rehab/eldercare domain credibility and Gulf capital. Weaknesses: brand-new product with zero deployment evidence, no disclosed sensing/compute/price, and softer AI story than AgiBot/Galaxea peers. Threat to an EU entrant: medium-high and rising — Fourier is one of the few Chinese players whose eldercare positioning directly overlaps European demographics-driven demand, and its rehab business already sells into European healthcare channels, giving it a regulatory and distribution head start most Chinese humanoid firms lack.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.ithome.com/0/978/489.htm | 16 kg, 720×618×1160-1650 mm, ~160 kg, 29 DoF, 585 mm shoulders, 2 m envelope, 3 EE types, 4 h hot-swap, FOCUS | third-party (quoting vendor) |
| 2 | https://finance.sina.com.cn/tech/roll/2026-07-18/doc-iniifhua1538003.shtml | WAIC 2026 launch, safety features, applications, FOCUS details | third-party |
| 3 | https://ai.zol.com.cn/1213/12130171.html | Parallel-mechanism wheel drive w/ independent drive+steering, compliant control, GR-series context | third-party |
