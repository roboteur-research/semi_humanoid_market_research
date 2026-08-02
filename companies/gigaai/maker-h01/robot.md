# Maker H01 — GigaAI (极佳科技)

> Maker H01 is GigaAI's first robot: a 160 cm, 64 kg wheeled dual-arm humanoid (28 DoF, dual 7-DoF arms, 0-2 m vertical reach) on an omnidirectional all-wheel-drive base, unveiled November 2025 as a "Physical AGI Native Platform". Its role is to embody GigaAI's world-model stack (GigaWorld + GigaBrain end-to-end control) — hardware as a training/validation vehicle for models, not a vertical service product. Listed at ~$160k prototype pricing for home service, hospitality, workplace assistance and light logistics.

| Field | Value |
|---|---|
| Company | GigaAI (极佳科技) |
| HQ | Beijing, China |
| Status (2026) | prototype [third-party] |
| First shown / launch | Unveiled 11/2025 [S1][S2] |
| Target applications | Home service, hospitality/reception, workplace assistance, light logistics, education; primarily world-model training/validation platform |
| Price | ~$160,000 (listed; unverified) [S3, third-party] |
| Availability | Not generally available; prototype [S3] |

## Design & morphology
Wheeled humanoid: 160 cm, 64 kg; 28 DoF total; vertical working reach 0-2 m (torso articulation); shipping dims 170 × 70 × 50 cm [S3, third-party DB]. Five-finger hands visible on demo units; modular end-effectors (grippers or dexterous hands) [S2].

## Locomotion
Omnidirectional all-wheel-drive chassis; max speed 8 km/h (2.2 m/s — high for the class) [S2][S3]. Indoor use; IP20 [S3].

## Upper body & manipulation
Dual 7-DoF bionic arms, 5 kg payload per arm (8 kg system payload listed); modular end-effectors: grippers or 5-finger dexterous hands [S2][S3]. Reach envelope 0-2 m via torso [S2]. Repeatability n/a.

## Sensing
5 RGB + 4 RGBD cameras distributed across head, chest and hands; 360° lidar on chassis for obstacle avoidance [S2, vendor-claimed via press].

## Actuation & power
Actuators n/a (not disclosed). Runtime ~4 h per charge [S3]. Battery capacity n/a.

## Compute & software
End-to-end GigaBrain system coordinating arms, torso and chassis; world-model-driven stack (GigaWorld family, incl. policy-evaluation world models) combined with VLA + RL; glass-to-action latency reported 250-450 ms [S2][S3]. Onboard compute hardware n/a. Connectivity: WiFi, Ethernet, Bluetooth [S3].

## Safety & compliance
n/a (not disclosed); IP20 [S3].

## Deployment evidence & traction
Prototype unveiled 11/2025; no customers/pilots disclosed. Purpose framed as scaling world-model training/validation [S1][S2]. Funding momentum (Huawei Hubble-led A1) is the main traction signal [S1].

## Assessment (analyst view)
*Analyst opinion.* Strengths: a coherent model-first thesis (world models + VLA + RL) with real research pedigree (DriveDreamer/GigaWorld lineage), Huawei-aligned backing, and a sensibly spec'd platform (7-DoF/5 kg arms, 0-2 m reach, rich camera suite). Weaknesses: hardware is a means to an end — no vertical focus, no deployment evidence, $160k prototype pricing uncompetitive as a product; success depends entirely on unproven world-model transfer claims. Threat to an EU entrant: low as hardware; medium-term watch as an AI-stack competitor/licensor — if GigaBrain-class models commoditize autonomy, hardware differentiation shrinks for everyone.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://news.housebots.com/news/gigaai-launches-maker-h01-setting-the-stage-for-physical-agi | Launch, purpose, funding, CEO claims | third-party |
| 2 | https://x.com/XRoboHub/status/1993604526449074473 + search snippets | 28 DoF, 7-DoF/5kg arms, 0-2m reach, 5 RGB + 4 RGBD cameras, 360° lidar, GigaBrain end-to-end, omni AWD chassis | third-party |
| 3 | https://humanoid.guide/product/maker-h01/ | 160cm/64kg, 8 km/h, 8kg payload, 4h runtime, $160k, prototype, IP20, latency 250-450ms | third-party (DB, unverified) |
| 4 | https://gigaai.cc/maker-h01 | Official product page (JS-rendered, minimal extractable) | vendor-claimed |
