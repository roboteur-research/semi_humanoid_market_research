# Zerith H1 — Zerith Robotics (零次方)

> H1 is a hotel-housekeeping wheeled humanoid ("轮臂式" wheel-arm robot): a height-adjustable dual-arm torso (workspace 0-220 cm, 23 DoF, ~55 kg) on a compact universal-wheel chassis, purpose-built to clean bathrooms, vacuum, make up rooms and restock amenities. Announced May 2025 by a post-'00s Tsinghua team, backed by >¥100M and already in 20+ venues with a claimed 100-units/month ramp — the clearest Chinese "one-vertical closed loop" semi-humanoid play, claiming ~50% hotel cleaning cost reduction. A sibling model Z1 exists in the lineup.

| Field | Value |
|---|---|
| Company | Zerith Robotics (零次方机器人) |
| HQ | Hefei/Beijing, China |
| Status (2026) | shipping (early production; 20+ venues) [third-party] |
| First shown / launch | Announced 05/2025 [S4] |
| Target applications | Hotel housekeeping: bathroom cleaning (shower/toilet/sink), vacuuming, amenity restocking, tidying; hospitality services |
| Price | n/a (not disclosed); orders "tens of millions ¥" reported [S1] |
| Availability | China; direct/RaaS-style hotel deployments [estimated] |

## Design & morphology
Wheeled humanoid ~1.3-1.8 m (height-adjustable body), ~55 kg; total workspace reach 0-220 cm vertically (floor pickup to high shelves); 23 DoF; arm length 797.6 mm [S3, third-party spec DBs]. Compact universal-wheel chassis sized for narrow hallways, elevators and furnished rooms [S3].

## Locomotion
Universal-wheel (omni-capable) chassis; speed n/a (not disclosed). Elevator- and corridor-compatible footprint [S3].

## Upper body & manipulation
Dual arms (797.6 mm each) with grippers/dexterous end-effectors capable of scrubbing motions, picking items from floor, placing toiletries, organizing shoes; multi-plane operation (vertical surfaces, floor, counters) [S2][S3]. Payload n/a (not disclosed). Torso height adjustment provides the 0-2.2 m envelope [S3].

## Sensing
3D lidar (1), 5 ultrasonic sensors, depth cameras, and 4 array-type tactile sensors (contact-rich cleaning tasks) [S3, third-party]. Multi-sensor fusion for navigation among furniture and guests [S2].

## Actuation & power
n/a (not disclosed).

## Compute & software
Dual Intel Core i7-1265U processors [S3]; ROS 2-based stack [S4]; Zerith-V0 specialized-scenario embodied foundation model powering ultra-long-sequence multi-task operation — claimed 5-hour continuous error-free runs [S1, vendor-claimed]. Autonomy level: task-loop autonomy in constrained hotel-room scenario.

## Safety & compliance
n/a (not disclosed). Operates around guests in pilot venues [S2, third-party observation].

## Deployment evidence & traction
20+ venues deployed; orders in the tens of millions of yuan, intention orders ~¥100M; production ramp claimed at 100 units/month with 500-unit year-end multi-model target [S1][S3, third-party reporting of vendor claims]. Independent coverage (Interesting Engineering) of real housekeeping operation [S2]. Claim: ~50% reduction in hotel cleaning cost [S4, vendor-claimed].

## Assessment (analyst view)
*Analyst opinion.* Strengths: sharpest vertical focus in the Chinese cohort — bathroom cleaning is high-frequency, high-pain, measurable-ROI work; tactile sensing + height-adjust morphology fit the task; real multi-venue deployments within a year of founding; specialized foundation model avoids general-VLA fragility. Weaknesses: months-old company with unproven reliability economics (water, chemicals, edge-cases); no published pricing/safety certification; hotel labor economics differ sharply between China and the EU. Threat to an EU entrant: high in hospitality — this is the exact beachhead segment (hotel housekeeping loop) an EU semi-humanoid would want, and Zerith will arrive with Chinese cost structure; monitor for EU market entry via hotel chains.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://36kr.com/p/3399692881725574 | Funding, V0 model, 5h error-free claim, orders, ramp targets | third-party |
| 2 | https://interestingengineering.com/innovation/chinas-zerith-h1-housekeeping-robot | Housekeeping capabilities, deployment coverage | third-party |
| 3 | https://www.originofbots.com/robot/zerith-h1-by-zerith-details-specifications-rating (+ rbtx.com, aparobot, humanoid.press DB entries) | 23 DoF, 0-220cm, 1.3-1.8m/55kg, 797.6mm arms, dual i7-1265U, tactile/lidar/ultrasonic suite, 20+ venues, 100/mo | third-party |
| 4 | _work/discovery_china.md entry 32 | 05/2025 announcement, ROS2, Z1 sibling, 50% cost-cut claim | third-party (compiled) |
