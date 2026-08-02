# CLOiD — LG Electronics

> CLOiD is LG's AI home robot debuted at CES 2026: a wheeled semi-humanoid with two 7-DoF arms and five-fingered hands that cooks simple meals, loads/starts laundry, folds clothes, and acts as a mobile ThinQ smart-home hub. It is the flagship of LG's "Zero Labor Home" strategy and the clearest signal yet that a top-3 global appliance maker intends to own the consumer home-manipulation category.

| Field | Value |
|---|---|
| Company | LG Electronics |
| HQ | Seoul, South Korea |
| Status (2026) | announced (pilot production of test units since July 2026) |
| First shown / launch | CES 2026 (Jan 6-9, Las Vegas; previewed at LG World Premiere) |
| Target applications | household chores (kitchen, laundry), ambient care, smart-home orchestration |
| Price | n/a (not disclosed); industry estimates USD 15-25k [S6, estimated] |
| Availability | not for sale; in-home pilots expected late 2026, consumer ~2028 (estimated, not LG-confirmed) |

## Design & morphology
Compact wheeled home robot, roughly counter-top height (appears ~1.0-1.2 m in demo footage, estimated — no official dimensions). Rounded white consumer styling: head unit (AI hub with animated-face display, speaker, cameras, sensors), tiltable articulated torso that adjusts working height from knee-level upward, two articulated arms, five-fingered hands, wheeled base with low center of gravity [S1][S2]. Total DoF n/a (not disclosed); 7 DoF per arm plus 5 independently actuated fingers per hand [S1].

## Locomotion
Autonomous wheeled base; drive type, speed and terrain limits n/a (not disclosed). Low-CG design for stability in homes [S1].

## Upper body & manipulation
Two 7-DoF arms (shoulder, elbow, wrist with forward/backward/rotational/lateral motion) [S1]. Hands: five independently actuated fingers each, for fine manipulation — demonstrated retrieving milk from a refrigerator, placing a croissant in an oven, starting laundry cycles, folding and stacking garments [S1][S2]. Payload, reach, repeatability n/a (not disclosed). Torso tilt substitutes for a lift column to span knee-height to above-counter workspace [S1].

## Sensing
Head unit: multiple cameras, unspecified sensors, mics/speaker for voice interaction [S1]. No lidar disclosed. Hand/wrist sensing n/a (not disclosed).

## Actuation & power
LG unveiled the AXIUM actuator alongside CLOiD — integrated motor + drive + reducer, lightweight, high-efficiency, modular for multi-variety robot production; presumed used in CLOiD (LG shows them together, not explicitly confirmed per-joint) [S1]. Battery capacity/runtime/charging n/a (not disclosed).

## Compute & software
"Vision-based Physical AI": a Vision Language Model (scene understanding to language) plus a Vision-Language-Action model (visual/verbal input to physical action), trained on tens of thousands of hours of household task data (vendor-claimed) [S1]. Voice-based generative AI agent; deep ThinQ / ThinQ ON hub integration — CLOiD orchestrates other LG appliances and serves as mobile AI home hub; remote interaction via app [S1][S2]. No SDK/open API announced (consumer product).

## Safety & compliance
Nothing published (no ISO 13482/CE claims yet — pre-commercial). Independent researchers have flagged that home-robot LLM/VLA stacks broadly still fail safety-compliance tests, a gating risk for the category [S2, third-party commentary].

## Deployment evidence & traction
No customers or pilots yet. Milestones: CES 2026 live demos (breakfast prep, laundry folding) [S1][S2]; pilot production of test units started July 2026 [S5]; LG robotics reorganized into a CEO-adjacent Business Center [S5]. Timeline of late-2026 in-home pilots and ~2028 consumer launch at ~$15-25k is analyst/press expectation, not LG guidance [S6, estimated]. Strategic context: LG hedges via stakes in AgiBot (Aug 2025) and Dexmate (Mar 2026, LG Technology Ventures/LG CNS) [S3][S4].

## Assessment (analyst view)
*Analyst opinion.* Strengths: appliance ecosystem integration nobody else can match (robot + washer + oven as one orchestrated system), enormous brand/distribution/manufacturing muscle, credible VLA data program, and in-house actuators (AXIUM). Weaknesses: unproven manipulation reliability in real homes, no pricing, 2+ years from consumers, and LG's own multi-vendor hedging suggests internal uncertainty about its hardware. Threat to a new EU industrial entrant is low directly (consumer focus) but high indirectly: LG legitimizes the wheeled semi-humanoid form factor at CES scale and funds AgiBot/Dexmate hardware that does compete in industrial/service settings. Watch whether CLOiD pilots slip — home manipulation is the hardest reliability environment in robotics.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.lg.com/global/newsroom/news/home-appliance-solution/lg-electronics-presents-lg-cloid-home-robot-to-demonstrate-zero-labor-home-at-ces-2026/ | full spec/feature set, AXIUM, Zero Labor Home | vendor-claimed |
| 2 | https://newatlas.com/robotics/lg-cloid-domestic-humanoid-robot/ | design details, demos, safety commentary | third-party |
| 3 | https://www.yicaiglobal.com/news/south-koreas-lg-electronics-mirae-asset-co-invest-in-chinese-humanoid-robot-startup-agibot | AgiBot stake | third-party |
| 4 | https://www.thelec.net/news/articleView.html?idxno=5769 | Dexmate stake, RX strategy | third-party |
| 5 | https://www.usine-digitale.fr/intelligence-artificielle/robotique/robots-humanoides-lg-lance-la-production-pilote-du-prototype-de-cloid-concu-pour-les-taches-menageres.FBVHWFW5MRAFZC6YUTJZYZNECQ.html | July 2026 pilot production, Business Center | third-party |
| 6 | Discovery lead (_work/discovery_startups.md #18) + CES press consensus | $15-25k est., late-2026 pilots, ~2028 consumer | estimated |
