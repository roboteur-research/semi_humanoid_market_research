# TIAGo Pro — PAL Robotics

> TIAGo Pro is PAL Robotics' flagship dual-arm wheeled semi-humanoid: an omnidirectional (4x mecanum) mobile manipulator with a 35 cm lifting torso, two fully torque-controlled 7-DoF series-elastic (SEA) arms (3 kg each), and an expressive HRI head with face touchscreen. Announced mid-2023 as the successor-tier platform above the classic TIAGo, it targets research labs and early industrial/embodied-AI users and is PAL's competitive answer to the new generation of wheeled humanoid manipulation platforms — fully ROS 2-native, EtherCAT-based, and already field-tested in EU industrial pilots (CO-HAND textile, TRL 7). [S1][S2][S3][S6]

| Field | Value |
|---|---|
| Company | PAL Robotics (Barcelona, Spain) |
| HQ | Barcelona, Spain |
| Status (2026) | shipping (quote-based) [S1] |
| First shown / launch | Announced ~May/June 2023 ("TIAGo Pro Edition"); current edition marketed 2024-2026 [S2] |
| Target applications | Research (mobile manipulation, HRI, embodied AI), industry, agrifood, healthcare, logistics, retail, education [S1] |
| Price | n/a (not disclosed; quote-based). Reportedly ~USD 85-95k in market chatter — unconfirmed (estimated) |
| Availability | Global, direct from PAL via "Request a Quote"; lead time not disclosed [S1] |

## Design & morphology
Wheeled omnidirectional base (4x mecanum, 4 DoF) + 1-DoF prismatic lifting torso (35 cm stroke) + two 7-DoF arms + 2-DoF pan/tilt head. Height 120-155 cm (torso-dependent), weight 80 kg, footprint 50 x 72 cm, total workspace 7 m³, 23 DoF including default grippers. [S3, datasheet — all vendor-claimed]

## Locomotion
Omnidirectional drive via 4 mecanum wheels ("4 DoF" per vendor); indoor use. Max speed not disclosed (n/a). Safety brakes at joint level; emergency stop button. [S1][S3]

## Upper body & manipulation
Two 7-DoF arms with series-elastic actuation: joint-level torque sensing "on each arm actuator", 6x safety brakes per arm at joint level, 1 kHz EtherCAT communication bus, impedance control and gravity compensation; arms "absorb energy upon impact" [S1][S3][S4]. Payload 3 kg per arm (extended, excluding end-effector); vertical reach 92 cm; horizontal reach 236 cm (dual-arm span); the SEA arm itself has ~96 cm extended reach with ISO 9409-1 flange [S3][S4]. New shoulder placement enlarges the common bimanual workspace and enables floor-to-high-shelf reach [S2]. End-effectors: 2x PAL parallel grippers standard, quick tool changer, optional Allegro Hand (16 DoF) with 4x Xela fingertip tactile sensors, optional 6-axis wrist F/T sensors [S1][S3]. Repeatability not stated (n/a).

## Sensing
Head: RGB-D camera, 4-microphone array, 2x 4W speakers, 10-inch face touchscreen, RGB LEDs; expressive eyes/emotions with gaze direction [S1][S2]. Base: 2x LiDAR (laser range finders), 10 m range, 360° combined FoV (25 m upgrade) [S1][S3]. Arms: joint torque sensors; optional wrist F/T; tactile fingertips with Allegro hand [S1][S3]. ROS4HRI perception stack: 2D/3D skeleton tracking, 6D head pose, facial landmarks, gaze tracking, face ID, probabilistic person fusion [S2].

## Actuation & power
Series Elastic Actuators in arms (torque control at joint level); brakes in arms and torso [S2][S4]. Battery capacity not disclosed (n/a); autonomy 8 h (vendor datasheet); optional additional battery and dock charging station [S3]. Expansion: 2x USB 3, 1x HDMI, 2x Ethernet, 36V/5A + 12V/8A power outputs, detachable laptop tray [S3].

