# Axol — Almond (Almond Robotics)

> Axol is a dual 7-DoF-arm torso robot for physical-AI development — teleop data collection and policy deployment — sold from $7,999 and shipping from San Francisco in about a week. Mountable standalone, on the Axol Mount, or on the wheeled Axol Cart, it undercuts Chinese dev platforms (ARX/AgileX/Trossen class) with stronger arms (860 mm reach, 6.5 kg peak) and a fully open-source SDK; competitively it is the US price-anchor for bimanual embodied-AI hardware.

| Field | Value |
|---|---|
| Company | Almond (Almond Robotics), YC-backed |
| HQ | San Francisco, CA, USA |
| Status (2026) | shipping (batch orders, ~1 week lead from SF) [S1] |
| First shown / launch | 2026 (YC launch + Product Hunt; press June 2026) |
| Target applications | Physical-AI R&D, teleoperation/data collection, light assembly-line automation, kitchens/warehouse experimentation |
| Price | From $7,999 (robot); $11,999 full kit (base + 3x ZED X One S cameras + ZED Box Orin NX 16GB) [S1][S2] |
| Availability | Direct order, ships from San Francisco ~1 week; US-built |

## Design & morphology
Bimanual torso: two independent 7-DoF arms on a shared torso frame; steel/aluminum/TPU construction with fully internal wiring [S1]. Mounting options: standalone bench mount, "Axol Mount" fixed stand, or "Axol Cart" wheeled base (semi-humanoid configuration) [S1]. Height/weight n/a (not disclosed). DoF: 14 in arms (+ grippers).

## Locomotion
None in base product; Axol Cart provides a pushed/positioned wheeled platform (no evidence of powered autonomous navigation) [S1, vendor-claimed; mobility class estimated].

## Upper body & manipulation
2× 7-DoF arms; 860 mm reach each; 6.5 kg peak payload per arm; 1 mm repeatability; full 180° wrist pitch and yaw; 500 Hz control over CAN [S1][S2]. End-effectors: 2× 2-finger grippers standard [S2]. FAKRA GMSL 2.0 passthrough at the wrist for cameras (media at flange: data) [S1].

## Sensing
Optional perception kit: 2 wrist cameras + 1 head camera (ZED X One S) with mounts/cabling; ZED ecosystem streaming [S1][S2]. No lidar/base sensors (not a navigating robot).

## Actuation & power
Electric joint motors on CAN bus (type/gearing not disclosed; QDD-class estimated from 500 Hz control + price point). 1500 W power supply included; mains-powered (no battery disclosed; Cart battery n/a) [S1].

## Compute & software
Kit compute: ZED Box Orin NX 16GB [S2]. Open-source Python SDK: bimanual IK solver, low-level CAN motor interface, ZED camera streaming, LeRobot bindings; WebXR VR teleoperation in-browser [S1]. Designed for imitation-learning pipelines (ACT/diffusion/VLA via LeRobot).

## Safety & compliance
n/a (not disclosed); research/dev platform, no industrial safety certification claimed.

## Deployment evidence & traction
- Shipping in batches; first-batch pricing $7,999 [S2, vendor-claimed].
- Marketed to physical-AI teams; Product Hunt + Hackster/TechEBlog coverage (June 2026) [S2][S4].
- No named customers or unit counts disclosed; data-collection service and on-site Bay-Area repair offered [S1].

## Assessment (analyst view)
*Analyst opinion.* Strengths: aggressive price/spec ratio (6.5 kg × 860 mm arms at $8k), genuinely open SDK with LeRobot/WebXR integration, US assembly with 1-week lead — a clean wedge into research labs and AI startups. Weaknesses: no mobility/autonomy, no safety certification, unknown reliability at duty cycle, and a services-light two-person-scale company. Threat to a new EU entrant: low on industrial deployments, but real in the dev-platform segment — an EU entrant selling €50k+ research platforms will be price-anchored against Axol; conversely it validates buying such platforms for data collection rather than building them.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://almond.bot/ | Full specs, SDK, pricing, configurations, shipping | vendor-claimed |
| 2 | https://www.hackster.io/news/almond-wants-to-put-their-dual-arm-axol-robot-on-your-assembly-line-6c6fb2e99428.amp | Founders, grippers, repeatability, kit contents/pricing | third-party |
| 3 | https://www.ycombinator.com/launches/QlH-axol-a-dual-arm-robot-built-for-ai | YC launch framing | vendor-claimed |
| 4 | https://www.techeblog.com/almond-axol-dual-arm-ai-robot/ | Spec confirmation | third-party |
