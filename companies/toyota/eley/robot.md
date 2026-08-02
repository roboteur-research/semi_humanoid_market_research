# ELEY — Toyota (Frontier Research Center)

> Toyota's new flagship semi-humanoid: "Embodied LEarning robot for Enhanced Yield" — a
> dual-arm wheeled mobile manipulator with QDD actuators in every joint for compliant
> "gentle touch" contact, unveiled at World Robot Summit 2025 Aichi (Dec 2025) and
> detailed in a Frontier Research interview on 2026-03-31. Successor to the single-arm
> HSR, aimed at production sites (labor shortage, skill transfer). The clearest signal
> yet that Toyota's service-robot lineage lands on wheels + two arms, not legs.

| Field | Value |
|---|---|
| Company | Toyota Motor Corp., Frontier Research Center (Factory Innovation Robotics Group; researcher Toshihide Yamada) |
| Status (2026) | research / pre-production prototype (deployment "under conditions close to real production sites" planned) |
| First shown | WRS 2025 Aichi (Dec 2025); official article 2026-03-31 |
| Target applications | production-site assembly & handling, human-robot collaboration, learning-based skill transfer |

## Design & morphology
Human-like joint structure sized to an average adult Japanese male (joint spacing, arm
thickness); dual arms with grippers; head with status display; rounded wheeled base
(official render). Distinctive: an actuated **scapular (shoulder-blade) axis** for
human-like bimanual range — pushing, reach extension, jar opening — absent on HSR. [S1]

## Actuation — the core innovation
Quasi-direct-drive (QDD) actuators in EVERY joint: gear ratio ≤10:1 with high-torque
motors → high backdrivability, low inertia, arms yield to external forces ("gentle
touch"); validated on prototypes pressing cups to the floor and opening door handles.
Direct-drive mechanism without wires/resin belts for positional accuracy. Rationale
documented with the backdrivability equation in Toyota's article. [S1]

## Software & AI
Physical-AI approach: imitation learning from human movements; "collecting data for one
hour, then processing and implementing it on ELEY"; plan to convert successes AND
failures at near-production deployments into training data (fast improvement cycle).
Related: Toyota "Robotics Foundation Models" collaborative research. [S1]

## Lineage & spin-offs
HSR (2012) → autonomous-navigation tech into "Potaro" hospital transport robot;
recognition/decision tech into "KumiPro" factory robot (Toyota Motor East Japan) → ELEY
integrates the lessons (contact-rich manipulation was HSR's key weakness — arms broke on
unexpected contact). [S1]

## Open challenges (per Toyota)
(1) long-duration reliability, (2) end-effector repeatability, (3) learning-data
infrastructure — self-declared "not on par with the world's leading technologies" yet. [S1]

## Assessment (analyst view)
*Analyst opinion.* ELEY is a research program, not a product — but it is Toyota, with
manufacturing scale, the HSR academic ecosystem, and a stated production-site deployment
path. The QDD-everywhere + scapula design differentiates on safe contact-rich
manipulation rather than payload, mirroring European compliance philosophy (Franka, DLR)
more than Chinese spec-sheet competition. Commercialization timing undisclosed; treat as
the highest-credibility Japanese entrant of the late 2020s.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://global.toyota/en/mobility/frontier-research/44105171.html | full interview, design, QDD, name, lineage (2026-03-31) | vendor-claimed |
| 2 | https://robotstart.info/article/2025/12/08/381477.html | WRS 2025 Aichi unveiling | third-party |
