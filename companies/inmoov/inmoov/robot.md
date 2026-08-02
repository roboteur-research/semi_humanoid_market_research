# InMoov — open source (Gaël Langevin)

> InMoov is the first open-source life-size 3D-printed humanoid: head, torso and two arms with five-fingered tendon-driven hands, printable on any 12 cm-bed hobby printer, driven by hobby servos and Arduino, and controlled with MyRobotLab. Since 2012 it has been built worldwide (~under $1,000 in parts plus printing); it has no legs, and the community's standard mobility solution is a DIY wheeled base — making it the archetype of the hobbyist wheeled semi-humanoid. Licence is CC BY-NC (non-commercial), which deliberately blocks commercial productization.

| Field | Value |
|---|---|
| Company | Open-source project (Gaël Langevin, FR) |
| HQ | Paris, France / global community |
| Status (2026) | shipping (open files; actively maintained with i2 part revisions) |
| First shown / launch | Hand 2011/2012 (Thingiverse); full torso developed 2012-2015 |
| Target applications | Education, maker/hobbyist builds, HRI and prosthetics-adjacent research, exhibitions |
| Price | Commonly cited under $1,000 in components + filament (third-party, 2013 figure; realistic builds higher) |
| Availability | Worldwide STL/instructions downloads; no official kit (CC BY-NC restricts commercial kits) |

Design: life-size upper body — articulated head (eyes with cameras, jaw), neck, torso with waist rotation, two arms with 5-finger hands using tendon-driven fingers (the hand began as the first open-source 3D-printed prosthetic-style hand) [S1][S2]. Actuation: standard hobby servos throughout (~30+ servos in a full build, estimated); electronics: Arduino Mega with the project's "Nervo Board" breakout [S1]. Software: MyRobotLab (Java) with gesture recording, speech recognition/synthesis; ROS integrations exist; sensors optional (PIR, ultrasonic, Kinect, Leap Motion, Neopixel) [S1]. Mobility: no legs (a non-motorized leg kit exists for display); builders commonly mount the torso on custom wheeled bases [S2]. No payload/safety specs — it is a display/education platform, not a working manipulator. Deployment evidence: thousands of builds worldwide (builder map, galleries, schools/universities); countless derivative projects over 14 years [S1][S2] (third-party corroborated).

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://inmoov.fr/ | Design, hardware/software, variants, community | vendor-claimed |
| 2 | https://en.wikipedia.org/wiki/InMoov | History, CC BY-NC, Arduino, wheeled builds (lead photo) | third-party |
| 3 | https://www.cnn.com/2013/01/25/tech/innovation/inmoov-robot-3d-printing/index.html | Sub-$1,000 build cost | third-party |
