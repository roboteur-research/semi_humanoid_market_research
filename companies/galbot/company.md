# Galbot / Galaxy General (银河通用机器人)

| Field | Value |
|---|---|
| HQ | Beijing, China |
| Founded | May 2023 |
| Founders / key people | Wang He (王鹤, founder/CTO-scientist, b. 1992; PKU assistant professor, EPIC Lab founder; Tsinghua BSc, Stanford PhD under Leonidas Guibas) [third-party] |
| Employees (approx.) | n/a (not disclosed); several hundred [estimated] |
| Ownership / listing | Private |
| Total funding / valuation | Lifetime ~$1.15B: angel/pre-A RMB 700M; strategic RMB 500M (2024); Series B 06/2025 RMB 1.1B (CATL lead, unicorn); Series C 12/2025 >$300M @ ~$3B (China Mobile fund, CICC); Series D 03/2026 RMB 2.5B (~$350M; national IC "Big Fund", Sinopec, CITIC, SAIC, Bank of China). Other backers: HKIC, Meituan [third-party] |
| Semi-humanoid products | [Galbot G1](g1/robot.md) (wheeled + telescoping-leg dual-arm); [Galbot S1](s1/robot.md) (heavy-industrial wheeled dual-arm, Jan 2026, 30 kg/arm, deployed at CATL) |
| Other products | GraspVLA / SynGrasp-1B grasping foundation model + synthetic dataset; unmanned "Galbot store/pharmacy" kiosk system; G1 Premium/factory variants |
| Website | https://www.galbot.com |

## Company background
Galbot (Beijing Galaxy General Robot Co., 银河通用) was spun out of Peking University's embodied-AI research in May 2023 by Wang He, and has become the best-funded pure-play wheeled semi-humanoid company in China (~$1.15B lifetime, ~$3B valuation at Series C, state-strategic Series D investors including the national IC Big Fund, Sinopec, CITIC, SAIC and Bank of China) [third-party]. Its founding thesis is explicitly anti-biped: Wang He argues a wheeled chassis is ~10x cheaper than legs and more stable, freeing budget for manipulation intelligence [third-party].

Technology strategy centers on simulation-first learning: the SynGrasp-1B billion-scale synthetic grasping dataset pre-trains GraspVLA, a grasping foundation model doing zero-shot open-vocabulary grasping (99.5% claimed success across ~5,000 pharmacy SKUs) [vendor-claimed/third-party]. The commercial wedge is unusual for the sector: 24/7 unmanned retail. Galbot operates ~170 robot-run kiosk stores/pharmacies in 40+ cities (target 100+ flagship stores end-2026), and on 2026-03-12 obtained a pharmaceutical retail license in Beijing Haidian — billed as China's first drugstore license issued around a robot operator, with G1 robots picking up to 370 orders/day in 70 m² stores [third-party].

In January 2026 Galbot released the S1, a second, heavy-industrial wheeled model (1.79 m, 320 kg, up to 30 kg per arm / ~50 kg dual-arm, 2.3 m working-height coverage, 8 h runtime with autonomous charging, "zero-teleoperation" autonomy) reported in regular use on CATL production lines — confirming "S1" is a real second model, not a mislabel of the G1 [see s1/].

Second leg: factory logistics/assembly pilots and orders — CATL ("world's first AI humanoid robot in regular operation" claim), Mercedes-Benz China (sunroof transfer), Bosch, Toyota, BAIC, SAIC, Zeekr, BYD (15% efficiency-gain claim); orders "several thousand units" cumulative per vendor [vendor-claimed; BMW pilot unverified]. Go-to-market is direct plus a JD.com storefront (G1 listed ¥690-700k, flash sale ¥630k 02/2026) and enterprise software subscriptions (~$27k/robot/yr) [third-party/estimated].

## Relevance to the semi-humanoid market
Galbot is the flagship proof that wheeled semi-humanoids can run real, revenue-generating, unmanned commercial operations today — not just factory pilots. Its pharmacy fleet is the largest publicly verifiable retail deployment of manipulating semi-humanoids worldwide, and its funding base ties it into China's state industrial policy. Trajectory: scaling aggressively in both retail and automotive/battery logistics. For an EU entrant, Galbot defines the retail/pharmacy use-case benchmark and the "simulation-first, no-teleop-army" data strategy alternative.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.galbot.com | Official site | vendor-claimed |
| 2 | https://technode.com/2026/03/02/humanoid-robot-maker-galbot-raises-rmb-2-5-billion/ | Series D RMB 2.5B, investor list, cumulative funding | third-party |
| 3 | https://chozan.co/galbot-g1/ | Pharmacy ops detail (370 orders/day, 5,000 SKUs, 99.5%), pricing ¥630-700k, customers | third-party |
| 4 | https://arxiv.org/abs/2505.03233 | GraspVLA / SynGrasp-1B | third-party (paper) |
| 5 | _work/market_context.md §2.1, §3, §7 | Wang He wheels-vs-legs rationale; funding history; ~170 kiosks, license 2026-03-12, factory customers | third-party (compiled) |
| 6 | DuckDuckGo-indexed CN sources (founding search) | Founded 05/2023, Wang He bio | third-party |
