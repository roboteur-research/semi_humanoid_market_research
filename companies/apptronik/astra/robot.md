# Astra (+ Apollo wheeled/pedestal variants) — Apptronik

> Astra was Apptronik's dual-armed upper-body humanoid (circa 2021-22): a force-controlled manipulation platform on a fixed stand or AMR that served as the direct precursor to Apollo's upper body. It is superseded as a product, but its DNA lives on in Apollo's wheeled-base and pedestal-mounted configurations — the semi-humanoid faces of the best-funded US humanoid program (~$935M raised, Google DeepMind Gemini Robotics onboard, Mercedes/Jabil/GXO pilots). This dossier covers Astra historically and Apollo's non-legged variants as the current competitive threat.

| Field | Value |
|---|---|
| Company | Apptronik |
| HQ | Austin, TX, USA |
| Status (2026) | Astra: discontinued/superseded (internal R&D platform). Apollo wheeled/pedestal variants: announced/pilot (legged Apollo in commercial pilots) |
| First shown / launch | Astra ~2021-22; Apollo unveiled Aug 23 2023; Apollo 2 (current gen) with bipedal + wheeled configurations |
| Target applications | Astra: manipulation R&D, interactive service. Apollo (all bases): logistics case/tote handling, kitting, packout, inspection/sorting, machine tending, goods-to-person |
| Price | n/a (not disclosed; direct partner engagements) |
| Availability | Apollo via partner pilots (US/EU pilots at Mercedes, Jabil, GXO); no open ordering |

## Design & morphology
**Astra:** human-scale upper body (torso to ~140 cm) with two arms and five-fingered hands; ~24 DoF total (12 in the hands; some sources cite 17 DoF) — figures vary by source, tag third-party. 10 kg payload per arm. Mountable on fixed stand or third-party AMR. Designed around force-controlled series-elastic-style actuation for safe human contact; explicitly "a modular precursor that fed directly into Apollo" [S2][S3].

**Apollo (current):** 173 cm, 73 kg, 25 kg payload, humanoid proportions with swappable lower body: bipedal legs, wheeled base, or stationary pedestal; third-party coverage: legs↔wheels swap in under an hour [S1][S4]. The wheeled configuration is marketed for "stability and efficiency in high-throughput environments" [S5].

## Locomotion
Astra: none (stand/AMR). Apollo wheeled variant: wheeled base, drive type and speed not disclosed; pedestal variant: fixed. Apollo biped: walking (out of scope here).

## Upper body & manipulation
Astra: two force-controlled arms, 10 kg per arm; five-fingered force-controlled hands (12 hand DoF total per aggregated specs) [S3]. Apollo: 25 kg payload (55 lb); gripper/hand options evolving — commercial pilots use application grippers for case/tote handling; dexterous manipulation showcased with Gemini Robotics demos (e.g., multi-step tasks from natural language) [S1][S4][S5]. Reach/repeatability n/a.

## Sensing
Apollo: head perception suite (stereo/depth cameras; details not fully disclosed), "advanced perception systems" with hardware-level safety zones and impact detection [S5]. Astra: head cameras for manipulation research (details n/a).

## Actuation & power
Apptronik's core IP: proprietary linear/rotary actuators descending from Valkyrie work — "patented actuator technology" with claimed 90%+ energy efficiency [S5]. Apollo: swappable batteries, 4 h per pack, enabling "7x22" operation with opportunity charging or tethering (pedestal config can run tethered continuously) [S1][S5].

## Compute & software
Onboard "Artemis" autonomy stack (perception, planning, controls, safety, task execution, HRI) + Fleet Connect fleet management [S5]. AI partnerships: Google DeepMind — Apollo is the reference embodiment for Gemini Robotics VLA models (partnership Dec 2024, demos from Mar 2025); also NVIDIA Project GR00T collaboration [S4]. No public SDK; closed commercial platform.

## Safety & compliance
Hardware-level safety zones, impact detection, configurable perimeter zones (vendor) [S5]. No published ISO 10218/TS 15066 certification status. Human-safe force-controlled actuation is a core design claim dating back to Astra.

## Deployment evidence & traction
- Mercedes-Benz: Apollo pilots on factory floor since March 2024 (one of the earliest humanoid commercial pilots anywhere); Mercedes invested in 2025 and again 2026 [S4] (third-party).
- Jabil: Apollo piloted in Jabil plants; Jabil contracted to manufacture Apollo at "automotive-grade scale" [S4] (third-party).
- GXO Logistics: warehouse deployments scheduled 2026 [S4] (third-party).
- NASA: 2022 partnership supporting Apollo development [S6] (third-party).
- Configuration note: all public pilot footage to date shows the **legged** Apollo; **no named customer confirmed on wheeled or pedestal configs as of Aug 2026** — the wheeled/pedestal variants are vendor-offered options awaiting visible commercial proof [analyst observation].
- Astra: never commercially deployed; internal R&D milestone only.

## Assessment (analyst view)
*Analyst opinion.* Strengths: deepest partner/capital stack in Western humanoids (~$935M, ~$5B valuation), Gemini Robotics exclusive-embodiment halo, Jabil manufacturing route to real volume, and a modular architecture that lets Apptronik attack wheeled/pedestal semi-humanoid niches at marginal cost whenever it chooses. Weaknesses: the wheeled/pedestal variants remain commercially unproven (no named deployments), Apollo autonomy is still pilot-stage, and the company's attention is dominated by the legged flagship. Threat to a new EU entrant: HIGH and rising — Mercedes gives Apptronik a German automotive beachhead, and a legs-optional Apollo undercuts the "wheels are cheaper" differentiation of semi-humanoid specialists. An EU entrant's window is Apptronik's current focus on bipeds and its closed, partner-only sales model: faster availability, open integration, and EU service coverage are the counters.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://apptronik.com/news-collection/apptronik-unveils-apollo | Apollo specs (5'8", 160 lb, 55 lb payload, 4 h battery), legged/wheeled/pedestal modularity, applications | vendor-claimed |
| 2 | https://apptronik.com/company/our-work | Astra as upper-body platform; QDA/QDH lineage; Valkyrie heritage; Apollo consolidation | vendor-claimed |
| 3 | Aggregated Astra spec coverage (search) | Astra ~24 DoF (12 hand) / 17 DoF variance, 10 kg/arm, 140 cm torso, stand/AMR mounting, precursor role | third-party |
| 4 | Aggregated partnership coverage (search) | DeepMind partnership + Gemini Robotics on Apollo, GR00T, Mercedes pilots since Mar 2024, Jabil pilot + manufacturing, GXO 2026, legs↔wheels <1 h swap | third-party |
| 5 | https://apptronik.com/apollo/apollo-2 | Apollo 2 configurations, Artemis, Fleet Connect, 90%+ actuator efficiency, safety zones, swappable batteries 7x22 | vendor-claimed |
| 6 | NASA partnership 2022 coverage (NASA/Axios via search) | NASA Sept 2022 partnership, Cardenas quote | third-party |
