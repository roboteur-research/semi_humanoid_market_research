# I-Series — Simplexity Robotics (至简动力)

> Prototype humanoid platform from Hangzhou unicorn Simplexity Robotics
> (至简动力), founded July 2025 by ex-Li Auto autonomous-driving executives.
> The listed variant is wheeled: dual-arm torso with 5-finger dexterous hands on
> a mecanum-wheel base with lidar. Positioned as a general platform ("perception,
> reasoning, action") for both service (malls, museums, homes) and industrial
> (factory/warehouse handling, sorting) use. Matters because of its funding
> velocity (~$289M in 6 months, Tencent/Alibaba/HongShan) and AD-derived
> World-Model+VLA stack, not current hardware maturity.

| Field | Value |
|---|---|
| Company | Simplexity Robotics (至简动力), Hangzhou, China |
| HQ | Hangzhou, China |
| Status (2026) | prototype (guide; "Not Verified" listing) [S1] |
| First shown / launch | 2026 (guide listing March 2026) [S1] |
| Target applications | AI research, industrial automation, logistics, retail; service (guiding, restocking) and industrial (handling, sorting) variants [S1][S2] |
| Price | USD 78,000 (guide) [S1] |
| Availability | not commercially available; prototype, China [S1][S2] |

## Design & morphology
175 cm, 60 kg. Humanoid torso with sensor-head, articulated waist/pelvis linkage
mounted on a boxy mecanum-wheeled base (image shows blue mecanum rollers and a
base lidar puck). 20 DoF overall + 10 hand DoF; aluminum + composite structure
[S1][S4]. A bipedal variant may exist in the I-Series family; the listing covers
the wheeled configuration [S2].

## Locomotion
Omnidirectional mecanum-wheel base; max 3 km/h (0.83 m/s) [S1][S4].

## Upper body & manipulation
Two arms with 5-finger dexterous hands (10 hand DoF total per guide — likely
underactuated); payload 5 kg total; torque-controlled electric actuators.
"Full-body interaction", "stability and coordination over speed" per vendor
description [S1]. Reach/repeatability n/a.

## Sensing
Head camera behind black visor plus chest camera; base lidar puck and
front/side sensor apertures on base (image) [S4]. Camera resolution and depth
sensing not disclosed [S1].

## Actuation & power
Electric actuators with torque control; harmonic/reduction gears [S1]. Battery
capacity n/a; runtime ~2 h per charge [S1].

## Compute & software
AI compute platform (GPU + edge accelerators, guide inference); LLM integration:
yes; Ethernet + WiFi [S1]. Core differentiator: World Model paired with VLA for
autonomous execution across service and industrial domains — architecture
carried over from founders' Li Auto autonomous-driving work [S2][S3].

## Safety & compliance
n/a (not disclosed). No standards or certifications claimed [S1].

## Deployment evidence & traction
None found — prototype, no customers, pilots or unit counts. Traction is purely
financial: ~$289M raised across 5 rounds in ~6 months, unicorn valuation,
investors incl. Tencent, Alibaba, HongShan, Legend Capital, CAS Star [S3].

## Assessment (analyst view)
*Analyst opinion.* Strengths: elite autonomous-driving founding team, tier-1
Chinese capital at unprecedented velocity, dual-market wheeled platform with a
world-model software thesis. Weaknesses: hardware is unremarkable (5 kg payload,
2 h runtime, 20 DoF) and unproven; no deployments; company is under a year old.
Threat to a new EU entrant: low today, potentially high within 2-3 years if the
software thesis converts funding into deployed fleets — this is one of the
Chinese entrants most worth monitoring quarterly.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/simplexity-robotics-i-series/ | full specs, $78k, prototype, China | third-party |
| 2 | https://html.duckduckgo.com/html/?q=Simplexity+Robotics+%22I-Series%22+humanoid+robot | wheeled design, World Model + VLA, service/industrial split | third-party |
| 3 | https://html.duckduckgo.com/html/?q=%22Simplexity+Robotics%22+Hangzhou+humanoid+funding | founding, CEO Jia Peng, funding/unicorn, investors | third-party |
| 4 | image: humanoid.guide featured image (see images.md) | mecanum base, base lidar, dexterous hands (visual) | third-party |

*Specs carry confidence per source column; unknown fields marked n/a.*
