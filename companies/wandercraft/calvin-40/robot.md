# Calvin-40 — Wandercraft  **[EXCLUDED-as-biped]**

> **SCOPE FLAG: Calvin-40 is a BIPEDAL, headless industrial humanoid — it walks on two legs and is therefore OUTSIDE the semi-humanoid (wheeled/pedestal) scope of this study.** The discovery-survey note describing it as "wheeled" is incorrect (conflict resolved against primary press reporting: "the first two-legged, headless robot is already hard at work" at Renault Douai [S2]). This dossier is retained because Calvin-40 is the reference European humanoid factory deployment (Renault, 350 units by ~2027) that wheeled competitors will be benchmarked against.

| Field | Value |
|---|---|
| Company | Wandercraft |
| HQ | Paris, France (+ New York) |
| Status (2026) | shipping (limited production / pilot deployments; Renault line duty) |
| First shown / launch | Calvin gen-1 April 2025; Calvin-40 unveiled with Renault partnership June 2025 |
| Target applications | Heavy lifting in automotive/industrial manufacturing: tire handling, panel carrying, bin picking (planned) |
| Price | ~USD 65,000 (third-party reported; not officially confirmed) [S3] |
| Availability | Direct/strategic partnerships (Renault, Sapa); not generally orderable |

## Design & morphology
Headless bipedal humanoid, 170 cm tall, ~80 kg. DoF: 28 overall incl. 10 in hands (third-party spec sheets; one press source says 32 — 28 is the more repeated figure) [S3]. Sensors and cameras are waist-mounted instead of head-mounted — lower vantage improves sight of tools/parts and lets the robot fit under equipment and between shelves; LED lights communicate status [S2].

## Locomotion
Dynamic self-balancing bipedal walking (Wandercraft's exoskeleton balance-control heritage); walking speed ~3 km/h; force sensors in feet for balance on uneven floors [S3]. **Not wheeled.**

## Upper body & manipulation
Two arms; total lift capacity up to 40 kg ("several hundred times a day without rest") [S2]. Hands with 10 DoF total; current production tasks limited to tire lifting and panel carrying — bin picking of mixed parts trainable but not yet deployed (speed and dexterity are the limiting factors, per Renault) [S2][S3].

## Sensing
Waist-mounted HD/4K day/night cameras; foot force sensors; voice-command interface; LED status signaling [S2][S3].

## Actuation & power
Electric actuation derived from Atalante exoskeleton drivetrain know-how (details not disclosed). Battery runtime ~4 h per charge [S3].

## Compute & software
NVIDIA Jetson edge compute with NVIDIA Isaac robotics platform; Linux real-time stack with ROS 2; LLM/VLM integration for voice-commanded task reasoning (third-party spec aggregation) [S3][S4]. AI training doubled the machine's speed within six months of gen-1 [S2].

## Safety & compliance
No published ISO/CE robot-safety certification for the humanoid; designed "to integrate safely and reliably into any industrial setting" (vendor claim). Operating on a live automotive line implies plant-level risk assessment/CE machinery conformity, but nothing is publicly documented (n/a).

## Deployment evidence & traction
- Renault Douai EV plant (Renault 5 line): first unit(s) in production duty mounting/moving tires to the assembly conveyor; verified by Renault executives in press (Mar 2026) [S2].
- 350 units planned across Renault EV factories within ~18 months of Mar 2026 (i.e. by 2027) [S2][S3].
- Renault Group minority investment, $75M Series D (June 2025); design-to-cost industrialization support [S1][S5].
- Sapa Group (plastic automotive components) signed late 2025 [S3].

## Assessment (analyst view)
*Analyst opinion.* Calvin-40 is the strongest evidence in Europe that humanoid labor is entering real production — but it also demonstrates why bipeds remain constrained: tasks are limited to heavy, slow, repetitive lifts; Renault itself cites speed/dexterity limits and no presence on final assembly. For a wheeled semi-humanoid entrant this is both threat and validation: threat, because Renault's ~$65k biped resets price expectations and locks in a flagship account; validation, because a wheeled platform with better uptime (no balance energy cost, 4 h runtime is weak), higher speed, and cheaper certification can attack the same intralogistics tasks. Wandercraft's balance-control moat does not transfer to wheeled competitors' domain.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.therobotreport.com/wandercraft-unveils-new-industrial-humanoid-renault/ | Unveiling, Renault minority investment, company background | third-party |
| 2 | https://insideevs.com/news/790259/renault-wandercraft-humanoid-robot-ev-factory/ | BIPEDAL confirmation, Douai, tire task, 350 units/18 mo, 40 kg, $75M, waist cameras, 2nd gen in 40 days | third-party |
| 3 | https://humanoid.guide/product/calvin-40/ | 170 cm, 80 kg, 28 DoF (10 hands), 3 km/h, 4 h runtime, $65k, Sapa, Jetson/Isaac/ROS 2 | third-party (aggregator) |
| 4 | https://www.globenewswire.com/news-release/2025/06/11/3097632/0/en/wandercraft-announces-series-d-round-bringing-75m-in-total-funding-secured-for-global-acceleration-of-ai-powered-robotics.html | Series D, NVIDIA partnership, 40-day dev, Renault production in 40 weeks | vendor-claimed (PR) |
| 5 | https://www.imveurope.com/article/wandercraft-partners-renault-launch-ai-powered-humanoid-industrial-robot-computer-vision | Renault partnership, vision system | third-party |
