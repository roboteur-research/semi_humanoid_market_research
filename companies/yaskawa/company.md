# Yaskawa Electric (安川電機)

| Field | Value |
|---|---|
| HQ | Kitakyushu, Fukuoka, Japan |
| Founded | 1915 |
| Founders / key people | Keiichiro Yasukawa (founding family); robotics division = Yaskawa MOTOMAN |
| Employees (approx.) | ~13,000 group (estimated) |
| Ownership / listing | Listed, TYO:6506 |
| Total funding / valuation | Public company; revenue ~¥500-580B/yr (estimated); world's leading servo/inverter maker, top-3 industrial robot maker (~600k cumulative MOTOMAN robots, estimated) |
| Semi-humanoid products | [motoman-next-nhc10de/](motoman-next-nhc10de/) — AI dual-arm (iREX 12/2025, release 2026); legacy: MOTOMAN-SDA 15-axis dual-arm series (shipping since mid-2000s); SmartPal service-robot research line (2005-2010s, never commercialized) |
| Other products | MOTOMAN industrial arms (GP/AR/HC series), MZ cobots, servo motors/drives (Sigma), inverters, i3-Mechatronics factory-digitalization stack |
| Website | https://www.yaskawa.co.jp / https://www.e-mechatronics.com |

## Company background
Yaskawa is one of the "big four" industrial-robot makers and the world's dominant servo supplier — it launched Japan's first all-electric industrial robot (MOTOMAN-L10, 1977) and coined the word "mechatronics." Its dual-arm heritage is long: the **MOTOMAN-SDA series** (SDA5/10/20; 15 axes = 2×7-axis arms + torso rotation; 5/10/20kg per arm; reach 843-1,323mm) has shipped since the mid-2000s for cell assembly, and the **SmartPal** wheeled service humanoid line (2005 Aichi Expo through SmartPal V/VII, ~132cm, 21-DoF, 2×7-axis arms, 2kg payload) was a full semi-humanoid a decade too early — it never commercialized and remains Yaskawa's in-house cautionary tale [S3][S4].

In 2023 Yaskawa launched **MOTOMAN NEXT**, billed as the industry's first autonomous-decision industrial robot line (AI judgment layer atop the controller) [S5]. At **iREX 2025 (3-6 Dec)** it unveiled the **MOTOMAN NEXT-NHC10DE**, an AI dual-arm robot with tactile fingertip sensors, trained via imitation learning and NVIDIA Isaac Sim/Isaac Lab synthetic data, demonstrating picking/packing; commercial release is slated for **2026** [S1][S2]. Strategy language is "engineering-less" automation — removing teaching/integration cost — plus a **SoftBank partnership on "physical AI" robots using AI-RAN** communications [S2]. Yaskawa runs its own NVIDIA-partnered AI subsidiary (AI Cube, "MOTOMAN NEXT" AI models) and manufactures in Japan, China, Slovenia and the US.

## Relevance to the semi-humanoid market
Yaskawa's entry is the strongest incumbent validation the dual-arm semi-humanoid category has received: the company that supplies servos to half the robot industry is productizing an AI dual-arm with tactile hands and sim-trained skills, at industrial reliability grades and with a global sales/service network in place. Expect aggressive vertical-integration economics (in-house motors/drives) and immediate credibility in EU factories, where Yaskawa already has manufacturing (Slovenia) and channel. Trajectory: scaling into the category from above — arguably the most dangerous long-term competitor for any EU industrial semi-humanoid entrant, though its DNA (fixed/cell automation) leaves mobile service niches open.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://monoist.itmedia.co.jp/mn/articles/2512/04/news059.html | NHC10DE iREX 2025 debut, 10kg, tactile fingertips, imitation learning, Isaac Sim/Lab, 2026 release | third-party |
| 2 | https://www.today-jp.com/news/irex-2025-yaskawa-ai-cobots-engineeringless-manufacturing-strategy | engineering-less strategy, SoftBank AI-RAN partnership, MZ cobot | third-party |
| 3 | https://www.e-mechatronics.com/product/robot/lineup/sda/index.html | SDA5/10/20 specs (15 axes, payloads, reach) | vendor-claimed |
| 4 | https://www.yaskawa.co.jp/newsrelease/technology/8933 | SmartPal V specs (2007): 1,325mm, 127kg, 21 DoF, 2×7-axis arms, 2kg, waist, 3.6km/h | vendor-claimed |
| 5 | https://www.yaskawa.co.jp/motoman-next/ | MOTOMAN NEXT series 2023, autonomous-decision positioning, application domains | vendor-claimed |
