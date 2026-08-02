# PAL Robotics (PAL Robotics S.L.)

| Field | Value |
|---|---|
| HQ | Barcelona, Spain (C/ Pujades 77-79, 08005); additional offices in Toulouse (FR) and Bari (IT) [S1][S2] |
| Founded | 2004 [S1] |
| Founders / key people | Francesco Ferro (co-founder & CEO since founding era; President of euRobotics, Chair of IFR Service Robot Group, "CEO of the Year 2024 in Robotics" — European CEO) [S1][S3][S4] |
| Employees (approx.) | ~100 (vendor about page, 2025/26); one aggregator claims 150+ (unreliable) [S1][S5] |
| Ownership / listing | Private. Deliberately no-VC: Ferro — "Not going down the venture capital route allowed us to keep the freedom we need for innovation" [S3]. Origin financing linked to UAE backers (REEM program repeatedly showcased at UAE state events; see background) — ownership details not disclosed [S6][S7] |
| Total funding / valuation | n/a (not disclosed). One AI-generated aggregator claims "$50M+ Series B, ~$100M valuation" — contradicts CEO's no-VC statements; treat as unverified [S5][S3] |
| Semi-humanoid products | [TIAGo Pro](tiago-pro/), [TIAGo++ / TIAGo OMNI++](tiago-plus-plus/), [ARI](ari/) |
| Other products | Legged: REEM-C (2013 biped research), TALOS (2017 torque-controlled biped), Kangaroo (biped research); AMRs: TIAGo Base / TIAGo OMNI Base; retail: StockBot (RFID inventory); distributes SOLO 12 quadruped. Legacy: REEM line (see section below) [S8][S9] |
| Website | https://pal-robotics.com |

## Company background

PAL Robotics was founded in Barcelona in 2004 when "a small group of engineers built the first fully autonomous humanoid biped robot in Europe" (REEM-A, 2005) [S1][S8]. The founding program was financed from the United Arab Emirates: the REEM name was chosen as "an elegant female name from the Arabic world" [S6], and REEM robots served as showcase pieces at UAE events (UAE pavilion at Yeosu World Expo 2012 — billed as the "UAE-designed robot" —, Yas Island Abu Dhabi, RECON Dubai) [S7]. Confidence: vendor-claimed for the Barcelona founding story; third-party/estimated for the UAE financing link (widely reported, not verifiable from primary sources in this session). Over 20+ years the company evolved from walking-humanoid prototypes (REEM-A 2005, REEM-B 2008) through the wheeled service humanoid REEM (2010) into today's modular product families: TIAGo mobile manipulators (2015), TALOS biped (2017), ARI social humanoid (2019), TIAGo OMNI++ (2021), TIAGo Pro (2023) [S8][S9][S10].

Strategically, PAL is the archetypal EU research-platform vendor with a slowly growing commercial services leg. It is deeply embedded in the European funding machine: 40+ collaborative EU projects on the TIAGo platform alone [S11], membership in euROBIN (Network of Excellence, 31 partners, EUR 12.5M, coordinated by DLR, joined July 2022) [S12], SPRING (H2020, socially assistive robots in a Paris gerontology hospital) [S13], CANOPIES (agricultural HRI, from which the new SEA arm emerged) [S14], CO-HAND (TIAGo Pro reaching TRL 7 in textile manufacturing, 2026) [S15], plus ROSALYA, PRO-CARED, SHAPES, EnrichMe, OpenDR, DIH-HERO and others. CEO Ferro's institutional roles (euRobotics President, IFR service-robot chair, Adra board) give PAL outsized influence over the EU robotics agenda [S1][S4]. Go-to-market is direct, quote-based sale of customizable platforms (research pricing on request), with premium software packages, maintenance plans and accessories as add-ons; distribution partners (e.g., research distributors) exist but most sales appear direct. Manufacturing is in-house in Barcelona at limited-series scale; ~200 partners and operations in 30+ countries claimed [S1].

Commercially relevant deployments beyond academia: TIAGo Delivery / TIAGo Conveyor logistics variants ran at Hospital Municipal de Badalona and Hospital Clinic Barcelona during COVID-19 (DIH-HERO project, with Accerion, Sept 2020) [S16]; ARI works as receptionist at engineering firm Ayesa and starred at the Cruilla music festival 2022; StockBot does RFID inventory for fashion retail (Tendam) [S17][S2]. In 2017 Dubai Police introduced a "robocop" based on the REEM platform (widely reported; third-party, not re-verified from primary press in this session) [S18]. In October 2025 PAL announced a collaboration with NVIDIA (Isaac Sim / Isaac Lab for RL training, VR teleoperation, foundation-model integration) — its clearest move toward embodied-AI-era relevance [S19]. PAL maintains active ROS 2 support (TIAGo packages continuously released into ROS 2 Humble) [S20].

## Relevance to the semi-humanoid market

PAL matters because it effectively *owns* the European research market for wheeled semi-humanoids: TIAGo is the default dual-arm mobile-manipulation platform in EU labs (deployed in 14+ EU countries, 27 countries worldwide per vendor) [S11], and every European robotics PhD cohort trains on it. For a German market entrant this is a double-edged benchmark: PAL's install base, ROS/ROS 2 depth, and EU-project network raise the bar for credibility, yet its trajectory shows the limits of the research-platform business — quote-based, low-volume, project-funded, with no evidence of scaled commercial deployments of its manipulator humanoids. TIAGo Pro (2023) is PAL's attempt to bridge from research into industry-grade collaborative mobile manipulation (torque-controlled SEA arms, EtherCAT, ROS 2, expressive HRI head), and the NVIDIA/embodied-AI alignment signals scaling ambitions, but pricing and volumes remain undisclosed. Threat assessment: high in EU research/academic channels, moderate and slower-moving in industrial semi-humanoid applications — a window a well-capitalized industrial entrant could exploit. (Analyst view.)

