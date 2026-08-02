# Tian Yi 2.0 (天轶2.0) — X-Humanoid (Beijing Humanoid Robot Innovation Center)

> Wheeled dual-arm "wheel-arm robot" from the Tiangong biped maker: humanoid torso with two 7-DoF arms and dexterous hands on an AMR-style wheeled base via an articulated pitch linkage. Competition-proven autonomy (gold at the 2025 World Humanoid Robot Games materials-handling event) and retail availability on JD.com make it one of the most credible Chinese wheeled semi-humanoids for inspection and industrial tasks.

| Field | Value |
|---|---|
| Company | X-Humanoid / Beijing Humanoid Robot Innovation Center (北京人形机器人创新中心) |
| HQ | Beijing, China |
| Status (2026) | shipping (retail on JD.com since 2025-10-17) [S2] |
| First shown / launch | 2025 (Tian Yi 2.0; medals at World Humanoid Robot Games Aug 2025) [S2] |
| Target applications | Patrol & inspection (visible + thermal IR), tour-guide/reception, industrial manufacturing, power-grid inspection, elderly-care services |
| Price | ~USD 60,000 (third-party listing; not vendor-confirmed) [S3] |
| Availability | China; retail purchase via JD.com [S2] |

## Design & morphology
Humanoid upper body (head, torso, two arms) mounted via an articulated pitch linkage on a low AMR-style wheeled base — the linkage lets the torso pitch forward/extend to vary working height, from floor-level reach to standing height [S1, vendor imagery]. Overall height/weight n/a (not disclosed). DoF: 7 per arm plus multi-DoF five-finger hands; total DoF not disclosed.

## Locomotion
Four-wheel AMR base (enclosed; wheel arrangement suggests diff-drive or double-steer — not disclosed). Speed, gradeability, brakes n/a (not disclosed). Elevator use and door/button operation demonstrated as autonomous behaviors [S1].

## Upper body & manipulation
Dual 7-DoF arms with five-finger dexterous hands controlled at 20 Hz (灵巧手:20 Hz per vendor spec graphic) [S1]. Payload and reach n/a (not disclosed). Manipulation credibility: 27 fully autonomous precision insertions of 8 mm-diameter material at the Aug 2025 World Humanoid Robot Games (gold + silver medals) [S2, third-party]. Tool changer / media at flange n/a.

## Sensing
Head: single-line lidar (单线激光雷达) plus 720P RGB camera and linear microphone array [S1]. Patrol payloads add visible-light and thermal-infrared inspection sensing [S1]. Wrist/hand and base sensor details beyond the above n/a (not disclosed).

## Actuation & power
Actuator types n/a (not disclosed). Battery: 48 V 15 Ah (~0.72 kWh) [S1]. Runtime, hot-swap, dock n/a (not disclosed).

## Compute & software
NVIDIA Jetson AGX Orin 64 GB onboard; Wi-Fi 6, Ethernet, Bluetooth [S1]. OS: Ubuntu 22.04 with a ROS 1 control layer [S1]. Autonomy built on the center's Huisi Kaiwu (慧思开物) general embodied-AI platform [S3]. Interaction: low-latency emotional voice dialogue for guide/reception roles; VR/teleoperation-cabin remote control offered for high-risk settings [S1].

## Safety & compliance
n/a (not disclosed). No ISO/CE claims found; teleop cabin marketed for hazardous environments.

## Deployment evidence & traction
Retail sale on JD.com from 2025-10-17 (alongside Tiangong 2.0 biped) [S2]. Competition wins Aug 2025 (World Humanoid Robot Games materials-handling) [S2]. Power-grid inspection and industrial deployments claimed by vendor; named customers n/a (not disclosed).

## Assessment (analyst view)
*Analyst opinion.* Strengths: state backing and ecosystem pull, competition-validated autonomous precision manipulation (rare, verifiable evidence), retail availability at ~$60k, sensible inspection-first go-to-market. Weaknesses: modest published hardware specs (0.72 kWh battery, 720P camera, ROS 1 legacy layer), undisclosed payload/runtime, and the center's priorities may stay research/ecosystem-oriented rather than commercial support. Threat to a new EU entrant: moderate — strong domestic benchmark and price anchor, but state-affiliated origin and China-first channel limit near-term EU penetration.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.x-humanoid.com/detail/tianyi.html (+ /img/m_tianyi.png spec graphic) | form factor, sensors, battery, compute, OS, use cases | vendor-claimed |
| 2 | DuckDuckGo aggregated snippets (Baidu Baike, Sina, Sohu) | competition results, JD.com launch, 7-DoF arms | third-party |
| 3 | https://humanoid.guide/product/tian-yi-2-0/ | price ~$60k, applications | third-party |
