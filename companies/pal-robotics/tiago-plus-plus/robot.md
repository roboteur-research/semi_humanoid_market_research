# TIAGo++ / TIAGo OMNI++ — PAL Robotics

> TIAGo++ is the dual-arm configuration of PAL Robotics' modular TIAGo mobile-manipulator family (single/dual/no-arm, differential or omnidirectional base, lifting torso): two 7-DoF arms with 3 kg payload each on a wheeled base with a 35 cm torso lift. Launched 2019 (TIAGo++, diff-drive) and refreshed 2021 as TIAGo OMNI++ with a 4-mecanum omnidirectional base, it is *the* workhorse dual-arm research platform of European robotics — deployed in 14+ EU countries and 27 countries worldwide, backbone of dozens of Horizon projects and RoboCup@Home wins. Competitively it matters as the installed-base anchor that keeps EU labs (and their graduates) inside PAL's ecosystem. [S1][S2][S3][S4]

| Field | Value |
|---|---|
| Company | PAL Robotics (Barcelona, Spain) |
| HQ | Barcelona, Spain |
| Status (2026) | shipping [S1] |
| First shown / launch | TIAGo base platform 2015; TIAGo++ dual-arm June 2019; TIAGo OMNI++ Nov 2021 [S2][S3] |
| Target applications | Academic/industrial research: mobile manipulation, bi-manipulation, HRI, AI/ML, healthcare & assisted living, agrifood, robotics competitions [S1][S2] |
| Price | TIAGo++ from ~EUR 90,000 (2019, config-dependent) [S3]; single-arm TIAGo lower; current pricing quote-based (n/a) |
| Availability | Global, direct quote-based sale (+ research distributors); free simulation (ROS/Gazebo) before purchase [S1][S2] |

## Design & morphology
Modular columnar semi-humanoid on a wheeled base: height 110-145 cm (35 cm prismatic torso lift), footprint ø54 cm (diff-drive base), weight ~70 kg (vendor datasheet baseline; dual-arm configs heavier — estimated). DoF: 2x7 arms + 1 torso + 2 head + 2 base = 19 (dual-arm, before end-effectors); gripper adds 2 DoF, Hey5 hand 19 DoF (3 actuated). [S1 datasheet, S5]

## Locomotion
Differential drive (classic TIAGo/++) or omnidirectional 4x mecanum drive (OMNI / OMNI++, 2021); max speed 1.5 m/s (datasheet; older third-party figure 3.6 km/h = 1.0 m/s), indoor environments. [S1][S3][S5]

## Upper body & manipulation
Two modular 7-DoF arms; payload 3 kg per arm at full extension (without end-effector); arm reach 87 cm (standard arm; new SEA arm option 96 cm). Torque-controllable joints: standard arm with current-based sensorless torque control + optional 6-axis wrist F/T sensor (admittance control); since 2023 an SEA arm option with joint torque sensing, brakes and 1 kHz EtherCAT (developed in CANOPIES, standard on TIAGo Pro). End-effectors: PAL parallel gripper (default), PAL Hey5 five-finger hand, Robotiq 2F-85 / 2F-140, ePick vacuum; interchangeable, plug-and-play. [S1][S4][S6]

## Sensing
Base laser (Hokuyo 5.6 m or SICK TiM561 10 m / 25 m options), 3x rear sonars (1 m), IMU, actuator current feedback; head RGB-D camera; 2x microphone array, 2x 5 W speakers; optional wrist F/T; mounting points on head, laptop tray and base for user sensors. [S1 datasheet]

## Actuation & power
Brushless/brushed DC motors (robotsguide: 9 brushless + 8 brushed on single-arm config); optional SEA arm. Battery 36 V 20 Ah (~0.72 kWh); 4-5 h on one battery, 8-10 h with second battery; hot-swap not stated; charger + optional dock. [S1][S5]

## Compute & software
Intel i5 (8 GB/250 GB) standard, i7 (16 GB/500 GB) upgrade, optional NVIDIA Jetson (TX2 historically; current Jetson offered as add-on). Ubuntu LTS with RT-Preempt, ROS LTS (Noetic) with full ROS 2 migration underway — PAL continuously releases TIAGo packages into ROS 2 Humble; open-source Gazebo simulation, URDF, MoveIt, ros_control, Whole Body Control, Advanced Grasping premium package, web-based visual programming. Wi-Fi 6, Bluetooth. [S1][S5][S7]

