# KR1 / Kinisi 01 — Kinisi Robotics

> Low-cost dual-arm wheeled humanoid ("Physical AI platform") for warehouse
> logistics: pick-and-place, tote handling, sorting, palletizing. Notable for an
> aggressive ~$75k price point, edge-only AI, and a 2026 exit into Bear Robotics'
> fleet — a direct low-price competitor archetype for any EU semi-humanoid entrant.

| Field | Value |
|---|---|
| Company | Kinisi Robotics |
| HQ | New York, USA + Bristol, UK |
| Status (2026) | prototype (pre-series; being absorbed into Bear Robotics fleet) |
| First shown / launch | 2024-2025; won Automate Start-up Challenge May 2025 [S1] |
| Target applications | warehouse pick-and-place, totes, sorting, replenishment, palletizing, inspection |
| Price | USD 75,000 (third-party, humanoid.guide) [S1] |
| Availability | not generally available; pilot/prototype stage, future channel via Bear Robotics |

Naming note: the vendor's current site markets the platform as **"Kinisi 01"**;
"KR1" is the original platform name and the vendor uses both interchangeably
("KR1, our Physical AI platform") [S3]. Treated as one dossier.

## Design & morphology
Dual-arm humanoid torso with articulated spine/waist on a compact round wheeled
base (image shows Ranger/tri-lobe-style omni base). Height 162 cm, weight 100 kg,
21 DoF total (2 in hands) [S1]. IP65 rated [S1].

## Locomotion
Omnidirectional zero-turn base with active suspension/damping; top speed 2.4 m/s
(vendor: adaptive speed control in confined spaces; humanoid.guide lists 14.4 km/h
≈ 4 m/s — discrepancy, vendor figure preferred) [S1][S3].

## Upper body & manipulation
Two arms built from compact strain-wave ("wave gear") actuator modules with
integrated encoders. Payload: 10 kg per humanoid.guide [S1]; vendor claims 25 kg
dynamic / 40 kg static for Kinisi 01 [S3] (likely total/system figures). Modular
gripper with quick-swap interface, vacuum end-effector option [S3]. Reach n/a.

## Sensing
Head sensor pod with stereo depth cameras; 180° lidar array for SLAM; vendor claims
depth accuracy ±2 mm @ 2 m [S3]. Sub-100 ms perception-to-action latency [S1].

## Actuation & power
BLDC motors with strain-wave gears [S1]. Hot-swappable 48 V / 20 Ah Li-ion pack
(~1 kWh); 6-8 h runtime typical industrial duty; 80% charge in 90 min [S3].

## Compute & software
NVIDIA Jetson onboard, Linux; edge-deployed "real-time transformer inference" for
navigation and manipulation — explicitly no cloud dependency for autonomy [S1][S3].
Modes: autonomous / semi-autonomous / teleop ("Shadow Play"). Fleet telemetry +
OTA via "Kinisi Mission Control" [S3]. Wi-Fi connectivity.

## Safety & compliance
Dual safety controllers with watchdogs, HW/SW e-stop, automatic deceleration and
posture lock on critical alerts [S3]. No ISO/CE certifications claimed. IP65 [S1].

## Deployment evidence & traction
No named customers or unit counts disclosed. Traction signals: Automate Start-up
Challenge win (May 2025), ~$2M funding [S1], and the Bear Robotics acquisition
(2026) which is expected to bring KR1 into Bear's deployed service-robot fleet
[S2][S3]. Confidence: vendor-claimed except award (third-party).

## Assessment (analyst view)
*Analyst opinion.* Strengths: very low target price (~$75k), pragmatic wheeled
morphology, hot-swap battery, credible founder, and now a scaled parent (Bear
Robotics) for manufacturing/distribution. Weaknesses: prototype maturity, thin
public spec sheet with internally inconsistent numbers, no certifications, 2-DoF
hands limit dexterity. Threat to a new EU entrant: moderate-to-high on price and
channel if Bear executes; low near-term in EU industrial settings lacking CE/ISO
safety evidence.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/kinisi-kr1/ | dimensions, DoF, speed, price, IP65, funding, award | third-party |
| 2 | https://kinisi.com/ | positioning, applications, Bear Robotics deal | vendor-claimed |
| 3 | https://kinisi.com/kinisi-01/ | Kinisi 01 specs (speed, payload, battery, sensors, safety) | vendor-claimed |
