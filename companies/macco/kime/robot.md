# Kime — Macco Robotics

> Kime is a fixed-kiosk beverage-serving humanoid from Seville: a head-torso-dual-arm robot sealed in a ~2 m² service booth that pulls beer taps, mixes drinks and serves customers through a hatch, at rates up to ~300 drinks/hour. Trialed by Portuguese fuel retailer Prio and used in Seville bars during the pandemic, it is a niche but shipping example of humanoid form applied to automated vending — competitively marginal for manipulation players, but instructive for hospitality-segment economics.

| Field | Value |
|---|---|
| Company | Macco Robotics |
| HQ | Seville, Spain |
| Status (2026) | shipping (niche, project-based; company active but low-profile) |
| First shown / launch | ~2019 (kiosk); pandemic bar deployments 2020-21; iterated to v5 |
| Target applications | Beer/coffee/cocktail service in bars, festivals, stadiums, malls, gas-station convenience retail |
| Price | n/a (not disclosed; sale/lease per project) |
| Availability | Spain/Portugal projects; direct from vendor |

## Design & morphology
Humanoid upper body (head with expressive face screen, torso, two articulated arms) mounted **inside a fixed kiosk/pedestal enclosure** of ~2 m² footprint; ~2 m tall unit [S1][S3]. 22 DoF total (v5) [S4]. Variant: rolling-cart Kime for events/festivals (pushed, not self-driving) [S1].

## Locomotion
None — fixed kiosk pedestal (cart variant is manually moved). Excluded from mobility comparisons.

## Upper body & manipulation
Two articulated arms optimized for structured dispensing: pulling tap handles, angling glasses for correct pour, grabbing bottles/cups, mixing cocktails [S1][S4]. Claimed rates: beer in ~6-23 s (version-dependent; v5 claims <8 s), cocktails ~30 s, up to 300 drinks/hour [S1][S4]. Payload: glass/bottle-class (~1 kg, estimated). Works only with fixtures inside its kiosk.

## Sensing
3D lidar, RGB-D camera, proximity and safety sensors, facial-recognition cameras for customer interaction (v5 spec) [S4].

## Actuation & power
Electric arms (details n/a); mains-powered kiosk.

## Compute & software
NVIDIA Jetson Xavier NX for real-time AI (v5); app/kiosk ordering integration, face recognition for personalization [S4]. Proprietary stack, no SDK.

## Safety & compliance
Physical separation is the safety concept: the robot works behind the kiosk enclosure and serves through a hatch — no shared workspace with humans. No robot-safety certifications published; food-contact/hygiene compliance n/a (not disclosed).

## Deployment evidence & traction
- Seville bars: contact-free beer pouring/delivery during COVID (Euronews video coverage, Feb 2021) [S2].
- **Prio (Portugal)**: gas-station kiosk trial; next phase planned to rotate the kiosk between stations and expand menu to fountain drinks, milkshakes, fresh food [S1].
- Spanish beer brand event/festival cart deployments [S1].
- No published unit counts (est. single digits); no large rollout announced through 2026 [S5].

## Assessment (analyst view)
*Analyst opinion.* Strengths: real (if small) commercial deployments, high-throughput structured-task design, and a safety-by-enclosure approach that avoids certification burden entirely. Weaknesses: the humanoid form is marketing rather than function — a dispensing machine with arms — and the company has no visible capital to scale; Chinese beverage-robot vendors undercut this niche aggressively. Threat to a new EU entrant: negligible for general-purpose semi-humanoids; relevant only as evidence that hospitality buyers pay for spectacle, and that enclosed-workspace designs can ship without safety-standard friction.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://thespoon.tech/macco-robotics-beer-pouring-kime-bot-has-big-kitchen-plans/ | Kiosk design, pour mechanics, Prio trial, cart variant | third-party |
| 2 | https://www.euronews.com/2021/02/24/robots-used-to-pour-and-deliver-beers-in-seville-bars-during-pandemic | Seville bar use | third-party |
| 3 | https://www.aparobot.com/robots/kime | 2 m form factor, overview | third-party (aggregator) |
| 4 | https://www.originofbots.com/robot/kime-v5-by-macco-robotics-spain-details-specifications-rating | v5: 22 DoF, Jetson Xavier NX, sensors, 300 drinks/h, <8 s beer | third-party (aggregator) |
| 5 | https://humanoidindex.org/companies/macco-robotics | Active 2026, hospitality deployments Europe | third-party |
