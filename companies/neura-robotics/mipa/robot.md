# MiPA ("My intelligent Personal Assistant") — NEURA Robotics

> MiPA is NEURA Robotics' wheeled, dual-arm "cognitive household and service robot" — a tall lift-column torso on an actuated wheeled base with two arms and multi-finger hands, marketed at a headline €9,999 for the MiPA Home variant. It is the most aggressively priced western semi-humanoid by a wide margin and the product with which Germany's best-funded robotics startup wants to take service robots from B2B into private households and care. Competitively it matters less for what it can verifiably do today (nothing has shipped; no real deployment is documented) than for the price anchor, the domestic-market head start, and the Bosch/Schaeffler/Tether-funded ecosystem behind it.

| Field | Value |
|---|---|
| Company | NEURA Robotics GmbH |
| HQ | Metzingen, Germany |
| Status (2026) | announced (reservations open; NOT shipping as of Aug 2026) |
| First shown / launch | "Market launch" at Automatica, June 24, 2025 [S1][S2]; live demos at IFA Sept 2025 [S5] and CES 2026 [S6] |
| Target applications | Household (dishwasher unloading, tidying, transport), elderly care & health monitoring, hospitality, retail, workplace assistance [S3][S4] |
| Price | €9,999 introductory, MiPA Home model for private households only; €100 fully refundable reservation fee; commercial/industrial pricing on request [S4] |
| Availability | Reservation queue since June 2025; vendor FAQ targets "late 2026 release"; original claim was deliveries in 2025 — slipped [S1][S4] |

## Design & morphology
Single tall column torso ("linear axis" vertical lift is listed among body components [S3]) on a compact wheeled base, with two arms mounted on the column and multi-finger black hands; front touch display, projector, and light strip [S3]. Vendor datasheet (V5, 05.06.2026) states 17 DoF for the base robot excluding end-effectors [S7]; the reservation page states "Manipulation 16 DoF; modular attachments" [S4] — the discrepancy is unexplained (plausibly 2×7-DoF arms + linear axis + head/base DoF). Height and weight are not disclosed anywhere (n/a). Modular hardware: backpack, shelf, table, hook, clip-system and tool-change attachments convert MiPA between carrying/serving/guiding roles; white-label configuration for B2B partners [S3].

## Locomotion
"Actuated wheels" on a flat base; drive geometry (diff vs omni) not disclosed — discovery-file note that base geometry is single-sourced remains true. Indoor use; autonomous mobility with SLAM mapping, path planning, localization and obstacle detection [S3][S7]. Speed not disclosed (n/a).

## Upper body & manipulation
Two arms with multi-finger hands (renders/datasheet show 4-5-finger underactuated hands with black finger shells [S7]). Single-arm payload 3 kg (vendor datasheet [S7]; a third-party profile estimated 5 kg/arm and ~15 kg deadlift — inconsistent with the datasheet, treat the 3 kg vendor figure as authoritative [S6]). Reach, wrist DoF, repeatability: n/a (not disclosed). Tool-change attachment listed among modular accessories [S3]; no media-at-flange details. Demos shown: unloading a dishwasher (CES 2026), tidying plushies into boxes (IFA 2025), beverage service coordinated via Neuraverse (Automatica 2025) [S2][S5][S6].

## Sensing
360° perception (vendor) [S7]. Listed sensors: LiDAR, dedicated navigation sensors, RGB camera plus webcam, ultrasonic, infrared, GPS, temperature, humidity (reservation page adds pressure and air-quality) [S3][S4]. "Safe touchless human detection" recognizing people up to 3 m away [S3]. Microphone array; integration with wearables for vital-sign data in care scenarios [S1]. Force/torque sensing in arms: implied by NEURA's cobot heritage but not explicitly specified for MiPA (estimated).

## Actuation & power
Actuator technology not disclosed (NEURA builds its own joint actuators for LARA/MAiRA; carry-over is likely but estimated). "Motion endurance 2-8 h" depending on load profile; automatic recharging capability (self-docking) [S7]. Battery capacity: n/a (not disclosed).

