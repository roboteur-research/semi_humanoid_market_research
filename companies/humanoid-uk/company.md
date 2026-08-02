# Humanoid (Humanoid Ltd / legal entity: SKL Robotics Ltd)

| Field | Value |
|---|---|
| HQ | London, UK (additional offices: Boston, Vancouver, San Diego) [S4][S12] |
| Founded | 2024 [S2][S5] |
| Founders / key people | Artem Sokolov (founder & CEO; founder of SOKOLOV jewellery, large retail/e-commerce group); Jarad Cannon (CTO since May 2025, ex-CTO Brain Corp, ex-iRobot); Sotirios Stasinopoulos (CPO, ex-UBTECH); Jochen Rudat (CGRO, ex-Tesla); Boris Yangel (Head of AI, ex-Nebius); Thomas Shepherd (COO, ex-General Dynamics, Arrival); Devin Billings (Head of Core Platform, ex-Boston Dynamics); Hessam Maleki (Head of Locomanipulation, ex-Sanctuary AI) [S13][S14] |
| Employees (approx.) | ~250 (Jul 2026); growth: 175 (Sep 2025) → 200+ (May 2026) → 250+ (Jul 2026) [S2][S5][S12] |
| Ownership / listing | Private (VC-backed) |
| Total funding / valuation | $270M total: $118M pre-Series A (incl. ~$50M founder-led capital reported Sep 2025) + $152M Series A (Jul 2026) at $1.35B post-money — Europe's first pure-play humanoid-robotics unicorn. Series A led by Prime Movers Lab; participants: Schaeffler, Bosch, Fubon Financial Holding VC, Aglaé Ventures (Arnault family) [S4][S12][S2] |
| Semi-humanoid products | [HMND 01 (wheeled)](hmnd-01-wheeled/) — dossier subject |
| Other products | HMND 01 Alpha Bipedal (179 cm, 90 kg, 29 DoF; unveiled a few months after the wheeled Alpha; aimed at service/home longer-term) [S15] |
| Website | https://thehumanoid.ai/ |

## Company background

Humanoid was founded in London in 2024 by Artem Sokolov, a retail/e-commerce entrepreneur (SOKOLOV jewellery), and has moved unusually fast: the wheeled HMND 01 Alpha was built in seven months and unveiled in September 2025, with a bipedal Alpha following about five months of development later [S2][S11]. The engineering organisation (~250 people across London, Boston, Vancouver, San Diego) is stocked with alumni of Boston Dynamics, Sanctuary AI, Brain Corp, iRobot, UBTECH, Dyson, Arrival, 1X and Tesla; Forbes reports over 50 hires from Boston Dynamics, Sanctuary AI, Apptronik and 1X alone [S4][S13]. The AI layer, KinetIQ, is a four-layer hierarchical stack (fleet orchestrator → omni-modal LM reasoning → VLA execution at 5–10 Hz → 50 Hz RL whole-body control) that is cross-embodiment across the wheeled and bipedal platforms [S10]. In 2026 the company introduced KinetIQ Ascend, an end-to-end vision-based RL manipulation system claiming 99.9% manipulation reliability and up to 1.5x human-demonstration speed on bin picking, handovers and dual-arm container moves — billed as the first production deployment of end-to-end vision-based RL on humanoid manipulation [S16, vendor-claimed].

Strategy is explicitly commercial-industrial-first with a Robots-as-a-Service (RaaS) model [S2]. In roughly 10 months the company ran a dense series of European PoCs: Ford (Cologne Innovation Centre, Jan 2026 — 97% autonomous pick-and-place reliability, 83 picks/h vs. a 50 target) [S9]; SAP + Martur Fompak (automotive logistics, robot driven by SAP EWM via the Joule agent layer, Jan–Feb 2026) [S7]; Bosch Bühl (box transfer, Mar 2026) [S8]; Siemens Erlangen electronics factory with NVIDIA (60 tote moves/h, 8+ h uptime, 90%+ pick success, Apr 2026) [S6]. By July 2026 the company counted nine completed PoCs with a tenth underway [S4].

The industrialisation setup is notably German: Schaeffler signed a landmark RaaS deal (May 2026) for a four-digit number of wheeled robots across its global plants by 2032 plus a five-year actuator-supply agreement covering >50% of Humanoid's joint-actuator demand through 2031 (a seven-digit actuator volume); first deployments at Herzogenaurach and Schweinfurt from Dec 2026 [S5]. Bosch (Robert Bosch Robotics GmbH) will contract-manufacture HMND 01 for the European market under a DfX framework, with Forbes reporting planned capacity of ~100,000 units over five years [S8][S4]. Both Schaeffler and Bosch then invested in the Series A [S12]. CEO claims at CES 2026 included ~25,000 preorders and pilots with six Fortune 500 companies (vendor-claimed, not independently verified) [S11].

