# FlashBot Arm — Pudu Robotics

> FlashBot Arm is a "semi-humanoid embodied AI service robot": Pudu's proven FlashBot multi-floor hotel-delivery base fitted with dual 7-DoF liftable arms and PUDU DH11 dexterous hands. Announced 31 March 2025 (after a CES 2025 showing), it targets hotels, offices, restaurants, retail and healthcare — closing the last-metre gap (pressing elevator buttons, opening doors, handing items to guests) that pure delivery robots cannot. Competitively it is arguably Pudu's stronger semi-humanoid play than the D7: it inherits a field-proven base platform plus Pudu's existing elevator/door/IoT integrations and worldwide hospitality channel.

| Field | Value |
|---|---|
| Company | Pudu Robotics (普渡科技) |
| HQ | Shenzhen, China |
| Status (2026) | shipping (pilot/pre-order production ramp) [third-party] [S4] |
| First shown / launch | CES Jan 2025 (concept), official unveiling 2025-03-31 [S2] |
| Target applications | Hotels, office buildings, restaurants, retail, healthcare — delivery + light manipulation + guest interaction [S1][S2] |
| Price | ~USD 34,000 [third-party, S4]; not officially published (base FlashBot ~$28k [S5]) |
| Availability | Via Pudu global dealer network (RobotLAB etc.); FlashBot Arm listed but "pricing/availability pending" at some dealers [S5] |

## Design & morphology
Cylindrical FlashBot delivery-robot body (539 × 515 mm footprint, 1440 mm tall, ~70 kg) with a sensor head, 10.1-inch touch screen, enclosed delivery compartment, and two shoulder-mounted 7-DoF arms that can be *lifted* (arm-base elevation) to expand the workspace to 1600 × 2000 × 1600 mm — about 2 m operating diameter/reach height [S1, vendor-claimed; weight/height cross-checked third-party S4]. Total payload 15 kg [S1]. DoF: 14 in the arms plus 2 × 11-DoF hands (6 active + 5 passive each) [S1].

## Locomotion
Wheeled base (differential drive, as on FlashBot); max speed ~4.5 km/h [S4, third-party]; minimum passable path width 65 cm [S1]. Autonomous elevator riding via IoT elevator integration *or* physically pressing buttons with its hand [S2]. Indoor, flat-floor use only; no stated climbing capability (n/a, not disclosed).

## Upper body & manipulation
Two 7-DoF arms with height-adjustable mounting; combined reach envelope up to 2 m [S1][S2]. End-effectors: PUDU DH11 self-developed dexterous hands, 11 DoF each (6 active + 5 passive), five fingers, used for pressing buttons, grasping bottles/items, carrying trays, handing objects to people [S1][S2]. Per-arm payload not separately disclosed (total 15 kg). Repeatability n/a (not disclosed). No tool changer / media at flange (n/a).

## Sensing
RGBD cameras, LiDAR, panoramic cameras and pressure-sensitive skin; VSLAM + laser SLAM with 3D mapping and omnidirectional obstacle perception [S1][S2, vendor-claimed]. Hand/wrist force-torque sensing not explicitly disclosed (pressure-sensitive skin is claimed on body/arms).

## Actuation & power
Actuator type n/a (not disclosed). Runtime 8 h (no load), charge time 4 h, automatic self-recharging on dock [S1, vendor-claimed]. Battery capacity n/a (not disclosed).

## Compute & software
Onboard compute not disclosed. Pudu software stack: PUDU cloud fleet platform, multimodal AI interaction (voice, facial expressions, gestures), building/elevator IoT integration inherited from FlashBot line; embodied-AI development by Pudu X-Lab [S2, vendor-claimed]. No open SDK advertised for this product (n/a).

## Safety & compliance
No specific standards cited for FlashBot Arm (n/a, not disclosed). Marketing claims safe operation alongside humans (obstacle avoidance, pressure-sensitive skin) [S1][S4, vendor-claimed]. Base FlashBot line carries CE for EU distribution [estimated from Pudu's EU sales presence].

## Deployment evidence & traction
Announced with pilot/pre-order intent March 2025; humanoid.guide lists it "in production" at ~$34k [S4, third-party]. Distributed through Pudu's established dealer network (e.g. RobotLAB in the US offers turnkey FlashBot deployments incl. elevator/door integration; FlashBot Arm listed with pricing pending) [S5]. No named FlashBot Arm hotel customers publicly confirmed yet [as of 08/2026]; the underlying FlashBot base has substantial multi-floor hotel deployments worldwide [vendor-claimed]. Confidence: pilots likely, mass deployment unproven.

## Assessment (analyst view)
*Analyst opinion.* Strengths: cheapest credible path to "delivery + manipulation" in hospitality — a proven base, existing elevator/door integrations, a global sales/service channel of 80k+ installed robots, and an aggressive (~$34k) price point that undercuts nearly every dual-arm competitor. The liftable-arm + dexterous-hand combination is well matched to its narrow task set (buttons, handovers, trays). Weaknesses: 15 kg total payload and hotel-centric design limit industrial relevance; manipulation autonomy beyond scripted tasks is unproven; compute/SDK openness undisclosed. Threat to a new EU entrant: high in hospitality/facility services — Pudu can push this through existing EU hotel accounts faster than any startup — but low in industrial/logistics niches.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.pudurobotics.com/en/products/flashbot-arm | Dimensions 539×515×1440mm, 15kg payload, 7-DoF arms, DH11 6+5 DoF, workspace 1600×2000×1600mm, VSLAM+lidar, 65cm path, 8h/4h charge, 10.1" screen | vendor-claimed |
| 2 | https://www.prnewswire.com/news-releases/pudu-robotics-unveils-flashbot-arm-a-semi-humanoid-embodied-ai-service-robot-for-commercial-applications-302415118.html | Announcement 2025-03-31, positioning, target markets, elevator-button autonomy | vendor-claimed (PR) |
| 3 | https://newatlas.com/robotics/pudu-robotics-flashbot-arm-semi-humanoid-delivery-robot/ | Independent coverage, hotel bellhop framing | third-party |
| 4 | https://humanoid.guide/product/flashbot-arm/ | 70kg weight, 144cm, 4.5 km/h, ~$34,000, "in production" | third-party |
| 5 | https://www.robotlab.com/store/pudu-flashbot/ | Dealer channel, base FlashBot $28k, FlashBot Arm pricing pending | third-party (dealer) |
