# Sciurus17 (シューラス17) — RT Corporation

> Sciurus17 is a ¥3.3M, 17-axis dual-arm upper-body research robot (上半身人型ロボット) with native ROS/ROS 2 support and open GitHub packages — a de-facto standard Japanese lab platform for dual-arm manipulation, imitation learning and avatar research. Since June 2025 the Sciurus Lift option (70cm vertical axis) docks it onto Preferred Robotics' Kachaka Pro mobile base, converting it into a low-cost mobile semi-humanoid — a Japanese counterpart to Western mobile-manipulation research rigs at a fraction of the price.

| Field | Value |
|---|---|
| Company | RT Corporation (株式会社アールティ) |
| HQ | Tokyo, Japan |
| Status (2026) | shipping (made-to-order) |
| First shown / launch | 2018; Sciurus Lift option orderable 06/2025 |
| Target applications | University/corporate research: dual-arm manipulation, imitation/reinforcement learning, avatar robots, education |
| Price | ¥3,300,000 base (≈USD 22k); mic/speaker head option ¥55,000; Lift and Kachaka Pro base sold separately |
| Availability | Japan, made-to-order, 2-3 month lead time |

## Design & morphology
Tabletop/bench-mount torso: 270 × 393 × 665mm, ~6kg incl. mounting bracket [S1]. 17 axes: 2 (neck) + 7 per arm + 1 waist, plus separate hand actuators per side; 7-axis arms give elbow redundancy for obstacle avoidance [S1]. Workspace ~1,200mm diameter [S1].

## Locomotion
None natively. With Sciurus Lift (model S17-LIFT, 70cm vertical travel, integrated battery, mounting hardware) it docks onto a Preferred Robotics Kachaka Pro autonomous mobile base, giving floor-to-shelf mobile manipulation; ROS 2 sample software provided for the combination; orderable since June 2025 [S3].

## Upper body & manipulation
Two 7-DoF arms, ~0.5kg payload each (vendor-claimed) [S1]. Simple 1-DoF grippers driven by dedicated servos; position/velocity/current(torque) control selectable per joint [S1].

## Sensing
Intel RealSense D415 RGB-D camera in head [S1]. Optional RT-Sciurus17-OP1 head with stereo microphones + speaker for dialogue/HRI research (¥55,000) [S1]. No base/torque-sensor suite (current-based torque estimation via Dynamixel servos).

## Actuation & power
ROBOTIS Dynamixel servos: XM430-W350-R, XM540-W270-R, XM540-W150-R (RS-485) [S1]. Power 12V/12.5A (150W) [S1]. Lift unit carries its own battery [S3].

## Compute & software
No onboard PC — external PC over USB 3.0/LAN; internal wiring 3× RS-485 + 2× USB 3.0 [S1]. Native ROS and ROS 2 packages, Gazebo simulation, C++ servo library, sample code — all open on GitHub (rt-net) [S1]. Widely used for imitation-learning research; Sciurus Lift release explicitly targets imitation/reinforcement-learning and vision-based mobile manipulation [S3].

## Safety & compliance
Research product; no safety certification (n/a). Low-power servo arms (0.5kg payload) are intrinsically low-risk.

## Deployment evidence & traction
Sold since 2018 to Japanese universities, technical colleges and corporate research teams (vendor-claimed; unit counts n/a). Its ROS packages are the reference dual-arm stack in Japanese academia [S1][S3] (third-party visibility via robotstart coverage). Sciurus Lift launched as made-to-order June 2025 [S3].

## Assessment (analyst view)
*Analyst opinion.* Sciurus17's significance is ecosystem, not payload: at ¥3.3M it seeded a generation of Japanese dual-arm/imitation-learning researchers on RT's stack, and the 2025 Kachaka docking shows how cheaply a static torso becomes a mobile semi-humanoid using an off-the-shelf consumer AMR. Weaknesses: toy-grade 0.5kg payload, hobby-class Dynamixel actuation, no industrial path. Threat to an EU entrant: negligible commercially, but it shapes researcher expectations and tooling in Japan — an EU platform selling into Japanese labs competes with this price point.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://rt-net.jp/products/sciurus17/ | full specs, price, servos, ROS, options | vendor-claimed |
| 2 | https://github.com/rt-net/sciurus17_ros | open ROS packages | vendor-claimed |
| 3 | https://robotstart.info/2025/05/27/rt-developed-sciurus-lift.html | Sciurus Lift specs, Kachaka Pro docking, 06/2025 orders | third-party |
