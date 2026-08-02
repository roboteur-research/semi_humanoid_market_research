# iggyRob ("Iggy Rob") — igus GmbH

> iggyRob is igus's €47,999 wheeled humanoid service robot: two 6-DoF ReBeL plastic-geared cobot arms with bionic hands on a ReBeLMove AMR base, a virtual smiley-face display, and igus Robot Control software. Built almost entirely from igus's lubrication-free "motion plastics" catalogue components, it is the cheapest CE-certified humanoid-format robot from any established Western manufacturer — a deliberate price-floor play ("comparable humanoids cost two to three times more") aimed at Mittelstand machine tending, in-plant transport and service/reception tasks rather than at high-performance manipulation. Competitively it defines the European entry-level price point that any new semi-humanoid entrant will be measured against.

| Field | Value |
|---|---|
| Company | igus GmbH |
| HQ | Cologne, Germany |
| Status (2026) | shipping (catalogue product; igus.eu claims "ready to ship from 24 hours"; Home variant ~3-week delivery) [S2][S4] |
| First shown / launch | April 29, 2025 (press launch); "iggyRob Home" variant listed on RBTX by mid-2026 [S1][S4] |
| Target applications | machine tending (injection molding), intralogistics/transport, reception/service desk, canteen (clearing cutlery), pick & place, education/research, AI training [S1][S4] |
| Price | €47,999 (~$54,500) for iggyRob; iggyRob Home price not published (quote via RBTX) [S1][S4] |
| Availability | Global via igus direct sales + RBTX marketplace; "test before you invest" on-site trial program [S1] |

## Design & morphology
Humanoid-format torso shell on a flat AMR base; approx. 1.70 m tall, 101 kg (iggyRob) / 120 kg (iggyRob Home) [S1][S2][S4]. 16 DoF total (vendor RBTX figure; 2×6-DoF arms + head/neck and base) [S3][S4]. No torso lift column and no waist articulation — working height is fixed (analyst observation from vendor imagery). Head is a rounded dome with a "virtual face" LED/display for human interaction [S2]. Signature igus black-and-orange styling; structural and drive components are lubrication-free, maintenance-free polymer parts (cycloidal plastic gearboxes from the ReBeL line) [S1]. A third-party database lists 160 cm / 20 DoF — conflicts with vendor data, treat as low confidence [S6].

## Locomotion
ReBeLMove Pro AMR base (differential drive, three-point bearing chassis) [S1][S2]. Base load capacity 50 kg, payload up to 100 kg on the standard iggyRob listing; the iggyRob Home listing rates the ReBeLMove Pro chassis to 250 kg payload [S2][S4]. Speed: 2 m/s claimed for iggyRob Home [S4]; a third-party profile lists 2 km/h (0.56 m/s) for the original — unresolved discrepancy, the 2 m/s figure looks like the AMR platform maximum rather than a safe humanoid-configuration speed (estimated) [S6]. Indoor, flat-floor operation; VDA/VDE-5050-compatible fleet interface for mixed AMR fleets [S1][S2].

## Upper body & manipulation
Two ReBeL-6DOF-03 cobot arms: 6 DoF each, 2 kg payload per arm, 664 mm reach, joint speed up to 45°/s, max joint torque 20 Nm [S2][S3]. iggyRob Home lists 2.5 kg per arm [S4]. Max recommended component weight for handling tasks: 1.5 kg [S2]. End-effectors included on the standard unit: one suction pad with igus CobotPump (vacuum) and one ReBeL gripper; "bionic hands" (igus ReBeL Hand, 2023) that "grip like a person" are the humanoid signature option; Home variant offers vacuum gripper / multi-finger gripper / bionic hand options plus an optional 50 kg transport basket on the back [S1][S2][S4]. No force-torque sensor at the flange is documented; repeatability not stated for the integrated robot (n/a).

## Sensing
LiDAR sensor(s) on the AMR base for SLAM navigation; 3D cameras in the chest and in the vehicle base for object detection and navigation [S1][S2]. Virtual face display for HRI [S2]. No documented tactile, wrist F/T, or microphone array (n/a — not disclosed).

