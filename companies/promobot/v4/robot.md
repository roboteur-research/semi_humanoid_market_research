# Promobot V.4 — Promobot

> The V.4 is Promobot's flagship wheeled service humanoid: a 1.5 m, 130 kg receptionist/promoter with two gesturing 6-7 DoF arms, a chest touchscreen, face recognition, document scanning and payment processing. It matters because it is one of the highest-volume semi-humanoids ever sold (800+ units claimed, 40+ countries) — proof of a real market for sub-$30k reception robots — while illustrating the ceiling of gesture-only arms without manipulation.

| Field | Value |
|---|---|
| Company | Promobot LLC |
| HQ | Perm, Russia |
| Status (2026) | shipping (Russia/MENA/Asia focus; US market closed by Jul 2026 FCC import ban) |
| First shown / launch | V.4 generation ~2019 (V.1 from 2015) |
| Target applications | reception, promotion, government service (MFC), banks, airports, malls, museums, education |
| Price | from ~USD 25,000 purchase; ~$2,000/day event rental (third-party distributor) |
| Availability | direct + international distributors (e.g., UAE/GCC); purchase or rental |

## Design & morphology
Wheeled service humanoid: height 1,485-1,585 mm (head/torso lift extendable to 2,060 mm per user guide), width 740-2,060 mm (arms out), length 716 mm, weight up to 130 kg with battery [S1][S2]. Chest touchscreen for interaction; expressive LED-face head with 2-DoF rotation; torso rotation 2-3 DoF with height adjustment [S2]. Overall DoF ~17-19 (estimated from 2×6-7 arm + head + torso).

## Locomotion
Two-wheel differential drive with support casters; indoor smooth-floor use; autonomous docking with charging station [S2]. Max speed n/a (not disclosed; walking-pace, estimated).

## Upper body & manipulation
Two arms with 6-7 DoF each (8 motors per arm pair per vendor news), used for gesturing, pointing, handshakes — not load manipulation; no payload rating published (effectively ~0-1 kg, estimated) [S1][S2]. Hands are static shells with touch sensors; no gripper, no tool flange.

## Sensing
16 ultrasonic sensors around base; 3D sensor for navigation; HD face-recognition camera (25-30 fps); omnidirectional microphone array; touch sensors on head and arms [S2].

## Actuation & power
Electric servos (details n/a). Battery: capacity n/a; up to 480 min (8 h) continuous operation; autonomous recharge docking [S2].

## Compute & software
Onboard PC, Linux OS with proprietary (closed-source) stack: face/speech recognition, autonomous navigation, dialogue system, e-queue management, payment processing, third-party integration APIs; remote content management [S2]. Russian/English and multilingual packs. No ROS, no open SDK.

## Safety & compliance
No ISO 13482 / CE service-robot certification found (n/a, not disclosed). Low-speed operation, ultrasonic obstacle avoidance; e-stop at rear (visible in product photos).

## Deployment evidence & traction
Vendor/partner claims: 800+ units, 40+ countries ("robots work in 43 countries") [S1][S3]. Verified-by-press deployments: Perm MFC "civil servant" issuing documents, 30,000+ inquiries since 2019 [S4]; Kuwait Oil Corporation reception [S1]; Baltimore/Philadelphia-area US installs pre-2022 via Promobot Corp NY; event rentals across Europe/GCC [S3][S5]. Post-2022 traction shifts to Russia, GCC (UAE hub strategy, Dec 2025) and Asia (China factory plan reported Oct 2025) [S6]. Confidence: unit count vendor-claimed, direction of travel third-party.

## Assessment (analyst view)
*Analyst opinion.* Strengths: real volume production and distributor network, proven ~$25k price point, robust kiosk-grade software (payments, queue, documents) that most Western startups lack. Weaknesses: no manipulation (arms are theatrical), dated sensor/compute stack, closed software, and severe geopolitical constraints — US import ban (2026), EU payment/logistics barriers. Threat to a new EU entrant: low in manipulation-centric segments; moderate only in price-sensitive reception/promo tenders in MENA/CIS where Promobot undercuts on price. Its main lesson for an EU entrant is the size of the service/reception segment and the importance of turnkey business software.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://promo-bot.ai (product + news pages, incl. arms-with-8-motors article) | arm DoF, deployments, countries | vendor-claimed |
| 2 | https://promo-bot.ai/wp-content/uploads/2024/05/Promobot-V.4-User-guide-2024-07-05-2024.pdf | full V.4 specs (dimensions, sensors, runtime, software) | vendor-claimed |
| 3 | https://bankofpartners.com/en/service/view?id=12121 + https://reliablerobotics.ai/products/interactive-robots/humanoid-robots/promobot-v4/ | 800+ units, from $25k, GCC distribution | third-party (distributor) |
| 4 | https://roboticsandautomationnews.com/2020/08/04/prombot-puts-its-humanoid-robot-to-work-as-a-civil-servant/34685/ | MFC deployment, 30k inquiries | third-party |
| 5 | https://www.robot-rental.co/robots/promobot-v4/ | $2k/day rental | third-party |
| 6 | 2025 press (UAE hub Dec 2025; China factory Oct 2025) + https://www.pbs.org/newshour/world/u-s-bans-foreign-made-humanoid-robots-targeting-china-over-national-security | current market orientation, US ban | third-party |
