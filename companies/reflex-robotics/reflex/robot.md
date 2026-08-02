# Reflex — Reflex Robotics

> Reflex is a compact wheeled humanoid for warehouse work: a sub-2×2 ft mobile base carrying a dynamic-height telescoping spine, two arms with parallel grippers, a stereo-camera head and a chest e-stop, operated teleop-first with autonomy layered on progressively from supervised production data ("Reflex Intelligence"). Deployed under RaaS at GXO since September 2024 (operational within 60 minutes of unboxing) and an RBR50 2025 winner, it is the leading US example of the ship-now-automate-later wheeled strategy — with a Nuevo León (Mexico) factory announced in February 2026 to scale it.

| Field | Value |
|---|---|
| Company | Reflex Robotics |
| HQ | New York City, NY, USA |
| Status (2026) | shipping (RaaS pilots/production at GXO; lease-only) |
| First shown / launch | Public emergence with $7M seed 03/2024; GXO deployment announced 2024-09-18 [S3][S2] |
| Target applications | Warehouse/factory: tote transfers between automation systems, product and shelf picking, order replenishment, quality assurance, general repetitive material handling |
| Price | Lease/RaaS only; reported target below $50,000/unit [S4, third-party/estimated] |
| Availability | US deployments via direct RaaS agreements; Nuevo León (MX) plant announced 02/2026 for volume production [S5] |

## Design & morphology
- Compact wheeled base with footprint under 2×2 ft (<61×61 cm), letting it work in standard aisles and at existing human workstations [S6, third-party discovery].
- Vertical column ("dynamic-height spine", REFLEX-branded) that changes working height to reach both low bins and high shelves [S1][S6]; photographic evidence shows shoulder assembly riding the column [S7].
- Two arms with white/purple industrial-design shells; head pod with stereo camera pair; red e-stop button on the chest [S7, photo evidence].
- Height/weight/DoF: n/a (not disclosed).

## Locomotion
- Wheeled base (drive type not disclosed); designed for flat warehouse floors [S1].
- Speed: n/a (not disclosed). Vendor claims "superhuman... battery life and speed" without figures [S1].

## Upper body & manipulation
- Dual arms; combined payload 50+ lb (~23 kg) [S4, third-party].
- Parallel-jaw two-finger grippers (visible in GXO deployment photo and og image, handling apparel polybags, totes and boxes) [S7, photo evidence].
- Works with the customer's existing carts, monitors, scanners and touchscreens — no facility retrofit ("zero integration & day one readiness") [S1, vendor-claimed].
- Reach/per-arm payload/repeatability: n/a (not disclosed).

## Sensing
- Stereo camera head pod; additional cameras/sensors n/a (not disclosed) [S7].
- Perception supports learning-from-demonstration and remote supervision views for teleoperators [S1][S4].

## Actuation & power
- Actuators: n/a (not disclosed).
- Battery life 16+ hours for extended shifts [S4, third-party]; charging details n/a.

## Compute & software
- "Reflex Intelligence": real-time human supervision for predictable recovery, teleoperation of edge cases, and progressive autonomy — "robots learn from supervised work in real operations, enabling them to become more capable... and become more autonomous over time" [S1, vendor-claimed].
- Deployment speed: operational within 60 minutes at GXO [S2, third-party].
- GXO pilot began with teleoperated control by human staff for tote transfers and picking, transitioning tasks to autonomy as models mature [S2][S4].
- Fleet/operator ratio: n/a (not disclosed).

## Safety & compliance
- Chest-mounted e-stop visible; statically stable wheeled platform [S7]. No published ISO/ANSI R15.08 certifications found (n/a, not disclosed).

## Deployment evidence & traction
- GXO Logistics RaaS agreement (announced 2024-09-18; GXO's second RaaS deal ever): live at a Fortune 100 retailer's omni-channel fulfillment operation; tasks include tote transfers, product/shelf picking, order replenishment, QA; CEO Ragavender: "rapidly accelerating our robot production" [S2, third-party/customer].
- Genuine deployment photo (GXO press asset) shows Reflex picking apparel into green totes in a live GXO facility [S7].
- RBR50 Robotics Innovation Award 2025 ("wheeled mobile manipulator uses teleoperation to multi-task") [S3].
- Manufacturing scale-up: Nuevo León, Mexico plant announced 2026-02-02 by Governor Samuel García — described as Latin America's first humanoid-robot factory [S5, third-party].
- Unit counts: n/a (not disclosed; pilot-scale, est. single-to-low-double digits).

## Assessment (analyst view)
*Analyst opinion.* Strengths: fastest deployment story in the category (60 minutes, zero integration), honest teleop-first economics that generate revenue and training data from day one, marquee 3PL validation (GXO), 16+ h endurance, and a nearshore factory plan pointing at sub-$50k volume pricing. Weaknesses: only $7M disclosed funding; almost no published hardware specs; autonomy progress is asserted, not benchmarked; single-customer concentration risk. Threat to a new EU entrant: high in intralogistics — Reflex's model (RaaS, existing-infrastructure compatibility, human-in-the-loop guarantee) is precisely what European 3PLs will ask EU vendors to match, and GXO operates massive European sites that could import it quickly. Countermoves: EU entrants should lead with certified safety (Machinery Regulation 2023/1230, R15.08-equivalent) and published autonomy metrics, where Reflex is opaque.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.reflexrobotics.com/ | positioning, zero integration, Reflex Intelligence, supervision model, investors | vendor-claimed |
| 2 | https://gxo.com/news_article/gxo-partners-with-reflex-robotics-to-deploy-new-warehouse-automation/ | GXO deal 2024-09-18, tasks, 60-min readiness, Fortune 100 site, RaaS, quotes | third-party (customer) |
| 3 | https://www.therobotreport.com/rbr50-company-2025/wheeled-mobile-manipulator-uses-teleoperation-to-multi-task/ | RBR50 2025 award, teleop-multi-task framing | third-party |
| 4 | https://aijack.info/robot/reflex-robotics-1/ + funding search 2026-08-02 (Crunchbase synthesis: $7M seed Khosla 2024-03-13, <$50k target) | 50+ lb payload, 16+ h battery, lease-only, teleop-to-autonomy, funding | third-party / estimated |
| 5 | https://www.milenio.com/negocios/samuel-garcia-anuncia-instalacion-fabrica-robots-humanoides-nuevo-leon (+ La Jornada, MVS, Heraldo 2026-02-02, Spanish, translated) | Nuevo León factory, first in Latin America | third-party |
| 6 | _work/discovery_us_canada.md entry 3 | <2×2 ft footprint, dynamic-height spine, NYC HQ | third-party (project discovery) |
| 7 | images/reflex-gxo-warehouse.jpg (GXO press photo) + images/reflex-og.png | visual: stereo head, chest e-stop, parallel grippers, column-riding shoulders, live GXO operation | third-party (photo evidence) |
