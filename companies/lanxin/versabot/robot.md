# VersaBot VB1 / VB1-I / VB2 — Lanxin Robotics (蓝芯科技)

> Wheeled dual-arm mobile manipulators from Hangzhou vision-AMR maker Lanxin: compact dual arms on 3D-vision AMR bases, aimed at factory intralogistics, machine tending and inspection. VB1/VB1-I put small 6-joint arms on a mast over an AMR chassis (0.2–2 m working height); VB2 is a taller anthropomorphic torso with 7-joint arms on a wheeled base. Competitive significance: an installed-base AMR/vision player (Huawei, BYD, LG accounts) upselling dual-arm manipulation into existing factories.

| Field | Value |
|---|---|
| Company | Lanxin Robotics (Hangzhou Lanxin Technology, 蓝芯科技) |
| HQ | Hangzhou, China |
| Status (2026) | shipping / limited production, pilot deployments [S4] |
| First shown / launch | ~2025 (VersaBot line on vendor site; exact dates n/a) |
| Target applications | Factory intralogistics, machine tending, 3C/electronics handling, inspection, R&D |
| Price | ~USD 120,000 (third-party listing, model unspecified; not vendor-confirmed) [S4] |
| Availability | China; direct/solution sales bundled with MCS/RCS software |

## Design & morphology
Three variants [S1][S2][S3, all vendor-claimed]:
- **VB1**: dual 6-joint arms on a vertical mast over an AMR chassis; 700×610×1650 mm, operating height 0.4–2 m, rotation diameter 580 mm, ground clearance 22 mm.
- **VB1-I**: same footprint (700×610×1650 mm) with operating height 0.2–2 m, ground clearance 30 mm; faster base.
- **VB2**: anthropomorphic torso/head on wheeled base; 580×480×1700 mm, operating height 0.4–2 m, rotation diameter 760 mm.
Weights n/a (not disclosed). The mast/torso gives an effective torso lift covering floor-to-2 m working heights.

## Locomotion
VB1/VB2: four-wheel omnidirectional drive; VB1-I: dual-wheel differential. Max speed 1.2 m/s (VB1/VB2), 1.5 m/s (VB1-I). Indoor 0–40 °C, 10–90 % RH. 3D laser SLAM navigation. [S1][S2][S3]

## Upper body & manipulation
VB1/VB1-I: two 6-joint arms, gripping payload 2 kg each. VB2: 7-joint arms, gripping payload 5 kg. Reach n/a (not disclosed). End-effectors: grippers (VB1 image shows two-finger grippers); tool-changer/media at flange n/a. [S1][S2][S3]

## Sensing
Panoramic RGB-D depth vision system (Lanxin LX-MRDVS 3D vision), 3D laser SLAM lidar; OmniHead sensor-head module offered separately. Force/tactile sensing n/a (not disclosed). [S1][S2][S3]

## Actuation & power
Actuators n/a (not disclosed; third-party listing assumes servo motors with harmonic/planetary gears [S4, estimated]). Runtime: VB1/VB1-I 2–3 h; VB2 4–6 h. Battery capacity, hot-swap, dock n/a. [S1][S2][S3]

## Compute & software
Onboard compute n/a (third-party: industrial CPU + optional AI accelerator, Linux/ROS [S4, estimated]). Software: "Multimodal AI Interaction Hub"; integrates with Lanxin MCS (fleet/mission control) and RCS (robot control) platforms — the key differentiator, as VersaBots slot into existing Lanxin AMR fleets. [S1][S2][S3]

## Safety & compliance
n/a (not disclosed). Third-party listing: "safe for human collaboration under controlled conditions" [S4, estimated]. No ISO 10218/13482/CE claims found.

## Deployment evidence & traction
Lanxin's AMR business claims Huawei, BYD, LG and other blue-chip factory customers [S1, vendor-claimed]; no VersaBot-specific deployment counts disclosed. Third-party listing status: "limited production / pilot deployments" [S4].

## Assessment (analyst view)
*Analyst opinion.* Strengths: real factory channel and deployed 3D-vision/fleet software into which dual-arm units can be sold; pragmatic mast-based design covering 0.2–2 m working heights. Weaknesses: light payloads (2–5 kg), short 2–3 h runtime on VB1-class units, no disclosed force sensing or safety certification, and arms appear to be light collaborative modules rather than industrial-grade manipulators. Threat to a new EU entrant: moderate in China intralogistics; low in the EU near-term (no EU channel), but the "AMR incumbent upsells dual arms" playbook is exactly the pattern an EU entrant must beat on manipulation quality.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.lanxinrobotics.com/humanoid-robots/vb1/ | VB1 specs (dimensions, 6-joint 2 kg arms, omni base, 1.2 m/s, 2–3 h, RGB-D, SLAM) | vendor-claimed |
| 2 | https://www.lanxinrobotics.com/humanoid-robots/vb1-i/ | VB1-I specs (diff-drive, 1.5 m/s, 0.2–2 m height) | vendor-claimed |
| 3 | https://www.lanxinrobotics.com/humanoid-robots/vb2-2/ | VB2 specs (7-joint 5 kg arms, 4–6 h, dimensions) | vendor-claimed |
| 4 | https://humanoid.guide/product/versabot/ | price ~$120k, status; NOTE: its 165 cm/75 kg/38-DoF/15 kg-payload figures conflict with vendor data and look auto-generated | third-party |
