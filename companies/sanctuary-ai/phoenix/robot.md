# Phoenix (Generation 8) — Sanctuary AI

> Phoenix is Sanctuary AI's general-purpose humanoid, now in its 8th generation (Dec 2024): a human-scale torso with the industry's most dexterous hydraulic hands (21 DoF each), mounted on a small wheeled base after Sanctuary concluded legs were "too frail to support a strong torso". It is not a product for sale but a teleoperation-first data-capture and pilot platform feeding the Carbon AI control system — and since 2026 the hardware has become secondary to Sanctuary's pivot toward selling Physical AI software into industrial automation. Competitively it matters as the dexterity benchmark and as evidence that a top-funded humanoid firm chose wheels over legs.

| Field | Value |
|---|---|
| Company | Sanctuary AI |
| HQ | Vancouver, BC, Canada |
| Status (2026) | prototype (pilot deployments; not for general sale) |
| First shown / launch | Phoenix line unveiled May 2023 (Gen 6); Gen 7 April 2024; Gen 8 (wheeled) December 2024 |
| Target applications | Automotive manufacturing (Magna plants), retail back-of-store, logistics; primarily human-behaviour data capture for AI training |
| Price | n/a (not disclosed; not for open sale) |
| Availability | Pilot/partner deployments only (Canada/US); RaaS-style engagements with strategic partners |

## Design & morphology
Human-scale upper body: 170 cm height, ~70 kg (third-party figures for Gen 7 era) [S3]. Gen 7 (April 2024) still had legs; Gen 8 (Dec 2024) replaced them with a compact wheeled base after customer feedback that bipedal legs were "too frail to support a strong torso" — trading locomotion generality for uptime, stability, lower BoM cost and faster manufacturing/commissioning [S1][S2]. Full-body DoF count not disclosed for Gen 8; the defining subsystem is the pair of 21-DoF hydraulic hands (four fingers + opposable thumb, human-like dimensions) [S4]. Vendor image filenames from the Gen 8 announcement still carry "gen_7" labels; Sanctuary itself mostly says "new generation" rather than "Generation 8" — generation numbering is press/analyst usage (noted ambiguity).

## Locomotion
Small wheeled mobile base (drive type not disclosed; appears non-balancing, low platform). No stair/terrain capability claimed. Speed n/a (not disclosed). Legged locomotion abandoned for this generation; Sanctuary has not published a legged roadmap since [S1].

## Upper body & manipulation
Two human-proportioned arms (DoF per arm not disclosed; Gen 7 improved wrist/hand/elbow range of motion) [S2]. Hands: 21 DoF each, hydraulically actuated via proprietary miniaturized hydraulic valves — Sanctuary's core IP; capable of in-hand manipulation (zero-shot RL policies demonstrated Dec 2024), tool use (wrench, connector plugging) [S4][S6]. Payload figures not disclosed for Gen 8. Hydraulics chosen for power density and speed at human-hand scale; Gen 7 "further miniaturized hydraulics, reducing weight, power consumption and complexity" [S2].

## Sensing
Gen 8 upgraded depth + RGB cameras (wider FoV, higher resolution) and audio/video systems for telepresence-quality data capture [S1]. Tactile: fingertip sensors detecting forces down to ~5 mN (vendor claim); new touch sensors integrated Feb 2025 [S4][S6]. Base sensing not disclosed.

## Actuation & power
Hybrid actuation: hydraulic hands/wrists (proprietary micro-valves), electric elsewhere (details not disclosed). Battery capacity/runtime n/a (not disclosed). Gen 8 emphasis on "increased uptime" for data-capture shifts [S1][S2].

## Compute & software
Carbon AI control system: cognitive architecture + teleoperation pipeline; Phoenix is explicitly optimized as a data-capture device for training foundation models on human behaviour [S1]. Training stack uses NVIDIA Isaac Lab for sim-to-real RL on the hydraulic hands (March 2025) [S6]; Microsoft collaboration for AI models/cloud [S1]. Autonomy today: teleop + task-specific automated policies; Magna trials reported new tasks automated in <24 h from captured data [S5]. No public SDK; closed platform.

## Safety & compliance
"Increased hardware and software measures that exceed specified safety standards" (Gen 7, vendor wording); no specific ISO/CE certifications published [S2]. n/a (not disclosed) otherwise.

## Deployment evidence & traction
- Gen 5 commercial deployment January 2023 (retail back-of-store pilot, Canada) [S2] (third-party).
- Magna: strategic relationship announced Oct 2024 (deployments in Magna manufacturing, potential contract manufacturing of Phoenix, second Magna investment) [S5] (third-party). Trials at Magna plants late 2025: material handling, sub-assembly, sorting/packing; new assembly tasks mastered in <24 h [S5] (third-party, vendor-sourced claims).
- June 17 2026: "world-class performance" on automated wire/connector-plugging production task with a Tier 1 automotive supplier — presented as proof of the new industrial Physical-AI strategy rather than a humanoid sale [S6] (vendor-claimed).
- No unit counts ever disclosed; no open-market sales.

## Assessment (analyst view)
*Analyst opinion.* Strengths: the 21-DoF hydraulic hand remains the world benchmark for robot dexterity, and the teleop-first data pipeline plus Magna's automotive channel are genuinely valuable assets. Weaknesses: eight hardware generations without a sellable product, severe leadership churn (both founders gone, three CEO changes in two years, layoffs), modest funding (~$140M) versus US/Chinese rivals, and a 2026 pivot that de-emphasizes the robot itself. Threat to a new EU entrant: LOW as a hardware competitor — Phoenix will likely never be sold in volume in Europe; MEDIUM as a software/AI rival if Sanctuary's dexterity stack gets licensed onto third-party industrial arms via partners like Magna and Accenture. The strategic lesson for an EU entrant: Sanctuary validated wheels-over-legs for strong torsos years before it became consensus, but also shows that dexterity leadership alone does not produce revenue.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.sanctuary.ai/blog/sanctuary-ai-releases-new-generation-of-ai-robots-for-high-quality-data-capture | Gen 8: wheeled base, "legs too frail" feedback, camera/telemetry upgrades, cost/manufacturing improvements, <8 months after Gen 7, Microsoft collab | vendor-claimed |
| 2 | https://www.robotics247.com/article/sanctuary_ai_releases_next_generation_of_phoenix_general_purpose_robot | Gen 7 (Apr 2024): hydraulics miniaturization, ROM/durability, uptime, Gen 5 Jan 2023 deployment, Rose quotes | third-party |
| 3 | Aggregated search results (roboatlas, humanoid DBs) | 170 cm / 70 kg body figures | third-party |
| 4 | Phoenix hand technology coverage (sanctuary.ai + press) | 21 DoF hydraulic hands, 5 mN tactile, in-hand manipulation | vendor-claimed |
| 5 | https://www.therobotreport.com/sanctuary-ai-enters-strategic-relationship-with-magna-to-build-embodied-ai-robots/ + originofbots.com Magna trials report | Magna deployments, <24 h task learning, contract manufacturing option | third-party |
| 6 | https://www.sanctuary.ai/news | RL hand control, zero-shot in-hand manipulation, Isaac Lab, touch sensors, 2026 industrial pivot + wire-plugging demo, Friedmann CEO | vendor-claimed |
