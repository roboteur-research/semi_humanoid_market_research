# PR-34D (+ PR-9D note) — Perceptyne

> Stationary dual-arm semi-humanoid workcell for fine assembly: **34 DoF = 2 × 7-DoF arms + 2 × 10-DoF three-finger hands**, with all-joint force sensing and high-resolution fingertip tactile arrays, ~6 kg payload per arm, priced around **$120K** and pitched as a drop-in replacement for a human worker on existing electronics/automotive assembly lines (no line retooling). In commercial pilots / early production with Indian manufacturers. Competitively it stakes out the low-cost stationary-dexterity niche that mobile humanoid vendors skip.

| Field | Value |
|---|---|
| Company | Perceptyne, Hyderabad |
| HQ | Hyderabad, India |
| Status (2026) | announced/early production — commercial pilots running |
| First shown / launch | Public 2024 (seed announcement Oct 2024) |
| Target applications | Electronics assembly (insertion, screwing, connector mating), automotive sub-assembly, fine manipulation |
| Price | ~USD 120,000 (third-party listing) |
| Availability | India; direct engagements with automotive/electronics OEMs; pilot-scale |

## Design & morphology
**Stationary pedestal/pillar-mounted torso** (renders show a column-mounted shoulder yoke with sensor head and status light ring) — no mobile base by design [S1][S4]. **34 DoF total: 7 per arm × 2, 10 per hand × 2** [S1][S2]. Height/weight n/a (workcell-scale).

## Locomotion
None (stationary; mounts at existing workstations without infrastructure change) [S1][S4].

## Upper body & manipulation
- Two **7-DoF arms**, **~6 kg payload each** [S1] (third-party).
- Two **10-DoF articulated three-finger hands** (renders show underactuated multi-link fingers with fingertip pads) — "highly articulate end-effectors" [S1][S2].
- **All-joint force sensing** + compliant control for contact-rich assembly; repeatability n/a.

## Sensing
**High-resolution tactile sensing** at fingers; integrated computer-vision camera system (head + presumably wrist cams); multi-modal sensing (vision + force + touch) [S1][S2].

## Actuation & power
Electric servo motors with **proprietary/custom gear technology** [S1] (third-party). Mains-powered workcell (battery n/a).

## Compute & software
Dedicated onboard **CPU/GPU for AI and vision**; **ROS/Linux-compatible**; **LLM integration** supported; "AI-centered control for robust physical intelligence" — task-level programming aimed at fast retasking [S1] (third-party/vendor). NVIDIA ecosystem association [S4].

## Safety & compliance
"Collaborative safety features for human shared workspaces" claimed [S1]; no specific ISO 10218/TS 15066 certification disclosed (n/a).

## Deployment evidence & traction
- **Commercial pilots / early production** status [S1] (third-party listing).
- "Working closely with manufacturing giants in automotive and electronics" in India [S2][S3] (third-party, unnamed customers).
- $3M seed (Oct 2024, Endiya + Yali + Whiteboard) explicitly for productization and customer acquisition [S2]. No unit counts public.
- Sibling **PR-9D**: single-arm 9-DoF variant sharing vision/AI stack for simpler stations [S2] (third-party; few public specs).

## Assessment (analyst view)
*Analyst opinion.* Strengths: focused wedge — tactile dual-arm dexterity at a ~$120K price on a stationary mount is far cheaper to build and certify than mobile humanoids, and matches how electronics lines actually deploy automation (station by station); strong local tailwind from India's electronics-manufacturing incentives. Weaknesses: $3M funding is thin for custom actuators + hands + AI; no named customers; stationary form cedes the intralogistics market entirely. Threat to an EU entrant: low in Europe near-term, but instructive — if EU customers' real need is bench-top dexterity rather than mobility, a Perceptyne-class product undercuts mobile semi-humanoids on price 3-5×; also a plausible future low-cost exporter.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | https://humanoid.guide/product/pr-34d/ | 34 DoF breakdown, 6 kg/arm, $120K, tactile/force sensing, ROS/Linux, LLM, pilots status | third-party |
| S2 | https://inc42.com/buzz/robotics-startup-perceptyne-bags-3-mn-from-endiya-partners-yali-capital-others/ | Seed round, founders, PR-34D + PR-9D, OEM engagements | third-party |
| S3 | https://entrackr.com/2024/10/deeptech-robotics-startup-perceptyne-raises-3-mn-in-seed-round/ | Product/positioning corroboration | third-party |
| S4 | https://www.perceptyne.com/ | Renders, drop-in positioning, NVIDIA association | vendor-claimed |
