# Nyokkey (ニョッキー) — Kawasaki Heavy Industries

> Nyokkey is Kawasaki's ~150cm, 75kg wheeled dual-arm "social robot" — the service-sector sibling of its Kaleido biped — built to automate hospital logistics, café service and facility rounds where a human-shaped, elevator-riding, door-opening robot is needed. It is Japan's most institutionally validated semi-humanoid pilot platform: specimen transport with automatic analyzer loading at Fujita Health University (claimed world first, 08/2025), the AI-SCAPE robot café at Haneda, a hydrogen fuel-cell variant (01/2026), and it is the hardware basis of the Foxconn/NVIDIA Nurabot.

| Field | Value |
|---|---|
| Company | Kawasaki Heavy Industries / Kawasaki Robotics |
| HQ | Tokyo/Kobe, Japan |
| Status (2026) | prototype (pilots; units marked "reference exhibit — not for sale") |
| First shown / launch | Developed from spring 2021; public from ~Jan 2022 (iREX/International Robot Exhibition 2022) |
| Target applications | Hospital logistics (specimens, pharmaceuticals), café/food service, patrol & inspection, guidance |
| Price | Not for sale (pilot/PoC placements); n/a (not disclosed) |
| Availability | Japan pilots only; derivative Nurabot targeted for FY2026 commercial launch |

## Design & morphology
Wheeled AMR base carrying a humanoid torso with two arms and a sensor/display head; height ~150cm, weight 75kg [S2, third-party]. Payload trays/cargo space can be fitted between/behind arms for transport missions. Part of the Kaleido humanoid family engineering line [S1]. DoF total n/a (not disclosed).

## Locomotion
Indoor wheeled AMR: autonomous navigation that "recognizes surrounding conditions and adapts to environmental changes", obstacle/collision avoidance, and **elevator integration** — Nyokkey rides elevators between floors either via building-system link [S1][S4]. Speed n/a (not disclosed).

## Upper body & manipulation
Two 6-DoF arms, ~6kg payload each [S2, third-party]. Demonstrated: picking up specimen containers and **loading them into clinical analyzers** (precision machine-tending in a live hospital lab) [S4]; carrying trays, operating doors; approaching objects with arm-mounted sensors for close measurement [S3]. End-effectors are task-specific grippers; no tool-changer disclosed.

## Sensing
LiDAR + vision sensors for navigation; arm-mounted sensors for close-range measurement; screen and speakers for interaction [S1][S2][S3]. The **Eureka Robotics** partnership adds high-accuracy 3D camera + controller ("eyes and brain") for autonomous precision picking (99.5% reliability claimed by Eureka), slated to broaden Nyokkey's autonomous manipulation from 2026 [S6, third-party].

## Actuation & power
Battery-electric; capacities n/a (not disclosed). **Hydrogen fuel-cell variant** unveiled 15 January 2026 with Toyota Boshoku (fuel-cell packaging) and Daido University — hydrogen canister swap eliminates charging downtime ("zero charging wait"), targeting continuous facility rounds [S5, third-party].

## Compute & software
Onboard compute n/a (not disclosed). Modes: full autonomy on mapped routes, or remote operation via Kawasaki's **Successor** remote-collaboration system (communicator device), with motion-learning to convert repeated teleop into semi-automation — Kawasaki's skill-transfer thesis [S1]. Generative-AI conversation capability incorporated for guidance/interaction tasks [S3]. Fleet/coordination: at Fujita, Nyokkey coordinated with the FORRO delivery robot and hospital systems (phase 3 plans deeper HIS integration) [S1][S4].

## Safety & compliance
Collision avoidance, human-coexistence design from cobot (duAro) heritage; no published ISO 13482/10218 certification for Nyokkey — n/a (not disclosed).

## Deployment evidence & traction
- **Fujita Health University hospitals** (partnership since 2021; Okazaki Medical Center): phased PoC — ward patrol (COVID era), inter-floor transport of specimens/pharmaceuticals with elevator use; **4-6 August 2025**: FORRO delivered specimens from wards, Nyokkey unloaded and **auto-loaded them into clinical analyzers** — claimed world first for robot-coordinated specimen workflow (with Sysmex lab equipment) [S3][S4, third-party/university].
- **AI-SCAPE robot café, Haneda Innovation City** (from April 2022): meal serving and dish clearing/washing support in a working café [S1, vendor-claimed].
- **Hydrogen Nyokkey** demo with Toyota Boshoku + Daido University, video released 15 January 2026 [S5].
- Basis platform for **Nurabot** (see ../nurabot/robot.md): TCVGH Taiwan pilots from 04/2025 — first overseas medical use of the Nyokkey platform [S7].
- No commercial sales; all placements are partner pilots [S2].

## Assessment (analyst view)
*Analyst opinion.* Strengths: real regulated-environment validation (live hospital lab, not a demo booth), elevator/building integration, conglomerate-grade safety and manufacturing, unique energy option (hydrogen), and a credible autonomy roadmap via Eureka vision + Successor teleop. Weaknesses: five years in, still "not for sale" — classic Japanese-incumbent pilot purgatory; specs (battery, compute, DoF) undisclosed; 6-DoF arms lag the 7-DoF dexterity norm. Threat to an EU entrant: high in hospital logistics — the Fujita workflow (transport + analyzer loading) is exactly the beachhead EU healthcare semi-humanoids (e.g. Mirokai, MiPA) target, and Kawasaki + Foxconn can out-scale anyone in Asia once FY2026 productization lands; low in the EU near-term, where Kawasaki has no announced service-robot channel.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://kawasakirobotics.com/asia-oceania/blog/story_16/ | origin 2021, capabilities, Successor teleop, Fujita phases, AI-SCAPE café | vendor-claimed |
| 2 | https://www.robotatta.com/products/484 | ~150cm, 75kg, 2×6-DoF arms, 6kg/arm, Jan 2022, not-for-sale | third-party |
| 3 | https://kawasakirobotics.com/uploads/sites/2/2024/09/JRW2024_Nyokkey_en.pdf | autonomous driving, machine loading, arm-sensor measurement, gen-AI conversation, reference-exhibit status | vendor-claimed |
| 4 | https://www.fujita-hu.ac.jp/news/vsfo8q0000009ctb.html + https://www.khi.co.jp/pressrelease/news_250821-1.pdf | 08/2025 world-first specimen transport + analyzer auto-loading (FORRO+Nyokkey, Sysmex) | third-party |
| 5 | https://robotstart.info/article/2026/01/15/381561.html | hydrogen fuel-cell variant, Toyota Boshoku + Daido Univ, 2026-01-15 | third-party |
| 6 | Eureka Robotics partnership coverage (LinkedIn/aeo.washinmura.jp aggregations) | Eureka 3D vision "eyes and brain" for Nyokkey, 99.5% picking claim | third-party |
| 7 | https://global.kawasaki.com/en/corp/newsroom/news/detail/?f=20250704_7252 | Nurabot = Nyokkey-based, first overseas medical use | vendor-claimed |
