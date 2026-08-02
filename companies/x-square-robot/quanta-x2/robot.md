# Quanta X2 — X Square Robot (自变量机器人)

> Wheeled dual-arm humanoid built as the embodiment for X Square's WALL-A 10B+-parameter embodied foundation model. Notable for very high hand dexterity (62 DoF total, 20 in the hands) at a mid-range price (~USD 80k); aimed at home/hotel "butler" service, commercial cleaning, logistics and research. Competitive significance comes from the AI stack and blockbuster funding (Meituan, Alibaba Cloud, ByteDance, Sequoia China, SAIC) more than the hardware.

| Field | Value |
|---|---|
| Company | X Square Robot (自变量机器人) |
| HQ | Shenzhen, China |
| Status (2026) | prototype (third-party assessment) |
| First shown / launch | 2025 (exact date n/a) |
| Target applications | Home service / robot butler, hotels, commercial cleaning, logistics, research & education |
| Price | ~USD 80,000 (third-party listing) [S1] |
| Availability | China; availability/lead time n/a (not disclosed) |

## Design & morphology
Humanoid torso with articulated waist on a low sculpted wheeled chassis with concealed wheels (verified image shows a boot-like base with small wheels at the corners). Height 172 cm, weight ~95 kg, 62 DoF overall of which 20 are in the two hands [S1, third-party]. Torso lift n/a; the leaning waist visible in imagery suggests at least 1–2 waist DoF (estimated).

## Locomotion
Wheeled base, drive topology not disclosed (multi-wheel, likely omni/steerable given corner wheel pods — estimated from image). Max speed ~1 m/s [S1]. Terrain/climbing limits and brakes n/a (not disclosed).

## Upper body & manipulation
Two arms, per-arm DoF n/a (not disclosed; visually ~7). Payload 6 kg per arm; reach ~750 mm [S1]. End-effectors are five-finger dexterous hands, 20 DoF combined, with sub-millimeter repeatability claimed for fine grasping [S1, vendor-claimed via listing]. Tool changer / media at flange n/a (not disclosed).

## Sensing
Head with cameras and an expressive display face (blue "eye" screen in verified image) [S1, estimated]. Base: LiDAR, IMU, ultrasonic sensors [S1]. Wrist/hand tactile or force-torque sensing n/a (not disclosed).

## Actuation & power
Actuator types n/a (not disclosed). Battery capacity n/a; runtime ~2 h per charge [S1]. Hot-swap/charging dock n/a (not disclosed).

## Compute & software
Onboard compute n/a (not disclosed). Software: WALL-A / Wall-X family of end-to-end embodied foundation models (10B+ parameters), a unified perception-planning-control policy enabling autonomous long-horizon task execution; the company open-sourced a Wall-OSS variant to seed an ecosystem (third-party reporting) [S1][S2]. SDK/API details n/a. Fleet management n/a.

## Safety & compliance
n/a (not disclosed). No ISO 13482/CE claims found.

## Deployment evidence & traction
None found beyond demo videos (long-horizon household/manipulation demos); no named customers or pilots as of 2026-08 [estimated from absence of reports]. The investor list (Meituan, SAIC) hints at intended channels in local services and automotive manufacturing.

## Assessment (analyst view)
*Analyst opinion.* Strengths: one of China's strongest embodied-AI teams by funding and model pedigree; genuinely dexterous 20-DoF hands at a disruptive ~$80k price point; investor-strategic channels (Meituan services, SAIC manufacturing). Weaknesses: hardware maturity unproven, 2 h runtime is weak for commercial duty, no safety/compliance story, and specs rest on a single third-party listing. Threat to a new EU entrant: moderate-to-high in the medium term — if WALL-A generalisation holds, X Square could commoditise manipulation autonomy; near-term EU exposure is low as focus is domestic services.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/quanta-x2/ | full spec set, price, image | third-party |
| 2 | DuckDuckGo aggregated snippets (X Square Robot / WALL-A / 融资) | WALL-A model, Wall-OSS, funding rounds, founding | third-party |
