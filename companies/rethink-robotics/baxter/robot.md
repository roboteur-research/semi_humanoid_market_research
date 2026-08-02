# Baxter — Rethink Robotics

> Baxter (2012) was the first mass-produced, affordable ($22k) dual-arm humanoid-torso cobot: two 7-DoF series-elastic arms, an animated screen face, and train-by-demonstration instead of programming. Aimed at light US manufacturing, it instead found its market in research/education before Rethink's 2018 collapse. It is the historical benchmark for "cheap dual-arm torso" — and for why compliance without precision fails in industry.

| Field | Value |
|---|---|
| Company | Rethink Robotics |
| HQ | Boston, MA, USA |
| Status (2026) | discontinued (production ended ~2018; company defunct twice — 2018 and 2025) |
| First shown / launch | 18 Sept 2012; Baxter Research Edition early 2013 |
| Target applications | light industrial pick/place, packing, kitting, machine tending; research & education (Research Edition) |
| Price | USD 22,000 base (+pedestal, ~$25k typical); Research Edition similar [S1][S2] |
| Availability | discontinued; large secondhand/lab install base persists |

## Design & morphology
Stationary torso on optional wheeled pedestal (manually pushed, not self-driving) — a "semi-humanoid" without autonomous mobility. Torso height 0.94 m; 1.78-1.91 m on adjustable pedestal; weight 74 kg bare / ~139 kg with pedestal [S1][S2]. Two 7-DoF arms + 2-DoF head (pan + screen nod); 12" LCD "face" showing eyes that telegraph intent (looks where it will reach) [S2].

## Locomotion
None powered — pedestal has casters for manual repositioning. (Included here as the canonical dual-arm torso platform; frequently mounted on carts/AMRs by researchers.)

## Upper body & manipulation
2× 7-DoF arms, 104 cm reach, 2.2 kg (5 lb) payload each [S1][S2]. Series-elastic actuators (springs in series with motors) give passive compliance and force sensing at every joint — safe to bump, but repeatability only ~±5 mm class and slow motion, the root of its industrial shortcomings [S2][S3]. End-effectors: interchangeable electric parallel gripper or vacuum cup kit. Zero-G "guide by hand" teaching (Intera software); no code required, or full ROS SDK on Research Edition.

## Sensing
Head: 360° sonar ring (presence detection), front camera; each wrist: camera + IR rangefinder + accelerometer; joint torque sensing throughout via SEA deflection [S2]. No lidar, no depth camera stock.

## Actuation & power
Series-elastic actuators (brushed DC + spring), the signature Brooks-era safety tech. Mains-powered (no battery) [S2].

## Compute & software
Onboard PC in torso (3rd-gen Intel Core-class), running Intera (proprietary train-by-demo + behavior engine) or, on Research Edition, an open ROS SDK that made Baxter the most common bimanual research platform of the 2010s [S2][S4]. Fleet management: none (pre-dates the concept in cobots).

## Safety & compliance
Designed to run cage-free alongside workers ("inherently safe" via SEAs + sonar presence slow-down); pre-dated ISO/TS 15066 and was never formally certified to it — safety was engineering-argument-based, a notable regulatory footnote [S2][S3]. E-stop provided.

## Deployment evidence & traction
Thousands of units shipped across Baxter+Sawyer lifetime (Rethink-claimed "thousands"; exact Baxter split not disclosed); early industrial users included plastics/packaging SMEs (e.g. Vanguard Plastics), but industrial churn was high; the durable install base was hundreds of university labs — for years the default bimanual manipulation-learning testbed [S2][S3][S4]. Production wound down as Sawyer took over (~2016-18); support ended with the 2018 collapse; HAHN/URG relaunch (2024) revived only single-arm products before itself shutting down in Aug 2025 [S5][S6].

## Assessment (analyst view)
*Analyst opinion.* Baxter proved demand for an affordable dual-arm humanoid form factor and pioneered hand-guided teaching and screen-face social signaling that modern semi-humanoids reuse. Its failure defined the trap an EU entrant must avoid: passive compliance traded away the precision and cycle time industry actually pays for, and $22k hardware still lost money at Rethink's volumes. Threat: zero (defunct), but expect Baxter comparisons in every industrial sales conversation about dual-arm cobots, and note that its research niche is now served by ALOHA-class rigs at a third of the price.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://en.wikipedia.org/wiki/Baxter_(robot) | launch date, price, dimensions, payload | third-party |
| 2 | https://robotsguide.com/robots/baxter | specs, SEAs, sensors, Intera, history | third-party (IEEE) |
| 3 | https://www.therobotreport.com/rethink-robotics-closes-doors/ | failure analysis, 2018 shutdown | third-party |
| 4 | https://spectrum.ieee.org/rethink-robotics-baxter-robot-factory-worker | launch coverage, design intent | third-party |
| 5 | https://www.therobotreport.com/rethink-robotics-relaunches-with-cobots-amrs-mobile-manipulation/ | 2024 relaunch has no dual-arm | third-party |
| 6 | https://www.therobotreport.com/rethink-robotics-shuts-down-again/ | Aug 2025 second shutdown | third-party |
