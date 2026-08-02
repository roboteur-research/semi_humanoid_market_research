# AILA — DFKI Robotics Innovation Center Bremen (T3 compact)

> AILA ("Artificial Intelligence Lightweight Android", ~2010) was DFKI Bremen's female-styled mobile dual-arm research robot: 32 DoF, two lightweight 7-DoF arms (payload-to-weight ratio >1), 4-DoF torso, 2-DoF head, on a six-wheeled omnidirectional base. Used in SemProM, BesMan, HySociaTea and Robofoot projects (2010-2016); now retired. Relevant only as German research heritage in wheeled dual-arm manipulation.

| Field | Value |
|---|---|
| Company | DFKI Robotics Innovation Center |
| HQ | Bremen, Germany |
| Status (2026) | discontinued (research platform, "not actively used anymore" per DFKI) |
| First shown / launch | ~2010 (design paper ICRA 2011) |
| Target applications | Research: mobile dual-arm manipulation, logistics/product handling (RFID), space-analog demos |
| Price | n/a (never for sale) |
| Availability | None (retired) |

AILA measured 1.15 x 0.75 x 1.70 m with 32 DoF: two 7-DoF lightweight arms designed for a payload-to-weight ratio greater than one, a 4-DoF adjustable torso extending the dual-arm workspace, a 2-DoF head, and a mobile base with six wheels, each wheel a 2-DoF module (drive + steer — omnidirectional) [S1][S2]. Wrists carried two 6-axis force/torque sensors; perception included a Prosilica GC780C stereo pair in the head, a Mesa SR-4000 time-of-flight 3D camera, a chest-mounted short-range Hokuyo URG scanner, two long-range Hokuyo UTM scanners around the base, and a Skyetek M4 RFID reader (for the SemProM semantic-product-memory scenario) [S1]. Control ran over five CAN buses (arms, torso, wheels) and Gigabit Ethernet linking three onboard computers [S2]. Projects: SemProM (RFID product handling), Robofoot (2010-2013), BesMan (2012-2016, mobile manipulation incl. ISS-mockup tasks and SpaceBot Cup), HySociaTea (2014-2016, human-robot teamwork) [S1]. The platform is retired; DFKI's humanoid work moved toward space systems and exoskeletons.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://robotik.dfki-bremen.de/en/research/robot-systems/aila | Dimensions, DoF breakdown, sensor suite, projects, retired status | vendor-claimed |
| 2 | https://ieeexplore.ieee.org/document/5979775/ (AILA — design of an autonomous mobile dual-arm robot, ICRA 2011) | 32 DoF, lightweight arm design goal, CAN/Ethernet architecture, wrist F/T sensors | vendor-claimed (peer-reviewed) |
| 3 | https://robotsguide.com/robots/aila | Independent profile (fetch blocked; listed for reference) | third-party |
