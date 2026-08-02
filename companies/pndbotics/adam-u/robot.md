# Adam-U — PNDbotics

> Pedestal-mounted upper-body humanoid for imitation-learning data collection and algorithm research: 31 QDD force-controlled DoF (incl. two 13-DoF arm+hand chains and a 3-DoF waist) on a height-adjustable lifting column. Reseller-listed at $45,000 — a mid-price entry in the stationary data-collection platform segment.

| Field | Value |
|---|---|
| Company | PNDbotics, Beijing |
| HQ | Beijing, China |
| Status (2026) | shipping (in-stock at resellers) |
| First shown / launch | 2025 |
| Target applications | Mocap/teleop data collection, imitation & reinforcement learning research, algorithm testing |
| Price | USD 45,000 (reseller, in-stock) [S3] |
| Availability | Global via resellers (Robots LATAM/Asia network); direct from PNDbotics |

| Spec | Value | Confidence |
|---|---|---|
| Base type | fixed pedestal: lifting column + chassis (needs ~40 kg counterweight) | vendor-claimed [S1] |
| Height | 1.35-1.77 m adjustable | vendor-claimed [S1] |
| Weight | 26 kg main unit; 48 kg with lift platform + chassis | vendor-claimed [S1] |
| DoF | 31 total: per arm 3 shoulder +1 elbow +1 forearm +2 wrist +6 fingers (=13); waist 3 (with brakes); head 2 | vendor-claimed [S1] |
| Hands | Inspire RH56E2 6-DoF dexterous hands | vendor-claimed [S1][S3] |
| Actuators | in-house QDD flexible force-controlled joints, modular | vendor-claimed [S1] |
| Sensors | ZED Mini stereo depth camera (head); PND-Network protocol for sensor expansion | vendor-claimed [S1] |
| Compute | Intel NUC12 i7 (motion) + Jetson Orin NX 16GB, 100 TOPS (AI) | vendor-claimed [S1] |
| Battery | 1,172 Wh, 46.2 V / 25 A | vendor-claimed [S1] |
| Software | ROS 2 Humble, WBC + MPC; Noitom PNLink mocap-suit teleop; WiFi 6/BT 5.0/Ethernet | vendor-claimed [S1] |

Adam-U is the upper body of PNDbotics' Adam biped remounted on a manual-height pedestal for benchtop research. Its differentiators are force-controlled QDD joints throughout (rather than position-controlled servos typical at this price) and a genuine 3-DoF braked waist, giving human-like reachable workspace for imitation-learning data whose kinematics transfer to full humanoids [S1][S2]. The bundled ecosystem — Noitom PNLink mocap suit for whole-upper-body teleoperation plus Inspire dexterous hands — makes it a turnkey data-collection cell [S3]. Press coverage emphasizes its unusually lifelike motion (dancing, cloth handling demos) [S2]. Note a spec discrepancy: press reports cite 61 kg total weight vs the vendor wiki's 26/48 kg breakdown [S1][S2]. As a stationary pedestal unit it sits at the edge of the semi-humanoid category (no mobility).

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://wiki.pndbotics.com/en/half_robot/half_robot/ | full specs (DoF, weights, compute, battery, software) | vendor-claimed |
| 2 | https://interestingengineering.com/innovation/chinas-humanoid-robot-nails-human-like-motion | 31 DoF, adjustable height, 61 kg figure, demos | third-party |
| 3 | https://www.robotslatam.com/PNDbotics.htm | $45,000 price, Noitom + Inspire RH56E2 partnership | third-party (reseller) |
