# Genie G2 (精灵 G2) — AgiBot / Zhiyuan Robotics

> The Genie G2 is AgiBot's second-generation wheeled interactive/industrial semi-humanoid: a full anthropomorphic torso (3-DoF neck, 3-DoF waist, dual 7-DoF force-controlled arms, dexterous hands) on a height-adjustable "waist-and-leg" mechanism over a 4-DoF omnidirectional chassis. Launched 2025-10-16, it is the commercial productization of the Genie data-collection line that produced the AgiBot World dataset, and it immediately booked one of China's largest embodied-AI orders (Longcheer, hundreds of millions RMB, ~1,000 units for tablet production).

| Field | Value |
|---|---|
| Company | AgiBot / Zhiyuan Robotics (智元机器人) |
| HQ | Shanghai, China |
| Status (2026) | shipping |
| First shown / launch | 2025-10-16 (online livestream launch) [S2] |
| Target applications | Electronics/3C assembly (sub-mm precision), automotive parts assembly (e.g. seatbelt lock cylinders), logistics sorting, commercial guiding/interaction, data collection for embodied AI [S2][S1] |
| Price | n/a (not disclosed); predecessor Genie G1 listed at ¥450k (~$62k) [third-party] |
| Availability | China direct; international via RobotShop; deliveries under Longcheer framework from late 2025 [S3][third-party] |

## Design & morphology
Human-proportioned white/black torso on wheeled base: height 1,225–1,795 mm (kneel-to-stand lift), 640 mm W × 760 mm L footprint, 185 kg with batteries [S1, vendor-claimed]. 26 total active DoF: 3 neck, 7 per arm (×2), 5 waist-and-leg (waist yaw ±174.5°, roll ±25°, pitch −110°…+64°; knee 0–152°; ankle −62–0°), 4 chassis [S1]. IP42 whole-machine, IP50 arms; "100% automotive-grade components"; operating temp −15…50°C [S1][S2, vendor-claimed]. Facial interaction screen with expressive animations and eye-gaze tracking [S4, vendor-claimed].

## Locomotion
4-DoF omnidirectional wheeled chassis: omnidirectional movement, crab-walk lateral translation, in-place rotation (spec PDF variant lists Ackermann steering + lateral + in-place); chassis speed 1.5 m/s [S1, vendor-claimed].

## Upper body & manipulation
Dual 7-DoF arms, rated 5 kg each; joint ranges up to ±178° [S1, vendor-claimed]. Launch claims: "world's first cross-wrist (十字腕) force-controlled arm", high-precision joint torque sensors along the whole arm, ~0.5 N force-control resolution, sub-millimeter assembly precision [S2][S4, vendor-claimed]. Hands: five-finger dexterous hands shown on launch renders (AgiBot OmniHand family); grippers configurable — exact hand DoF for the shipping config n/a (not disclosed). Wrist RGB-D cameras on both arms [S1].

## Sensing
2× 3D lidar, 1× stereo camera, 3× fisheye cameras, 1× head RGB-D, 2× wrist RGB-D; microphone array + speaker; multi-color LED strip [S1, vendor-claimed]. Joint torque sensing in arms [S1].

## Actuation & power
Electric actuators with full-arm torque sensing (harmonic/precision reducers per launch coverage) [S2, third-party]. Dual hot-swappable batteries, 1,652 Wh total, ≈4 h per charge; supports direct charging, battery swapping and autonomous dock recharge (≤2 h, 100–240 V, 54.75 V/15 A charger); dual-battery swap rotation marketed as enabling 24/7 factory operation [S1][S2, vendor-claimed].

## Compute & software
NVIDIA Jetson Thor T5000, 2,070 TFLOPS (FP4), end-to-end latency <10 ms claimed [S1][S2, vendor-claimed]. Wi-Fi, Bluetooth, 4G/5G (optional), NFC; handheld wireless teach terminal; smart OTA; remote wake-up; secondary development supported (B2B SDK; core stack closed-source) [S1]. AI stack: GO-1/GO-2 (Genie Operator) VLA foundation models; "采训推一体" (collect-train-deploy) data flywheel inherited from Genie G1; AgiBot World 2026 dataset collected on wheeled G2 units (RGB-D/tactile/lidar, error-recovery, digital twins) [S5, third-party].

## Safety & compliance
No published third-party certifications found [flag]. Vendor: joint torque sensing for compliant contact, IP42/IP50, automotive-grade components, collision-aware force control [S1][S2, vendor-claimed].

## Deployment evidence & traction
- Longcheer Technology (龙旗科技, 603341.SH; major ODM): framework order "hundreds of millions RMB", reported ~1,000 units for tablet production lines (flexible grasping, multi-station coordination; AgiBot cites 310 tablets/h line rate) — announced at/around the 10/2025 launch; one of China's largest embodied-AI robot orders [S2][S3, third-party].
- Junpu Intelligent (均普智能) partnership for automotive assembly announced at launch [S2, third-party].
- Genie G1 history: concept shown 11/2023; released 2025-08-18 at ¥450k as a "data-collection-native" wheeled robot (20 DoF, ~6 kg/arm, 4 h battery, 1.3–1.8 m variable height); G1 fleets collected the AgiBot World dataset (1M+ trajectories, 217 tasks) and did 60-day warehouse data-collection deployments; G2 inherits this ecosystem [S6][S5, third-party].
- AgiBot total: 5,100+ units shipped in 2025 across models [third-party].

## Assessment (analyst view)
*Analyst opinion.* The G2 is the most complete "industrial + interactive" wheeled semi-humanoid spec sheet on the market: Jetson Thor-class compute, full-arm torque sensing, hot-swap dual batteries, height-adjustable posture, and a launch-day thousand-unit anchor order. Its data-flywheel lineage (AgiBot World) means software improves fleet-wide — the key moat. Weaknesses: 5 kg/arm rated payload, ~4 h battery (mitigated by swap), undisclosed pricing, and zero Western certification/footprint so far. Threat to an EU entrant: very high on capability-per-yuan and AI stack; the realistic EU defense is certification, local integration/service, and data governance (AgiBot World-style fleet learning may face EU data/compliance friction).

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://www.agibot.com/products/G2 (spec table; mirrored in images/genie-g2-spec-table.jpg) and https://cdn.robotshop.com/media/A/AGE/RB-Age-04/pdf/AgiBot-G2-Specification.pdf | Full official specs: dims, 185kg, 26 DoF, ROM, sensors, 1652Wh, Thor T5000, IP42/IP50 | vendor-claimed |
| S2 | https://qiye.chinadaily.com.cn/a/202510/16/WS68f0b2b8a310c4deea5ecac8.html | Launch 2025-10-16, cross-wrist force arm, Thor 2070 TFLOPS <10ms, −15–50°C, 24h dual-battery, Longcheer + Junpu orders | third-party |
| S3 | DuckDuckGo-indexed CN press (launch coverage, 10/2025) | Longcheer ~1,000 units, "hundreds of millions RMB" framework | third-party |
| S4 | https://www.aparobot.com/robots/agibot-g2 | 0.5N force control, IP ratings, sensor list, closed source | third-party |
| S5 | _work/market_context.md §5.1-5.2 | GO-1/GO-2, AgiBot World & AgiBot World 2026 on G2 | third-party |
| S6 | https://toolnavs.com/article/1010 + DuckDuckGo-indexed G1 coverage | Genie G1 positioning, ¥450k, 2025-08-18 release, 20 DoF, data-collection role | third-party |