## Actuation & power
ReBeL joints: brushless motors with igus's lubrication-free plastic cycloidal ("strain wave"-style polymer) gearboxes — the core igus differentiator: cheap, light, maintenance-free, but low stiffness/torque versus metal harmonic drives [S1][S3]. Battery: capacity not disclosed; up to 8 hours runtime per charge [S1][S2]. iggyRob Home adds wireless (inductive) charging for uninterrupted operation [S4]. Automatic dock charging for the standard unit: not explicitly documented (n/a).

## Compute & software
Onboard compute not disclosed (n/a). Software: free igus Robot Control (iRC) with 3D simulation/digital twin; web-based visual/no-code mission programming on the Home variant; ROS 2 interface for research/integration; VDA/VDE 5050 fleet-management compatibility [S1][S2][S4]. No AI/VLA autonomy stack is claimed — task programming is classical (teach/waypoint/no-code), which is honest but limits it to structured tasks (analyst note). RBTX ecosystem provides accessories (3D scanner, grippers) [S4].

## Safety & compliance
CE-certified (vendor) [S1][S2]. Cobot-class arms with low speeds/torques (45°/s, 20 Nm) inherently limit impact energy; no ISO 13482 or ISO/TS 15066 validation is published (n/a — not disclosed). Approved for fleet management under the VDA/VDE 5050 interface standard (vendor wording "VDE 5050") [S1][S2].

## Deployment evidence & traction
No named external customers found (Aug 2026). igus states it will use iggyRob internally for placing components into its own injection-molding machines [S1]. Sales channel evidence: live catalogue listings with ship-from-24h (igus.eu) and ~3-week delivery (RBTX Home variant) indicate genuine series availability rather than vaporware [S2][S4]; the "test before you invest" program implies units in field trials [S1]. No unit counts, case studies or independent hands-on reviews located; press imagery remains rendered rather than photographic — deployment evidence is therefore weak (third-party observation).

## Assessment (analyst view)
*Analyst opinion.* Strengths: unbeatable published price (€47,999) with real orderability, CE mark, an existing global sales machine touching most European factories, in-house component cost control, and a maintenance-free plastics story that resonates with cost-driven Mittelstand buyers; the RBTX "test before you invest" motion lowers adoption friction. Weaknesses: capability ceiling — 2 kg/arm, 664 mm reach, 45°/s joints and no torque-controlled manipulation or AI autonomy stack put it a class below TIAGo Pro, let alone logistics humanoids; fixed torso height; no documented customers or real-world footage; the humanoid form is arguably packaging around an AMR + two cobots. Threat to a new EU entrant: moderate-high on price anchoring and channel reach (it will cap what customers accept as "reasonable" pricing for wheeled humanoids), low on technology. A differentiated entrant should position clearly above iggyRob on payload, compliance-controlled manipulation and autonomy — and expect igus to keep iterating variants cheaply.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://press.igus.com/2025/04/29/iggy-rob-humanoid/ | launch date, €47,999, 1.70 m, 8 h, components lineage, AMR base 50/100 kg, applications, CE, VDE 5050, test-before-invest, internal molding use | vendor-claimed |
| 2 | https://igus.eu/product/22702 + https://www.igus.com/product/0-LCA-IROB | part 0-LCA-IROB, 101 kg, arm specs (2 kg / 664 mm / 45°/s), 1.5 kg component weight, suction pad + ReBeL gripper, 3D cameras chest+vehicle, virtual face, ship 24 h | vendor-claimed |
| 3 | https://rbtx.sg/en-SG/components/humanoid/iggyrob-humanoid-robot | 16 DoF, 100 kg, 20 Nm max joint torque, ReBeLMove Pro | vendor-claimed |
| 4 | https://rbtx.com/en-US/components/humanoid/iggyrob-home + https://www.igus.co.uk/product/RBTX-IGUS-0353 | iggyRob Home: 120 kg, 2.5 kg/arm, 250 kg chassis, 2 m/s, wireless charging, 50 kg basket, web app, 3-week delivery | vendor-claimed |
| 5 | https://interestingengineering.com/innovation/germanys-53k-iggy-rob-is-a-humanoid-robot-built-for-real-world-industry-tasks | independent coverage of launch, price ~$53-54.5k, spec confirmation | third-party |
| 6 | https://www.robothub.app/en/robots/iggy-rob | third-party profile (160 cm, 20 DoF, 2 km/h, "Demo" stage) — conflicts with vendor data | third-party |
