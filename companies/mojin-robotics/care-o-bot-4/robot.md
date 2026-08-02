# Care-O-bot 4 ("Paul") — Mojin Robotics / Fraunhofer IPA

> Care-O-bot 4 is the fourth generation of Fraunhofer IPA's modular omni-wheeled service humanoid, commercialized by IPA spin-off Mojin Robotics and best known as "Paul", the Saturn electronics-store greeter deployed from 2016. With spherical torso/neck joints, optional dual 7-DoF arms and a fully modular kit architecture, it was Europe's flagship social/service semi-humanoid of the 2015-2020 era — now commercially discontinued after Mojin's 2023 pivot into AMRs (as 4am Robotics), but still relevant as the benchmark for what modular German service humanoids achieved and where the business model failed.

| Field | Value |
|---|---|
| Company | Mojin Robotics (→ 4am Robotics GmbH); platform by Fraunhofer IPA |
| HQ | Stuttgart, Germany |
| Status (2026) | discontinued (commercial); legacy research platform at Fraunhofer IPA |
| First shown / launch | 2015 (platform); Oct 2016 ("Paul" retail deployment) |
| Target applications | Retail greeting/guidance, museum & airport information, hospitality, elderly-care assistance, fetch-and-carry |
| Price | USD 66,000–232,000 depending on configuration (historical) [S3] |
| Availability | No longer sold; was direct/project-based in DACH |

## Design & morphology
Modular stack: omnidirectional base, torso with patented ball-joint pivot, optional one/two arms, sensor ring, touchscreen head. Height 148–158 cm (config-dependent), footprint 72 × 72 cm, weight ~140 kg [S1][S3]. 23 DoF fully configured: base 2, 2×7-DoF arms, 2×2-DoF grippers, 2-DoF torso spherical joint, 1-DoF sensor ring [S3]. Spherical joints at hip and neck allow 360° head/torso rotation for expressive "body language" [S1]. Modules swappable — hand→tray, or base alone as serving trolley [S1].

## Locomotion
Omnidirectional wheeled base (6 Wittenstein motors), max speed 4.3 km/h (~1.2 m/s) [S3]. Indoor use.

## Upper body & manipulation
Optional one or two 7-DoF arms built from Schunk PowerBall modules (PRL100, ERB145, ERB115); 2-DoF one-finger-style grippers with integrated sensors [S3]. Payload not officially stated (Schunk PowerBall-class arms: ~5-6 kg est.). Fetch-and-carry, tray service, door opening demos.

## Sensing
Head touchscreen + cameras for face/gesture recognition, microphone for speech [S3]. Torso: three 2.5D depth sensors; sensor ring configurable with SICK Visionary-T ToF and Intel RealSense [S3]. Base: three safety laser scanners tied to a safety PLC [S3].

## Actuation & power
Electric: Wittenstein base motors, Schunk arm modules, 2 Maxon motors per spherical joint [S3]. 40 Ah li-ion pack, ~5 h autonomous operation (4–6 h range cited) [S3][S4].

## Compute & software
Multiple Intel i7 NUC PCs; Ubuntu Linux + ROS, Python control application [S3]. Care-O-bot ecosystem was a major early ROS contributor (cob_* packages, open research stack).

## Safety & compliance
Safety laser scanners + safety PLC on base (performance-level safety for mobile platform) [S3]. No public ISO 13482 certification for the full manipulator configuration; retail deployments ran greeter configs without arms or with limited arm use (estimated).

## Deployment evidence & traction
- "Paul" greeter at Saturn stores from Oct 2016 (Ingolstadt first; later additional Saturn/Media-Markt group stores) — multi-year, publicity-heavy retail deployment [S2].
- Museum, airport information and elderly-care trials in German projects (vendor/Fraunhofer) [S1].
- Total installed base: small numbers (single-to-low-double digits, estimated). No new deployments announced since ~2020; product no longer marketed after Mojin became 4am Robotics (Apr 2023) [S5].

## Assessment (analyst view)
*Analyst opinion.* Strengths (historical): genuinely modular architecture, expressive omni-wheeled design years ahead of its time, solid German industrial components (Schunk/SICK/Wittenstein) and deep ROS openness. Weaknesses: high price for low task value (greeting, guiding), no manipulation-driven ROI, and reliance on showcase customers; the line was quietly abandoned when the parent group chose AMR intralogistics revenue. Threat to a new EU entrant: none directly (discontinued), but it is the case study buyers in DACH remember — a new entrant pitching service humanoids in retail/care will meet skepticism calibrated by Paul, and should differentiate with hard manipulation ROI and modern AI autonomy.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.care-o-bot.de/en/care-o-bot-4.html | Modularity, spherical joints, applications, arm options | vendor-claimed |
| 2 | https://www.ipa.fraunhofer.de/en/press-media/press_releases/2016-11-06_Care-O-bot-4-celebrates-its-premiere-as-shopping-assistant.html | Paul at Saturn from Oct 2016 | vendor-claimed (Fraunhofer PR) |
| 3 | https://robotsguide.com/robots/careobot | 148 cm, 140 kg, 23 DoF, 4.3 km/h, sensors, actuators, compute, 40 Ah/5 h, $66k-232k | third-party |
| 4 | https://www.originofbots.com/robot/care-o-bot-4-by-fraunhofer-ipa-details-specifications-rating | 158 cm full config, 4-6 h runtime | third-party |
| 5 | https://www.scio-automation.com/update/4am/mojin-becomes-4am | Mojin → 4am Robotics renaming, AMR pivot (discontinuation evidence) | vendor-claimed (corporate) |
