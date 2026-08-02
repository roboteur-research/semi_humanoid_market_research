# Psi V1 — PsiBot (灵初智能)

> Psi V1 is PsiBot's wheeled dual-arm humanoid ("轮式双臂，长程专家" — wheeled dual-arm, long-horizon expert): ~1.75 m, 32 DoF, with PsiBot's own H1 16-DoF dexterous hands, built as the embodiment for the company's Psi R-series RL+VLA "fast-slow brain". Its 30-minute autonomous mahjong-playing demo (Psi R1, 05/2025) became one of the defining Chinese dexterity showcases. Target market: semi-structured logistics, retail and 3C — sectors where long-horizon dexterous manipulation, not locomotion, is the bottleneck.

| Field | Value |
|---|---|
| Company | PsiBot / Lingchu Intelligence (灵初智能) |
| HQ | Beijing, China |
| Status (2026) | prototype / pilots (small-scale warehouse validation) [third-party] |
| First shown / launch | 2025 (Psi R1 + mahjong demo 05/2025) |
| Target applications | Logistics sorting, retail, 3C electronics; long-horizon dexterous tasks (mahjong, block building, dexterous packing) |
| Price | n/a (not disclosed) |
| Availability | Not publicly for sale; pilot partnerships [estimated] |

## Design & morphology
Wheeled humanoid: humanoid torso and head on a rounded two-wheel-visible (hub-motor) chassis; ~1.75 m tall [S5, third-party]. 32 DoF body plus two PsiBot H1 dexterous hands at 16 DoF each [S5][S1]. Weight n/a (not disclosed).

## Locomotion
Wheeled base (drive configuration not detailed publicly; renders show two large side wheels + casters) [vendor render, estimated]. Speed n/a.

## Upper body & manipulation
Dual ~7-DoF arms (32-DoF body budget implies 7/arm + torso/head/base, breakdown not published — estimated); PsiBot H1 five-finger dexterous hands, 16 DoF each, tactile-capable; demonstrated fine manipulation: mahjong tile pick/flip/chirality recognition, block building, packing tasks sustained >30 minutes autonomously [S1][S5, vendor-claimed demos].

## Sensing
Head with stereo/depth cameras (dark visor housing sensors); chest camera module visible in renders; tactile sensing via dexterous hands and 62+-DoF exoskeleton haptic gloves used for data collection (Psi-SynEngine) [S1, vendor-claimed]. Details n/a.

## Actuation & power
n/a (not disclosed).

## Compute & software
Psi R-series models: Psi R0 end-to-end RL (12/2024); Psi R1 VLA with CoAT (chain-of-action-thought) framework enabling 30+ minute long-horizon reasoning (05/2025); Psi R2 (04/2026) claimed to top Molmospace benchmarks. Hierarchical "fast-slow brain": RL dexterity policies + VLA planner [S1][S3, vendor-claimed]. NVIDIA simulation-training cooperation [S5, third-party]. Onboard compute n/a.

## Safety & compliance
n/a (not disclosed).

## Deployment evidence & traction
Small-scale warehouse sorting validation with claimed efficiency gains [S1, vendor-claimed]; Meituan "Little Yellow Bee" last-mile delivery robot co-development (separate product line) [S5, third-party]; extensive public demos (mahjong at tech events, FORCE conference appearances). No commercial fleet or named paying customers for Psi V1 [as of 08/2026].

## Assessment (analyst view)
*Analyst opinion.* Strengths: arguably China's strongest dedicated dexterous-manipulation software team (PKU RL lab pedigree), fastest model cadence in the cohort, in-house hands + haptic-glove data engine, and a ¥2B war chest with strategic backing from AgiBot and state funds. Weaknesses: hardware platform is secondary and spec-opaque (no payload/runtime/price data); commercialization is still at validation stage; the company may pivot to licensing models rather than selling robots. Threat to an EU entrant: high on the autonomy axis — Psi R-class long-horizon dexterity is the software benchmark an EU semi-humanoid must match or buy; low as a direct hardware competitor today.

## Second model: ψ-SynRobot (Psi SynRobot) — first mass-production platform
Unveiled 20 April 2026 with simultaneous start of large-scale mass production,
ψ-SynRobot is PsiBot's second wheeled dual-arm humanoid and its first
mass-production machine — successor/productization of the Psi V1 prototype
line. Vendor tagline: "The Smartest Embodied Carrier — a wheeled robot with
multiple skills and reasoning abilities" (自带多技能与推理能力) [S6]. Form
factor: wheeled mobile manipulator with humanoid dual-arm upper body for
structured indoor environments (logistics, retail, industrial), engineered for
"reliable long-duration operation" [S7]. Its defining design choice is
dual-purpose operation + data collection: the robot gathers real-world visual
and tactile data while executing tasks, feeding PsiBot's "data + model
dual-drive" strategy (Psi-SynEngine naming lineage) — effectively putting the
SynEngine data flywheel on wheels in customer sites [S7]. Detailed specs
(DoF, payload, runtime, price) not yet disclosed; hands presumably PsiBot H1
family. Confidence: launch date/mass-production third-party; positioning
vendor-claimed; specs n/a (not disclosed).

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.psibot.ai/en/about-us/ (+ /en/home/) | Model timeline (R0/R1/R2), SynEngine gloves, warehouse validation, team | vendor-claimed |
| 2 | https://www.qbitai.com/2024/11/218183.html | Angel funding, dexterous-manipulation positioning | third-party |
| 3 | http://finance.sina.com.cn/tech/csj/2026-03-10/doc-inhqnrqv6329051.shtml | ¥2B funding, seed investors | third-party |
| 4 | https://aixzd.com/robot/psi-v1 | Psi V1 directory entry: 1.75m, 32 DoF, 16-DoF hands, wheeled dual-arm long-horizon framing | third-party |
| 5 | Search snippets (灵初智能 Psi V1 mahjong; ofweek funding roundup) | Mahjong demo, Meituan Little Yellow Bee, NVIDIA cooperation, H1 hand | third-party |
| 6 | https://www.psibot.ai/en/home/ | ψ-SynRobot "Smartest Embodied Carrier" wheeled multi-skill positioning | vendor-claimed |
| 7 | https://html.duckduckgo.com/html/?q=PsiBot+ψ-SynRobot+灵初智能+SynRobot | ψ-SynRobot unveiling 2026-04-20, mass production start, dual operation+data-collection design, target scenarios | third-party |
