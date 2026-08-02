# Mirokai (Mirokaï) — Enchanted Tools

> Mirokai is a 1.23 m, 26 kg semi-humanoid "character robot" that balances and drives on a single ball (ballbot) — unique among commercial robots — with two co-manipulating arms, animated projected face and articulated ears. Sold into hospitals, senior care, airports, retail and hospitality rather than industry, it competes on emotional engagement plus light logistics (3 kg carry, 15 kg trolley pull). It matters competitively as Europe's furthest-along social semi-humanoid: commercial V1 launched June 2026, Paris production line running, Japan distribution signed with Kanematsu, US pilots underway.

| Field | Value |
|---|---|
| Company | Enchanted Tools |
| HQ | Paris, France |
| Status (2026) | shipping (commercial V1 since 16 June 2026; first customer delivery July 2024) [S6][S7] |
| First shown / launch | Miroki character unveiled 29 Nov 2022; CES 2023 debut; Miroka added June 2023; major redesign at CES 2025; commercial V1 at VivaTech June 2026 [S4][S5][S6] |
| Target applications | Hospitals/clinics, senior & supported living, airports, hotels/restaurants, retail, museums; light logistics + social interaction [S1] |
| Price | ~€50,000 purchase + several hundred €/month subscription (2026, third-party); earlier vendor target was ~€30k/unit (2023); ~$40k cited at CES [S8][S12] |
| Availability | Direct in France; deployment partners in USA, Germany, Italy, Japan (Kanematsu/Nagakura), Peru, Saudi Arabia; order via contact form, no public lead times [S2][S9] |

## Design & morphology
Semi-humanoid torso with two arms and an expressive animated head (projected-screen face, 2-DoF articulated long ears) mounted on a ballbot base: the robot balances on a sphere stabilized/driven by three omnidirectional wheels [S4][S10]. Height 123 cm, weight 26 kg (Kanematsu 2025 datasheet-level figures [S9]; the 2024 vendor spec sheet said ~1.30 m / ~30 kg for the prototype [S3]). 28 DoF total per the vendor spec sheet [S3]; The Robot Report cited 22 actuators at the ISIR delivery [S7] — the delta is not publicly reconciled. CES 2025 redesign added a sensor-embedded ring base around the ball, lower center of gravity, protected joints and internal cable routing; the 2026 V1 adds a fully enclosed premium shell, reinforced forearms and carrying structure [S5][S10][S11]. ~1,500 components per robot [S8].

## Locomotion
Ball-balancing drive (three omni wheels on a sphere) gives omnidirectional motion in minimal footprint; the robot can also be physically nudged/guided by touch ("can be moved in any direction"), a deliberate compliance feature for crowded human spaces [S10]. Max speed ~3.2 km/h (~0.9 m/s) [S3]. Vendor claims reliable traversal of carpets, cables and indoor thresholds (V1) [S1]; indoor-only, flat-floor use. Dynamic balancing implies no parking brake in the classic sense — the CES 2025 ring base stabilizes it and provides obstacle detection [S5][S10].

## Upper body & manipulation
Two co-manipulating arms with hands featuring opposable thumbs; per-arm DoF and reach not disclosed [S3]. Payload: lifts/carries up to ~3 kg and pulls trolleys up to ~15 kg [S9]. Signature "connected handles" (a.k.a. runes) concept: standardized handles/universal grips are attached to objects, carts and doors so the robot grasps known geometry — vendor claims a 97% grasping success rate vs ~60% market standard [S3][S10]. This is an environment-adaptation philosophy ("adapt the environment to the robot, not the robot to the environment") rather than general dexterous manipulation [S3]. No tool changer or media at flange. Discovery-note "magnetized forearms" could not be confirmed as such; sources describe the connected-handle system instead.

## Sensing
Vendor spec sheet (2024): 2 RGBD cameras + 2 infrared cameras (head), 12 time-of-flight cameras (8x8 px, distributed), 6 ultrasound sensors, 4 microphones, 3 IMUs (base + both hands), one 6-axis torque sensor [S3]. CES 2025 added the sensor ring around the ball for near-field obstacle detection and 360° coverage [S5][S10]. Face and voice recognition; face tracking is claimed GDPR-compliant [S5][S13]. No lidar disclosed.

