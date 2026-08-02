# ByteDance (字节跳动) — Seed Robotics team

| Field | Value |
|---|---|
| HQ | Beijing, China (Seed team also Shanghai/Shenzhen/Singapore/US) |
| Founded | 2012 (ByteDance); Seed research org ~2023 |
| Founders / key people | Zhang Yiming (ByteDance founder); Seed Robotics team (GR-series authors) |
| Employees (approx.) | >110,000 (ByteDance group) |
| Ownership / listing | Private (world's most valuable startup class) |
| Total funding / valuation | Corporate-funded; no external robotics funding |
| Semi-humanoid products | [ByteMini](bytemini/robot.md) — internal research platform, not a product |
| Other products | TikTok/Douyin, Doubao LLMs; robotics models GR-1/GR-2/GR-3, GR-Dexter, GR-RL |
| Website | https://seed.bytedance.com/en/direction/robotics |

## Company background
ByteDance's Seed team is the company's frontier AI research organization; its robotics direction develops generalist robot policies (VLA models) rather than commercial robot hardware. The GR series culminated in GR-3 (technical report July 2025, arXiv 2507.15493), a large-scale vision-language-action model co-trained on web-scale vision-language data, VR-collected human trajectories and robot teleoperation data [S1][S2]. To embody GR-3, the team built ByteMini, a 22-DoF bimanual wheeled mobile robot. Follow-on reports GR-Dexter and GR-RL (Dec 2025) extend the platform toward dexterous multi-finger hands and long-horizon RL [S3].

## Relevance to the semi-humanoid market
ByteDance is not selling robots: ByteMini exists to generate and consume manipulation data for Seed's VLA research. Its relevance is indirect but significant — a hyperscaler validating the wheeled bimanual form factor (rather than legs) as the reference embodiment for VLA research, and a potential future software supplier ("brains") to Chinese hardware makers. Any ByteDance hardware commercialization would be a major market event but is currently not announced.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://arxiv.org/abs/2507.15493 | GR-3 technical report, ByteMini introduction, July 2025 | third-party (peer-visible preprint) |
| 2 | https://seed.bytedance.com/en/blog/seed-research-gr-3-released-a-generalist-robot-model-for-generalization-long-horizon-tasks-and-bi-manual-deformable-object-manipulation | GR-3/ByteMini capabilities, task demos | vendor-claimed |
| 3 | https://arxiv.org/pdf/2512.24210 | GR-Dexter follow-on (dexterous hands) | third-party (preprint) |
