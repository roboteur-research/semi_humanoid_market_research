# XMAN-R1 — Keenon Robotics (擎朗智能)

> The XMAN-R1 is Keenon's wheeled "embodied service robot" (人形具身服务机器人): a 174 cm, 36-DoF humanoid torso with dual 7-DoF arms and 6-DoF dexterous hands on a two-wheel-module chassis, designed to fill defined service "job positions" (barista, greeter, laundry hand) while orchestrating Keenon's delivery/cleaning fleet around it. It matters because it is the semi-humanoid spearhead of the world's #1 service-robot company (IDC 22.7% share) and already works in a revenue hotel (Shangri-La Traders, Shanghai Hongqiao, since 10/2025).

| Field | Value |
|---|---|
| Company | Keenon Robotics (擎朗智能) |
| HQ | Shanghai, China |
| Status (2026) | shipping (commercial deployment since 10/2025; pilots and event operations through 2026) |
| First shown / launch | Announced 2025-03-31 (robot "birthday" on official spec poster) [S1][S2] |
| Target applications | Hotels & restaurants: greeting, beverage/coffee prep, tray placement, laundry folding, luggage assistance — in collaboration with Keenon T/S/C-series robots [S2][S4] |
| Price | ~$100,000 [third-party, S5] |
| Availability | China first; global rollout leveraging Keenon distributor network; purchase/RaaS mix typical of Keenon [estimated] |

## Design & morphology
Official spec poster [S1]: height 174 cm, weight 110 kg; human-proportioned silver/black body with face screen. 36 DoF whole body: 2× 7-DoF arms, 6-DoF waist/leg linkage (forward/reverse flexing for large fore-aft and lateral motion "without tipping"), 2-DoF head, 2-DoF wheeled chassis, 2× 6-DoF dexterous five-finger hands. (Aggregator humanoid.guide lists 172 cm — official poster says 174 cm.)

## Locomotion
Wheeled drive (2-DoF chassis; two wheel modules visible, kneeling-leg linkage above) [S1]. Max speed ~2.9 km/h (0.8 m/s) per third-party listing [S5]. Indoor use; navigation stack inherited from Keenon's 100k-robot delivery fleet ("industry-leading navigation/planning") [S2, vendor-claimed].

## Upper body & manipulation
Dual 7-DoF "high-bionic" arms + 2× 6-DoF anthropomorphic dexterous hands (10 fingers) [S1, vendor-claimed]. Demonstrated: pouring/mixing drinks, coffee workflow (grind-to-serve), placing trays, folding towels/laundry, handing items to delivery robots [S2][S4, third-party]. Payload: ~3 kg lifting per third-party listing [S5]; official figure n/a. Repeatability n/a.

## Sensing
Official poster [S1]: 2× lidar (front + rear chassis), 4× depth vision cameras (motion planning + environment), 4× HD wide-angle cameras (360° coverage). Launch coverage cites "11 multimodal sensors" + proprietary real-time 3D reconstruction [S2, vendor-claimed]. Omnidirectional HD microphone array, dual-channel speakers, HD flexible curved face screen [S1].

## Actuation & power
High-precision electric motors [S5, third-party]; actuator details n/a. Battery: ~3 h runtime per charge (third-party) [S5]; official capacity n/a (not disclosed).

## Compute & software
275 TOPS onboard AI compute, 64 GB VRAM + 64 GB storage [S1, vendor-claimed]. VLA large-model-driven skills with deep reinforcement learning ("fast iteration, strong robustness"); LLM conversation + facial-expression feedback; proprietary low-latency communication protocol building a robot "private network"; VR dual-arm teleoperation for multimodal data collection; open "hardware + software" ecosystem for custom skill expansion; multi-robot scheduling system coordinating XMAN with T10/T9 delivery, S100 heavy-load, C30/C40 cleaning robots [S1][S2, vendor-claimed].

