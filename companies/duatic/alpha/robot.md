# Alpha — Duatic AG

> Alpha is a "vision-enabled half-humanoid": two of Duatic's lightweight quasi-direct-drive DynaArms mounted on a mecanum-wheeled mobile base, aimed at research, automation and industrial/intralogistics applications. It matters competitively because it packages ETH-RSL-grade dynamic manipulation (backdrivable QDD joints, 30 kg peak lift, IP66, hot-swap 48 V batteries, native ROS 2) into a Swiss-made platform — exactly the formula a new EU semi-humanoid entrant would pursue, from a team with ANYmal/ALMA lineage.

| Field | Value |
|---|---|
| Company | Duatic AG |
| HQ | Zürich, Switzerland |
| Status (2026) | prototype (early demos/units; research + industrial pilots) |
| First shown | 2024–2025 (company inc. 2024-04-26; LogiMAT 2026 appearance reported but unverified) |
| Target applications | research platforms, intralogistics, floor-to-shelf object handling, industrial automation |
| Price | n/a (not disclosed); humanoid.guide estimates USD 150k [S4, estimated] |
| Availability | direct from vendor; no published lead times; research customers first |

## Design & morphology
Half-humanoid torso with two DynaArms on a low-slung four-wheeled mobile base (yellow mecanum wheels visible in official renders), with a sensor/screen head unit and grab handles [S1, images]. No legs; torso appears fixed on the base pedestal (no lift column disclosed — modular design "allows various configurations", vendor-claimed) [S1]. Height/weight not officially published; humanoid.guide lists 175 cm / 90 kg / 19 DoF total (estimated, unverified) [S4]. Vendor emphasizes modularity and IP66 protection for the whole platform [S1].

## Locomotion
Mecanum omnidirectional wheels (visible in renders); max platform speed 2 m/s (vendor-claimed) [S1]. Terrain/climbing limits n/a (not disclosed). IP66 rating suggests washdown/dusty industrial environments [S1].

## Upper body & manipulation
Two DynaArm manipulators: per-arm reach 0.990 m; arm mass 9.2 kg; standalone DynaArm payload 6 kg continuous / 12 kg for 10 s [S2]. As a dual-arm system Alpha is rated 12 kg continuous / 30 kg peak (10 s) payload, with marketing claims of "30 kg lift & 200 kg carry" (carry = pushing/supporting load via base) [S1]. End-effector speed up to 10 m/s (DynaArm, vendor-claimed) [S2]. Arms are carbon-fiber-tubed, highly backdrivable QDD designs derived from ETH RSL work (ALMA/ANYmal manipulation) [S3]. End-effector: modular flange; demo shows a jaw-type gripper lifting a 20 kg bag autonomously (vendor video) [S1][S5]. Media at flange n/a (not disclosed). Repeatability not stated; joint torque accuracy ±0.5 Nm (vendor-claimed) [S2].

## Sensing
"Vision-enabled" with real-time AI-driven decision-making; head unit contains cameras plus what appears to be a depth sensor bar; base carries a small lidar puck (visible in render) [S1, images]. Detailed sensor list n/a (not disclosed). Joint-torque sensing implicit in QDD design with ±0.5 Nm torque accuracy [S2].

## Actuation & power
DynaDrive QDD actuator family: Armadillo (wrist, high transparency/accurate torque), Baboon (60 Nm peak / 27 Nm nominal — used for ANYmal hips/knees), Coyote (same torque class, wheel drive); 48 V, 32 A peak, 930 W max, integrated 6D IMU, EtherCAT [S3]. Platform: 48 V DC, hot-swappable batteries for claimed 24/7 operation [S1]. Battery capacity kWh and runtime n/a (not disclosed); humanoid.guide estimates 8 h (estimated) [S4].

## Compute & software
Native ROS 2 control with open API; no external control box for arms [S1][S2]. Open-source ROS 2 driver on GitHub (dynaarm_driver, ros2_control based) [S6]. Compute n/a officially; humanoid.guide lists NVIDIA Jetson AGX (estimated) [S4]. AI: vendor claims vision-based real-time decision-making and ML-driven manipulation; no VLA model named [S1].

## Safety & compliance
No certifications published (no ISO 13482 / TS 15066 claims found). Backdrivable QDD actuation and torque control support collision-tolerant operation (analyst inference). E-stop visible on base in renders. IP66 ingress protection (vendor-claimed) [S1].

## Deployment evidence & traction
No named customers or unit counts. Evidence base: official demo video of autonomous 20 kg bag lift [S1]; DynaArm demos on ANYmal and Festo BionicMobileAssistant (pre-spin-off) [S5]; open ROS 2 drivers with community engagement on ROS Discourse [S6]; reported LogiMAT 2026 exhibit (unverified) [S7]. Overall: prototype/demo stage, research-platform sales likely first revenue. Confidence: third-party evidence thin.

## Assessment (analyst view)
*Analyst opinion.* Strengths: world-class actuation pedigree (ETH RSL/ANYmal), genuinely differentiated lightweight dynamic arms (9.2 kg arm lifting 12 kg peak is an exceptional payload-to-mass ratio), IP66, hot-swap power, and an open ROS 2 stack that will win research mindshare. Weaknesses: tiny funding (CHF 50k Venture Kick), no disclosed pricing, customers, or certifications; manipulation autonomy stack appears immature relative to hardware. For a new EU entrant, Duatic is the closest European technical rival in the wheeled dual-arm class and a possible component supplier (arms/actuators) or acquisition target as much as a competitor; near-term threat moderate, rising if it lands VC funding and intralogistics pilots in 2026-27.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.duatic.com/alpha | Alpha specs, features, demo | vendor-claimed |
| 2 | https://www.duatic.com/dynaarm | DynaArm specs | vendor-claimed |
| 3 | https://rsl.ethz.ch/robots-media/actuators/DynaDrives.html | DynaDrive actuators, ANYmal lineage | third-party (academic) |
| 4 | https://humanoid.guide/product/duatic-alpha/ | est. height/weight/DoF/price | estimated (third-party aggregator) |
| 5 | https://www.duatic.com/about-us | ANYmal/Festo demos | vendor-claimed |
| 6 | https://github.com/Duatic/dynaarm_driver/ + ROS Discourse announcement | open software stack | third-party |
| 7 | LinkedIn mention via search (LogiMAT 2026) | trade-show presence | estimated (unverified) |
