# ADAM — Richtech Robotics

> ADAM is Richtech's dual-armed, pedestal-mounted beverage-service semi-humanoid — an egg-shaped white torso with two 6-axis cobot-style arms behind a counter, working as barista, bartender and boba maker. Shipping since ~2022, it is among the most widely field-proven Western semi-humanoids in commercial hospitality (Walmart ghost kitchens, stadiums, arenas, Kennedy Space Center) and anchors the Western F&B price envelope at $180k list / $3,500 per month RaaS. Competitively it shows that stationary dual-arm "human workstation" robots can generate real (if modest) revenue today — and it supplies the arm/manipulation stack for Richtech's mobile Dex.

| Field | Value |
|---|---|
| Company | Richtech Robotics (Nasdaq: RR) |
| HQ | Las Vegas, NV, USA |
| Status (2026) | shipping (since ~2022) |
| First shown / launch | ~2021-22 (CES appearances; commercial installs from 2022) [S4, estimated] |
| Target applications | Beverage prep and service: coffee/espresso, cocktails, boba tea; customer interaction/upsell in QSR, cafés, bars, stadiums, events |
| Price | $180,000 list; RaaS $3,500/robot/month (25-unit/60-month/$5.25M agreement); event rentals from ~$15k/day [S3] |
| Availability | US direct + RaaS; China via Beijing Tongchuang distribution deal ($4M+) [S1][S3] |

## Design & morphology
- Stationary pedestal/counter-integrated base — rounded egg-shaped torso shell with head unit, flanked by two arms; no mobility (ADAM works a fixed human-shaped workstation) [S2][S5, photo evidence].
- Two white 6-axis collaborative-robot-style arms with tube-and-joint architecture (photo evidence) [S5].
- Height/weight/DoF: n/a (not disclosed).

## Locomotion
- None — fixed installation (mobility is what Dex adds by putting ADAM-line arms on a Titan AMR base) [S2].

## Upper body & manipulation
- Dual coordinated 6-axis arms perform multi-step drink workflows: grabbing cups, operating espresso machines and dispensers, shaking cocktails, sealing boba cups; choreographed dual-arm motion is the core IP ("brainchild of Wayne Huang, who has spent decades building AI systems to control robotic arms") [S2].
- End-effectors: gripper fingers adapted to cups/utensils (details n/a); throughput reported at 200+ drinks/day in commercial settings [S4, third-party directory].
- Payload/reach: n/a (not disclosed).

## Sensing
- Vision-AI system for workspace monitoring and consistency; interactive customer-facing behavior (gesture animation, NLP dialog for orders/recommendations) [S2][S4, vendor-claimed].
- Details of cameras/F/T sensors: n/a (not disclosed).

## Actuation & power
- Mains-powered fixed installation (no battery); actuator details n/a (not disclosed).

## Compute & software
- Proprietary Richtech stack: AI arm-control algorithms + cloud management software ("R&D innovation first, focusing on AI algorithms and cloud management software") [S2].
- NLP-based ordering/interaction; recipe/workflow library for drinks; remote fleet monitoring [S2][S4].
- ADAM's manipulation stack feeds the Dex program (Isaac Sim Sim2Real training added there) [S2].

## Safety & compliance
- Operates behind counters/sneeze guards in human-facing venues; no published ISO 10218/13482 or NSF/UL certification details (n/a, not disclosed). Food-service deployments imply local health-code compliance [estimated].

## Deployment evidence & traction
- One Kitchen ghost kitchens inside Walmart stores: first install Dawsonville GA (2024-06-13), Rockford IL (08/2024); Jan-2024 non-binding LOI for 240 ADAM systems; Oct-2024 binding LOI — Richtech to franchise-operate 20 Walmart-located restaurants (AZ/CO/TX) [S3][S6, third-party].
- Las Vegas Clouffee & Tea café: 16,000+ drinks served by 06/2025 [S3, third-party].
- botbar boba café (Brooklyn, NY); Vegas Golden Knights arena (T-Mobile Arena); Texas Rangers' Globe Life Field; Kennedy Space Center Visitor Complex [S3, third-party].
- RaaS economics disclosed: 25 units / 60 months / $5.25M = $3,500/robot/month; FY2024 ADAM leasing revenue $857K [S3, third-party from filings].
- Claimed ARCO/ampm rollout: UNVERIFIED [S3, flag].
- Fleet size: ADAM units are part of Richtech's claimed 450+ total robot deployments; ADAM-specific count n/a [S2].

## Assessment (analyst view)
*Analyst opinion.* Strengths: multi-year, revenue-generating field record in unforgiving public venues; clear unit economics ($3,500/mo RaaS vs. one FTE barista at ~$3-4k/mo makes the pitch arithmetic work); entertainment value drives venue marketing. Weaknesses: stationary (a "robot kiosk" more than a robot worker), low throughput ceiling, thin specs disclosure, and the parent's financial fragility (FY2025 revenue $5.05M, -$15.75M loss, restatement) undermines fleet-support credibility. Threat to an EU entrant: low-to-medium — ADAM proves and popularizes the F&B semi-humanoid use case (relevant to any EU hospitality play) but has no European installs, no CE narrative, and its $180k price is exposed to Chinese dual-arm drink cells at a fraction of the cost (cf. Keenon XMAN-R1 ~$100k). The bigger lesson is its RaaS pricing benchmark.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://stockanalysis.com/stocks/rr/ + filings synthesis (market_context §3) | financials, Tongchuang China deal | third-party |
| 2 | https://www.therobotreport.com/richtech-dex-demonstrates-potential-wheeled-mobile-manipulators/ | Huang arm-control background, product line, 450 deployments, RaaS model, ADAM→Dex lineage | third-party (interview) |
| 3 | _work/market_context.md §4.4/§7 (project research w/ underlying PRs) | $180k list, $15k/day, $5.25M/25-unit RaaS, $857K FY2024 leasing, Dawsonville 06/2024, Clouffee 16k drinks, arenas/stadium/KSC, ARCO unverified | third-party / estimated |
| 4 | https://robotomated.com/ + robot directories (search 2026-08-02) | 200+ drinks/day, Vegas hotel/airport presence, interaction features | third-party (directory, low authority) |
| 5 | images/adam-serving.jpg (Richtech photo via The Robot Report) | visual: egg torso, dual 6-axis arms, counter workstation at burger/cheesesteak QSR | third-party (photo evidence) |
| 6 | https://lite.duckduckgo.com/lite/?q=Richtech+Ghost+Kitchens+America+robot+service+agreement+ADAM (search synthesis) | Ghost Kitchens 240-unit LOI, binding 10/2024 franchise, Rockford install | third-party |
