# Eggie — Tangible Robots

> Wheeled dual-arm home humanoid from a stealthy Bay-Area startup, revealed November 2025. An "egg-shaped", 160 cm robot with five-finger hands on a wheeled base, built around dexterity, compliance and whole-body control for household chores (spill cleaning, laundry folding, plant watering, fragile-object handling). Competitively a US consumer-side data point: sub-$35k listed price for a manipulation-capable home semi-humanoid.

| Field | Value |
|---|---|
| Company | Tangible Robots |
| HQ | Palo Alto / San Francisco, USA |
| Status (2026) | prototype (not commercially available) [S1] |
| First shown / launch | Emerged from stealth November 2025 [S2] |
| Target applications | Home assistance, exhibitions/customer engagement, research & education, small-object delivery |
| Price | ~USD 32,000 (third-party listing) [S1] |
| Availability | Not commercially available; no ordering channel found |

## Design & morphology
Rounded ("egg-shaped") aesthetic: cream-and-black dual-arm torso on a black column over a squat four-wheel base, boxy camera head on a short neck (verified image). Height 160 cm, weight ~45 kg, 20 DoF overall [S1, third-party]. Torso lift n/a (column appears fixed; possible vertical travel not documented).

## Locomotion
Wheeled base (four small wheels visible; drive type n/a), max speed ~3 km/h [S1]. No stair/terrain capability; indoor domestic focus.

## Upper body & manipulation
Two arms (per-arm DoF n/a) with five-finger hands, 3 DoF per hand — anthropomorphic but low-articulation hands [S1]. Payload ~4 kg [S1]. Demonstrated: folding laundry, cleaning spills, watering plants, grasping mugs and fragile items [S2, third-party video reporting]. Design emphasis on compliant control rather than raw payload. Tool interfaces n/a.

## Sensing
Dual 1080p RGB + depth cameras in head [S1][S2]. Wrist/hand, base sensors, force/tactile n/a (not disclosed).

## Actuation & power
Electric servo motors (listing estimate) [S1, estimated]. Runtime ~7 h per charge [S1]. Battery capacity, charging dock n/a.

## Compute & software
Embedded AI board (Jetson-class, listing estimate); Linux/ROS environment; Wi-Fi/Bluetooth [S1, estimated]. Control approach marketed as whole-body control with compliant manipulation; autonomy vs teleop split in demo videos not verifiable — treat demos as possibly teleoperated (analyst caution). End-to-end latency <200 ms claimed [S1].

## Safety & compliance
"Designed to be safe with humans" (listing) [S1, estimated]. No certifications disclosed.

## Deployment evidence & traction
Demo videos only (household tasks, Nov 2025 reveal). No customers, pilots or pre-orders found.

## Assessment (analyst view)
*Analyst opinion.* Strengths: sensible wheeled-home-form-factor choices, compliance-first control story, low listed price. Weaknesses: anonymous team, no funding disclosure, thin specs from third-party directories, 3-DoF-per-hand limits dexterity claims, and no path to market visible. Threat to a new EU industrial entrant: negligible — different segment (consumer/home) and pre-commercial; worth a periodic check only in case it pivots to services/light-commercial.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/eggie/ | specs (160 cm, 45 kg, 20 DoF, 4 kg, 3 km/h, 7 h), $32k, prototype status, image | third-party |
| 2 | https://lite.duckduckgo.com/lite/?q="Tangible+Robots"+Eggie (aggregated snippets) | Nov 2025 stealth exit, HQ, design pillars, demo tasks, dual 1080p cameras | third-party |
| 3 | https://tangiblerobots.ai/ | company existence, contact | vendor-claimed |
