# EVE — 1X Technologies (ex-Halodi Robotics)

> EVE is a 1.86 m, two-wheeled, self-balancing android with tendon-driven arms, a friendly LED face and a Robotiq 3-finger gripper hand, developed in Norway from ~2015 and deployed commercially since ~2020 — chiefly as a night security guard for Everon/ADT Commercial ("EvoGuard") and in logistics/care pilots. It matters because it was arguably the West's largest deployed humanoid fleet (est. 150-250 units), proved the wheeled-base + RaaS model years before the humanoid hype cycle, and then was deliberately deprioritized in favor of the legged consumer robot NEO — with the EVE fleet re-tasked as a real-world data engine for 1X's "Redwood" VLA.

| Field | Value |
|---|---|
| Company | 1X Technologies (founded as Halodi Robotics) |
| HQ | Moss, Norway + Palo Alto/San Mateo, CA, USA |
| Status (2026) | discontinued for new sales / deprioritized; existing fleet still operating as data source (active deployment confirmed as of mid-2025) [S1][S2] |
| First shown / launch | Public demo July 2017 (warehouse/kitchen tasks); commercial deployments from ~2020 [S1] |
| Target applications | Commercial security patrol/night guarding, logistics, inspection, care pilots; internally: embodied-AI data collection |
| Price | RaaS only; ADT/Everon lease ~NOK 500,000 (~$50k)/unit/year (2022 agreement) [S1] |
| Availability | No longer marketed (EVE page retired after NEO pivot); previously "available now" B2B via contact [S2][S6] |

## Design & morphology
- Humanoid torso, head and two arms on a two-wheel, self-balancing wheeled base with "multi-terrain wheels"; no legs [S2][S6].
- Height 6 ft 2 in (~1.86 m); weight 192 lb (~87 kg) [S2, vendor-claimed].
- ~25 degrees of freedom total [S6, third-party].
- Soft-goods covered body ("soft, organically-inspired mechanics"), LED matrix face with two camera "eyes", side mic/speaker grilles [S2, vendor-claimed + photo evidence S7].

## Locomotion
- Two-wheel dynamically balancing base; top speed 9 mph (~14.5 km/h / 4.0 m/s) [S2, vendor-claimed].
- Navigates corners, unstructured space and can take elevators; opens doors with different handle types [S2, vendor-claimed].
- Note: as a dynamically stable platform EVE does not enjoy the statically-stable certification shortcut of 4-wheel semi-humanoids (cf. ISO/CD 25785-1 gap).

## Upper body & manipulation
- Two tendon-driven arms powered by 1X's Revo1 motors — a deliberate rejection of high-ratio harmonic gears to minimize friction, reflected inertia and impact energy; joints are low-stiffness/back-drivable ("human-inspired musculature") [S1, vendor-claimed].
- Carry capacity 33 lb (~15 kg) [S2, vendor-claimed]; per-arm payload n/a (not disclosed).
- End-effector: Robotiq 3-Finger Adaptive Gripper (clearly visible in official imagery) on at least the standard configuration; adaptive underactuated fingers [S7, photo evidence, third-party].
- Reach/repeatability: n/a (not disclosed).

## Sensing
- High-resolution panoramic cameras; two eye-cameras in the face display; microphones/speakers for HRI [S1][S2].
- Used for remote "tap into their cameras" fleet supervision [S2]. Lidar/depth details: n/a (not disclosed).

## Actuation & power
- Revo1 proprietary low-gear-ratio, tendon-drive actuators throughout [S1, vendor-claimed].
- Runtime: up to 6 hours per charge, ~1-hour recharge [S2, vendor-claimed] (contrary.com cites "up to four hours autonomous runtime" for earlier config [S1]) — battery capacity n/a (not disclosed).

## Compute & software
- Hybrid onboard compute: Intel Core i7 for real-time control + NVIDIA Xavier for AI inference [S1, third-party].
- Operating model: autonomous by default with shared autonomy — a single human operator supervises a fleet of EVEs, taps into cameras and teleoperates (VR) when the robot requests help [S2, vendor-claimed].
- Neural-network stack: 1X Studio "All Neural Networks. All Autonomous." program; EVE fleet experience trains the Redwood VLA and NEO behaviors ("NEO builds on years of EVE's real world experience") [S2][S4, vendor-claimed].
- SDK/open APIs: none public.

## Safety & compliance
- Safety approach: soft mechanics, low-inertia tendon drives, real-world scenario testing before deployment [S2, vendor-claimed]. No published ISO 13482/10218 or UL certification found (n/a, not disclosed).

## Deployment evidence & traction
- Everon (ex-ADT Commercial) "EvoGuard" autonomous guarding suite (launched CES 2023) used EVE for night patrols of US commercial buildings; 2022 ADT agreement: 140 units/year leased at ~NOK 500k/unit/yr (~$7M/yr); cumulative deployed/contracted fleet estimated 150-250 units [S1][S5, third-party + estimated].
- Earlier pilots/customers: Altopack (packaging), Strongpoint (retail logistics), Sunnaas Hospital (Norway, care), I-Mens (Belgian care org) [S1, third-party].
- ~$3M order pipeline by 2021, mostly security [S1].
- 2024-25: fleet's main role is data generation for NEO's models; EVE marketing pages removed from 1x.tech [S4][S6].

## Assessment (analyst view)
*Analyst opinion.* EVE proved three things an EU entrant should internalize: (1) wheeled semi-humanoids could be fielded in paying, unsupervised night-shift roles years before biped rivals left the lab; (2) RaaS at ~$50k/robot/yr is a viable security-sector price; (3) a deployed fleet is a defensible data asset (EVE→Redwood/NEO). Weaknesses: the two-wheel balancing base added complexity without the certification benefits of statically stable platforms, manipulation was limited (single Robotiq gripper, 15 kg carry), and the platform was ultimately abandoned by its own maker for strategic reasons rather than field failure. Threat to a new EU entrant is now low directly — EVE is off the market — but 1X's brand, Norwegian engineering base and $10B-valuation war chest mean it could re-enter commercial wheeled robotics quickly. The vacated European security niche is a near-term opportunity.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://research.contrary.com/company/1x | history, Revo1 tendon design, ~25 DoF, i7+Xavier compute, ADT/Everon economics, pilots, pivot, 4h runtime figure, active deployment mid-2025 | third-party (research) |
| 2 | https://web.archive.org/web/2024/https://www.1x.tech/androids/eve | official specs: 6'2", 192 lb, 9 mph, 33 lb carry, 6h runtime/1h charge, multi-terrain wheels, elevators, shared-autonomy fleet ops, safety language | vendor-claimed |
| 3 | https://techcrunch.com/2024/01/11/1x-a-humanoid-robotics-firm-backed-by-openai-raises-100m/ | $100M Series B context | third-party |
| 4 | _work/market_context.md §5.2/§7 (project research) | EVE fleet → Redwood VLA data; est. 140-unit security deployment | third-party / estimated |
| 5 | EvoGuard/Everon CES 2023 launch coverage (securityinfowatch.com et al., corroborated via search 2026-08-02) | EvoGuard brand, 150-250 unit estimate | third-party / estimated |
| 6 | _work/discovery_us_canada.md entry 5 | two-wheel self-balancing config, 25 DOF, deprioritization | third-party (project discovery) |
| 7 | images/eve-scene.jpg (official 1X photo, cdn.prod.website-files.com .../1x_EVE_03_C_1240x700_2x-p-1600.jpg) | Robotiq 3-Finger Adaptive Gripper as end-effector | third-party (photo evidence) |
