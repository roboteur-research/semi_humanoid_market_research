# ARMAR-7 — KIT H2T (with ARMAR-6 and ARMAR-III lineage)

> ARMAR-7 is the seventh generation of KIT's ARMAR humanoid family (since 1998): a wheeled, dual-arm household/care assistance robot unveiled at Automatica 2025. It learns tasks from human demonstration, understands speech and gestures, and performs chores (dishwasher unloading, laundry sorting) autonomously. Competitively it matters as the German academic benchmark for semi-humanoid eldercare robotics and as a talent/technology source, not as a product.

| Field | Value |
|---|---|
| Company | KIT — H2T lab (Institute for Anthropomatics and Robotics) |
| HQ | Karlsruhe, Germany |
| Status (2026) | research (active; shown Automatica 2025, Hannover Messe 2026) |
| First shown / launch | Automatica, June 2025 [S1][S3] |
| Target applications | Household assistance, eldercare/nursing facilities, learning from demonstration research |
| Price | n/a (not for sale) |
| Availability | Not available; university research platform |

## Design & morphology
Anthropomorphic upper body (head, torso, two arms, five-finger hands) on a holonomic mobile platform with three omni-wheels. A 2-DoF knee/hip kinematic lets the robot bow forward and adjust torso height (reaching floor to overhead). ~32 actuated DoF total, EtherCAT-networked [S1][S2]. Height/weight not published (n/a, not disclosed).

Lineage context — **ARMAR-6** (2018, SecondHands/Ocado): 152-192 cm via 40 cm telescopic torso lift, 160 kg (without batteries), footprint 60x80 cm, four Mecanum wheels, two 8-DoF torque-controlled arms with 10 kg payload each, underactuated 5-finger hands (10 kg hook-grasp holding force), 2-DoF neck, two stereo camera systems + RGB-D head, 6-axis F/T sensors in both wrists, 1 m/s, NiMH 48 V 38 Ah (1.824 kWh) battery, four onboard PCs + GTX 1080 GPU, Ubuntu + ArmarX [S4][S5]. **ARMAR-III** (2006): the wheeled "kitchen humanoid" with dual 7-DoF arms and pneumatic hands; loaded dishwashers, still functional after 19 years [S6].

## Locomotion
ARMAR-7: holonomic omnidirectional platform, three omni-wheels [S1]. Speed not published; ARMAR-6 reference: 1 m/s [S4]. Indoor flat-floor use.

## Upper body & manipulation
Two anthropomorphic 8-DoF torque-controlled arms (as in ARMAR-6, which achieved 10 kg per arm — ARMAR-7 payload not separately published) [S1][S4]. Hands: 4-DoF underactuated humanoid five-finger hands with integrated RGB cameras in the hand (in-hand vision for grasping) [S1, vendor-claimed]. Torso height adjustment + bowing via knee/hip joints extends the vertical workspace. ARMAR-6 demonstrated bimanual power-tool use (drill handover/use), ladder-support and overhead maintenance assistance [S3][S5]. No tool changer / media at flange (n/a).

## Sensing
3-DoF head with multiple integrated camera systems (stereo + depth); joint torque sensors in all arm joints; 6-axis force/torque sensors in wrists; absolute encoders; in-hand RGB cameras [S1][S2]. Microphones for speech interaction (speech-based command interface demonstrated at Automatica 2025) [S3].

## Actuation & power
Custom sensor-actuator-controller (SAC) units: integrated BLDC motor + reduction gear + sensing + electronics per joint (design established with ARMAR-6) [S4][S5]. Battery-powered autonomous operation; ARMAR-7 battery details n/a; ARMAR-6: 48 V NiMH 1.824 kWh [S4].

## Compute & software
ArmarX — H2T's open-source cognitive robot software architecture (memory-centric, skill-based) runs the whole family; ARMAR-6 carried four onboard PCs incl. one GPU (GTX 1080) vision PC and a real-time EtherCAT master [S4][S2]. AI features: learning new tasks from single human demonstrations, speech/gesture understanding, autonomous task execution with stated attention to on-device privacy of sensitive data [S1][S3, vendor-claimed]. No commercial SDK/fleet layer (research).

## Safety & compliance
No certifications (research platform). Torque-controlled compliant arms and force-controlled interaction modes provide intrinsic safety for human-robot collaboration experiments [S4, vendor-claimed]. n/a for ISO 13482/10218.

## Deployment evidence & traction
No deployments/customers (research). Traction evidence: EU H2020 SecondHands project — Ocado co-developed ARMAR-6 as a warehouse maintenance assistant, with live demos of proactive tool handover and physical assistance (2018-2020) [S3][S5]; ARMAR-III's multi-year kitchen demos; ARMAR-7 public demos at Automatica 2025 and Hannover Messe 2026 (dishwasher unloading, laundry sorting, learning-from-demonstration) [S1][S3]. Extensive publication record.

## Assessment (analyst view)
(Analyst opinion.) Strengths: 27-year continuous humanoid lineage; credible bimanual manipulation and human-robot physical collaboration demos; eldercare focus matches exactly the German market need; open ArmarX stack. Weaknesses: one-off hardware, no manufacturing/product path, unpublished specs for the newest generation; academic pace. Threat to a new EU entrant: none commercially; moderate reputationally (sets expectations for what a "care humanoid" should do). High partnering value: learning-from-demonstration IP, Karlsruhe talent, and the SecondHands template for industry co-funding.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://h2t.iar.kit.edu/397.php | ARMAR-7 hardware: 3 omni-wheels, 8-DoF arms, 4-DoF hands w/ RGB cameras, 3-DoF head, 2-DoF knee/hip, 32 DoF, EtherCAT, ArmarX, privacy | vendor-claimed |
| 2 | https://www.originofbots.com/robot/armar-7-by-karlsruhe-institute-of-technology-kit-details-specifications-rating | ARMAR-7 spec summary (32 DoF, torque sensors, wrist F/T) | third-party (low authority) |
| 3 | https://www.messe.tv/en/2025/automatica/kit-armar-7-robot-recognizes-speech-and-helps-in-everyday-life | Automatica 2025 demo: speech, learning from demonstration, eldercare framing | third-party |
| 4 | https://h2t.iar.kit.edu/pdf/Asfour2018a.pdf | ARMAR-6 specs: 152-192 cm, 160 kg, 60x80 cm, 1 m/s, 10 kg/arm, 40 cm torso travel, 1824 Wh NiMH, 4 PCs + GTX1080 | vendor-claimed (peer-reviewed) |
| 5 | https://spectrum.ieee.org/kit-armar6-humanoid | ARMAR-6 configuration, SecondHands/Ocado role | third-party |
| 6 | https://www.100objekte.kit.edu/en/object/082 | ARMAR-III 2006 kitchen robot, still functional 19 years on | vendor-claimed |
