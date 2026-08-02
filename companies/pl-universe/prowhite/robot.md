# ProWhite 2.0 (+ Zeus 1) — PL-Universe (普罗宇宙)

> Industrial-precision wheeled dual-arm humanoid from a young Suzhou startup: four-wheel omnidirectional base, 7-DoF arms with >7 kg payload each and a claimed ±0.05 mm repeatability with adaptive accuracy compensation — aimed squarely at 3C/semiconductor/automotive smart-factory tasks, not service interaction. A heavier sibling, Zeus 1 (~300 kg, 42 DoF, modular tooling, ~$140k), appears on third-party listings. Matters competitively as a Chinese attempt to marry humanoid form with cobot-grade precision claims.

| Field | Value |
|---|---|
| Company | PL-Universe Robotics Technology (Suzhou) (普罗宇宙机器人科技（苏州）有限公司) |
| HQ | Suzhou, China |
| Status (2026) | prototype / pre-commercial (third-party); vendor markets as product |
| First shown / launch | 2025 (ProWhite; "2.0" generation current; exact dates n/a) |
| Target applications | 3C/consumer electronics, automotive parts, semiconductor manufacturing & packaging/test, biomedicine; handling, assembly, inspection, packaging |
| Price | ProWhite: n/a (not disclosed; humanoid.guide's $45k entry conflicts with vendor data); Zeus 1 ~USD 140,000 [S3][S4] |
| Availability | China; no commercial availability confirmed [S4] |

## Design & morphology
ProWhite 2.0: dual-arm humanoid torso with sensor head on a four-wheel omnidirectional wheeled base. Vendor pages give two spec sets — Products page: 1051×800×2035 mm, 400 kg, 6-DoF arms, 910 mm arm span; product-detail page: height 165–195 cm adjustable, 300 kg, 7-DoF arms, 954 mm span — suggesting configuration variants or an in-progress spec revision [S1][S2, vendor-claimed, conflicting]. Operational height range 0.7–1.3 m; the adjustable 165–195 cm height implies a torso lift column. Zeus 1: heavy industrial humanoid, 160–175 cm, ~300 kg, 42 DoF (14 in hands), steel frame + aluminium [S3, third-party].

## Locomotion
Four-wheel omnidirectional drive; speed >2.5 m/s claimed (vendor "walking speed" wording; high for a wheeled indoor platform — treat cautiously) [S1][S2]. Zeus 1: 8 km/h max (third-party) [S3]. Terrain/brakes n/a.

## Upper body & manipulation
ProWhite 2.0: two 7-DoF (or 6-DoF per older page) arms; max load per arm >7 kg, total ~12 kg; arm span 910–954 mm; repeatability ±0.05 mm with "adaptive dynamic accuracy compensation" [S1][S2, vendor-claimed]. End-effectors: parallel grippers shown in vendor imagery; in-house PL-WitHand dexterous hand and end-effector line available [S1]. Zeus 1: 2-finger claws, 25 kg grip strength, modular end-effector/tool-switching system [S3]. Media at flange n/a.

## Sensing
Head camera module and torso sensor bar visible in vendor imagery; no sensor datasheet published. Third-party listings estimate RGB + depth cameras ~1080p [S3][S4, estimated]. Force/tactile sensing n/a (not disclosed) — notable gap given the precision claims.

## Actuation & power
Actuators n/a for ProWhite (Zeus 1 third-party: high-torque electric motors, harmonic + reinforced planetary gears [S3, estimated]). ProWhite battery: 40 V 100 Ah (~4 kWh), endurance ≥8 h, 2 h recharge [S1][S2]. Hot-swap n/a.

## Compute & software
Compute n/a (not disclosed). Third-party reporting says ProWhite runs "end-to-end flexible industrial VLA models" for assembly/inspection/packaging collaboration [S4]. Linux-based OS per third-party listing [S3, estimated]. SDK/fleet software n/a.

## Safety & compliance
n/a (not disclosed). No ISO 10218/TS 15066/CE claims found — a gap for a robot marketed into semiconductor/3C lines.

## Deployment evidence & traction
None found: no named customers, pilots or unit counts. Third-party assessment: pre-commercial prototype as of 2026 [S4]. Zeus 1 listed as "production-ready prototype with early commercial units" [S3, unverified].

## Assessment (analyst view)
*Analyst opinion.* Strengths: clear industrial focus, aggressive precision claim (±0.05 mm — cobot-class, unusual for a mobile humanoid), 8 h endurance, native dexterous-hand/end-effector line, early multilingual export posture. Weaknesses: one-year-old company, conflicting vendor spec sheets, no verified deployments, no safety certification, and the precision claim on a wheeled base is unproven physics-wise (base registration not explained). Threat to a new EU entrant: low today, but its marketing template — humanoid form + cobot precision + $50–140k price — is exactly the pitch an EU industrial semi-humanoid must out-credential; monitor for real pilots.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://en.pl-universe.com/ (+ /Products) | ProWhite 2.0 specs (400 kg set, 6-DoF, 910 mm, 40V 100Ah, ±0.05 mm), applications | vendor-claimed |
| 2 | https://en.pl-universe.com/product/12 | ProWhite 2.0 specs (300 kg set, 7-DoF, 954 mm, 165–195 cm adjustable, >2.5 m/s) | vendor-claimed |
| 3 | https://humanoid.guide/product/zeus-1/ | Zeus 1 specs, ~$140k, status | third-party |
| 4 | https://lite.duckduckgo.com/lite/?q=PL-Universe+ProWhite (aggregated snippets) | Chinese company name, VLA models, pre-commercial status | third-party |
| 5 | https://humanoid.guide/product/prowhite/ | $45k listing; NOTE: its 45–55 kg "walking" reception-robot description conflicts with vendor industrial specs and looks auto-generated | third-party |
