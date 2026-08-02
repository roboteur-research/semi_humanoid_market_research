# AMIGO (+ SERGIO) — Tech United, TU Eindhoven (T3 compact)

> AMIGO ("Autonomous Mate for IntelliGent Operations", ~2010) was TU Eindhoven's open-hardware domestic service semi-humanoid: four omni wheels, spindle-lift torso (1.00-1.35 m), two Philips PERA arms (1.5 kg lift each), Kinect head. RoboCup@Home Dutch Open winner 2012, world runner-up 2014; retired after the team moved to a Toyota HSR ("HERO"). Historical relevance only.

| Field | Value |
|---|---|
| Company | Tech United, TU Eindhoven (CST group) |
| HQ | Eindhoven, Netherlands |
| Status (2026) | discontinued (retired; successor SERGIO also retired; team now on Toyota HSR "HERO") |
| First shown / launch | ~2010-2011 |
| Target applications | Domestic service / care research, RoboCup@Home |
| Price | n/a (self-built; open hardware CERN OHL v1.1 except arms) |
| Availability | None (CAD/drawings still published) |

Specs (from the Robotic Open Platform wiki, all vendor-claimed): dimensions 100-135 x 65 x 65 cm (spindle torso lift gives 35 cm height range); weight ~80 kg; base with four omni wheels housing batteries and electronics; 4x Makita 24 V NiMH batteries (3.3 Ah each) — autonomy only 15 min active / 30 min normal use; three AOpen i5 PCs (8 GB each), EtherCAT 1 kHz control network; Microsoft Kinect head plus Hokuyo UTM-30LX lidar; Rode directional microphone, JBL speaker [S1]. Arms: two Philips Experimental Robotic Arms (PERA — commercially bought, not open-sourced): 4 arm + 3 wrist DoF + 1-DoF gripper (90 mm opening), 1.5 kg liftable force with straight arm, upper arm 320 mm / forearm 280 mm [S1]. Software: Ubuntu + ROS (C++/Python) [S1]. Competition record: Dutch Open champion 2012; 2nd place RoboCup@Home world championship 2014 (João Pessoa, Brazil); demonstrator in EU RoboEarth (cloud-robotics knowledge sharing) and Bobbie Robotics projects [S2][S3]. Successor SERGIO (~2014) reused the concept with improved hardware; both were retired when Tech United migrated its @Home software stack to the Toyota HSR "HERO" (world champion 2019 and 2022), confirming the pattern of academic teams switching to commercial platforms [S3][S4].

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://wiki.roboticopenplatform.org/wiki/AMIGO (accessed via web.archive.org; live page restricted to TU/e network) | Full hardware specs, PERA arms, batteries, compute, CERN OHL | vendor-claimed |
| 2 | https://robots.ros.org/ (AMIGO entry) | Acronym, RoboEarth/Bobbie demonstrator, ROS | third-party |
| 3 | https://www.tue.nl/en/our-university/community/tech-united | Dutch Open 2012, 2nd place worlds 2014, HERO migration | vendor-claimed (university) |
| 4 | https://link.springer.com/chapter/10.1007/978-3-031-28469-4_22 | AMIGO/SERGIO → HSR software migration; 2022 world title | third-party (peer-reviewed) |
