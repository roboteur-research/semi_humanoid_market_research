# Open Droids (OpenDroids)

| Field | Value |
|---|---|
| HQ | Wichita, Kansas, USA (site contact coordinates 37.69°N/97.34°W = Wichita); founded in / early press datelined San Francisco, CA |
| Founded | March 2024 |
| Founders / key people | Abhishek Gupta, Jackson Jesionowski (public persona "Jack Jay"), Ashish Gupta [S1][S3] |
| Employees (approx.) | n/a (not disclosed); hiring in US, Canada, India (2024) [S1] |
| Ownership / listing | Private |
| Total funding / valuation | Amounts not disclosed. Backers per company site: "funded by the founder of Tether", DNA Fund, Percival, Blockchain Founders Fund, Welara (crypto-ecosystem investors) [S2, vendor-claimed] |
| Semi-humanoid products | [r2d3/](r2d3/) — dual-arm mobile manipulator |
| Other products | R1D1 single 6-DoF-arm mobile manipulator ($18,500), R1D3 single 7-DoF-arm service robot, DH116 dexterous hand (11-16 DoF class, 30 kg hook load, 508-dot tactile, EtherCAT), motion-capture data-collection glove |
| Website | https://www.opendroids.com |

## Company background
Open Droids is a 2024-vintage US startup building low-cost, open-source mobile manipulators. It launched the single-arm R1D1 in August 2024 ($18,500; 6-DoF arm, 3 kg payload, 1.22 m lift column, AMR base) and showed the dual-arm R2D3 at CES 2025, where co-founder Jack Jay pitched it as "a Roomba on crack" for household and back-of-house restaurant chores [S1][S3]. The company's differentiator is openness: full ROS 2 stacks for its robots are published on GitHub under Apache 2.0 (github.com/Open-Droids-robot), and hardware is positioned as modifiable by the community.

The GitHub sources reveal an integrator model rather than deep in-house hardware development: R2D3 is assembled from Chinese RealMan RM75-B 7-DoF arms, a Woosh AGV chassis, RealSense cameras and RealMan dexterous hands/grippers (see robot dossier) [S4, third-party]. Funding comes from crypto-adjacent investors (Tether-founder circle, DNA Fund, Blockchain Founders Fund); the company also advertises Google DeepMind and NVIDIA (Inception) partnerships on its homepage — both should be read as marketing-level affiliations, not disclosed commercial contracts [S2, vendor-claimed].

Go-to-market is direct sale at aggressive price points ($18.5k single-arm, ~$55-60k dual-arm, ~1 month lead time claimed), plus side products (DH116 hand, data glove) that target the embodied-AI data-collection market. Early traction claims include pilot programs in rehabilitation centers and pre-order talks with food franchises (Baskin-Robbins, Subway) [S1][S3, vendor-claimed].

## Relevance to the semi-humanoid market
Open Droids matters as a price disruptor and open-source rallying point in the US market: a $55k dual-arm mobile manipulator with a public ROS 2 stack undercuts most Western competitors. However, because the platform is largely re-badged Chinese components (RealMan, Woosh), its moat is thin, and its crypto-investor base and small team make execution uncertain. Trajectory: expanding product line (R1D3, hand, glove) and visibility (CES 2025, ITU AI for Good), but no evidence of volume deployments.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.therobotreport.com/open-droids-develops-both-single-dual-arm-mobile-manipulators/ | Founders, founding date, R1D1 specs/price, target customers | third-party |
| 2 | https://www.opendroids.com/ | Product line, investors, DeepMind/NVIDIA partnership claims, Wichita coordinates | vendor-claimed |
| 3 | https://tech.yahoo.com/general/articles/ces-unveiled-2025-opendroids-r2d3-042543404.html | CES 2025 demo, ~$60k price, rehab pilots, Jack Jay quotes | third-party |
| 4 | https://github.com/Open-Droids-robot/R2D3_ros2 | RealMan/Woosh component sourcing, Apache 2.0 ROS 2 stack | third-party (primary code) |
