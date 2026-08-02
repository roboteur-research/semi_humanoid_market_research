# Pepper (ペッパー) — SoftBank Robotics / Aldebaran

> Pepper is the wheeled, 121cm "emotional" humanoid unveiled by SoftBank in 2014 — the first mass-produced semi-humanoid and still the category's largest install base (~27,000 produced, ~17,000 sold). Aimed at retail greeting, reception and education rather than manipulation, it defined both the promise (instant brand recognition, huge distribution) and the failure mode (subscription churn, thin utility) of interaction-first semi-humanoids. Production stopped in 2021, its European maker Aldebaran was liquidated in 2025, yet SoftBank Robotics Japan relaunched it as the LLM-powered "Pepper+" rental in February 2026.

| Field | Value |
|---|---|
| Company | SoftBank Robotics (Japan); originally Aldebaran/SoftBank Robotics Europe; manufactured by Foxconn |
| HQ | Tokyo, Japan (Aldebaran: Paris, liquidated 2025) |
| Status (2026) | discontinued (production halted 06/2021); B2B/consumer rental of existing fleet continues in Japan incl. "Pepper+" relaunch 02/2026 |
| First shown / launch | Unveiled 5 June 2014; consumer sales June 2015 (first 1,000 units sold in 60 seconds) [S1] |
| Target applications | Retail greeting/promotion, reception, care-home recreation, education/STEM, events |
| Price | 2015 JP: ¥198,000 + 36-mo subscriptions ≈ ¥1.08M 3-yr total; Pepper for Biz ~$440-550/mo; 2026 Pepper+: ¥79,800/mo (retail, 1-yr) / ¥39,800/mo (care) / ¥150,000 one-off month [S1][S2][S6] |
| Availability | Japan only (rental-only, 3-4 week lead); no new production; RobotLAB (US) services legacy fleet |

## Design & morphology
Wheeled tri-omni base with a fixed (non-lifting) torso, articulated arms and 5-finger cosmetic hands. Height 1,210mm, width 485mm, depth 425mm, weight 28kg [S1, vendor-claimed]. 20 DoF (motors) total across head (2), shoulders/elbows/wrists (2×5), hands (2×1), hip (2), knee (1), base (3) [S1]. A 10.1-inch touch tablet is fixed on the chest — Pepper's primary UI and a design element widely copied by Chinese service humanoids.

## Locomotion
Three omnidirectional wheels, max 3 km/h, obstacle/step tolerance ~1.5cm [S1, vendor-claimed]. Indoor flat-floor only; no dock — manual cable charging (unit can operate while plugged).

## Upper body & manipulation
Two 5-DoF arms + 1-DoF hands, reach ~560-620mm (estimated), payload effectively negligible (~0.1-0.3kg, estimated) — the hands are expressive, not functional grippers. No tool flange, no media at flange. Pepper performs gestures, handshakes and object-pointing; it was never a manipulation platform, a core reason its utility plateaued at "greeter".

## Sensing
Head: 4 directional microphones, 2 HD cameras (forehead + mouth), 1 3-D depth sensor (behind the eyes) [S1]. Touch sensors in head and both hands; torso gyroscope. Base: 2 sonar, 6 laser line sensors, 3 bumper sensors, gyro [S1]. No lidar. Emotion recognition ran in SoftBank's cloud "emotion engine" (voice tone + expression analysis).

## Actuation & power
Brushed DC servomotors (20), position-controlled, no force/torque sensing (vendor-claimed via spec sheets). Battery: lithium-ion 30.0Ah / 795Wh; runtime ~12h in shop use — best-in-class endurance that even 2025-era semi-humanoids rarely match [S1, vendor-claimed].

