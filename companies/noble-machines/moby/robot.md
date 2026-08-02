# Moby — Noble Machines

> **SCOPE NOTE: Moby is a bipedal (legged) humanoid, not a wheeled semi-humanoid.** The discovery sweep listed it as "wheeled dual-arm"; primary evidence (vendor site "walking speed 0.8 m/s", worksite photos showing legs with shoes, aparobot "bipedal", stairs/scaffolding navigation) contradicts that. It is documented here for competitive periphery: a rugged, outdoor-capable legged humanoid for construction/industrial material handling, ~$75k (aggregator), with a claimed Fortune Global 500 first deployment.

| Field | Value |
|---|---|
| Company | Noble Machines (ex-Under Control Robotics) |
| HQ | Sunnyvale, CA, USA |
| Status (2026) | prototype / early pilots (claimed G500 deployment; "in development, expected 2026" per aparobot) [S1][S5] |
| First shown / launch | Exited stealth March 2026 (3rd-gen hardware) [S1] |
| Target applications | Material handling, inspection and hazardous-environment work in construction, manufacturing, semiconductor, energy, mining, logistics |
| Price | $75,000 (humanoid.guide, unverified); vendor discloses no price [S2] |
| Availability | Dev "Platform" access + limited RaaS pilots operated by Noble's team [S3] |

## Design & morphology
Bipedal humanoid, ~170 cm; weight reported 45 kg (humanoid.guide) to "45-70 kg depending on configuration" (aparobot) [S2][S5]. 34 DoF total incl. multi-fingered hands (10 finger DoF) [S2][S5]. Composite polymer + aluminum frame; photographed wearing sneakers for outdoor traction ("rugged shoes") [S2][S4].

## Locomotion
Legged walking, 0.8 m/s (vendor) / up to 3 km/h (aggregator); steep inclines, stairs, scaffolding, outdoor unstructured terrain [S1][S3][S5].

## Upper body & manipulation
Two arms with modular end-effectors ("modular hands"); dexterous multi-fingered hands optional [S3][S5]. Payload conflicting: 9 kg (humanoid.guide "strength"), 23 kg/50 lb (vendor homepage), 27 kg/60 lb lift (The Robot Report) — plausibly continuous-carry vs peak-lift figures; treat 23 kg carry / 27 kg lift as vendor-claimed [S1][S2][S3].

## Sensing
Not itemized publicly; cameras implied for VLM-driven autonomy; n/a (not disclosed).

## Actuation & power
Brushless motors with harmonic or planetary gears [S2]. Battery ~5 h runtime; capacity n/a [S2][S3].

## Compute & software
NVIDIA Jetson Orin edge AI compute [S5]. Linux/Ubuntu + ROS; LLM integration; whole-body AI control; multi-modal task learning via natural language, physical demonstration and gestures; teleoperation mode; Bluetooth/Wi-Fi [S2][S5]. Partners: NVIDIA, ADLINK, Solomon (vision), Schaeffler, SHMZ [S3].

## Safety & compliance
"Safe with humans" claimed; IP20; no certifications cited [S2].

## Deployment evidence & traction
- First deployment at an unnamed Fortune Global 500 industrial customer within 18 months of founding (vendor-claimed, echoed by TRR) [S1][S3].
- Worksite photos show hardware handling lumber outdoors at night — real hardware, uncontrolled environment [S4, third-party image].
- No unit counts, no named customers, no independent verification.

## Assessment (analyst view)
*Analyst opinion.* Strengths: fast-iterating credible team, payload-first positioning for rugged/outdoor industrial niches most wheeled semi-humanoids avoid, and early G500 pilot claim. Weaknesses: legged platform means higher cost/complexity/safety burden, conflicting specs, tiny funding vs legged competitors (Figure, Agility), and unverified traction. For an EU wheeled semi-humanoid entrant the direct overlap is small — Moby targets terrain wheeled robots can't reach; the relevant lesson is its payload-led sales pitch, which is exactly the axis where industrial customers judge wheeled platforms too.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.therobotreport.com/noble-machines-exits-stealth-with-moby-humanoid/ | Stealth exit, 27kg, G500 claim, rebrand | third-party |
| 2 | https://humanoid.guide/product/moby/ | 170cm/45kg/34DoF/9kg/3km/h/5h/$75k/brushless+harmonic/Linux-ROS | third-party (aggregator, unverified) |
| 3 | https://www.noblemachines.ai/ | 23kg payload, 5h battery, 0.8 m/s walking, partners, platform/RaaS models | vendor-claimed |
| 4 | https://www.therobotreport.com/wp-content/uploads/2026/03/noble-machines-featured.jpg | Bipedal form factor with shoes, outdoor worksite | third-party (photo) |
| 5 | https://www.aparobot.com/robots/moby | Bipedal, 45-70kg configs, Jetson Orin, stairs/scaffolding, expected 2026 | third-party (aggregator) |