Go-to-market: RaaS subscriptions including fleet-management software, maintenance, 24/7 support and updates [S5]; enterprise integration via SAP and Siemens Xcelerator; an "Early Access" program on the website. Roadmap: Beta wheeled robot launching Q3–Q4 2026, commercial pilot deployments from Q4 2026, CE certification targeted 2027, then scale manufacturing via Bosch [S4][S12][S2].

## Relevance to the semi-humanoid market

For a German market entrant, Humanoid is arguably the most direct European threat: it is Europe's best-funded pure-play humanoid startup ($270M, $1.35B valuation), it deliberately leads with the wheeled semi-humanoid (not the biped) for industrial logistics, and it has already locked up two pillars of the German industrial supply chain — Schaeffler (actuators + anchor customer) and Bosch (contract manufacturing) — plus reference PoCs at Ford, Siemens, SAP and Bosch sites in Germany. Its trajectory is steeply up: from unveiling (Sep 2025) to nine PoCs, a 1,000+-unit anchor order and unicorn status within ten months. The main open questions are whether Alpha-stage reliability metrics survive scale deployment, and how much of the claimed preorder book converts; but its speed, capital and German industrial partnerships materially raise the bar for any new EU entrant.

## Sources

| # | URL | What it supports | Confidence |
|---|---|---|---|
| S2 | https://www.therobotreport.com/u-k-based-startup-humanoid-unveils-hmnd-01-alpha-mobile-manipulator/ | Founding, SKL Robotics legal name, $50M founder capital, RaaS, Alpha unveiling Sep 2025, Beta Q3 2026 | third-party |
| S3 | https://www.roboticstomorrow.com/news/2025/09/18/humanoid-unveils-the-uks-first-humanoid-robot-for-industrial-use/25559/ | 175 employees (2025), team pedigree, 2 PoCs in first year, bipedal timeline | third-party (vendor PR syndication) |
| S4 | https://www.forbes.com/sites/johnkoetsier/2026/07/21/humanoid-raises-152-million-at-135-billion-valuation-europes-newest-robot-unicorn/ | $152M Series A, $1.35B valuation, $270M total, $118M pre-Series A, investors, 9 PoCs, 1,000-robot Schaeffler order, 100k-unit Bosch capacity, CE 2027, 50+ hires from BD/Sanctuary/Apptronik/1X | third-party |
| S5 | https://thehumanoid.ai/humanoid-secures-landmark-deal-with-schaeffler-to-deploy-thousands-of-humanoid-robots/ | Schaeffler deal scope, actuator supply agreement, deployment sites/timeline, 200+ employees (May 2026) | vendor-claimed |
| S6 | https://thehumanoid.ai/siemens-and-humanoid-bring-physical-ai-to-the-factory-floor-deploying-humanoids-in-industrial-operations-with-nvidia/ | Siemens Erlangen deployment, metrics, NVIDIA Jetson Thor / Isaac | vendor-claimed |
| S7 | https://thehumanoid.ai/hmnd-01-alpha-goes-to-work-humanoid-completes-automotive-manufacturing-logistics-poc-with-sap-and-martur-fompak/ | SAP/Martur Fompak PoC details | vendor-claimed |
| S8 | https://thehumanoid.ai/humanoid-secures-partnership-with-bosch-following-a-successful-poc/ | Bosch contract manufacturing, Bühl PoC | vendor-claimed |
| S9 | https://www.euronews.com/next/2026/01/20/can-humanoid-ai-robots-really-handle-arduous-factory-work-a-new-ford-factory-trial-exceeds | Ford Cologne trial metrics | third-party |
| S10 | https://thehumanoid.ai/introducing-kinetiq/ | KinetIQ four-layer architecture | vendor-claimed |
| S11 | https://www.cnet.com/tech/computing/ive-seen-it-with-my-own-eyes-the-robots-are-here-and-walking-among-us/ | CES 2026 live demo, 25,000 preorders claim, six Fortune 500 pilots claim, bipedal built in 5 months | third-party (reporting vendor claims) |
| S12 | https://thehumanoid.ai/humanoid-raises-152-million-at-1-35-billion-post-money-valuation-becoming-europes-first-pure-play-humanoid-robotics-unicorn/ | Series A details, 250+ staff, offices, Beta Q4 2026 | vendor-claimed |
| S13 | https://thehumanoid.ai/te%d0%b0m/ | Leadership names, roles, prior companies | vendor-claimed |
| S14 | https://html.duckduckgo.com/html/?q=Jarad+Cannon+Humanoid+CTO+Boston+Dynamics | Cannon appointment May 2025, Brain Corp background | third-party |
| S15 | https://thehumanoid.ai/hmnd-01-alpha-bipedal/ | Bipedal variant specs (context) | vendor-claimed |
| S16 | thehumanoid.ai / press coverage of KinetIQ Ascend (2026) | KinetIQ Ascend RL system: 99.9% reliability, 1.5x speed claims | vendor-claimed |
