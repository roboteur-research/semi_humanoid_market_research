# AIREC / Dry-AIREC (アイレック) — Waseda University (Moonshot Goal 3)

> AIREC (AI-driven Robot for Embrace and Care) is Japan's flagship government-funded nursing humanoid: a ~150kg full-size robot developed under JST Moonshot Goal 3 by Prof. Shigeki Sugano's Waseda consortium to physically care for Japan's ageing population — rolling patients over, sitting them up, dressing socks, cooking, ultrasound scanning. Current prototype Dry-AIREC ver. 1.0 (hardware built by Tokyo Robotics) is WHEELED: a torque-controlled dual-arm torso with multi-finger hands on an articulated column lower body over a round mobile base — resolving conflicting reports, it is not bipedal. Facility use is targeted around 2030 at no less than ¥10M.

| Field | Value |
|---|---|
| Company | Waseda University Sugano Lab / JST Moonshot Goal 3 consortium |
| HQ | Tokyo, Japan |
| Status (2026) | research (Dry-AIREC ver. 1.0 prototypes; care-facility trials since 2024) |
| First shown / launch | Project start 2020; Dry-AIREC demos 2022-2025; Reuters world coverage 02/2025 |
| Target applications | Nursing/elder care (repositioning, transfer, diaper change support, bathing/feeding assist), housework (cooking, laundry), medical support (ultrasound, medication, vitals) |
| Price | Target "no less than ¥10M" (~USD 67k) at ~2030 introduction (vendor-stated) |
| Availability | Not available; ~2030 for care/medical facilities; 10 final prototypes planned for social demonstration |

## Design & morphology
Full-size humanoid, ~150kg [S2]. Dry-AIREC configuration (verified from photos and the platform's research papers): dual 7-DoF arms with torque sensors at every joint, multi-finger humanlike hands, sensor head with binocular RGB cameras, torso on an articulated single-column "leg" (knee-like bend for floor-to-bed reach) mounted on a round WHEELED base [S3][S4]. **Base-type conflict resolved: current prototypes are wheeled/column, not bipedal**; bipedal claims appear to stem from concept-level descriptions of the 2050 goal [S3][S4].

## Locomotion
Wheeled round base (drive details n/a); the articulated column provides large vertical workspace for bed-height care tasks [S4 - photo evidence].

## Upper body & manipulation
7-DoF torque-sensing arms; multi-finger hands (finger DoF n/a). Demonstrated physical-assist tasks: rolling a person onto their side (diaper change/bedsore prevention), supine-to-sitting transfer (reach-hold-lift sequence), assisting sit-up and sock dressing, folding laundry, cooking scrambled eggs, tabletop wiping [S2][S3]. Medical demos: autonomous ultrasound probe operation, palpation, medication workflow with 5R verification, vitals acquisition with cloud integration [S5].

## Sensing
Binocular RGB head cameras; whole-arm proprioception (joint angles + torques — 28-dim signal used in research); skeletal recognition of patients for height-adaptive guidance [S3][S5].

## Actuation & power
"Dry" = electric torque-controlled actuation (Tokyo Robotics platform lineage). A future "wet" phase plans back-drivable hydraulic elements and self-healing materials for softer human contact [S1]. Battery/runtime n/a.

## Compute & software
Research AI stacks: predictive-processing neural networks (PV-RNN) integrating high-dimensional vision + proprioception for caregiving tasks; deep predictive learning; Level 1→3 autonomy roadmap (individual tasks → semi-autonomous service/housework 2025 → collaborative care autonomy 2030) [S1][S3].

## Safety & compliance
Research stage; human-contact safety via torque sensing/compliance. No certification (n/a). Human-subject verification planned within project governance [S1].

## Deployment evidence & traction
- Care-facility (介護老人保健施設) testing since 2024 [S5] (JST-reported).
- Reuters/global press demonstration of patient-rolling, Feb 2025 [S2].
- Plan: 10 final-version AIREC units for social demonstration; dozens of business-purpose units for evaluation [S1].
- No commercial deployments; ≥¥10M initial price and ~2030 facility introduction per Sugano [S2].

## Assessment (analyst view)
*Analyst opinion.* AIREC is the world's most serious attempt at contact-rich care robotics — patient repositioning is a heavier, riskier manipulation regime than anything commercial semi-humanoids ship today, and the torque-sensing/compliance pedigree (Waseda + Tokyo Robotics/Yaskawa) is real. But it is a research program on a 2030 clock with government-flagship economics; the ¥10M price is aspirational and the autonomy levels remain lab-bound. For an EU entrant, AIREC is less a competitor than a market-maker: it legitimizes the care vertical, defines Japanese regulatory/acceptance groundwork, and signals that whoever industrializes compliant heavy-contact manipulation first inherits a state-primed market.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://airec-waseda.jp/en/about_en/ + https://www.jst.go.jp/moonshot/program/goal3/31_sugano.html | project structure, levels, wet-mechanism plan, 10-unit plan | vendor-claimed (project/JST) |
| 2 | https://www.usnews.com/news/technology/articles/2025-02-27/ai-robots-may-hold-key-to-nursing-japans-ageing-population | Reuters: 150kg, rolling demo, ~2030, ≥¥10M, task list | third-party |
| 3 | https://arxiv.org/pdf/2510.25053 | Dry-AIREC built by Tokyo Robotics; 7-DoF torque-sensing arms; binocular head; repositioning/wiping experiments | third-party (peer research) |
| 4 | https://interestingengineering.com/innovation/japan-tests-airec-robot-easing-elderly-care | photos showing wheeled column base, multi-finger hands | third-party |
| 5 | https://www.jst.go.jp/moonshot/program/goal3/appeal/31_sugano_ap03.html | 2024 care-facility trials, ultrasound/medication/vitals demos | vendor-claimed (JST) |
