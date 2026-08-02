# XLeRobot — open source (Vector Wang)

> XLeRobot is a ~$660 open-source (Apache 2.0) dual-arm mobile robot: two SO-100/SO-101 arms on an IKEA RÅSKOG cart driven by three omni wheels, running the Hugging Face LeRobot stack for teleop, imitation learning and VLA policies. Assembly takes under 4 hours; a $579 kit is sold by Wowrobo. With ~5.4k GitHub stars it is the flagship of the hobbyist semi-humanoid wave — commoditizing the wheeled dual-arm form factor for education and embodied-AI research.

| Field | Value |
|---|---|
| Company | Open-source project (creator Gaotian "Vector" Wang, Rice University) |
| HQ | Houston, TX, USA / global community |
| Status (2026) | shipping (kits + self-build; active development) |
| First shown / launch | v0.2.0 2025-06-13 (first fully capable); v0.3.0 2025-08-30 |
| Target applications | Education, embodied-AI/VLA research, hobbyist household-task demos |
| Price | From ~$660 self-sourced; Wowrobo kit $579 / CNY 3,699; options: stereo cams +$30, Raspberry Pi +$79, RealSense RGB-D +$220 [S1] |
| Availability | Worldwide (open BOM + kit) |

Design: IKEA RÅSKOG steel cart as chassis/torso (shelves double as storage), three omni wheels (Lekiwi-style triangular drive) for holonomic motion, two 6-DoF SO-100/SO-101 arms (Feetech STS3215 bus-servo based, ~14 DoF total with grippers) mounted on the cart top, head camera options from single RGB to stereo to RealSense D415 [S1] (vendor-claimed, open design — fully verifiable). Compute: laptop offboard or Raspberry Pi 5 onboard. Software: LeRobot-based; teleop via keyboard, Xbox controller, Switch Joy-Con, or Quest 3 VR; MuJoCo simulation with VR and (since 2026-01) browser-based control incl. 3D Gaussian splat scenes; supports imitation-learning data collection and VLA training/deployment; RL environments available [S1]. Battery: cart-mounted power bank (runtime not specified). Traction: ~5.4k stars / ~590 forks, active contributor community, household-task demo videos (fruit fetching, tidying) [S1]. No safety certification (hobby platform).

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://github.com/Vector-Wangel/XLeRobot | Full BOM, pricing, versions, capabilities, community stats | vendor-claimed (open repo) |
| 2 | https://xlerobot.readthedocs.io | Assembly/docs site | vendor-claimed |
