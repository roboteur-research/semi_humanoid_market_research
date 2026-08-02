# pib.Pro — isento robotics (pib.rocks), Germany

> Commercial "pro" version of the open-source 3D-printable pib humanoid from
> Nuremberg's isento GmbH: a full-body humanoid form standing on a two-wheeled
> self-balancing mobile base (renders show a hoverboard-style platform), sold
> "ready-to-ship" at ~$6k for work, learning and care pilots. It matters
> competitively as the German open-source / GDPR-sovereignty entry — mindshare
> and ecosystem play, not an industrial-capability play.

| Field | Value |
|---|---|
| Company | isento GmbH / isento robotics, pib.rocks project |
| HQ | Nuremberg, Germany |
| Status (2026) | announced / early production — "in production, ready-to-ship" per guide [S1], vendor recruiting pilot customers [S3]; listing "Not Verified" |
| First shown / launch | 2025 (renders Sep 2025 on pib.rocks; humanoid.guide listing Feb 2026) [S1][S3] |
| Target applications | education, research, manufacturing support, healthcare/rehab assistance, custom automation [S1][S3] |
| Price | USD 5,999 [S1] |
| Availability | ready-to-ship (guide); pilot-customer program via pib.rocks [S1][S3] |

## Design & morphology
Full humanoid form (head with face display, torso, two arms with 5-finger hands,
legs) mounted on/standing atop a two-wheeled self-balancing base in official
renders [S4]. Structure: 3D-printed polymers (PLA/ABS lineage from the DIY pib).
humanoid.guide lists height 80 cm and 20 DoF overall — the 80 cm figure matches
the desktop DIY pib rather than the full-body Pro render; treat height as
uncertain [S1]. Weight n/a (not disclosed).

## Locomotion
Two-wheeled self-balancing (hoverboard-style) mobile base per renders [S4]; max
speed 2.5 km/h (0.7 m/s) [S1]. No terrain/climbing data.

## Upper body & manipulation
Two arms with 5-finger 3D-printed hands (visible tendon/linkage fingers in
renders). Payload claim 4 kg ("improved precision and payload vs earlier pib
models") [S1][S3]. Manipulation score 2/8 on humanoid.guide. No reach,
repeatability, or per-arm DoF disclosed.

## Sensing
"State-of-the-art 3D vision, LiDAR" claimed for the Pro [S3]; RGB camera in head
(~720p+, guide inference); mics/speakers for interaction [S1].

## Actuation & power
Servomotors with hobby-servo/belt gearing lineage [S1]; "precise motors, stronger
hardware" claimed for Pro without specifics [S3]. Battery capacity n/a; runtime
~2 h per charge [S1].

## Compute & software
Onboard compute of Raspberry Pi class / modular (guide inference); Linux + ROS 2;
open-source stack with community-developed ROS modules for navigation,
manipulation, interaction; Bluetooth + WiFi; "powerful onboard AI" claimed, LLM
integration unconfirmed [S1][S3]. Fully open documentation, no vendor lock-in —
the strongest differentiator [S1][S3].

## Safety & compliance
"Safe with humans" (guide attribute); DSGVO/GDPR-compliant data handling is a
core marketing claim [S3]. No ISO 13482 / TS 15066 / CE certification claims
found. IP rating n/a.

## Deployment evidence & traction
DIY pib is deployed in German schools via the pib.Education sponsorship program;
German Design Award 2025 [S2]. For pib.Pro itself: pilot-customer recruitment
ongoing, no named customers or unit counts found [S3].

## Assessment (analyst view)
*Analyst opinion.* pib.Pro's strengths are price (~$6k), full open-source stack,
German origin, GDPR/sovereignty narrative, and an education pipeline that builds
local talent and goodwill. Weaknesses: hobby-grade actuation, 3D-printed
structure, ~2 h runtime, 4 kg payload claim unlikely to survive industrial
scrutiny, and specs that conflate the desktop pib with the Pro. Threat to a new
EU entrant: low in industrial segments, but non-trivial in German education/
research procurement and in shaping the "open European humanoid" narrative a
commercial entrant might want to own.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/pib-pro/ | specs table, $5,999, status, materials, scores | third-party |
| 2 | https://pib.rocks/ | project background, education program, Design Award, isento GmbH | vendor-claimed |
| 3 | https://pib.rocks/de/pib-pro/ | Pro positioning: 3D vision, lidar, onboard AI, DSGVO, pilots, applications | vendor-claimed |
| 4 | https://pib.rocks/wp-content/uploads/2025/09/pibPro-mitBeinen.png | official render: full-body humanoid on two-wheel self-balancing base | vendor-claimed |

*Specs carry confidence per source column; unknown fields marked n/a.*
