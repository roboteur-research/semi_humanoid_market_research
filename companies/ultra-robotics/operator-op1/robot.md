# Operator OP1 — Ultra (Ultra Robotics)

> **BORDERLINE FOR THIS STUDY: OP1 is a stationary multi-arm workcell on locking casters — a repositionable workstation, not a mobile semi-humanoid.** It pairs a large positioning arm with a dual-arm manipulation head (two smaller arms + stereo depth camera), giving a 10×10 ft work area, 0-10 ft vertical reach and ~10 lb payload from a 5×5 ft footprint on a standard 120 V outlet. Offered as RaaS at $2,500-3,000/month, it is deployed in live 3PL operations (Highline Commerce, Brooklyn — ~30% of a linear fulfillment workflow), making it the cost/uptime benchmark that mobile semi-humanoids must beat in packing/kitting.

| Field | Value |
|---|---|
| Company | Ultra (YC S24) |
| HQ | Brooklyn, NYC, USA |
| Status (2026) | shipping (RaaS; live commercial deployments) [S2][S4] |
| First shown / launch | Aug 2024 (YC launch); commercial deployments 2025-26 |
| Target applications | E-commerce order packing, sorting, kitting, returns processing in warehouses/3PLs |
| Price | RaaS $2,500-3,000/month; 3-month trial, scale-up option [S4] |
| Availability | US; deployment "in hours, not weeks"; no fixed infrastructure [S1] |

## Design & morphology
Workcell: a large white 6-axis-class positioning arm mounted on a caster-based cell frame carries a black dual-arm "head" — two smaller ~6/7-axis manipulator arms with 2-finger grippers and a stereo depth camera — i.e., an arm-on-arm architecture rather than a humanoid torso [S3, official imagery]. Footprint 5×5 ft; work area to 10×10 ft; vertical reach 0-10 ft (can pick from floor level) [S1]. Locking casters allow manual repositioning; no powered locomotion.

## Locomotion
None (stationary by design — "zero risk of tipping over"; repositioned manually on casters) [S1][S4].

## Upper body & manipulation
Dual manipulation arms (DoF per arm not published; ~6-7 est. from imagery) plus the positioning arm; payload up to 10 lb (4.5 kg) [S1]. End-effectors: parallel grippers (imagery); tooling per task. Reach envelope up to 10 ft via positioning arm.

## Sensing
Stereo depth camera (ZED-class, per imagery) on the manipulation head; additional cameras n/a (not disclosed).

## Actuation & power
Off-the-shelf arm hardware ("reliable off-the-shelf hardware") [S2]. Mains-powered: standard 120 V outlet, 10 A peak — no batteries, enabling 24/7 operation [S1].

## Compute & software
Imitation-learned autonomous policies trained on teleoperation data; "trained with examples"; emergent behaviors reported in YC launch demo [S2]. Dedicated 10 Mbps Ethernet uplink (cloud inference/telemetry implied) [S1]. Teleop fallback presumed (not explicitly stated).

## Safety & compliance
Stationary cell reduces risk profile; no ISO/UL certifications published; n/a (not disclosed).

## Deployment evidence & traction
- Highline Commerce (Brooklyn/Atlanta 3PL): OP1 units automate ~30% of its linear pick-tote-scan-conveyor fulfillment workflow in live commercial retail operation — one of the first humanoid-style deployments outside the Amazon ecosystem [S4, third-party].
- "Robots operational in warehouses across America"; "zero down days" at customer sites (vendor-claimed) [S1][S4].
- YouTube videos show OP1 packing real e-commerce orders [S5].

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.ultra.tech/ | Footprint, reach, payload, power, trial model, 24h operation | vendor-claimed |
| 2 | https://www.ycombinator.com/launches/LeE-ultra-building-the-next-million-robots-to-automate-american-warehouses | Imitation learning, off-the-shelf hardware, team | vendor-claimed |
| 3 | https://cdn.sanity.io/images/cyk6luo4/production/6683a89bd942d28e9618d2471f34ff225788a027-1280x854.png | Arm-on-arm dual-manipulator architecture, grippers, depth camera | vendor image (analyst read) |
| 4 | https://www.humanoidsdaily.com/news/highline-commerce-taps-ultra-robotics-to-automate-30-of-fulfillment-in-brooklyn-hub + https://thenewwarehouse.com/2025/12/22/ai-powered-warehouse-robots-redefining-order-packing/ | Highline 30%, $2.5-3k/mo, stationary rationale | third-party |
| 5 | https://www.youtube.com/watch?v=zH44CNV33_4 | Live packing operation video | third-party |
