# MH3 — Mirsee Robotics

> Premium industrial wheeled humanoid from Cambridge, Ontario (Canada):
> 180 cm dual-arm torso with 5-finger dexterous hands on a black column over a
> large white AMR base (verified from render). Pitched at hazardous industrial
> work — manufacturing, healthcare, defense, critical infrastructure — with
> immersive-VR haptic teleoperation. Competitively notable for aggressive paper
> specs (30 kg/arm, 10 h runtime, IP54) at USD 200k, but with a thin public
> footprint and no deployment evidence.

| Field | Value |
|---|---|
| Company | Mirsee Robotics, Cambridge, Ontario, Canada |
| HQ | Cambridge, Ontario, Canada |
| Status (2026) | announced / late prototype — guide says "in production", press says production launches planned 2027 [S1][S2] |
| First shown / launch | 2025 (guide listing June 2025); third-generation design [S1][S2] |
| Target applications | hazardous/physically demanding industrial tasks: manufacturing, healthcare, defense, critical-infrastructure maintenance [S1][S2] |
| Price | USD 200,000 [S1] |
| Availability | not yet commercially deployed; 2027 production target [S2] |

## Design & morphology
180 cm; weight reported as 125 kg (guide) vs 75 kg (press) — conflicting,
treat as unresolved [S1][S2]. Dual-arm humanoid torso with sensor head on a
black column over a large skirted AMR base with wraparound bumpers (image).
31 DoF overall incl. 6 DoF per hand; aluminum 6061 structure; IP54 [S1][S4].

## Locomotion
Wheeled base (configuration undisclosed; low emergency-stop-equipped AMR
chassis), chosen explicitly over legs for battery life and tip-over stability;
max 5 km/h (1.4 m/s) [S1][S2].

## Upper body & manipulation
Two arms, 30 kg strength per arm (27 kg combined force also cited — figures
inconsistent); 5-finger dexterous hands with 6 DoF each; "human-like dexterity"
claimed [S1][S2]. Reach/repeatability n/a.

## Sensing
12 MP head camera; sub-100 ms visual-input-to-action latency claimed; base
sensor bar visible in render (depth/lidar type undisclosed) [S1][S4].

## Actuation & power
BLDC motors with harmonic and planetary gears; up to 10 h runtime per charge —
best-in-class claim if real; battery capacity n/a [S1].

## Compute & software
NVIDIA-based compute; ROS 2; WiFi, cellular and satellite connectivity
(satellite implying remote-infrastructure use cases); immersive VR
teleoperation with haptic feedback; autonomy level undisclosed [S1][S2].

## Safety & compliance
"Certified for human interaction" per guide — certification body/standard NOT
specified; IP54 [S1]. No ISO 10218/TS 15066/13482 references found; claim
should be treated as unverified marketing.

## Deployment evidence & traction
None found: no named customers, pilots or unit counts. "In production" status
(guide) conflicts with 2027 production timeline (press). Listing "Not
verified" [S1][S2].

## Assessment (analyst view)
*Analyst opinion.* On paper MH3 is one of the strongest wheeled industrial
humanoids in this batch: 30 kg/arm, 6-DoF hands, 10 h runtime, IP54, ROS 2 and
satellite-linked teleop for hazardous sites — a coherent hazardous-work thesis.
But the evidence base is weak (no team, funding, or customer footprint;
contradictory weight and status data), suggesting a company earlier-stage than
its marketing. Threat to an EU entrant: potentially moderate in
infrastructure/defense teleoperation niches by 2027-28; monitor for funding
news and first pilots before treating specs as real.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/mh3/ | full specs, $200k, Canada, status | third-party |
| 2 | https://html.duckduckgo.com/html/?q=Mirsee+Robotics+MH3+humanoid | Cambridge Ontario, wheeled rationale, 75 kg figure, VR teleop, 2027 timeline | third-party |
| 3 | http://www.mirsee.com | vendor site | vendor-claimed |
| 4 | image: humanoid.guide featured image (see images.md) | morphology: dual-arm torso, dexterous hands, column on AMR base (visual) | third-party |

*Specs carry confidence per source column; unknown fields marked n/a.*
