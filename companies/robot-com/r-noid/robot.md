# R-noid — Robot.com

> R-noid is Robot.com's wheeled workplace humanoid, launched commercially mid-2026 under a pure RaaS model: dual 7-DoF arms on a 4-DoF articulated torso (floor to 1.9 m reach) over a holonomic base, driven by Physical Intelligence's π0.7 VLA model with VR-teleop fallback. It matters competitively because it pairs proven fleet operations (Kiwibot heritage) with the fastest published deployment promise in the segment (8-12 weeks) and already has <40 units at ~a dozen customers in kitchens, laundries and warehouses.

| Field | Value |
|---|---|
| Company | Robot.com (ex-Kiwibot) |
| HQ | San Francisco, CA, USA |
| Status (2026) | shipping (RaaS; <40 units deployed) [S2] |
| First shown / launch | Commercial launch June/July 2026 [S1] |
| Target applications | Restaurant Assistant, Packer, Picker, Folder (linen), Host — across industrial, logistics, healthcare, food service, lodging, experiential |
| Price | RaaS subscription; rates not disclosed |
| Availability | US; site visit → live in 8-12 weeks [S1][S2] |

## Design & morphology
Humanoid upper body on wheeled base: 1.7 m tall, 90 kg, base footprint 0.55 m [S4]. 4-DoF articulated torso gives a vertical workspace from floor (0 m) to 1.9 m [S1][S3]. Total DoF ≈ 21+ (2×7 arms + 4 torso + base; estimated). Design closely resembles Astribot's platform — Astribot is a named launch partner, suggesting hardware sourcing/licensing (analyst inference, unconfirmed) [S1].

## Locomotion
Holonomic wheeled base ("no legs, all lift") [S1][S3]. Speed n/a (not disclosed). Indoor commercial environments.

## Upper body & manipulation
Dual 7-DoF arms, 4 kg payload each [S4]. Modular end-effector options per task (grippers for picking/packing, folding tools) [S4]. Reach: ground to 1.9 m via torso articulation. Repeatability n/a.

## Sensing
Cameras for VLA perception (visual scene data fed to π0.7); detailed sensor suite n/a (not disclosed). LED expression display ("R-Soul" personality layer: dynamic face, conversational voice, brand-customizable apparel) [S4].

## Actuation & power
Actuators n/a (not disclosed). Battery: ~3 h operation per charge, plug-in charging [S4] — short runtime is a notable weak point vs competitors with swappable packs.

## Compute & software
Manipulation driven by Physical Intelligence π0.7 vision-language-action model; custom models co-developed with PI since 2025 [S2][S3]. Natural-language task instruction; autonomous or VR-teleoperated modes; initial deployments ~70% autonomy with teleop backfill; ~50 h of demonstration data needed for some tasks [S2]. NVIDIA Robotics and FieldAI among software/ecosystem partners [S1]. Fleet operations leverage Kiwibot's teleop infrastructure.

## Safety & compliance
n/a (not disclosed). No ISO/UL claims found in launch materials.

## Deployment evidence & traction
- Fewer than 40 units deployed across ~a dozen customers at launch (third-party reported) [S2].
- Disclosed customer: Harbor Links Golf Course, NY — loading delivery robots + order packing (synergy with Kiwibot fleet) [S2].
- Verticals in production: kitchens, packing lines, laundries, warehouses, hosting [S1][S4].
- Kiwibot heritage: 500+ delivery robots, 2.5M+ tasks — operations credibility [S2].

## Assessment (analyst view)
*Analyst opinion.* Strengths: real RaaS operating muscle (teleop centers, fleet ops, hospitality channels incl. Sodexo relationships), top-tier VLA partner in Physical Intelligence, fast 8-12-week deployment promise, and honest public traction numbers. Weaknesses: 3-hour battery is thin for multi-shift claims, 4 kg/arm payload limits industrial scope, hardware appears externally sourced (Astribot), and RaaS pricing opacity hides unit economics. Threat to a new EU entrant: moderate-high in hospitality/food-service/laundry verticals — they will likely define customer expectations for deployment speed there; low in heavier manufacturing where payload and safety certification dominate.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.prnewswire.com/news-releases/robotcom-launches-r-noid-a-humanoid-built-for-the-work-that-burns-people-out-no-legs-all-lift-to-the-bottom-line-302806619.html | Launch, 5 roles, partners, 8-12 wk deployment | vendor-claimed |
| 2 | https://thenextweb.com/news/robot-com-kiwibot-r-noid-humanoid-workplace-physical-intelligence | <40 units, ~12 customers, Harbor Links, 70% autonomy, 50h data, investors | third-party |
| 3 | https://www.automationmag.com/robot-com-launches-r-noid-enters-the-humanoid-market/ | 7-DoF arms, 4-DoF torso, holonomic base, π0.7 | third-party |
| 4 | https://www.robot.com/r-noid | 1.7m/90kg/0.55m base, 4kg/arm, 0-1.9m workspace, 3h battery, R-Soul, VR teleop | vendor-claimed |
