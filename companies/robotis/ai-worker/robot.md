# AI Worker (AI워커, FFW series) — ROBOTIS

> The AI Worker is ROBOTIS's "Physical AI" semi-humanoid: dual 7-DoF DYNAMIXEL-based arms on a lift column, offered as a swerve-drive mobile robot (FFW-SG2), a stationary base (FFW-BG2, ~$40k) and matching teleoperation "leader" devices (FFW-LG2) for imitation-learning data collection. Everything — ROS 2 code, URDF/MJCF/USD sim models, Docker images, tutorials, pre-trained models and datasets — is open source, making it the most open commercial semi-humanoid anywhere and a reference price point for the segment.

| Field | Value |
|---|---|
| Company | ROBOTIS |
| HQ | Seoul, South Korea |
| Status (2026) | shipping |
| First shown / launch | 2025 (FFW-BG2/SG2 lineup; Reuters imitation-learning coverage May 2026) |
| Target applications | industrial imitation learning: wiring-harness assembly, welding assist, inspection; research |
| Price | FFW-BG2 ~USD 40,000 (incl. VAT, EU reseller); US quotes via america@robotis.com [S3] |
| Availability | Global via ROBOTIS shops/subsidiaries; FFW-BG2 listed "Korea only" on some pages; leader devices sold separately |

## Design & morphology
Variants: FFW-SG2 (mobile, swerve-drive 3-wheel base, 604×602×1,623 mm, 90 kg, 25 DoF total) and FFW-BG2 (stationary, 604×564×1,607 mm, 85 kg, 19 DoF); FFW-SH3P (with dexterous hands) in preparation. DoF budget (SG2): 2×7 arms + 2×1 grippers + 2 head + 1 lift + swerve modules. Leader models FFW-LG2 / LH5 are master devices mirroring the follower kinematics for teleop data capture. [S1]

## Locomotion
SG2: swerve drive — three wheel modules with independent steering + drive, giving true omnidirectional motion; 1.5 m/s max. BG2: none (bench/floor stand, AC-powered). [S1]

## Upper body & manipulation
Arms: 7 DoF each, reach 641 mm to wrist (+ hand), nominal payload 3.0 kg single / 6.0 kg dual; peak 5.0 kg single / 10.0 kg dual. Standard end-effector: RH-P12-RN 1-DoF two-finger gripper (5 kg grip payload, 500 g mass). Five-finger dexterous hand (16-20 DoF target per hand; 20-joint version shown at CES 2026) under development. Media at flange: RS-485 daisy-chain (DYNAMIXEL bus). [S1][S5]

## Sensing
Head: Stereolabs ZED Mini stereo/depth camera (102°×57°, 0.1-9 m). Hands: 2× Intel RealSense D405 close-range depth (87°×58°, 7-50 cm) for manipulation. Base: 2× LakiBeam 1 2D ToF lidar (270°, 25 m) + IMU (SG2). No F/T or tactile sensing in current gripper spec. [S1]

## Actuation & power
All joints use ROBOTIS DYNAMIXEL smart actuators (integrated servo+driver+network; company's core product). Battery (SG2): 25 V / 80 Ah = 2,040 Wh; runtime n/a (not disclosed). BG2: AC via SMPS (24 VDC, 80 A, 1,920 W). Hot-swap not claimed. [S1]

## Compute & software
NVIDIA Jetson AGX Orin 32GB onboard; RS-485 bus at 4 Mbps; Ethernet host interface. Software: ROS 2, Python/C++, Web UI. Fully open source: GitHub ROBOTIS-GIT/ai_worker (ROS 2 packages), cyclo_control, physical_ai_tools (LeRobotDataset generation); sim models in URDF/MJCF/USD (Isaac Sim/Lab ready); pre-trained models and training datasets on Hugging Face (huggingface.co/ROBOTIS); Docker Hub images; tutorial videos. Integrated pipeline: leader-follower teleop data collection → visualization → training → inference. [S1][S2]

## Safety & compliance
No ISO 13482/10218/CE certifications published. Operating temp 0-40 °C. E-stop present on hardware; safety concept otherwise n/a (not disclosed). [estimated — absence of claims]

## Deployment evidence & traction
Reuters (May 2026): ROBOTIS trains the robots on skilled human workers' motions for industrial tasks; targeted at wiring-harness assembly, welding and inspection reflecting "requirements from overseas AI companies" (Korean trade press). Sold through ROBOTIS US/EU shops (BG2 listed ~$40k incl. VAT at Swiss reseller). Unit numbers: n/a (not disclosed). K-Humanoid Alliance member robot; joint Korean exhibit at CES 2026. Open-source repos and HF datasets show active external use. [S3][S4][S5]

## Assessment (analyst view)
*Analyst opinion.* Strengths: unbeatable openness (code+sim+data+models), vertical integration into its own DYNAMIXEL actuators (cost + margin advantage), ~$40k price undercuts RB-Y1 by half, credible leader-device teleop workflow. Weaknesses: light payload class, basic 2-finger gripper today, no published safety certification, modest brand presence outside research/education. Threat to an EU entrant: medium-high — it commoditizes the "open imitation-learning platform" niche and anchors price expectations low; an EU entrant should not try to out-open ROBOTIS but differentiate on certified, turnkey industrial capability.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://ai.robotis.com/ai_worker/hardware_ai_worker | full FFW-SG2/BG2 specs, sensors, battery, compute | vendor-claimed |
| 2 | https://ai.robotis.com/opensource.html | open-source repos, HF models/datasets, Docker, sim formats | vendor-claimed |
| 3 | ROBOTIS shop listings via DDG (robotis.us / Swiss reseller) | FFW-BG2 ~$40,000 incl. VAT; US quote process | third-party |
| 4 | https://www.business-standard.com/world-news/south-korean-startup-trains-humanoid-robots-using-human-workers-skills-126051200076_1.html (Reuters syndication) | imitation learning from human workers, May 2026 | third-party |
| 5 | Korean press via DDG (edaily 01964726642137432; biz.chosun CES 2026; irobotnews 38412) | launch coverage, 20-joint hand at CES 2026, skilled-worker learning | third-party |
| 6 | https://www.robotis.com/en/product/ecosystem-aiworker.php | positioning, target tasks, hand DoF target 16-20 | vendor-claimed |
