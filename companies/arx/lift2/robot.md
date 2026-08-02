# LIFT2 (ARX-LIFT2) — ARX (方舟无限)

> LIFT2 is ARX's mobile bimanual research platform: dual force-controlled arms on a lift column and omnidirectional wheeled base, sold from ¥249,800 as a ready-made rig for π0/ALOHA-style imitation learning, VR-teleop data collection and mobile autonomous grasping. Marketed as "the world's first omnidirectional lifting dual-arm platform", it is one of the leading domestic ALOHA-descendant platforms (alongside AgileX Cobot Magic and Galaxea R1) and covers the same competitive ground as far pricier Western research semi-humanoids. Notes here also cover the X7|LIFT predecessor and the stationary AC one data-collection station.

| Field | Value |
|---|---|
| Company | ARX Robotics (方舟无限) |
| HQ | Beijing, China |
| Status (2026) | shipping (research market) |
| First shown / launch | LIFT line 2024; LIFT2 upgrade 2025 [estimated from repo/press timeline] |
| Target applications | Embodied-AI research: imitation-learning data collection, VLA (π0/ALOHA) reproduction, mobile manipulation experiments |
| Price | From ¥249,800 (~$34k) [third-party] |
| Availability | Direct (contact@arx-x.com), China + international research sales |

## Design & morphology
Dual arms mounted on a motorized lift column atop a compact omnidirectional mobile base. Reported lift stroke ~900 mm with maximum working height ~2.4 m from floor [S4, third-party snippet — treat as indicative]. Overall height/weight n/a (not disclosed). LIFT-mini sibling offers a smaller footprint; AC one is the stationary leader-follower dual-arm cart.

## Locomotion
Omnidirectional wheeled base ("全向" — omni; wheel configuration not documented publicly). Speed n/a (not disclosed).

## Upper body & manipulation
Two ARX force-controlled arms (6-DoF class, X5/R5 family; exact model per config): ~5 kg payload per arm on LIFT-class platforms [S4, third-party]; single-arm family specs: L5 620 mm reach/1.5 kg (L5 Pro 3 kg), full-joint force feedback, collision detection, autonomous grasping demos at 4.2 s cycle times [S1]. Parallel-jaw grippers standard; leader-arm teleop and VR teleop supported [S3].

## Sensing
Cameras for data collection (head/wrist mounts, config-dependent); joint torque/force feedback in arms [S1][S3]. Lidar not standard (n/a).

## Actuation & power
ARX integrated force-controlled joint motors, CAN-FD bus (ARX-CAN SDK); onboard battery with XT60/DC distribution, powering compute + arms (capacity n/a) [S3, vendor GitHub docs/photos].

## Compute & software
Onboard mini-PC (photos show consumer mini-PC + CAN hub on base); ROS/ROS 2 stacks (ROS2_LIFT_Play), ARX_PLAY imitation-learning framework (ACT pipelines, conda envs scripted), VR teleoperation SDK, full 采集-训练-部署 (collect-train-deploy) manuals; supports π0 and ALOHA algorithm reproduction [S3][S4, vendor-claimed]. Fully open-source tooling on GitHub.

## Safety & compliance
n/a (research platform; no certifications published). Collision detection in arms [S1].

## Deployment evidence & traction
Shipping into the research market since 2024; ARX arms and LIFT platforms are widely adopted in Chinese university/startup imitation-learning labs and rank among the leading domestic ALOHA-style data-collection platforms [S5, third-party compilation]. Active open-source ecosystem (20+ repos, current manuals). No unit counts disclosed.

## Assessment (analyst view)
*Analyst opinion.* Strengths: complete, cheap, open research stack — hardware + teleop + training pipelines — at ¥249,800 for a mobile bimanual robot, with an installed academic base that creates ecosystem lock-in. Weaknesses: research-grade build (consumer mini-PC, no safety certification, sparse formal specs), 5 kg-class arms, and no path shown toward certified commercial deployment. Threat to an EU entrant: low in commercial markets, high in the research/data-collection segment — an EU platform priced European-style cannot win labs against ARX economics; the smarter play is interoperability with (or procurement of) such platforms.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://news.qq.com/rain/a/20240712A061RI00 | ARX arm family specs/prices, ALOHA reproduction, grasp benchmarks | third-party |
| 2 | https://arx-x.com/ | Product lineup incl. LIFT 2, AC one, X7 | vendor-claimed |
| 3 | https://github.com/ARXroboticsX (LIFT, LIFT-mini, ARX_PLAY, X7s_PLAY, ARX_VR, ARX_all_in_one_readme) | Software stack, VR teleop, CAN SDK, collect-train-deploy manuals, base hardware photos | vendor-claimed (open source) |
| 4 | DuckDuckGo snippets (ARX LIFT2 249800 / lift specs) | ¥249,800 entry price, omnidirectional lifting dual-arm claim, π0/ALOHA support, ~900mm stroke, ~2.4m reach, ~5kg/arm | third-party (snippet-grade) |
| 5 | _work/discovery_china.md entry 28 | Ecosystem role: leading domestic ALOHA-style data-collection platform | third-party (compiled) |
