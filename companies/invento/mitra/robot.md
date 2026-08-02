# Mitra (मित्र) — Invento Robotics

> India's flagship indigenous service semi-humanoid (2017): a 1.5 m, ~50 kg fiberglass wheeled robot with chest touchscreen, face recognition, multilingual speech and gesturing (non-manipulating) arms, deployed in banks, hospitals, malls and airports and immortalized by greeting PM Modi and Ivanka Trump at GES 2017. Competitively it defined the low-cost Indian reception-robot segment; activity has wound down since ~2022 (company at ~3 staff by late 2024), leaving the niche open.

| Field | Value |
|---|---|
| Company | Invento Robotics, Bengaluru |
| HQ | Bengaluru, India |
| Status (2026) | discontinued (residual rentals of existing units; company pivoted to AI training/software) |
| First shown / launch | 2017 (GES Hyderabad debut Nov 2017); Mitra 2 ~2019; Mitra 3 ~2020-21 |
| Target applications | Reception/customer engagement: banks, hotels, malls, cinemas, airports, hospitals, events |
| Price | n/a (not officially disclosed; media reports historically suggested low-lakh INR range, ~USD 10-15K class — estimated) |
| Availability | India; event rental via mitraai.com; new-unit sales effectively ceased |

## Design & morphology
Humanoid-styled shell of **fiberglass**, **~1.5 m tall, ~50 kg**, on a concealed wheeled base; **10-inch chest touchscreen**; molded arms used for greeting gestures — no grasping hands [S2][S6]. DoF counts n/a (not disclosed).

## Locomotion
Wheeled base (layout undisclosed), indoor autonomous navigation using **lidar + ultrasonic sensors** [S2]. Speed n/a.

## Upper body & manipulation
Arms are gestural only (wave/namaste poses); no payload, no end-effectors [S1][S2]. Interaction happens via speech + touchscreen (CRM-integrable: check-in, FAQs, telepresence video calls) [S1].

## Sensing
Camera system for **facial recognition** (claimed to recognize returning customers), microphones/speakers for speech recognition, lidar + ultrasonic for navigation [S1][S2].

## Actuation & power
Rechargeable battery, **8-10 h runtime** claimed [S2][S6] (vendor-claimed via press). Actuator details n/a.

## Compute & software
Proprietary stack: NLP in **English, Hindi and Kannada** (more Indian languages claimed for later versions), contextual dialogue, face recognition, CRM/app integration; COVID-era variants added visitor screening and patient-family telepresence [S1][S2]. No SDK/ecosystem.

## Safety & compliance
n/a (not disclosed).

## Deployment evidence & traction
- **GES 2017 (Hyderabad)**: on-stage greeting of PM Modi and Ivanka Trump — global press moment [S1] (third-party).
- Deployments across banks (HDFC, Canara pilots reported), hotels, malls, cinema halls, airports, weddings/corporate events, 2017-2021 [S1] (third-party; unit counts never disclosed — likely low dozens total, estimated).
- **COVID-19**: Mitra connected ICU patients to relatives at Yatharth Super Speciality Hospital, Noida (2020), widely covered internationally [S1].
- Post-2022: headcount collapse to ~3 (Oct 2024), Tracxn "not active" flag; rentals continue [S3].

## Assessment (analyst view)
*Analyst opinion.* Mitra's strength was cost-engineering and cultural fit (multilingual, made-in-India, national-icon status) — it owned the Indian reception-robot niche with almost no capital. Its weaknesses were structural: no manipulation capability, event-driven demand, ~$1.3M total funding, and no path from greeter to worker. It poses zero competitive threat to an EU industrial entrant, but two lessons transfer: (1) India's services market rewarded local language/price adaptation over hardware sophistication; (2) gesture-only semi-humanoids consistently fail to build recurring revenue — manipulation is the moat.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://en.wikipedia.org/wiki/Mitra_Robot | Identity, GES 2017, deployment sectors, COVID use, Mitra 2/3 existence | third-party |
| S2 | https://mikekalil.com/blog/made-in-india-humanoid-robots/ | 1.5 m/50 kg, 10" touchscreen, EN/HI/KN NLP, 10 h battery, lidar+ultrasonic | third-party |
| S3 | https://tracxn.com/d/companies/mitrarobot/__DuWbb5bDp8FlR-O_FM_1GNW2e1WFe2_3D10puqScPhU | Funding $1.3M, 3 employees Oct 2024, activity decline | third-party |
| S6 | https://inc42.com/features/indian-robot-mitra/ | Fiberglass, Bengaluru assembly, 8-10 h battery, face/speech recognition | third-party |
