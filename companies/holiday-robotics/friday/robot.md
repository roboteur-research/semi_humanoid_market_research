# Friday — Holiday Robotics

> Korean wheeled industrial humanoid from the ex-SUALAB founder's startup: 176 cm, 63 DoF (7-DoF arms, 5-DoF torso, 20-DoF tactile hands), QDD/BLDC actuation and a Vision-Language-Skill AI stack, aimed at factory manipulation — bin-picking, tool use, light assembly, internal logistics. Competitively significant for an EU entrant: same industrial wheeled-humanoid thesis, backed by ~$110–155M Series A and a Cognex-pedigree vision team, with H2 2026 commercialisation targeted.

| Field | Value |
|---|---|
| Company | Holiday Robotics |
| HQ | Seoul, South Korea |
| Status (2026) | prototype → early commercial (commercialisation targeted H2 2026) [S2] |
| First shown / launch | 2025 (public profile Nov 2025 on humanoid.guide; company founded Apr 2024) |
| Target applications | Manufacturing: bin-picking, tool use, light assembly, internal logistics; retail assistance; research |
| Price | ~USD 200,000 listed ("inquire"); mass-production goal ~₩100M (~$72k) [S1][S2] |
| Availability | Korea first; ~100 units/year planned initial capacity [S2] |

## Design & morphology
Full-height humanoid torso on a compact wheeled base (verified image: white/black body, sensor visor head, articulated waist, low two-section base with camera apertures). Height 173–176 cm, weight ~115 kg [S1]. DoF: 63 total — 7 per arm, 5-DoF torso/waist, 20 per hand [S1][S2]. The 5-DoF torso provides bend/twist working-height flexibility rather than a lift column.

## Locomotion
Wheeled mobile base; drive type n/a (enclosed). Max speed 6.84 km/h (1.9 m/s) [S1]. Terrain/brakes n/a.

## Upper body & manipulation
Two 7-DoF arms; total payload ~20 kg [S1]. End-effectors: in-house five-finger tactile hands, 20 DoF each, with high-precision tactile/force sensing — the company's core differentiation ("Freeing Human Hands") [S1][S2]. Demonstrated/targeted tasks: bin-picking, tool use, light assembly [S1]. Repeatability, tool changer n/a.

## Sensing
Head sensor visor (cameras; details n/a); tactile/force sensing in hands; collision-avoidance and obstacle-detection capability claimed [S1]. Base camera apertures visible in image. Lidar n/a (not disclosed).

## Actuation & power
BLDC motors with QDD (quasi-direct-drive) gearing [S1]. Runtime ~4 h per charge [S1]. Battery capacity, hot-swap, dock n/a.

## Compute & software
NVIDIA Jetson Orin onboard; Wi-Fi [S1]. AI: "Vision-Language-Skill" architecture — a skills-based VLA variant leveraging the team's industrial-vision heritage; teleop/data-collection approach n/a [S2]. SDK/fleet software n/a.

## Safety & compliance
"Designed as safe for human interaction" (listing) [S1, estimated]. No certifications disclosed.

## Deployment evidence & traction
No named customers yet; CEO states commercialisation at manufacturing sites in H2 2026 with ~100 units/year capacity [S2]. Series A ~₩155bn (Jul 2026) is the strongest traction signal [S2]. Demo videos show dexterous-hand manipulation (third-party reporting).

## Assessment (analyst view)
*Analyst opinion.* Strengths: exceptional founder pedigree in factory AI vision (SUALAB→Cognex), genuine 20-DoF tactile hands + 20 kg payload — top-quartile manipulation spec for wheeled humanoids — and serious funding with a clear factory-first plan and price-down roadmap. Weaknesses: 4 h runtime, unproven reliability at scale, Korea-centric channel, and $200k entry price. Threat to a new EU entrant: high — this is arguably the closest non-Chinese analogue to an EU industrial semi-humanoid play, and it will compete for the same automotive/electronics pilots if it enters Europe.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/friday/ | specs (176 cm, 115 kg, 63 DoF, 20 kg payload, 6.84 km/h, QDD/BLDC, Jetson Orin, 4 h), price, image | third-party |
| 2 | https://lite.duckduckgo.com/lite/?q=Holiday+Robotics+Friday (aggregated Korean media) | founding, Series A ₩155bn Jul 2026, Vision-Language-Skill, commercialisation plan, hand DoF | third-party |
