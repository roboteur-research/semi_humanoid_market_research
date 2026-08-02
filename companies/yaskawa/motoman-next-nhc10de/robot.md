# MOTOMAN NEXT-NHC10DE — Yaskawa Electric

> The NEXT-NHC10DE is Yaskawa's AI-era dual-arm semi-humanoid: a 10kg-payload two-armed robot with tactile fingertip sensors whose skills are built by imitation learning (motion-captured human demonstrations) and NVIDIA Isaac Sim/Isaac Lab synthetic data rather than point teaching. Debuted at iREX 2025 (3-6 Dec, Tokyo) doing vision-guided picking and packing, with commercial release targeted for 2026, it marks the world's largest servo maker entering the semi-humanoid category — an inflection signal for the entire dual-arm market. This dossier also covers its lineage: the shipping MOTOMAN-SDA 15-axis dual-arm series and the never-commercialized SmartPal service humanoid research line.

| Field | Value |
|---|---|
| Company | Yaskawa Electric |
| HQ | Kitakyushu, Japan |
| Status (2026) | announced (iREX 2025 debut; commercial release slated 2026) |
| First shown / launch | iREX 2025, 3-6 December 2025, Tokyo Big Sight [S1] |
| Target applications | Picking/packing, kitting, food handling, medical-device sorting, flexible-material and irregular-item manipulation — tasks needing "human-like sensory and fine motor capability" [S1][S5] |
| Price | n/a (not disclosed) |
| Availability | Release 2026 (regions n/a; Yaskawa global channel expected) |

## Design & morphology
Dual-arm upper-body robot in the MOTOMAN NEXT autonomous line. Configuration details (arm DoF, torso axes, mounting) not yet fully disclosed; SDA-family convention is 2×7-axis arms + torso rotation axis on a fixed base [S3, estimated by lineage]. Payload **10kg** (per the "10" class designation; per-arm vs total not explicitly broken out — 10kg class per arm estimated) [S1]. No mobile base shown at iREX — pedestal/cell mounting (third-party show reports).

## Locomotion
None disclosed — stationary cell robot (estimated from iREX presentation). Yaskawa's mobility plays run separately (SmartPal heritage; SoftBank physical-AI partnership).

## Upper body & manipulation
Two arms with **tactile fingertip sensors** enabling delicate, force-aware handling of irregular and deformable objects (fabric handling shown in NEXT-line demos) [S1][S5]. iREX demo: identify → grasp → pack items via vision + dexterous manipulation [S1]. Grippers: multi-finger tactile-tipped end-effectors (detail n/a). Repeatability/reach n/a (not disclosed).

## Sensing
Vision-based object recognition; fingertip tactile arrays; force control from Yaskawa's servo stack [S1]. Details (cameras, depth, wrist F/T) n/a (not disclosed).

## Actuation & power
In-house Yaskawa AC servo actuation (Sigma-series ecosystem, vendor-claimed by lineage); mains-powered. Yaskawa's vertical servo integration is its core cost/reliability advantage.

## Compute & software
MOTOMAN NEXT autonomous-robot architecture: an AI decision layer above the motion controller that lets the robot "understand situations, make independent decisions, and act" instead of replaying taught paths [S5]. Skill acquisition: **imitation learning from human demonstrations** captured via marker tracking/motion capture; **NVIDIA Isaac Sim + Isaac Lab** generate synthetic training data (e.g. weight-variation robustness without physical trials) [S1]. Strategic goal: **"engineering-less"** deployment — eliminating teaching and slashing system-integration cost, Yaskawa's answer to labor-shortage economics [S2]. Connectivity to i3-Mechatronics factory-data stack; SoftBank AI-RAN physical-AI partnership announced for multi-role robots [S2].

## Safety & compliance
Collaborative-design claims at iREX (human-coexistence operation); certifications n/a (not disclosed pre-release). Sister MZ cobot line shows Yaskawa's autonomous-safety direction (approach-stop/resume) [S2].

## Deployment evidence & traction
- iREX 2025 live demos: dual-arm picking/packing with tactile grasping [S1, third-party observed].
- Commercial release 2026 announced; no customers/pricing yet [S1].
- Context/lineage traction: **MOTOMAN-SDA** dual-arms (SDA5: 5kg/arm, 843mm; SDA10: 10kg, 1,003mm; SDA20: 20kg, 1,323mm; all 15-axis) shipping since the mid-2000s into electronics/appliance cell assembly worldwide [S3] — Yaskawa knows how to sell and service dual-arms at industrial scale.
- Cautionary lineage: **SmartPal** (2005 Aichi Expo → SmartPal V 2007: 1,325mm, 127kg incl. 23kg battery, 21 DoF, 2×7-axis arms, 2kg payload, waist bend for floor pickup, 3.6km/h → SmartPal VII research) never commercialized — Yaskawa has attempted the service semi-humanoid before and retreated [S4].

## Assessment (analyst view)
*Analyst opinion.* Strengths: the deepest actuation supply chain in robotics, industrial-grade reliability, a global integrator network, and a pragmatic AI stack (imitation learning + Isaac sim2real + tactile) aimed at measurable factory tasks rather than humanoid theater; "engineering-less" attacks the real adoption bottleneck (integration cost, not hardware price). Weaknesses: announced-not-shipping; stationary scope cedes mobile/service use cases; Yaskawa's SmartPal history shows institutional caution — it kills lines that don't hit industrial volume. Category meaning: when the world's top servo maker productizes an AI dual-arm, component costs fall and customer skepticism drops for everyone — but the competitive bar for an EU entrant in *fixed* dual-arm automation rises steeply. Threat level: high (2027+) in industrial cells, including in Europe where Yaskawa has plants and channel; low in mobile semi-humanoid niches.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://monoist.itmedia.co.jp/mn/articles/2512/04/news059.html | iREX 2025 debut (12/3-6), 10kg, tactile fingertips, imitation learning (mocap), Isaac Sim/Lab, picking/packing demo, 2026 release | third-party |
| 2 | https://www.today-jp.com/news/irex-2025-yaskawa-ai-cobots-engineeringless-manufacturing-strategy | engineering-less strategy, SoftBank AI-RAN physical-AI partnership, MZ cobot safety | third-party |
| 3 | https://www.e-mechatronics.com/product/robot/lineup/sda/index.html | SDA5/10/20: 15 axes, 5/10/20kg per arm, 843/1003/1323mm reach | vendor-claimed |
| 4 | https://www.yaskawa.co.jp/newsrelease/technology/8933 | SmartPal V (11/2007): 1,325mm, 127kg, 21 DoF, 2×7 arms, 2kg, 3.6km/h, waist | vendor-claimed |
| 5 | https://www.yaskawa.co.jp/motoman-next/ | NEXT series 2023, autonomous decisions, application domains (food, medical, flexible materials) | vendor-claimed |
