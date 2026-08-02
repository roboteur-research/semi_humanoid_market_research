# TORA-ONE — PaXini Tech (帕西尼)

> TORA-ONE is PaXini's tactile-first wheeled humanoid: a telescoping 1.46–1.86 m dual-arm robot whose defining feature is whole-hand/whole-body multi-dimensional tactile sensing — 2,280 self-developed ITPU units across 6,840 signal channels, with 0.01 N-class force control in its DexH-series hands — driven by a vision-tactile-language-action (VTLA) model. First shown 2023/2024 and now in its second generation, it is the clearest demonstration that Chinese vendors are competing on sensing richness, not just DoF counts, and PaXini doubles as a tactile-sensor/hand supplier to the rest of the industry.

| Field | Value |
|---|---|
| Company | PaXini Tech (帕西尼感知科技) |
| HQ | Shenzhen, China |
| Status (2026) | shipping (listed as commercially purchasable; volumes undisclosed — pilots) |
| First shown / launch | 1st gen 2023 (industry-first tactile humanoid claim); TORA-ONE current gen announced 2024, pilots since |
| Target applications | Warehousing/logistics, medical & eldercare, industrial manufacturing, commercial service, home assistance |
| Price | n/a (not disclosed) |
| Availability | China, direct; "available for purchase" per official site [S2] |

## Design & morphology
Wheeled humanoid with collapsible/telescoping torso: height 1.46 m folded to 1.86 m extended [S2]. Body DoF 21 (excl. hands); hands 16 DoF each (13 active + 3 passive) = 32 → 53 DoF total current-gen [S2]. (Earlier gen / discovery notes cite 47 DoF = 21 + 26 with 13-DoF DexH13 hands — superseded by current 16-DoF hands.) Max arm length 96.5 cm [S2]. Weight: n/a (not disclosed).

## Locomotion
Wheeled base, laser-SLAM autonomous navigation; max 0.6 m/s linear / 0.4 rad/s rotation; 2 cm obstacle / 2 cm gap clearance; 7° gradeability; positioning repeatability 1.5 cm (3 cm absolute, 3° heading) [S2].

## Upper body & manipulation
- Arms: dual, 5 kg nominal payload each; repeatability ±0.5 mm [S2].
- Hands: DexH-series bionic dexterous hands, 16 DoF (13 active + 3 passive) each; 0.01 N high-precision force control; 5 kg hand load; >100,000-cycle durability [S1][S2].
- Tactile: 2,280 ITPU multi-dimensional tactile units, 6,840 signal channels, 15 tactile modalities (normal/shear force, texture, slip etc.) across hands/body [S2].

## Sensing
Vision: 5 RGB cameras (3 head + 2 hands) + 2 RGBD (1 head + 1 base); base laser lidar [S2]. Tactile as above — the densest tactile suite claimed on any commercial humanoid. 6D object-pose recognition [S2].

## Actuation & power
Actuators: n/a (not disclosed). Battery 40 Ah; ~6 h charge; 8 h continuous runtime [S2].

## Compute & software
VTLA-Model — vision-tactile(-language)-action multimodal model for grasp planning and force-controlled manipulation [S2]. Onboard compute, SDK/ROS: n/a (not disclosed).

## Safety & compliance
n/a (not disclosed). Force-controlled compliant grasping implied by tactile stack (vendor-claimed).

## Deployment evidence & traction
- Pilots across warehousing/industrial/commercial scenarios claimed; no named customers found (vendor-claimed) [S2].
- PaXini hands/sensors ship to third-party robot makers (supplier traction, third-party) [S3].
- JD.com strategic investment (A round) suggests logistics-scenario pull (third-party) [S3].
- Unit counts: n/a (not disclosed).

## Assessment (analyst view)
*Analyst opinion.* Strengths: unmatched tactile density and force-control granularity at a believable cost point (¥199 fingertip sensors), a dual business model (component supplier + robot OEM) that funds itself even if the humanoid stalls, and a >RMB 10B-valuation war chest. Weaknesses: mobility and arm specs are mid-tier (0.6 m/s, 5 kg/arm, ±0.5 mm), no named robot deployments, and the whole-robot product looks like a technology showcase for the sensor business. Threat to an EU entrant: direct competition is moderate, but PaXini raises the manipulation bar industry-wide — and is simultaneously a potential component partner an EU builder could buy hands/tactile skin from rather than compete with.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.paxini.com/product/dex | DexH13 hand: 13 DoF, 0.01N, 5kg, 100k cycles | vendor-claimed |
| 2 | https://www.paxini.com/cn/robot | TORA-ONE full specs (53 DoF, 2280 ITPU/6840 ch, 1.46-1.86m, nav, cameras, 40Ah/8h, VTLA) | vendor-claimed |
| 3 | lite.duckduckgo.com aggregate (funding/press) | JD A-round, ¥1B+ B-round @ ¥10B+ val, sensor cost, supplier role, 2023 first-gen claim | third-party |

*Unknown fields = n/a (not disclosed).*
