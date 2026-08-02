# Mobile AI — Trossen Robotics

> Mobile AI is Trossen's bimanual wheeled data-collection and robot-learning platform: two 6-DoF WidowX AI follower arms (plus two matching leader arms for puppeteering teleoperation) and three RealSense D405 cameras on the company's SLATE differential-drive UGV. It is the commercial successor to Stanford's hugely influential Mobile ALOHA rig, sold at $22,995 (summer-2026 sale; list $33,695.95) with 2-3-week lead times. It is not a service robot — it is the cheapest credible way to collect bimanual mobile-manipulation data and train/evaluate VLA and imitation-learning policies (ACT, π0, OCTO, LeRobot), which makes it the price floor and the talent-pipeline machine of the semi-humanoid research segment.

| Field | Value |
|---|---|
| Company | Trossen Robotics |
| HQ | Downers Grove, IL, USA |
| Status (2026) | shipping |
| First shown / launch | Trossen AI line announced Jan 2025, available late Q1 2025 (lineage: Mobile ALOHA kit 2024) [S4] |
| Target applications | Embodied-AI research: bimanual teleoperation, imitation-learning data collection, VLA model training/evaluation |
| Price | $22,995 (sale, without laptop; list $33,695.95); $27,145 with high-performance laptop (list $37,845.95) [S2] |
| Availability | Direct e-commerce, worldwide; production 2-3 weeks; lifetime support; EU resellers (Generation Robots) [S2][S5] |

## Design & morphology
Open-frame "camera-tower" architecture rather than humanoid styling: a black extruded frame on the white SLATE base carries two follower arms at roughly counter height, two leader arms above for human puppeteering, a center camera mast and a 10" touchscreen [S2] (see images). SLATE base footprint 500 x 500 mm, height 222 mm, base weight 40 kg, base payload rating 70 kg [S3]. Total system height/weight not published; no torso lift or head DoF.

## Locomotion
SLATE UGV: differential drive, 2x 350 W hub motors, max speed 1.0 m/s (3.6 km/h), auto-charging dock capability, indoor flat-floor use [S3]. During data collection the base is typically driven/dragged by the teleoperator (Mobile ALOHA-style); autonomous navigation workflows optional [S2].

## Upper body & manipulation
Follower arms: 2x WidowX AI, 6 DoF each, 1.5 kg payload at full extension, 700 mm reach (1,400 mm bimanual span), 1 mm repeatability/accuracy, ~6 kg per arm, precision parallel grippers; leader arms carry ambidextrous pincher handles for kinesthetic teleop [S5]. Actuation: Trossen "Next-Gen QDD" hybrid-drive servos with in-house iNerve controller, multiphase PID at 10,000 Hz+, 500 Hz position feedback, <2 ms latency [S1][S5]. Optional TRumi gripper ($949.95 list). No dexterous hand, no force/torque sensor at the wrist disclosed.

## Sensing
3x Intel RealSense D405 close-range RGB-D cameras (two wrist-mounted on followers, one central overview) [S2]; leader-arm joint encoders provide demonstration data. Base sensors: none itemized for the standard kit (lidar optional via SLATE ecosystem, estimated).

## Actuation & power
Base battery 24 V 18 Ah (~0.43 kWh) lithium, hot-swap not stated, auto-charging dock supported [S3]. Arm power from base battery; runtime not published (n/a).

## Compute & software
Sold without compute or with a high-performance ML laptop; companion TOTL workstation (Intel Core Ultra 9 + NVIDIA RTX 5090) offered for training [S1][S2]. Stack: C++ Interbotix UDP driver with Python and ROS 2 bindings; Hugging Face LeRobot integration; data pipelines to HDF5/Parquet with GUI setup; sim support MuJoCo, Gazebo, NVIDIA Isaac; compatible policies/models: ALOHA/ACT, BiACT, OCTO, π0 (Physical Intelligence), ALOHA Unleashed, Crossformers [S1][S2]. Openness (docs, drivers, URDFs public) is a core selling point.

## Safety & compliance
Research equipment; no ISO 10218/TS 15066 or ISO 13482 claims. Low arm payloads and teleop-first operation are the implicit safety model (estimated). Lifetime support warranty covers materials/workmanship [S2].

## Deployment evidence & traction
- Direct successor to Stanford Mobile ALOHA (Fu, Zhao, Finn 2024) — one of the most-cited low-cost robot-learning platforms; Trossen built/sold the official ALOHA, ALOHA 2 and Mobile ALOHA kits used across academia and industry labs [S4][S6].
- ALOHA-class hardware underpins work at Google DeepMind (ALOHA Unleashed) and is a reference rig in the Physical Intelligence π0 / LeRobot ecosystem; Trossen markets dataset-visual-consistency (same table as π0/Gemini training data) as a feature [S1][S2][S6].
- Unit counts not disclosed; "one of the most widely used low-cost robotic training platforms in research" (vendor framing, plausible given citation footprint) [S6].

## Assessment (analyst view)
*Analyst opinion.* Strengths: unbeatable price point for bimanual mobile manipulation (~1/4 of a Vega), the ALOHA brand halo, deep integration with the winning open-source ML stack (LeRobot), and a 20-year-old company with real support infrastructure — this owns the entry tier of the research market. Weaknesses: it is a data-collection rig, not a robot product — 1.5 kg payload, no autonomy suite, no safety story, open-frame hardware with no path to commercial service deployment. Threat to a new EU entrant: indirect but strategic — it anchors researcher price expectations near $25k and standardizes data formats/models an EU platform must interoperate with; any EU research-platform play (a la Reachy) must beat or join the LeRobot/ALOHA ecosystem rather than fight it. Low threat in commercial service segments.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.trossenrobotics.com/aloha | Trossen AI line-up, QDD servos, iNerve, 10 kHz protocol, model/software compatibility, sale pricing incl. Mobile AI $22,995 | vendor-claimed |
| 2 | https://www.trossenrobotics.com/mobile-ai | Mobile AI configuration (2x leader-follower WidowX AI pairs, 3x D405, 10" touchscreen), $22,995/$27,145 pricing, SLATE compatibility, 2-3 wk lead time, software list, warranty | vendor-claimed |
| 3 | https://docs.trossenrobotics.com/slate_docs/specifications.html | SLATE base: 500x500x222 mm, 40 kg, 70 kg payload, 1.0 m/s, 24 V 18 Ah, diff drive, 2x350 W hub motors | vendor-claimed (documentation) |
| 4 | https://fox4kc.com/business/press-releases/ein-presswire/788100763/ + https://mobile-aloha.github.io/ | Jan 2025 launch/Q1 2025 availability; Stanford Mobile ALOHA lineage (Fu/Zhao/Finn) | vendor press release / academic |
| 5 | https://docs.trossenrobotics.com/trossen_arm/main/specifications/wxai.html + https://www.generationrobots.com/en/404333-widowx-ai.html | WidowX AI: 6 DoF, 1.5 kg at full extension, 700 mm reach, 1400 mm span, 1 mm repeatability, 6 kg, 500 Hz feedback, <2 ms latency, $4,545.95 list | vendor-claimed / third-party reseller |
| 6 | https://www.trossenrobotics.com/the-aloha-project | ALOHA/ALOHA 2/Mobile/Unleashed whitepaper lineage, Stanford/Berkeley/DeepMind partnerships, "most widely used" claim | vendor-claimed |

*Unknowns: system weight/height, runtime, unit counts. Note: discovery file's "Stationary AI ~$8-17k" is off — Stationary AI lists at $23,995.95 ($15,995 on sale); the $8-17k band fits Solo AI configurations.*
