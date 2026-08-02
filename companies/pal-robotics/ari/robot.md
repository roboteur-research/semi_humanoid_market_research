# ARI — PAL Robotics

> ARI is PAL Robotics' 1.65 m social semi-humanoid: a differential-drive wheeled platform with humanoid torso, two 5-DoF gestural (non-manipulation) arms, expressive LCD eyes, and a 10.1-inch torso touchscreen. Introduced in December 2019 as an HRI/AI research and front-desk robot, it became Europe's reference socially-assistive humanoid through the H2020 SPRING project (7 units in a Paris gerontology hospital, 100+ patients) and spawned the ROS4HRI standard. Competitively it defines the "receptionist/guide" segment of the semi-humanoid market in Europe — strong on speech/perception software and GDPR-compliant edge processing, deliberately weak on manipulation. [S1][S2][S3]

| Field | Value |
|---|---|
| Company | PAL Robotics (Barcelona, Spain) |
| HQ | Barcelona, Spain |
| Status (2026) | shipping [S1] |
| First shown / launch | December 2019 [S4] |
| Target applications | Reception/customer assistance, events & promotion, HRI/AI research, education, healthcare (socially assistive), entertainment [S1] |
| Price | n/a (not disclosed; quote-based) [S1] |
| Availability | Global, direct quote-based sale; free ROS simulation (wiki.ros.org/Robots/ARI) [S1][S5] |

## Design & morphology
Humanoid torso on skirt-covered wheeled base: height 165 cm, width 53 cm, depth 75 cm; weight not disclosed (n/a). DoF: 2 per arm x5 (2 shoulder, 1 upper-arm, 1 elbow, 1 wrist), 2 neck, 2 base = 14 total; hands are non-actuated cosmetic/gestural. Arms are for expression and gesture, not payload manipulation (no payload rating). [S2 datasheet]

## Locomotion
Differential drive (2 DoF base), standard ROS diff-drive API; indoor. Max speed not disclosed (n/a). [S2][S5]

## Upper body & manipulation
No manipulation capability by design: 5-DoF arms perform expressive gestures (wave, point, dance); no grippers, no payload rating, no tool interface (n/a). Gesture/motion authoring via web-based motion editor. [S1][S2]

## Sensing
Head: 8 MP RGB camera (optional RGB-D upgrade); torso front Intel RealSense D435i RGB-D; optional YDLIDAR TG15 LiDAR (navigation pack); optional thermal camera; 4x digital microphone array; 2x 30 W Hi-Fi speakers; 10.1" 1200x800 capacitive touchscreen; 2x LCD eye screens with 20+ expressions; LED rings on ears (2x16 RGB) and back (40 RGB). Perception software: face detection/recognition, 3D gaze estimation, realtime 2D/3D skeleton tracking, engagement detection, sound-source localization, probabilistic multi-modal person fusion — fully ROS4HRI-integrated. [S2]

## Actuation & power
Electric servo joints for arms/neck (details not disclosed); battery 24 V 40 Ah (~0.96 kWh; 60 Ah optional), autonomy 8-12 h; additional battery charger accessory; no autonomous dock stated. [S1][S2]

## Compute & software
Intel i5 / i7 / i9, 8-32 GB RAM, up to 1 TB SSD; optional NVIDIA Jetson Xavier NX or Orin (CUDA) for AI workloads; Wi-Fi 802.11ax dual-band + Gigabit Ethernet. Ubuntu LTS with RT-Preempt kernel, ROS Noetic (ROS 1; public simulation, tutorials and full ROS API), MoveIt, ros_controllers, web GUI for content/motions/presentations, custom HTML/JS touchscreen apps with ROS-JS bridge. Speech: on-board vosk ASR (20+ languages; vendor page: 30+ languages), acapela TTS (6 languages incl. SSML), rasa-based dialogue manager with intent detection, optional Google ASR/DialogFlow (with GDPR caveat), OWL/RDF knowledge base with first-order-logic reasoner. GDPR-compliant edge processing: all data on-board, cloud opt-in only. [S1][S2][S5]

## Safety & compliance
Low-risk social platform: no manipulation forces; GDPR compliance explicitly addressed (edge processing, deletable face DB) [S2]. CE marking / ISO 13482 status not publicly stated (n/a, not disclosed). E-stop not explicitly listed on public datasheet (n/a).

