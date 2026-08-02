# Honda Avatar Robot (Hondaアバターロボット) — Honda

> The Honda Avatar Robot is a teleoperated wheeled dual-arm robot built on ASIMO's technology inheritance, announced September 2021 with practical use targeted for the 2030s. Its differentiator is the multi-finger hand — 4 fingers, 16 joints, wire-driven by 11 forearm motors — capable of opening a pull-tab drink can, and an AI "shared autonomy" scheme that blends remote human judgment with autonomous fine-motion correction. It is a research program, not a product, but it represents the most credible dexterous-hand teleop stack held by any automaker.

| Field | Value |
|---|---|
| Company | Honda Motor / Honda R&D |
| HQ | Tokyo / Wako (Saitama), Japan |
| Status (2026) | research (prototype demos since FY2023; practical use target 2030s) |
| First shown / launch | Announced 2021-09-30; press demos 2022; technology verification from FY2023 |
| Target applications | Remote work ("second self"), hazardous environments, emergency medicine support, space/lunar teleoperation |
| Price | n/a (not a product) |
| Availability | Not available; open-innovation partnerships sought |

## Design & morphology
Wheeled mobile base carrying a dual-arm humanoid upper body (no legs — Honda deliberately parked ASIMO's bipedalism to focus on manipulation value) [S1][S2]. Dimensions, weight, DoF totals n/a (not disclosed).

## Locomotion
Wheeled base; details (drive type, speed) n/a (not disclosed) [S2].

## Upper body & manipulation
The program's core: ASIMO-derived multi-finger hand with 4 fingers and 16 joints, actuated by 11 motors housed in the forearm driving wires/tendons [S3]. Demonstrated: opening the pull-tab of a juice can, holding a ball while regulating force direction, tool use (screwdriver-class tasks), insertions and tool changes [S1][S3]. Honda states the hand reproduces 14 grasping postures covering ~80% of daily hand operations (humans use ~30) [S4]. Posture-mapping control predicts the operator's intended grip and switches control mode automatically — joint-angle control for power grasps, fingertip-distance control for precision grasps [S4].

## Sensing
Force-sensing fingertips inherited from ASIMO's manipulation research (ASIMO could sense object state to pour water and adjust grip to changing cup weight) [S1][S3]. Full sensor suite n/a (not disclosed).

## Actuation & power
Wire/tendon-driven hand from 11 forearm motors [S3]; arm/base actuation and battery n/a (not disclosed).

## Compute & software
"Shared autonomy" AI: the remote operator supplies situational judgment; onboard AI autonomously corrects precise movements (insertion, alignment), with seamless switching between teleoperation and autonomy [S1][S4]. Operator interface uses hand-posture capture devices; details of HMD/controllers n/a.

## Safety & compliance
n/a (research program).

## Deployment evidence & traction
No deployments. Public milestones: research announcement 2021-09-30 with FY2023 technology-verification target [S5]; press demonstrations (pull-tab, tool use) covered by Impress, Toyo Keizai (2022) [S2][S3]; multi-finger hand featured in Honda R&D advanced-technology showcase 2025 with 2030 practical aim and open-innovation call [S4]. JAXA collaboration context for remote/lunar operation exists within Honda's avatar program family (vendor-stated space use case) [S1].

## Assessment (analyst view)
*Analyst opinion.* Honda holds arguably the best dexterous-teleop-hand IP outside dedicated hand startups — the 16-joint wire-driven hand plus grip-intent prediction is exactly the operator-experience layer semi-humanoid teleop fleets lack. But the program is unhurried (2030s target, no productization, no disclosed platform specs), consistent with Honda's history of long research arcs. Near-term threat to an EU entrant: none. Long-term: high optionality — if the market matures, Honda can enter with automotive-grade manufacturing, a beloved robot brand, and a ready hand stack; it is also a plausible partner/licensor for hand technology.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://global.honda/jp/stories/025/ | program framing, ASIMO lineage, shared autonomy, use cases | vendor-claimed |
| 2 | https://www.watch.impress.co.jp/docs/news/1396176.html | wheeled dual-arm prototype demo coverage | third-party |
| 3 | https://toyokeizai.net/articles/-/537856 | hand: 4 fingers/16 joints/11 forearm motors, wire drive, pull-tab/ball demos, ASIMO pouring | third-party |
| 4 | https://global.honda/jp/RandD/activity/rdtopics/advancedtech2025/multi_finger/ | 14 grasp postures ~80% coverage, posture mapping, 2030 target | vendor-claimed |
| 5 | https://response.jp/article/2021/09/30/349938.html | 2021-09-30 announcement, FY2023 verification, 2030s practical use | third-party |
