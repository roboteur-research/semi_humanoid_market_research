# PR2 (Personal Robot 2) — Willow Garage

> The PR2 (2010) is the seminal wheeled dual-arm research platform: omnidirectional base, telescoping spine, two compliant 7-DoF arms, and ROS as its native software. Sold at $400k to roughly 50 institutions, it never was a commercial product — but it defined the semi-humanoid morphology and created the ROS ecosystem every modern competitor builds on.

| Field | Value |
|---|---|
| Company | Willow Garage |
| HQ | Menlo Park, CA, USA |
| Status (2026) | discontinued (sales ended 2014; Clearpath support ran through ~2016; some units still alive in labs) |
| First shown / launch | prototypes late 2008; Beta Program May 2010; on sale Sept 2010 |
| Target applications | robotics research: mobile manipulation, household tasks, HRI, ROS development |
| Price | USD 400,000 (two-arm); USD 285,000 single-arm "PR2 SE"; $120k open-source discount available [S1] |
| Availability | discontinued; ~11 beta units gifted + commercial sales to labs worldwide |

## Design & morphology
Omnidirectional wheeled base (66.8 × 66.8 cm footprint) with a 1-DoF telescoping spine raising the shoulders; overall height up to 165 cm extended, weight 226.8 kg [S1]. 20 actuated DoF above the base: 2 arms × (4 arm + 3 wrist + 1 gripper), head pan/tilt (2), laser tilt (1), spine (1) [S1]. Arms use passive spring counterbalance for gravity compensation, making them backdrivable and safe-ish around humans; ~1.8 kg payload per arm (est.).

## Locomotion
Four steered/driven caster modules give holonomic omnidirectional motion; max speed 3.6 km/h (1 m/s) [S1]. Flat indoor floors only; 226.8 kg mass makes it strictly a lab robot.

## Upper body & manipulation
Two 7-DoF arms (4 DoF arm + 3 DoF wrist) with 1-DoF parallel grippers; fingertip pressure-sensor arrays; forearm Ethernet cameras and 3-axis accelerometers in grippers for contact events [S1]. Continuous-rotation wrists. Famous manipulation milestones: opening doors and plugging itself into wall outlets (2009), Berkeley towel folding (2010), fetching beer, baking cookies, making lattes (2015) [S1][S4].

## Sensing
Head: wide- and narrow-angle stereo pairs, 5 MP camera, LED texture projector, later Microsoft Kinect standard; tilting Hokuyo UTM-30LX laser on torso; second Hokuyo UTM-30LX on base; Microstrain 3DM-GX2 IMU [S1].

## Actuation & power
32 brushed DC motors with harmonic/gear transmissions; spring counterbalanced arms. 1.3 kWh Li-ion pack (16 laptop-style battery modules), ~2 h runtime; can autonomously plug itself in (demo) [S1].

## Compute & software
Two onboard servers, each with quad-core Intel Xeon i7, 24 GB RAM total, 500 GB + 1.5 TB removable storage [S1]. Software: ROS + full open stack (navigation, MoveIt-precursor arm_navigation, OpenCV, PCL). The PR2 was ROS's reference platform; hundreds of papers and packages target it.

## Safety & compliance
No certifications; research use only. Runstop (wireless e-stop), current-limited backdrivable counterbalanced arms as intrinsic mitigations. Never intended for unsupervised deployment.

## Deployment evidence & traction
11 institutions received free Beta units (2010: Stanford, MIT, Berkeley, TUM, Freiburg, Tokyo, etc.); total build commonly cited around 50 units across top labs worldwide (third-party estimates vary 40-60) [S1][S3]. Enormous research output; iconic demos (towel folding, Subway sandwich fetch by Tokyo researchers) [S1]. Clearpath Robotics provided spares/support from Jan 2014 through ~2016 [S2]. No commercial deployments ever.

## Assessment (analyst view)
*Analyst opinion.* PR2 validated the exact morphology most 2024-26 semi-humanoids use, a decade early, and its failure mode is instructive: superb engineering at a price ($400k) and weight (227 kg) that capped the market at ~50 research labs. Its true legacy — ROS — lowers barriers for every new entrant today, including EU ones. Threat level: none directly (defunct), but expect customers and hires to benchmark any new wheeled dual-arm platform against "a modern PR2 at 1/10th the price"; the platforms that inherited its niche (TIAGo++, Fetch, Stretch, ALOHA-class rigs) show the research market clears at $20-100k, not $400k.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://robotsguide.com/robots/pr2 | full specs, DoF, sensors, price, history, beta program | third-party (IEEE) |
| 2 | https://www.therobotreport.com/clearpath-robotics-takes-over-pr2-support/ | Clearpath support 2014-2016 | third-party |
| 3 | https://en.wikipedia.org/wiki/Willow_Garage | unit counts, program history | third-party |
| 4 | https://spectrum.ieee.org/pr2-robot-figures-out-how-to-make-a-latte | late-life research demos | third-party |
