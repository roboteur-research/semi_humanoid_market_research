# Isaac 1 — Weave Robotics

> Isaac 1 is a wheeled, fabric-covered home robot with two 6-DoF arms, a collapsible telescoping torso (0.91-1.75 m) and simple two-finger grippers, sold at $7,999 (or $449/month) for laundry and daily tidying with first California deliveries in fall 2026. It is autonomous by default with remote human teleoperation as guaranteed fallback, and its design is all about domestic acceptance: swappable soft shells, physical camera shutters and a furniture-like charging "home". Competitively it defines the current Western entry price for a mobile two-armed home robot — half of 1X NEO's $20k and below Sunday's ~$10k target — from a YC-backed team that already ships a stationary laundry robot (Isaac 0).

| Field | Value |
|---|---|
| Company | Weave Robotics (YC S24) |
| HQ | San Francisco, CA, USA |
| Status (2026) | shipping (pre-orders open; first deliveries fall/September 2026) |
| First shown / launch | Isaac 1 launched 07/2026; predecessor Isaac 0 shipping since 02/2026 [S1][S3] |
| Target applications | Home: "Laundry Flow" (find/collect dirty clothes, handle hampers, fold, put away) and "Daily Reset" (make beds, arrange pillows/blankets, put toys/shoes/clutter away); possible washer/dryer loading depending on home |
| Price | $7,999 up-front or $449/month subscription; $250 fully refundable deposit; commercial pricing on request [S1] |
| Availability | Fall 2026 California first; broader US through 2027; direct pre-order online [S1] |

## Design & morphology
- Wheeled base with central column and collapsible telescoping torso; height range 3'0"-5'9" (0.91-1.75 m) — extends to human height to work, collapses to be "out of sight and out of mind" [S1, vendor-claimed].
- Footprint 20.5" × 22" (52 × 56 cm W×D) [S1].
- DoF: neck 2, arms 2×6, hands 2×1, torso 2, base 3 — 21 total [S1, vendor-claimed].
- Solid inner structure with swappable soft fabric shells (colorways: sage, brown, charcoal, slate, terracotta) providing passive safety and domestic look; rounded head with white face panel and two "Baymax-like" eyes [S1][S3][S5].
- Weight: n/a (not disclosed).

## Locomotion
- Wheeled base, 3 DoF (drive geometry not detailed); passively stable at all times [S1, vendor-claimed].
- Indoor home environments only; speed/terrain: n/a (not disclosed).

## Upper body & manipulation
- Two 6-DoF arms with 1-DoF two-finger grippers (orange-tipped parallel-jaw type visible in product imagery); in-house actuators, end-effectors and linkage systems [S1][S2][S5].
- Vertical reach 80" (2.03 m); horizontal reach 38" (0.97 m) [S1, vendor-claimed].
- Payload/repeatability: n/a (not disclosed). Handles "loaded hampers" (est. several kg) [S1].

## Sensing
- Head cameras with physical privacy shutters that make visually clear when the robot is/isn't working [S1][S4].
- Other sensors (depth, base lidar, force): n/a (not disclosed).

## Actuation & power
- Weave-designed proprietary actuators and "remote actuation system" [S2, vendor-claimed].
- Battery life 8 h; charge time 2 h; charging station integrated in its furniture "home" with privacy screen [S1, vendor-claimed].

## Compute & software
- Onboard compute: n/a (not disclosed). Connectivity: Wi-Fi [S1].
- Autonomy: navigates and completes Laundry Flow / Daily Reset autonomously by default; VLA + planner + VLM pipeline (per YC launch description of the stack) [S1][S2].
- Teleoperation: Weave "Remote Op" — company operators remotely complete tasks the robot cannot finish, guaranteeing task completion [S1][S2].
- Control: smartphone companion app; on-demand or scheduled tasks; works when owners are home or away; OTA capability updates [S1].

## Safety & compliance
- Passive safety via soft fabric shells and statically stable wheeled base; in-house-designed safety systems; physical camera shutters for privacy [S1][S2, vendor-claimed].
- No ISO 13482/UL certifications published (n/a, not disclosed).

## Deployment evidence & traction
- Isaac 1: pre-orders open (07/2026), deliveries from fall 2026 (CA) — pre-delivery demo visit or video call offered per order [S1, vendor-claimed]. No third-party field reports yet.
- Credibility via predecessor: Isaac 0 stationary laundry-folder shipping to homes/businesses since 02/2026 — 2,000+ cumulative field hours, 1,000+ lbs laundry folded per week fleet-wide [S2, vendor-claimed].
- Original YC plan was 30 units in fall 2025 — timeline slipped ~1 year to the mobile product [S4 vs S2, third-party].

## Assessment (analyst view)
*Analyst opinion.* Strengths: lowest price in the Western category by a wide margin, real (if small) shipping track record with Isaac 0, sensible autonomy-plus-Remote-Op model, and consumer-grade privacy/safety design others lack. Weaknesses: thin funding (~$500K disclosed pre-seed) against capital-intensive rivals ($200M Sunday, 1X $100M+), undisclosed payload/sensors, 21 DoF with 1-DoF grippers limits task ceiling, and teleop-fallback economics at $449/month may be structurally lossmaking until autonomy rates rise. Threat to a new EU entrant: medium — it anchors consumer price expectations near $8k and could reach Europe by 2028, but has no EU footprint, no CE story, and its capacity is likely to stay supply-constrained; the bigger risk is that it (with Sunday and 1X) locks up the "home robot" mindshare narrative before EU players ship.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.weaverobotics.com/isaac-1 | full spec table (8h battery, 2h charge, footprint, height 3'-5'9", reach 80"/38", DoF 2/12/2/2/3), pricing $7,999/$449, $250 deposit, fall 2026 CA, tasks, teleop fallback, app, shells, privacy | vendor-claimed |
| 2 | https://www.weaverobotics.com/about + https://www.ycombinator.com/companies/weave-robotics | in-house actuators/end-effectors/safety, CA assembly, Isaac 0 stats, founders, Remote Op, VLA/planner stack, original 2025 plan | vendor-claimed / third-party |
| 3 | https://newatlas.com/robotics/weave-robot-isaac1-laundry-bed/ | independent coverage: $8,000/$449, 3ft-5'9", Baymax-like design, Isaac 0 five months prior, camera disable, fall 2026 CA | third-party |
| 4 | _work/discovery_us_canada.md entry 2 + _work/market_context.md §3/§4.4 | Sept 2026 CA deliveries, $500K YC pre-seed, price-point context | third-party (project research) |
| 5 | images/isaac-1-sage.webp (official product photo) | visual: telescoping column, 2-finger orange grippers, fabric shells, wheeled base | third-party (photo evidence) |
