# Sunday Robotics (Sunday Inc.)

| Field | Value |
|---|---|
| HQ | Mountain View, California, USA |
| Founded | April 2024 (started in a Silicon Valley "hacker house"/apartment) [S4][S6] |
| Founders / key people | Tony Zhao (CEO; Stanford CS PhD dropout; Mobile ALOHA / ACT lead author), Cheng Chi (CTO; Diffusion Policy and UMI gripper lead author, Stanford/Columbia/TRI) [S1][S4] |
| Employees (approx.) | ~79 (mid-2026, Sacra) to "more than 100" (Zhao, 07/2026) — sources conflict [S3][S4] |
| Ownership / listing | Private, VC-backed |
| Total funding / valuation | ~$200M total; $165M Series B @ $1.15B post (2026-03-12, Coatue lead; Bain Capital Ventures, Fidelity, Tiger Global, Benchmark, Conviction, Xtal); prior ~$35M seed/Series A (Benchmark, Conviction, first check by Sarah Guo/Conviction, 11/2025 disclosed) [S2][S5] |
| Semi-humanoid products | [Memo](memo/robot.md) — wheeled home robot |
| Other products | Skill Capture Glove (data-collection wearable, ~$200-400/unit); ACT-1 / ACT-2 robot foundation models |
| Website | https://www.sunday.ai/ |

## Company background
Sunday Robotics was founded in April 2024 by two of the most-cited young researchers in robot imitation learning: Tony Zhao (Stanford Mobile ALOHA and ACT — Action Chunking with Transformers) and Cheng Chi (Diffusion Policy; UMI hand-held gripper for in-the-wild data collection, a Stanford/Columbia/Toyota Research Institute project). The company stayed in stealth for ~19 months, emerging on 2025-11-20 with Memo, a fully autonomous wheeled home robot, and a training method that deliberately avoids teleoperation [S4][S6]. In March 2026 it raised a $165M Series B led by Coatue at a $1.15B valuation, bringing total funding to ~$200M [S2][S5].

The core strategic bet is full-stack vertical integration ("We think the way to make a home robot is to be full stack" — Zhao [S1]) combined with a capital-efficient data flywheel: instead of teleoperating robots, Sunday pays a distributed workforce of "Memory Developers" (500+ at stealth exit, 2,000+ by mid-2026 per project discovery notes; company says "thousands of gloves shipped") up to ~$60/hour to do chores in their own homes wearing the Skill Capture Glove — a sensorized glove that mirrors the geometry and sensor layout of Memo's 3-finger hand and costs ~$200 to make (WIRED cites ~$400/pair) versus ~$20,000 for a teleop rig [S3][S4][S6]. Roughly 10 million behavioral episodes/trajectories had been collected by mid-2026 [S3]. A "Skill Transform" pipeline converts human-glove motion to robot trajectories at ~90% claimed fidelity [S3]. The robot hand and the glove were co-designed as mirrors of each other — hardware-AI co-design is the company's stated moat. Independent validation: Ken Goldberg (UC Berkeley, Ambi Robotics co-founder) called Memo "a beautiful design, and a much smarter kind of data capture", and WIRED's reporter watched Memo autonomously pull an espresso end-to-end, clear wine glasses (two in one hand) and load a dishwasher at the Mountain View demo home [S1].

Go-to-market is direct B2C: a beta ("Founding Families") program in late 2026 — Zhao has said first deliveries "by Thanksgiving" 2026 — followed by commercial rollout. Current hand-built units cost ~$20,000; Sunday expects the retail price to drop by at least 50% at scale (sub-$10k target) [S7]. Positioning is premium home appliance, justified against a $10-12k/year human housekeeper cost [S3].

## Relevance to the semi-humanoid market
Sunday is THE flagship US consumer semi-humanoid play: a $1.15B-valuation, research-founder-led company that explicitly chose a wheeled base + telescoping spine over legs for cost, safety and battery life, aiming at a <$10k consumer price point. Its ACT-2 result (99.1% zero-shot laundry folding in unseen homes, 785 trials, announced 2026-07-16) is the strongest publicly benchmarked autonomy claim of any home robot vendor, and its proposed "Solve" reporting standard is an attempt to define the category's evaluation rules [S8][S9]. If the beta lands on schedule, Sunday sets the reference price/performance point every EU entrant will be measured against. Main open risks: consumer service/liability layer, Chinese actuator cost advantage, and the 10% glove-to-robot fidelity loss in uncontrolled homes [S3].

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.wired.me/story/this-home-robot-clears-tables-and-loads-the-dishwasher-all-by-itself | founders, full-stack quote, glove ~$400, demos observed, beta timing | third-party (WIRED, 02/2026) |
| 2 | https://techcrunch.com/2026/03/12/humanoid-robotics-maker-sunday-reaches-1-15b-valuation-to-build-household-robots/ | $165M Series B @ $1.15B, Coatue, investor list, waitlist 1,000 | third-party |
| 3 | https://sacra.com/c/sunday/ | ~$200M total, ~79 employees, ~170 lb robot, glove economics, ~10M trajectories, 90% fidelity, pricing model, risks | third-party (analyst) |
| 4 | https://www.businessinsider.com/sunday-robotics-home-robot-training-hands-loading-dishwasher-2025-11 | stealth exit 11/2025, founded 04/2024, 500+ data collectors, $200 vs $20,000 capital efficiency, wine-glass demos | third-party |
| 5 | https://siliconangle.com/2026/03/12/sunday-raises-165m-1-15b-valuation-launch-memo-household-robot/ | $35M prior round 11/2025, investor list, beta within months | third-party |
| 6 | https://www.businessinsider.com/sunday-robotics-memo-home-robot-fold-laundry-99-success-2026-7 | ACT-2 launch 07/2026, >100 employees, glove $200, Solve standard, hacker-house origin | third-party |
| 7 | https://www.sunday.ai/ | ~$20k hand-built cost, ≥50% price drop at scale, beta late 2026, Founding Families | vendor-claimed |
| 8 | https://www.sunday.ai/blog/act-2-preview | ACT-2 99.1%±0.3% on 785 trials, 9 garment types, fold quality 4.72/5 | vendor-claimed |
| 9 | https://html.duckduckgo.com/html/?q=Sunday+Robotics+Memo+ACT-2+laundry+99%25 | corroborating third-party coverage of ACT-2 claim | third-party |
