# Vinci (轮式人形机器人) — SVT Robot (时空变量)

> Vinci is SVT Robot's wheeled humanoid: high-payload collaborative arms on a four-wheel-drive, four-wheel-steer omnidirectional chassis rated to 200 kg, teleoperated via exoskeleton/VR at millisecond latency to collect whole-body data for VLA models, with end-to-end VLA autonomy as the goal. It targets industrial material handling (bin packing, warehouse placement) and embodied-AI research. Competitively it is a long-tail entrant assembling a semi-humanoid from open-source arm technology (OpenArm lineage) and a heavy omni base — evidence of how low the entry barrier has become.

| Field | Value |
|---|---|
| Company | Hangzhou Spacetime Variable Technology (杭州时空变量科技有限公司) |
| HQ | Hangzhou, Zhejiang, China |
| Status (2026) | prototype (demos; no public sales evidence) [estimated] |
| First shown / launch | 2025 (company registered 2025-04; demo videos late 2025) [third-party] |
| Target applications | Industrial handling (autonomous bin packing, goods transfer, warehouse placement), VLA research/data collection |
| Price | n/a (not disclosed) |
| Availability | n/a (not disclosed); direct contact via svtrobot.com |

## Design & morphology
Wheeled humanoid (轮式人形机器人): dual collaborative arms on a boxy 4-wheel omnidirectional base; overall height/weight not disclosed. Base payload 200 kg [S3][S4, vendor-claimed via directory snippets]. Arm count/DoF not formally published; company's arm line is the open-source 7-DoF OpenArm design (leader/follower capable) [S1][S5], so dual 7-DoF is probable [estimated].

## Locomotion
Four-wheel-drive, four-wheel-steer (4WD/4WS) omnidirectional chassis: lateral, diagonal and in-place rotation [S3][S4, vendor-claimed]. Speed n/a (not disclosed). Indoor industrial floors [estimated].

## Upper body & manipulation
"High-load collaborative arm" integration [S4]; if OpenArm-based: 7 DoF per arm, high backdrivability/compliance, designed for contact-rich physical-AI tasks [S1, vendor-claimed]. Gripper/end-effector details n/a (demo videos show simple two-finger grippers handling bottles/cans) [S5, third-party observation]. Payload per arm n/a (not disclosed).

## Sensing
Multi-sensor fusion claimed (cameras for VLA); details n/a (not disclosed). Teleoperation rig provides whole-body motion capture via wearable exoskeleton [S4][S5].

## Actuation & power
n/a (not disclosed). OpenArm design uses backdrivable motor joints [S1, vendor-claimed]. Battery/runtime n/a.

## Compute & software
ROS 2; proprietary VLA data-collection pipeline and end-to-end VLA model integration (vision + language + action); millisecond-latency full-body teleoperation supporting exoskeleton and VR input [S3][S4, vendor-claimed]. Company also demonstrates MuJoCo + PPO RL sim2sim/sim2real workflows [S5]. Web console (control.svtrobot.com) and visualization tools [S2].

## Safety & compliance
n/a (not disclosed).

## Deployment evidence & traction
No customers, pilots or unit counts disclosed. Public evidence limited to office demo videos (dual-arm exoskeleton teleoperation pouring/pick tasks, late 2025) [S5, third-party observation]. Treat all industrial-application claims as aspirational marketing.

## Assessment (analyst view)
*Analyst opinion.* Strengths: sensible architecture (heavy 4WS omni base + compliant open-source arms + teleop-to-VLA pipeline) achievable by a tiny team; 200 kg base rating is unusual and could suit heavier industrial payloads than typical research platforms. Weaknesses: months-old company, no disclosed funding, pricing, customers, or even full specs; the robot may not exist beyond prototype/renders; reliance on open-source arm design offers no moat. Threat to an EU entrant: negligible directly, but symptomatic — dozens of such teams can now assemble credible wheeled dual-arm demos within months, so differentiation must come from reliability, safety certification and deployment operations, not raw hardware.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://svtrobot.com | OpenArm 7-DoF open-source arm positioning, company focus (meta/schema + JS-bundle docs text) | vendor-claimed |
| 2 | https://api.svtrobot.com/api/public/company/info | Address/contact; console links | vendor-claimed (API) |
| 3 | _work/master_list.md ADDENDUM 2 + _work discovery notes | Founded 2025-04-15; Vinci 4WD omni, 200kg, ROS2 + VLA | third-party (compiled) |
| 4 | DuckDuckGo/Bing search snippets (时空变量 Vinci 轮式人形机器人) | 4WD/4WS omni chassis, 200kg payload, lateral/diagonal/in-place motion, ms-latency teleop, VLA, bin-packing use case | third-party |
| 5 | https://www.youtube.com/@Svtrobot (videos EJ7ldRQBBkQ, FXkWcJ1IT2I, 9M48IdAHC5Y, 9p5jF8HegcM) | Exoskeleton dual-arm teleop demos, OpenArm hardware, RL sim2real | third-party (video observation) |
