# Ginger (XR-1 / Cloud Ginger 1.0 / Cloud Ginger 2.0) — CloudMinds / Dataa Robotics (达闼)

> Ginger was the first mass-produced compliant wheeled semi-humanoid: a 1.58-1.6 m humanoid torso with 34 in-house SCA smart compliant actuators on a three-wheeled self-balancing omni base, driven by the HARIX cloud brain. Shipping since ~2019 into reception, education, healthcare and exhibition roles (JD.com listing ¥698k), it proved the category years before the current wave — and its maker's 2024 collapse makes it the market's most instructive failure. Treated here as one dossier covering XR-1 (research/1.0) and Cloud Ginger 2.0.

| Field | Value |
|---|---|
| Company | CloudMinds / Dataa Robotics (达闼) |
| HQ | Shanghai, China |
| Status (2026) | discontinued (de facto — company dormant since late 2024; site still lists product) |
| First shown / launch | XR-1 unveiled 2019 (MWC); Cloud Ginger 1.0 commercial ~2020; Ginger 2.0 2021-22 |
| Target applications | Reception/greeting, education, eldercare/healthcare, exhibition guiding, COVID field-hospital service, tele-operated patrol |
| Price | ¥698,000 (JD.com listing, Cloud Ginger) [third-party] |
| Availability | Formerly direct + leasing in China and via partners; effectively unavailable since company standstill (09/2024) |

## Design & morphology
Humanoid torso, head and two arms with five-finger hands on a skirt-covered wheeled base; 1,600 mm tall, 65 kg with battery [S1, third-party spec DB]. 34 DoF total from 34 SCA integrated joints across neck, shoulders, elbows, wrists, hands, waist, knees and chassis [S1][S2, vendor-claimed]. Marketing emphasized 柔美 ("supple/graceful") compliant motion — every joint force-controlled.

## Locomotion
Three-wheeled omnidirectional chassis with active self-balancing; max 3.65 km/h (~1 m/s); 30 mm step tolerance; ±15° slope [S1, vendor/third-party]. Indoor use.

## Upper body & manipulation
Two ~7-DoF compliant arms with multi-DoF five-finger hands; payload light (single-digit kg class, exact figure n/a — not disclosed); designed for social gestures, object handover, tray carrying, sign-language and dance demos rather than industrial manipulation. Visual grasping algorithms via cloud [S1][S2]. Repeatability n/a.

## Sensing
Multiple 2D/3D cameras, lidar, ultrasonic sensors, IMU, joint force sensors (SCAs are torque-sensing), microphone arrays [S1]. SLAM/VSLAM navigation.

## Actuation & power
34 × SCA (Smart Compliant Actuator) — CloudMinds' in-house integrated servo joints (motor + driver + encoder + compliance control), commercialized separately via INNFOS/Mintasca [S2, vendor-claimed]. Battery: 8 h runtime [S1]; capacity n/a.

## Compute & software
Onboard processors paired with the HARIX (海睿) cloud brain: real-time multimodal deep learning, NLP multi-round dialogue, cloud multi-robot scheduling, and human-in-the-loop teleoperation ("cloud avatar") over 4G/5G VPN [S1][S2, vendor-claimed]. Closed source; robot largely dependent on CloudMinds cloud services — a key obsolescence risk now the company is dormant [analyst note].

## Safety & compliance
Compliant actuation marketed as inherently human-safe; no ISO 13482/CE certifications publicly documented (n/a, not disclosed).

## Deployment evidence & traction
Real deployments 2019-2023: COVID-19 Wuhan/Shanghai field hospitals (delivery, disinfection, entertainment), telecom flagship stores, schools/vocational training platforms, exhibition centers and government showcases; Ginger was the face of China's "cloud robotics" push and appeared at MWC/WAIC repeatedly [third-party]. Unit volumes never disclosed; JD listing at ¥698k signals low-volume flagship pricing. All momentum ended with the 2024 collapse: wage stoppages from early 2024, company standstill from 09/2024, ¥35.3M court-ordered debts by 03/2025; 2025 rescue attempts (Tianjin Jinnan agreement, HK "Boy Robotics" JV with Guohua Group) have not visibly revived the product [S3][S4][S5, third-party].

## Assessment (analyst view)
*Analyst opinion.* Ginger's strengths were genuinely ahead of their time: full-body compliant actuation from an in-house actuator line, a cloud teleop/autonomy hybrid, and real (if subsidized) deployments. Its failure is the category's clearest warning: a ¥698k social-service robot without a measurable labor-replacement ROI cannot sustain a unicorn burn rate, and cloud-dependency means dead company = dead fleet. For an EU entrant the direct threat is zero, but two legacies matter: cheap SCA-style integrated joints (now an open Chinese supply chain) and buyer skepticism in hospitality/eldercare channels burned by CloudMinds-era promises.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.aparobot.com/robots/cloud-ginger-xr-1 | Full spec set: 1600mm, 65kg, 34 SCA, 3.65 km/h, 8h, sensors, HARIX features | third-party (spec DB) |
| 2 | https://www.dataarobotics.com/zh/product-44 | Vendor product page: 34 DoF, 30+ SCA, HARIX OS, Ginger 1.0/2.0 lineup, Mintasca SCA link | vendor-claimed |
| 3 | https://www.recodechinaai.com/p/chinas-robotics-industry-is-booming | Collapse timeline, funding, valuations, HK JV | third-party |
| 4 | https://finance.sina.com.cn/jjxw/2025-04-01/doc-inerrnxw0465673.shtml | Lawsuits, wage arrears, standstill | third-party |
| 5 | https://www.smzdm.com/p/91235603/ | JD.com listing ¥698,000 | third-party |
