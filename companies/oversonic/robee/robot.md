# RoBee — Oversonic Robotics

> RoBee is a wheeled "cognitive humanoid" (variants: RoBee R industrial, RoBee M medical/rehab, RoBee F intralogistics) built in Lombardy, Italy. Human-scale (1.62–1.90 m), 40 joints, 5 kg per arm, CE-marked under the Machinery Directive and sold to real factories and hospitals — including a global supply deal with STMicroelectronics (first unit live in ST's Malta fab). It matters competitively as the most deployed certified European wheeled humanoid in industry today.

| Field | Value |
|---|---|
| Company | Oversonic Robotics |
| HQ | Besana in Brianza / Carate Brianza, Italy |
| Status (2026) | shipping |
| First shown / launch | Prototype 2021; commercial deployments from ~2023; US launch Jan 2026 |
| Target applications | Machine tending, quality inspection, intralogistics, hazardous environments (chemical/radioactive), hospital logistics & rehab support, aerospace |
| Price | n/a (not disclosed; B2B quote, sale or rental) |
| Availability | Italy (direct), EU orders (DE, FR), US launch Jan 2026 (Cincinnati, LA offices) [S4][S5] |

## Design & morphology
Full anthropomorphic torso, head and two arms on a wheeled base. Height 1.62–1.90 m (electrically adjustable torso lift; earlier variants cited 1.35–2.0 m range across versions), weight up to 180 kg, footprint 69 × 78 cm [S1]. 40 moving joints replicating human body mechanics [S2]. Three product variants share the platform: R (industrial), M (medical/rehabilitation), F (intralogistics).

## Locomotion
Differential-drive wheeled base (omnidirectional drive available on request); max speed 1.2 m/s (~4.3 km/h; some sources cite 3.6 km/h locomotion), max slope 8% [S1][S2]. Indoor industrial floors; inductive auto-recharge docking [S1].

## Upper body & manipulation
Two arms, 90 cm reach each, 5 kg payload per arm / 10 kg bimanual [S1]. Positioning: ±3 mm "cognitive" accuracy, ±1 mm deterministic accuracy, ±0.8 mm repeatability (vendor) [S1]. Anthropomorphic hands/grippers configured per application (details not published); motor controllers provide power/force feedback [S1]. Tool changer / media at flange: n/a (not disclosed).

## Sensing
Lidars, RGB cameras and depth cameras for navigation and vision; thermal camera optional; force feedback from joint motor controls; 60 W speakers + cardioid microphone for the integrated voicebot [S1]. Navigation via proprietary depth-camera-based algorithm [S2].

## Actuation & power
Electric actuation, 40 joints (actuator technology not disclosed). Lithium-ion battery, up to 8 h autonomy, inductive auto-recharge, AC 230 V supply [S1].

## Compute & software
Proprietary cognitive AI platform: multilingual conversation (voicebot), mission planning/execution, trainable ML vision, multimodal reasoning, predictive maintenance; cloud-connected via WiFi 6 / 5G-ready [S1]. No ROS/SDK openness advertised — closed vertical stack. Robots are configured per customer mission rather than end-user programmed.

## Safety & compliance
Vendor claims "only humanoid robot certified for industrial and medical sectors" [S3]. Exactly documented certifications: **CE marking under Machinery Directive 2006/42/EC, EMC-EMI compliance, ISO 27001:2013 (information security management), GDPR compliance, IPX4 ingress rating** [S1]. NOTE (analyst): ISO 27001 is a cybersecurity/ISMS certification, not a robot-safety standard; no ISO 13482, ISO 10218/TS 15066 conformity or medical-device (MDR) classification is published. "Healthcare certification" should be read as CE machinery compliance + hospital pilot approvals; expanded healthcare certifications were stated as planned "by end of 2026" [S6].

## Deployment evidence & traction
- STMicroelectronics global supply agreement (Dec 2025): custom RoBee units for production/logistics across ST plants; first unit operating in ST's advanced packaging & test fab, Kirkop, Malta — first humanoid integration in the semiconductor industry (vendor+third-party) [S4][S7].
- "Operational in several Italian industrial facilities" and hospital experimental programs (third-party; specific customer names largely undisclosed) [S5][S6].
- Mid-2026: STM, Fondazione ENEA Tech Biomedical, SpotInvest equity investment to fund rollout [S8].
- Revenue €4.5–5M (2025), 95% Italy; orders from Germany, France, USA [S6]. Unit count not disclosed (estimated: low tens).

## Assessment (analyst view)
*Analyst opinion.* Strengths: real paying industrial deployments (rare in this class), the STM lighthouse account with multi-plant rollout potential, torso-lift work envelope, 8 h runtime with auto-charging, and a certification-first narrative that resonates with EU factory buyers. Weaknesses: closed software stack, undisclosed pricing, modest 5 kg/arm payload, heavy 180 kg platform, and a certification story that is thinner than marketed (Machinery Directive CE + ISO 27001, not robot-safety or medical-device standards). Threat to a new EU entrant: high — same region, same segment, first-mover references and now chipmaker capital; a newcomer must beat it on openness, price transparency or genuine ISO 13482/10218 conformity.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.oversonicrobotics.com/robee-r/ | Full spec table: dimensions, 180 kg, 5 kg/arm, 1.2 m/s, 8 h, certifications list, sensors, connectivity | vendor-claimed |
| 2 | https://intnews.it/en/oversonics-robee-reshapes-the-future-of-cognitive-humanoid-robots/ | 40 joints, 3.6 km/h figure, navigation, hazardous-environment use | third-party |
| 3 | https://www.oversonicrobotics.com/ | "Only certified humanoid" claim, variants R/M/F | vendor-claimed |
| 4 | https://www.prnewswire.com/news-releases/oversonic-robotics-signs-humanoid-robots-supply-agreement-with-stmicroelectronics-302647593.html | ST deal, Malta first unit | vendor-claimed (joint PR) |
| 5 | https://roboticsandautomationnews.com/2026/01/28/oversonic-robotics-launches-humanoid-robot-robee-in-us-market/98323/ | US launch, Italian deployments, hospital programs | third-party |
| 6 | https://en.ilsole24ore.com/art/oversonic-robotics-italian-humanoid-robots-target-healthcare-and-manufacturing-AIyh9WKC | Revenue, healthcare certification plans, orders DE/FR/US | third-party |
| 7 | https://www.engineering.com/oversonic-and-stmicroelectronics-deploy-humanoid-robots/ | ST deployment context | third-party |
| 8 | https://www.prnewswire.com/news-releases/oversonic-robotics-stmicroelectronics-fondazione-enea-tech-biomedical-and-spotinvest-acquire-a-stake-in-the-company-302806639.html | 2026 equity round | vendor-claimed (PR) |
