# PUDU D7 — Pudu Robotics (普渡科技)

> The D7 is Pudu's first "semi-humanoid" (半人形) — the robot that coined the category label: a light (45 kg) 1.65 m wheeled dual-arm robot aimed at hospitality, retail and light industrial tasks, designed to ride Pudu's 80,000-robot global service channel. Competitively it matters less for raw specs than for category definition, price-position potential, and unmatched distribution into hotels/restaurants.

| Field | Value |
|---|---|
| Company | Pudu Robotics (普渡科技) |
| HQ | Shenzhen, China |
| Status (2026) | shipping |
| First shown / launch | Announced 2024-09-19; shown CES 2025; commercialization/shipping during 2025 [S1][S2][S5] |
| Target applications | Hospitality (hotels/restaurants), retail, hospitals, factories & logistics centers: sorting, item transport, elevator operation, shelf work [S1][S2] |
| Price | n/a (not announced publicly; pre-commercial pricing withheld) [S2] |
| Availability | Via Pudu direct + global dealer network (e.g. authorized dealers advertising D7); purchase and RaaS-style leasing typical of Pudu channel [S2][estimated] |

## Design & morphology
1.65 m tall, only 45 kg — by far the lightest full-size semi-humanoid in this study (competitors: 80-230 kg) [S1][S2, vendor-claimed]. Slim column torso on a compact omnidirectional base. 30 DoF standard; up to ~50 DoF with two DH11 11-DoF dexterous hands fitted [S2][S5, vendor-claimed]. Working range to ~2 m height [S5, third-party].

## Locomotion
Omnidirectional wheeled chassis; top speed 2 m/s (highest in class); stable on slopes to 10° [S2, vendor-claimed]. Elevator operation demonstrated (pressing buttons / API integration heritage from delivery fleet) [S2].

## Upper body & manipulation
Dual 7-DoF bionic arms; ~65 cm arm reach; payload 10 kg (vendor "10 kg lift"; one aggregator cites 14 kg dual-arm with 2 m working range); end-point precision ±0.1 mm claimed [S1][S2][S5, vendor-claimed/third-party]. End effectors: gripper standard; optional PUDU DH11 dexterous hand (11 DoF, 5 fingers) [S5, vendor-claimed]. Media at flange n/a (not disclosed).

## Sensing
Multi-sensor suite for 3D obstacle avoidance (lidar + RGB-D cameras per Pudu platform practice; exact BOM n/a); voice/gesture interaction; multi-robot coordination with Pudu delivery/cleaning fleet [S2][S5, vendor-claimed/estimated].

## Actuation & power
Electric actuators (details n/a). Battery >1 kWh; runtime >8 h continuous; autonomous battery-swap/charging referenced by dealers [S2][S5, vendor-claimed/third-party].

## Compute & software
Onboard compute n/a (not disclosed). Software: multi-layered "data-driven embodied intelligence" stack — VLM/foundation-model planning (PuduFM 1.0 referenced by dealer/aggregator material) + real-time manipulation control; integrates with Pudu cloud fleet management used across 80k robots; voice interaction in multiple languages [S2][S5, vendor-claimed/third-party]. No open SDK advertised.

## Safety & compliance
No D7-specific certifications published [flag]. Pudu's delivery/cleaning products carry CE marks in the EU; the same channel/compliance machinery is expected to be applied to D7 for export, but manipulation changes the certification basis (Machinery Regulation) [estimated]. Low 45 kg mass is itself a safety advantage (low collision energy) [estimated].

## Deployment evidence & traction
- Commercialization declared for 2025; D7 marketed on Pudu's site and via authorized dealers (e.g. Neil AI Global Solutions) [S2][S5, third-party].
- No named end-customers or unit counts published as of research date [flag]. Contrast: Pudu's channel strength — 80k+ robots, 60+ countries — is the deployment engine awaiting the product [S4, vendor-claimed].
- D9 biped contrast: announced 2024-12-19 (170 cm, 65 kg, 42 DoF, DH11 hands) as technology flagship; D7 is the commercial semi-humanoid track [S6, third-party].

## Assessment (analyst view)
*Analyst opinion.* The D7's engineering story is "light, fast, cheap enough to channel": 45 kg and 2 m/s suit hospitality floors far better than 200 kg industrial rigs, and Pudu's dealer network can put it in front of thousands of existing hotel/restaurant accounts overnight. Weaknesses: no public price, no named deployments 18+ months after announcement, thin disclosed sensor/compute specs, and manipulation claims (±0.1 mm) that look aspirational for a 45 kg cable-light platform. Threat to an EU entrant: high in EU hospitality/facilities once it ships at volume — Pudu already has EU sales, service and CE experience; near-term the window remains open while D7 traction is unproven.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://www.pudurobotics.com/en/news/917 | Announcement 2024-09-19, semi-humanoid positioning, industrial+hospitality targeting | vendor-claimed |
| S2 | https://www.startupselfie.net/2024/09/23/pudu-robotics-d7-semi-humanoid-robot/ | Specs: 165cm/45kg, 30→50 DoF, 65cm arms, 10kg, ±0.1mm, 2 m/s, 10° slope, >1kWh, >8h, 2025 commercialization | third-party (vendor material) |
| S3 | https://www.pudurobotics.com/en/products/d7 | Official product page (JS; confirms current marketing) | vendor-claimed |
| S4 | _work/market_context.md §7 | Pudu 80k+ robots/60+ countries channel | third-party (compiled) |
| S5 | DuckDuckGo-indexed dealer/aggregator pages (Neil AI etc.) | DH11 hand option, PuduFM 1.0, 14kg/2m variant claims, battery swap | third-party |
| S6 | DuckDuckGo-indexed press (D9 search) | D9 biped 2024-12-19 contrast | third-party |
