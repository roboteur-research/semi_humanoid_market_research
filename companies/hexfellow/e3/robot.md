# e³ (e³-Mobile / e³-Desktop / e³-Mobile-π) — HexFellow Robotics

> The e³ ("e-cubed") is HexFellow's modular embodied-AI robot platform family: pre-configured combinations of the company's omnidirectional chassis, vertical lifts, 6/7-axis force-controlled arms and grippers, sold to researchers and VLA data-collection teams. The mobile variants are de-facto wheeled semi-humanoids (dual arms + lift on holonomic base). Competitively it plays in the same ALOHA-descendant research-platform market as ARX, AgileX Cobot Magic and Galaxea R1 — with a fully modular, open-SDK, screwdriver-assembly angle.

| Field | Value |
|---|---|
| Company | HexFellow Robotics Co., Ltd. |
| HQ | Nansha, Guangzhou, China |
| Status (2026) | shipping (direct online sale; prices on request) [vendor site] |
| First shown / launch | ~2024-2025 (site/catalogue live 2025; GitHub org since 06/2023) [estimated] |
| Target applications | Embodied-AI research, VLA data collection (desktop + mobile), prototyping |
| Price | n/a (not disclosed — storefront shows $0.00 / quote-based) |
| Availability | Direct worldwide (Shopify store, shipping policy published); Discord support |

## Design & morphology
Three packaged configurations [S1][S2, vendor-claimed]:
- **e³-Desktop** — stationary all-in-one bimanual data-collection rig; x2 config (dual ARCHER-D6Y 6-axis arms) or x4 config (quad ARCHER-L6Y, i.e. dual leader-follower teleop pairs).
- **e³-Mobile** — indoor holonomic wheeled platform ("TidyBot-based chassis with a modular frame"); chassis, lift and arms swappable across the catalogue (MAVER-L4/X4 powered-caster or ARK diff chassis; IOTA/ZETA lifts).
- **e³-Mobile-π** — flagship mobile config: TRIGGER-A3 omnidirectional triangular 3-omni-wheel chassis + vertical lift + dual ARCHER-L6Y 6-axis arms.
Overall height/weight/DoF totals not published; a dual-6-axis-arm mobile config with lift ≈ 13-15 DoF plus grippers [estimated].

## Locomotion
TRIGGER-A3: 3-omni-wheel holonomic, 50 kg capacity, 2 m/s max, 9-axis IMU. MAVER-X4/L4: 4 powered-caster wheels, 80 kg, 2 m/s. ARK: two-wheel differential, 80 kg, 2 m/s. PCW-25 single powered-caster module (25 kg, 1.3 m/s) for custom builds [S1, vendor-claimed]. Indoor flat-floor platforms; no climbing spec (n/a).

## Upper body & manipulation
ARCHER-D6Y arm: 6 axes, 2 kg payload, 608 mm reach, 4.7 kg own weight, ±0.1 mm repeatability, 48 V, CAN/Ethernet, 250 W max, planetary integrated joint motors, internal wiring, gravity compensation, aluminum CNC + carbon fiber [S6, vendor-claimed]. ARCHER-L6Y = larger 6-axis variant (specs n/a); SABER-D7Y/H7X = 7-axis line (specs n/a). GP-100 gripper: 30 N grip, 100 mm span, planetary servo, pressure-sensor compatible [S1]. Vertical lifts IOTA/IOTA-P/ZETA give torso travel (stroke n/a).

## Sensing
RGBD cameras offered for data collection; HEXSENSE-Y200 9-axis IMU (CAN); chassis IMUs integrated. Lidar not standard but supported in software (Livox drivers, FAST-LIO SLAM repos on GitHub) [S1][S4]. Force sensing: gravity-compensated arms marketed as force-control capable; gripper pressure sensing optional [S1][S6].

## Actuation & power
In-house HEXMOTOR planetary joint actuators (48 V, 3 Nm rated / 7 Nm peak, CAN-FD) power arms and modules [S1, vendor-claimed]. HEXPOWER-M10/S3 multi-voltage distribution modules. Battery capacity/runtime per configuration n/a (not disclosed).

## Compute & software
HEXCOMPUTER-P1 compute module (spec n/a). Software: ROS 2 Humble/Jazzy and Python SDK, open-source demos, Apache-2.0 repos (chassis toolkit, arm controller, SLAM/localization, Livox drivers) on github.com/hexfellow; XVIEW browser-based device verification/control UI; CAN-bus protocol openly documented [S2][S3][S4, vendor-claimed]. The "π" in e³-Mobile-π strongly suggests targeting Physical Intelligence π0-style VLA pipelines, but no formal Physical Intelligence partnership or openpi integration is documented anywhere found — treat as branding, not partnership [analyst note, estimated].

## Safety & compliance
n/a (not disclosed). Research platforms; no ISO 13482/10218 or CE claims found.

## Deployment evidence & traction
No named customers or unit counts published. Evidence of real activity: 75 public GitHub repos with active maintenance (updated through late 2025), a public Discord, published shipping/return policies indicating international fulfilment [S1][S4, third-party]. Traction vs ARX/AgileX unknown — likely small [estimated].

## Assessment (analyst view)
*Analyst opinion.* Strengths: genuinely modular catalogue (chassis/lift/arm/actuator all in-house), open ROS 2/Python stack and documented CAN protocol — attractive to labs that outgrow closed kits; low-cost Guangzhou manufacturing. Weaknesses: no published pricing, no disclosed funding or customer base, thin brand, arms limited to 2 kg-class payloads — it competes on openness against ARX/AgileX ecosystems that already own the Mobile-ALOHA mindshare. Threat to an EU entrant: low as a direct competitor, but relevant as a commoditizer — it shows a complete dual-arm mobile platform supply chain is available off-the-shelf from China, compressing hardware margins for research-grade semi-humanoids.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://hexfellow.com/ | Component specs (TRIGGER-A3, MAVER, ARK, GP-100, HEXMOTOR, HEXPOWER, HEXSENSE) | vendor-claimed |
| 2 | https://hexfellow.com/pages/e3 | e³ variants: Desktop x2/x4, Mobile, Mobile-π (TRIGGER-A3 + lift + dual ARCHER-L6Y); Python SDK/XVIEW/ROS2 | vendor-claimed |
| 3 | https://docs.hexfellow.com/ | Documented product range, XVIEW, CAN protocol, firmware | vendor-claimed |
| 4 | https://github.com/hexfellow | Open-source repos (Apache-2.0), org since 06/2023, active maintenance | third-party (GitHub) |
| 5 | DuckDuckGo snippets (hexfellow 机器人 公司) | HQ Nansha, Guangzhou; business description | third-party |
| 6 | https://hexfellow.com/products/archer-d6y | ARCHER-D6Y arm full specs | vendor-claimed |
