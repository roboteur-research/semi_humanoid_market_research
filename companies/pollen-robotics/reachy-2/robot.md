# Reachy 2 — Pollen Robotics (Hugging Face)

> Reachy 2 is a fully open-source, human-scale bimanual semi-humanoid on an omnidirectional wheeled base (or stationary mount), built for embodied-AI research labs. At ~$70k with two bio-inspired 7-DoF "Orbita"-joint arms, VR teleoperation and first-class LeRobot/ROS 2 integration, it is the flagship hardware of Hugging Face's open robotics ecosystem — competitively important as the platform around which Western open-source robot learning is standardizing.

| Field | Value |
|---|---|
| Company | Pollen Robotics (Hugging Face since Apr 2025) |
| HQ | Bordeaux, France |
| Status (2026) | shipping |
| First shown / launch | Announced 2023; commercial debut CES 2025 |
| Target applications | Embodied-AI research, teleoperation data collection, HRI research, education |
| Price | ~USD 70,000 (dual-arm + mobile base config) [S2][S4] |
| Availability | Direct order worldwide; 4 kit variants (single/dual arm × mobile base/stationary) [S1] |

## Design & morphology
Human-inspired torso + head on a cylindrical omnidirectional base. Manually adjustable height 136–166 cm; weight up to ~50 kg full configuration [S1]. 17 actuated DoF in upper body + base (2×7-DoF arms, 3-DoF Orbita neck) plus animated antennas for expressiveness [S3]. Modular: right and left arms strictly identical; internal cable routing. No powered torso lift (manual height adjustment only) [S3].

## Locomotion
Omnidirectional mobile base with three omniwheels; RPLIDAR S2 lidar, IMU and Hall-effect wheel sensors for navigation [S4]. Indoor flat-floor use; speed not officially published (slow, human-safe research speeds). Stationary desk/stand mounting is an alternative configuration [S1].

## Upper body & manipulation
Two 7-DoF arms sized and proportioned like an adult human arm: shoulder and elbow each a 2-DoF Orbita parallel actuator, wrist a 3-DoF Orbita spherical parallel actuator [S3][S4]. Payload ~3 kg per arm [S1][S5]. End effector: simple 2-finger parallel gripper (vendor docs; dexterous hands not standard). No tool changer / media at flange (n/a). Reach not officially stated (human-arm scale, est. ~650–700 mm).

## Sensing
Head: 2× Sony IMX296 global-shutter RGB cameras (stereo pair in Orbita-actuated head), microphones and speaker for HRI [S4]. Torso: Orbbec Gemini 336 RGB-D camera + Luxonis OAK ToF sensor for depth [S4]. Base: RPLIDAR S2, IMU, Hall sensors [S4]. No published force-torque or tactile sensing in hands; arm joints are torque-controllable for compliant behavior (vendor demos).

## Actuation & power
Proprietary Orbita 2D/3D parallel actuators (brushless motors; maxon motors used per maxon case study) plus Dynamixel-class units in gripper/antennas [S3][S6]. Battery in mobile base for untethered runtime; capacity/runtime not disclosed (n/a). Mains operation when stationary.

## Compute & software
Onboard: SolidRun Bedrock v3000 fanless industrial PC (CPU-only; heavy AI inference expected to run on the user's external GPU machines) [S3]. Stack: ROS 2 Humble core, open Python SDK, WebRTC-based remote access, full VR teleoperation app (Meta Quest) for data collection [S1][S5]. First-class integration with Hugging Face LeRobot (policies, datasets, training pipelines); entire hardware CAD + software being open-sourced post-acquisition [S5][S7]. This open stack is the robot's main differentiator.

## Safety & compliance
No ISO 13482 / ISO 10218 certification claimed; CE marking as machinery for research use assumed but not documented (n/a — research platform, not certified for unattended commercial operation). Compliant, low-power actuators and light arms (3 kg payload) keep inherent risk low.

## Deployment evidence & traction
- Research deployments at Cornell University and Carnegie Mellon University (third-party reported) [S7].
- Used inside Hugging Face/Pollen for LeRobot demos and community datasets; frequent conference presence (CES 2025, ICRA) [S2].
- Unit counts not disclosed; realistically tens of units (estimated). No commercial/industrial customers known.

## Assessment (analyst view)
*Analyst opinion.* Strengths: the only credible fully open-source human-scale bimanual platform in Europe; unmatched software ecosystem gravity via Hugging Face/LeRobot; low price for a dual-arm mobile manipulator; excellent teleop-to-dataset pipeline. Weaknesses: 3 kg payload, CPU-only compute, no safety certification, no torso lift and no industrial support organization — it is a lab instrument, not a deployable worker. Threat to a new EU entrant: low as a direct commercial competitor, but high strategically — it sets developer mindshare and de-facto software standards, and Hugging Face could later commoditize the hardware layer a commercial entrant charges for. Partnering (LeRobot compatibility) may be smarter than competing.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://pollen-robotics.com/reachy-2/ | Height 136–166 cm, ~50 kg, 3 kg/arm, kit variants, ROS 2 Humble, VR teleop | vendor-claimed |
| 2 | https://www.therobotreport.com/pollen-robotics-debuts-reachy-2-humanoid-at-ces-2025/ | CES 2025 debut, price ~$70k | third-party |
| 3 | https://docs.pollen-robotics.com/hardware-guide/specifications/general/ | DoF architecture, Orbita actuators, SolidRun compute, modularity | vendor-claimed |
| 4 | https://docs.pollen-robotics.com (hardware guide, sensor pages, via search summary) | Cameras IMX296, Orbbec Gemini 336, OAK ToF, RPLIDAR S2, omniwheels | vendor-claimed |
| 5 | https://huggingface.co/docs/lerobot/en/reachy2 | LeRobot integration, teleop | vendor-claimed |
| 6 | https://www.maxongroup.com/en-us/knowledge-and-support/blog/reachy-2-the-open-source-humanoid-robot-257768 | maxon drives in Orbita actuators | third-party |
| 7 | https://www.forbes.com/sites/janakirammsv/2025/06/02/the-strategy-behind-hugging-faces-acquisition-of-pollen-robotics/ | Cornell/CMU deployments, open-source plan | third-party |