## Actuation & power
Ball propulsion: maxon ECi 40 brushless motors with planetary gearboxes; remaining axes use 22 mm maxon ECX Torque brushless motors [S10] (third-party/maxon-sourced article). Battery: capacity not disclosed; vendor-claimed 8 h runtime [S3]. Self-aligning charging dock with autonomous docking on V1 [S1]; vendor roadmap: fully autonomous self-recharging Q4 2026, supervision/fleet management early 2027, "full autonomy" Q1 2027 [S2].

## Compute & software
Onboard: "2 processing units (2 CPUs + 2 GPUs)" per vendor sheet [S3]; press reports Nvidia Jetson-class compute [S5]. Connectivity: embedded cellular modem + Wi-Fi 6E [S1]. Software: proprietary stack with hybrid edge/cloud split optimized for interaction latency; multimodal vision-language(-action) models for perception and interaction; built-in support for ChatGPT, Llama and other LLMs; ~50 languages including Japanese [S5][S8][S9][S11]. Programming: no-code "If This Then That"-style Natural Interaction Programming for non-technical staff [S3]; "Mirokai Explorer Suite" tooling launched spring 2025 [S6]; a Dev Program and Discord community exist for research partners [S1]. Autonomous navigation from floor-plan ingestion ("show it the floor plans") with spatial mapping [S1][S3].

## Safety & compliance
No formal certification (ISO 13482, ISO 10218, UL) publicly claimed; CE status not disclosed. Vendor-described safety package: compliant arms and base, protected joints, low center of gravity, 360° sensor coverage, emergency stop (visible red button on the shoulder handle), explicit LED visual signaling, speed limited to ~3.2 km/h, ergonomic anti-pinch design, GDPR-compliant face tracking [S1][S3][S13]. Operates in sensitive settings (pediatric radiotherapy rooms at ICM, AP-HP geriatric wards) under research/pilot protocols, which implies institutional ethics/safety review but is not a product certification [S14].

## Deployment evidence & traction
- ISIR (Sorbonne, Paris): first commercial delivery, July 2024 — first commercial ballbot delivery anywhere (third-party) [S7].
- AP-HP (Paris hospitals): logistics trial; Broca geriatric hospital partnership; 2-week caregiving pilot at Annie Girardot AP-HP nursing home (28 caregivers, 10 residents, hydration reminders / wellbeing checks), mid-2025 (vendor case study) [S5][S10][S14].
- Institut du Cancer de Montpellier: Miroki accompanies children in pediatric radiotherapy incl. inside treatment rooms — claimed world first (vendor + Les Echos/Le Point coverage) [S14].
- Lyon-Saint Exupéry Airport (VINCI Airports), Nov-Dec 2025: passenger guidance in Terminal 1 and duty-free; 4/5 usefulness, 90% approval among 120 interviewed (vendor-reported stats) [S14].
- APREH (France): contract to deploy 11 Mirokai across care facilities; first unit operating at Foyer La Marcelline (vendor) [S14].
- USA: Mather Institute senior-living study, Evanston IL (Jan 2026); Live Oak Adult Day Services, San Jose CA (Jan 2026, CBS News covered Feb 2026); California silver-economy pilots [S8][S14].
- Japan: Kanematsu domestic sales agreement 8 Sep 2025; Nagakura Mfg. as distributor/maintenance; debut at iREX 2025 [S9].
- Scale: CES 2025 goal of "100 additional robots in 2025" [S5]; as of March 2026 production was "in the dozens" with 250,000 minutes of cumulative robot usage over the prior year — the 100-unit goal appears missed; install base realistically in the low tens (estimated) [S8].

