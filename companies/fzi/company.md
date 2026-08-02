# FZI Forschungszentrum Informatik (FZI Research Center for Information Technology)

| Field | Value |
|---|---|
| HQ | Karlsruhe, Germany |
| Founded | 1985 (non-profit research foundation affiliated with KIT); HoLLiE robot since 2011 |
| Founders / key people | Foundation of the State of Baden-Württemberg/KIT ecosystem; HoLLiE contact: Georg Heppner (department manager, service robotics) |
| Employees (approx.) | ~200+ researchers (third-party, typical FZI scale) |
| Ownership / listing | Independent non-profit research institution (Stiftung), applied-research transfer partner of KIT |
| Total funding / valuation | n/a — contract research + public grants (BMBF funded HoLLiECares; Teleskoop) |
| Semi-humanoid products | [hollie/](hollie/) (HoLLiE, HoLLiE C) |
| Other products | Autonomous driving test field Baden-Württemberg, industrial AI/robotics contract R&D, Teleskoop telepresence-care system (with Devanthro Robody) |
| Website | https://www.fzi.de/ |

## Company background
FZI is Karlsruhe's applied-research transfer institute (closely tied to KIT): a non-profit that turns informatics and robotics research into pilots with industry and public-sector partners. Its semi-humanoid platform HoLLiE ("House of Living Labs intelligent Escort") has existed since 2011 and is deliberately built from robust industrial components with in-house integration: a Clearpath Ridgeback omnidirectional base, a 2-joint actuated torso, two 6-DoF Pilz PRBT arms, and interchangeable end effectors including Schunk SVH five-finger hands — all on ROS/ROS 2 [S1][S2][S3].

The flagship application program was HoLLiECares (BMBF-funded, ~2020-2024): developing HoLLiE into a multi-functional nursing-support robot, tested in real hospital wards at Städtisches Klinikum Karlsruhe and Knappschaftsklinikum Saar. Six use cases were implemented and field-tested: pushing a wheelchair, escorting patients to examinations (haptic guidance via shoulder F/T sensors), instructing movement exercises (MediaPipe/YOLOv5 pose tracking), voice-based wound documentation, medicine restocking (ArtiMinds RPS), and handling deformable objects such as transfusion bags [S2]. The upgraded platform generation is documented as HoLLiE C (arXiv 2312.06292, Dec 2023) [S4]. FZI also ran Teleskoop (concluded Jan 2025) with Devanthro (Robody): a cooperative telepresence system letting remote care staff embody a robot in ambulant care — relevant context for the avatar-care model in Germany [S5].

FZI does not sell robots; it sells applied R&D and runs "living lab" demonstrators. HoLLiE's value to the market is as Germany's most concrete evidence base for what hospital-support semi-humanoids can and cannot yet do (the project's own conclusion: robots can take over specific tasks but cannot provide the empathy nursing requires, and doors/elevators/IT integration remain hard) [S2].

## Relevance to the semi-humanoid market
High evidentiary relevance for a German entrant targeting healthcare: HoLLiECares is one of very few multi-month, real-ward European trials of a bimanual wheeled humanoid, with published lessons on use-case selection, safety, data protection and hospital integration. FZI is a natural pilot/integration partner (and a route to Klinikum Karlsruhe-style trial sites). No commercial threat; trajectory steady as a contract-research platform.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.fzi.de/en/research/projekt-details/hollie/ | HoLLiE overview, modularity, ROS 2, applications, contact | vendor-claimed |
| 2 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1325143/full | HoLLiECares hardware, six use cases, two hospitals, findings | third-party (peer-reviewed) |
| 3 | https://www.fzi.de/en/project/holliecares-2/ | HoLLiECares project, BMBF funding | vendor-claimed |
| 4 | https://arxiv.org/abs/2312.06292 | HoLLiE C platform paper (Dec 2023) | vendor-claimed (preprint) |
| 5 | https://www.fzi.de/en/2025/01/23/closing-of-teleskoop-research-project-robotics-for-future-care/ | Teleskoop conclusion Jan 2025, telepresence care with Devanthro | vendor-claimed |
