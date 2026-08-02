# ALPHA (Automated Litter Processing Humanoid Assistant) — TeknTrash

> Waste-sorting semi-humanoid from UK waste-analytics firm TeknTrash: dual-arm
> torso with depth-camera head on a ~2 m lift column over an AMR base with
> orange collection bin. Form factor verified from official render — it IS an
> anthropomorphic dual-arm wheeled system (no annex flag needed). Aimed at
> recycling facilities to replace hazardous, fatiguing manual sorting.
> Competitive significance: an early vertical-specific European application of
> the wheeled dual-arm form at a ~$55k price.

| Field | Value |
|---|---|
| Company | TeknTrash, UK |
| HQ | United Kingdom |
| Status (2026) | prototype; pilot deployments with waste operators claimed [S1][S2] |
| First shown / launch | 2025 (guide listing July 2025) [S1] |
| Target applications | recycling facilities, waste processing: sorting/picking contaminated streams, hazardous-material handling [S1][S2] |
| Price | USD 55,000 [S1] |
| Availability | not commercially available; pilots; UK [S1][S2] |

## Design & morphology
200 cm tall (at column extension), 90 kg. Dual-arm humanoid torso with
depth-camera "head" mounted on a tall lift column rising from a low AMR base
with integrated orange bin (image). 13 DoF total (incl. 2 gripper DoF);
aluminum + plastic construction; IP32 [S1][S4].

## Locomotion
Wheeled AMR base, autonomous navigation with obstacle avoidance; max speed
0.9 km/h (0.25 m/s) — facility-floor creep speed [S1].

## Upper body & manipulation
Two 6-DoF arms (Realman motor/arm technology — i.e. Chinese cobot-arm supply)
with parallel grippers (finger-rake style end-effectors in render); 5 kg lift
capacity; up-to-2 m reach via the adjustable lift column [S1][S2].
3D vision-guided deep-learning picking; no force sensing disclosed.

## Sensing
Head: stereo/depth camera bar (RealSense-class; 640×480 depth per guide);
hyperspectral vision claimed for material identification; base: LiDAR,
ultrasonic, IMU [S1][S2].

## Actuation & power
Realman servo joints [S1]; battery capacity n/a; ~7 h runtime, ~3 h charge
[S1][S2].

## Compute & software
NVIDIA Orin AGX 64 GB (275 TOPS), Ubuntu 24, WiFi; cloud fleet coordination;
deep-learning object recognition; claimed 20 ms glass-to-action latency
(implausibly low for full perception-action loops; treat as marketing) [S1][S2].

## Safety & compliance
IP32; no safety standards (ISO 10218/TS 15066/13482) or CE claims found —
notable given intended operation alongside sorting staff [S1].

## Deployment evidence & traction
"Pilot deployments underway, including partnerships with waste management
operators" — vendor/third-party claim, no named facilities or unit counts
found [S2]. humanoid.guide lists as "Not verified".

## Assessment (analyst view)
*Analyst opinion.* Sensible niche: waste sorting is dirty, dangerous,
labor-short work with quantifiable pick-rate economics — a classic first
market for wheeled manipulators. TeknTrash's analytics heritage gives it
domain data, but the hardware is integrated commodity kit (Realman arms, Orin,
lift column) at prototype maturity, 0.25 m/s and 5 kg — far from the 30-40
picks/min of human sorters it cites. Threat to an EU entrant: low as a
platform competitor; moderately interesting as a niche rival or channel partner
in EU recycling automation.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/alpha/ | full specs, $55k, prototype, UK | third-party |
| 2 | https://html.duckduckgo.com/html/?q=TeknTrash+ALPHA+robot+waste | ALPHA acronym, reach, sensors, pilots, pick-rate rationale | third-party |
| 3 | https://www.tekntrash.com/ | company background | vendor-claimed |
| 4 | image: humanoid.guide featured image (see images.md) | morphology verification: dual-arm torso on lift column over AMR base | third-party |

*Specs carry confidence per source column; unknown fields marked n/a.*
