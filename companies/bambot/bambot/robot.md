# BamBot (B0) — open source (Tim Qian)

> BamBot is a ~$300 open-source wheeled dual-arm mini semi-humanoid by Tim Qian: two SO-ARM100-style arms of Feetech STS3215 bus servos plus 3D-printed parts on a differential wheeled base, controllable from a web browser via the creator's feetech.js library and LeRobot-compatible for imitation learning. First demoed March 2025, ~950+ GitHub stars. It is the cheapest notable entry in the hobbyist semi-humanoid tier and a direct ancestor credited by XLeRobot.

| Field | Value |
|---|---|
| Company | Open-source project (Tim Qian) |
| HQ | n/a (global community) |
| Status (2026) | shipping (open BOM self-build; active) |
| First shown / launch | 2025-03 (demo video on X) |
| Target applications | Education, hobbyist embodied-AI experiments, web-based robotics teaching |
| Price | ~$300 in parts (vendor-claimed) [S2] |
| Availability | Worldwide (open CAD + BOM; no official kit) |

Design: variant B0 places two SO-ARM100-derived 6-DoF arms (Feetech STS3215 serial-bus servos) and a camera on a 3D-printed torso over a wheeled base (B0-base variant); all CAD and assembly docs in the repo [S1][S2] (vendor-claimed, verifiable open design). Software: feetech.js drives the servos directly from the browser (WebSerial) — bambot.org offers in-browser 3D simulation and teleoperation of BamBot and other models (SO-ARM100, Unitree Go2/G1); LeRobot-compatible for dataset collection and policy training [S1][S2]. No battery/runtime/payload specs published; no safety certification (desk-scale hobby platform). Traction: ~956 stars / 93 forks, Discord and WeChat communities, viral demo March 2025 [S2]. Competitive note: BamBot, Lekiwi and SO-101 form the lineage on which XLeRobot builds; together they anchor the open-source end of the semi-humanoid spectrum.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://bambot.org | Variants, browser sim/control | vendor-claimed |
| 2 | https://github.com/timqian/bambot | ~$300 price, STS3215/3D-printed hardware, Apache 2.0, community stats | vendor-claimed (open repo) |
