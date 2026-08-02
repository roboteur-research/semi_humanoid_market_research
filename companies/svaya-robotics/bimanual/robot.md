# Bimanual — Svaya Robotics

> An industrial dual-arm semi-humanoid built from Svaya's own cobot technology: two high-precision **6-DoF SR-series arms** (10 kg payload each) on a humanoid torso with sensor head — **155 cm, 70 kg**, joint-level force sensing, EtherCAT industrial backbone, no-code programming and digital-twin tooling, at roughly **$90K**. Sold as a stationary platform (mountable on mobile bases per company positioning) for hazardous industrial work (welding, forging, foundry), R&D and education; early production / limited release. Competitively: the first credible "made-in-India" industrial dual-arm torso, priced well under Western equivalents.

| Field | Value |
|---|---|
| Company | Svaya Robotics, Hyderabad |
| HQ | Hyderabad, India |
| Status (2026) | announced/early production — limited release |
| First shown / launch | ~2025 (LinkedIn/marketing push 2025; 2026 site refresh) |
| Target applications | Hazardous industrial tasks (welding, forging, foundry), industrial R&D, education, defense |
| Price | ~USD 90,000 (third-party listing) |
| Availability | India, direct; limited production |

## Design & morphology
Humanoid torso + sensor head on box pedestal; **155 cm tall, 70 kg** [S1] (third-party). **12 arm DoF total (2 × 6-DoF)**; renders also show articulated 3-finger hands and a 2-DoF-look neck — total DoF n/a. Standard mounting is **stationary pedestal**; company/discovery positioning notes mountability on third-party mobile bases (option, not a shipped mobile product) [S1][S2].

## Locomotion
None as sold (stationary; max speed 0) [S1]. Mobile-base integration left to customer/integrator.

## Upper body & manipulation
- Two **high-precision 6-DoF industrial arms** (SR-L series derivation), **10 kg payload per arm** [S1] (third-party). No 7th redundancy axis — elbow-posture flexibility is limited vs 7-DoF rivals.
- End-effectors: **2-finger gripper claws** per humanoid.guide listing [S1]; 2026 site renders show articulated **3-finger hands** — gripper options appear configurable [S2]. Modular wrist highlighted by vendor [S2].
- **Built-in force sensing** at joints for compliant contact tasks [S1][S3].

## Sensing
Head sensor module (cameras; details n/a); joint torque/force sensing; teleoperation with **150-250 ms glass-to-action latency** claimed (remote operation capability) [S1]. IP67 dust/fluid protection claimed for arm hardware [S3].

## Actuation & power
Electric servo joints from Svaya's cobot line (details n/a); mains-powered stationary platform (battery n/a).

## Compute & software
**EtherCAT backbone**; Ethernet, Modbus TCP, Profinet fieldbus connectivity [S1]; no-code programming interface, AI/digital-twin tooling, "software-defined robot" architecture [S2][S3]. SDK details n/a.

## Safety & compliance
Collaborative-robot heritage (force-limited joints); no ISO 10218/TS 15066 certification publicly documented for the bimanual configuration (n/a).

## Deployment evidence & traction
- **Early production / limited release** [S1] (third-party). No named customers or unit counts for the Bimanual.
- Company references: DRDO-funded quadruped + exoskeleton demonstrators (2022-23) [S4]; SR-L cobots marketed as India's first indigenous collaborative robots. Bimanual demo content on LinkedIn/YouTube (engine-assembly line renders/videos) [S2].

## Assessment (analyst view)
*Analyst opinion.* Strengths: real vertical integration (own arms/controllers), industrial fieldbus-first design that drops into factory networks, defense R&D pedigree, and an aggressive ~$90K price for a dual-arm force-sensing torso. Weaknesses: 6-DoF arms and simple grippers cap dexterity; stationary-only as shipped; traction and funding undisclosed; branding ("Bimanual") and materials still research-flavored. Threat to a new EU entrant: low in Europe today, moderate in price-sensitive export markets — an Indian vendor selling force-controlled dual-arm cells at half Western prices could pressure the entry tier, especially in welding/foundry niches EU vendors deprioritize.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://humanoid.guide/product/bimanual/ | 2×6-DoF, 155 cm/70 kg, 10 kg/arm, $90K, EtherCAT/fieldbus, 150-250 ms teleop latency, stationary, status | third-party |
| S2 | https://svayarobotics.com/product/ | Renders (3-finger hands, modular wrist), no-code/digital-twin positioning | vendor-claimed |
| S3 | https://blog.althumans.com/svaya-robotics/ | IP67, force-controllable arms, welding/forging/foundry/defense applications | third-party |
| S4 | https://www.indiablooms.com/health-details/S/12469/hyderabad-s-svaya-robotics-develops-quadruped-robot-and-exoskeleton-for-defence-sector.html | DRDO quadruped/exoskeleton credibility context | third-party |
