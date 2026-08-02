# Toyota Research Institute (TRI)

| Field | Value |
|---|---|
| HQ | Los Altos, CA, USA (also Cambridge, MA; Ann Arbor, MI) |
| Founded | 2015 (operational Jan 2016) |
| Founders / key people | Gill Pratt (CEO, ex-DARPA Robotics Challenge); Russ Tedrake (VP Robotics Research, MIT); Punyo "Tactile Team" (Alex Alspach et al.) |
| Employees (approx.) | ~300+ |
| Ownership / listing | subsidiary of Toyota Motor Corporation (TYO: 7203) |
| Total funding / valuation | USD 1B initial 5-year commitment from Toyota (2015); ongoing corporate funding |
| Semi-humanoid products | [punyo/](punyo/) (research platform, not for sale) |
| Other products | dual-arm Franka-based LBM research stations; Diffusion Policy (with Columbia); Large Behavior Models; earlier: T-HR3, HSR (Toyota parent) |
| Website | https://www.tri.global/ ; https://punyo.tech/ |

## Company background
TRI is Toyota's US advanced-research arm, created in 2015 with a $1B commitment under Gill Pratt to work on automated driving, robotics and machine learning, with an explicit mission around amplifying people (eldercare motivation from Japan's demographics). Its robotics division under Russ Tedrake became one of the most influential manipulation-learning groups: Diffusion Policy (2023, with Columbia's Shuran Song/Cheng Chi) and the Large Behavior Models (LBM) program — training a single model on hundreds of teleoperated bimanual skills — set much of the current VLA agenda, and in 2024 TRI partnered with Boston Dynamics to bring LBMs to Atlas [S1][S4]. In January 2026 the LBM program was spun out as Walden Robotics (Tedrake as CEO; $300M seed at $1.1B, out of stealth 2026-07-15) — see [companies/walden-robotics/](../walden-robotics/company.md).

Punyo is TRI's hardware thesis: instead of rigid precision, cover off-the-shelf arms and a torso with air-filled tactile "bubbles" so the robot can hug, brace and carry large objects against its body the way humans actually do. It began as Punyo-1 (paper Nov 2021, RoboSoft 2022) and was relaunched publicly as the Punyo platform in Feb 2024 [S2][S3]. TRI does not sell robots; everything is research with open publications (and some open hardware for the Soft-Bubble gripper).

## Relevance to the semi-humanoid market
TRI matters as a technology bellwether, not a competitor: whole-body/contact-rich manipulation and soft tactile skins address the payload ceiling that plagues arm-only semi-humanoids (a few kg per gripper vs 5-20 kg hugged against the chest). Its LBM/Diffusion-Policy stack is already the software baseline for many startups. Expect Punyo-style compliant surfaces and body-contact strategies to appear in commercial wheeled humanoids; an EU entrant can read TRI's publications as a free R&D roadmap — while noting Toyota's own commercialization runs through Toyota/Woven and partners, on Toyota's timeline.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.tri.global/ | mission, structure, research areas | vendor-claimed |
| 2 | https://punyo.tech/ | Punyo platform, bubble tech, team contact | vendor-claimed |
| 3 | https://medium.com/toyotaresearch/meet-punyo-tris-soft-robot-for-whole-body-manipulation-research-949c934ac3d8 | Feb 2024 Punyo reveal | vendor-claimed |
| 4 | https://www.therobotreport.com/punyo-soft-robot-from-tri-designed-for-whole-body-manipulation/ | independent coverage, hardware details | third-party |