## Compute & software
Intel Atom-class embedded PC in the head running NAOqi OS (Aldebaran's robot framework, shared with NAO); Wi-Fi 802.11 a/b/g/n + Ethernet [S1]. SDKs: Choregraphe visual programming, Python/C++ NAOqi APIs, Android app layer for the tablet (2016+). Cloud dependence proved fatal for the consumer fleet: units not migrated to the new cloud by 28 Feb 2025 became unusable ("機体交換が必要" — device replacement required) [S5]. Pepper+ (02/2026) adds a generative-AI customer-service agent that recognizes clothing/expressions via a new head 2D camera + 3D sensor package and an upgraded chest tablet, reproducing "professional sales demonstrator" talk tracks [S6][S7].

## Safety & compliance
CE-marked for EU sale (vendor-claimed); designed inherently low-risk (28kg, 3km/h, no payload). Bumpers + sonar for collision avoidance. No ISO 13482 certification publicly documented — n/a (not disclosed).

## Deployment evidence & traction
- ~27,000 units manufactured by June 2021; ~17,000 sold; NAO ~20,000; 70 countries [S1][S2, third-party].
- 12,000 sold in Europe alone by May 2018 [S1].
- Notable sites: all Hamazushi restaurant branches, Japanese bank receptions, Pepper PARLOR café Tokyo (12 units, 12/2019), Prague and Montréal-Trudeau airports, Fukuoka SoftBank Hawks robot cheerleading squad (07/2020), thousands of Japanese homes (2017), CARESSES EU-Japan eldercare research [S1].
- Pepper for Biz subscription ≈ $440-550/month; first-renewal rate reportedly only ~15% (2015 cohort) [S2, third-party].
- 2026: Pepper+ rental relaunch (retail/care plans) and Pepper for Home 2.0 (¥43,780/mo) / Education (¥39,800/mo) rentals continue in Japan [S4][S6].
- Guinness World Record: certified first mass-produced humanoid robot [S7, third-party].

## Assessment (analyst view)
*Analyst opinion.* Pepper proved distribution and brand can put five-figure unit counts of semi-humanoids into the field — a scale no competitor has repeated — but also that interaction-only robots without manipulation utility cannot sustain ~$5k/yr subscriptions: churn (~15% renewal), a thin app ecosystem, and cloud lock-in killed the economics, and the hardware margin never existed (SoftBank reportedly sold below cost). Its ghost still shapes the market: Japanese buyers benchmark rental pricing against Pepper (¥40-80k/mo), and the 2025 liquidation shows how fast an install base strands when cloud services die. For an EU entrant the lessons are direct: sell measurable labor substitution (arms that work), keep autonomy on-device, and treat Pepper's surviving Japan fleet plus Maxvision's revived NAO/Pepper IP as low-threat legacy competition — the real heirs to Pepper's niche are Chinese wheeled greeters (Cruzr S2, Pudu D7) at lower price points.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://en.wikipedia.org/wiki/Pepper_(robot) | specs (120-121cm, 28kg, 20 DoF, sensors, 795Wh/12h, 3km/h), timeline, 27k produced, deployments | third-party |
| 2 | https://www.therobotreport.com/aldebaran-pepper-nao-robots-receivership/ | ~17k sold, pricing ($30k US / $2k+$550/mo), 15% renewal, insolvency | third-party |
| 3 | https://www.therobotreport.com/maxvision-buys-core-robot-assets-including-nao-pepper-aldebaran/ | Maxvision IP purchase 07/2025 | third-party |
| 4 | https://www.softbankrobotics.com/jp/product/pepper/ | current rental-only model lineup and prices (Home 2.0 ¥43,780/mo, Education ¥39,800/mo) | vendor-claimed |
| 5 | https://jp.softbankrobotics.com/support/pepper/biz/news_contents/ (2025 notices) | 2025-02-28 cloud migration deadline / consumer service end | vendor-claimed |
| 6 | https://www.softbankrobotics.com/jp/product/pepper-plus/ | Pepper+ features and plan pricing (¥79,800/mo retail, ¥39,800/mo care, ¥150,000 short-term) | vendor-claimed |
| 7 | https://gigazine.net/news/20260203-pepper-plus-softbankrobotics/ | Pepper+ launch 2026-02-02, new sensors/tablet, Guinness note | third-party |
| 8 | ROOT/_work/market_context.md §4.1/§7 | ¥198,000 + 36-mo ≈ ¥1.08M; Pepper for Biz $440/mo; install-base ranking | estimated (synthesis) |