## Compute & software
Onboard compute not disclosed (Qualcomm is a Series C strategic investor pitching "AI capabilities, high-performance computing and connectivity" for the Neuraverse — future Qualcomm silicon is plausible, estimated [S8]). Software: NEURON OS + Neuraverse ecosystem ("app store" for robot skills, networked learning across robot types), no-code application development, digital-twin simulation, sim-to-real training at physical "NEURA Gym" centers [S1][S7]. AI stack: language model + computer vision + reinforcement learning (vendor) [S7]. Connectivity: Wi-Fi, 5G, Bluetooth, Matter smart-home protocol [S3]. Open APIs / real-time data access for developers and integrators (vendor) [S3]. Voice (multi-language), hand-gesture control, customizable touch interfaces [S3].

## Safety & compliance
No published certifications (no ISO 13482 / ISO 10218 / CE declaration found — n/a, not disclosed). Vendor safety claims: touchless human detection to 3 m with instant reaction, safe operation around people [S3]. For a robot aimed at private households and care, the absence of any published safety-standard compliance is a notable gap (analyst observation).

## Deployment evidence & traction
No verified customer deployment, pilot or shipped unit found (searched German and English sources, Aug 2026) — trade-fair demos only: Automatica June 2025 (beverage service), IFA Sept 2025 (tidying a child's room), CES 2026 (dishwasher unloading, health monitoring) [S2][S5][S6]. NEURA's head of engineering claimed at IFA 2025 that its robots (plural, referring to the platform range) "are already being used in enterprise settings" — no MiPA-specific customer has ever been named (vendor-claimed, unverified) [S5]. Reservation volume: not disclosed. Timeline slippage is documented: The Robot Report (June 2025) relayed deliveries planned for 2025 [S1]; the current vendor FAQ says "late 2026 release" and that reservation holders will receive status updates "before release in 2026" [S4]. Confidence: the robot is real and demos exist (third-party observed), but shipping status = not shipping, deployments = none verified.

## Assessment (analyst view)
*Analyst opinion.* Strengths: unmatched price signal (€9,999 vs $70-90k US/CN peers), German engineering brand, deep-pocketed strategics (Bosch, Schaeffler, Qualcomm, Amazon, EIB) and a coherent ecosystem story (Neuraverse skills + NEURA Gym data engine) that could compound if third-party developers actually arrive. Weaknesses: chronic gap between announcements and delivery — market launch was declared in June 2025 yet a year later there is no shipped unit, no named MiPA customer, no published spec sheet with height/weight/reach, and no safety certification for a robot supposedly entering homes; the €9,999 price is plausibly a loss-leader reservation-builder rather than a sustainable price. For a new EU entrant the threat is high in narrative and fundraising competition (NEURA soaks up German talent, strategic partners and press), but currently low in the field: there is no deployed MiPA fleet to displace. The main risk is timing — if MiPA ships even semi-competently in late 2026 at anywhere near €10k, it resets EU customer price expectations for the entire category.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.therobotreport.com/neura-robotics-launches-latest-cognitive-robots-neuraverse-ecosystem/ | Automatica 2025 launch, reservations open, 2025 delivery claim, care/wearable integration | third-party |
| 2 | https://neura-robotics.com/neura-robotics-launches-technological-revolution/ | June 24 2025 PR: "market launch of the world's first cognitive household and service robot MiPA" | vendor-claimed |
| 3 | https://neura-robotics.com/products/mipa/ | Body components (linear axis, actuated wheels, LiDAR, sensors, projector), modular attachments, open APIs, white-label, human detection 3 m, Wi-Fi/5G/Matter | vendor-claimed |
| 4 | https://neura-robotics.com/product/mipa-reservation/ | €9,999 / €100 reservation, MiPA Home only, 16 DoF manipulation, late-2026 release FAQ | vendor-claimed |
| 5 | https://www.bgr.com/1961409/ifa-2025-neura-humanoid-robots/ | IFA 2025 MiPA demo (tidying plushies), "wheeled mobile manipulation platform", enterprise-use claim | third-party |
| 6 | https://humanoza.com/robots/neura-mipa | CES 2026 demos, no confirmed shipping, teleop caveats, 5 kg/arm estimate (conflicts with datasheet), no consumer deployment | third-party |
| 7 | https://neurarobotics.px.media/plk/7D/MiPA_NEURA_Robotics_Datasheet_Web.pdf | Datasheet V5 (05.06.2026): 17 DoF, 3 kg single-arm payload, 2-8 h endurance, auto recharge, 360° perception, LLM/CV/RL, NEURA Gym | vendor-claimed |
| 8 | https://neura-robotics.com/series-c/ | Qualcomm compute/connectivity partnership context | vendor-claimed |
