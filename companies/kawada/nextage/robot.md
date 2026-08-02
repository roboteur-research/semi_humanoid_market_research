# NEXTAGE / NEXTAGE Fillie (ネクステージ / フィリー) — Kawada Robotics

> NEXTAGE is the original industrial semi-humanoid: a pedestal-mounted dual-arm robot with a camera head, sold since 2009 for cell production (many-variety, small-lot assembly) as a drop-in replacement for a human workstation. The 2022 **NEXTAGE Fillie** refresh (from ¥6M) made it smaller, faster and customer-facing; **Fillie OPEN** is the research SKU; the discontinued **HIRO** was its university-lab twin. With 100+ corporate users over 15 years it is the longest-lived commercial proof of the humanoid-form factory robot — the incumbent every new dual-arm entrant is measured against in Japan.

| Field | Value |
|---|---|
| Company | Kawada Robotics (Kawada Industries group) |
| HQ | Tokyo, Japan |
| Status (2026) | shipping |
| First shown / launch | NEXTAGE: 2009; NEXTAGE OPEN/HIRO research: ~2010-13 (HIRO discontinued); NEXTAGE Fillie: orders from March 2022 (iREX 2022 debut); Fillie OPEN: current research model |
| Target applications | Cell production: assembly, kitting, inspection, dispensing, machine tending (electronics, auto parts, cosmetics, food); Fillie adds reception/customer-facing roles |
| Price | Fillie from **¥6,000,000** (pedestal, hand cameras etc. optional extra) [S2]; original NEXTAGE historically ~¥7.4M class (estimated) |
| Availability | Japan direct + THK Intex; Europe via Rollomatic SA (CH); purchase (no RaaS) |

## Design & morphology
Fixed pedestal (no mobility) carrying a human-scale torso: two 6-axis arms, 2-axis neck with camera head, 1-axis waist rotation — **15 axes total** [S1, vendor-claimed]. Human-workstation footprint lets it slot into existing cell lines without layout change. Fillie: lighter, more compact re-design with softer styling ("cool, cute, reliable" per launch release), reach 576mm per arm [S2][S3].

## Locomotion
None — pedestal mount; repositioned by pallet/cart between cells (the original "manual reposition" pattern later copied by Epson WorkSense). This is a deliberate scope limit: Kawada sells arms+eyes, not navigation.

## Upper body & manipulation
- Original NEXTAGE: 2×6-axis arms, **1.5kg payload per arm** [S1]; later NXA variant rated ~2.5kg (max 3.0kg) per arm [S4, third-party listing]; repeatability ±0.03mm (Rollomatic NXA figure) [S5].
- Fillie: **2kg per hand**, reach 576mm, faster and lighter than the original [S2][S3].
- End-effectors: application-specific grippers/screwdrivers; dual-arm coordination for bimanual assembly; hand cameras optional at the wrist for visual servoing [S1][S2]. No public tool-changer/media-at-flange standard — n/a (not disclosed).

## Sensing
Head: stereo camera pair (2 cameras) for workspace overview and part localization; optional 2 hand cameras → 4-camera configuration (NXA) [S5]. Integrated image recognition is the core teach-and-see workflow: parts located visually rather than by fixtures — a 2009-era precursor of today's vision-first manipulation [S1]. No lidar/depth (fixed workspace). Force sensing: n/a (not disclosed; original design used low-power position control).

## Actuation & power
Low-power electric servos sized for human-safe coexistence (arms deliberately weaker than industrial norms); mains-powered (no battery). Details n/a (not disclosed).

## Compute & software
Controller in pedestal; programming via Kawada's task-oriented GUI — positioned as "no programming expertise required," multi-task repertoire per robot [S1]. Research lineage: NEXTAGE OPEN / HIRO ran ROS with open APIs (community support by TORK), making it one of the first industrially-derived ROS humanoids; **Fillie OPEN** continues this as the research platform [S1][S3]. No VLA/foundation-model story announced as of 2026 — the stack is classic vision + motion planning.

## Safety & compliance
Fence-free human coexistence by design (low-power actuation, speed limitation, visual monitoring) — NEXTAGE predates and helped shape Japanese practice for collaborative dual-arm cells; formal cert status n/a (not disclosed; risk-assessment-based deployments under ISO 10218/TS 15066 regime, estimated).

## Deployment evidence & traction
- **100+ companies** deployed since 2009 [S4, third-party] — the largest verified industrial semi-humanoid install base outside Pepper's service niche.
- Sectors: electronics/electrical, automotive, cosmetics, food; named user: Makino Technical Service; famous early case: GLORY Saitama coin-machine assembly lines running multi-robot NEXTAGE cells (from ~2011, estimated/widely reported).
- Distribution: THK Intex (JP), **Rollomatic SA (Switzerland)** selling NEXTAGE NXA into European precision manufacturing [S5] — a quiet, rare example of a Japanese semi-humanoid sold in Europe.
- Fillie shown doing reception at iREX 2022; Fillie OPEN adopted as current research SKU [S2][S3].
- 15-year service/maintenance track record is itself the moat: training, consultation, maintenance from Kawada [S3].

## Assessment (analyst view)
*Analyst opinion.* Strengths: unmatched longevity and reference density in humanoid-form industrial automation; a price (¥6M ≈ €37k) that undercuts most new AI dual-arm platforms; European channel already in place; HRP-grade mechanical pedigree. Weaknesses: no mobility, modest payloads, ageing controller/software stack with no announced learning-based autonomy — exactly where Yaskawa's MOTOMAN NEXT-NHC10DE and Chinese AI-native dual-arms attack; brand nearly invisible outside Japan/watchmaking. Threat to a new EU entrant: moderate — in pedestal cell-production it is the entrenched, cheaper incumbent an EU dual-arm robot must displace with better AI and force control; it poses no threat in mobile or service segments.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://nextage.kawada.jp/en/specification/ + https://nextage.kawadarobot.co.jp/ | 15 axes (2×6 arms, 2 neck, 1 waist), 1.5kg/arm, vision-integrated workflow, industries, distributors | vendor-claimed |
| 2 | https://www.kawadarobot.co.jp/news/1150/ | Fillie launch 03/2022, from ¥6M (options extra), concepts, reception market, iREX 2022 | vendor-claimed |
| 3 | https://nextage.kawadarobot.co.jp/ (Fillie/Fillie OPEN pages) | Fillie 2kg/hand, 576mm reach, 6-axis arms, lighter/faster; Fillie OPEN research SKU | vendor-claimed |
| 4 | https://botmarket24.com/en/robot-database/kawada-nextage/ + https://mono.ipros.com/en/product/detail/2000337479/ | 100+ companies; NXA-era 2.5kg rated / 3.0kg max per arm | third-party |
| 5 | https://www.rollomatic.ch/product/nextagenxa/ | NXA in Europe, 15 axis, 4 cameras, ±30µm repeatability | vendor-claimed (distributor) |