## REEM (legacy wheeled semi-humanoid, discontinued)

REEM (2010) was PAL's wheeled service humanoid and an early ancestor of today's commercial semi-humanoid category: 1.70 m tall, 90 kg, 22 DoF, wheeled base at up to 4 km/h, ~8 h battery, torso touchscreen, two motorized arms (1 kg payload per arm, plus 30 kg cargo capacity on its back), Intel Core 2 Duo + Atom compute [S9]. It served as event guide/receptionist (CosmoCaixa museum, Barcelona malls, Yeosu Expo 2012 UAE pavilion) [S7]. In 2017 Dubai Police fielded a REEM-based "robot police officer" for tourist information and fine payment — the famous "Robocop" story [S18]. Lineage: REEM-A (2005, 1.4 m biped, 30 DoF), REEM-B (2008, 1.47 m biped, 41 DoF, could lift 12 kg), REEM (2010, wheeled), REEM-C (2013, 1.65 m biped research platform, 44 DoF, 80 kg, still marketed to labs) [S9]. The wheeled REEM is no longer in PAL's product line-up ("Hall of Fame" status on the vendor site) — status: discontinued [S12-page footer/S8].

## Sources

| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://pal-robotics.com/about-us/ | Founding 2004, first EU biped claim, ~100 employees, offices, partners, Ferro roles | vendor-claimed |
| 2 | https://pal-robotics.com/blog/ (recent posts listing) | Product/news timeline, StockBot Tendam, CO-HAND | vendor-claimed |
| 3 | https://pal-robotics.com/blog/uncertainty-evolutionary-tool-vision-francesco-ferro/ | No-VC/bootstrap strategy quote, CEO of the Year 2024, 20-year leadership | vendor-claimed |
| 4 | https://pal-robotics.com/blog/francesco-ferro-appointed-president-of-eurobotics/ | Ferro euRobotics presidency | vendor-claimed |
| 5 | https://www.airobotphysical.com/manufacturers/pal-robotics/ | Aggregator claims: 150+ employees, "$50M Series B", "$100M valuation", TALOS ~$500k | third-party (low reliability, AI-generated aggregator; contradicts S3) |
| 6 | https://pal-robotics.com/blog/reem-the-meaning-of-the-word/ | REEM name origin (Arabic), 2011 post | vendor-claimed |
| 7 | https://pal-robotics.com/blog/reem-at-in-park-magazine-uae-designed-robot-welcomes-visitors-to-countrys-pavilion-at-yeosu-expo-2012/ (also /reem-at-recon-dubai/, /robot-reem-is-at-yas-island-abu-dhabi/) | UAE showcase events, "UAE-designed robot" framing | vendor-claimed |
| 8 | https://www.automatedwarehouseonline.com/pal-robotics-launches-tiago-omni-mobile-manipulation-robot/ | Company history recap (2004 first autonomous biped in Europe), product portfolio, TIAGo OMNI++ launch Nov 2021 | third-party |
| 9 | https://en.wikipedia.org/wiki/REEM | REEM-A/B/REEM/REEM-C specs table, years | third-party |
| 10 | https://pal-robotics.com/blog/ari-social-robotics-artificial-intelligence-one-platform/ | ARI introduction Dec 2019 | vendor-claimed |
| 11 | https://pal-robotics.com/robot/tiago/ | 9+ years on market, 40 collaborative projects, 14 EU countries, 27 countries worldwide | vendor-claimed |
| 12 | https://pal-robotics.com/blog/pal-robotics-joins-eurobin-project-with-leading-european-research-labs-on-ai-driven-robotics/ | euROBIN: 31 partners, 14 countries, EUR 12.5M, DLR-coordinated, July 2022 | vendor-claimed |
| 13 | https://pal-robotics.com/blog/assistive-robots-in-healthcare-spring-project/ | SPRING: 7 ARIs, Broca hospital (AP-HP Paris), 100+ patients, ROS4HRI, completed Oct 2024 | vendor-claimed |
| 14 | https://pal-robotics.com/blog/introducing-new-tiago-sea-arm/ | SEA arm from CANOPIES project, Sept 2023 | vendor-claimed |
| 15 | https://pal-robotics.com/blog/pal-robotics-in-co-hand-project/ | CO-HAND TRL 7, TIAGo Pro textile validation (2026) | vendor-claimed |
| 16 | https://pal-robotics.com/blog/tiago-delivery-impact-hospitals-covid19/ | Hospital Municipal de Badalona + Hospital Clinic Barcelona deployments (TIAGo Delivery/Conveyor, DIH-HERO, Accerion, Sept 2020) | vendor-claimed |
| 17 | https://pal-robotics.com/blog/ari-as-humanoid-receptionist-at-ayesa/ | ARI receptionist at Ayesa | vendor-claimed |
| 18 | https://www.telegraph.co.uk/technology/2017/03/20/real-life-robocops-will-soon-replace-human-police/ | Dubai Police robot officer program 2017 (REEM-based "robocop" widely reported) | third-party (not re-verified this session; paywalled) |
| 19 | https://pal-robotics.com/blog/pal-robotics-and-nvidia-shaping-the-next-generation-of-robotics/ | NVIDIA collaboration (Isaac Sim/Lab, VR teleop), Oct 16, 2025 | vendor-claimed |
| 20 | https://discourse.ros.org/search.json?q=tiago | Ongoing TIAGo package releases into ROS 2 Humble (2025-2026) | third-party |
