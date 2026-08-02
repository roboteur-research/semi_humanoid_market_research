# Nyro — hobbyist project (Ryota Kobayashi)

> Nyro is a self-described "semi-humanoid" upper-body robot built by a single Japanese maker (published on Hackaday.io, January 2026): dual 7-DoF arms with distinctive differential-gear joints, SteadyWin QDD motors on ODrive controllers, open-source Amazing Hand five-finger hands, a LattePanda 3 Delta for compute, all mounted on a camera tripod and teleoperated via a DYNAMIXEL leader arm. It matters not commercially but as evidence that the semi-humanoid term and component stack (QDD + dexterous hands + leader-arm imitation learning) have reached individual hobbyists.

| Field | Value |
|---|---|
| Company | Individual maker: Ryota Kobayashi |
| HQ | Japan |
| Status (2026) | prototype (personal project, ongoing) |
| First shown / launch | Hackaday.io project created 2026-01-20 |
| Target applications | Personal R&D; testbed for imitation learning |
| Price | n/a (one-off build) |
| Availability | Not available (project documentation public; no kit/files release found) |

Design (all vendor-claimed from the maker's project page [S1]): upper body with two 7-axis arms; joints use differential gear mechanisms (the project's signature) for smooth motion; most structural parts are 3D-printed; no lower body — the torso is mounted on a video-camera tripod for stability. Actuation: SteadyWin quasi-direct-drive motors driven by ODrive controllers — 12x ODrive Micro plus 2x ODrive S1 — on dual CAN buses (one per arm). Hands: open-source "Amazing Hand" (Pollen Robotics design) with Feetech servos, integrated via a custom STM32G4 bridge board that imitates the ODrive CAN protocol so hands and arms share one bus. Compute: LattePanda 3 Delta x86 SBC. Control: teleoperation with a self-built leader device using DYNAMIXEL motors matching the follower arm's 7 axes; hand upgrades and imitation learning are the stated next steps. Traction: 436 views, 5 likes (niche). Terminology note: the maker explicitly labels the project "semi-humanoid robot" — a grassroots adoption datapoint for the category name.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://hackaday.io/project/204888 | All design, actuation, compute, teleop details | vendor-claimed (maker's project page) |