## Deployment evidence & traction
- SPRING (H2020): 7 ARI robots to INRIA Grenoble, Univ. Trento, CVUT Prague, Heriot-Watt, Bar-Ilan, ERM, AP-HP; deployed at Broca gerontology day hospital (AP-HP, Paris) — reception, information, wayfinding, entertainment; tested with 100+ patients; >50 parallel software modules; project completed Oct 2024; produced the ROS4HRI open standard. [S3][S6] (vendor-claimed; EU-project documented)
- Receptionist at Ayesa (Spanish engineering firm). [S7] (vendor-claimed)
- PRO-CARED pilots: education robot practicing Catalan with students. [S8] (vendor-claimed)
- SHAPES (H2020): home-assistance pilots. [S9] (vendor-claimed)
- Cruilla music festival Barcelona 2022 (public-facing event host); met King Felipe VI at IOT Solutions World Congress; AMIBA foundation assistant. [S10] (vendor-claimed)
- No unit counts or commercial fleet numbers disclosed (n/a). Note: the "Metropolis/airport deployment" from preliminary discovery notes could NOT be verified — no airport deployment found in vendor or third-party sources this session.

## Assessment (analyst view)
*Analyst opinion.* ARI is the most software-mature European social semi-humanoid: its ROS4HRI perception stack, multilingual offline speech pipeline and GDPR-by-design posture are real differentiators for EU public-sector buyers (hospitals, municipalities) that US/Chinese rivals struggle to match. But the category itself is commercially fragile — reception robots have thin ROI, ARI cannot manipulate, and its ROS 1 (Noetic) base is aging. Deployments remain overwhelmingly EU-project-funded rather than repeat commercial purchases. For a German entrant planning manipulation-capable semi-humanoids, ARI is not a direct competitor but a warning: the social/receptionist niche alone did not scale even with flagship EU funding. Its HRI software layer, however, is licensable inspiration — pairing ARI-grade social perception with real manipulation (as PAL now attempts with TIAGo Pro's expressive head) is where the segment converges. Threat level: low-moderate, confined to HRI/public-facing tenders.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://pal-robotics.com/robot/ari/ | Dimensions, touchscreen, autonomy 8-12 h, 30+ languages, applications, add-ons | vendor-claimed |
| 2 | https://pal-robotics.com/datasheet/ari/ (PDF, 5 pages) | DoF breakdown (5/arm, 2 neck, 2 base), 165/53/75 cm, battery 24V 40Ah, sensors, compute i5-i9, Jetson options, ROS Noetic, vosk/acapela/rasa stack, GDPR, LED/eye specs | vendor-claimed |
| 3 | https://pal-robotics.com/blog/assistive-robots-in-healthcare-spring-project/ | SPRING: Broca hospital Paris, 100+ patients, 5 use cases, 50+ modules, ROS4HRI, completion Oct 2024 | vendor-claimed |
| 4 | https://pal-robotics.com/blog/ari-social-robotics-artificial-intelligence-one-platform/ | ARI introduction Dec 18, 2019; i7 + Jetson TX2 positioning | vendor-claimed |
| 5 | http://wiki.ros.org/Robots/ARI (fetched via web.archive.org) | Public simulation packages, tutorials, ROS API, maintainer PAL Robotics | third-party (ROS community wiki, PAL-maintained) |
| 6 | https://pal-robotics.com/blog/ari-social-robot-delivered-to-hospitals/ | 7 ARIs delivered to SPRING partners (Dec 2021), planned hospital tasks | vendor-claimed |
| 7 | https://pal-robotics.com/blog/ari-as-humanoid-receptionist-at-ayesa/ | Ayesa receptionist deployment | vendor-claimed |
| 8 | https://pal-robotics.com/blog/pro-cared-pilots-robot-ari-as-education-robot-with-catalan-language/ | PRO-CARED education pilots (Catalan) | vendor-claimed |
| 9 | https://pal-robotics.com/blog/start-pilot-home-robot-ari-project-shapes/ | SHAPES home pilot | vendor-claimed |
| 10 | https://pal-robotics.com/blog/ari-social-robot-takes-the-spotlight-at-the-cruilla-festival/ (+ /ari-at-iot-swc-social-event-host-meets-the-king/) | Cruilla 2022, IOT SWC / King of Spain events | vendor-claimed |
