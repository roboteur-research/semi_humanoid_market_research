# TITAN — RoboForce

> TITAN is RoboForce's dual-arm industrial robot for harsh outdoor environments, offered on interchangeable wheeled or tracked bases. With 40 kg payload per arm, a claimed 1 mm manipulation accuracy, 8-hour runtime and an NVIDIA Jetson + RF-Net 3D-foundation-model stack, it targets utility-scale solar installation, mining, ports and data-center construction — segments almost no other semi-humanoid addresses. Vendor claims 11,000+ pre-orders via LOIs; pilots ran through 2025 with commercial launch targeted end-2025.

| Field | Value |
|---|---|
| Company | RoboForce |
| HQ | Milpitas, CA, USA |
| Status (2026) | shipping/pilot (US availability claimed 2025; energy-sector pilots underway; scaling manufacturing) |
| First shown / launch | Public debut Intersolar San Diego, February 2025; commercial launch targeted end-2025 |
| Target applications | Solar module installation ("ground to grid"), mining, shipping/ports, data-center construction, manufacturing, space |
| Price | n/a (not disclosed) |
| Availability | USA (2025-26); certified early partners claimed in 12+ countries; direct/partner engagements |

## Design & morphology
Dual-arm torso on an interchangeable mobile chassis: customers choose **wheeled or tracked** locomotion variants for terrain [S1][S2]. Standing height 2,100 mm; weight n/a. Industrial (non-anthropomorphic head) design with sensor mast; built for outdoor dust/heat conditions. DoF counts not disclosed [S2].

## Locomotion
Wheeled variant (drive type n/a) or tracked variant for rough terrain; speed n/a; outdoor terrain operation is the design point (solar farms, mine sites) [S1][S2].

## Upper body & manipulation
- Two arms, up to **40 kg payload per arm** (88.1 lb) [S1].
- Reach: 1,100 mm [S2].
- Claimed manipulation accuracy: **1 mm (0.03 in)** — vendor-claimed, notable if held under outdoor conditions [S2][S3].
- Task repertoire: pick, place, press, twist, connect (e.g., solar module mounting and electrical connection) [S1].
- Multiple end-effector options on the dual-arm assembly; details n/a [S2].

## Sensing
Sensor suite not itemized publicly; perception built around RF-Net, RoboForce's 3D foundation model for spatial awareness in unstructured outdoor scenes [S2][S3]. Assume multi-camera + depth; lidar unconfirmed.

## Actuation & power
Electric actuation (details n/a). 8-hour continuous production runtime per charge (480 min max operating time) [S2]. Battery capacity/hot-swap n/a.

## Compute & software
NVIDIA Jetson onboard compute; WiFi + 5G connectivity; closed-source software stack; RF-Net 3D foundation model + "domain intelligence stack" co-designed with the hardware [S2][S3]. Highlighted by NVIDIA CEO Jensen Huang at GTC keynote Oct 28 2025 [S4]. No public SDK.

## Safety & compliance
n/a (not disclosed). Outdoor/industrial siting reduces human-proximity requirements; no certifications published.

## Deployment evidence & traction
- Intersolar 2025 debut (Feb 2025); pilot projects with early customers through 2025; demonstration at Three Rivers Solar installation [S3] (third-party).
- "Currently testing with customers in field environments"; certified early partners in 12+ countries [S1] (third-party, vendor-sourced).
- **11,000+ robot orders via letters of intent across six industries — vendor-claimed; LOIs, not firm POs** [S4].
- $52M YZi Labs round (Mar 2026) explicitly for commercialization/manufacturing scale-up [S1].
- No named paying customers or delivered-unit counts published.

## Assessment (analyst view)
*Analyst opinion.* Strengths: unique outdoor positioning with real tailwinds (solar labor shortages), heavyweight payload (40 kg/arm) far above indoor rivals, tracked option, credible AI-compute story (Jetson + RF-Net, NVIDIA keynote visibility), and fresh capital. Weaknesses: aggressive marketing numbers (11,000 LOIs, 1 mm outdoor precision) with thin independent verification, no disclosed pricing/customers, and the brutal reliability economics of outdoor robotics. Threat to a new EU entrant: LOW in indoor factory/lab segments, but HIGH if the EU entrant targets energy/construction verticals — RoboForce would arrive in EU utility-solar tenders with a purpose-built product. Recommended stance: monitor for verified solar-farm deployments and treat all volume claims as unaudited.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.therobotreport.com/roboforce-raises-52m-to-commercialize-its-titan-robot/ | Funding, wheeled+tracked variants, 40 kg/arm, task repertoire, field testing, 12+ countries, scale-up plans | third-party |
| 2 | https://www.aparobot.com/robots/titan | Height 2100 mm, reach 1100 mm, 1 mm accuracy, 8 h/480 min runtime, Jetson, WiFi/5G, closed source, availability USA 2025, end-effector options | third-party (database) |
| 3 | Search-aggregated coverage (Intersolar 2025, Three Rivers Solar, RF-Net) | Debut, pilots, commercial launch end-2025, RF-Net co-design, 1 mm solar-module claim | third-party |
| 4 | Search-aggregated order/keynote coverage | 11,000+ LOI orders across 6 industries; Jensen Huang GTC keynote Oct 28 2025 | vendor-claimed / third-party |
