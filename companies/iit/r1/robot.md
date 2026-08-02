# R1 ("R1 — your personal humanoid") — IIT Genoa

> R1 is IIT's affordable wheeled semi-humanoid (2016): ~1.2 m, 51 kg, two driving wheels + castors, extensible torso (1.15-1.35 m), two 8-DoF arms with simplified sensorized hands, body largely of polymer, targeting a "small family car" price point. It pioneered the low-cost service semi-humanoid concept in Europe and was applied to hospital/rehabilitation assistance with Fondazione Don Gnocchi, but was never commercialized at scale; IIT's humanoid focus has since shifted to the legged ergoCub.

| Field | Value |
|---|---|
| Company | Istituto Italiano di Tecnologia (iCub Facility / AMI) |
| HQ | Genoa, Italy |
| Status (2026) | research (active platform, no longer flagship; ergoCub era) |
| First shown / launch | Unveiled July 2016 [S3] |
| Target applications | Domestic and professional service, healthcare/rehabilitation assistance, HRI research |
| Price | Target "cost of a small family car" (~EUR 20-30k class, estimated); never sold commercially at volume |
| Availability | Research platform; units placed with partner labs/clinics; travel case purchasable from IIT (research distribution) [S2] |

## Design & morphology
Height 1.2 m nominal; torso mechanism varies height 1.15-1.35 m (200 mm travel) to match work-surface heights [S2, vendor-claimed]. (IIT's current web page states up to 1.45 m — inconsistent with the official spec PDF; the PDF (rev. 2019) is taken as authoritative for mark 1/2 [S1][S2].) Weight 51 kg incl. batteries [S2]. Footprint 400x350 mm, support widened by three 75 mm castors [S2]. Structure ~50% polymer, 50% carbon fibre/metal — key to the cost target [S3]. Fully closed covers, no pinch points [S2].

## Locomotion
Two driving wheels (diff-drive) + three pivoting castors; max speed software-limited to 0.6 m/s [S2]. Indoor flat-floor.

## Upper body & manipulation
Two 8-DoF arms; target payload 1 kg per arm at 0.6 m full stretch (more at shorter reach) [S2]. Torso height adjustment substitutes for arm lift. Hands: 4-DoF / 2-DoA underactuated, series-elastic actuation, distributed pressure sensors (IIT skin technology), joint encoders; fingertip force ~20 N; specifically designed to open doors (handles, push bars) [S1][S2]. Overload safety clutches in all arm joints [S2]. No tool changer / media at flange (n/a).

## Sensing
Head (2-DoF): Leopard Imaging OV580 twin-camera module, ASUS XtionPro Live RGB-D (upgradeable), 2 microphones, loudspeaker, programmable RGB LED matrix face [S2]. Arms: two 6-axis F/T sensors for active compliant control; IMUs (accelerometer+gyro) embedded in most motor boards for impact detection; pressure-sensitive skin on hands [S2]. Base: RoboPeak RPLidar [S2].

## Actuation & power
Electric actuators with series-elastic elements in hands; joint overload clutches; active force-torque control [S2]. Onboard battery in base, designed for ~3 h operation; 24 V + 12 V power buses [S2]. No hot-swap/dock disclosed.

## Compute & software
Two Nano-ITX i7 PCs + MYIR Xilinx Z-turn FPGA board; ASUS 5 GHz Wi-Fi AP onboard [S2]. Software: open-source YARP middleware (shared with iCub), ROS interface via bridges, Gazebo/RViz simulation; open APIs [S2]. Assistive intelligence developed in the open "assistive-rehab" framework (skeleton tracking, exercise coaching, speech interaction) [S4].

## Safety & compliance
Designed for safe HRI: joint safety clutches, compliant force-torque control, closed covers, e-stop "in conformance with ISO 13482" (vendor wording — conformance of the e-stop function, not a certified ISO 13482 robot) [S2, vendor-claimed]. No third-party certification found.

## Deployment evidence & traction
No commercial installs. Clinical/assistive traction: joint lab with Fondazione Don Carlo Gnocchi Onlus — R1 as rehabilitation assistant guiding upper-limb/torso exercises, developed and trialled in Don Gnocchi rehabilitation settings (assistive-rehab framework, ~2018-2022) [S4]; HR1 healthcare-assistant work published 2022 [S5]; concierge/museum demos; appearance at IIT 20th anniversary (Dec 2023) confirms platform still operational [S6]. Media splash at 2016 launch positioned it as a near-term consumer product — that never materialized (n/a on any sales figures).

## Assessment (analyst view)
(Analyst opinion.) Strengths: genuinely cost-optimized design (polymer structure, simplified 2-DoA hands, diff-drive), full compliant-control and skin sensing pedigree from iCub, open software ecosystem, real clinical-partner use cases. Weaknesses: very low arm payload (1 kg), 0.6 m/s, research-grade reliability; institutional owner with no commercial channel — after 10 years R1 remains a prototype family, and IIT's attention moved to legged ergoCub. Threat to a new EU entrant: none commercially; strategically useful as design-for-cost case study and as proof that the "affordable semi-humanoid" concept needs a company, not an institute, to reach the market.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://icub.iit.it/products/r1-robot | Overview, 8-DoF arms, hand sensors, cost target, (1.45 m claim — conflicting) | vendor-claimed |
| 2 | https://www.iit.it/documents/175012/528824/Technical_Specification_R1_20200531.pdf | Official spec rev. 2019: 1.2 m / 1.15-1.35 m, 51 kg, 400x350 mm, 0.6 m/s, 1 kg payload, hands 4-DoF/2-DoA/20 N, sensors, 2x i7 + Xilinx, 3 h battery, YARP/ROS, ISO 13482-conform e-stop | vendor-claimed |
| 3 | https://opentalk.iit.it/en/r1-is-born-the-first-robot-by-iit-specifically-designed-for-applications-in-domestic-and-professional-environments/ | 2016 launch, 50% plastic, domestic/professional positioning | vendor-claimed |
| 4 | https://robotology.github.io/assistive-rehab/doc/mkdocs/site/ | Don Gnocchi joint lab, rehab use cases | vendor-claimed |
| 5 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8860235/ | HR1 healthcare assistant (2022, peer-reviewed) | third-party |
| 6 | https://opentalk.iit.it/en/a-new-robot-for-the-first-20-years-of-iit/ | R1 at IIT 20th anniversary; ergoCub 150 cm / 55.7 kg / ~10 kg loads (context) | vendor-claimed |