## Safety & compliance
No certifications published [flag]. Vendor: 360° high-precision perception with real-time spatial reconstruction and collision avoidance for dense human environments; safety-first design pillar [S2, vendor-claimed]. Wheeled statically-stable base; 110 kg mass at walking-pace speeds [estimated].

## Deployment evidence & traction
- Shangri-La Traders Hotel, Shanghai Hongqiao Airport: commercial deployment announced 2025-10-31 — billed as world's first "general-purpose + special-purpose" collaborative hotel robot model; XMAN-R1 greets guests while C40, S100, T10, T3 and W3 robots handle cleaning/transport [S4, third-party].
- WAIC 2026 (Shanghai, 07/2026): "invited barista" running full coffee workflow at NOWWA Coffee (挪瓦咖啡) booth — first global humanoid-x-coffee-chain collaboration (NOWWA: 10,000+ stores); also hotel laundry folding demo with DINERBOT T9 transporting [S6, third-party].
- Restaurant closed-loop demo (order→prep→delivery→clearing) with T10 handoff at launch 03/2025 [S2].
- Fleet-data advantage: 100k+ robots in 60+ countries feed training data [S2, vendor-claimed].

## XMAN-F1 (bipedal sibling — context, out of semi-humanoid scope)
Unveiled at WAIC 2025 (poster "birthday" 2025-07-23; public premiere 2025-07-26): full biped, 175 cm / 68 kg, 43 DoF (2×7-DoF arms, 2×6-DoF legs, 3-DoF waist, 2-DoF head, 2×6-DoF hands), 3D lidar + 4 depth + 4 wide-angle cameras, same 275 TOPS/64 GB compute and VLA stack; marketed as Keenon's "first commercial embodied service robot" for F&B/reception (beverage prep, presentations) [S3, vendor-claimed]. Note: some discovery notes listed F1 as wheeled — the official spec poster confirms it is bipedal; the wheeled semi-humanoid in the XMAN line is the R1.

## Assessment (analyst view)
*Analyst opinion.* Keenon's edge is not the robot but the system: XMAN-R1 slots into an existing global service-robot fleet, scheduler, sales channel and support network, and it is already producing drinks in real venues — deployment maturity most humanoid startups lack. Hardware specs are mid-pack (3 h runtime, ~3 kg lift, 0.8 m/s), clearly tuned for front-of-house service rather than industrial work. Threat to an EU entrant: very high in European hospitality — Keenon has EU distribution and reference chains (Shangri-La, NOWWA) and can bundle the humanoid with proven delivery/cleaning robots at fleet pricing; low threat in industrial/logistics semi-humanoid segments.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://www.keenon.com/en/product/XMAN-R1 (official spec poster, saved as images/xman-r1-hero.png) | 174cm/110kg, 36 DoF breakdown, sensors (2 lidar, 4 depth, 4 wide-angle), 275 TOPS/64GB, VR teleop, comms, launch date 2025-03-31 | vendor-claimed |
| S2 | https://www.ithome.com/0/841/931.htm + https://news.qq.com/rain/a/20250331A0777500 | Launch, 11 multimodal sensors, job-position concept, restaurant/hotel loops, fleet-data advantage | third-party |
| S3 | https://www.keenon.com/en/product/XMAN-F1 (official spec poster, saved as images/xman-f1-hero.png) | XMAN-F1: biped, 175cm/68kg, 43 DoF, WAIC 2025 | vendor-claimed |
| S4 | Travel Daily News Asia / Webull / Boutique Hotel News (via search) | Shangri-La Traders Hongqiao deployment 2025-10-31, multi-robot model | third-party |
| S5 | https://humanoid.guide/product/keenon-xman-r1/ | ~$100k price, 2.9 km/h, 3h runtime, 3kg lift | third-party |
| S6 | CN press via search (WAIC 2026 NOWWA coverage) | NOWWA barista + hotel laundry demos, first coffee-chain collab | third-party |
