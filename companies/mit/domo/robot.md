# Domo — MIT CSAIL

> Domo (2004-07) was Aaron Edsinger's compliant dual-arm upper-torso humanoid at MIT CSAIL: series-elastic, force-controlled in every joint, built to manipulate in unstructured human environments. Its design DNA went straight into Meka Robotics and, later, Hello Robot. Retired.

| Field | Value |
|---|---|
| Company | MIT CSAIL Humanoid Robotics Group (advisor Rodney Brooks) |
| HQ | Cambridge, MA, USA |
| Status (2026) | discontinued (PhD platform, retired ~2007) |
| First shown / launch | 2004 (build); PhD work through 2007 |
| Target applications | force-controlled manipulation research in human environments (shelving objects, handing items, tool use with humans) |
| Price | n/a (one-off; sponsored by Toyota + NASA) |
| Availability | n/a |

Domo was a stationary upper torso with 29 active DoF: two 6-DoF arms and a 2-DoF neck driven entirely by Series Elastic Actuators, plus two 4-DoF hands with Force Sensing Compliant actuators — force control everywhere, a radical choice in 2004 [S1]. It stood 86 cm (34 in) with a 168 cm arm span and weighed just 19 kg (42 lb); sensing included stereo Point Grey and Videre camera pairs, a 3-axis gyro, 24 tactile sensors and 49 potentiometers, controlled by 5 embedded DSPs at 1 kHz over CAN, with a 15-node Linux cluster (YARP-based) off-board [S1]. Edsinger and mechanical collaborator Jeff Weber used it to demonstrate behavior-based, contact-tolerant manipulation — placing objects on shelves, working cooperatively with a person — documented in the 2007 dissertation "Robot Manipulation in Human Environments" [S1][S2]. The project's stated commercial offshoot is Meka Robotics (Edsinger/Weber), acquired by Google in 2013; Edsinger later founded Hello Robot [S1].

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://people.csail.mit.edu/edsinger/domo.htm | full specs, sponsors, lineage | vendor-claimed (lab page) |
| 2 | https://en.wikipedia.org/wiki/Domo_(robot) | project summary | third-party |
