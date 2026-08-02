# Tokyo Robotics Inc. (東京ロボティクス株式会社)

| Field | Value |
|---|---|
| HQ | Bunkyo-ku, Tokyo, Japan |
| Founded | January 2015 |
| Founders / key people | Yoshihiro Sakamoto, Ph.D. — founder & CEO |
| Employees (approx.) | n/a (not disclosed; small engineering firm) |
| Ownership / listing | Private — wholly owned subsidiary of Yaskawa Electric Corporation (per company about-us page, 2026) |
| Total funding / valuation | Capital ¥100M; acquisition terms by Yaskawa n/a (not disclosed) |
| Semi-humanoid products | [Torobo / Torobo2](torobo/robot.md) |
| Other products | Torobo Hand (10-axis multi-finger hand with in-house micro cycloidal reducers), Torobo Arm, Torobo Puppet teleop device; 2026 bipedal "Torobo Humanoid" (RL-driven — separate, legged) |
| Website | https://robotics.tokyo/ |

## Company background
Tokyo Robotics was founded in January 2015 by Yoshihiro Sakamoto to build torque-controlled research robots under the mission of freeing people from manual labor. Its signature technology is whole-body torque sensing and impedance control: every joint of its robots carries a torque sensor, enabling compliant contact-rich manipulation, and its Torobo Hand uses what the company calls the world's smallest cycloidal reducer (developed in-house) to bring impedance control into a 10-axis multi-finger hand. [S1][S2]

The flagship Torobo is a wheeled full-body research humanoid (dual 7-axis torque arms, 3-axis waist, 3-axis neck, omni base) sold to research labs; a puppet-type teleoperation device with a 1:1 joint mapping (2024) supports imitation-learning data collection, and the company open-sourced torobo_isaac_lab for NVIDIA Isaac Lab. A lighter second-generation Torobo (Torobo2, ~120kg vs ~160kg) shipped in Japan from March 2025 and overseas from October 2025. In 2026 the company entered the bipedal arena with an RL-driven "Torobo Humanoid" (excluded here — legged). Significantly, Tokyo Robotics is now a wholly-owned subsidiary of Yaskawa Electric, giving Japan's top robot maker an in-house humanoid/torque-control capability. [S1][S2][S3][S4]

## Relevance to the semi-humanoid market
Torobo is Japan's premier domestically-built full-body wheeled research humanoid — the platform on which Japanese labs and corporates prototype semi-humanoid applications — and the Yaskawa ownership makes it a strategic asset: expect Torobo technology (torque joints, hands, teleop) to feed Yaskawa's industrial humanoid ambitions (MOTOMAN NEXT). As a market player it sells tens of units to labs, not fleets; its competitive weight is as the R&D seedbed of a giant. [S1][S3][S4]

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://robotics.tokyo/ | products, mission, news | vendor-claimed |
| 2 | https://robotics.tokyo/technologies/torobo/ | Torobo specs, torque control | vendor-claimed |
| 3 | https://robotics.tokyo/about-us/ | founded 2015-01, CEO Sakamoto, capital ¥100M, Yaskawa full ownership | vendor-claimed |
| 4 | https://www.humanoidsdaily.com/news/tokyo-robotics-steps-into-the-bipedal-arena-with-rl-driven-humanoid | Torobo2 timing (JP 03/2025, overseas 10/2025), bipedal 2026 | third-party |
