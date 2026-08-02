# Dyna Robotics

| Field | Value |
|---|---|
| HQ | Redwood City, California, USA |
| Founded | late 2024 |
| Founders / key people | Lindon Gao (CEO; co-founded Caper AI, acquired by Instacart for $350M), York Yang (co-founded Caper AI), Jason Ma (ex-DeepMind, ex-NVIDIA robotics foundation-model researcher) |
| Employees (approx.) | n/a (not disclosed); described as small frontier AI/robotics team |
| Ownership / listing | Private |
| Total funding / valuation | ~$143.5M: $23.5M seed (March 2025, ~$100M valuation, co-led CRV + First Round Capital); $120M Series A (September 2025, $600M+ post-money; RoboStrategy, CRV, First Round, Salesforce Ventures, NVentures/NVIDIA, Amazon Industrial Innovation Fund, Samsung Next, LG Technology Ventures) [S2][S3] |
| Semi-humanoid products | [dyna-1/](dyna-1/robot.md) — DYNA-1 stationary/cart dual-arm robot |
| Other products | DYNA-1 foundation model (robot control model + reward-model training pipeline); custom arms and a mobile base under development [S3] |
| Website | https://www.dyna.co |

## Company background
Dyna Robotics was founded in late 2024 in Redwood City by repeat founders Lindon Gao and York Yang — whose smart-shopping-cart company Caper AI sold to Instacart for $350M — together with Jason Ma, a former DeepMind/NVIDIA researcher known for robotics foundation-model and reward-learning work. The company's stated mission is to bring embodied AI into the real world with "cost-effective, easy to deploy robots for businesses of all sizes", deliberately pairing frontier research with immediate commercialization rather than pursuing general humanoids first [S2][S3].

Its core asset is the DYNA-1 foundation model, built for "round-the-clock, high-throughput dexterous autonomy". Distinctive technical elements: a scalable foundation reward model providing nuanced feedback across diverse robot experience, automatic streaming data segmentation with progress estimation and subtask labeling, and reward-model-in-the-loop iterative training. Headline result: a 24-hour fully autonomous run folding 850-900+ napkins at 99.4% success, ~60% of human speed, zero interventions [S1]. The hardware is deliberately simple — two fixed arms plus a central sensor mast at a workstation (initially off-the-shelf arms, now moving to custom arms and a mobile base) [S3].

Go-to-market: deploy dual-arm workcells into labor-squeezed commercial operations — hotels and commercial laundries (folding by the pound), restaurants/food prep, gyms — with robots reportedly working 16+ hours per day alongside human staff. Third-party coverage describes a robots-as-a-service, "sell labor not hardware" model with monthly pricing; exact rates undisclosed [S4]. In 2025 it raised one of the larger Series A rounds in robotics ($120M at $600M+), with strategic investors spanning NVIDIA, Amazon, Samsung and LG — notable validation for a stationary-first strategy.

## Relevance to the semi-humanoid market
Dyna is the strongest US counter-example to the humanoid form-factor race: no legs, no wheels (yet), just two arms, a camera mast and a foundation model that hits production-grade reliability numbers (99%+ over 24 h) that no legged humanoid vendor has published. For an EU entrant it defines the reliability bar buyers will quote ("99.4% for a full shift, zero interventions") and shows that laundry/food-prep verticals can be won with drastically cheaper hardware. Trajectory: scaling deployments, moving toward custom arms + mobility — i.e., converging on the semi-humanoid form factor from below.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.dyna.co/research/dyna-1 | DYNA-1 model architecture, reward model, 24h napkin run 850+/99.4%, skills | vendor-claimed |
| 2 | Bloomberg/TechCrunch/press aggregated (seed + Series A coverage) | $23.5M seed Mar 2025 (~$100M val), $120M Series A Sep 2025 ($600M+), investor list | third-party |
| 3 | https://salesforceventures.com/perspectives/welcome-dyna-robotics/ | Founders' backgrounds (Caper AI, DeepMind/NVIDIA), off-the-shelf → custom hardware strategy, deployment environments, 900+ napkins | third-party |
| 4 | https://www.dyna.co/ + RaaS coverage in search results | Deployments (hotels, laundromats, restaurants, gyms; 16+ h/day), 40+ shirts/hour, RaaS "sell labor" model | vendor-claimed / third-party |