## Compute & software
Standard: Intel i5, 16 GB RAM, 512 GB SSD; upgrades: i7/32 GB/1 TB and an additional NVIDIA Jetson PC [S1][S3]. Connectivity: Wi-Fi 6, Bluetooth 5.2, WireGuard VPN [S3]. Software: Ubuntu LTS with PREEMPT-RT, ROS 2 native, ros2_control, MoveIt 2, Nav2, navigation stack + motion library included, PAL Web GUI ("Web Commander"), Docker image with PAL SDK, RViz plugins, MuJoCo and Gazebo simulator support [S1][S3]. HRI software: offline ASR in 20+ languages, chatbot engine, TTS with gesture markup, automatic subtitling, optional wake-word [S2]. NVIDIA collaboration (Oct 2025) adds Isaac Sim/Isaac Lab RL training and VR-teleop data-collection workflows across PAL platforms [S7].

## Safety & compliance
Vendor-claimed safety features: energy-absorbing SEA arms, joint-level brakes (6x/arm + torso), emergency stop button, torque sensing for collision-aware control [S1][S3]. No CE declaration, ISO 13482 or ISO/TS 15066 certification publicly stated for TIAGo Pro (n/a, not disclosed) — typical for research-platform sales where the integrator carries conformity. GDPR-conscious edge processing inherited from PAL's HRI stack [S2].

## Deployment evidence & traction
- CO-HAND EU project: TIAGo Pro validated at TRL 7 in real textile-manufacturing environments (vendor blog, 2026) — includes deployment photos of the robot handling yarn bobbins [S6]. (vendor-claimed)
- ROSALYA EU project: mobile manipulation in food industry [S1]. (vendor-claimed)
- euROBIN network platform; research early adopters across EU labs [company S12]. (vendor-claimed)
- No public unit counts, industrial customers or RaaS deals disclosed (n/a). (analyst note)

## Assessment (analyst view)
*Analyst opinion.* TIAGo Pro is the most credible European wheeled semi-humanoid for collaborative mobile manipulation today: torque-controlled SEA arms with joint brakes, 1 kHz EtherCAT, ROS 2-native stack and a genuinely strong HRI layer (ROS4HRI is effectively PAL's standard) — capabilities Chinese rivals rarely match in safety-relevant compliance control. Weaknesses: undisclosed pricing and speed specs, 3 kg per-arm payload at the low end for intralogistics, no published certification path, and PAL's research-first go-to-market that has historically capped volumes at tens of units per year. For a German entrant, TIAGo Pro defines the domestic benchmark for "safe dual-arm mobile manipulator with EU credibility"; beating it requires either meaningfully higher payload/speed at industrial price points or a certified turnkey application. Threat level: high in EU research procurement, moderate in industry — PAL is just beginning its own industrial transition and the CO-HAND TRL 7 milestone shows it is moving. 

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://pal-robotics.com/robot/tiago-pro/ | Full spec set, options, applications, quote-based sales | vendor-claimed |
| 2 | https://www.automatedwarehouseonline.com/pal-robotics-introduces-tiago-pro-edition-mobile-manipulator/ | Launch (article dated Jun 1, 2023), SEA torque-control arms, EtherCAT, arm placement, ROS4HRI/HRI features | third-party |
| 3 | https://pal-robotics.com/datasheet/tiago-pro/ (PDF) | Height 120-155 cm, 80 kg, 50x72 cm, 8 h autonomy, 7 m³ workspace, 23 DoF, 35 cm torso, reaches, compute, ports | vendor-claimed |
| 4 | https://pal-robotics.com/blog/introducing-new-tiago-sea-arm/ | SEA arm: 7 DoF, 96 cm reach, brakes, 1 kHz EtherCAT, ISO 9409-1 flange, impedance control, CANOPIES origin (Sept 2023) | vendor-claimed |
| 5 | https://pal-robotics.com/robot/tiago/ | Family context, TIAGo baseline | vendor-claimed |
| 6 | https://pal-robotics.com/blog/pal-robotics-in-co-hand-project/ | TRL 7 validation in textile manufacturing | vendor-claimed |
| 7 | https://pal-robotics.com/blog/pal-robotics-and-nvidia-shaping-the-next-generation-of-robotics/ | NVIDIA Isaac Sim/Lab + VR teleop collaboration (Oct 2025) | vendor-claimed |

*Price note: the ~USD 85-95k figure circulating in discovery notes could not be confirmed against any citable source this session; treat as estimated/unverified.*
