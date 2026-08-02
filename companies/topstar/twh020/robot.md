# TWH020 "Xiaotuo" (小拓) — Topstar (拓斯达)

> TWH020 is Topstar's industrial wheeled humanoid: dual bionic 7-DoF arms (±0.05 mm repeatability, 20 kg max dual-arm load) on a 2-DoF waist (95° bend + 550 mm lift) and four-steering-wheel omnidirectional chassis, height-adjustable across a 1.2-1.8 m working envelope. Launched 2025 in the 拓星纪 series alongside the stationary TDM020 dual-arm, it targets material handling, sorting and inspection in injection-molding/3C plants — billed as China's first humanoid working in injection-molding scenarios. It matters as a machine-builder's datasheet-grade semi-humanoid sold into a captive industrial customer base.

| Field | Value |
|---|---|
| Company | Topstar Technology (SZSE 300607) |
| HQ | Dongguan, China |
| Status (2026) | announced / early shipping into own integration projects [estimated] |
| First shown / launch | 2025 [S3] |
| Target applications | Material handling, sorting, inspection; injection-molding machine tending; semiconductor/3C assembly support [S3][S4] |
| Price | n/a (not disclosed) |
| Availability | Via Topstar direct/integrator channels, China [estimated] |

## Design & morphology
Humanoid torso on lift column and wheeled base; working height adjustable ~1.2-1.8 m (waist lift 0-550 mm + 0-95° waist bend) [S2][S4]. 21 DoF excluding hands: 2×7 arms + 2 head + 2 waist + 3 chassis [S2, vendor datasheet]. Weight n/a (not disclosed).

## Locomotion
Four steering-wheel (四舵轮) chassis, 360° omnidirectional; max chassis speed 1.5 m/s [S2]. Indoor factory floors.

## Upper body & manipulation
Dual bionic 7-DoF arms, 690 mm working radius each; rated load 10 kg, max load 20 kg (dual-arm); repeatability ±0.05 mm; TCP max speed 1 m/s; joint speeds 180°/s (all 7 arm joints); joint ranges up to ±170° [S2, vendor datasheet]. End-effector: 8-pin custom connector (M8 A-coded) at flange; compatible with industrial grippers, vacuum cups and dexterous hands via modular swap [S2][S4]. Head: 2 DoF (pan ±90°, tilt -28°~45°).

## Sensing
RGBD (dual-eye depth) camera, microphone, speaker, touch display [S2]; single-line + 3D lidar options on chassis [S4, third-party]. Force/torque sensing not specified (n/a).

## Actuation & power
Joints with dual encoders and brake (关节抱闸); EtherCAT internal bus; 48 V DC internal power; typical consumption 500 W [S2]. Battery ≥3 kWh, >6 h full-load runtime; auto-return charging, battery swap, and direct-power modes [S4, third-party]. Actuator type (harmonic/planetary) n/a.

## Compute & software
Claimed onboard compute "3352 TOPS" [S2, vendor datasheet — figure as printed; plausibly aggregate/INT8 marketing number, treat with caution]. Software stack/SDK n/a (not disclosed); EtherCAT internals suggest industrial controller architecture [estimated].

## Safety & compliance
Joint brakes (mechanical safety); environmental spec 0-50°C, 20-80% RH [S2]. No ISO/CE certifications published (n/a).

## Deployment evidence & traction
Vendor/press claim: first humanoid robot applied in injection-molding scenarios in China; intended deployment inside Topstar's own automation projects (semiconductor assembly, welding, machining contexts mentioned in press) [S3][S4, vendor-claimed/third-party]. No named external customers or unit counts [as of 08/2026].

## Assessment (analyst view)
*Analyst opinion.* Strengths: real machine-builder engineering (complete joint-level datasheet, EtherCAT, brakes, ±0.05 mm claim), a differentiated 1.2-1.8 m height-adjust envelope, and a captive injection-molding customer base for first deployments — the most credible immediate ROI path among Tier-2 entrants. Weaknesses: no disclosed AI/autonomy stack (likely scripted/teleop initially), no safety certification, unknown pricing, and zero brand outside industrial Asia; the "3352 TOPS" claim is marketing-grade. Threat to an EU entrant: moderate in Asian factory automation, low in Europe near-term — but Topstar's template (precision arms + lift + omni base at machine-tool costs) previews the price-performance bar EU industrial semi-humanoids must beat.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.topstarltd.com/lang-cn/productlist/001005001001.html | Tuoxingji series lineup (TWH020, dual-arm, arm; 星仔 quadruped) | vendor-claimed |
| 2 | https://www.topstarltd.com/lang-cn/productview/2239.html | Full TWH020 datasheet: DoF budget, 690mm radius, 10/20kg, ±0.05mm, joint ranges/speeds, EtherCAT, 48V, 500W, 3352TOPS, 550mm lift, 1.5m/s | vendor-claimed |
| 3 | https://news.zol.com.cn/1168/11687893.html | TWH020/TDM020/TM010 context, injection-molding first application | third-party |
| 4 | https://www.ithome.com/0/955/215.htm (+ sohu/csdn roundups) | 3kWh/6h battery, charge/swap modes, lidar suite, 1.2-1.8m height | third-party |
