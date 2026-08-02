# Dex — Richtech Robotics

> Dex is Richtech's first mobile humanoid: the dual-arm precision of its ADAM service-robot line mounted (with a telescoping neck/torso) on the AMR technology of its Titan delivery series, accelerated by an NVIDIA Jetson Thor and trained through an Isaac Sim "Sim2Real" pipeline. Unveiled 2025-10-28 and demonstrated assembling baseball caps at NVIDIA GTC DC and at CES 2026, it targets light/medium industrial work — machine operation, part sorting, inspection, packaging. It matters as a US public-company entry into wheeled industrial semi-humanoids on NVIDIA's reference stack, though as of late 2025 it still awaited its first customer announcement.

| Field | Value |
|---|---|
| Company | Richtech Robotics (Nasdaq: RR) |
| HQ | Las Vegas, NV, USA |
| Status (2026) | announced (demos at GTC DC 10/2025, CES 2026; pilot invitations open; no customer announced as of 12/2025) [S1][S2] |
| First shown / launch | Unveiled 2025-10-28; public demos GTC Washington DC (booth 368), CES 2026 [S1][S3] |
| Target applications | Light/medium industrial: machine operation for manufacturing, part sorting and material handling, quality inspection, packaging; longer-term service contexts |
| Price | n/a (not disclosed); RaaS-anchored model expected [S2] |
| Availability | Pilot opportunities by contact; US-first [S1] |

## Design & morphology
- Dual production arms (ADAM lineage) on a wheeled AMR platform derived from Richtech's Titan delivery series [S1][S2].
- Telescoping neck/torso section raises the head and shoulder line for varied work heights (visible in official imagery) [S4, photo evidence].
- Height/weight/footprint/DoF: n/a (not disclosed).

## Locomotion
- Wheeled AMR base; "fast braking, tight maneuvering, and stability in shared human environments"; explicit wheels-over-legs decision driven by battery life, payload, response time, stability and energy/maintenance cost ("Humans are great at object manipulation, and wheels are best for fast, efficient, and stable transportation" — Matt Casella) [S1][S2, vendor-claimed].
- Speed: n/a (not disclosed).

## Upper body & manipulation
- Dual arms "with the two-armed precision of the ADAM service robot line"; modular end-effectors — hands, clamps, or specialized tools [S1, vendor-claimed].
- Payload/reach: n/a (not disclosed).
- Demonstrated task: operating industrial machinery to assemble custom baseball caps live at GTC [S1].

## Sensing
- Four-camera vision system for navigation and task execution in changing environments [S1, vendor-claimed].
- Lidar-based SLAM navigation with "millisecond obstacle detection" [S2, vendor-claimed].

## Actuation & power
- 4+ hour battery life in mobile mode; continuous 24/7 operation from a static (docked/mains) base [S1][S2, vendor-claimed].
- Actuator types/battery capacity: n/a (not disclosed).

## Compute & software
- NVIDIA Jetson Thor onboard for real-time AI vision, decision-making and task execution [S1][S2].
- Training: NVIDIA Isaac Sim "Sim2Real" pipeline — tasks learned virtually then transferred to live environments; simulated learning + real-world reinforcement [S1].
- Proprietary edge-computing algorithms for autonomy without constant cloud connectivity; NLP for human interaction; cloud fleet management [S2].
- Data strategy: "American robotics data initiative" — large-scale US data collection, portions to be licensed to other physical-AI companies [S1].

## Safety & compliance
- Vendor language on fast braking and stability in shared spaces; no published certifications (n/a, not disclosed) [S1].

## Deployment evidence & traction
- No paying customer announced as of the 12/2025 Robot Report interview: "the industry is still waiting for the first Dex customer announcement" [S2, third-party].
- Public demos: GTC 2025 Washington DC hat-assembly demo (with Jensen Huang visiting the booth); CES 2026 appearance [S1][S2][S5].
- Design leverages "insights from more than 450 Richtech robot deployments nationwide" [S1, vendor-claimed].
- NVIDIA partnership (Jetson Thor + Isaac Sim) is the robot's headline credential [S1][S2].

## Assessment (analyst view)
*Analyst opinion.* Strengths: pragmatic architecture reusing two field-proven subsystems (ADAM arms, Titan AMR), first-mover use of Jetson Thor among US wheeled semi-humanoids, dual-mode endurance (4 h mobile / 24-7 static), and a public-company platform for visibility. Weaknesses: no announced customers or pricing, unproven industrial manipulation payloads, and a parent company whose ~$5M revenue and restatement issues limit the capital available for an industrial-grade productization race against Dexterity, Reflex or Chinese A2-W-class machines. Threat to a new EU entrant: currently low — Dex is a well-marketed prototype-stage product — but its NVIDIA-reference-stack approach shows how quickly a mid-size player can assemble a credible wheeled humanoid; EU entrants should expect Isaac-Sim-trained competitors and should counter with certified safety and demonstrated payload/throughput data.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.globenewswire.com/news-release/2025/10/28/3175859/0/en/Richtech-Robotics-Offers-First-Look-at-Dex-A-Mobile-Humanoid-Robot-for-Real-World-Work.html | unveiling 2025-10-28, Titan AMR + ADAM arms, Jetson Thor, Isaac Sim Sim2Real, 4h/24-7 battery modes, modular end-effectors, 4-camera vision, task list, GTC demo, data initiative, Casella quotes | vendor-claimed (PR) |
| 2 | https://www.therobotreport.com/richtech-dex-demonstrates-potential-wheeled-mobile-manipulators/ | wheels-vs-legs rationale, lidar SLAM, edge computing, NLP, no first customer as of 12/2025, 450 deployments, RaaS model, Grand View 65% wheeled context | third-party (interview) |
| 3 | _work/discovery_us_canada.md entry 4 | CES 2026 appearance, announcement date | third-party (project discovery) |
| 4 | images/dex-telescoping-neck.jpg (Richtech photo via The Robot Report) | telescoping neck/torso, wheeled AMR base | third-party (photo evidence) |
| 5 | https://www.therobotreport.com/wp-content/uploads/2025/12/Huang_Richtech.jpg | Jensen Huang at Richtech GTC booth | third-party (photo) |
