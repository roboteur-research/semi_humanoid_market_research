# Zero-shiki Jinki ver.2.0 / Multifunctional Railway Heavy Machine (零式人機 ver.2.0 / 多機能鉄道重機) — Jinki Ittai × Nippon Signal × JR West

> A teleoperated humanoid torso mounted on the telescoping crane boom of a road-rail vehicle, working overhead-line infrastructure at up to 12m with 40kg grip capacity under power-amplified force-feedback control. In revenue service on JR West lines since July 2024 for structure painting and vegetation cutting, it is Japan's highest-profile deployed semi-humanoid (2024) and the robot that coined the 人型重機 ("humanoid heavy machinery") category — proof that human-piloted, non-autonomous semi-humanoids can win safety-critical infrastructure budgets today.

| Field | Value |
|---|---|
| Company | Developer/licensor: Jinki Ittai; manufacturer: Nippon Signal; customer: JR West (operation: Nishi-Nippon Electric Systems) |
| HQ | Kusatsu, Shiga (Jinki Ittai); Tokyo (Nippon Signal); Osaka (JR West) |
| Status (2026) | shipping (in revenue service since 07/2024) |
| First shown / launch | Zero-shiki Jinki ver.1.x from ~2019 (Fukushima program); ver.2.0 PoC 2021-22; commercial service July 2024 |
| Target applications | Railway electrification maintenance: painting overhead-line support structures, cutting obstructing trees; roadmap: power-line and civil-engineering work |
| Price | n/a (not disclosed) — sold as integrated maintenance vehicle by Nippon Signal; Jinki Ittai earns licensing |
| Availability | Japan (JR West network); expansion via consortium partners |

## Design & morphology
Humanoid upper body (head + two arms, no legs) mounted at the tip of a telescoping boom on a **road-rail vehicle** (drives on road, rides on rails). Working height up to **12m** above the ground [S1][S2]. The torso replaces the human worker in a cherry-picker basket. Overall DoF n/a (not disclosed). Styling by Macross designer Shoji Kawamori — deliberately iconic to aid category recognition [S3].

## Locomotion
Vehicle-based: road-rail truck positions the robot along the track; boom slews/telescopes to place the torso at the work site. The robot itself does not locomote — a category-defining trait of 人型重機.

## Upper body & manipulation
Two heavy-duty arms; **maximum grip/handling capacity 40kg** [S1][S2]. Tools: powered saws/cutters for vegetation, painting equipment for steel structures; tool exchange between missions ("multifunctional") [S1]. Control: **power-amplified bilateral master-slave** — operator's arm motions map to the robot with force feedback scaled down to human level, so the operator *feels* contact while commanding super-human force; Jinki Ittai's core patented technology (force control, torque control, power-amplified bilateral control) [S1][S2, vendor-claimed].

## Sensing
Robot-head cameras streamed to **VR goggles** giving the operator the robot's eye-line ("robot's-eye view" work); force/torque sensing throughout the arms feeds the bilateral loop [S1][S2]. No autonomy sensors (lidar/SLAM) — deliberately none.

## Actuation & power
High-power electric/hydraulic actuation from the vehicle platform (exact type n/a — not disclosed); powered by the road-rail vehicle, so no battery/runtime constraint.

## Compute & software
Master-slave control system (Jinki Ittai licensed stack); no AI/autonomy layer — the human is the intelligence. This "zero-autonomy" architecture avoided certification and reliability barriers and got it into service years before AI competitors.

## Safety & compliance
Primary purpose is safety: it removes humans from work at height near live overhead lines, eliminating fall and electrocution risk (高所での墜落・感電) and enabling older/more diverse workers to do heavy maintenance [S1][S2]. Rail-industry operational approval implied by revenue service on JR West; formal standards/certs n/a (not disclosed).

## Deployment evidence & traction
- **In revenue service on JR West operating lines since July 2024** for overhead-line support painting and obstructing-tree cutting [S1][S2, vendor + third-party]. Widely reported as the world's first humanoid heavy machine in regular railway service.
- Unit count n/a (not disclosed; initial deployment believed single-digit, estimated).
- Development lineage funded by Fukushima reconstruction program (2019-21) + Minamisoma City (2021); ver.1.3 permanently displayed at Fukushima Robot Test Field [S2].
- Consortium: Nippon Signal (manufacture), Nishi-Nippon Electric Systems (operation), with announced collaborations toward Tohoku Electric Power Network (transmission) and Takenaka Civil Engineering [S2].
- Extensive media coverage (Toyo Keizai, robotstart, international tech press) established 人型重機 as a mini-category [S3][S4].

## Assessment (analyst view)
*Analyst opinion.* Strengths: only semi-humanoid in this study earning railway-infrastructure revenue; force-feedback power amplification is genuinely differentiated IP; the vehicle-mounted model sidesteps navigation, battery and safety-certification problems that stall every mobile competitor; anchor customer (JR West) and manufacturing partner de-risk scale-up. Weaknesses: not autonomous and not general-purpose — each new task needs tooling and consortium engineering; the licensing model caps direct revenue; addressable volume (rail maintenance vehicles) is hundreds, not tens of thousands. Threat to an EU entrant: low as a direct competitor (Japan-locked, niche), but high as a strategic template — EU rail/utility incumbents (e.g. DB, SNCF, grid operators) are the obvious buyers for an equivalent, and whoever brings this model to Europe first inherits an uncontested niche.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://robotstart.info/2024/07/19/jrwest-humanoid-heavy-machinery.html | service from 07/2024, tasks, 12m, 40kg, VR goggles, bilateral control, safety rationale | third-party |
| 2 | https://prtimes.jp/main/html/rd/p/000000036.000070266.html | roles (Nippon Signal mfr, licensing model), Fukushima funding, ver.1.3/2.0 lineage, partners, 40kg/12m | vendor-claimed |
| 3 | https://toyokeizai.net/articles/-/797495 | Kawamori design, category framing (paywalled; headline/lead only) | third-party |
| 4 | ROOT/_work/discovery_japan.md entry 7 | 人型重機 category coinage, "highest-profile JP deployment 2024" | third-party (synthesis) |
