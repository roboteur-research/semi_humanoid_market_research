# ALLEX — WIRobotics

> Korean dual-arm upper-body humanoid from wearable-robot maker WIRobotics, notable
> for ultra-low-friction backdrivable actuators, 15-DoF human-sized compliant hands
> and "sensorless" force detection down to ~100 gf. Currently a pedestal/upper-body
> platform; wheeled mobile configurations and full biped locomotion are stated as
> under development. Competes as a safe-manipulation platform for service/logistics.

| Field | Value |
|---|---|
| Company | WIRobotics (위로보틱스) |
| HQ | South Korea |
| Status (2026) | prototype |
| First shown / launch | 2025 [S2] |
| Target applications | commercial cleaning, home services, logistics; household/elder-care and manufacturing cited [S1][S2] |
| Price | USD 180,000 (third-party) [S1] |
| Availability | not generally available; partner/R&D stage |

## Design & morphology
Upper-body humanoid: torso with head, two arms with 15-DoF human-hand-sized hands
(10 fingers total), shown on a pedestal column [image]. ~170 cm / ~60 kg reported
for the full configuration (third-party search results, unverified) [S3]. Whole
shoulder-down arm assembly ~5 kg incl. hand (~9 kg total arm weight per vendor
page); hand ~0.7 kg each [S1][S2].

## Locomotion
None in current form (pedestal). humanoid.guide notes full biped locomotion under
development; the guide's wheeled-platform listing implies a wheeled mobile-base
configuration [S1]. Confidence: third-party/estimated.

## Upper body & manipulation
Hands: 15 DoF, fingertip force up to 40 N, hook-grip strength >30 kg, load
capacity ≥3 kg per hand, fingertip repeatability ≤0.3 mm (vendor page says
≤0.5 mm) [S1][S2]. Arms use custom actuators with ~1/10 friction and ~1/24 inertia
vs commercial actuators; gravity-compensated, integrated position/force/stiffness
control [S2].

## Sensing
Sensorless force detection (~100 gf resolution) via backdrivable actuation instead
of dedicated force/torque sensors; whole-body force and interaction control [S2].
Head cameras visible in imagery; details n/a.

## Actuation & power
Proprietary ultra-low-friction, low-inertia actuators; unified motor control;
20 kHz real-time control loop over EtherCAT [S2]. Battery/runtime n/a.

## Compute & software
n/a (not disclosed). Physical-AI collaboration with RLWRLD for foundation-model
training on the platform [S1].

## Safety & compliance
Whole-body compliance for safe human interaction is the core design claim [S1][S2].
No certifications claimed.

## Deployment evidence & traction
No customers or deployments disclosed; RLWRLD partnership is the main traction
signal (third-party) [S1].

## Assessment (analyst view)
*Analyst opinion.* Strengths: genuinely differentiated compliant actuation and
best-in-class hand specs on paper (40 N fingertip, ≤0.3 mm repeatability), backed
by a company already shipping wearable robots. Weaknesses: no mobile base shipping
yet, no disclosed compute/software stack, prototype stage. Threat to an EU entrant:
moderate — if mounted on a wheeled base it becomes a strong safe-manipulation
competitor, but commercialization is early.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/allex/ | price, status, hand specs, base type, applications, RLWRLD | third-party |
| 2 | https://rih.wirobotics.com/en/allex | actuator, hand, control specs | vendor-claimed |
| 3 | DuckDuckGo search results (WIRobotics ALLEX specs) | height ~170 cm, weight ~60 kg, launch 2025 | third-party |
