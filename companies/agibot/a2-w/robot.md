# Yuanzheng A2-W (远征 A2-W) — AgiBot / Zhiyuan Robotics

> The A2-W is AgiBot's wheeled flexible-manufacturing robot: a dual 7-DoF-arm torso on a boxy four-wheel-drive base with an integrated tote-carrying frame, sold into auto-parts, 3C and logistics lines. It matters competitively because it anchors what Chinese press calls the first at-scale commercial contract for industrial embodied robots (~100 units to Fulin Precision, 08/2025) and because it is the volume industrial SKU of one of the world's two highest-shipping humanoid makers.

| Field | Value |
|---|---|
| Company | AgiBot / Zhiyuan Robotics (智元机器人) |
| HQ | Shanghai, China |
| Status (2026) | shipping |
| First shown / launch | Unveiled 2024-08-18 (AgiBot annual launch, with A2/A2 Max/Lingxi X1); volume shipping through 2025 [S1][S4] |
| Target applications | Bin/tote destacking & feeding, machine loading/unloading, connector/terminal plugging, logistics transport, battery production lines [S1] |
| Price | Not published; insider range ¥400-800k (~$56-112k) via Yicai [estimated] [S6] |
| Availability | China direct; international via resellers (RobotShop, Generation Robots); purchase (RaaS not advertised) [S3][estimated] |

## Design & morphology
Upper-body-on-vehicle layout rather than anthropomorphic torso: 770 (L) × 620 (W) × 1630 (H) mm, 230 kg with battery [S1][S2, vendor-claimed]. 22 DoF total, including a waist with elevation + pitch (tilt) that gives a 0–2 m working height envelope [S1][S3, vendor-claimed]. The chassis carries a rack/frame for totes so the robot transports what it picks (see images). Operating temp 0–45°C [S1].

## Locomotion
Four-wheel-drive omni chassis with zero turning radius and "crab-walk" lateral translation [S1, vendor-claimed]. Max speed not disclosed; flat-floor robot (max step ~2 mm per third-party spec table) [S2, third-party]. n/a (not disclosed): brakes, slope rating.

## Upper body & manipulation
Dual bionic 7-DoF arms, 5 kg rated payload each (10 kg dual, estimated), capable of parallel and asynchronous dual-arm operation [S1, vendor-claimed]. End effectors are application-swappable (two-finger grippers in the Fulin bin-handling deployment; AgiBot's OmniHand O12 dexterous hand exists in the portfolio) — exact flange/media spec n/a (not disclosed) [estimated]. Skills library: UniGrasp (adaptive grasping), Uni6DPose (6D pose estimation), UniPlug (connector insertion) [S1][S3, vendor-claimed]. Repeatability n/a (not disclosed).

## Sensing
360° lidar on base; 4 AI vision sensors (RGB-D + fisheye mix); two six-axis wrist force/torque sensors; arm collision detection [S1][S2, vendor-claimed]. No tactile skin claimed.

## Actuation & power
Proprietary integrated joint actuators (PowerFlow family used across AgiBot products; A2-W-specific torque figures n/a). 2 kWh hot-swappable battery, ~5 h runtime (300 min), ~2 h recharge [S1][S2, vendor-claimed]. Hot-swap enables near-continuous shift operation [vendor-claimed].

## Compute & software
275 TOPS onboard AI compute (platform not named; consistent with Jetson AGX Orin-class ×2) [S1, vendor-claimed; estimated]. Software: AimRT real-time middleware (open-sourced, ROS 2-compatible); GO-1/GO-2 vision-language-action foundation models and AgiBot World data ecosystem apply across the fleet; robot itself is closed source with SDK/secondary development offered B2B [S2][S7, vendor-claimed/third-party]. Fleet/teleop tooling for data collection available [third-party].

## Safety & compliance
No published ISO 13482 / ISO 10218 / CE certification found [flag]. Vendor claims: 360° obstacle avoidance, arm collision detection, redundant monitoring (PLd-level safety claimed for sibling A2) [S1][S5, vendor-claimed]. Statically stable wheeled base simplifies future certification vs bipeds [estimated].

## Deployment evidence & traction
- Fulin Precision (富临精工, auto parts): order for ~100 A2-W, tens of millions RMB, signed 08/2025 — billed as China's first industrial-scale commercial embodied-robot contract; robots do multi-layer rack bin picking/feeding while AMRs haul pallets; July 2025 live demo: 4 robots, 800+ tote transfers in 3 h, zero failures; vendor says each replaces up to 2 workers [S4, third-party].
- AgiBot company volume: 5,100+ units shipped 2025 (all models), 5,000th production unit 12/2025, ~10k cumulative by 03/2026 [S8, third-party] — A2-W-specific split n/a.
- Battery production line operations cited at launch (undisclosed customer) [S1, vendor-claimed].

## Assessment (analyst view)
*Analyst opinion.* Strengths: proven multi-unit industrial deployment with quantified throughput, hot-swap battery for multi-shift work, strong skills stack (UniGrasp/UniPlug) and the AgiBot data flywheel behind it; price (¥400-800k) undercuts European mobile-manipulator combinations. Weaknesses: utilitarian non-anthropomorphic build limits HRI/service crossover; 5 kg/arm payload is modest; no visible Western safety certification, which blocks EU factory sales in the near term. Threat to a new EU entrant: high in global industrial accounts and any price-sensitive tender; moderate inside the EU until CE/Machinery-Regulation conformity is solved — a certification window an EU entrant can exploit, but likely only for 2-3 years.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://www.agibot.com/products/A2_W | Official specs: dims, 230kg, 22 DoF, 7-DoF arms, 5kg, 2kWh/5h hot-swap, 275 TOPS, sensors, apps | vendor-claimed |
| S2 | https://www.aparobot.com/robots/agibot-a2-w | Spec table incl. AimRT, RGBD/fisheye, collision detection | third-party |
| S3 | https://bikmantech.com/blogs/blogs/agibot-a2-w-wheeled-general-purpose-robot-everything-you-need-to-know | Reseller overview; UniGrasp/Uni6DPose/UniPlug; 1,000th robot 01/2025 | third-party |
| S4 | https://cn.chinadaily.com.cn/a/202508/11/WS6899903da310626720042078.html (also thepaper.cn/newsDetail_forward_31370294) | Fulin Precision ~100-unit order, demo stats | third-party |
| S5 | https://static.generation-robots.com/media/agibot-a2-datasheet.pdf | Sibling A2 datasheet (PLd safety claim, actuator 512 Nm context) | vendor-claimed |
| S6 | _work/market_context.md §4.3 (Yicai) | Insider price range ¥400-800k; A2 Lite $44,560 | estimated |
| S7 | _work/market_context.md §5.1-5.2 | GO-1/GO-2 models, AgiBot World | third-party |
| S8 | https://finance.sina.com.cn/stock/relnews/hk/2026-01-09/doc-inhfswxt0516492.shtml | 2025 shipment volume | third-party |
