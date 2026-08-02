# DAL-e (달이) — Hyundai Motor Group

> Compact wheeled customer-service semi-humanoid piloted in a Seoul Hyundai showroom from January 2021: 1,160 mm / 80 kg, four omnidirectional wheels, a chest touchscreen, face/mask recognition and two short gesturing arms (expressive only — no object manipulation). Competitively it is a cautionary datapoint: Hyundai's Robotics Lab subsequently dropped the humanoid arms and pivoted the DAL-e name to an armless delivery robot, signaling that gesture-only arms did not justify their cost in service roles.

| Field | Value |
|---|---|
| Company | Hyundai Motor Group (Robotics Lab) |
| HQ | Seoul, South Korea |
| Status (2026) | discontinued (as humanoid form; name continued by armless DAL-e Delivery line) |
| First shown / launch | Pilot began 2021-01-25, Hyundai showroom, southern Seoul [S1] |
| Target applications | Showroom/customer service: greeting, product info, escorting, photo engagement |
| Price | n/a (internal pilot, never sold) |
| Availability | Never commercially available |

## Design & morphology
"Truncated humanoid" (Hyundai's phrase): head with eye display + torso with integrated touchscreen on a wheeled skirt base. **1,160 × 600 × 600 mm, 80 kg** [S1] (vendor-claimed). Two short arms for gestured feedback; no hands for grasping. DoF counts n/a (not disclosed).

## Locomotion
**Four omnidirectional wheels** for free movement in showroom aisles [S1]. Speed n/a (not disclosed); indoor flat floors only.

## Upper body & manipulation
Arms provide **gesture feedback only** (waving, pointing, photo poses) — no payload, no grippers, no manipulation [S1][S2]. This is the design decision later reversed entirely (arms deleted) in DAL-e Delivery [S3].

## Sensing
Cameras for **facial recognition** and mask detection (advised unmasked customers to wear masks — COVID-era feature); microphones/speaker for automated dialogue; touchscreen input [S1]. Base sensor suite n/a.

## Actuation & power
n/a (not disclosed).

## Compute & software
Language-comprehension and automated-dialogue stack; face recognition; **wireless connection to showroom display screens** (robot pushes content to signage); responds to verbal and touchscreen commands [S1]. No SDK/third-party platform.

## Safety & compliance
n/a (not disclosed); low-speed indoor pilot.

## Deployment evidence & traction
- Pilot at one Hyundai Motor showroom in southern Seoul from 2021-01-25; Hyundai stated plans to expand to other Hyundai/Kia showrooms based on pilot data [S1] (vendor-claimed). No evidence of broad rollout found; the program's public follow-ups concern the armless **DAL-e Delivery** instead: introduced Dec 2022, redesigned April 2024 on four PnD wheel modules (10 kg / 16 coffees, 1.2 m/s, KISA-certified 99.9% face ID, elevator/door integration), deployed at Factorial Seongsu smart building Q2 2024 [S3][S4] (vendor-claimed/third-party).

## Assessment (analyst view)
*Analyst opinion.* DAL-e's strength was corporate: automotive-grade engineering, a captive deployment network (dealerships) and HMG's budget. Its weakness was the value proposition — gesture-only arms on a kiosk robot added anthropomorphic charm but no task capability, and Hyundai's own pivot to an armless delivery form is strong evidence that non-manipulating semi-humanoids fail ROI tests. Threat to a new EU entrant: negligible directly (discontinued form factor); indirect relevance is that HMG channels its humanoid ambition through legged Boston Dynamics Atlas, and could re-enter the wheeled dual-arm space quickly if it chose. EU entrants should cite this case when arguing that semi-humanoids must manipulate, not merely gesture.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-group-introduces-advanced-humanoid-robot-%E2%80%98dal-e%E2%80%99-for-automated-customer-services-0000000560 | Dimensions/weight, 4 omni wheels, gesture arms, face/mask recognition, pilot date/location, expansion plans | vendor-claimed |
| S2 | https://newatlas.com/robotics/hyundai-dal-e-customer-service-robot/ | Independent pilot coverage | third-party |
| S3 | https://www.hyundaimotorgroup.com/en/news/CONT0000000000144931 | DAL-e Delivery armless successor: PnD modules, 10 kg, 1.2 m/s, face-ID, Factorial Seongsu | vendor-claimed |
| S4 | https://newatlas.com/robotics/hyundai-kia-dal-e-delivery-robot/ | DAL-e Delivery capabilities (elevators), deployment | third-party |
