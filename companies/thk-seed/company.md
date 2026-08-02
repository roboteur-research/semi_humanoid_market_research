# THK / SEED Solutions (THK株式会社 / SEEDソリューションズ)

| Field | Value |
|---|---|
| HQ | Tokyo, Japan (THK Co., Ltd.) |
| Founded | 1971 (THK); SEED Solutions service-robot business active since mid-2010s |
| Founders / key people | THK founded by Hiroshi Teramachi; SEED Solutions is THK's next-generation service-robot RT-system business |
| Employees (approx.) | ~10,000+ group-wide (THK, listed manufacturer) |
| Ownership / listing | Listed — Tokyo Stock Exchange Prime, ticker 6481 |
| Total funding / valuation | n/a (listed industrial; robotics is an internal business line) |
| Semi-humanoid products | [SEED-Noid / SEED-R7 series](seed-noid/robot.md) |
| Other products | LM guides (world leader in linear-motion components), ball screws, actuators, SEED smart actuators, "Simple Automation" modules |
| Website | https://www.seed-solutions.net/ / https://www.thk.com/ |

## Company background
THK is Japan's dominant linear-motion component maker (LM guides, ball screws) and a tier-one supplier to the global machine-tool and robot industry. SEED Solutions is THK's service-robotics arm: a "next-generation service robot RT system" built around THK's own smart actuators — compact, daisy-chain-wired servo units — plus unitized mechanical modules, intended to let customers assemble service robots without doing mechanical, electrical and low-level software design themselves. [S1][S2]

The flagship of this program is the SEED-R7 platform-robot series: SEED-Noid (life-size upper-body humanoid), SEED-Lifter (vertical elevation unit) and SEED-Mover (omnidirectional cart), which can be bought individually or combined into a full mobile semi-humanoid. SEED-Noid was supplied as a common research platform in the World Robot Summit ecosystem (Future Convenience Store Challenge era, 2018) and has open ROS packages (seed_r7_ros_pkg). THK formally opened order intake for the SEED-R7 series on 1 June 2021. [S2][S3][S4]

Go-to-market is B2B platform sales to robot developers and integrators rather than end-user deployment; a notable external validation was NTT Communications selecting SEED-Noid-Mover for its ExTorch Open Innovation Program (May 2021). [S5]

## Relevance to the semi-humanoid market
THK matters less as a robot vendor than as the component giant one layer down: SEED-R7 is effectively a reference design proving THK actuators/modules for anyone building wheeled humanoids, and THK components appear across the industry's supply chains. The Noid+Lifter+Mover modular decomposition (buy only the units you need) anticipated the architecture now standard in commercial semi-humanoids. Volume traction of SEED-R7 itself appears modest (research/development platform, orders since 2021, no public unit counts) — the strategic significance is THK positioning for the humanoid components market. [S2][S3]

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.thk.com/ | THK corporate facts | vendor-claimed |
| 2 | https://prtimes.jp/main/html/rd/p/000000010.000069594.html | SEED-R7 series order start 2021-06-01, unit lineup, smart actuators | vendor-claimed |
| 3 | https://github.com/seed-solutions/seed_r7_ros_pkg | open ROS packages, MoveIt/nav integration | vendor-claimed |
| 4 | https://www.automation-news.jp/2021/06/56672/ | series composition, positioning | third-party |
| 5 | https://www.thk.com/jp/ja/news/products/article-17052021-1.html | NTT Communications ExTorch adoption of SEED-Noid-Mover | vendor-claimed |
