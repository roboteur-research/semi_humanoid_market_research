# HMND 01 (wheeled) "Alpha Wheeled" — Humanoid (UK)

> HMND 01 Alpha Wheeled is a 220 cm, 300 kg dual-arm humanoid torso on an omnidirectional wheeled base, built by London-based Humanoid Ltd in seven months and unveiled in September 2025. It targets industrial logistics, manufacturing and retail (tote/box handling, picking, machine feeding, kitting) under a RaaS model, and it matters competitively because it is Europe's best-funded semi-humanoid program, already validated in PoCs at Ford, Siemens, Bosch, SAP/Martur Fompak sites and anchored by a 1,000+-unit Schaeffler order with Bosch contract manufacturing — exactly the wheeled-industrial-first strategy a new EU entrant would pursue.

| Field | Value |
|---|---|
| Company | Humanoid Ltd (legal: SKL Robotics Ltd), London, UK |
| HQ | London, UK |
| Status (2026) | prototype (Alpha units in PoCs; Beta launch Q3–Q4 2026; no commercial shipments yet) [S1][S4] |
| First shown / launch | 16–18 September 2025 (Alpha Wheeled unveiling) [S2][S3] |
| Target applications | Warehouses, logistics hubs, retail, manufacturing intralogistics: picking/sorting, machine feeding, kitting, loading/unloading, packaging/fulfilment [S2] |
| Price | n/a (not disclosed); RaaS subscription incl. fleet software, maintenance, 24/7 support [S2][S5] |
| Availability | "Early Access" program; Beta Q3–Q4 2026; first commercial RaaS deployments (Schaeffler) Dec 2026 – Jun 2027; CE certification targeted 2027 [S1][S4][S5] |

## Design & morphology
Humanoid torso with head, two arms and interchangeable protective "garments" (soft covers) on an omnidirectional wheeled pedestal base — no legs, no visible lift column disclosed [S1]. Height 220 cm, weight 300 kg, 29 active DoF excluding end-effectors (vendor-claimed) [S1][S2]. Work envelope: floor to 2 m height, shelf depths up to 60 cm [S2]. Per-arm DoF not disclosed (n/a). Torso lift: n/a (not disclosed). Note the unusually large mass vs. typical wheeled semi-humanoids (~150 kg class) — suggests a heavy stability base.

## Locomotion
Omnidirectional wheeled mobile base, max speed 7.2 km/h (2 m/s) (vendor-claimed) [S1][S2]. Terrain/climbing limits, brakes: n/a (not disclosed).

## Upper body & manipulation
Dual arms; bimanual payload 15 kg total (vendor-claimed; "more when objects closer to body" [S3]); in PoCs the robot operated with an 8 kg dual-arm limit (SAP/Martur Fompak; Ford totes up to 8 kg) [S7][S9]. Modular end-effectors: 12-DoF five-fingered hand OR 1-DoF parallel gripper [S1][S2]; Forbes notes modular grippers for variable tasks [S4]. Repeatability: n/a (not disclosed). Media at flange: n/a (not disclosed) beyond the modular hand/gripper interface. Handled parts in the field: KLT totes (3 types), 5 box sizes at Bosch, metal car-body parts at Ford, bearing rings at Schaeffler [S5][S7][S8][S9].

## Sensing
Head: 360° RGB camera array + 2 depth sensors [S1][S2]. Wrist: RGB cameras [S1]. Torso: 6D force/torque sensors [S1]. End-effectors: F/T sensors + haptic feedback sensors [S1]. Base sensors (lidar/ultrasonic/bumpers): n/a (not disclosed).

## Actuation & power
Actuator type: n/a (not disclosed); joint actuators supplied by Schaeffler under a 5-year agreement covering >50% of demand through 2031 (seven-digit actuator volume) [S5]. Battery capacity: n/a (not disclosed). Average runtime 4 h (vendor-claimed) [S1]; Siemens Erlangen deployment reported 8+ h uptime (likely with charging/battery management) [S6]. Hot-swap/dock: n/a (not disclosed).

