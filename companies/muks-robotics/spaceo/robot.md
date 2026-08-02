# Spaceo M1 & Spaceo Pro — Muks Robotics

> Indian wheeled service/industrial humanoid family from Pune-based Muks Robotics.
> Spaceo M1 is a low-cost social/service android (receptions, airports, retail);
> Spaceo Pro is a heavier industrial variant (palletizing, manufacturing assist).
> Competitively notable mainly for extreme price points ($11k / $60k) rather than
> verified capability — humanoid.guide flags both as "Not Verified".

| Field | Value |
|---|---|
| Company | Muks Robotics |
| HQ | Pune, India |
| Status (2026) | announced / early production ("in production", pre-orders 2025, unverified) |
| First shown / launch | 2025 [S2][S3] |
| Target applications | M1: reception, airports, retail, hospitality, healthcare; Pro: palletizing, AGV guidance, manufacturing assistance |
| Price | M1 from ~USD 11,000; Pro USD 60,000 (third-party) [S2][S3] |
| Availability | India; pre-orders from 2025; "BUY NOW" on vendor site |

## Design & morphology
**Spaceo M1**: 1625×420×390 mm, ~45 kg incl. battery (vendor) — humanoid.guide
instead lists 167 cm / 65 kg. 12 DoF total (5 per arm + 2 base) per vendor; guide
says 16 servo joints. Humanoid torso with two arms and 5-finger cosmetic-looking
hands on a boxy wheeled base (image) [S2][S4].
**Spaceo Pro**: 167 cm / 65 kg; 20 DoF total, 7 per arm; adjustable chassis height
for high racks/bench work; 200 kg payload claim (guide; almost certainly trunk/
push capacity, not manipulation), 10 kg lift per arm [S3].

## Locomotion
Wheeled base; ~2 m/s / 7.2 km/h max (guide) vs 1.5 m/s (vendor, M1) [S2][S3][S4].

## Upper body & manipulation
M1: arm length 600 mm (reach ~650 mm per guide); max arm torque ~160 kg·cm
(≈16 Nm); 10 fingers total [S2][S4]. Pro: 7-DoF arms, dual-encoder servo joints +
harmonic-drive gearboxes, 10 kg per arm [S3]. No force/torque sensing disclosed.

## Sensing
M1: 5 MP RGB camera, Intel RealSense depth, 2D lidar (guide says 3D lidar), 4-mic
array, 7-inch touch display [S2][S4]. Pro: RealSense D435i [S3].

## Actuation & power
Servo-driven joints; aluminium frame. M1 battery: 25.6 V 45 Ah LiFePO4 (~1.15 kWh),
~8 h operation / 72 h standby (vendor) — guide says 4 h [S2][S4]. Pro: 4 h [S3].

## Compute & software
M1 vendor spec: Ryzen 7, 16 GB RAM, 500 GB SSD; optional Jetson AGX Orin (~275
TOPS) or RTX 5070; WiFi 6, BT 5.2, OTA [S4]. Guide lists Intel i5 + NVIDIA GPU for
both models [S2][S3]. Software: Linux + custom OS with FusionMax "Omni-Modal"
vision-audio-language-action model, claimed 2B parameters, on-device [S1].

## Safety & compliance
"Built-in safety systems" (vendor, unspecified). No standards/certifications
claimed [S1].

## Deployment evidence & traction
No named customers, pilots or unit counts found. "In production" is vendor/guide
claimed and unverified.

## Assessment (analyst view)
*Analyst opinion.* Marketing-forward, spec-inconsistent (weight, DoF, speed and
battery figures differ between vendor and guide), with payload claims (60 kg/arm on
the guide's M1 entry, 200 kg on Pro) that are implausible for the stated arm torque
and almost certainly refer to chassis/trunk load. Threat to an EU entrant: low on
capability, but the sub-$15k service-humanoid price anchor matters for hospitality/
reception segments.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.muksrobotics.com/ | product line, FusionMax, applications | vendor-claimed |
| 2 | https://humanoid.guide/product/spaceo-m1/ | M1 specs, $11k price, status | third-party |
| 3 | https://humanoid.guide/product/spaceo-pro/ | Pro specs, $60k price, status | third-party |
| 4 | https://www.muksrobotics.com/spaceo-m1 | M1 vendor spec sheet | vendor-claimed |
