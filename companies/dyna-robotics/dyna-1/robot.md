# DYNA-1 — Dyna Robotics

> DYNA-1 is a stationary dual-arm robot workcell — two arms flanking a central camera/sensor mast on a table or cart — driven by Dyna's DYNA-1 dexterous foundation model. It is shipping today into hotel/commercial laundry and food-prep operations, where it has demonstrated 24-hour fully autonomous runs at 99.4% success with zero interventions. Competitively it matters because it sets the production-reliability benchmark for dexterous manipulation at a fraction of humanoid cost, and because its Series A ($120M @ $600M+) shows investors backing "arms first, mobility later".

| Field | Value |
|---|---|
| Company | Dyna Robotics |
| HQ | Redwood City, CA, USA |
| Status (2026) | shipping (commercial deployments) |
| First shown / launch | Emerged from stealth March 2025 (seed + first napkin-folding results) |
| Target applications | Commercial laundry folding (hotels, laundromats-by-the-pound), food prep/plating, kitting/assembly, gyms (towels) |
| Price | n/a (not disclosed); RaaS/monthly "sell labor not hardware" model per third-party coverage |
| Availability | US commercial deployments; direct engagements, no public ordering |

## Design & morphology
Stationary bimanual workcell: two robot arms permanently mounted left/right of a central white pillar carrying the main camera head (visible in deployment footage), installed on a table or wheeled cart/stand at a folding station [S1][S4]. No head/torso anthropomorphism beyond the sensor mast; no legs or powered base. Early units used off-the-shelf arms; Dyna states it is moving to custom arms and a mobile base for future versions [S3]. Dimensions/weight n/a (not disclosed).

## Locomotion
None — stationary/cart-mounted (repositionable by staff). A mobile base is in development per Salesforce Ventures [S3].

## Upper body & manipulation
Two arms (vendor does not disclose make, DoF or payload; deployment video shows compact ~6-DoF arms with simple parallel-jaw style grippers augmented with custom fingers) [S4, observed]. The assignment/discovery notes quick-swap grippers; this is consistent with task-specific finger modules seen across laundry vs. food tasks but is not documented on the vendor site — tag vendor-claimed/unverified. Manipulation skills demonstrated: napkin folding (production grade; 75% of folds at top quality grade 4-5/5), shirt folding across fabrics/sizes (40+ shirts/hour), cup filling, plating [S1][S4].

## Sensing
Central mast-mounted camera head (RGB; depth not specified); additional wrist/scene cameras not disclosed. The DYNA-1 model consumes streaming video for progress estimation and subtask labeling [S1].

## Actuation & power
Electric arms (details n/a); mains-powered workcell (battery n/a — stationary deployment). 24/7-capable: 24-hour continuous runs demonstrated; deployed robots reportedly work 16+ h/day [S1][S2].

## Compute & software
DYNA-1 foundation model: dexterous manipulation policy plus a foundation reward model (RM) that scores robot experience, enables automatic data segmentation/progress estimation, and closes an RM-in-the-loop training cycle for continuous improvement; model "adapts across environments and learns new skills within hours" (vendor) [S1]. Real-time self-correction claimed. Compute location (onboard vs. edge server) not disclosed. No public SDK — closed commercial system.

## Safety & compliance
n/a (not disclosed). Operates in shared back-of-house spaces alongside staff; no ISO/CE claims published.

## Deployment evidence & traction
- Paying customers folding napkins/laundry: hotels, commercial laundries ("by the pound" operations), restaurants, gyms — vendor "Deployed Today" + Bloomberg-cited deployments working 16+ h/day [S1][S2] (vendor-claimed / third-party).
- Benchmark run: 24 h autonomous, 850+ napkins (Salesforce Ventures says 900+), 99.4% success, ~60% human speed, zero interventions [S1][S3] (vendor-claimed, third-party-repeated).
- Factory/kitting use case marketed with "99%+ reliability" claim [S4] (vendor-claimed).
- No customer names or unit counts disclosed.

## Assessment (analyst view)
*Analyst opinion.* Strengths: best published reliability figures in the sector, elite AI team (reward-model pedigree), cheap simple hardware, real revenue-generating deployments, and deep-pocketed strategic investors (NVIDIA, Amazon, Samsung, LG). Weaknesses: single-task-family deployments so far (fabric folding), undisclosed unit economics, no mobility (fixed workcell limits addressable tasks), and total dependence on its closed model stack. Threat to a new EU entrant: HIGH in laundry/food-service verticals — DYNA-1 will likely be the incumbent benchmark in any EU commercial-laundry deal within 1-2 years; LOW in mobile/multi-station industrial work until their mobile base ships. Counter-positioning for an EU entrant: mobility + European service/compliance footprint + open integration, while matching their published reliability metrics.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.dyna.co/research/dyna-1 | Model architecture, 24h/850+ napkins/99.4%, quality grades, skills, paying customers | vendor-claimed |
| 2 | Bloomberg + funding press (via search) | Series A $120M @ $600M+; deployments in hotels/restaurants/laundromats/gyms 16+ h/day | third-party |
| 3 | https://salesforceventures.com/perspectives/welcome-dyna-robotics/ | Founders, off-the-shelf → custom arms + mobile base, 900+ napkins/99% | third-party |
| 4 | https://www.dyna.co/ | Positioning ("Autonomous Dexterity at Production Scale"), 40+ shirts/hour, factory/food applications, deployment video frames (arm/gripper/cart observations) | vendor-claimed |
