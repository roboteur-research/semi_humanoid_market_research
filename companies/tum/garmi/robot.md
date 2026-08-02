# GARMI — TUM MIRMI Geriatronics

> GARMI is TUM's eldercare semi-humanoid research platform: a wheeled base with extendable lifting column, two 7-DoF torque-controlled Franka-lineage arms, chest touchscreen and expressive-eyes head, developed since 2018 at the Geriatronics centre in Garmisch-Partenkirchen for assistance in daily living, tactile telemedicine and rehabilitation. A fully redesigned "new GARMI" (loden-clad, Munich Design Institute) was presented on 22 Jan 2026. It matters as Germany's flagship care-robot program and validation of the wheels+lift-column+compliant-arms architecture for eldercare.

| Field | Value |
|---|---|
| Company | TUM MIRMI (Geriatronics project) |
| HQ | Munich / Garmisch-Partenkirchen, Germany |
| Status (2026) | research (active; model-apartment trials; care-home deployment "several years" away per TUM 2024) |
| First shown / launch | Program since 2018; first GARMI ~2019-2021; redesigned "new GARMI" presented 22 Jan 2026 [S1][S2] |
| Target applications | Eldercare assistance (fetching, help getting up), tactile telemedicine (remote examination: ECG, blood pressure, ultrasound), rehabilitation exercises, social interaction |
| Price | n/a (not for sale) |
| Availability | Not available; research prototypes in Garmisch model apartment / MSRM labs |

## Design & morphology
Human-sized wheeled robot: stable mobile base with low centre of mass, extendable lifting column carrying the upper body, dual arms mounted either side of the column, head with expressive blinking eyes, chest-mounted screen for information display and video consultations [S1][S2]. New 2026 version clad in Alpine loden wool — deliberately friendly, explicitly non-humanoid appearance [S2]. Exact height/weight/DoF totals not published (n/a, not disclosed).

## Locomotion
Wheeled mobile base (drive type not detailed publicly; earlier GARMI used an omnidirectional base). TUM notes the drivetrain could theoretically reach ~20 km/h but is governed by MIRMI's "Safety Motion Unit," which decelerates near people [S4, vendor-claimed]. Indoor use.

## Upper body & manipulation
Two 7-jointed torque-controlled robot arms (Franka Emika lineage — MIRMI/Haddadin technology) with force/tactile sensing; anthropomorphic artificial hand demonstrated for grasping [S4]. Demonstrated: grasping cups and glasses with ~90% success, bringing water/breakfast to a bedside, assisting a person to get up, guiding rehab exercises with physical interaction, and bimanual support tasks [S4]. Telemedicine end-effectors: handling/positioning of ultrasound probe and diagnostic devices in remote-examination demos [S1][S3]. No tool changer disclosed.

## Sensing
Cameras at eye level in the head; lidar at leg height in the base; 3D cameras planned for arm-workspace coordination (2026 redesign); force sensors on arms registering slightest contact; tactile sensors; integrated medical devices as payloads (ECG, blood pressure, ultrasound) plus external IoT health sensors [S2][S3][S4].

## Actuation & power
Torque-controlled arm joints with 1 ms control cycle (perception-interaction-navigation loop at 1 kHz) [S4, vendor-claimed]. Battery/runtime n/a (not disclosed).

## Compute & software
Onboard compute not itemized publicly. Software: MIRMI stack with digital-twin simulation for collision-free planning before execution; ChatGPT-based natural-language command interface (15-20 commands as of May 2024: "start rehab", call doctor, weather, etc.), autonomous task planning; teleoperation for remote medical examination [S4][S3]. No public SDK.

## Safety & compliance
Research platform, no certification (n/a). Safety concept: 1 ms reaction to contact via arm force sensors, immediate stop on touch, Safety Motion Unit speed governor near humans, digital-twin pre-checking [S4, vendor-claimed] — an unusually explicit safety architecture for an academic platform, reflecting MIRMI's human-robot-safety heritage.

## Deployment evidence & traction
No commercial deployments. Trials: permanent model apartment at the Garmisch-Partenkirchen Geriatronics centre with seniors and care partners (Caritas, LongLeif) [S1][S4]; telemedicine demos with remote physicians; rehab-exercise studies. TUM stated (May 2024) real care-home deployment is still "several years" away [S4]. Discovery-note claim of spin-off intent could not be verified — no GARMI spin-off company found as of Aug 2026 (open question). Program continuity confirmed post-Haddadin: redesigned robot presented Jan 2026 under Prof. Alexander König [S2].

## Assessment (analyst view)
(Analyst opinion.) Strengths: best-funded and most visible German eldercare robot program; real safety architecture; Franka-grade compliant manipulation; strong clinical/care partnerships and a live model apartment; fresh 2026 redesign signals continued investment. Weaknesses: still research-grade — no published specs, no certification path shown, deployment horizon repeatedly "several years"; founder departure (Haddadin → MBZUAI, Jan 2025) removes its most forceful commercial champion. Threat to a new EU entrant: low as competitor, high as the reference customer-validation ecosystem — a care-focused entrant should seek Garmisch/Caritas-style pilots or partnership rather than compete for the same public attention.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.mirmi.tum.de/en/mirmi/research/projects/geriatronics/ | Program since 2018, GARMI description, Garmisch centre, telemedicine | vendor-claimed |
| 2 | https://www.tum.de/en/news-and-events/all-news/press-releases/details/researchers-present-new-garmi | New GARMI 22 Jan 2026: base + lifting column + dual arms, sensors, loden design, team | vendor-claimed |
| 3 | https://www.medica-tradefair.com/en/medtech-devices/garmi-assistance-robot-care | Telemedicine devices (ECG, BP, ultrasound), IoT health data | third-party |
| 4 | https://www.tum.de/en/news-and-events/all-news/press-releases/details/garmi-care-robot-becomes-a-universal-assistant | May 2024: ChatGPT commands, 90% grasp, 1 ms cycle, Safety Motion Unit, 20 km/h theoretical, model apartment | vendor-claimed |
| 5 | https://en.wikipedia.org/wiki/Sami_Haddadin + https://mbzuai.ac.ae/study/faculty/sami-haddadin/ | Haddadin to MBZUAI Jan 2025 (context) | third-party |
