# Robody — Devanthro

> Robody is a wheeled, human-sized avatar robot teleoperated through VR, built to let remote caregivers physically help elderly people in ordinary private homes. It is deployed in real German households since 2024 under the "Robody Cares" service model, making Devanthro the leading (and self-claimed only) provider of legally home-deployable humanoid care avatars in Europe. Competitively it defines the teleop-first, service-revenue path into domestic care that autonomy-first vendors cannot yet enter.

| Field | Value |
|---|---|
| Company | Devanthro GmbH |
| HQ | Munich, Germany |
| Status (2026) | prototype / early pilots (real-home deployments since early 2024; 3+ hardware generations) |
| First shown / launch | Avatar concept from ~2021; care-generation Robody unveiled Sept 2024 |
| Target applications | In-home elderly care & assistance (meals, medication, fetching, conversation), ambulatory-care augmentation |
| Price | n/a (not sold as hardware; care-service model "Robody Cares", pricing undisclosed) |
| Availability | Germany only, via care-provider partnerships and pilots |

## Design & morphology
Human-scale torso + head + two arms on a **wheeled mobile base** (no legs); newest generation redesigned torso/arms specifically for home care, covered with soft, flexible customizable "skin" for safe close contact [S1][S2]. Sized to operate in unmodified private homes — carpets, narrow hallways [S2]. Exact height/weight/DoF not published (n/a).

## Locomotion
Wheeled indoor base, drive type not disclosed (diff-drive est.); must handle carpets and domestic thresholds [S2]. Speed n/a.

## Upper body & manipulation
Two arms with hands/grippers for fine bimanual tasks — demonstrated: fetching items from fridges, retrieving clothing, dusting, playing board games, transporting open liquids, preparing meals, administering pills [S2][S3][S4]. Payload/reach not disclosed. Synchronized gesture/hug capability for social touch [S4].

## Sensing
Stereo RGB + depth cameras (operator sees through them in VR at "twice the resolution" of prior gen), microphones/speakers for operator voice; haptic feedback to the operator via VR controllers [S1][S2][S3].

## Actuation & power
Battery-powered, electric actuation (details not disclosed). Earlier Roboy 3.0 lineage was tendon-driven/series-elastic, but the care-generation Robody uses conventional (undisclosed) arm actuation with compliant behavior for safety (estimated).

## Compute & software
Edge AI onboard + cloud processing; 5G and WiFi 6 for ultra-low-latency telepresence; immersive VR operation via Meta/Oculus Quest with haptic controllers [S1][S3]. "Hybrid intelligence": human operators handle novel/empathic tasks, AI progressively automates routines; every teleop session creates training episodes for learning [S1]. No public SDK (closed service platform).

## Safety & compliance
No robot-safety certification published. Vendor claims Robody is "the first and only humanoid robot that can be legally used in domestic settings" (Germany) — i.e. cleared for household operation under German law/insurance frameworks rather than an ISO certification [S1][S2]. Soft skin + teleoperator-in-the-loop are the primary safety arguments. Reimbursement pathways with care insurers under validation [S2].

## Deployment evidence & traction
- Real private-home deployments since early 2024; 3+ hardware generations iterated [S1].
- **Teleskoop** (BMBF €690k, 3 years, closed Jan 2025): consortium lead with FZI and Charité; Robody permanently installed in ambulatory-care households (Diakoniezentrum Pirmasens, Aiutanda, Augustinum); 23 days real-world deployment; validated precise physical assistance via VR+haptics [S3].
- Jan 2026: first humanoid robot caring for a dementia patient at home (vendor-claimed) [S2].
- Collaborations with "Germany's largest care providers"; German ARD TV feature; Forbes coverage [S2][S5].
- Unit numbers: single digits estimated; no commercial revenue disclosed.

## Assessment (analyst view)
*Analyst opinion.* Strengths: only player operating humanoids inside real German homes; regulatory/reimbursement head start; teleop-first model sidesteps the autonomy gap and generates training data; strong narrative fit with the 4.3M-caregiver shortage. Weaknesses: essentially unfunded relative to competitors (grants + bootstrap), no published specs or certifications, tiny fleet, and a service model whose economics (one operator per robot per session) scale poorly until autonomy improves. Threat to a new EU entrant: minimal in industrial segments; in care, Devanthro is more a potential partner/acquisition target than a blocker — but it could lock up German care-provider channels and reimbursement codes if it scales first.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.devanthro.com/ | Concept, hybrid intelligence, sensors, 5G/WiFi6, deployments since 2024, home-legality claim | vendor-claimed |
| 2 | https://www.devanthro.com/robody_unveiled/ | Care-gen redesign, soft skin, home tasks, VR resolution, dementia-care first | vendor-claimed |
| 3 | https://www.fzi.de/en/2025/01/23/closing-of-teleskoop-research-project-robotics-for-future-care/ | Teleskoop partners, funding, household pilots, haptic VR control, open-liquid transport | third-party |
| 4 | https://interestingengineering.com/innovation/robodies-advancing-in-home-elderly-care-telepresence | Teleop model, care tasks, soft skin, hugs/gestures | third-party |
| 5 | https://www.tomorrowsworldtoday.com/robotics/meet-the-advanced-robotic-avatar-for-next-gen-elderly-care/ | Eldercare avatar coverage | third-party |