## Compute & software
NVIDIA Jetson Thor edge compute [S6]; "built on NVIDIA compute" per vendor [S1]. Software: proprietary KinetIQ four-layer AI stack [S1][S10]: System 3 fleet orchestrator (agentic multi-robot coordination, integrates with facility systems); System 2 omni-modal language-model reasoning (task decomposition, dynamic planning, human-assist requests); System 1 VLA network at 5–10 Hz (action chunks with prefix conditioning); System 0 RL whole-body controller at 50 Hz (trained ~15k sim-hours; cross-embodiment wheeled + bipedal) [S10]. Training: NVIDIA Isaac Sim + Isaac Lab, simulation-first (claimed 7-month development vs. typical 18–24) [S6]. Enterprise integration proven via SAP EWM/Joule agent APIs (robot commanded by an external ERP over the internet, fully autonomous) [S7] and Siemens Xcelerator (digital twins, PLC interfaces, fleet management) [S6]. KinetIQ Ascend: real-world RL for manipulation reliability/speed [S1][S16]. Open SDK/API: robot API exists (used by SAP) but no public SDK disclosed.

## Safety & compliance
CE certification targeted for 2027 (not yet achieved) [S4]. Interchangeable garments described as serving "protection and safety" [S1]. No ISO 13482/ISO 10218/TS 15066 claims found; e-stop, safety-rated speed limits: n/a (not disclosed). Safety data collection is a stated purpose of the Alpha pilots [S3].

## Deployment evidence & traction
All Alpha-stage PoCs, no revenue deployments yet:
- Ford, Cologne Innovation Centre (6-week PoC, announced Jan 2026): totes to 8 kg between workstations; 97% autonomous pick-and-place reliability; 83 picks/h vs. 50 target; ~1 h on-site data to deploy models — third-party (Euronews) [S9].
- CES 2026 (Jan 2026): live demo sorting car parts at Schaeffler's booth — third-party observed (CNET) [S11].
- SAP + Martur Fompak (Jan–Feb 2026): fully autonomous order-picking driven by SAP EWM via Joule agents; 3 tote types, 8 kg dual-arm payload — vendor-claimed [S7].
- Bosch, Bühl plant (Mar 2026): autonomous box transfer conveyor→trolley, 5 box sizes — vendor-claimed [S8].
- Siemens electronics factory, Erlangen (Apr 2026): 60 tote moves/h, 8+ h uptime, 90%+ pick success — vendor-claimed [S6].
- Schaeffler RaaS deal (May 2026): four-digit number of wheeled units across global plants by 2032; first deployments Herzogenaurach (box handling in live production) and Schweinfurt (3-month capability demo + 3-month production validation) Dec 2026 – Jun 2027 — vendor-claimed, corroborated by Forbes [S5][S17].
- Aggregate claims (Jul 2026): 9 PoCs completed, 10th underway [S4]; ~25,000 preorders and six Fortune 500 pilots (CEO statement at CES, unverified) [S11]; Bosch manufacturing capacity ~100,000 units over 5 years [S4].

