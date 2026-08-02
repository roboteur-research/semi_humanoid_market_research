# AgiBot / Zhiyuan Robotics (智元机器人)

| Field | Value |
|---|---|
| HQ | Shanghai, China |
| Founded | February 2023 |
| Founders / key people | Deng Taihua (邓泰华, Chairman/CEO, ex-Huawei VP); Peng Zhihui (彭志辉 "稚晖君", co-founder/CTO, ex-Huawei "genius youth", 2.7M+ Bilibili followers) [third-party] |
| Employees (approx.) | n/a (not disclosed); >1,000 estimated from hiring/press scale [estimated] |
| Ownership / listing | Private core company; de-facto listed via backdoor: acquired 63.62% of STAR-Market-listed Shangwei New Materials (上纬新材, 688585) for ~RMB 2.1B, completed 11/2025; Shangwei stock rose ~10.8x in 16 days [third-party] |
| Total funding / valuation | 11+ rounds; investors incl. Hillhouse, BYD, Sequoia China, Tencent (led 03/2025 round), JD.com, LG Electronics + Mirae Asset (08/2025). Valuation ~RMB 15B (~$2.1B) as of 05/2025; HK IPO reportedly explored [third-party] |
| Semi-humanoid products | [远征 A2-W](a2-w/robot.md) (wheeled industrial), [精灵 Genie G2](genie-g2/robot.md) (wheeled interactive/industrial; Genie G1 history covered there) |
| Other products | 远征 A2 / A2 Max / A3 (bipeds), A2 Lite/Youth, 灵犀 Lingxi X1 (open-source biped, buildable <$20k), Lingxi X2 / X2-N (wheel-leg hybrid), OmniHand O12 dexterous hand, AimRT middleware |
| Website | https://www.agibot.com |

## Company background
AgiBot (Zhiyuan Robotics, 智元机器人) was founded in Shanghai in February 2023 by former Huawei VP Deng Taihua and celebrity engineer Peng Zhihui ("Zhihui Jun"). In under three years it became one of the two dominant Chinese humanoid makers by volume: it shipped 5,100+ units in 2025 (Omdia; ~39% of global humanoid shipments in that count), was first to roll its 5,000th production unit off the line (2025-12-08), passed ~10,000 cumulative units around 03/2026, and celebrated its 15,000th robot off the line in 06/2026 — on pace for its 10k+/year 2026 target (also showing Genie G2 at STK in Seoul) [third-party]. Its product strategy spans bipeds (Yuanzheng A2/A3, Lingxi X1/X2) and wheeled semi-humanoids (A2-W, Genie G1/G2) — Chinese press treats it as the de-facto wheeled-humanoid market leader.

AgiBot pursues an unusually open AI/data strategy: the AgiBot World dataset (1M+ real robot trajectories, 217 tasks, collected on Genie-series wheeled robots in a dedicated data-collection facility) underpins its GO-1 (03/2025, ViLLA architecture) and GO-2 (04/2026, Action Chain-of-Thought, 98.5% on LIBERO) foundation models; the Lingxi X1 robot and AimRT real-time middleware are open source [vendor-claimed/third-party]. Capital strategy is equally aggressive: 11+ funding rounds (Tencent-led 03/2025; LG/Mirae 08/2025) and the RMB 2.1B backdoor listing via Shangwei New Materials completed 11/2025, giving it public-market access while peers wait for IPO windows [third-party].

Go-to-market is direct B2B plus channel resellers (RobotShop, Generation Robots carry datasheets in the West). Commercial anchors: Fulin Precision (富临精工) ordered ~100 A2-W for auto-parts factories (08/2025, tens of millions RMB — billed as China's first at-scale industrial embodied-robot contract); Longcheer (龙旗科技) placed a "hundreds of millions RMB" framework order (~1,000 units) of Genie G2 for tablet manufacturing (10/2025); China Mobile RMB 78M order; RMB 124M joint win with Unitree [third-party]. Pricing spans ¥400-800k (A2-W insider range) down to A2 Lite at $44,560 and Lingxi X2 Youth <$14k [estimated/third-party].

## Relevance to the semi-humanoid market
AgiBot is arguably the single most important competitor in the wheeled semi-humanoid segment worldwide: top-2 global shipment volume, the largest verified industrial orders for wheeled dual-arm robots (Fulin, Longcheer), a data flywheel (AgiBot World → GO-2) built specifically on wheeled platforms, and public-market funding. Trajectory is steeply scaling up (5k units 2025 → 10k target 2026). For any EU entrant, AgiBot defines the reference price-performance curve in industrial wheeled manipulation.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.agibot.com | Official site, product family | vendor-claimed |
| 2 | https://eu.36kr.com/en/p/3371292992477316 | Shangwei backdoor listing (63.62%, RMB 2.1B), valuation RMB 15B, investors | third-party |
| 3 | https://cn.chinadaily.com.cn/a/202508/11/WS6899903da310626720042078.html | Fulin Precision ~100-unit A2-W order, first industrial-scale embodied contract | third-party |
| 4 | https://qiye.chinadaily.com.cn/a/202510/16/WS68f0b2b8a310c4deea5ecac8.html | Genie G2 launch 2025-10-16, Longcheer order | third-party |
| 5 | https://interactanalysis.com/insight/humanoid-robot-production-surges/ | AgiBot >5k units shipped 2025 | third-party |
| 6 | https://finance.sina.com.cn/stock/relnews/hk/2026-01-09/doc-inhfswxt0516492.shtml | Omdia: AgiBot 5,100+ units 2025 (39% share) | third-party |
| 7 | https://www.trendforce.com/presscenter/news/20260409-13007.html | 10k cumulative by late Mar 2026; Unitree+AgiBot ≈80% of CN shipments | third-party |
| 8 | _work/market_context.md (§3, §4.3, §5.1-5.2) | Funding history, GO-1/GO-2, AgiBot World, price bands | third-party (compiled) |
