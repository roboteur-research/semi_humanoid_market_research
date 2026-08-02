# Q5 (星动Q5) — Robot Era (星动纪元)

> The 星动Q5 is Robot Era's wheeled service humanoid: ~1.65 m, 65-70 kg, 44 DoF with 7-axis arms, 11-DoF "spirit hand" (精灵手) dexterous hands (~10 kg single-arm lift), a signature ultra-slim waist and 3-DoF flexing/height-adjusting wheeled leg section, driven by the company's ERA-42 end-to-end VLA model with 37+ language interaction. Launched mid-2025 (Chengdu debut 19 Jun 2025, 100+ intent orders), it is deployed in malls and at the Chengdu Panda Base, and — critically — is the platform behind Haier's HIVA (海娃) smart-home robot. It matters as one of the most dexterous commercial wheeled humanoids and the clearest OEM-channel play in the category.

| Field | Value |
|---|---|
| Company | Robot Era (星动纪元), Tsinghua IIIS spin-off |
| HQ | Beijing, China |
| Status (2026) | shipping (pilots + commercial units since 2025) |
| First shown / launch | H1 2025; Chengdu commercial debut 19 Jun 2025 [S3]; Haier HIVA variant unveiled 26 Jul 2025 [S4] |
| Target applications | Mall/retail guidance & sales, museums (Chengdu Panda Base), hotels (elevator operation, shoe polishing), medical/eldercare assistance (water delivery, object retrieval), smart-home (as Haier HIVA) |
| Price | n/a (not disclosed) |
| Availability | China direct + Haier OEM channel; no Western distribution documented |

## Design & morphology
Wheeled full-size humanoid, ~1.65 m, 65-70 kg (sources vary within this band) [S3][S4]. 44 DoF whole-body [S1][S2]. Signature ultra-compact waist — marketed as "narrower than an iPhone" (小腰精 = "slim-waist sprite" launch tagline) — giving a distinctive hourglass silhouette and large torso articulation range [S1][S3]. Lower body: 3-DoF wheeled "leg" section with flexible bending and height adjustment for floor-to-shelf reach [S1].

## Locomotion
Wheeled base (configuration not detailed) with lidar + vision fusion navigation, autonomous path planning and narrow-corridor obstacle avoidance [S1]. Speed n/a. Indoor commercial environments.

## Upper body & manipulation
Dual 7-axis high-precision biomimetic arms; ~10 kg single-hand/arm lift (demo: ~20 bottles of water one-handed) [S1][S3]. Hands: 11-DoF dexterous "spirit hand" (精灵手) — related to Robot Era's XHAND direct-drive hand family (XHAND1: 12 active DoF, full direct-drive, 1,000+ operation types) [S1][S2]. Speed demo: 10 clicks per second [S1][S3]. Repeatability/flange media n/a. Full-body teleoperation supported via data gloves and VR devices (also its data-collection mode) [S1].

