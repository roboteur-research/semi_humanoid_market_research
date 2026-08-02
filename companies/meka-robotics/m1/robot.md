# M1 Mobile Manipulator — Meka Robotics

> The Meka M1 (2011) was a commercial compliant dual-arm mobile manipulator for HRI research: holonomic omni base, torso, expressive head, two 7-DoF series-elastic arms with 5-DoF hands, ~$320-340k. Explicitly inspired by Georgia Tech's Cody; discontinued when Google acquired Meka in 2013.

| Field | Value |
|---|---|
| Company | Meka Robotics |
| HQ | San Francisco, CA, USA |
| Status (2026) | discontinued (company absorbed by Google 12/2013) |
| First shown / launch | Feb 2011 |
| Target applications | human-robot collaboration and mobile manipulation research |
| Price | USD 320,000-340,000 depending on configuration [S1][S2] |
| Availability | discontinued; a handful of units in labs |

M1 stacked Meka's module catalog into one robot: B1 holonomic omnidirectional base (46 × 67 cm footprint), torso, two A2 7-DoF SEA arms with torque control at every joint, H2 5-DoF underactuated hands, and the 9-DoF expressive S2 head with HD camera plus optional 3D/Kinect sensor — 33 DoF total, 160 cm tall, 165 kg, 3.6 km/h, 24 V 60 Ah battery (~1 h runtime) [S1]. Compute was three Core2 Duo machines running Ubuntu, ROS and the RTAI-based Meka M3 real-time framework [S1][S2]. It was among the first commercial ROS-native compliant mobile manipulators — cheaper than a PR2's $400k but still research-priced, and only a few sold before Google's December 2013 acquisition ended the product line [S3]. The related "Dreamer" (UT Austin HCRL) used Meka torso/arms with the S2 head in its distinctive white/blue anime styling.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://robotsguide.com/robots/m1 | full specs, $320k, Cody inspiration | third-party (IEEE) |
| 2 | https://spectrum.ieee.org/meka-robotics-announces-mobile-manipulator-with-kinect-and-ros | launch, $340k config, ROS/Kinect | third-party |
| 3 | https://spectrum.ieee.org/google-acquires-seven-robot-companies | Google acquisition | third-party |