## Safety & compliance
Research platform: e-stop, torque/current-limited arms, admittance control with F/T sensor, joint brakes (SEA option). No public CE/ISO 13482 certification statement for the manipulator platform (n/a, not disclosed); PAL participated in the Assuring Autonomy International Programme (safety research). [S1]

## Deployment evidence & traction
- Vendor: "over 9 years in the market, 40 collaborative projects, 14 EU countries, 27 countries worldwide, 120 citations" (TIAGo family) [S1]. (vendor-claimed)
- RoboCup@Home: Homer Team (Koblenz) won 2019 with TIAGo (third consecutive title); CATIE Robotics 3rd in OPL 2019; SciRoc challenge loans [S3]. (third-party)
- EU projects using TIAGo/++: EnrichMe (assisted living), OpenDR, CANOPIES (vineyard co-work), CO-HAND lineage, many more [S2][S6]. (vendor-claimed)
- Hospital logistics spin-offs (TIAGo Delivery/Conveyor at Hospital Municipal de Badalona and Hospital Clinic Barcelona, 2020) built on the TIAGo Base [company S16]. (vendor-claimed)
- Unit counts not disclosed; installed base plausibly in the hundreds across EU labs (estimated).

## Assessment (analyst view)
*Analyst opinion.* TIAGo++'s strength is ecosystem gravity: a decade of ROS tutorials, open simulation, EU-project integration and competition presence means every European robotics lab knows it, and procurement favors it. Hardware is now mid-life — 3 kg arms, 1.5 m/s, aging sensor loadout — and clearly outclassed by TIAGo Pro and newer Chinese wheeled humanoids on actuation and compute, which is why PAL positions it as the affordable research entry (~EUR 90k dual-arm in 2019; the "€50k-class" reputation applies to single-arm configs). For a German entrant the lesson is dual: (1) the research channel is defensible and sticky but small; (2) TIAGo's openness (free sim, ROS-first, modular EEs) is the playbook that built loyalty — a new industrial platform that ignores this loses the talent pipeline. Direct threat to a commercial semi-humanoid entrant: moderate-low; threat as incumbent mindshare in EU: high.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://pal-robotics.com/robot/tiago/ (+ https://pal-robotics.com/datasheet/tiago/ PDF) | Full family specs: 110-145 cm, 70 kg, ø54 cm, 3 kg arm payload, 87 cm reach, 35 cm lift, 1.5 m/s, 36V 20Ah battery, 4-10 h, sensors, compute, LITE/TIAGo/++ config matrix | vendor-claimed |
| 2 | https://www.automatedwarehouseonline.com/pal-robotics-launches-tiago-omni-mobile-manipulation-robot/ | TIAGo OMNI++ launch Nov 2021: mecanum omnidrive, dual 7-DoF arms, 2x LiDAR 360°, quotes (Jordi Pages, TIAGo product manager), TIAGo history since 2015 | third-party |
| 3 | https://www.therobotreport.com/tiago-robot-pal-robotics-ready-two-armed-tasks/ | TIAGo++ launch June 2019, from EUR 90,000, 92 cm reach, floor-to-1.75 m workspace, Jetson TX2 option, RoboCup results | third-party |
| 4 | https://pal-robotics.com/blog/introducing-new-tiago-sea-arm/ | SEA arm option (2023): 96 cm reach, torque sensing, brakes, EtherCAT, ISO 9409-1 | vendor-claimed |
| 5 | https://robotsguide.com/robots/tiago | Third-party specs: 70 kg, 110/145 cm, 3.6 km/h, actuator count, 12 DoF single-arm breakdown, Hey5 hand 19 DoF/3 actuated | third-party |
| 6 | https://www.automatedwarehouseonline.com/pal-robotics-launches-tiago-omni-mobile-manipulation-robot/ | EU projects EnrichMe, OpenDR, CANOPIES using TIAGo | third-party |
| 7 | https://discourse.ros.org/search.json?q=tiago | Active TIAGo package releases into ROS 2 Humble (2025-26) | third-party |

*Unknowns: dual-arm config weight (estimated ~75-85 kg), certification status, unit counts, current list prices — all n/a (not disclosed).*