## Sensing
Lidar + vision fusion for navigation [S1]; camera/mic configuration not itemized (n/a). Anthropomorphic voice interaction with LLM-backed dialog [S1]. Tactile/F-T sensing not documented for Q5 (XHAND family has per-finger sensing per company materials — unconfirmed for Q5's spirit hand).

## Actuation & power
Robot Era self-developed joint modules (company-level claim; L7 sibling uses 400 Nm peak, 25 rad/s joints — Q5-specific figures n/a) [S2]. Battery/runtime n/a (not disclosed).

## Compute & software
Onboard compute n/a (not disclosed). Software: ERA-42 self-developed end-to-end embodied VLA model (world model + fast-slow layered architecture); understands instructions in 37+ languages; anthropomorphic voice engine; complete data pipeline (collection → processing → training → validation) for continuous skill learning [S1][S2]. Teleop via VR/data gloves. SDK/openness n/a.

## Safety & compliance
n/a (not disclosed). Public-space deployments (malls, tourist sites) imply basic collision avoidance/e-stop but no certifications published.

## Deployment evidence & traction
- Malls: Q5 units guiding customers in Chinese shopping malls (video evidence cited by independent blog) [S5] (third-party).
- Chengdu: commercial debut 19 Jun 2025 with 100+ intent orders reported; deployment at the Chengdu Research Base of Giant Panda Breeding (tourism/guide role) [S3] (third-party).
- Company-level: >200 units delivered across product line, orders >RMB 500M cumulative, "9 of global top-10 tech companies" as customers [S2] (vendor-claimed, unverified).
- **Haier HIVA (海娃) OEM relationship — verification finding:** multiple independent sources agree HIVA is **built on a customized Robot Era Q5 platform**, jointly developed by Haier and Beijing Xingdong Jiyuan (= Robot Era), not an in-house Haier robot. Evidence: (a) search-aggregated product coverage states "HIVA Haiwa is built on a customized version of RobotEra's Q5 wheeled humanoid platform… 44 DoF, dexterous hands, deep integration with Haier Smart Home cloud" (165 cm, 70 kg — matching Q5's spec band) [S4]; (b) independent US blog: "Haier's Hiva appears to be a customized version of RobotEra's Q5" [S5]; (c) Haier Capital co-led Robot Era's Series A (Jul 2025), giving Haier strategic equity alignment [S6]; (d) the discovery sweep found no in-house Haier humanoid program. Unveil date reported as 26 Jul 2025; one source attributes it to "AWE 2025" — AWE 2025 ran in March, while 26 July matches WAIC 2025 timing, so the event attribution is uncertain (date third-party, venue unresolved). No credible source claims HIVA is Haier's own robot; the "conflicting info" reduces to Haier-branded marketing omitting Robot Era's name.

## Assessment (analyst view)
*Analyst opinion.* Strengths: top-tier dexterity for the class (44 DoF + 11-DoF direct-drive-heritage hands), genuine full-stack (actuators→hands→VLA), fast commercial traction, and the Haier OEM deal — a scale channel into homes/retail that no competitor has replicated. Weaknesses: thin published specs (no battery, compute, price, safety data), vendor-heavy claims (top-10 tech customers), and consumer/service positioning that is harder to monetize than factory work. Threat to an EU entrant: high in service/retail verticals; the OEM playbook is the bigger strategic lesson — European appliance and retail brands (BSH, Miele, retail chains) are open flanks that Robot Era-style platform vendors could capture as branded channels before EU robot makers do.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://www.robothot.com/product/robotera-q5 | 44 DoF, 7-axis arms, 11-DoF spirit hand, 10 kg, 10 clicks/s, slim waist, 3-DoF legs, lidar+vision nav, ERA-42, 37+ languages, teleop, applications | vendor-claimed (reseller reproducing vendor materials) |
| 2 | https://www.stcn.com/article/detail/3018906.html | Company/product family (L7, XHAND1, ERA-42), >200 units, customer claims | third-party (quoting vendor) |
| 3 | https://lite.duckduckgo.com/lite/?q=星动纪元+Q5+身高+体重 (Chinese press snippets: Toutiao/Baidu Baike/Sohu) | 1.65 m, 65-70 kg, Chengdu debut 19 Jun 2025, 100+ intent orders, water-bottle demo | third-party |
| 4 | https://lite.duckduckgo.com/lite/?q=Haier+Hiva+RobotEra+Q5 (aggregated coverage) | HIVA = customized Q5, joint development, 165 cm/70 kg, unveil 26 Jul 2025, Haier Smart Home cloud integration | third-party |
| 5 | https://mikekalil.com/blog/china-humanoid-summer-2025/ | Independent: HIVA appears to be customized Q5; mall guidance deployments | third-party |
| 6 | https://lite.duckduckgo.com/lite/?q=星动纪元+融资 (funding coverage) | Haier Capital co-led Series A Jul 2025 | third-party |
