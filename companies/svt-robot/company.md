# SVT Robot — Hangzhou Spacetime Variable Technology (杭州时空变量科技有限公司)

| Field | Value |
|---|---|
| HQ | Room 309, Block A, Building C, 958 Xixi Road, Liuxia, Xihu District, Hangzhou, Zhejiang, China [vendor API] |
| Founded | 2025-04-15 (business registration) [third-party]; site schema claims "foundingDate 2020" — likely team/prior-activity claim [vendor-claimed, conflicting] |
| Founders / key people | n/a (not disclosed) |
| Employees (approx.) | n/a (not disclosed); very small startup [estimated] |
| Ownership / listing | Private |
| Total funding / valuation | n/a (not disclosed) |
| Semi-humanoid products | [Vinci](vinci/robot.md) (轮式人形机器人, 4WD/4WS omni wheeled humanoid) |
| Other products | OpenArm open-source 7-DoF humanoid arm (build/derivative of the Enactic OpenArm design), exoskeleton teleoperation system, mobile robot chassis, wheel-legged quadruped (per discovery notes), DummyX RL sim work |
| Website | https://svtrobot.com (control.svtrobot.com console, visual.svtrobot.com; YouTube @Svtrobot) |

## Company background
Hangzhou Spacetime Variable Technology (时空变量, "SVT Robot") is a young Hangzhou startup (registered April 2025) focused on "robot core algorithms" — intelligent control of arms and chassis — plus the hardware to carry them: mobile robot platforms, robotic arms and integrated mobile-manipulation robots for embodied-AI R&D, system integration and application validation [vendor-claimed, site/API]. The company runs a small web platform with customer console and visualization tools, and publishes demo videos (dual-arm exoskeleton teleoperation, RL sim-to-real with MuJoCo/PPO) on YouTube [vendor-claimed/third-party].

Two product threads are visible. First, the **Vinci** wheeled humanoid: a four-wheel-drive/four-wheel-steer omnidirectional chassis rated to 200 kg carrying high-payload collaborative arms, with full-body millisecond-latency teleoperation (exoskeleton/VR) for VLA data collection and end-to-end VLA autonomy, aimed at industrial handling (bin packing, warehouse placement) [vendor-claimed/third-party snippets]. Second, **OpenArm**: SVT's site and documentation are heavily built around the open-source 7-DoF OpenArm — its docs describe leader/follower teleop configs and use the exact language of the Enactic OpenArm project ("open-source 7-DOF humanoid robotic arm designed for physical AI research... high backdrivability and compliance"). SVT thus appears to manufacture/sell and support hardware based on the Enactic open-source design rather than an independent arm of the same name; no formal affiliation with Enactic is documented [analyst assessment, third-party].

## Relevance to the semi-humanoid market
SVT is a data-point in the long tail of Chinese wheeled-humanoid startups: algorithm-first teams assembling semi-humanoids from open-source arm designs and commodity omni chassis, targeting the VLA data-collection/research market at presumably low price points. Individually minor; collectively this cohort compresses prices and validates the "teleop-to-VLA" industrial-handling playbook an EU entrant would compete against. Trajectory unproven — no funding, customers or pricing disclosed.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://svtrobot.com (page meta + schema.org) | Company name, Hangzhou address, OpenArm 7-DoF positioning, "foundingDate 2020" claim | vendor-claimed |
| 2 | https://api.svtrobot.com/api/public/company/info | Registered address, contact, mission, YouTube link | vendor-claimed (API) |
| 3 | _work/master_list.md ADDENDUM 2 (registry check) | Founded 2025-04-15; Vinci 4WD omni, 200kg, ROS2+VLA; wheel-legged quadruped | third-party (compiled) |
| 4 | DuckDuckGo/Bing search snippets (时空变量 Vinci) | Vinci: 4WD/4WS omni chassis, 200kg, lateral/diagonal/in-place motion, VLA, industrial handling | third-party |
| 5 | https://www.youtube.com/@Svtrobot | Demo videos: OpenArm exoskeleton teleop, DummyX MuJoCo RL sim2real | vendor-claimed (videos) |
