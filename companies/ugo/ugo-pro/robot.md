# ugo Pro — ugo, Inc.

> ugo Pro is a 180cm wheeled avatar robot with two 7-axis arms on a height-adjustable lifter, built for building security, inspection and reception in Japan. It is the workhorse of Japan's teleop+autonomy hybrid model: autonomous patrols with remote human pilots for exceptions, operating elevators and card readers with its arms. Since October 2025 a research variant, **ugo Pro R&D**, is sold as an imitation-learning/physical-AI data-collection kit (LeRobot-integrated, bilateral haptic teleop) — making ugo a competitor in both service RaaS and embodied-AI research platforms.

| Field | Value |
|---|---|
| Company | ugo, Inc. (ex-Mira Robotics) |
| HQ | Tokyo, Japan |
| Status (2026) | shipping |
| First shown / launch | Lineage from 2019 (gen-1); current Pro generation from 2021/22 (ugo G4); Pro R&D kit announced 10/2025 |
| Target applications | Security patrol, facility inspection, reception/guidance, meter reading; R&D variant: imitation learning research |
| Price | n/a (not disclosed) for Pro — RaaS monthly fee via partners ("negotiable"); sibling ugo Ex listed at ¥98,000/mo (2021) as price anchor [S4] |
| Availability | Japan, via facility-management/security partners (Taisei Co., Toyo Tech, Telwell West Japan); R&D kit sold direct to labs |

## Design & morphology
Upper-body-on-lifter avatar: H1,800 × W440 × D580mm, ~54kg [S1, vendor-claimed]. Two 7-axis arms flank a torso with a facial display screen; a vertical lift mechanism adjusts working height (range not disclosed) so cameras/arms can reach panels, desks and card readers at different heights [S1]. Slim 44cm width is deliberate — it fits standard Japanese office corridors, elevator cars and security gates.

## Locomotion
Wheeled base (drive type not disclosed; diff-drive estimated), 0.4-3.6 km/h, climbs ~1cm steps, 5° (8.5%) max gradient [S1, vendor-claimed]. Indoor use; elevator transitions handled either physically (arm presses buttons) or via building-system API integration [S1].

## Upper body & manipulation
Two 7-axis arms with collision detection; demonstrated tasks: pressing elevator/door buttons, IC-card authentication at security gates, flipping switches, opening door handles, gesturing [S1][S2]. Payload per arm n/a (not disclosed; light, est. ≤1kg — designed for interface actuation, not carrying). Standard end-effectors are simple pointer/gripper tips; R&D variant supports gripper work for assembly/sorting experiments [S2]. No tool changer / media at flange disclosed.

## Sensing
3 HD cameras with ring lights for dark environments, 360° coverage; 2D LiDAR; 2 depth sensors; ultrasonic sensors; charging-marker sensor; barometric (floor-detection) sensor [S1, vendor-claimed]. R&D kit adds a head-mounted camera synchronized with arm-motion logging [S2].

## Actuation & power
Actuator type n/a (not disclosed). Runtime ~8h standby / ~4h continuous travel at 1.9 km/h; recharge ~2.5h; autonomous return-to-charger via marker [S1, vendor-claimed]. Battery capacity n/a (not disclosed).

## Compute & software
Onboard compute n/a (not disclosed). Connectivity: Wi-Fi, LTE/5G via external router+SIM [S1]. **ugo Platform**: cloud fleet management — multi-unit monitoring, route mapping, workflow automation ("ugo flows"), automated reporting; pilots operate via browser from a remote operations center [S1]. Hybrid autonomy: scheduled autonomous patrols, human teleop takeover for exceptions. **ugo Pro R&D** software: LeRobot (Hugging Face) open-source framework integration, ugo RobotConfig Library for data collection/visualization/training/inference, bilateral force-feedback dual-arm controller, Meta Quest 3S support planned — positioning it as a VLA-model development platform [S2, vendor-claimed].

## Safety & compliance
Arm collision detection; low speed; obstacle avoidance [S1]. No published ISO 13482 / other certification — n/a (not disclosed).

## Deployment evidence & traction
- **Teikyo University Itabashi Campus** — security system via Taisei Co. (Nagoya facility services), from 05/2024 [S5, third-party].
- **YANMAR FLYING-Y BUILDING (Yanmar HQ, Osaka)** — formal security deployment via Yanmar Business Services/Taisei, 11/2024 [S6, third-party].
- **Mainichi Newspaper Building, Osaka** — "ugo TS series" avatar security robot via Toyo Tech, 04/2025 [S7, third-party].
- **Osaka Kogin Building** — security ugo with generative-AI auto-guidance, 10/2025 [S7, third-party].
- Earlier gen deployments in Tokyo office towers (Mitsui Fudosan/Takeshiba area pilots, 2020-21) [estimated, from company timeline].
- Strategic investors JR East, Daiwa House, Tokyo Gas, Hankyu Hanshin signal pipeline in stations, buildings, gas metering, and commercial facilities [S3].
- ugo Pro R&D kit: launched 10/2025; buyers not yet disclosed [S2].

## Assessment (analyst view)
*Analyst opinion.* Strengths: proven multi-year paid deployments in the world's most labor-short building-services market; a mature human-in-the-loop operations platform (the hard, unglamorous part of service robotics); distribution and capital locked in via strategic investors who are also customers. Weaknesses: light manipulation payload confines it to "interface actuation" tasks; no disclosed pricing/certifications; hardware is modest versus Chinese wheeled humanoids now entering Japan at aggressive prices. The Pro R&D pivot cleverly reuses its teleop stack for the imitation-learning gold rush, but faces global competition (Trossen, AgiBot, Unitree research SKUs). Threat to an EU entrant: low in Europe (ugo is Japan-only), but in Japan its channel lock-up makes it the partner-or-obstacle for any foreign security/FM robot — a moderate barrier-to-entry threat rather than a product threat.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://ugo.plus/products/ugo-pro/ | full spec set (1800/440/580mm, 54kg, speeds, runtime, sensors, platform) | vendor-claimed |
| 2 | https://ugo.plus/products/ugo-pro-rd/ | R&D kit contents, LeRobot, haptic controller, VLA positioning | vendor-claimed |
| 3 | https://ugo.plus/information/2026/04/15/financing_news/ | Series B3, investors, physical-AI roadmap | vendor-claimed |
| 4 | https://corp.ugo.plus/news/2021/11/15/ | 2021 lineup refresh; ugo Ex ¥98,000/mo anchor | vendor-claimed |
| 5 | https://www.taisei-bm.co.jp/topics/10928/ | Teikyo University deployment 05/2024 | third-party |
| 6 | https://drone-journal.impress.co.jp/docs/news/1186718.html | Yanmar FLYING-Y deployment 11/2024 | third-party |
| 7 | https://www.toyo-tec.co.jp/2025/04/01/6265/ + https://www.taisei-bm.co.jp/topics/koginbill/ | Mainichi Osaka 04/2025, Osaka Kogin 10/2025 deployments | third-party |
