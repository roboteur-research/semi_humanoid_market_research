# AlphaBot 2 (爱宝 / "Aibao") — AI² Robotics (智平方)

> AlphaBot 2 is a wheeled, dual-arm general-purpose robot with a retractable waist-leg torso giving a 0–240 cm vertical working range, launched 17 April 2025 in Shenzhen. It is the flagship "AGI terminal" carrying AI² Robotics' GOVLA (Global & Omni-body VLA) foundation model, and one of the few Chinese semi-humanoids with paying deployments in regulated environments — automotive plants, a Geely-affiliated semiconductor fab, and Bloomage Biotech sterile cleanrooms. With 100+ units/month shipping since December 2025 off its own production line, it is a leading indicator of how fast Chinese wheeled humanoids can industrialize.

| Field | Value |
|---|---|
| Company | AI² Robotics (智平方科技) |
| HQ | Shenzhen, China |
| Status (2026) | shipping |
| First shown / launch | 2025-04-17 (Shenzhen launch event); AlphaBot 1 predecessor shown WRC 2024 |
| Target applications | Semiconductor fab intralogistics, biopharma cleanrooms, automotive manufacturing, airports/public service, community/retail (coffee/ice-cream service) |
| Price | n/a (not disclosed) |
| Availability | China; direct B2B contracts; own production line (Sep 2025-), 1,000s/yr capacity, 100+ units/month as of 12/2025 [S4][S6] |

## Design & morphology
Wheeled mobile base + torso with retractable "waist-leg" (腰腿) lifting structure; the working envelope spans 0–240 cm vertically — it can pick from floor level and reach high shelves (vendor-claimed) [S2][S3]. Full-body 34+ DoF [S2][S3]. Dual arms with 5-finger dexterous hands (seen in official imagery handling PCB/glass sheets) [S5]. Height/weight not disclosed. Core components claimed at >50,000 h MTBF [S7].

## Locomotion
Wheeled base (configuration not detailed; imagery suggests a compact omnidirectional platform). Speed n/a (not disclosed). Designed for cleanroom-compatible indoor operation (deployed in Class-controlled sterile and semiconductor environments) [S2][S8].

## Upper body & manipulation
- Arms: dual; single-arm span 700 mm excluding end-effector (vendor-claimed) [S3].
- Payload: up to 10 kg single-arm max (third-party aggregated figure) [S3].
- End-effectors: multi-finger dexterous hands in current imagery; earlier AlphaBot units at Geely Jingneng show two-finger/parallel tooling — EEs appear swappable per scenario (estimated from imagery) [S5][S8].
- Repeatability: n/a (not disclosed).

## Sensing
"360° × 360° full-space perception" multi-modal sensor suite (vendor phrase): head cameras plus torso/base sensors; details (lidar type, depth cameras) not itemized [S2][S3]. Wrist-mounted cameras visible on both forearms in official imagery (estimated) [S5].

## Actuation & power
Actuator types not disclosed. Runtime 6+ h continuous operation (vendor-claimed) [S3]. Battery capacity, hot-swap, dock: n/a (not disclosed).

## Compute & software
- AlphaBrain / GOVLA (Global & Omni-body Vision-Language-Action): dual-system architecture — System 2 (slow): spatial-interaction foundation model + reasoning (DeepSeek integration) for long-horizon task decomposition; System 1 (fast): real-time control outputting arm motion, torso motion, and base trajectory (i.e., whole-body, not arm-only, action space) [S2][S5].
- On-device ("end-side") inference emphasized for data privacy in customer plants [S3].
- Zero-shot / few-shot task generalization claimed ("completes many tasks without training, quickly masters new ones") [S2].
- FiS-VLA open-source release (06/2025) claims +30% vs π0 benchmark [S1].
- SDK/ROS support: n/a (not disclosed); developer docs at docs.ai2robotics.com.

## Safety & compliance
No ISO/CE certifications publicly cited. Cleanroom/sterile-environment compatibility implied by Bloomage and semiconductor deployments (sterile transport, reduced cross-contamination claims) but no stated cleanliness class certification [S8]. Confidence: vendor-claimed.

## Deployment evidence & traction
- Geely Jingneng Microelectronics (晶能微电子): strategic agreement 2025-03-18 (Hangzhou); AlphaBot performs loading/unloading and inter-line material transport in a running semiconductor fab; plan for scale deployment [S8] (third-party + vendor).
- Bloomage Biotech (华熙生物): sterile transport, visual inspection, culture monitoring in biomanufacturing cleanrooms; announced at 04/2025 launch [S2] (vendor-claimed).
- Automotive: contracts with "leading automakers"; names not confirmed (vendor-claimed) [S2].
- Public service: airport deployment planned Q3 2025; residential community services Q4 2025 [S2].
- Volume: >100 units delivered in December 2025 alone; own line (Sep 2025) with thousands-unit annual capacity; 100+ cups/day coffee & ice-cream service operations across multiple cities [S4][S6] (third-party).
- Targets: 10,000 units by 2028; 1M by 2033 (vendor-claimed, aspirational) [S2].

## Assessment (analyst view)
*Analyst opinion.* Strengths: rare combination of a genuinely whole-body VLA stack (base + torso + arms in the action space), a 0–240 cm reach envelope that beats most fixed-torso rivals, own manufacturing, and deployments in cleanroom/semiconductor niches with high switching costs and thin Western competition. Funding depth (Baidu, CRRC, >RMB 10B valuation) means it can sustain a price war. Weaknesses: hardware specs are unusually opaque (no height/weight/speed/price), suggesting per-account customization and immature productization; deployment claims are mostly vendor-narrated with limited independent verification of unit economics. Threat to a new EU entrant: high in Chinese-supplied verticals (electronics, biopharma logistics) and medium in Europe near-term — no EU channel or CE track record yet, but its cleanroom references would resonate with EU pharma customers if it lands a distributor.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://ai2robotics.com/en/about/ | Company/model background, FiS-VLA | vendor-claimed |
| 2 | https://www.sznews.com/news/content/mb/2025-04/18/content_31541723.htm | Launch date, GOVLA, deployments, targets | third-party |
| 3 | DuckDuckGo aggregate (spec snippets: 34+ DoF, 700mm, 0-240cm, 6h, 10kg, 360°×360°) | Core hardware specs | vendor-claimed (via aggregators) |
| 4 | https://www.jiemian.com/article/14027312.html | 100+ units/month 12/2025, line online 09/2025 | third-party |
| 5 | https://ai2robotics.com/智平方发布全新一代智能机器人alphabot-2开启agi终端新/ | GOVLA dual-system detail; official imagery | vendor-claimed |
| 6 | https://www.sohu.com/a/989230728_114988 | Series B, delivery metrics, coffee ops | third-party |
| 7 | https://www.sohu.com/a/989389484_430392 | 50,000h MTBF, wheeled dual-arm description | third-party |
| 8 | https://ai2robotics.com/智平方携手吉利科技旗下企业晶能微真实场景驱/ | Geely Jingneng fab deployment, signing photo | vendor-claimed |

*Specs carry confidence tags inline; unknown = n/a (not disclosed).*
