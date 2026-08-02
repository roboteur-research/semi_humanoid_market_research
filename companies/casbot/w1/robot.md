# CASBOT 02 (灵贰) — CASBOT / Zhongke Huiling
*(incl. the wheeled siblings CASBOT W1/W2 — see correction note)*

> CASBOT 02 ("灵贰", Ling'er) is CASBOT's full-size commercial-interaction humanoid: ~163 cm, ~55 kg, 275 TOPS onboard, sold openly on JD.com from June 2025 at ¥328,800 with first orders inside 48 hours. **Correction vs. discovery notes: CASBOT 02 is a BIPED, not a wheeled robot** — the discovery sweep inverted the lineup (it "excluded CASBOT 01 as the biped"). The company's actual semi-humanoid/wheeled machines are CASBOT W1 (WAIC 2025) and W2 (2026), covered below, which put humanoid dual 7-DoF arms on a multi-stage lifting chassis for industrial work. Competitively, CASBOT matters for its CAS pedigree, Lenovo production-line deployments, low-cost "skeleton/shell decoupled" modular construction, and mainstream e-commerce distribution.

| Field | Value |
|---|---|
| Company | CASBOT / Beijing Zhongke Huiling (灵宝CASBOT) |
| HQ | Beijing, China |
| Status (2026) | shipping (JD.com retail listing with confirmed orders; W1 in industrial pilots) [S1][S2] |
| First shown / launch | CASBOT 02: JD listing mid-June 2025 (discovery notes 2025-06-16), public debut WAIC 2025 (26 Jul 2025); W1: WAIC 2025; W2: 2026 [S1][S2][S3] |
| Target applications | 02: mall "digital shopping guide", exhibition halls, culture/entertainment performance, commercial service, (later) home; W1/W2: smart retail, sorting/logistics, warehouse packaging & QC, factory material handling [S2] |
| Price | CASBOT 02: from ¥328,800 (~USD 45k) on JD.com; CASBOT 02 Lite dev platform: ¥99,000 promo (2026); W1/W2: n/a (not disclosed) [S1][S4] |
| Availability | China; JD.com self-operated CASBOT flagship store + direct sales [S1] |

## Design & morphology
**CASBOT 02 (biped):** ~163 cm, ~55 kg, friendly consumer-styled shell; 33 DoF bionic joint layout (GeekPark WAIC report; one syndicated report says 36 DoF — discrepancy unresolved) [S2][S5]. Modular "skeleton/shell decoupled" (骨架/外壳解耦) construction reduces assembly time and production cost — the design signature of the whole family [S1]. Fast battery-swap.
**CASBOT W1/W2 (wheeled semi-humanoid):** dual humanoid 7-DoF arms on a multi-stage lifting chassis (多级升降底盘) that varies working height for shelf-to-floor tasks; sub-millimeter manipulation precision claimed; validated at -20 °C for cold environments [S2].

## Locomotion
02: bipedal walking (interactive walking demos; gait specs n/a). W1/W2: wheeled chassis with multi-stage vertical lift; drive type, speed n/a (not disclosed) [S2].

## Upper body & manipulation
02: dual arms with multi-functional bionic dexterous hands; company demonstrates dual-finger twisting and inter-finger grasping, dual-arm dual-hand hybrid force/position control with sub-millimeter precision (skills proven on Lenovo notebook assembly line, family-level claim) [S6]. W1: 7 DoF per arm, sub-mm precision pick/place, sorting, packaging [S2]. Payload figures: n/a (not disclosed).

## Sensing
02: multimodal perception — face recognition and voiceprint identification for "exclusive following", cameras in head and chest (visible in WAIC photos: stereo/depth modules in visor and torso), microphone array for natural-language interaction [S2]. Force sensing implied by force/position hybrid control; details n/a.

## Actuation & power
Self-developed bionic joints (details n/a). 02: fast battery-swap modules; CASBOT 01 claimed >4 h runtime (sibling datum) [S7]. Battery capacity: n/a (not disclosed).

## Compute & software
02: 275 TOPS onboard AI compute [S2][S5]. Software: hierarchical end-to-end model architecture ("CASBOT Embodied Brain", v2.0 on W1) with VLA-style natural-language task execution via AI agent; training pipeline mixes real-to-sim, synthetic data, hybrid training, sim-to-real [S2][S6]. Smart OTA upgrades. SDK: CASBOT 02 Lite (¥99,000) is explicitly sold as a secondary-development platform [S4].

## Safety & compliance
n/a (not disclosed). No published ISO 13482/10218 or CE certification claims found.

## Deployment evidence & traction
- JD.com listing June 2025 at ¥328,800; first paid orders within 48 h, >3,000 product-page views in days (third-party press) [S1].
- Family-level: robots performing dual-arm assembly tasks on a Lenovo notebook production line (vendor-claimed, reported third-party) [S6].
- CASBOT Mini 50-unit batch sold out (2026, third-party database/press) [S4].
- WAIC 2025 booth demos of 02 (interaction) and W1 (sorting/handling) [S2][S3].

## Assessment (analyst view)
*Analyst opinion.* Strengths: credible CAS precision-assembly heritage, Lenovo strategic backing plus a real electronics-line use case, cost-focused modular construction, and rare retail distribution that builds brand and pricing transparency. Weaknesses: specs are thin and partly inconsistent (33 vs 36 DoF), no certifications published, funding (~RMB 100m+) is small against Tier-1 Chinese rivals, and the strategically relevant wheeled line (W1/W2) is younger and largely spec-silent. Threat to a new EU entrant: moderate — low direct threat in Europe near-term, but CASBOT's ¥328k full-size humanoid and ¥99k dev platform illustrate the price anchor Chinese vendors will set; the W-series could become a cheap competitor in light industrial handling if it matures.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://news.qq.com/rain/a/20250627A02C7J00 (also m.yicai.com/news/102693097.html) | JD ¥328,800 listing, 48h first orders, skeleton/shell decoupled design, VLA | third-party |
| 2 | https://www.geekpark.net/news/352008 | WAIC 2025: 02 specs (163cm, 55kg, 33 DoF, 275 TOPS, battery swap, face/voiceprint), W1 specs (7-DoF arms, lifting chassis, sub-mm, -20°C, Embodied Brain 2.0), applications | third-party |
| 3 | https://finance.sina.com.cn/jjxw/2025-06-27/doc-infcnmtt2807963.shtml | JD sales performance, e-commerce context | third-party |
| 4 | https://www.robothub.app/zh/companies/casbot | Family lineup incl. W2 (2026), 02 Lite ¥99,000, Mini sold out | third-party (database) |
| 5 | https://www.xhby.net/content/s685a50a1e4b0589b06da5119.shtml | 02 as ~¥300k-class product, 36 DoF figure (discrepant), 618 campaign | third-party |
| 6 | https://www.qbitai.com/2024/10/213641.html | Lenovo line deployment, dexterous-hand skills, training approach, C919/CAS lineage | third-party (vendor-sourced) |
| 7 | https://www.qbitai.com/2024/11/218675.html | CASBOT 01 sibling: >4h runtime, Nov 2024 launch | third-party |

*Unknown fields: n/a (not disclosed). DoF discrepancy (33 vs 36) flagged above.*
