# Rollin' Justin — DLR Institute of Robotics and Mechatronics

> Rollin' Justin is DLR's flagship wheeled semi-humanoid research platform: a 1.91 m, ~200 kg torque-controlled bimanual robot on a four-wheeled sprawling base, built from the LWR-III lightweight arms and DLR Hand II four-finger hands. It is not a product, but since 2008 it has been the European reference system for compliant bimanual mobile manipulation and shared-autonomy space telerobotics (METERON SUPVIS 2017, Surface Avatar 2023-2025), and its technology lineage (torque control, compliant arms) flows directly into KUKA iiwa, Franka Emika and Agile Robots.

| Field | Value |
|---|---|
| Company | DLR Institute of Robotics and Mechatronics (RMC) |
| HQ | Oberpfaffenhofen/Weßling, Germany |
| Status (2026) | research (active; one-off platform, ~18 years in service) |
| First shown / launch | Torso "Justin" 2006; Rollin' Justin public debut 2008; Agile Justin variant 2012 [S1][S2] |
| Target applications | Research: household/service mobile manipulation, on-orbit servicing, planetary-surface telerobotics from orbit |
| Price | n/a (not for sale) |
| Availability | Not available; internal DLR research platform |

## Design & morphology
Height 1.91 m, weight ~200 kg, workspace floor to 2.7 m [S1, vendor-claimed]. 51 total DoF: mobile platform 8 (4 wheels, each steered + extensible legs), torso 3, arms 2×7, hands 2×12, neck 2 [S1]. Anthropomorphic upper body on a distinctive four-legged "sprawling" wheeled base whose legs can extend outward for stability or retract to pass doorways — footprint is variable. Nominal load capacity 20 kg [S1].

## Locomotion
Four independently steered, spring-suspended wheels on extensible legs (8 platform DoF); max speed 2 m/s [S1, vendor-claimed]. Indoor, flat-floor operation; the variable-footprint base trades stability against confined-space mobility. Battery operation >60 min untethered [S1].

## Upper body & manipulation
Two DLR LWR-III torque-controlled carbon-fiber lightweight arms, 7 DoF each, ~14 kg per arm class, payload roughly equal to arm mass (~14-15 kg per arm; Wikipedia cites ~31 lb/arm) [S1][S2, third-party]. 3-DoF torso adds reach envelope. Two DLR Hand II four-finger hands, 12 DoF each, with fingertip torque sensing — dexterous, ambidextrous manipulation (unscrewing thermos flasks, making coffee, tool use) [S1]. Famous dynamic capability: catching thrown balls with ~80% success (whole-body catch planning at ms rates); Agile Justin (2012 upgrade) has ~1.5x faster arms and can also throw [S2, third-party]. No tool changer / media at flange (research hands).

## Sensing
Head: 2 stereo camera pairs plus RGB-D; institute lists 2 stereo cameras and 5 RGB-D cameras total across the system; earlier 3DMo sensor head combined stereo, laser-stripe sensor and IMU [S1][S2]. Joint torque sensors in nearly all joints (41 link-side torque sensors), 2 IMUs for balance/state estimation [S1][S2]. Whole-body compliance and collision detection come from joint torque sensing rather than skins.

## Actuation & power
Harmonic-drive joints with motor-side position and link-side torque sensing (LWR-III technology — the same base licensed to KUKA for the LBR iiwa) [S1][S2, third-party]. Battery-powered, runtime >60 min [S1, vendor-claimed]; hot-swap/charging dock n/a (not disclosed).

## Compute & software
Onboard computers in the base (details not publicly itemized; historically multiple x86 boards + FPGA/real-time buses; Agile Justin added a new bus architecture) [S2]. Control via torque-level whole-body controllers; programming historically via Matlab/Simulink real-time toolchain; operator interfaces include force-feedback exoskeleton teleoperation, tablet task-level UI, and the scalable-autonomy command stack used from the ISS (object-centered task-level commands with local autonomy) [S2][S3]. Not ROS-based as primary stack (DLR in-house middleware); no public SDK.

## Safety & compliance
Research platform — no ISO 13482/10218 certification (n/a, not applicable). Intrinsic safety approach via joint torque sensing, impedance control and collision reaction, the paradigm DLR later brought into cobot standards work [estimated from S1/S2].

## Deployment evidence & traction
No commercial deployments (research). Traction = scientific missions: METERON SUPVIS-Justin — astronaut Paolo Nespoli commanded Justin from the ISS in 2017 [S2]; Surface Avatar (DLR+ESA, 4 sessions 2023-2025) — ISS astronauts Frank Rubio (2023), Tracy Dyson & Jeanette Epps (2024), Jonny Kim (2025, final phase) teleoperated a robot team incl. Rollin' Justin and ESA's Spot in a simulated Mars environment at Oberpfaffenhofen, concluding the campaign successfully in 2025 [S3][S4, vendor-claimed]. Hundreds of publications; catching/coffee demos widely covered by press since 2011 [third-party].

## Assessment (analyst view)
(Analyst opinion.) Strengths: unmatched torque-controlled whole-body manipulation pedigree; nearly two decades of continuous development; the definitive proof point that wheeled bases + compliant arms deliver humanoid-level manipulation without legs. Weaknesses: one-off, heavy (~200 kg), expensive research hardware with no path to sale; core hardware (LWR-III, Hand II) is now a generation old. Threat to a new EU entrant: zero as a competitor, high as a benchmark — investors and customers in Germany will compare any semi-humanoid's compliance/manipulation story against DLR demos. Opportunity: DLR is a licensing, talent and credibility partner; its alumni companies (Agile Robots, Franka lineage) are the real competitive spillover.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.dlr.de/en/rm/research/robotic-systems/humanoids/rollin-justin | Specs: 1.91 m, ~200 kg, 51 DoF, 2 m/s, 20 kg load, sensors, >60 min battery, 2008 debut | vendor-claimed |
| 2 | https://en.wikipedia.org/wiki/Justin_(robot) | Timeline, Agile Justin 2012, catching 80%, arm payload, sensors, SUPVIS 2017, control interfaces | third-party |
| 3 | https://www.dlr.de/en/latest/news/2025/marching-towards-mars-iss-robot-experiment-surface-avatar-successfully-concludes | Surface Avatar final phase 2025, Jonny Kim, campaign conclusion | vendor-claimed |
| 4 | https://www.dlr.de/en/latest/news/2023/03/surface-avatar-an-astronaut-on-board-the-iss-controls-a-robot-team-on-earth | Surface Avatar 2023 start, Frank Rubio, lander unloading/seismometer task | vendor-claimed |
