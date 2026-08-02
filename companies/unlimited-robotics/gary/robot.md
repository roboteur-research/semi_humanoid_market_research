# Gary — Unlimited Robotics

> Gary is a 1.4 m dual-arm wheeled service robot that has found product-market fit in hospitals: about a dozen units work at Israel's Rabin and Shamir medical centers (Ministry of Health supply agreement) and ~10 more at a Philadelphia hospital, fetching supplies, delivering medication, guiding patients, translating in real time and transcribing consultations into medical records. It matters as one of the few semi-humanoids in daily frontline healthcare operation — proving a ~$30k + subscription model in exactly the labor-shortage niche many entrants target.

| Field | Value |
|---|---|
| Company | Unlimited Robotics |
| HQ | Petah Tikva, Israel |
| Status (2026) | shipping (dozens deployed; healthcare focus) |
| First shown / launch | unveiled Oct 2021 (general-purpose); hospital deployments from ~2023, scaled early 2024 |
| Target applications | hospital logistics & patient services; earlier: hotels, offices, homes |
| Price | ~USD 30,000 + monthly fee (hospital model); 2021 consumer plan was $99 waitlist + monthly subscription |
| Availability | direct/B2B (Israel MoH channel; US pilot); Matrix Software Products marketing partner (IL) |

## Design & morphology
Wheeled humanoid ~140 cm tall with rounded white head (LED bar "face"), chest touchscreen, two arms with parallel-jaw grippers, and a skirted four-wheel base [S4][S6, images]. Weight n/a (not disclosed). Torso lift column per discovery lead (third-party, unconfirmed in current coverage — head/torso fixed in product photos) [S7]. DoF counts n/a (not disclosed).

## Locomotion
Four-wheel base, autonomous indoor navigation in new and known environments; max speed 1.2 m/s [S3][S4]. Hospital corridors/elevator interaction demonstrated (press video coverage) [S1].

## Upper body & manipulation
Two arms marketed at launch as "the first fully autonomous two-armed robot" [S4]; combined payload ~5 kg (discovery lead, third-party) [S7]. End-effectors: two-finger grippers (visible in images); tray/cart carrying for meal and supply delivery; no dexterous hand, no tool changer [S5, images]. Reach/repeatability n/a (not disclosed).

## Sensing
6 cameras and ~20 sensors total (vendor via press): chest RGB-D camera cluster, head sensors, base obstacle sensors; lidar not explicitly documented [S4]. Microphone/speaker stack supports conversation, real-time translation (Hebrew/other), and consultation recording/transcription [S1].

## Actuation & power
Electric actuators (details n/a). Battery capacity/runtime n/a; self-charging implied for "24/7" operation claims [S1, vendor-claimed].

## Compute & software
Ra-Ya platform: open, Python-based SDK/app framework — "any Python developer can program it easily", free beta, app-store model; built on ROS underneath (estimated; not explicitly documented) [S3][S4]. Healthcare apps: delivery workflows, wayfinding, translation, transcription into medical files, cognitive engagement activities for elderly patients [S1][S5]. Fleet/teleop details n/a.

## Safety & compliance
No published certifications (ISO 13482 etc. n/a). Operates among patients/staff in hospitals under staff supervision; obstacle avoidance via camera/sensor suite [S1, estimated].

## Deployment evidence & traction
- Rabin Medical Center + Shamir Medical Center: ~a dozen Garys in daily work since early 2024 (third-party, All Israel News/Israel21c) [S1][S2].
- Israel Ministry of Health agreement to supply public hospitals (third-party) [S1].
- Philadelphia hospital: ~10 units since July 2024 (hospital unnamed in coverage; Jefferson link unconfirmed) [S2].
- Earlier: 10 units total in 2022 with a 500-unit production goal that wasn't met (third-party) [S4].
- Funding: $5M seed May 2024 (lool ventures, Wix/Fiverr founder angels), ~$8M total [S5].

## Assessment (analyst view)
*Analyst opinion.* Strengths: real, referenceable daily hospital operation on two continents, a government supply channel, healthcare-specific software (translation/transcription) that generates value beyond logistics, and a genuinely developer-friendly SDK. Weaknesses: modest manipulation (5 kg combined, simple grippers), thin capitalization (~$8M) versus the capital intensity of healthcare scaling, undisclosed reliability/uptime data, and specs opacity. Threat to a new EU entrant: moderate in EU hospital-logistics tenders if it internationalizes, but its main significance is as validation that mid-spec dual-arm robots at ~$30k+subscription can win healthcare contracts today — speed to workflow integration beats raw hardware specs.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://allisraelnews.com/gary-the-versatile-robot-revolutionizing-patient-care-in-israeli-hospitals | dozen units, Rabin/Shamir, MoH deal, tasks (Aug 2024) | third-party |
| 2 | https://israel21c.org/the-versatile-hospital-worker-that-never-calls-in-sick/ | Philadelphia 10 units Jul 2024, task list | third-party |
| 3 | https://www.jpost.com/israel-news/meet-gary-the-personal-israeli-robot-assistant-for-your-home-or-office-679453 | 2021 unveiling, 1.2 m/s, $99 waitlist, subscription | third-party |
| 4 | https://nocamels.com/2022/12/meet-gary-the-robot-that-does-the-stuff-you-dont-want-to/ | 140 cm, 6 cameras/20 sensors, Ra-Ya Python, dual-arm claim, 500 goal | third-party |
| 5 | https://www.calcalistech.com/ctechnews/article/bjlpqgber | funding, founders, hospital duties | third-party |
| 6 | https://unlimited-robotics.com | product imagery, positioning | vendor-claimed |
| 7 | _work/discovery_row.md lead | 5 kg combined payload, lift column | third-party (unconfirmed) |
