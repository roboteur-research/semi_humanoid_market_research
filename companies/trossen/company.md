# Trossen Robotics

| Field | Value |
|---|---|
| HQ | Downers Grove, Illinois, USA |
| Founded | ~2004-2005 |
| Founders / key people | Matt Trossen (founder) |
| Employees (approx.) | n/a (small; ~20-year-old SME) |
| Ownership / listing | Private |
| Total funding / valuation | n/a (bootstrapped/no disclosed VC rounds) |
| Semi-humanoid products | [mobile-ai/](mobile-ai/robot.md) — Mobile AI bimanual wheeled data-collection platform (successor to the licensed Mobile ALOHA kit) |
| Other products | Stationary AI ($15,995 sale / $23,995.95 list), Solo AI single-arm ($7,995+), WidowX AI arms ($2,995+), TRumi gripper, SLATE UGV base, AgileX UGVs (Scout/Tracer distribution), Interbotix arm line (PhantomX/WidowX 250/ViperX 300), TOTL ML workstation (RTX 5090) |
| Website | https://www.trossenrobotics.com |

## Company background
Trossen Robotics is a two-decade-old Illinois robotics hardware supplier (founded by Matt Trossen ~2004-2005) that grew from hobby/education kits into the de-facto hardware vendor of the embodied-AI research boom [S4]. Its Interbotix arms (WidowX 250, ViperX 300) were chosen by Stanford's ALOHA project (Tony Zhao, Zipeng Fu, Chelsea Finn et al.) as the "A LOw-cost Open-source HArdware" for bimanual teleoperation and imitation learning; Trossen then productized the official ALOHA / ALOHA 2 / Mobile ALOHA kits, in collaboration threads spanning Stanford, UC Berkeley and Google DeepMind (ALOHA 2, ALOHA Unleashed) [S2][S3]. Mobile ALOHA — two ViperX follower arms plus leader arms on an AgileX wheeled base — became one of the most cited low-cost robot-learning platforms of 2024, and Trossen was the place to buy it.

In 2025 Trossen replaced the legacy ALOHA kits with its own-IP "Trossen AI" line (announced availability late Q1 2025): WidowX AI arms (6-DoF, 1.5 kg at full reach, QDD-hybrid servos, in-house iNerve controller, 10 kHz+ async data protocol) packaged as Solo AI, Stationary AI and Mobile AI kits, the last putting dual leader-follower arm pairs on its SLATE differential-drive UGV [S1][S5]. Go-to-market is direct e-commerce with 2-3-week production lead times, lifetime support, plus EU/international resellers (e.g. Generation Robots). The software strategy is deliberately ecosystem-native: Hugging Face LeRobot integration, MuJoCo/Isaac/Gazebo sim support, and compatibility with ACT, OCTO, ALOHA Unleashed and Physical Intelligence's π0 — Trossen even advises customers to buy the same maple-top table used in π0/Gemini training datasets for visual consistency [S1][S6].

## Relevance to the semi-humanoid market
Trossen is not building a service humanoid; it supplies the picks and shovels of the VLA/imitation-learning wave. Its kits define the entry price for bimanual mobile manipulation research (~$23k on sale vs ~$80-90k for a Dexmate Vega, ~$70k Reachy 2), and its ALOHA lineage means an enormous installed base in exactly the labs (and companies like Physical Intelligence and DeepMind) whose models will run tomorrow's semi-humanoids. For an EU entrant, Trossen matters as (a) the benchmark for research-segment pricing, (b) a channel/ecosystem to be compatible with (LeRobot, ALOHA data formats), and (c) evidence that open, cheap, teleop-first hardware wins academic mindshare. Trajectory: doubling down on data-collection tooling and own-IP arms; no sign of moving into integrated service robots.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.trossenrobotics.com/aloha + /ai | Trossen AI line, pricing (WidowX AI $2,995+, Solo $7,995+, Mobile $22,995 sale), iNerve/QDD servo tech, LeRobot + model compatibility | vendor-claimed |
| 2 | https://www.trossenrobotics.com/the-aloha-project | ALOHA project history, Stanford/UC Berkeley/Google DeepMind collaborations, four whitepapers (ALOHA, ALOHA 2, Mobile, Unleashed) | vendor-claimed |
| 3 | https://mobile-aloha.github.io/ | Stanford Mobile ALOHA authorship (Fu/Zhao/Finn), ViperX/WidowX arms, AgileX base | third-party (academic) |
| 4 | https://www.trossenrobotics.com/post/how-to-select-robotic-arm-for-ai-research + Generation Robots reseller listings | Company age (~20 years), founder, WidowX AI specs, EU distribution | vendor-claimed / third-party |
| 5 | https://fox4kc.com/business/press-releases/ein-presswire/788100763/ | Trossen AI launch press release, late Q1 2025 availability | vendor-claimed (press release) |
| 6 | https://www.trossenrobotics.com/stationary-ai | Stationary AI $15,995 (list $23,995.95), 4x RealSense D405, TOTL workstation bundle, π0/Gemini dataset-table note | vendor-claimed |
