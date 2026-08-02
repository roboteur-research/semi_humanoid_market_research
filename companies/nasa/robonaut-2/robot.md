# Robonaut 2 (R2) — NASA JSC + General Motors

> Robonaut 2 is NASA/GM's dexterous humanoid torso — 42 DoF including two 12-DoF tendon-driven hands — that flew on the ISS 2011-2018 as the first humanoid robot in space. Its mobility was modular: a fixed ISS stanchion, the wheeled Centaur 2 rover base on Earth, and (troubled) climbing legs from 2014. Retired and now in the Smithsonian, it remains the historical benchmark for human-tool-compatible dexterity in a semi-humanoid.

| Field | Value |
|---|---|
| Company | NASA Johnson Space Center + General Motors |
| HQ | Houston, TX, USA |
| Status (2026) | discontinued (returned from ISS May 2018; never re-flew; museum display since 2024) |
| First shown / launch | unveiled Feb 2010; launched to ISS on STS-133, Feb 2011; first powered ops Aug 2011 |
| Target applications | ISS intravehicular maintenance/task-board work; GM: dexterous manufacturing tech transfer |
| Price | n/a (government program; not for sale) |
| Availability | n/a — one flight unit + ground units; never commercialized |

## Design & morphology
Human-scale torso: head, 3-DoF neck, 1-DoF waist, two 7-DoF arms and two 12-DoF hands — 42 DoF total; weight ~150 kg (330 lb; some sources 140 kg) [S1][S2]. Gold/white "helmet" head contains vision; backpack houses power conversion. Mobility modular by design: ISS pedestal/stanchion, Centaur 2 four-wheel rover base for planetary-analog work (Desert RATS 2010), and a 2014 leg kit — two 7-DoF climbing legs with gripping end-effectors for ISS handrails [S2][S4].

## Locomotion
Baseline: none (mounted torso). Centaur 2 variant: 4-wheel omnidirectional rover base (Earth demos). Leg kit (2014): zero-g climbing, not walking; integration + power problems left R2 mostly disabled 2015-18 (root cause: missing return wire in computer-chassis power supply, found only after return to Earth) [S4][S5].

## Upper body & manipulation
Arms: 7 DoF each, ~9 kg payload per arm/hand system [S2][S3]. Hands: 12 DoF each with 2-DoF wrist; four fingers + opposable thumb, tendon-driven with series-elastic finger actuation, designed explicitly to use unmodified astronaut EVA/IVA tools (drills, task boards, switches, soft goods) [S3]. Grasp strength ~2.3 kg per hand grip (est.). This hand remains a reference design; GM derived RoboGlove from it [S6].

## Sensing
~350 sensors total: head cameras (stereo + IR), hand/finger position and force sensing via tendon tension, joint torque sensing throughout, tactile load cells [S2][S3].

## Actuation & power
Brushless DC motors with harmonic drives (arms/neck/waist); tendon-driven series-elastic fingers; ISS 120V power (no battery in baseline; battery backpack developed for legged ops) [S2][S3].

## Compute & software
38 PowerPC processors onboard [S2]; supervised autonomy with ground/crew tasking plus full teleoperation (VR glove/helmet); NASA open-sourced the R2 simulator and r2_description URDF for ROS [S2]. Safety-rated force limits for operation beside crew inside the ISS — an early "certified to work around humans" milestone in practice, though not to terrestrial standards.

## Safety & compliance
Human-rated for ISS interior operations per NASA flight-safety review (impact-limited, compliant joints, crew-supervised) — the space-station equivalent of collaborative certification; no terrestrial ISO/UL certifications (n/a) [S1][S2].

## Deployment evidence & traction
Single ISS deployment 2011-2018: task-board experiments, switch/valve operation, handrail-climbing prep; first human-humanoid handshake in space (2012) [S1][S2]. Ground fleet: several units at JSC/GM including Centaur 2 configuration [S2]. Retired; displayed at Smithsonian NASM from Oct 2024 [S4]. Technology descendants: RoboGlove (Bioservo licence 2016), Valkyrie biped, Persona AI (Nic Radford) [S6].

## Assessment (analyst view)
*Analyst opinion.* R2 proved 15 years ago that human-tool-level hand dexterity is achievable — at government cost and near-zero duty cycle. Its lessons for commercial semi-humanoids: modular mobility bases on a common torso is a sound architecture; extreme-DoF hands drive cost, mass and reliability problems (R2 spent more ISS years broken than working); and single-wire-level faults can idle a flagship for years without field-serviceability. No competitive threat; relevant to an EU entrant mainly as the dexterity benchmark investors cite and as the origin of US talent networks (Radford/Persona).

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.nasa.gov/robonaut2/ | mission timeline, first humanoid in space | vendor-claimed (NASA) |
| 2 | https://robotsguide.com/robots/robonaut | specs, 42 DoF, compute, Centaur 2, history | third-party (IEEE) |
| 3 | https://ntrs.nasa.gov/api/citations/20110023122/downloads/20110023122.pdf | hand design: 12 DoF, tendon-driven, 9 kg payload, tool use | vendor-claimed (NASA paper) |
| 4 | https://www.airandspace.si.edu/air-and-space-quarterly/issue-14/nasa-robonaut | leg problems, missing-wire root cause, 2018 return, NASM display | third-party (Smithsonian) |
| 5 | https://spectrum.ieee.org/nasas-robonaut-to-return-to-iss-with-legs-attached | leg kit plans and issues | third-party |
| 6 | https://www.nasa.gov/general/roboglove/ | GM RoboGlove derivation, Bioservo | vendor-claimed (NASA) |
