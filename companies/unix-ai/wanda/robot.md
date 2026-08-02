# Wanda / Wanda 2.0 (万达) — UniX AI (优理奇)

> Wanda 2.0 is UniX AI's full-size wheeled humanoid for household and commercial service: 1.4–1.68 m tall (280 mm torso lift), 33 DoF with industry-first mass-produced 8-DoF bionic arms, 12 kg dual-arm payload, and a tactile-model-driven software stack (Unitouch). Pre-sales opened December 2024 from RMB 88,000 — the first "ten-thousand-yuan-class" full-size humanoid — making it the price-disruption benchmark of the category. Viral demos (laundry, burger-flipping, tofu handling) and a Yale/SJTU founding team give it outsized visibility relative to its funding.

| Field | Value |
|---|---|
| Company | UniX AI (优理奇) |
| HQ | Suzhou, China |
| Status (2026) | shipping |
| First shown / launch | Wanda 1: 2024-08 (WRC 2024 + CCTV coverage); Wanda 2.0: pre-sales 2024-12-25, mass-production deliveries spring 2025 |
| Target applications | Household service (laundry, kitchen, tidying), reception/guiding, retail & mall service, eldercare, catering, research & education, security |
| Price | Wanda 2.0 from RMB 88,000 (~USD 12k) pre-sale base config [S3] |
| Availability | China + international inquiries (global@unix-group.ai); direct purchase; mass production since 2025 |

## Design & morphology
Full-size wheeled humanoid: height adjustable 1,400–1,680 mm via 280 mm torso lift; minimum passage width 750 mm; 33 DoF total [S1][S4]. Dual 8-DoF bionic arms in a "4+1+3" configuration (shoulder/elbow 4 + torso-coupling 1 + wrist 3) — vendor claims world's first mass-produced 8-DoF arm [S3][S4]. 2-DoF head (yaw ±90°, pitch ±30°) [S1]. Weight: n/a (not disclosed).

## Locomotion
Wheeled chassis (quiet, obstacle-avoiding; drive layout not detailed — renders show concealed casters/drive wheels), max speed 1.5 m/s [S1][S4].

## Upper body & manipulation
- Arms: 2 × 8 DoF; single-arm span 982 mm; max reach height 2,300 mm (with lift) [S1][S4].
- Payload: 12 kg dual-arm peak [S1].
- Repeatability: ±0.5 mm at end-effector (vendor-claimed) [S1].
- End-effector: biomimetic 2-finger adaptive underactuated gripper; tactile sensing integrated with Unitouch visual-tactile model (fabric discrimination, tofu handling, cable insertion) [S1][S2].

## Sensing
Head: dual RGB + RGBD cameras; 6-microphone circular array [S1]. Base: 360° lidar + ultrasonic sensors [S1]. Tactile: gripper tactile sensors feeding Unitouch multimodal model [S2]. 3D vision for real-time localization/navigation [S2].

## Actuation & power
Actuator types not disclosed. Battery runtime 8–16 h (vendor-claimed) [S1]. Hot-swap/charging dock: n/a (not disclosed).

## Compute & software
Onboard compute up to 275 TOPS [S1]. Unitouch visual-tactile multimodal large model (vendor-claimed world first) + self-developed multimodal LLM integration; natural-language dialogue; VR teleoperation; demonstration-based rapid task learning ("multimodal semantic keypoint learning + efficient trajectory imitation"); pre-installed L4-level task apps for target scenarios [S2][S3][S4]. SDK/ROS: n/a (not disclosed).

## Safety & compliance
No certifications publicly cited. Quiet chassis with obstacle avoidance; consumer-safety posture implied by household targeting but unverified. Confidence: vendor-claimed.

## Deployment evidence & traction
- CCTV News feature (08/2024): laundry, dishwashing, burger prep, tofu handling in home-like sets — nationally broadcast demos, curated conditions [S2] (third-party).
- WRC 2024 Beijing booth with live demos drawing crowds [S2].
- Pre-sales opened 2024-12-25; mass-production deliveries reported from Feb 2025 (one source) / 2025-05-08 (another); unit counts n/a (not disclosed) [S3][S4].
- Successor Panther (3rd gen) launched 2026-04-08 with "documented deployment in real household settings" — 160 cm, ~80 kg, 34 DoF, dual 8-DoF arms 12 kg each, 80 cm lift, 2,070 TOPS [S5]. Wanda continues as the value line.

## Assessment (analyst view)
*Analyst opinion.* Strengths: category-defining price point (RMB 88k for a full-size 33-DoF platform), real tactile-manipulation IP (Unitouch), 8-DoF arms giving human-like elbow-around-obstacle reach, and unmatched consumer-media visibility. Weaknesses: household autonomy is still teleop/demo-assisted; no disclosed weight, actuator, or safety data; funding (~RMB 0.5-0.7B total) is modest for a hardware consumer play; ±0.5mm repeatability claim is unverified. Threat to an EU entrant: medium-high — not via EU industrial channels but by resetting price expectations globally; if Wanda-class hardware reaches EU consumer/light-commercial channels at 5-figure euro prices with CE marking, it undercuts any EU-built service humanoid on cost. Watch the Panther generation for consumer traction evidence.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.unix-group.ai/wanda/181.html | Official Wanda 2.0 specs (height, lift, reach, 12kg, ±0.5mm, 1.5m/s, 8-16h, 275 TOPS, sensors, gripper) | vendor-claimed |
| 2 | https://news.qq.com/rain/a/20240828A07DPN00 | Unitouch, CCTV demos, founder, VR teleop, 3-finger gripper on Wanda 1 | third-party |
| 3 | DuckDuckGo aggregate (预售 articles) | ¥88,000 pre-sale 2024-12-25, mass production 2025-05-08, 8-DoF arm first, funding | third-party |
| 4 | https://lite.duckduckgo.com aggregate (33自由度 articles) | 33 DoF, "4+1+3" arm config, 2300mm reach height, Feb 2025 delivery, founding 04/2024 | third-party |
| 5 | DuckDuckGo aggregate (Panther articles) | Panther 3rd-gen specs & 2026-04-08 launch | third-party |

*Unknown fields = n/a (not disclosed).*
