# Elephant Robotics (大象机器人)

| Field | Value |
|---|---|
| HQ | Shenzhen (Futian District), China |
| Founded | 2016 |
| Founders / key people | Kirin Wu (CEO), Joey Song (co-founder) |
| Employees (approx.) | ~100-200 (estimated; not disclosed) |
| Ownership / listing | Private |
| Total funding / valuation | Seed via HAX/SOSV; later rounds from Cloud Angel, Orient Securities, Shenzhen Venture Capital, ZhenFund; pre-Series B closed May 2024 (amounts not disclosed) [S2] |
| Semi-humanoid products | [Mercury X1](mercury-x1/robot.md) (wheeled humanoid; dossier also covers Mercury B1 torso) |
| Other products | myCobot 280/320, myPalletizer, mechArm, myArm, Mercury A1 7-axis cobot, ultraArm, robot pets (MarsCat/metaCat), AI kits, myController S570 exoskeleton teleoperator |
| Website | https://www.elephantrobotics.com |

## Company background
Elephant Robotics is a Shenzhen-based collaborative-robot maker founded in 2016 by Kirin Wu and Joey Song, incubated in the HAX hardware accelerator with SOSV seed funding [S2]. Its core business is low-cost desktop cobots for education, research and light automation: the myCobot family had sold over 10,000 units in 50+ countries by early 2024 [S2, third-party]. The company runs a high-volume e-commerce go-to-market (own web shop plus resellers such as RobotShop, OpenELAB, OzRobotics, Robot Pi Shop) — unusual among humanoid vendors, whose products rarely have public list prices.

The Mercury series (announced December 2023, CES 2024 debut) moved the company up-market into semi-humanoids while keeping the education/research positioning and price discipline: Mercury A1 is a 7-axis single arm, Mercury B1 a dual-arm torso with LCD "face", and Mercury X1 the B1 torso mounted on a wheeled AGV base. All Mercury robots use the company's in-house harmonic "Power Spring" joint modules with electromagnetic brakes and ship with an open software stack (ROS 1/2, MoveIt, Gazebo, Mujoco, Python pymycobot, C++ API, myBlockly visual programming, ChatGPT integration) [S1][S3].

Go-to-market is direct sale (not RaaS) at published prices in the $10k-20k class — an order of magnitude below most Chinese wheeled humanoids — targeting universities, embodied-AI labs and developer teams rather than factory deployment. The myController S570 wearable exoskeleton (1:1 joint mapping) provides low-cost teleoperation/data collection for imitation learning [S1].

## Relevance to the semi-humanoid market
Elephant Robotics matters as the price-floor setter for wheeled dual-arm humanoids: a complete 19-DoF mobile bimanual platform at ~$16k undercuts research platforms from Galaxea, ARX or AgileX and virtually every Western equivalent. Its distribution network and 10k+ install base of cobots give it a channel into every robotics teaching lab. Payload (1 kg/arm) confines it to education/research and light demonstration tasks, so it is not a threat in industrial or logistics deployments — but it shapes buyer price expectations at the entry level and seeds the developer ecosystem around its APIs.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.elephantrobotics.com/en/mercury-x1-en/ | Mercury series design, software stack, S570 teleop | vendor-claimed |
| 2 | https://wikitia.com/wiki/Elephant_Robotics + https://www.elephantrobotics.com/en/our-company/ | founding, funding, myCobot sales | third-party / vendor-claimed |
| 3 | https://shop.elephantrobotics.com/products/mercury-humanoid-robot-series | Mercury A1/B1/X1 variants, Power Spring joints | vendor-claimed |
| 4 | https://www.cnx-software.com/2024/11/22/mercury-x1-wheeled-humanoid-robot-combines-nvidia-jetson-xavier-nx-ai-controller-and-esp32-motor-control-boards/ | X1 price $15,999, compute evolution | third-party |
