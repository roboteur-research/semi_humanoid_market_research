# ROBOTIS (로보티즈)

| Field | Value |
|---|---|
| HQ | Seoul (Magok), South Korea |
| Founded | 1999 |
| Founders / key people | Kim Byoung-soo (김병수), founder & CEO (~27.4% stake) |
| Employees (approx.) | n/a (not disclosed; mid-sized, global subsidiaries incl. ROBOTIS America) |
| Ownership / listing | Listed KOSDAQ (Oct 2018, ticker 108490); LG Electronics holds ~7.5% |
| Total funding / valuation | Public company; LG Electronics strategic stake (~7.53%) |
| Semi-humanoid products | [AI Worker (FFW series)](ai-worker/robot.md) |
| Other products | DYNAMIXEL smart actuators (core business), TurtleBot 3 (with Open Robotics), OP/Darwin research humanoids, ThorMang3, delivery robots (GAEMI), open-source robot kits |
| Website | https://www.robotis.com / https://ai.robotis.com |

## Company background
ROBOTIS is Korea's best-known robot components and education company, founded in 1999 by Kim Byoung-soo. Its DYNAMIXEL all-in-one smart actuators are a global de-facto standard in research robotics, and it co-developed TurtleBot 3, one of the most widely used ROS platforms. It listed on KOSDAQ in October 2018; LG Electronics took a strategic stake (~7.5%) and remains a shareholder. This actuator + open-source heritage is the foundation of its "Physical AI" push. [S1][S2]

The AI Worker (FFW series), launched in 2025, is a semi-humanoid built almost entirely from ROBOTIS's own DYNAMIXEL actuators, with a swerve-drive omnidirectional base, dual 7-DoF arms and a Jetson AGX Orin. Its differentiator is radical openness: all source code (ROS 2 packages), simulation models (URDF/MJCF/USD), Docker environments, tutorials, pre-trained models and training datasets (LeRobotDataset format on Hugging Face) are public. The commercial model is selling hardware (leader/follower kits) and actuators into the imitation-learning wave — a "picks and shovels plus reference robot" strategy. [S3][S4]

ROBOTIS is a core industry member of Korea's government-led K-Humanoid Alliance (launched April 2025 by MOTIE), contributing actuators and platforms toward the alliance's goal of a domestic humanoid supply chain (first commercial model targeted ~2028). It exhibited jointly with other Korean robot makers at CES 2026, showing a 20-joint five-finger dexterous hand in development for the FFW series. [S5][S6]

## Relevance to the semi-humanoid market
ROBOTIS matters twice over: as a component supplier to everyone (DYNAMIXEL), and as maker of the only fully open-source commercial semi-humanoid (hardware ~$40k, all software/data free). Reuters covered its approach of capturing skilled human workers' motions for imitation learning (May 2026), signalling credible commercial intent beyond the lab. For an EU entrant, ROBOTIS sets the open-source price/ecosystem benchmark. Trajectory: scaling up, with government (K-Humanoid Alliance) tailwind. [S4][S5][S7]

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | DDG results: ROBOTIS founded 1999 Kim Byoung-soo KOSDAQ | founding 1999, CEO, KOSDAQ Oct 2018, LG 7.53% stake | third-party |
| 2 | https://en.wikipedia.org/wiki/Robotis | DYNAMIXEL, TurtleBot 3, OP series products | third-party |
| 3 | https://ai.robotis.com/ai_worker/hardware_ai_worker | FFW series hardware specs | vendor-claimed |
| 4 | https://www.robotis.com/en/product/ecosystem-aiworker.php + https://ai.robotis.com/opensource.html | full open-source claim (code/sim/data), imitation-learning pipeline | vendor-claimed |
| 5 | Korean press via DDG (로보티즈 K-휴머노이드 얼라이언스; edaily, biz.chosun) | K-Humanoid Alliance core member; CES 2026 20-joint hand | third-party |
| 6 | https://www.upkoreanews.kr/news/articleView.html?idxno=95551 | K-Humanoid Alliance 2028 target | third-party |
| 7 | https://www.business-standard.com/world-news/south-korean-startup-trains-humanoid-robots-using-human-workers-skills-126051200076_1.html (Reuters syndication; access-blocked, per discovery) | Reuters story on training robots with human workers' skills | third-party |
