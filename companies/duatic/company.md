# Duatic AG

| Field | Value |
|---|---|
| HQ | Zürich, Switzerland (Affolternstrasse 42, 8050 Zürich) |
| Founded | Incorporated 2024-04-26 (CHE-211.244.464) |
| Founders / key people | Dhionis Sako and Dimitris Sako (co-founders, ex-ETH Robotic Systems Lab); Timo Schwarzer (Duatic AG, engineering/leadership per LinkedIn). Team claims 25+ years combined ETH robotics research experience. |
| Employees (approx.) | Small startup team, est. <15 (estimated) |
| Ownership / listing | Private (AG, Swiss stock corporation) |
| Total funding / valuation | Venture Kick CHF 50,000 (2024); no VC round publicly disclosed as of mid-2026 |
| Semi-humanoid products | [Alpha](alpha/robot.md) — dual-DynaArm wheeled half-humanoid |
| Other products | DynaArm (standalone QDD lightweight arm, 9.2 kg), DynaDrive actuators (Armadillo wrist / Baboon hip-knee / Coyote wheel) |
| Website | https://www.duatic.com |

## Company background
Duatic AG is a young ETH Zürich spin-off (incorporated 26 April 2024) commercializing the DynaArm and DynaDrive actuator technology developed at ETH's Robotic Systems Lab (RSL) — the lab behind ANYmal and the ALMA legged-manipulation platform [S2][S5]. The DynaDrive actuator family (Coyote/Baboon: 60 Nm peak, 27 Nm nominal, 48 V, 32 A peak, 930 W, integrated 6D IMU, EtherCAT) was originally used to upgrade ANYmal's joints and wheels, and the DynaArm was demonstrated on ANYmal and Festo's BionicMobileAssistant before the spin-off [S5][S6]. The founders, Dhionis and Dimitris Sako, position Duatic as a "full-stack robotic mobile manipulation" company merging Swiss-made quasi-direct-drive (QDD) hardware with machine-learning-based control [S3].

Products span three levels: DynaDrive actuators, the DynaArm (9.2 kg arm mass, 6 kg continuous / 12 kg 10 s payload, 0.99 m reach, 10 m/s end-effector speed, IP66, ROS 2 native with open API, no external control box) [S4], and the Alpha half-humanoid — two DynaArms on a mecanum-wheeled base [S1]. Go-to-market is direct, aimed at research labs first and industrial/intralogistics customers second; ROS 2 drivers are published openly on GitHub (Duatic/dynaarm_driver), signaling a research-friendly open-platform strategy [S7].

Funding is minimal so far: CHF 50k from Venture Kick (2024) [S3]. Duatic targets labor-shortage industries and quotes the physical-labor market at ~50% of global GDP in its pitch. A LinkedIn-sourced mention suggests Duatic exhibited Alpha at LogiMAT 2026 (Stuttgart, 24–26 March 2026) for intralogistics — plausible but not independently verified [S8].

## Relevance to the semi-humanoid market
Duatic is the most credible Swiss entrant in the wheeled dual-arm category and a direct geographic/technical neighbor to any new EU entrant. Its differentiators are pedigree (ETH RSL / ANYmal lineage), highly dynamic backdrivable QDD arms that are far lighter than industrial cobots of similar reach, IP66 sealing, and ROS 2 openness. It is still pre-scale — prototype/early-unit stage, no disclosed pricing or paying deployments — so its threat is currently in talent and technology rather than installed base. Trajectory: moving from research-platform sales toward intralogistics pilots.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.duatic.com/alpha | Alpha specs | vendor-claimed |
| 2 | https://www.venturekick.ch/duatic | Venture Kick CHF 50k, ETH background, incorporation | third-party |
| 3 | https://www.venturekick.ch/duatic + https://startup-seeker.com/company/duatic~com | founding 2024, positioning | third-party |
| 4 | https://www.duatic.com/dynaarm | DynaArm specs | vendor-claimed |
| 5 | https://rsl.ethz.ch/robots-media/actuators/DynaDrives.html | DynaDrive actuator family, ANYmal use | third-party (academic) |
| 6 | https://www.duatic.com/about-us | address, ANYmal/Festo demos | vendor-claimed |
| 7 | https://github.com/Duatic/dynaarm_driver/ | open ROS 2 driver | third-party |
| 8 | LinkedIn/WebSearch mention of LogiMAT 2026 presence | trade-show appearance | estimated (unverified) |
