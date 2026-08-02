# Memo — Sunday Robotics

> Memo is a fully autonomous wheeled home robot from Sunday Robotics (Mountain View, CA): a Wall-E-like semi-humanoid with two arms, three-finger grippers and a telescoping central column on a wheeled base, aimed squarely at consumer household chores (dishes, laundry, tidying, even espresso). It matters competitively because it pairs the strongest publicly benchmarked autonomy claim in the home category (ACT-2: 99.1% zero-shot laundry folding in unseen homes) with a sub-$10k target price and a capital-efficient data flywheel (Skill Capture Glove instead of teleoperation) — making it the reference point against which every Western consumer semi-humanoid will be judged.

| Field | Value |
|---|---|
| Company | Sunday Robotics (Sunday Inc.) |
| HQ | Mountain View, California, USA |
| Status (2026) | announced (beta "Founding Families" late 2026) |
| First shown / launch | Stealth exit 2025-11-20; WIRED hands-on demo published 2026-02-12 [S1][S4] |
| Target applications | Home chores: table clearing, dishwasher loading, laundry folding, tidying, espresso/coffee prep |
| Price | Not announced. Hand-built cost ~$20,000/unit today; company says large-scale manufacturing will cut costs "by at least 50%"; sub-$10k retail target at scale [S2][S3] |
| Availability | Beta "Founding Families" late 2026 ("by Thanksgiving" per Zhao); waitlist ~1,000 (03/2026); US first [S2][S5] |

## Design & morphology
- Wheeled platform base with a central telescoping column ("spine") — no legs. Memo "changes its height by sliding up and down a central column atop that platform" [S1, third-party].
- Working envelope: can lower to touch the floor and reach as high as ~7 ft (~2.13 m) with its arms; rests at ~4 ft (~1.22 m) for most tasks [S2, vendor-claimed].
- Weight ~170 lb (~77 kg) [S3, third-party/analyst].
- Two arms; friendly cartoonish face (two eye-slits) and a baseball-cap head styling (red/blue/navy variants); gleaming white body with soft-touch silicone shell [S1][S2].
- Total DoF: n/a (not disclosed).

## Locomotion
- Wheeled base (drive type not disclosed; demo videos show smooth indoor rolling between counter and table) [S1].
- Deliberately trained to move at ~50% of human pace for safety and precision [S2, vendor-claimed].
- Passive stability: robot "won't drop if powered off" — statically stable, a certification/safety advantage over bipeds [S2, vendor-claimed].
- Max speed, terrain limits: n/a (not disclosed).

## Upper body & manipulation
- Two arms terminating in simplified 3-finger grippers that mimic the most-used human fingers; hand co-designed as a geometric mirror of the Skill Capture Glove — the company's core hardware-AI co-design idea [S3][S4].
- Demonstrated dexterity (observed by WIRED): operating an espresso machine end-to-end (filling and tamping a portafilter, slotting it, pressing buttons, retrieving the cup); holding two glasses in one hand (one pinched between "thumb" and "pointer", one grasped with the remaining finger); loading a dishwasher; folding socks; clearing napkins and dumping food scraps [S1][S2].
- Garment envelope for folding: from baby clothes (16"×8") to 8XL shirts (38"×42") [S6, vendor-claimed].
- Reach, per-arm payload, repeatability: n/a (not disclosed).

## Sensing
- Cameras feeding the ACT policy ("input from the robot's sensors") [S1]; details of head/wrist sensors, depth, lidar: n/a (not disclosed).
- Skill Capture Glove is sensorized to capture human tactile/motion signal for training; the robot hand mirrors its sensor layout [S3][S4, vendor-claimed].

## Actuation & power
- Actuator types, battery capacity, runtime, charging dock: n/a (not disclosed).
- Compliant control — limbs are safe to push/grab mid-task [S2, vendor-claimed].
- Lightweight structure + silicone shell chosen for household safety [S2].

## Compute & software
- Onboard compute: n/a (not disclosed).
- AI stack: ACT-1 (launch model, 11/2025): long-horizon mobile manipulation combining map-conditioned navigation with manipulation, zero-shot generalization to unseen homes [S3][S6]. ACT-2 (preview 2026-07-16): 99.1% ±0.3% success over 785 autonomous folding attempts across 9 garment types in unseen homes, same checkpoint, no per-home adaptation; mean fold quality 4.72/5 (73.8% perfect scores); median fold time 2 min 13 s; company claims scaling glove-data pretraining narrowed the seen→unseen generalization gap from 82% to ~0%, and that a single fine-tuning example can teach a generalizing new behavior [S6, vendor-claimed].
- Training data: ~10M behavioral episodes/trajectories from 2,000+ paid "Memory Developers" doing chores at home wearing the Skill Capture Glove (~$200 build cost, ~$400/pair per WIRED; workers paid up to $60/h); "Skill Transform" pipeline converts glove motion to robot trajectories at ~90% claimed fidelity — explicitly NOT teleoperation [S1][S3][S4].
- "Solve" evaluation standard proposed by Sunday: report performance (success/quality/speed), scope (declared distribution of environments/objects) and adaptation cost per capability [S6].
- User-teaching planned: "people should be able to teach their own robots" (Zhao) [S1]. Privacy positioning: no continuous learning required in customer homes [S2].

