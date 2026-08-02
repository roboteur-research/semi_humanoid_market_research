# Foodly (フードリー) — RT Corporation

> Foodly is a ~150cm dual-arm "humanoid collaborative robot" (人型協働ロボット) that stands shoulder-to-shoulder with human workers on bento (boxed-lunch) assembly lines and picks irregular bulk foods — fried chicken, cherry tomatoes, meatballs — into trays using deep-learning vision. Launched at FOOMA 2019 and productionized in early 2021, it is one of the very few humanoid-form robots anywhere doing paid production work in food factories, and the anchor case for semi-humanoid economics in food processing.

| Field | Value |
|---|---|
| Company | RT Corporation (株式会社アールティ) |
| HQ | Tokyo, Japan |
| Status (2026) | shipping |
| First shown / launch | FOOMA Japan 2019 (announced 07/2019); standard production model early 2021 |
| Target applications | Bento/prepared-food factories: picking bulk ingredients into bento boxes/trays on existing conveyor lines |
| Price | n/a (not disclosed); made-to-order, customized per factory; monthly rental service available |
| Availability | Japan, direct sale + monthly rental; per-customer customization |

## Design & morphology
Human-scale torso robot: height ~150cm ("small adult size"), shoulder width ~40cm, so it fits into a single human work slot on an existing line without line modification [S1]. Two arms, head with status-indicator lights, mounted on a caster base (pedestal beside the conveyor, manually repositionable — not self-driving). Exact DoF count not disclosed (n/a).

## Locomotion
None (passive casters for manual repositioning between lines) [S1].

## Upper body & manipulation
Dual arms sized for tray-scale reach; payloads are food-piece scale (grams, not kg — not formally disclosed). Interchangeable, washable sanitary grippers ("hands") designed for food handling; arm covers designed to avoid finger-pinch points [S1]. Throughput ~800 meal-portions/hour depending on ingredient (vendor-claimed) [S1]. Handles primarily round/solid items: karaage, cherry tomatoes, meatballs, fish cakes, nuggets, hamburg steaks, shrimp dumplings [S1].

## Sensing
Head-mounted AI vision system ("Foodly AI Vision", NEKONOTE-branded recognition) that segments individual food items in random bulk piles and recognizes containers, robust to lighting changes; industry-first random bulk food picking claim [S1]. Recent software update allows containers to be configured on the fly without pre-registration [S1].

## Actuation & power
Hybrid torque/position motor control with "soft control" so contact with humans is low-force [S1]. Power: AC 100V or battery, 8+ hours battery operation (vendor-claimed) [S1]. Actuator make/model n/a (not disclosed).

## Compute & software
Deep-learning stack built on TensorFlow; ROS-compatible; a "Foodly TypeR" research variant is sold to labs [S1]. Operation is "teaching-less": operators pick the menu item and container on a display panel and the AI plans motions [S1]. NVIDIA Jetson used in RT's stack (vendor materials) [S1].

## Safety & compliance
Collaborative-by-design: soft torque-limited control, pinch-free arm design, status lights; works without safety fencing next to human workers (vendor-claimed; no ISO 13482/TS 15066 certification publicly stated — n/a) [S1].

## Deployment evidence & traction
- Hirai Co. (Kumamoto) — bento line, portioning into containers [S2] (vendor-claimed case study).
- Ichibiki Co. (Aichi) — retort side-dish line, filling cylindrical containers [S2] (vendor-claimed).
- Partnership with Will of Factory/Will of Work (2020): dispatches pre-trained human staff together with rented robots ("hybrid staffing") [S2].
- METI "Innovative Robot R&D Foundation Building" projects FY2020/FY2021 [S2].
- Vendor states adoption "by bento/prepared-food makers across Japan" as of 02/2023; total unit count n/a (not disclosed) [S1][S3].

## Assessment (analyst view)
*Analyst opinion.* Foodly proves the narrow-slot thesis: a humanoid form factor pays off where lines are built for human shoulder widths and re-engineering is off the table. Strengths: real production deployments since 2021, food-grade washable grippers, rental + staffing go-to-market that de-risks adoption for conservative food SMEs. Weaknesses: single-vertical (bento picking of roundish solids), no autonomous mobility, artisanal made-to-order volumes, and RT's SME scale caps growth. Threat to an EU entrant is low directly (Japan-only), but Foodly is the best public benchmark for food-sector semi-humanoid ROI and would be the incumbent reference in any Japanese food-factory deal.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://rt-net.jp/service/foodly/ | specs, vision, throughput, safety, power, TypeR | vendor-claimed |
| 2 | https://rt-net.jp/service/foodly-results/ | customers, partnerships, METI projects | vendor-claimed |
| 3 | https://rt-net.jp/notice/foodly190701/ | 2019 announcement, "industry-first" claim | vendor-claimed |
