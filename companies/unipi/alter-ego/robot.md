# Alter-Ego / Alter-Ego X — Univ. Pisa Centro Piaggio + IIT SoftBots

> Alter-Ego is a ~1.2 m two-wheel self-balancing semi-humanoid built on soft-robotics principles: variable-stiffness "artificial muscle" arms and Pisa/IIT SoftHands make it intrinsically compliant and light. Alter-Ego X hardened the design for the ANA Avatar XPRIZE, and the platform now runs a pilot clinical avatar study at IRCCS Maugeri Milan (Fit4MedRob) for ALS/neurodegenerative care. Competitively it is the European reference for the "soft, teleoperated care avatar" concept rather than a product.

| Field | Value |
|---|---|
| Company | Univ. Pisa Centro Piaggio + IIT SoftBots (team AlterEgo) |
| HQ | Pisa / Genoa, Italy |
| Status (2026) | research (active; clinical pilot at Maugeri Milan) |
| First shown / launch | Alter-Ego paper 2019; Alter-Ego X ~2022 (ANA Avatar XPRIZE finals Nov 2022) |
| Target applications | Hospital/home-care telepresence avatar (ALS, neurodegenerative disease), physical HRI research |
| Price | n/a (not for sale) |
| Availability | Not available; lab-built research units |

## Design & morphology
~120 cm tall humanoid upper body on a two-wheeled, dynamically self-balancing base (inverted-pendulum, Segway-like) [S1][S2]. Lightweight soft design: arm modules are variable-stiffness actuators (VSA, qbmove lineage) reproducing muscle-like elasticity; anthropomorphic layout with pan-tilt head (+2 VSA DoF) [S2][S3]. Exact weight not published (lightweight, est. 20-40 kg class) (estimated).

## Locomotion
Two-wheel self-balancing drive; requires active stabilization (LQR-type pitch control) [S2]. Speed not published. Flat indoor floors; balancing base gives a very small footprint and human-like maneuverability at the cost of standing stability guarantees.

## Upper body & manipulation
Two compliant arms (~5-6 DoF each, VSA-driven; exact count varies by generation — original paper: 5 DoF per arm) [S2]. End effectors: Pisa/IIT SoftHand on each arm — 5 fingers, 19 joints, single actuator (synergy-based underactuation), 0.29 kg, 130 mm; adaptive grasping of objects and door handles without per-finger control [S3]. Payload not published (SoftHand grasps everyday objects; low single-kg class, estimated). Variable stiffness allows safe physical contact and impact robustness.

## Sensing
Head: double stereoscopic vision (ZED-Mini stereo camera), pan-tilt; microphones and speakers for verbal interaction [S3]. Body: tilt sensors, accelerometers, gyroscopes (balancing), proximity sensors [S1][S3]. No lidar disclosed.

## Actuation & power
Variable Stiffness Actuators (qbmove-class series-elastic/antagonistic units) in arms and neck; wheel drives; battery onboard (capacity/runtime n/a, not disclosed) [S2][S3].

## Compute & software
Intel NUC mini-PCs (Linux) integrated in the body [S3]. Modes: full teleoperation (VR headset + joysticks for clinician embodiment), semi-autonomous, autonomous [S1]. Pilot-side avatar interface developed for ANA Avatar XPRIZE (immersive visual/audio, haptic feedback via hand interface) [S3]. Software stack ROS-based (research code); no commercial SDK.

## Safety & compliance
No certification (research). Safety philosophy is intrinsic: low mass, soft VSA actuation, adaptive hands — "safe by design" physical interaction [S2]. Two-wheel balancing introduces a fall-risk failure mode that would need addressing for any certified care deployment (analyst note).

## Deployment evidence & traction
Pilot clinical study at IRCCS Maugeri Milan (Fit4MedRob, Italy's PNRR): patient welcome/guidance, information, pain-assessment administration, accompanying patients, and clinician telepresence follow-up incl. home-care support — with named clinical leads (Lunetta, Piras) [S1, vendor-claimed]. ANA Avatar XPRIZE: team AlterEgo competed at the Long Beach finals (Nov 2022) with Alter-Ego X [S3]. Usability studies published 2024 [S4]. No commercial customers (n/a).

## Assessment (analyst view)
(Analyst opinion.) Strengths: genuinely differentiated soft-actuation stack (VSA + SoftHand — the hand is commercially available via qbrobotics); lightest-touch safety story in the segment; real hospital pilot with a major rehab network; avatar/teleop maturity from XPRIZE. Weaknesses: two-wheel balancing is hard to certify and limits payload; no whole-robot commercialization path; specs sparsely published. Threat to a new EU entrant: minimal directly; the component technologies and the Maugeri clinical-avatar playbook are the assets to watch (or license). If a company productized Alter-Ego's concept with a statically stable base, it would compete in eldercare telepresence against Devanthro-style offerings.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.unipi.it/en/news/alter-ego-bring-robotics-into-hospital-wards/ | 120 cm, two wheels, modes, Maugeri Milan pilot, tasks, Fit4MedRob | vendor-claimed (university press) |
| 2 | https://arpi.unipi.it/retrieve/e0d6c92f-c47d-fcf8-e053-d805fe0aa794/EGO_RAM_2019.pdf | Original design: VSA arms, self-balancing, functional anthropomorphism | vendor-claimed (peer-reviewed) |
| 3 | https://www.ais.uni-bonn.de/ICRA2023AvatarWS/contributions/ICRA_2023_Avatar_WS_Zambella.pdf | Alter-Ego X: XPRIZE, SoftHand 19 DoF/1 DoA/0.29 kg/130 mm, ZED-Mini, Intel NUCs, head VSA pan-tilt | vendor-claimed (workshop paper) |
| 4 | https://www.researchgate.net/publication/386022096_Usability_of_a_Robot_Avatar_Designed_for_the_Real_World_The_Alter-Ego_X_Case_Study | Alter-Ego X real-world usability evaluation | third-party |