## Safety & compliance
- No certifications disclosed. Safety design features: statically stable wheeled base (no fall on power loss), compliant limbs, 50%-of-human-speed motion, lightweight body, soft silicone shell [S2, vendor-claimed]. No ISO 13482/UL 3300 claims found.

## Deployment evidence & traction
- No robots in customer homes yet (as of 08/2026). Beta "Founding Families" scheduled late 2026; Zhao targets first deliveries "by Thanksgiving" 2026 [S2][S5, vendor-claimed].
- Waitlist ~1,000 as of Series B (03/2026) [S5, third-party].
- Independent observation: WIRED reporter watched multi-step espresso prep, table clearing and dishwasher loading in a Sunday demo kitchen (Mountain View) — slow but successful; reporter cautions demos ≠ field reliability [S1, third-party].
- Data operation is the real deployed asset: 2,000+ paid glove workers ("thousands of gloves shipped"), ~10M episodes [S3][S4, mixed].
- External validation: Ken Goldberg (UC Berkeley): "a beautiful design, and a much smarter kind of data capture" [S1, third-party].

## Assessment (analyst view)
*Analyst opinion.* Strengths: the strongest research pedigree in the category (Mobile ALOHA + Diffusion Policy authors), a genuinely differentiated and capital-efficient data strategy whose cost per episode is orders of magnitude below teleop fleets, quantified autonomy claims with a proposed public evaluation standard, and $200M of funding at a $1.15B valuation. Weaknesses: zero field deployments to date, undisclosed hardware specs, a 3-finger gripper that may cap task breadth, and the unproven leap from 99% laundry benchmark to open-ended chores in kid/pet-filled homes; consumer service, liability and support layers are unbuilt. For a new EU entrant the threat is high but indirect: Sunday defines price ($10k) and evidence expectations (Solve-style reporting) for consumer semi-humanoids, yet ships US-first with no EU presence, CE/Machinery-Regulation work presumably not started — leaving a 1-2 year window in Europe. Its glove-based data model is the element most worth emulating or countering.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.wired.me/story/this-home-robot-clears-tables-and-loads-the-dishwasher-all-by-itself | hands-on demos (espresso, two glasses, dishwasher), morphology, glove $400/pair, full-stack quotes, Goldberg quote, beta this year (article 2026-02-12) | third-party (WIRED) |
| 2 | https://www.sunday.ai/ | floor-to-7ft envelope, 4 ft rest height, 50% human pace, compliant control, passive stability, silicone shell, ~$20k build cost, ≥50% cost reduction, Founding Families beta late 2026, task list, privacy | vendor-claimed |
| 3 | https://sacra.com/c/sunday/ | ~170 lb weight, 3-finger gripper, $6-20k prototype cost, sub-$10k target, ~10M trajectories, 90% Skill Transform fidelity, $60/h pay, business model, risks | third-party (analyst) |
| 4 | https://www.businessinsider.com/sunday-robotics-home-robot-training-hands-loading-dishwasher-2025-11 | stealth exit 2025-11-20, glove ~$200 vs $20k teleop rig, 500+ collectors at launch | third-party |
| 5 | https://techcrunch.com/2026/03/12/humanoid-robotics-maker-sunday-reaches-1-15b-valuation-to-build-household-robots/ | $165M Series B @ $1.15B (Coatue, Tiger, Benchmark, Bain), waitlist 1,000, Thanksgiving target | third-party |
| 6 | https://www.sunday.ai/blog/act-2-preview | ACT-2 99.1%±0.3% / 785 trials / 9 garment types / 4.72/5 quality / 2:13 median, garment size envelope, Solve standard, single-example fine-tuning, 82%→0% generalization-gap claim, ACT-1 description | vendor-claimed |
| 7 | https://www.businessinsider.com/sunday-robotics-memo-home-robot-fold-laundry-99-success-2026-7 | ACT-2 launch coverage, >100 employees, glove workforce scale (2,000+ memory developers per project discovery synthesis) | third-party / estimated |
