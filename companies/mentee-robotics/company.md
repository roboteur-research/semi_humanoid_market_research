# Mentee Robotics (Mentee by Mobileye)

| Field | Value |
|---|---|
| HQ | Herzliya, Israel |
| Founded | 2022 (emerged from stealth April 2024) |
| Founders / key people | Prof. Amnon Shashua (co-founder; also Mobileye co-founder/CEO), Prof. Lior Wolf (CEO), Prof. Shai Shalev-Shwartz |
| Employees (approx.) | n/a (not disclosed; "deep AI talent" cited in acquisition PR) |
| Ownership / listing | Acquired by Mobileye Global (NASDAQ: MBLY) — announced CES 2026 (Jan 2026), completed 2026-02-03; now "Mentee by Mobileye" |
| Total funding / valuation | Acquisition consideration $900M (~$612M cash + up to ~26.2M MBLY Class A shares); earlier VC rounds n/a |
| Semi-humanoid products | [MenteeBot (wheeled-variant question)](menteebot-wheeled/robot.md) — see note: wheeled variant NOT verified; flagship is the bipedal MenteeBot V3.0 |
| Other products | none (single humanoid platform, vertically integrated) |
| Website | https://www.menteebot.com |

## Company background
Mentee Robotics was founded in 2022 in Herzliya by three of Israel's most prominent AI figures — Amnon Shashua (Mobileye, OrCam, AI21), Lior Wolf (ex-Meta AI research, Tel Aviv Univ.) and Shai Shalev-Shwartz (Mobileye CTO). It de-cloaked in April 2024 with MenteeBot V1, pitching an "AI-first" humanoid: Sim2Real reinforcement learning, NeRF-based 3-D mapping, LLM-driven task reasoning, camera-centric (lidar-free) sensing [S3][S4]. **MenteeBot V3.0** (announced 17 Feb 2025) is the third-generation bipedal platform: 175 cm, ~70 kg, 25 kg lift, 1.5 m/s walk, hot-swappable battery for 3+ h operation, dual Jetson AGX Orin, custom actuators claimed 3× power density, 360° camera vision (back + fisheye side cameras), ~40 DoF with high-pinch-force hands [S2][S4].

At CES 2026 **Mobileye announced the $900M acquisition** of Mentee (Shashua recused himself from the Mobileye board vote); the deal closed 3 Feb 2026. The combined pitch is "Physical AI" spanning autonomous driving and humanoids, using Mobileye's production/automotive-grade engineering to industrialize Mentee's platform: first on-site customer proof-of-concepts in 2026, series production and commercialization targeted 2028 [S1][S5]. Demonstrated use cases center on warehouse logistics (uncut 18-min video of two V3 units collaboratively sorting/moving boxes) and long-term household ambitions [S6].

## Relevance to the semi-humanoid market
Mentee is primarily a **bipedal** competitor — our sweep found no confirmed wheeled variant (the "modular biped-or-wheels lower body" note in discovery appears to be a mix-up with UK startup Humanoid's HMND-01; see robot.md). Its relevance to wheeled semi-humanoid players is strategic: a $900M-backed, automotive-industrialized, camera-only AI stack out of Israel targeting the same warehouse/logistics tasks as wheeled platforms, with series production planned for 2028. If Mobileye's cost engineering delivers, the biped-vs-wheeled price gap could narrow — the core structural advantage EU wheeled entrants currently enjoy.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://www.mobileye.com/news/mobileye-to-acquire-mentee-robotics-to-accelerate-physical-ai-leadership/ | $900M acquisition, deal structure, 2026 POCs, 2028 series production | vendor-claimed |
| S2 | https://interestingengineering.com/innovation/israel-humanoid-robot-with-360-vision | V3.0 specs (175 cm, 25 kg lift, 1.5 m/s, 3h battery, 2× Jetson AGX Orin, 360° vision), Feb 2025 | third-party |
| S3 | https://www.therobotreport.com/mentee-robotics-de-cloaks-launches-ai-driven-humanoid-robot/ | Founding team, April 2024 de-cloak, AI-first approach | third-party |
| S4 | https://www.aparobot.com/robots/menteebot | 70 kg weight, 40 DoF, 30N pinch/finger, tactile sensors, camera-only production plan | third-party |
| S5 | https://www.robotics247.com/article/ces-2026-mobileye-set-to-acquire-humanoid-robot-startup-mentee-robotics-for-900m | CES 2026 announcement, completion 2026-02-03 | third-party |
| S6 | https://interestingengineering.com/ai-robotics/humanoid-robot-pair-32-boxes | Warehouse dual-robot box-sorting demo | third-party |


**Corpus note (2026-08-02):** the robot subfolder for a "wheeled MenteeBot" was removed — no such variant exists (early discovery confusion with Humanoid's HMND-01). Company profile retained for the Mobileye acquisition context ($900M, closed 2026-02-03); MenteeBot itself is bipedal and out of scope.
