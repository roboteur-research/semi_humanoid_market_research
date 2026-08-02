# Model-T (モデルT) — Telexistence

> Model-T was Telexistence's 22-DoF wheeled dual-arm teleoperated semi-humanoid that stocked shelves in real FamilyMart and Lawson convenience stores in Tokyo from summer 2020, driven by VR pilots over a 50ms-latency video link. It was among the world's first humanoid-form robots doing real retail work — and its subsequent retirement in favor of the cheaper single-arm TX SCARA (deployed to 300+ stores) is one of the market's most instructive datapoints on when the humanoid form factor does and does not pay.

| Field | Value |
|---|---|
| Company | Telexistence Inc. |
| HQ | Tokyo, Japan |
| Status (2026) | discontinued (superseded by single-arm TX SCARA/GHOST) |
| First shown / launch | Unveiled July 2020 (Model H predecessor 2017); FamilyMart trial from summer 2020; Lawson Takeshiba store 2020-09-14 |
| Target applications | Convenience-store shelf stocking (bento, drinks, onigiri, snacks) via remote human pilots; "Augmented Workforce Platform" remote labor |
| Price | n/a (not sold; operated by TX under service model) |
| Availability | Pilot-only, Japan, 2020-2021; never generally available |

## Design & morphology
Human-proportioned upper body (torso + two arms + sensor head) on a wheeled base with a vertical axis; 22 DoF in body and arms, expressly dimensioned to restock shelves in the narrow aisles/backrooms of convenience stores without store modification [S1][S2]. Press described it as roughly human height on its base (~2m class with mast; "7 feet" in some coverage — third-party, imprecise) [S4].

## Locomotion
Wheeled base for repositioning along shelf fronts; robot works from the backroom side of walk-in drink shelves or aisle side. Speed/nav details n/a (pilot-controlled) [S1].

## Upper body & manipulation
Two arms; signature end-effector is the "Andrea-Yamaura End Effector" — a hybrid vacuum-suction + two-finger gripper in a single hand, so the pilot never swaps tools across product shapes (bottles, bento boxes, cans, pouches) [S2]. Payload n/a (convenience-goods scale, <1-2kg estimated).

## Sensing
Head-mounted stereo cameras streaming to the operator's VR HMD; end-to-end video latency of 50ms (camera → operator display) using H.265/HEVC encoding — the industry-leading claim at launch [S1][S2]. Additional sensor detail n/a.

## Actuation & power
n/a (not disclosed). Tethered/battery details not published.

## Compute & software
Teleoperation-first: pilot logs in via VR headset + controllers from TX's Toranomon office (later, the concept scaled to remote workers anywhere) through TX's Augmented Workforce Platform (AWP) cloud; semi-autonomous assistance blended in ("semi-autonomous remote-operated robot") [S1][S2]. The AI-autonomy emphasis (GORDON system) matured later on TX SCARA rather than Model-T [S5].

## Safety & compliance
Operated in customer-free zones (behind drink shelves) and pilot-supervised; no formal certification published (n/a).

## Deployment evidence & traction
- FamilyMart Toshima Ecomusée Town store, Tokyo — trial shelf stocking from summer 2020, pilot in Toranomon [S3] (vendor-claimed, widely covered third-party).
- Lawson Tokyo Port City Takeshiba store — Model-T stocking duty at store opening 2020-09-14 [S1][S4] (third-party confirmed).
- Extensive global press (New Atlas, Japan Times etc.) [S4].
- Superseded: TX pivoted to single-arm TX SCARA, deployed to 300 FamilyMart stores from 2022; GHOST next-gen arm manufactured by Foxconn (2023 partnership) [S5].

## Assessment (analyst view)
*Analyst opinion.* Model-T proved the teleop-retail concept — 50ms latency, one hybrid hand for all SKUs, real stores — and then disproved the business case for the humanoid form in that vertical: TX's own data pushed it to a fixed single-arm machine at 1/Nth the cost for the one task (beverage restock) that carried the ROI. Strengths of record: fastest path from humanoid demo to real-store work in 2020; AWP remote-labor model. For an EU semi-humanoid entrant the lesson is double-edged: Model-T validates teleop-first go-to-market, but TX's pivot is the argument competitors will cite against general-purpose dual-arm platforms in structured retail tasks. TX itself no longer competes in the semi-humanoid category.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://tx-inc.com/en/blog/2020/07/21/10624/ | Model-T launch, 22 DoF, 50ms, Lawson/FamilyMart, AWP | vendor-claimed |
| 2 | https://prtimes.jp/main/html/rd/p/000000015.000027631.html | 22 DoF torso/arms, H.265, Andrea-Yamaura end effector, pilots | vendor-claimed |
| 3 | https://tx-inc.com/en/blog/telexistence-begins-the-trial-operation-of-its-remote-controlled-robot-model-t-at-a-familymart-store-aims-to-realize-a-new-labor-saving-store-operation-platform/ | FamilyMart trial details | vendor-claimed |
| 4 | https://newatlas.com/robotics/telexistence-model-t-robot-shelf-stacker/ | independent coverage, deployment | third-party |
| 5 | https://tx-inc.com/en/blog/2023/07/06/12082/ | supersession by TX SCARA/GHOST, 300 stores, Foxconn | vendor-claimed |
