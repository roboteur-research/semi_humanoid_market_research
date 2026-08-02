# Mobile FR3 Duo — Franka Robotics

> Dual-arm mobile manipulation reference platform: two Franka Research 3 torque-controlled
> 7-DoF arms on the omnidirectional "Tactile Mobile Robot" (TMR) base with a sensor head.
> Prototype shown at Automatica 2025 with early access open — Germany's answer to the
> Chinese embodied-AI data-collection platforms, built on the most widely used research
> arm in the world. A stationary FR3 Duo variant shares the same architecture.

| Field | Value |
|---|---|
| Company | Franka Robotics GmbH, Munich (Agile Robots SE group) |
| Status (2026) | prototype / early access (announced 2025-08-01; Automatica 2025 showcase) |
| Target applications | physical-AI data collection & policy execution, teleoperation, whole-body coordination research, mobile manipulation |
| Price | not published (early access via lp.franka.de/upcomingproducts) |

## Design & morphology
Two FR3 arms (855 mm reach, 7 DoF, joint torque sensors — 14 across both arms) on a Duo
mounting bracket atop the TMR omnidirectional base (800 × 580 × 294 mm). Sensor head
mount (optional ZED Mini stereo). [S1]

## Locomotion
Omnidirectional base, max 1.75 m/s, 100 kg base payload. [S1]

## Upper body & manipulation
3 kg payload per arm; optional kit: 2× Robotiq 2F-85 grippers + 2× RealSense D405 wrist
cameras. Unified control across stationary and mobile variants. [S1]

## Sensing
2× lidar, 7× cameras (base + optional wrist/head), 1× IMU; arm joint torque sensing
("tactile" positioning). [S1]

## Compute & software
NVIDIA Jetson AGX Orin onboard; Wi-Fi/Ethernet/USB/Bluetooth. Franka Control Interface
(FCI) at 1 kHz (joint torque, position/velocity, Cartesian modes, external wrench
estimation); ROS 2 (franka_ros), MoveIt (PickNik MoveIt Pro partnership visible at the
Automatica showcase), URDF/Gazebo, C++/MATLAB/Simulink. [S1][S2]

## Safety & compliance
FR3 arms are certified collaborative arms (ISO 10218/TS 15066 heritage); platform-level
certification not stated for the prototype. [estimated]

## Deployment evidence & traction
Automatica 2025 showcase; early-access program; no commercial deployments disclosed. [S2]

## Assessment (analyst view)
*Analyst opinion.* The Mobile FR3 Duo is not a product competitor but an ecosystem play:
it standardizes the bimanual mobile research rig European labs previously had to
self-integrate, on a control stack (FCI/ROS 2) that dominates academia. For a German
entrant it is the natural domestic prototyping platform — and evidence that Agile
Robots/Franka could move further toward integrated semi-humanoids. Its 3 kg/arm payload
keeps it research-grade, well below industrial Chinese rivals.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://franka.de/de/mobile-fr3-duo | full specs | vendor-claimed |
| 2 | https://franka.de/news/real-world-robotics-insights-from-fr3-duo-mobile-showcase | showcase, date, quote | vendor-claimed |
