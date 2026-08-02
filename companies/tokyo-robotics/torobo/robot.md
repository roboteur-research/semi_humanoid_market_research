# Torobo / Torobo2 (トロボ) — Tokyo Robotics

> Torobo is a full-body wheeled research humanoid — dual 7-axis arms, 3-axis waist, 3-axis neck on a 4-axis omni base — with torque sensors in every joint for whole-body impedance control. Sold to research labs to accelerate industrial application research, it pairs with the Torobo Puppet 1:1 teleoperation device for imitation-learning data collection and ships with MuJoCo/Isaac Sim models. It is Japan's leading domestic wheeled research humanoid, and Tokyo Robotics is now wholly owned by Yaskawa Electric — making Torobo the de-facto R&D humanoid of Japan's largest robot maker.

| Field | Value |
|---|---|
| Company | Tokyo Robotics Inc. (wholly-owned Yaskawa Electric subsidiary) |
| HQ | Tokyo, Japan |
| Status (2026) | shipping (research labs; Torobo2 JP 03/2025, overseas 10/2025) |
| First shown / launch | Torobo torso platform mid-2010s onward; full mobile humanoid + Puppet teleop 2024; Torobo2 2025 |
| Target applications | Research platform: industrial humanoid application research, imitation learning, contact-rich manipulation |
| Price | n/a (not disclosed; quotation) |
| Availability | Japan direct; overseas since 10/2025 |

## Design & morphology
Torobo2 (current): height 1,615mm, cart width 590mm, weight ~120kg [S1]. DoF: 2× 7-axis arms + 3-axis waist (pitch-pitch-yaw) + 3-axis neck (yaw-pitch-roll) + 4-axis omni base = 24 axes [S1]. Previous generation was ~160kg with 8kg (20kg peak) arm payload; Torobo2 is deliberately lighter for faster dynamic motion (ball-throwing demos) [S2][S3].

## Locomotion
4-axis omnidirectional wheeled cart; ZMP-based fall-prevention control; speed n/a (not disclosed) [S1].

## Upper body & manipulation
Two 7-axis torque-controlled arms, 7kg payload each in worst-case posture (Torobo2) [S1]. Every joint carries a torque sensor enabling impedance control and compliant contact [S1]. End-effectors: force-controlled gripper option, or Torobo Hand — 10-axis multi-finger hand with in-house micro cycloidal reducer, impedance-controlled grasping of unknown-geometry objects [S1][S4].

## Sensing
Optional head sensor suites (two head configurations): wide-angle stereo camera, fisheye camera, ToF depth camera, stereo microphone + speaker [S1]. Joint torque sensors on all axes [S1].

## Actuation & power
Torque-sensored electric joints (in-house drive train; cycloidal reducers in hand) [S1][S4]. Battery: up to 3 hours continuous operation [S1].

## Compute & software
ROS-based stack; Gazebo, MoveIt (planning + self-interference detection); official MuJoCo and Isaac Sim models; open-source torobo_isaac_lab extension for Isaac Lab RL training; optional onboard vision PC with NVIDIA RTX 4070/5070 [S1][S2]. Torobo Puppet teleoperation device (2024): passive puppet with identical joint configuration to the robot for intuitive 1:1 whole-body teleop; base driven by a controller on the puppet's hand — designed for imitation-learning data collection [S2][S5].

## Safety & compliance
Research platform: safety stop on interference detection, ZMP fall prevention; no ISO certification published (n/a) [S1].

## Deployment evidence & traction
Shipping to research laboratories (universities and corporate labs) in Japan; overseas sales from October 2025 [S2]. Exhibited at SusHi Tech Tokyo 2026; Nikkei coverage 2026 [S3]. Unit counts and named customers n/a (not disclosed). Sim-to-real results published using Torobo Hand (Isaac Sim RL → MuJoCo → hardware) [S2].

## Assessment (analyst view)
*Analyst opinion.* Torobo is the most technically serious Japanese wheeled research humanoid: full-joint torque sensing, an impedance-controlled dexterous hand with in-house reducers, first-class sim assets, and a purpose-built puppet teleop pipeline — exactly the toolchain the imitation-learning era demands. Its weakness as a competitor is that it isn't one: no price list, lab-scale volumes, no deployment story. The strategic threat is the Yaskawa ownership: an EU entrant should assume Torobo's torque-control and hand technology resurfaces in Yaskawa's industrialized humanoids (MOTOMAN NEXT line) with global sales channels behind it.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://robotics.tokyo/technologies/torobo/ | full Torobo2 specs, DoF, sensors, software, safety | vendor-claimed |
| 2 | https://robotics.tokyo/videos/ + https://github.com/TokyoRobotics | Puppet teleop, Torobo2 timing, torobo_isaac_lab, Hand RL | vendor-claimed |
| 3 | https://robotics.tokyo/ | news: SusHi Tech 2026, Nikkei | vendor-claimed |
| 4 | https://robotics.tokyo/features/ | Torobo Hand cycloidal reducer, impedance grasping | vendor-claimed |
| 5 | https://www.humanoidsdaily.com/news/tokyo-robotics-steps-into-the-bipedal-arena-with-rl-driven-humanoid | Torobo2 lighter/faster, availability dates, bipedal contrast | third-party |
