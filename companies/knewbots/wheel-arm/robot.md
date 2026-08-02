# KNEWBOTS 轮臂式机器人 (wheel-arm robot) — KNEWBOTS (晓悟智能)

> A 35-DoF dual-arm wheeled humanoid from ThunderSoft-backed AMR maker KNEWBOTS: 7-DoF arms (4.5 kg each), height-adjustable 1.28-1.63 m torso on a wheeled logistics chassis, LLM task planning over real-time motion control. Minor vendor; exemplifies the Chinese "轮臂式" (wheel-arm) category of AMR companies moving up into manipulation.

| Field | Value |
|---|---|
| Company | KNEWBOTS (晓悟智能), Hangzhou; ThunderSoft-backed |
| HQ | Hangzhou, China |
| Status (2026) | announced (small-scale; demo/pilot stage) |
| First shown / launch | ~2025-26 (product page current 2026) |
| Target applications | Retail/showroom guidance, substation inspection, end-of-line sorting, box handling, line-side material transfer/replenishment |
| Price | n/a (not disclosed) |
| Availability | China, direct/solution sales |

| Spec | Value | Confidence |
|---|---|---|
| Base type | wheeled AMR chassis (company's logistics-robot heritage) | vendor-claimed [S1] |
| Height | 1,280-1,630 mm (adjustable torso lift) | vendor-claimed [S1] |
| Weight | 88 kg | vendor-claimed [S1] |
| DoF | 35 integrated joints; dual 7-DoF arms | vendor-claimed [S1] |
| Payload | 4.5 kg per arm; dexterous hand rated 3 kg | vendor-claimed [S1] |
| Arm span | 600 mm | vendor-claimed [S1] |
| Sensors | dual RGBD cameras on base + one on head; 6-axis force sensors; 4-mic linear array | vendor-claimed [S1] |
| Compute | Intel i7-1355U control unit + NVIDIA Orin AGX 275 TOPS (development config) | vendor-claimed [S1] |
| Battery | ~4 h runtime, 2 h charge; WiFi 6/Ethernet/Bluetooth | vendor-claimed [S1] |

KNEWBOTS' wheel-arm robot mounts a dual-arm humanoid torso (with waist articulation and height adjustment) on the company's wheeled AMR base, inheriting its navigation and fleet-scheduling stack [S1]. The differentiating pitch is "multi-robot unified control" — the humanoid is scheduled alongside latent and forklift AMRs in one system — plus "brain collaboration" pairing LLM task planning with real-time motion control [S1]. Payloads (4.5 kg/arm) and the 275-TOPS Orin option place it in the light industrial/commercial pilot class. Parent ThunderSoft (中科创达) is a major robotics software/module supplier, which explains the strong compute/software framing [S2]. No deployments, unit counts or prices are public; status is best treated as announced/small-scale.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.knewbots.com/wheelarm-robot/ | all specs, applications, control architecture | vendor-claimed |
| 2 | https://www.thundersoft.com/robotics/ | ThunderSoft parent, robotics platform heritage | vendor-claimed |