## Assessment (analyst view)
*Analyst opinion.* Strengths: exceptional capital ($270M) and iteration speed; a genuinely differentiated enterprise-integration story (SAP/Siemens) plus the strongest European industrialisation chain of any semi-humanoid startup — Schaeffler actuators/anchor order and Bosch contract manufacturing effectively pre-empt two of the best German scale-up partners. Weaknesses: the product is still Alpha; disclosed specs are thin (no battery, actuator, safety or price data), field payloads (8 kg) sit well below the claimed 15 kg, the 300 kg/220 cm form factor is large for mixed human spaces, and headline traction numbers (25,000 preorders, six Fortune 500 pilots) are founder statements without independent verification. CE certification only in 2027 leaves a compliance window. Threat to a new German entrant: high and rising — Humanoid is executing the same wheeled-first industrial playbook with more money, German lighthouse customers and locked-up supply relationships; a new entrant must differentiate on certified safety, payload/precision, price transparency or vertical depth rather than on the generic tote-handling use case Humanoid is already saturating.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://thehumanoid.ai/hmnd-01-alpha-wheeled/ | Official specs: 220 cm, 300 kg, 29 DoF, 2 m/s, 4 h runtime, 15 kg payload, sensors, end-effectors, KinetIQ, garments, omnidirectional base | vendor-claimed |
| S2 | https://www.therobotreport.com/u-k-based-startup-humanoid-unveils-hmnd-01-alpha-mobile-manipulator/ | Unveiling (Sep 2025), specs, reach envelope (floor–2 m, 60 cm shelf), applications, RaaS, Beta Q3 2026 | third-party |
| S3 | https://www.roboticstomorrow.com/news/2025/09/18/humanoid-unveils-the-uks-first-humanoid-robot-for-industrial-use/25559/ | 7-month build, payload nuance, bipedal roadmap, safety-data purpose | third-party (vendor PR syndication) |
| S4 | https://www.forbes.com/sites/johnkoetsier/2026/07/21/humanoid-raises-152-million-at-135-billion-valuation-europes-newest-robot-unicorn/ | Funding, 9 PoCs, Schaeffler 1,000-robot order, Bosch 100k capacity, CE 2027, Beta/commercial pilots Q4 2026, ~80% human speed target | third-party |
| S5 | https://thehumanoid.ai/humanoid-secures-landmark-deal-with-schaeffler-to-deploy-thousands-of-humanoid-robots/ | Schaeffler deal, actuator supply, deployment sites/timeline, RaaS scope | vendor-claimed |
| S6 | https://thehumanoid.ai/siemens-and-humanoid-bring-physical-ai-to-the-factory-floor-deploying-humanoids-in-industrial-operations-with-nvidia/ | Siemens Erlangen metrics, Jetson Thor, Isaac Sim/Lab, Xcelerator integration | vendor-claimed |
| S7 | https://thehumanoid.ai/hmnd-01-alpha-goes-to-work-humanoid-completes-automotive-manufacturing-logistics-poc-with-sap-and-martur-fompak/ | SAP EWM/Joule integration, autonomy, 8 kg field payload | vendor-claimed |
| S8 | https://thehumanoid.ai/humanoid-secures-partnership-with-bosch-following-a-successful-poc/ | Bosch Bühl PoC, contract manufacturing (Robert Bosch Robotics GmbH), DfX | vendor-claimed |
| S9 | https://www.euronews.com/next/2026/01/20/can-humanoid-ai-robots-really-handle-arduous-factory-work-a-new-ford-factory-trial-exceeds | Ford Cologne trial metrics | third-party |
| S10 | https://thehumanoid.ai/introducing-kinetiq/ | KinetIQ System 0–3 architecture, rates, 15k sim-hours | vendor-claimed |
| S11 | https://www.cnet.com/tech/computing/ive-seen-it-with-my-own-eyes-the-robots-are-here-and-walking-among-us/ | CES 2026 live demo, 25k preorders + 6 Fortune 500 pilots (CEO claims) | third-party (reporting vendor claims) |
| S16 | https://thehumanoid.ai/kinetiq-ascend-toward-100-reliable-manipulation-and-superhuman-speed/ | KinetIQ Ascend real-world RL focus | vendor-claimed |
| S17 | https://www.forbes.com/sites/johnkoetsier/2026/05/13/humanoids-1000-robot-deal-with-schaeffler-hints-at-100000-units-by-2031/ | Independent corroboration of Schaeffler deal scale | third-party |

*Every spec above references a source # and carries confidence: vendor-claimed / third-party / estimated. Unknown fields are marked `n/a (not disclosed)`.*
