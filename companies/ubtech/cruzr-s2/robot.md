# Cruzr S2 (克鲁泽S2) — UBTech Robotics

> Cruzr S2 is UBTech's "full-size general-purpose wheeled humanoid" (全尺寸通用轮式人形机器人), launched at the World Robot Conference on 9 Aug 2025. A 1.76 m, 185 kg, 44-DoF wheeled platform with a 0-40 cm body lift, 15 kg payload and UBTech's industrial dexterous hands, it targets sorting, assembly, pharma logistics and hospitality — and gives UBTech a wheeled sibling to its Walker biped line sharing the same Co-Agent/BrainNet software. It matters because a listed, vertically integrated humanoid leader has now fully endorsed the wheeled semi-humanoid form factor and is already exporting it (Japan, Oct 2025).

| Field | Value |
|---|---|
| Company | UBTech Robotics (优必选) |
| HQ | Shenzhen, China |
| Status (2026) | shipping (commercial availability in CN + JP since Oct 2025) |
| First shown / launch | 9 Aug 2025, World Robot Conference (WRC), Beijing [S2][S3] |
| Target applications | Industrial sorting, component assembly, pharmaceutical transfer, warehouse logistics, facility guidance/reception, hospital communications |
| Price | n/a (not disclosed) |
| Availability | China direct; Japan via GA Robotics from 15 Oct 2025 (purchase; cloud fleet mgmt, WMS API) [S4] |

## Design & morphology
Full-size wheeled humanoid: 1.76 m tall, 185 kg, 44 DoF total [S3]. Symmetrical torso with bidirectional bending and a 0-0.4 m lifting range, giving a 0-1.8 m vertical workspace from floor level to shelf height [S1]. Designed to rotate ±170° within 0.8 m-wide aisles — explicitly optimized for narrow commercial/industrial corridors [S1]. The heavy 185 kg mass (vs ~43-76 kg for Walker bipeds) buys stability for 15 kg handling at full arm extension. Confidence: vendor-claimed throughout.

## Locomotion
Wheeled base (drive type not detailed; stability-focused, slope/obstacle adaptive per Japanese distributor material), max speed 2 m/s while carrying loads [S1][S4]. Long-distance autonomous operation is a selling point in Japan (logistics runs) [S4]. No stair capability claimed.

## Upper body & manipulation
Dual arms with 15 kg payload capability (vendor does not break out per-arm figure; the 15 kg is stated as platform payload) and full-space carrying across the 0-1.8 m workspace [S1]. End-effectors: UBTech industrial dexterous hands — the official page says "gen-4 industrial dexterous hands" [S1] while WRC launch coverage describes the fifth-generation hand: 19 active DoF, <1.2 kg per hand, 20 N thumb-tip force, 10 kg grip load [S2] (discrepancy noted; likely gen-4 shipping / gen-5 announced). Claimed sub-millimeter manipulation precision for sorting and component assembly [S1]. Repeatability figure not published; tool changer / flange media n/a (not disclosed).

## Sensing
Pure RGB binocular stereo head vision with deep-learning stereo depth estimation (no structured light/ToF), same philosophy as Walker S2 [S1]. Navigation uses vision-laser (lidar) fusion [S2]. Japanese distributor lists RGB-D camera, IMU and microphone array [S4]. Torque/force sensing in arms/hands not detailed. Confidence: vendor-claimed.

## Actuation & power
UBTech in-house servo joints (long-standing vertical integration; specific actuator specs n/a). Battery: 30 Ah main + 3 Ah backup, hot-swappable, ~8 h runtime (per Japan distributor datasheet summary) [S4]. Charging dock not confirmed.

## Compute & software
Onboard compute not disclosed. Software: UBTech Co-Agent collaborative-intelligence framework and BrainNet 2.0 for multi-robot, multi-task orchestration — demonstrated at WRC 2025 with Cruzr S2, Walker S1/S2 and logistics vehicles co-operating in a warehouse scenario [S2]. Learning-based motion control; cloud fleet management and WMS integration via API in the Japanese offering [S4]. SDK/openness for third parties not documented publicly.

## Safety & compliance
No ISO 13482 / ISO 10218 / CE certification claims found (n/a, not disclosed). For Japan sales, standard commercial-robot practice (e-stop, speed limiting) is implied but not itemized in distributor materials [S4]. This is a gap versus EU expectations.

## Deployment evidence & traction
- WRC 2025 live multi-robot warehouse demo with Walker S2/S1 (vendor demo) [S2].
- Japan: GA Robotics commercial sales from 15 Oct 2025; use cases pitched at logistics warehouses, manufacturing parts supply, facility guidance, hospitals; multiple Japanese trade outlets covered it (LNEWS, LogiToday, RobotStart) [S4][S6]. No named end customers or unit counts yet — traction evidence is thin (third-party confirmed availability, no volume data).
- Legacy Cruzr (2017) history: original Cruzr launched at CES Jan 2017 as a 1.215 m, 17-DoF cloud-connected wheeled service humanoid with U-SLAM navigation and an 11.6" chest touchscreen; deployed over the years in banks, airports, retail and expos worldwide [S5]. S2 reuses the brand but is a different class of machine (full-size, manipulating). The 8-year Cruzr install history gives UBTech unusual service-fleet operations experience.

## Assessment (analyst view)
*Analyst opinion.* Strengths: full-size payload (15 kg) with narrow-aisle agility (±170° in 0.8 m), credible dexterous-hand program, shared software stack with the world's highest-volume industrial biped fleet, listed-company balance sheet, and already-active export channel in Japan. Weaknesses: 185 kg mass complicates safety certification for human-shared spaces; no published price, compute, or safety certifications; real deployment evidence for S2 specifically is still demo-grade. For an EU entrant this is one of the top two or three competitive threats from China: if UBTech pairs S2 with KUKA-class integrators or EU distributors the way it did with GA Robotics in Japan, it will occupy the "industrial wheeled humanoid" slot quickly. Its weakness in certified safety/compliance is the clearest attack surface for a European player.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.ubtrobot.com/en/commercial/products/cruzr-s2 | 0-40 cm lift, 15 kg, 0-1.8 m workspace, ±170°/0.8 m, 2 m/s, gen-4 hands, RGB stereo vision | vendor-claimed |
| 2 | https://news.qq.com/rain/a/20250811A073H200 | WRC 2025 launch, 5th-gen hand (19 DoF, <1.2 kg, 20 N thumb, 10 kg grip), Co-Agent/BrainNet 2.0, vision-laser nav | third-party (quoting vendor) |
| 3 | https://www.yicai.com/news/102765660.html | 1.76 m, 185 kg, 44 DoF, launch 9 Aug 2025 | third-party |
| 4 | https://www.lnews.jp/2025/10/r1015503.html | Japan sales 15 Oct 2025, GA Robotics, battery 30+3 Ah ~8 h, RGB-D/IMU/mics, fleet mgmt | third-party |
| 5 | https://lite.duckduckgo.com/lite/?q=UBTech+Cruzr+2017 (Baidu Baike etc. snippets) | Legacy Cruzr 2017: 1.215 m, 17 DoF, U-SLAM, 11.6" screen | third-party |
| 6 | https://robotstart.info/article/2025/10/15/381232.html | Japanese coverage of GA Robotics launch | third-party |
