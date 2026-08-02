# Alfie — Prosper Robotics

> Alfie is a wheeled, dual-arm home "robot butler" from London startup Prosper Robotics, designed around VR teleoperation by paid remote assistants rather than full autonomy, with a planned toolbox of 50–100 swappable attachments instead of dexterous hands. At a target of ~$5–15k plus a ~$500/month service subscription it is the cheapest serious semi-humanoid concept in Europe — competitively significant as a price-anchor and teleop-model experiment, though still pre-launch and prototype-only.

| Field | Value |
|---|---|
| Company | Prosper Robotics Ltd |
| HQ | London, UK |
| Status (2026) | prototype (testing in employee homes; no public sales yet) |
| First shown / launch | Prototype publicized 2023; repeated launch slippage; London pilots planned |
| Target applications | Household chores: dishwasher loading, laundry sorting/folding, surface & floor cleaning, tidying, simple meal prep |
| Price | Target from ~$5,000 hardware (earlier £5-10k / $10-15k range cited) + ~$500/month subscription (maintenance, insurance, teleoperation) [S1][S4] |
| Availability | Not yet purchasable; alpha pilots limited to London homes without kids/pets/stairs [S4] |

## Design & morphology
Wheeled base (founder explicitly rejects bipeds for home balance/safety), vertical body with two articulated arms that translate up and down the body column for different working heights [S1]. Height/weight/DoF not published (n/a).

## Locomotion
Indoor wheeled drive (type not disclosed); flat single-floor homes only — pilot criterion "no stairs" [S1][S4].

## Upper body & manipulation
Two arms with interchangeable end effectors: planned toolbox of **50–100 task attachments** (mops, suction cups, specialized grippers) and multiple "glove" sets to avoid cross-contamination between e.g. bathroom and kitchen tasks [S1]. Payload/reach n/a. Demonstrated (prototype/teleop): dishwasher loading, laundry sorting, wiping, salad prep, bed straightening [S1][S3].

## Sensing
Cameras for teleoperation view (operator sees via VR; privacy filter blurs faces and text on screen) [S1][S2]. Detailed sensor suite n/a.

## Actuation & power
n/a (not disclosed).

## Compute & software
Teleop-first stack: remote human assistants (planned: Philippines) control Alfie via VR interface; ~20% task autonomy at launch, autonomy share intended to grow from teleop data [S2][S3]. Privacy-preserving operator interface (face/text blurring) [S2]. No public SDK.

## Safety & compliance
No certifications published. Safety case rests on slow, light home tasks and human-in-the-loop; pilot exclusion of children/pets acknowledges risk immaturity [S4].

## Deployment evidence & traction
- Prototypes operating in Prosper employees' homes (2024-25 reporting) [S4].
- No paying customers, no public unit counts; launch not yet occurred as of mid-2026 (est./absence of announcements).
- Coverage in Sifted, MIT Technology Review (teleop economy context), Stacey on IoT [S1][S2][S4].

## Assessment (analyst view)
*Analyst opinion.* Strengths: radical cost target, pragmatic tool-changer approach (avoids the dexterous-hand problem), clear-eyed teleop labor arbitrage model, and a founder funding it patiently without VC deadlines. Weaknesses: sub-10-person team against a hardware-manufacturing problem; years of schedule slip; privacy and labor-ethics questions around offshore operators in the home; and no visible path to safety certification. Threat to a new EU entrant: negligible in B2B; in consumer, Alfie's $5k+subscription framing could shape buyer expectations — but Prosper's chief value to the ecosystem is proving (or disproving) the home-teleop model before better-funded players copy it.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://sifted.eu/articles/robot-butler-openai-prosper-robotics | Wheeled design, arm column, 50-100 tools, gloves, pricing, timeline, team | third-party |
| 2 | https://www.technologyreview.com/2024/12/23/1108466/general-purpose-robots-humanoids-ai-remote-assistants/ | Philippines teleoperators, remote-assistant economy | third-party |
| 3 | https://en.futuroprossimo.it/2024/12/robot-assistenti-ci-fideremo-mai-di-loro/ | ~20% autonomy at launch, teleop share | third-party |
| 4 | https://staceyoniot.com/privacy-and-ai-in-the-coming-age-of-home-robots/ | $5,000 + $500/mo, employee-home tests, pilot criteria (no kids/pets/stairs) | third-party |
