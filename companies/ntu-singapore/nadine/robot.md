# Nadine — NTU Singapore (IMI) / MIRALab Geneva

> Nadine is a realistic seated social android (built 2013 by Kokoro, Japan; software by NTU Singapore) with 27 DoF for facial expressions and upper-body/arm gestures, modeled on its creator Prof. Nadia Magnenat Thalmann. It is among the most field-tested research androids — 100k+ museum interactions, an AIA insurance customer-service role, and a dementia-ward eldercare study — and since 2022-2026 has been re-architected around LLMs with long-term memory at MIRALab Geneva. Competitively: a benchmark for front-office/eldercare social HRI, not a manipulation or mobility platform.

| Field | Value |
|---|---|
| Company | NTU Singapore Institute for Media Innovation (hardware: Kokoro, Japan); research continued at MIRALab, Univ. of Geneva since 2022 |
| HQ | Singapore |
| Status (2026) | research (active; LLM-driven trials at MIRALab into 2026) |
| First shown / launch | Built 2013 |
| Target applications | Social interaction research: reception, customer service, museums, eldercare companionship |
| Price | n/a (one-off research android; Kokoro androids historically ~$100-200k, estimated) |
| Availability | Not for sale |

Design: gynoid with natural-looking skin, hair and realistic hands, modeled on Prof. Thalmann; 27 DoF driving facial expressions and upper-body movements; typically seated (no locomotion; hands are gestural — a 2017 paper demonstrated limited human-like object grasping [S4]) [S1]. Software: three-layer architecture — perception (3D depth cameras, webcam, mic: face/emotion/gesture/object recognition), processing (behavior-tree "brain", dialog, affective system, episodic memory), interaction (motor control, speech synthesis; earlier versions used Google Assistant integration); speaks six languages (English, German, French, Chinese, Hindi, Japanese) [S1]. Since 2022 rebuilt as an LLM-driven agent with human-like long-term memory and emotional appraisal (Wiley CAVW 2024; arXiv 2405.20189), with trials continuing into 2026 [S2][S3]. Deployment evidence (third-party): ArtScience Museum Singapore May-Oct 2017, >100,000 visitor interactions; customer-service agent at AIA Singapore; eldercare assistant at Bright Hill Evergreen Home late 2020-Apr 2021 including research with light-dementia patients [S1].

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://en.wikipedia.org/wiki/Nadine_Social_Robot | Specs, 27 DoF, Kokoro, software layers, deployments | third-party |
| 2 | https://arxiv.org/html/2405.20189 | LLM architecture, memory, affect | third-party (peer-reviewed) |
| 3 | https://onlinelibrary.wiley.com/doi/10.1002/cav.2290 | LLM-driven Nadine (CAVW 2024) | third-party (peer-reviewed) |
| 4 | https://www.researchgate.net/publication/315607217_Nadine_A_Social_Robot_that_Can_Localize_Objects_and_Grasp_Them_in_a_Human_Way | Object localization/grasping capability | third-party (peer-reviewed) |
