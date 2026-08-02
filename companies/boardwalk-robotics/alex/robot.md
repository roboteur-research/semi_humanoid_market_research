# Alex — Boardwalk Robotics

> Alex is a legless humanoid upper torso (19 DoF, 10 kg payload) from IHMC-lineage Boardwalk Robotics, announced August 2024. It mounts on a fixed pedestal or a third-party AMR and targets manufacturing, food processing, logistics and maintenance — with aviation MRO as the first commercial pilot and immediate availability to researchers. Competitively it is the most direct US analogue to a European torso-on-any-base strategy: manipulation-first, mobility as a customer choice, backed by 20+ years of humanoid R&D pedigree.

| Field | Value |
|---|---|
| Company | Boardwalk Robotics |
| HQ | Pensacola, FL, USA |
| Status (2026) | shipping to researchers; commercial pilots (announced Aug 2024) |
| First shown / launch | August 2024 (IEEE Spectrum exclusive) |
| Target applications | Manufacturing (incl. composite sanding), food processing, logistics, maintenance, aviation MRO (first pilot) |
| Price | n/a (not disclosed) |
| Availability | Purchasable now by research groups; commercial deployment via pilot partnerships |

## Design & morphology
Legless humanoid upper body: torso + head + two arms, 19 DoF total, engineered in-house. Mounted either on a stationary pedestal or on a third-party autonomous mobile robot base ("glorified AMR", per Boardwalk) — mobility is explicitly outsourced/optional [S1][S2]. Height/weight n/a (not disclosed). Arms derive from the design developed for IHMC's Nadia research humanoid [S2]. Legs are on the roadmap but deliberately excluded from the first product.

## Locomotion
None built in. Pedestal (fixed) or third-party AMR mounting; base choice left to integrator/customer [S1]. n/a for speed/terrain.

## Upper body & manipulation
- Payload: 10 kg (vendor) [S1][S2].
- Joint speed: up to 9 rad/s ("high-speed joints") [S2].
- Wrists: 300° rotation range [S2].
- Actuators: in-house design with deliberately low gear ratios — backdrivable, high-bandwidth force behavior without expensive joint torque sensors [S2].
- End effectors: interchangeable grippers; improved gripper generation announced with faster tool changes [S1]. Hand details otherwise n/a.
- Arm DoF split not published (19 DoF covers torso + arms + neck; per-arm count n/a).

## Sensing
Head-mounted perception suite (cameras; details n/a — vendor site currently offline). Torque/force behavior achieved through actuator design rather than dedicated torque sensors [S2].

## Actuation & power
Proprietary electric actuators (low gear ratio, high joint speed). Power: pedestal-mounted units mains-powered; AMR-mounted power arrangement depends on base. Battery/runtime n/a.

## Compute & software
n/a (not disclosed in available sources). Boardwalk emphasizes manipulation software maturity from IHMC lineage; researcher sales imply a development API, but no public SDK documentation was found (site down).

## Safety & compliance
n/a (not disclosed). Design intent "safe, cost-effective industrial manipulation" [S2]; no certifications published.

## Deployment evidence & traction
- Researchers: Alex available for purchase since launch; research institutions were the first customers [S1] (third-party).
- Commercial: pilot partnerships in progress; first pilot application in aviation (MRO tasks) [S1] (third-party).
- Demonstration imagery: carbon-fiber sanding task (manufacturing) in launch coverage [S1].
- No unit counts, customer names, or revenue disclosed. Company website outage (Aug 2026) makes current status hard to verify — flag for follow-up.

## Assessment (analyst view)
*Analyst opinion.* Strengths: world-class humanoid pedigree (IHMC/Nadia), sensible manipulation-first architecture identical in philosophy to leading EU semi-humanoid plays, in-house actuators with attractive speed/compliance properties, and a defensible aviation-MRO wedge. Weaknesses: no disclosed funding, tiny team, no published pricing/certifications, minimal marketing presence — and a broken website in Aug 2026, which raises execution/viability questions. Threat to a new EU entrant: LOW-MEDIUM today (limited scale, US-centric), but HIGH conceptual overlap — Alex validates the exact same product thesis, so expect head-to-head competition in research sales and industrial pilots if Boardwalk secures funding. An EU entrant should track their aviation pilots and actuator IP most closely.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://spectrum.ieee.org/boardwalk-robotics-alex-humanoid | Launch (Aug 2024), IHMC lineage, legless rationale, 19 DoF, 10 kg, mounting options, aviation first pilot, researcher availability, gripper/tool-change improvements, leadership | third-party |
| 2 | Search-aggregated Alex spec coverage (IEEE-derived) | 9 rad/s joints, 300° wrists, low-gear-ratio no-torque-sensor actuators, Nadia-derived arms, "20 years of R&D" | third-party |
| 3 | https://www.boardwalkrobotics.com/ | Official site — currently a broken/parked Nicepage page (Aug 2026); could not verify current vendor claims | vendor-claimed (unavailable) |
