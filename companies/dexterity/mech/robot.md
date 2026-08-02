# Mech — Dexterity, Inc.

> Mech is Dexterity's "industrial superhumanoid": two Kawasaki-built 7-axis-class arms with a patented extra shoulder/second-elbow joint mounted on an omnidirectional, ramp-climbing rover packed with up to 16 cameras, dual vacuum pumps and an onboard AI supercomputer. It lifts 60 kg dual-arm, reaches above 2.4 m, spans 5.4 m, and works outdoors at loading docks in 0-50°C — specs that put it in a payload/reach class of its own among wheeled semi-humanoids. Launched March 2025 for truck loading, with Sanmina contract-manufacturing for scale, it is the reference "heavy logistics" competitor in the category.

| Field | Value |
|---|---|
| Company | Dexterity, Inc. |
| HQ | Redwood City, California, USA |
| Status (2026) | shipping (available to industrial/enterprise customers; pilots + contract manufacturing ramp) |
| First shown / launch | Announced 2025-03-17/18 [S1] |
| Target applications | Truck loading/unloading, palletizing, depalletizing, order picking from racks, multi-station box/parcel/polybag workflows |
| Price | n/a (not disclosed; enterprise quotes) [S2] |
| Availability | US-first, direct enterprise sales; task capabilities delivered as software apps (truck-loading app first, more through 2025+) [S1][S2] |

## Design & morphology
- Two industrial arms (manufactured by Kawasaki, precision components by HiWin) on an "ultra-compact" four-wheeled rover base [S2, vendor-claimed].
- Patented shoulder plus "second elbow" per arm for dexterity in tight trailer/container spaces [S2, vendor-claimed].
- Armspan 5.4 m; vertical reach "safely extends beyond 2.4 m" — can place boxes 8 ft high at the top of box trucks and build multiple tall stacks simultaneously [S1][S2].
- Mast with lighting and overhead sensors above the base (visible in official imagery) [S5].
- Height/weight/footprint figures: n/a (not disclosed).

## Locomotion
- Four independently steerable wheels: moves, spins, strafes and climbs ramps [S2, vendor-claimed].
- Navigates autonomously between workstations across warehouses and industrial yards; "press of a button" task start [S1].
- Speed: n/a (not disclosed).

## Upper body & manipulation
- Payload: 60 kg lift with both arms (130 lb total; ~65 lb / 29 kg per arm per launch coverage) [S1][S2].
- Handles boxes, parcels and polybags — including "crushable" packages — and packs them into tight crevices [S1][S2].
- End-effectors: vacuum suction-cup array grippers fed by dual onboard vacuum pumps in the rover (green multi-cup arrays visible in official photos) [S2][S5].
- Force control: ultra-low-latency 4 kHz torque control in the arms + "industry-first AI-driven sense of touch and pressure" for gentle, human-level industrial manipulation [S2, vendor-claimed].

## Sensing
- Up to 16 onboard cameras (rover + mast) for picking, pack-strategy planning and navigation [S1][S2].
- "The world's most sophisticated sensor and safety package" in the rover (vendor language; details not disclosed) [S2].
- Touch/pressure sensing via AI-driven force estimation with 4 kHz torque loops [S2].

## Actuation & power
- Industrial servo arms (Kawasaki; HiWin motion components); 10+ years mean time between failures claimed for the arms [S2, vendor-claimed].
- Onboard battery pack in rover; capacity/runtime n/a (not disclosed) [S2].
- Environmental envelope: 0-50°C (32-122°F), up to 1,500 m altitude, up to 90% humidity — i.e. outdoor dock and non-climate-controlled warehouse capable [S1][S2].

## Compute & software
- Onboard "AI supercomputer" in the rover; runs stand-alone (edge) or cloud-connected [S2].
- Dexterity Physical AI: 68+ autonomous skill agents (perception, motion planning, force control) orchestrated in real time; "hundreds of AI models" per launch coverage; each agent independently interpretable [S1][S2].
- New tasks delivered as installable software apps on the same hardware (truck-loading app at launch) [S1].
- Fleet supervision: one associate can manage/monitor up to 10 Mechs simultaneously [S1].

## Safety & compliance
- Vendor claims a comprehensive rover "sensor and safety package"; industrial setting implies ANSI/RIA R15.08 / ISO 10218-2:2025 relevance, but no specific certifications published (n/a, not disclosed) [S2].
- Statically stable base; designed to work in human workspaces at brownfield sites [S1][S2].

## Deployment evidence & traction
- Launched to industrial and enterprise customers for truck loading, 03/2025; new apps rolled out through 2025 [S1, vendor-claimed].
- Sanmina contract manufacturing partnership (2025-10-22): assembly + test at Sanmina California facilities, NPI/supply-chain/quality services, to "significantly scale" Mech delivery to parcel, ground logistics, e-commerce, retail and air-cargo customers [S3][S4, vendor + third-party].
- Predecessor traction: DexR dual-arm truck unloader deployed at loading docks (basis for FedEx-linked truck-loading trials reported in 2023) [S1, third-party; FedEx link estimated].
- Unit counts: n/a (not disclosed).
- Funding signal: $95M raised 03/2025, $1.65B valuation [S1, third-party].

## Assessment (analyst view)
*Analyst opinion.* Strengths: category-leading payload (60 kg) and reach (2.4 m+/5.4 m span), outdoor-rated environmental envelope, credible industrial supply chain (Kawasaki arms, HiWin, Sanmina assembly), a pragmatic software-app business model, and honest anti-hype positioning backed by production KPIs. Weaknesses: heavy, expensive, suction-only manipulation limits it to box/parcel flows; no price transparency; unit deployment numbers still undisclosed, suggesting early-ramp stage. Threat to a new EU entrant: high in logistics — any EU wheeled-humanoid pitch to parcel/3PL customers will be benchmarked against Mech's throughput and 1:10 supervision ratio; low outside logistics, where Mech does not play. An EU entrant should avoid contesting heavy truck loading head-on and instead exploit Mech's absence in lighter, dexterity-centric and service applications — or in CE-marked, Machinery-Regulation-2023/1230-ready packages for European sites.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.therobotreport.com/dexterity-launches-mech-dual-armed-mobile-manipulator-for-truck-unloading/ | launch date, 130 lb/65 lb per arm, 8 ft placement, 16 cameras, 32-122°F, 1:10 operator ratio, apps, $95M @ $1.65B, DexR, Menon quote | third-party |
| 2 | https://dexterity.ai/mech | 60 kg / 5.4 m span / >2.4 m reach, patented shoulder + second elbow, 4 kHz torque + touch, 68+ skill agents, Kawasaki/HiWin, 10y MTBF, 0-50°C/1500 m/90% RH, rover (4 steerable wheels, dual vacuum pumps, supercomputer, battery, 16 cameras), edge/cloud, made in California | vendor-claimed |
| 3 | https://dexterity.ai/blog/dexterity-and-sanmina-deepen-partnership-to-scale-mech-superhumanoids | Sanmina deal 2025-10-22, CA assembly, customer segments | vendor-claimed |
| 4 | https://www.robotics247.com/article/dexterity_sanmina_partner_to_scale_mech_superhumanoid_mmr_production | Sanmina deal corroboration | third-party |
| 5 | images/mech-enhanced.jpg + images/gripper.jpg (official dexterity.ai assets) | visual: dual Kawasaki arms, green suction-array grippers, blue rover, sensor mast | third-party (photo evidence) |
