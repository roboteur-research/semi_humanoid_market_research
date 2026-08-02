# Stanford University (IRIS Lab / Salisbury Lab)

| Field | Value |
|---|---|
| HQ | Stanford, CA, USA |
| Founded | 1885 (university); Mobile ALOHA project 2023-24 |
| Founders / key people | Mobile ALOHA: Zipeng Fu, Tony Z. Zhao (co-leads), Prof. Chelsea Finn (advisor, IRIS Lab). PR1 (2006-08): Prof. Kenneth Salisbury, Keenan Wyrobek, Eric Berger |
| Employees (approx.) | n/a (academic lab; core Mobile ALOHA team ~3) |
| Ownership / listing | private university (research, not a vendor) |
| Total funding / valuation | n/a (academic; project hardware budget ~USD 32k) |
| Semi-humanoid products | [mobile-aloha/](mobile-aloha/) |
| Other products | Static ALOHA bimanual rig (RSS 2023); lineage to ALOHA 2 and ALOHA Unleashed at Google DeepMind |
| Website | https://mobile-aloha.github.io/ |

## Company background
Stanford is not a commercial player, but its 2023-24 ALOHA work is arguably the single most influential low-cost semi-humanoid platform of the current wave. The original ALOHA ("A Low-cost Open-source Hardware system for bimanual teleoperation", Tony Zhao et al., RSS 2023) paired two Trossen ViperX 300 follower arms with two smaller WidowX leader arms for puppeteering, and introduced ACT (Action Chunking with Transformers) imitation learning. Mobile ALOHA (Fu, Zhao, Finn; arXiv Jan 2024) put that bimanual rig on an AgileX Tracer wheeled base for ~USD 32k total, with whole-body teleoperation (operator tethered at the waist backdrives the base) and demonstrated cooking, cabinet use and elevator riding from only 20-50 demonstrations per task, co-trained with static ALOHA data [S1][S2].

All hardware and code are open-source (MIT), which spawned a commercial ecosystem: Trossen Robotics sells official Stationary/Mobile ALOHA kits, AgileX sells the Cobot Magic clone, and countless labs replicated the rig. Google DeepMind continued the line with ALOHA 2 (ruggedized, more ergonomic gravity-compensated leader arms, 2024) and ALOHA Unleashed (diffusion-policy dexterity: tying shoe laces, hanging shirts; CoRL 2024) [S3][S4].

Historic note — PR1: in 2006-08, Kenneth Salisbury's Stanford lab built PR1 ("Personal Robot One"), a human-sized two-armed wheeled robot that, under teleoperation, tidied a living room and fetched a beer. Builders Keenan Wyrobek and Eric Berger took the concept to Willow Garage, where it became the PR2 — making Stanford the origin point of both of the field's landmark wheeled dual-arm platforms, two decades apart [S5].

## Relevance to the semi-humanoid market
Mobile ALOHA reset industry expectations on cost (tele-op bimanual mobile manipulation for ~$32k vs $250k+ research platforms) and seeded today's startup wave: co-lead Tony Zhao co-founded Sunday Robotics (Memo home robot, $1.15B valuation 2026) with Cheng Chi; advisor Chelsea Finn co-founded Physical Intelligence, whose π0 models train largely on ALOHA-style rigs [S6][S7]. Any EU entrant will compete against a talent pool and data ecosystem standardized on ALOHA-descended hardware.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://mobile-aloha.github.io/ | project, authors, tasks, code links | vendor-claimed (project site) |
| 2 | https://arxiv.org/abs/2401.02117 | hardware specs, cost, results | vendor-claimed (paper) |
| 3 | https://aloha-2.github.io/ | ALOHA 2 at DeepMind | vendor-claimed |
| 4 | https://aloha-unleashed.github.io/ | ALOHA Unleashed dexterity results | vendor-claimed |
| 5 | https://robotsguide.com/robots/pr1 | PR1 history, Wyrobek/Berger → Willow Garage | third-party |
| 6 | https://techcrunch.com/2026/03/12/humanoid-robotics-maker-sunday-reaches-1-15b-valuation-to-build-household-robots/ | Tony Zhao → Sunday Robotics | third-party |
| 7 | https://www.pi.website/ | Chelsea Finn → Physical Intelligence | third-party |
