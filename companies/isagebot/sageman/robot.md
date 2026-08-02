# SageMan / iSAGE STAR (赛智四臂人形机器人) — iSAGEBOT (Shanghai SAGE Intelligent Technology)

> The SageMan (also seen as "SageBot" / "iSAGE STAR-SageMan") is marketed as the world's first AI-powered FOUR-armed wheeled humanoid: 52 DoF, 156-181.5 cm telescoping height, 280 kg, four 7-axis force-controlled arms giving a 360° workspace and a claimed 4× throughput over dual-arm robots. It targets precision manufacturing (3C, semiconductor, biopharma, automotive parts) and represents the emerging Chinese "super-humanoid" (超人形) multi-arm category. A six-armed successor, MAHAKBOT, was teased in July 2026 with 100+ purchase LOIs claimed.

| Field | Value |
|---|---|
| Company | iSAGEBOT / Shanghai SAGE Intelligent Technology (智在无界/赛智) |
| HQ | Shanghai, China |
| Status (2026) | announced (pilots/"in development"; not yet shipping at scale) |
| First shown / launch | 2025 (four-arm SageMan); six-arm MAHAKBOT teased 2026-07-28 |
| Target applications | Precision assembly, 3C/semiconductor, biopharma lab automation, new energy, automotive parts, hazardous environments |
| Price | n/a (not disclosed) |
| Availability | China; direct/solution-integration sales; no published lead times |

## Design & morphology
Wheeled mobility platform carrying a symmetrical four-arm torso: 900 × 600 mm footprint, height 1,560 mm telescoping to 1,815 mm, 280 kg with battery [S1][S2]. 52 DoF total (vendor configurations quoted 28-56 DoF depending on arm/hand fit-out) [S1][S3]. Four arms arranged around the torso give a full 360° reach envelope without base rotation [S3].

## Locomotion
Wheeled base with multi-sensor-fusion navigation (built on the company's AMR heritage); speed, drive type and terrain limits n/a (not disclosed) [S1].

## Upper body & manipulation
Four 7-axis force-controlled arms; payload 3-16 kg per arm depending on configuration [S1]. Repeatability ±0.03 mm (best case), angular accuracy ±1°, torque control resolution 0.1 Nm — vendor-claimed millimetre-level assembly capability [S1][S3]. Dexterous hands offered; end-effector details and media at flange n/a (not disclosed).

## Sensing
Six-camera vision system for full-area scanning and 3D modelling; lidar; joint torque sensors [S1][S2]. Voice interaction supported.

## Actuation & power
Precision servo drives with harmonic gearing [S2]. Power supply SPS-6025: 54.6/54.75 V DC, 25 A max, 1,500 W rated [S1]; battery capacity/runtime n/a (not disclosed). Operating temperature 10-40 °C [S2].

## Compute & software
SageBrain controller (millisecond-class response) + SageOS real-time robot OS; supports plugging in external AI models (LLMs, VLAs) [S1][S2]. Control via voice, remote cloud and touchscreen. Closed-source stack [S2].

## Safety & compliance
n/a (not disclosed). No certification claims found.

## Deployment evidence & traction
Vendor lists solution work in new-energy, biopharma, automotive-parts and semiconductor industries from its AMR business [S1]. For the humanoids: third-party tracker Aparobot lists SageMan as "In Development" [S2]; the strongest traction signal is the claimed 100+ letters of intent for the six-armed MAHAKBOT gathered at the 12th China International Technology Fair, Shanghai (vendor-claimed via press) [S4][S5]. No confirmed paid deployments of the four-arm unit found. Confidence: vendor-claimed.

## Assessment (analyst view)
*Analyst opinion.* Strengths: genuinely differentiated multi-arm concept with a clear cycle-time argument (parallel tasking, 360° workspace, no base repositioning), strong precision claims (±0.03 mm), and an existing AMR customer base in exactly the target industries. Weaknesses: 280 kg mass and four-arm control complexity raise integration and safety hurdles; funding (pre-A scale as of 2023) looks thin for a program of this ambition; all traction is LOI-level. For an EU entrant the direct threat is low near-term, but the concept threat is real: if multi-arm "super-humanoids" set the productivity benchmark in Chinese 3C assembly, dual-arm semi-humanoid value propositions everywhere get repriced.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://en.sage-modi.com/ProductSeries/info.aspx?itemid=1322&lcid=15 | full spec set (dimensions, DoF, payload, accuracy, SageBrain/SageOS, power) | vendor-claimed |
| 2 | https://www.aparobot.com/robots/isage-star-sageman | 52 DoF, sensors, actuators, status "In Development" | third-party |
| 3 | https://mikekalil.com/blog/china-humanoid-summer-2025/ | "world's first four-armed humanoid", 360° reach, mm-level tasks | third-party |
| 4 | https://www.globaltimes.cn/page/202607/1367010.shtml | MAHAKBOT six-arm reveal 2026-07-28, ~120 DoF, 300mm lift, applications | third-party (state media) |
| 5 | Crunchbase / CB Insights profiles (Sage Intelligent) | founded 2017, AMR 2019, 100+ LOIs at CTIF | third-party |
