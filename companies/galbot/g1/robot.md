# Galbot G1 — Galbot / Galaxy General (银河通用)

> The G1 is Galbot's first-generation general-purpose semi-humanoid: dual 7-DoF arms on a single telescoping/folding leg over an omnidirectional wheeled base, purpose-built for 24/7 unmanned retail (pharmacy kiosks) and factory logistics. It matters because it is the most commercially proven retail semi-humanoid anywhere (~170 unmanned stores in 40+ cities, China's first robot-pharmacy license) and is backed by ~$1.15B of funding and blue-chip factory orders (CATL, Mercedes-Benz China, Bosch, Toyota).

| Field | Value |
|---|---|
| Company | Galbot / Galaxy General (银河通用) |
| HQ | Beijing, China |
| Status (2026) | shipping |
| First shown / launch | Unveiled June 2024; store/factory deployments through 2024-2026 [S3][S5] |
| Target applications | Unmanned pharmacy/retail picking, factory logistics (part transfer, machine tending), research [S3][S5] |
| Price | JD.com listing ¥690-700k (~$97k); flash sale ¥630k (02/2026); Western reseller $119,995; enterprise software ~$27k/robot/yr [S3][S6][estimated] |
| Availability | China direct + JD.com; limited international resellers; purchase + software subscription [S3][S6] |

## Design & morphology
1.73 m tall, ~85-92.5 kg (sources differ: 85 kg chozan/aparobot [S3][S2]; 92.5 kg discovery/CB Insights [S7]); arm span 1.9 m; workspace floor-to-2.4 m thanks to a single telescoping, knee-folding leg (~65 cm lift stroke) on an omni wheeled base [S2][S3, third-party]. The leg folds to lower the torso for floor-level picks and compact transport. ~24 joints/DoF total (third-party; one aggregator claims 47 DoF, likely counting hand DoF) [S7][S4, third-party]. No anthropomorphic neck; sensor head is fixed oval pod.

## Locomotion
Omnidirectional wheeled base; ~1.5 m/s max speed [S7, estimated/third-party]; indoor flat-floor operation. Brakes/slope n/a (not disclosed).

## Upper body & manipulation
Dual 7-DoF arms, 5 kg payload each (10 kg dual-arm) [S2][S3, third-party]. End effectors: parallel two-finger grippers in pharmacy/factory deployments; dexterous-hand and suction options shown in demos; wrist-mounted depth cameras on both arms [S3, third-party]. Grasping: GraspVLA foundation model (SynGrasp-1B synthetic pre-training) — zero-shot open-vocabulary grasping incl. transparent/specular objects (95% transparent-object claim; 99.5% success across ~5,000 pharmacy SKUs) [S4][S5, vendor-claimed]. Repeatability n/a (not disclosed).

## Sensing
Head: binocular/stereo camera pod (RGB-D) [S3, third-party]. Wrists: 2× depth cameras + 2× six-axis force/torque sensors [S3]. Base: lidar for navigation [estimated — visible in deployments, exact model n/a]. Speakers, Wi-Fi 2.4/5 GHz, Bluetooth, Ethernet/USB [S2][S3].

## Actuation & power
Electric actuators (details n/a). Battery: ~8 h continuous lab operation (market-context) to 10 h vendor claim (600 min); 54.6 V/6 A charging [S2][S3, vendor-claimed/third-party]. No hot-swap claimed; kiosk robots charge in-store between order bursts [estimated].

## Compute & software
Onboard NVIDIA Jetson AGX Orin 64GB (275 TOPS) [S7, third-party]. Software: three-tier "brain–cerebellum–controller" architecture (aggregators brand it "AstraBrain"): VLM task planner → GraspVLA/navigation skills → whole-body control; natural-language tasking; fleet/store management cloud for unmanned kiosks; enterprise software subscription ~$27k/robot/yr [S4][S6, third-party]. No open SDK/ROS support advertised (closed B2B) [S2, third-party].

## Safety & compliance
No published ISO/CE certifications found [flag]. Operates unmanned around the public in enclosed kiosk format (customers outside, robot inside) — a de-facto safety architecture that sidesteps close HRI [estimated]. Factory deployments run in fenced/monitored cells per customer norms [estimated].

## Deployment evidence & traction
- Unmanned retail: ~170 Galbot kiosk stores/pharmacies in 40+ cities; 10+ Beijing pharmacies fully autonomous; up to 370 orders/day per store; >50% labor-cost reduction claim; 100 flagship stores targeted by end-2026 [S3][S5, vendor-claimed/third-party].
- Regulatory first: pharmaceutical retail license granted in Beijing Haidian on 2026-03-12 — "China's first pharmacy robot" license [S5, third-party].
- Factory: CATL (claimed world-first humanoid in regular ops), Mercedes-Benz China sunroof transfer, Zeekr, BYD (15% efficiency claim), Bosch, Toyota, BAIC, SAIC; cumulative orders "several thousand units" [S5, vendor-claimed; BMW unverified].
- Funding validation: Series D 03/2026 RMB 2.5B with state-strategic investors [S6, third-party].

## Assessment (analyst view)
*Analyst opinion.* Galbot's strength is a real operating business: recurring-revenue unmanned stores, a regulatory moat (pharmacy license), simulation-first grasping IP that avoids expensive teleop data farms, and top-tier funding. Weaknesses: single-leg/no-neck morphology limits tasks needing torso pose diversity; specs (payload, runtime, DoF) are middling and inconsistently disclosed; the closed stack means no developer ecosystem. Threat to an EU entrant: very high in retail/pharmacy and intralogistics — Galbot could enter the EU through retail chains where certification burden is lower than factory HRI; EU entrants should expect it to defend aggressively on total cost per store and shelf-SKU generalization.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://www.galbot.com | Official site (JS; limited extractable spec) | vendor-claimed |
| S2 | https://www.aparobot.com/robots/galbot-g1 | 1730mm, 85kg, 65cm lift, 240cm reach, 600min runtime, connectivity | third-party |
| S3 | https://chozan.co/galbot-g1/ | Sensors (binocular head, 2 wrist depth cams, 2 F/T), 10h runtime, 54.6V charging, pricing, pharmacy KPIs | third-party |
| S4 | https://arxiv.org/abs/2505.03233 + https://www.robotsinternational.com/Galbot-G1.htm | GraspVLA/SynGrasp-1B; "AstraBrain" branding, $119,995 reseller price, first demo 03/2025 claim | third-party |
| S5 | _work/market_context.md §7 (Galbot entry) | ~170 kiosks/40+ cities, license 2026-03-12, 99.5%/5,000 SKUs, factory customers | third-party (compiled) |
| S6 | https://technode.com/2026/03/02/humanoid-robot-maker-galbot-raises-rmb-2-5-billion/ | Series D, valuation | third-party |
| S7 | _work/discovery_china.md entry 3 + DDG spec searches (AGX Orin 64GB/275 TOPS; 92.5kg; 24 joints; ~1.5 m/s) | Compute, weight variant, DoF | third-party |
