# M-Hubo — KAIST Hubo Lab

> M-Hubo is KAIST Hubo Lab's wheeled dual-arm "robotic butler" research platform (~2018-19, IROS 2019): 20 DoF total, two 7-DoF arms carried over from the DARPA-winning DRC-HUBO+, on an omnidirectional base with a waist DoF. It demonstrated end-to-end autonomous beverage fetching at 24% of human speed with 90% success. Competitively it matters as the peer-reviewed academic ancestor of Rainbow Robotics' RB-Y1 and as early Korean validation of the semi-humanoid service form factor.

| Field | Value |
|---|---|
| Company | KAIST Hubo Lab (research) |
| HQ | Daejeon, South Korea |
| Status (2026) | research (project concluded; lineage continues at Rainbow Robotics) |
| First shown / launch | ~2018-19; paper at IROS 2019, arXiv 2020-01 [S1] |
| Target applications | Indoor service / butler tasks (beverage fetching); aging-population assistance research |
| Price | n/a (research platform, not for sale) |
| Availability | n/a |

Design and specs (all third-party, peer-reviewed [S1]): 20 DoF total — two 7-DoF manipulator arms (design from DRC-HUBO+, 0.8 m reach, joint limits optimized for ~100° workspace each), a waist DoF, and an omnidirectional wheeled base with 3.5 km/h max speed; shape-adaptive 3-finger grippers rated 2 kg at the finger / 10 kg at the arm; bottom-heavy layout with Ni-ion 48 V 11 Ah battery packs (~0.53 kWh) to prevent tipping during fast motion. Head sensor pack: two RGB-D cameras (RealSense D415 + ZED stereo) and a Velodyne Puck VLP-16 lidar. Compute: separate Vision PC (Alienware ASM201: i7, 16 GB, GTX 960) running ROS, and Motion PC (Intel NUC6i7KYK: i7, 8 GB) running the lab's PODO real-time framework on Xenomai RT [S1]. Demonstrated performance: fetch-a-beverage at 24% of human task speed, 90% success in controlled settings and 80% at a dynamic public exhibition [S1][S2]. A companion paper (arXiv 2001.00358) documents the ROS-to-PODO motion interface. No commercial deployment; the platform's significance is its direct lineage into Rainbow Robotics' RB-Y1 (2024) via the shared Hubo Lab heritage [S3].

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://arxiv.org/abs/2001.00356 | All hardware specs, sensors, compute, performance (IROS 2019 paper) | third-party (peer-reviewed) |
| 2 | https://techxplore.com/news/2020-01-m-hubo-wheeled-humanoid-robot-humans.html | Performance summary, purpose | third-party |
| 3 | https://en.wikipedia.org/wiki/Rainbow_Robotics | Hubo Lab → Rainbow Robotics lineage | third-party |
