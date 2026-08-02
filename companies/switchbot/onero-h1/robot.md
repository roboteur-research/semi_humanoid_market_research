# Onero H1 — SwitchBot (OneRobotics)

> The Onero H1 is SwitchBot's consumer semi-humanoid: a ~1.3 m, ~40 kg upper-body humanoid (two arms with dexterous 5-finger hands, expressive head) on a cylindrical wheeled base, unveiled at CES 2026. It runs an on-device "OmniSense" VLA model and doubles as the command hub of SwitchBot's smart-home ecosystem. Officially listed at USD 9,999 (pre-production, "coming soon"), against CES press chatter of a $1,000–1,500 target, it is the strongest signal yet that wheeled humanoids are headed for consumer retail channels — from a company that already ships smart-home hardware to 100+ markets.

| Field | Value |
|---|---|
| Company | SwitchBot (OneRobotics, ex-Wonderlabs) |
| HQ | Shenzhen, China |
| Status (2026) | announced (pre-production; retail promised later 2026) |
| First shown / launch | CES 2026, Las Vegas (January 2026) |
| Target applications | Household chores (laundry folding, dishwashing, window wiping, tidying, object fetch), smart-home orchestration, companionship/monitoring |
| Price | USD 9,999 on official store ("coming soon") [S1]; CES press cited $1,000–1,500 target — unreconciled, see Assessment [S2] |
| Availability | Global D2C store waitlist ("notify me"); retail launch stated for later 2026; 30-day return, 1-year warranty per store boilerplate [S1] |

## Design & morphology
Upper-body humanoid torso on a cylindrical wheeled base (vacuum-robot-like puck at floor level); overall height ~1.3 m, weight ~40 kg [S2][S3]. 22 DoF across arms and hands [S2]. Expressive head with animated eyes and (in renders) a soft cap; central column torso with speaker grille and abdomen camera [S1]. Total-body DoF beyond arms/hands: n/a (not disclosed).

## Locomotion
Wheeled base (drive configuration not disclosed; circular footprint suggests diff-drive with casters, estimated). Speed, climbing limits: n/a (not disclosed).

## Upper body & manipulation
- Two articulated arms with 5-finger dexterous hands; 22 DoF combined arms+hands [S2][S3].
- Demonstrated at CES: laundry folding (signature demo), dishwashing, window wiping, object handovers [S2].
- Payload, reach, repeatability: n/a (not disclosed).

## Sensing
Multiple Intel RealSense depth cameras distributed across head, arms/hands, and abdomen (third-party CES reporting) [S3]. Additional base sensors (mapping/navigation heritage from SwitchBot vacuums, estimated). Microphones/speakers for voice interaction [S1].

## Actuation & power
Actuators: n/a (not disclosed). Battery capacity/runtime: n/a (not disclosed); CES coverage flagged battery life as an open question [S2].

## Compute & software
- On-device "OmniSense" VLA model — local processing pitched for privacy and latency; continuous learning claims ("thinks in real time, continuously optimizing movements") [S2][S3].
- Deep SwitchBot ecosystem integration: acts as mobile hub/controller for SwitchBot devices (locks, curtains, vacuums, sensors); ecosystem supports Matter and Home Assistant [S1][S2].
- SDK/API: n/a (not disclosed).

## Safety & compliance
n/a (not disclosed). Consumer positioning implies eventual CE/FCC/UL-type consumer certifications; nothing published. Confidence: estimated.

## Deployment evidence & traction
- CES 2026 live demos (laundry folding etc.); Engadget called it "one of the most intriguing robot helpers" of the show [S2] (third-party).
- Status "lab"/pre-production; no customer deployments, no unit counts [S3].
- Official store listing live with waitlist — evidence of genuine commercialization intent, not just concept [S1].

## Assessment (analyst view)
*Analyst opinion.* The H1's threat is channel + price, not robotics superiority: SwitchBot brings global consumer distribution, brand trust, manufacturing scale, and an installed device base no humanoid startup has. The price ambiguity matters: at the officially listed $9,999 it is already the cheapest credible consumer semi-humanoid from a shipping-at-scale company; the $1,000–1,500 figures circulating from CES look like long-term aspiration or confusion with a stripped SKU and should not be planning-based — but even a $5–10k street price would make it a category disruptor and set consumer reference pricing that bleeds into light-commercial procurement. Weaknesses: unproven manipulation reliability outside curated demos, undisclosed battery/payload specs, and SwitchBot's consumer-gadget QA model may not transfer to a 40 kg manipulator around children. For an EU entrant: minimal overlap in industrial accounts, but high risk of public price-anchoring ("why does yours cost €150k when SwitchBot's is $10k?").

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://switch-bot.com/products/onero-h1 | Official listing, $9,999, coming soon, ecosystem, product image | vendor-claimed |
| 2 | lite.duckduckgo.com aggregate (CES 2026 coverage; Engadget/Verge summaries) | CES debut, demos, 1.3m, on-device AI, $1,000-1,500 press range, 2026 retail | third-party |
| 3 | lite.duckduckgo.com aggregate (spec summaries) | ~40kg, 22 DoF arms/hands, RealSense cameras, OmniSense VLA, lab status | third-party |

*Unknown fields = n/a (not disclosed).*
