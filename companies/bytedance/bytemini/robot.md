# ByteMini — ByteDance Seed (字节跳动 Seed)

> Internal research robot, not a product: a 22-DoF bimanual mobile manipulator built by ByteDance's Seed team as the embodiment for its GR-3 vision-language-action model.

| Field | Value |
|---|---|
| Company | ByteDance Seed (robotics team) |
| HQ | Beijing, China |
| Status (2026) | research (internal platform; not for sale) |
| First shown / launch | July 2025 (GR-3 technical report) |
| Target applications | VLA research: generalizable pick-and-place, table bussing, deformable-object (cloth) manipulation |
| Price | n/a (not a product) |
| Availability | not available |

| Spec | Value | Confidence |
|---|---|---|
| Base type | wheeled mobile base with lift column (photos show column-mounted torso on wheeled cart) | third-party (photos) [S2] |
| DoF total | 22 | vendor-claimed [S1][S2] |
| Arms | 2× 7-DoF "unbiased" arms with unique sphere-wrist joint configuration for dexterity in confined spaces | vendor-claimed [S1][S3] |
| Control | whole-body motion control (WBC) for smooth trajectories in narrow spaces | vendor-claimed [S3] |
| End effector | parallel grippers (GR-3); multi-finger dexterous hands in GR-Dexter follow-on | vendor-claimed [S4] |
| Height/weight/battery/compute | n/a (not disclosed) | — |
| AI stack | GR-3 VLA (web-scale VL co-training + VR human-trajectory fine-tuning + robot imitation learning); GR-RL | vendor-claimed [S1] |

ByteMini is ByteDance Seed's purpose-built bimanual mobile robot, introduced alongside the GR-3 VLA model in July 2025 [S1]. It has 22 DoF with two 7-DoF arms whose sphere-wrist design gives human-like dexterity in confined spaces, coordinated by a whole-body motion controller [S1][S3]. Published demos cover long-horizon table bussing, generalizable pick-and-place with novel objects and instructions, and bimanual deformable-object tasks such as hanging clothes [S2]. The December 2025 GR-Dexter report upgrades the platform with multi-fingered hands and teleop gloves [S4]. It is strictly a research embodiment — no commercialization, pricing or external availability has been announced — and it is borderline "semi-humanoid": a bimanual torso on a wheeled cart/column without anthropomorphic styling.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://arxiv.org/abs/2507.15493 | GR-3 technical report; ByteMini 22 DoF, sphere wrist, WBC | third-party (preprint) |
| 2 | https://seed.bytedance.com/en/blog/seed-research-gr-3-released-a-generalist-robot-model-for-generalization-long-horizon-tasks-and-bi-manual-deformable-object-manipulation | demos, capabilities, photos | vendor-claimed |
| 3 | https://news.aibase.com/news/19853 | 22 DoF, wrist ball design, WBC summary | third-party |
| 4 | https://arxiv.org/pdf/2512.24210 | GR-Dexter dexterous-hand upgrade | third-party (preprint) |
