# L1 — Moon Dynamics (攬月動力)

> L1 is a wheeled-bipedal hybrid humanoid for heavy industrial carrying: 165 cm, ~60 kg, two self-balancing powered wheel-legs with large off-road tires, dual arms with 2-finger claws and a 25 kg lift capability at ~$60k. **SCOPE NOTE — BORDERLINE:** this is a wheel-LEG robot (dynamic balancing legs ending in wheels), not a statically stable wheeled-chassis semi-humanoid; it is included as a boundary datapoint (cf. Hexagon AEON, GAC GoMate). Its pitch: legged terrain tolerance and small footprint with wheeled efficiency for warehouse/factory transport.

| Field | Value |
|---|---|
| Company | Moon Dynamics (攬月動力) |
| HQ | Shenzhen, China |
| Status (2026) | shipping claimed ("in production" per DB — unverified) [third-party] |
| First shown / launch | surfaced 2025-26 [estimated] |
| Target applications | Repetitive lifting/moving in warehouses, factories, industrial parks; heavy-load logistics |
| Price | ~$60,000 [third-party, unverified] |
| Availability | Inquiry-based [third-party] |

## Design & morphology
165 cm tall, ~60 kg, aluminum-alloy construction; 18 DoF overall (DB also lists "12 in hands" — inconsistent with 2-finger claws; treat DoF split as unreliable) [S1, third-party]. Humanoid torso and arms on two articulated wheel-legs with large knobby tires (self-balancing) [S1, product imagery].

## Locomotion
Two-wheel dynamic balancing wheel-leg base; max 7 km/h; climbs slopes and crosses small obstacles; demonstrated carrying 20 kg uphill with smooth disturbance rejection; millisecond-level control latency claimed [S1][S2, third-party/vendor-claimed].

## Upper body & manipulation
Dual arms with 2-finger gripping claws; 25 kg lifting strength (system); reach up to ~1.8 m under load (high-reach clamping demos, water-tank transport) [S1][S2]. Per-arm payload/repeatability n/a.

## Sensing
n/a (not disclosed); cameras implied by autonomy claims [estimated]. Head module houses sensor visor [product imagery].

## Actuation & power
Actuators n/a (high-torque hub/joint motors implied by balancing + 25 kg lift [estimated]). Runtime ~3 h per charge [S1]. Battery capacity n/a.

## Compute & software
n/a (not disclosed); "quick learning from minimal training data" claimed [S1, vendor-claimed via DB]. No SDK/ROS information public.

## Safety & compliance
Claimed safe operation alongside human workers [S1, vendor-claimed]. No certifications published. Note: a dynamically balancing 60 kg robot carrying 25 kg raises fall-consequence questions no public material addresses [analyst note].

## Deployment evidence & traction
Demo videos (LinkedIn/social): 20 kg uphill carries, water-tank transport, high-reach clamping [S2, third-party]. No named customers, pilots or unit counts. "In production" status is database-listed, unverified [S1].

## Assessment (analyst view)
*Analyst opinion.* Strengths: highest lift-to-price ratio in this batch (25 kg / $60k), terrain-tolerant wheel-leg base, focused industrial-carrying use case. Weaknesses: near-total corporate opacity (no site, founders, funding), simplistic 2-finger end-effectors, 3 h runtime, and unaddressed safety implications of dynamic balancing under load; verification of production claims impossible. Threat to an EU entrant: low direct threat given opacity, but the price/capability point is a leading indicator — if wheel-leg carriers at $60k mature, they will squeeze wheeled semi-humanoids out of gross-payload logistics tasks, pushing EU entrants toward dexterity- and compliance-led differentiation.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/l1/ | Core specs: 165cm/60kg, 18 DoF, 25kg lift, 7 km/h, 3h, $60k, production status, applications | third-party (DB, unverified) |
| 2 | DuckDuckGo/LinkedIn snippets ("Moon Dynamics" L1) | 20kg uphill demo, ~1.8m reach under load, industrial demos | third-party |
| 3 | _work/discovery_startups.md entry 13 | Discovery classification: wheel-leg BORDERLINE, ~$60k | third-party (compiled) |
