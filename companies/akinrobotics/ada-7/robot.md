# ADA-7 (+ Mini ADA / ADA GH5-GH6 notes) — AKINROBOTICS

> Current flagship of Türkiye's only serial humanoid maker: a wheeled social/service robot with 360°-turning base (0.6 m/s), 4-axis gesturing arms with basic grasping hands, animated LED face, chest touchscreen and a 15-language conversational AI with face/emotion/age/gender analysis. Sold/rented for airports, malls, hotels, fairs and events; siblings Mini ADA (123 cm/45 kg, Istanbul Airport info robot) and legacy ADA GH5/GH6 (2017 factory line) round out the family. Competitively it is a regional reception-class player, not an industrial manipulator.

| Field | Value |
|---|---|
| Company | AKINROBOTICS (AKINSOFT), Konya |
| HQ | Konya, Türkiye |
| Status (2026) | shipping (sales + rental via akinoid.com; low volume) |
| First shown / launch | ADA-7: latest ADA-series generation (early 2020s); series since ADA GH5 (factory line Nov 2017) |
| Target applications | Airports, bus terminals, hotels, malls, stores, education, fairs/events, museum guiding |
| Price | n/a (not publicly listed; sale & rental offered) |
| Availability | Türkiye primarily; export claims unverified; direct sale + rental model |

## Design & morphology
- **ADA-7**: humanoid-styled torso on concealed wheeled base; **high-resolution dynamic LED face** (animated expressions/videos); movable hand joints. Height/weight n/a (not disclosed) [S1].
- **Mini ADA (v3)**: **123 cm, 45 kg**, 10.1" chest touchscreen, 3-axis arms (up/down/side/backward), LED smiley face [S2] (vendor-claimed).
- ADA GH5/GH6: adult-size predecessors from the 2017 Konya line (waitress/promoter styling, tray shelf); specs n/a.

## Locomotion
ADA-7: wheels, **0.6 m/s**, **360° rotation on the spot** [S1]. Mini ADA: ~50 m/min (≈0.83 m/s), 360° rotation, proximity + contact sensors for obstacle detection [S2]. Indoor flat floors.

## Upper body & manipulation
ADA-7: **4-axis arm structure** per arm, "human-like arm movements", **can grasp objects with robotic hands** — light social handover only, no payload rating published [S1] (vendor-claimed). Mini ADA: 3-axis gesture arms, no grasping. No force control, tool interface or manipulation autonomy claimed.

## Sensing
ADA-7: head camera for **face recognition and object detection**; **skeleton tracking; emotion, age and gender analysis**; microphone with speech-to-text [S1]. Mini ADA: stereo-vision camera with depth analysis, text recognition (standard fonts), directional sound filtering, proximity/contact sensors [S2].

## Actuation & power
Mini ADA: lithium-ion battery, **4 h charge → 8 h runtime** [S2] (vendor-claimed). ADA-7 battery n/a. Actuator types n/a (in-house electronics claimed).

## Compute & software
Fully in-house stack (AKINSOFT software heritage): speech-to-text + **AI-generated responses in 15 languages** (ADA-7); Mini ADA 4 languages, barcode/boarding-pass reading and map display for airport wayfinding [S1][S2]. No SDK/third-party ecosystem.

## Safety & compliance
n/a (not disclosed). Low-speed indoor operation; contact/proximity sensors on Mini ADA [S2].

## Deployment evidence & traction
- **Mini ADA at Istanbul Airport** (from 8 August; ongoing per museum/company 2023+ posts): passenger info, voice directions, on-screen routes, flight info via barcode scan, TR/EN [S3] (vendor-claimed, airport-confirmed via IGA social media).
- **Istanbul Robot Museum**: ADA family exhibited and Mini ADA as resident guide; museum is AKINSOFT-run [S4].
- Serial production at Konya factory since 2017 (ADA GH5 line photos show ~15+ units in assembly) [S5]; TV shows, openings, fairs across Türkiye. Unit totals/exports n/a (not disclosed).

## Assessment (analyst view)
*Analyst opinion.* Strengths: real vertical integration on Turkish soil, nine years of serial (if small-batch) production, sticky showcase deployments (national airport, own museum) and national-champion branding. Weaknesses: reception-class capability — 4-axis arms without meaningful payload, no autonomy/manipulation roadmap, opaque pricing and volumes, and marketing-heavy claims ("world's first humanoid factory", "smarter than Sophia") that don't survive scrutiny. Threat to an EU industrial entrant: negligible in industrial use cases; mildly relevant as a local incumbent should an EU vendor target Turkish service/hospitality channels.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://www.akinrobotics.com/en/social-robot-ada-7 | ADA-7: 0.6 m/s, 360°, 4-axis arms, grasping, LED face, 15 languages, analyses (via search snapshot; page blocks fetchers) | vendor-claimed |
| S2 | https://www.istanbulrobotmuzesi.com/en/blog/429/who-is-mini-ada-what-are-the-features-of-mini-ada | Mini ADA: 123 cm/45 kg, 50 m/min, 4h/8h battery, sensors, arms, languages | vendor-claimed |
| S3 | https://www.akinsoft.com/activities/akinsoft-6964 | Istanbul Airport deployment & functions | vendor-claimed |
| S4 | https://www.istanbulrobotmuzesi.com/en/ | Robot Museum context | vendor-claimed |
| S5 | https://www.aa.com.tr/en/science-technology/turkey-opens-its-first-humanoid-robotics-factory-/956696 | 2017 Konya factory, GH5 serial production | third-party |