## Assessment (analyst view)
*Analyst opinion.* Strengths: genuinely unique locomotion (only commercial ballbot) and best-in-class character design driving exceptional acceptance in care settings — reference customers (AP-HP, ICM, VINCI Airports, Kanematsu) that a newcomer would need years to win; local Paris manufacturing and a French-sovereignty halo that helps in EU public procurement. Weaknesses: light manipulation (3 kg, handle-dependent grasping) confines it to social/companion and micro-logistics roles; autonomy still maturing (self-recharge only Q4 2026, fleet management 2027); ~€50k + subscription is expensive against Chinese social robots, and the company burns ~€10M/yr on ~€15-33M disclosed funding, so a financing squeeze in 2026-27 is plausible. For a German entrant: Mirokai does not block industrial/logistics semi-humanoid plays at all, but it will be the emotional-design benchmark and incumbent in EU healthcare/hospitality tenders — competing head-on in "companion" niches would be unwise, whereas a payload/task-focused positioning coexists easily. Threat level: high in care/hospitality verticals, low elsewhere.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://enchanted.tools/robot (2026 site payload) | V1 features, Wi-Fi 6E/cellular, safety, dock, use cases, customization | vendor-claimed |
| S2 | https://enchanted.tools/buy-mirokai | Partner regions, deployment phases, autonomy roadmap Q4'26-Q1'27 | vendor-claimed |
| S3 | https://web.archive.org/web/20240722152318/https://enchanted.tools/robot | 2024 spec sheet: 28 DoF, sensors, 8 h battery, ~1.30 m/~30 kg proto, 3.2 km/h, 97% grasp, 2 CPU+2 GPU, NIP/IFTTT | vendor-claimed |
| S4 | https://fr.wikipedia.org/wiki/Enchanted_Tools | 123 cm/26 kg, ballbot w/ 3 omni wheels, character dates | third-party |
| S5 | https://roboticsandautomationnews.com/2025/01/10/enchanted-tools-unveils-advanced-ai-and-design-enhancements-for-character-robots-at-ces/88422/ | CES 2025 redesign, ring base, LLM support (ChatGPT/Llama), Jetson, 100-robot 2025 goal, US expansion | third-party |
| S6 | https://www.planeterobots.com/2026/06/24/enchanted-tools-lance-un-nouveau-robot-mirokai-commercial/ | Commercial V1 June 16 2026, factory/production-line timeline, Explorer Suite | third-party |
| S7 | https://www.therobotreport.com/enchanted-tools-delivers-mirokai-robot-to-its-first-customer/ | First delivery to ISIR July 2024, 22 actuators, first ballbot delivery | third-party |
| S8 | https://www.journaldunet.com/intelligence-artificielle/1549137-les-robots-d-enchanted-tools-assurent-des-missions-d-assistance-de-surveillance-mais-aussi-d-accompagnement-emotionnel/ | ~€50k + subscription, dozens→hundreds→thousands, 250k usage minutes, VLA/edge-cloud, 1,500 components | third-party |
| S9 | https://www.kanematsu.co.jp/en/press/release/20250908_release | 123 cm/26 kg, 3 kg lift/15 kg trolley, Japanese LLM dialogue, Japan deal, iREX 2025 | third-party |
| S10 | https://www.medicaldesignbriefs.com/component/content/article/48488-enchanted-tools-revolutionizing-robotics-with-mirokai | 123 cm, 3 kg, 97% vs 60% grasp, runes, maxon ECi 40/ECX Torque motors, AP-HP Broca, 100k/10yr ambition | third-party |
| S11 | https://www.journaldugeek.com/2026/06/20/le-francais-mirokai-veut-sortir-les-robots-de-science-fiction-des-laboratoires/ | V1 refinements, ~50 languages, multimodal AI, deployments EU/US/JP/KSA | third-party |
| S12 | https://search.brave.com/search?q=Mirokai+robot+price (Geekazine, L'Essentiel de l'Éco, forum aggregates) | €30k target price, ~$40k CES figure | third-party |
| S13 | https://search.brave.com/search?q=Mirokai+safety (aggregated vendor/press safety claims) | Compliant arms, 360° coverage, GDPR face tracking, e-stop | vendor-claimed |
| S14 | https://enchanted.tools/events/icm + /events/adl + /events/apreh + /events/ehpadanniegirardot + /events/mather-study + /events/liveoak | Deployment case studies incl. Lyon Airport stats, APREH 11 robots, ICM, Annie Girardot pilot | vendor-claimed |

*Every spec above references a source # and carries confidence: vendor-claimed / third-party / estimated. Unknown fields marked `n/a (not disclosed)`.*
