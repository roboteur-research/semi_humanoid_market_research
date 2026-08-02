# DiaroiD (ディアロイド) — Mitsubishi Electric

> DiaroiD is Mitsubishi Electric's teleoperated dual-arm humanoid for dangerous-work substitution — one of the very few TRACKED semi-humanoids in the world, riding on CuboRex CuGo MEGA crawlers. Built by the space-systems division on remote precision-control technology from the Subaru and ALMA telescopes, it pairs a ~42-DoF body with multi-finger hands whose dynamic range spans holding a cream puff to gripping 20kg loads, with visual-haptic feedback to the operator. Third-generation prototype; practical use targeted from FY2025.

| Field | Value |
|---|---|
| Company | Mitsubishi Electric (Electronic Communication Systems Works / Space Systems) |
| HQ | Tokyo / Amagasaki (Hyogo), Japan |
| Status (2026) | prototype (3rd generation; deployment target FY2025+) |
| First shown / launch | First giho technical report 2021; progress report 2023; Kansai Robot World 2024 exhibit (with Kubota KATV) |
| Target applications | Hazardous-work substitution: dangerous-materials handling, radiation environments, high-altitude telescope maintenance (ALMA), future space/lunar operations |
| Price | n/a (not commercialized) |
| Availability | Not for sale; internal prototype program |

## Design & morphology
Humanoid torso (head + dual arm/hand units + body housing control electronics and battery) mounted on electric crawler tracks [S1]. Total 42 DoF (third-party MathWorks case study; note: some secondary summaries cite 35 DoF — likely an earlier generation) [S4]. Dimensions/weight n/a (not disclosed).

## Locomotion
TRACKED: CuboRex CuGo MEGA crawler units — selected over overseas alternatives for cost, payload on steep slopes, and straight-line/directional stability [S2]. Crawler and robot body have independent batteries, so the base can still drive home if the torso battery is exhausted [S1]. Demonstrated mounted on Kubota's KATV all-terrain vehicle for leveled operation on rough terrain (Kansai Robot World 2024) [S3].

## Upper body & manipulation
Dual arms with multi-finger hands; grip dynamic range from delicate (holding a cream puff without crushing) to 20kg heavy objects [S1]. Hand axis is designed so a grasped object's centerline coincides with the wrist rotation axis, plus an automatic wrist-rotation function — together enabling tool use, demonstrated by fastening M6 bolts with a hex wrench [S1]. Verified tasks (2023 report): power-plug insertion into an outlet (~4 min), M6 bolt fastening with wrench, two-handed zipper-bag opening (~2 min; one hand stabilizes, the other operates a ~10mm zipper slider) [S1].

## Sensing
Head stereo camera; camera zoom controlled by operator VOICE command so hands stay on the controls [S1][S4]. Visual haptic feedback: loads/moments at the hand are displayed visually to the operator to prevent overload damage [S1].

## Actuation & power
Converted from wired 3-phase 200V AC to onboard 48V DC battery — wireless operation, ~1 hour runtime, no impact on drive performance; separate crawler battery; self-charging capability mentioned by supplier [S1][S2]. Actuator types n/a (not disclosed).

## Compute & software
Proprietary master-slave teleoperation with intuitive custom operating device (joystick-style controls) [S1][S2]. Control developed with MATLAB/Simulink Model-Based Design (Simscape Multibody plant models, Embedded Coder auto-generated code; ~40% development-time reduction claimed; real-time simulation used for operator training) [S4].

## Safety & compliance
n/a (prototype). Operator-in-the-loop with force/moment visual feedback as the primary overload safeguard [S1].

## Deployment evidence & traction
No commercial deployments. Motivating use case: ALMA telescope maintenance at 5,000m in Chile [S2]. Public demonstrations: Kansai Robot World 2024 with Kubota; press assessed it "one step from practical use"; Mitsubishi targets practical application FY2025 onward [S2][S3]. Space/lunar teleoperation named as a future field [S1].

## Assessment (analyst view)
*Analyst opinion.* DiaroiD is the most credible tracked semi-humanoid program globally: telescope-grade teleoperation, genuinely wide-dynamic-range hands (cream puff to 20kg is an unusual demonstrated span), and a conglomerate that can fund it indefinitely. Weaknesses: still a lab prototype after 3 generations, ~1h battery runtime, no announced productization path, price or customer. For an EU entrant the threat is low in commercial indoor markets but real in hazardous-environment tenders (nuclear, disaster response, remote infrastructure) should Mitsubishi productize — and its component choices (commodity CuboRex crawlers under a premium torso) show how cheaply the tracked-base niche can be entered.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.giho.mitsubishielectric.co.jp/giho/pdf/2023/2301008.pdf | battery 48V/1h, dual batteries, hands 20kg + cream puff, task trials, voice zoom, haptic feedback, tool use | vendor-claimed (technical journal) |
| 2 | https://cuborex.com/news/?id=70 | CuGo MEGA crawlers, selection rationale, ALMA 5,000m motivation, 3rd gen, joystick controls | third-party (supplier) |
| 3 | https://dempa-digital.com/article/564633 | Kansai Robot World 2024, Kubota KATV, near-practical status | third-party |
| 4 | https://jp.mathworks.com/company/user_stories/advancing-robotics-design-with-model-based-design.html | 42 DoF, stereo camera, Model-Based Design toolchain | third-party (vendor-supplied case study) |
