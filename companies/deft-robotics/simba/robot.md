# Simba (V1, "Medium Payload Unit") — Deft Robotics

> Wheeled dual-arm mobile manipulator sold as a drop-in workcell for automotive/electronics line feeding and kitting. Competitively notable for its price point ($34,900, down from $40k + $30k/yr maintenance), its teleop-to-autonomy learning loop with reward-model edge-case detection and OTA retraining, and 49 units already sold through a self-serve web store.

| Field | Value |
|---|---|
| Company | Deft Robotics |
| HQ | San Francisco, CA (+ Detroit, South Korea) |
| Status (2026) | shipping (web store "in stock", 49 sold) [S3] |
| First shown / launch | 2025 (company founded 2025; seed announced Feb 2026) |
| Target applications | Line feeding (compressor housings, cross cowl bars), kitting, cable handling, flexible assembly in automotive/appliance/electronics plants |
| Price | $34,900/unit (store, 2026); earlier $40,000 + $30,000/yr maintenance; roadmap V2 <$17k, V3 <$10k [S1][S3][S5] |
| Availability | In stock via deftai.co store; deployment as integrated workcell; product docs announced for Sept 2026 |

## Design & morphology
Boxy AMR base with a central vertical lift column carrying a torso unit; two arms mounted laterally on a cross-bar; sensor head on top with depth camera and Wi-Fi antennas (official render) [S1]. Config per tech page: dual 6-DoF arms + 1-DoF torso rotation + 1-DoF grippers ≈ 15 DoF core (estimated total incl. lift). Height/weight n/a (not disclosed); "Medium Payload Unit" designation implies planned payload variants.

## Locomotion
Holonomic wheeled base [S2, vendor-claimed]. Speed, gradeability n/a (not disclosed).

## Upper body & manipulation
Two 6-DoF arms, 700 mm reach each, 4 kg continuous payload (medium unit) [S2]. 1-DoF grippers standard; "deformable gripper" fingertips sold as $34 accessory (3D-printed compliant jaws); configurable payload/reach/gripper per customer [S1][S3]. Repeatability not stated; placement success 96.77% at 54.2 s/part in a production case study [S2, vendor-claimed].

## Sensing
Head depth camera (visible in render); wrist and "angled belly" camera mounts sold as accessories, GMSL2 camera cabling — implying multi-camera vision setup [S3]. Lidar/base sensors n/a (not disclosed).

## Actuation & power
Actuator types n/a (not disclosed; hardware sourced from established robot manufacturers per funding coverage [S4]). Dual battery packs (left/right, $299 each, XT60/SB50 Anderson charging) suggest swappable packs [S3]. Runtime advertised as continuous 24-h operation with 99.9% success (vendor-claimed, presumably with charging strategy) [S1].

## Compute & software
Compute n/a (not disclosed). Software: teleoperation-first data collection; lightweight transformer manipulation models pre-trained on diverse tasks, fine-tuned on customer production data; separate reward/failure-detection model flags unencountered scenarios; edge cases logged into training set; OTA model updates during maintenance windows; remote human intervention fallback [S1][S2][S4]. 75-95% of human speed from day one claimed [S1]. No public SDK; docs "coming Sept 2026".

## Safety & compliance
n/a (not disclosed). No ISO 10218/TS 15066 or CE claims found; workcell deployment model suggests fenced/enclosed operation is possible but unstated.

## Deployment evidence & traction
- 49 units sold via web store (vendor storefront counter, 2026) [S3, vendor-claimed].
- 2 paid contracts with global enterprises; POCs/pilots with global automotive and electronics manufacturers [S4][S6, third-party].
- Case studies: compressor-housing line feeding and cross-cowl-bar line feeding; testimonial from VP of Operations at a Tier-1 US automotive components manufacturer [S1, vendor-claimed].
- Goal: 30 robots deployed within 12 months (f.inc profile) [S6].

## Assessment (analyst view)
*Analyst opinion.* Strengths: sharply focused automotive Tier-1 use cases with quantified metrics, credible founder pedigree (Tesla/Hyundai/Motional), Korea+Detroit market access, and a working commercial motion (store, accessories, maintenance contract). Weaknesses: hardware is outsourced and modest (6-DoF arms, 4 kg, 1-DoF grippers), no safety certification story, and unit economics at $34.9k with $30k/yr service imply services-heavy margins. For a German entrant this is a direct competitor blueprint in automotive line feeding — the threat is moderate today but rising if the <$17k V2 lands; the counter is certified safety, EU OEM relationships and richer manipulation.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.deftai.co/ | Pricing history, case studies, metrics, render | vendor-claimed |
| 2 | https://www.deftai.co/tech | 6-DoF arms, 700mm reach, 4kg payload, holonomic base, AI stack, 96.77%/54.2s | vendor-claimed |
| 3 | https://www.deftai.co/hardware-products | $34,900, 49 sold, batteries/grippers/camera accessories | vendor-claimed |
| 4 | https://en.wowtale.net/2026/02/08/233492/ | Seed round, teleop-to-autonomy strategy, outsourced hardware, pilots | third-party |
| 5 | https://www.crunchbase.com/organization/deft-robotics (search snippet) | V2/V3 cost roadmap | third-party |
| 6 | https://f.inc/portfolio/deft/ | 2 paid contracts, 30-robot goal, team size | third-party (investor page) |
