# Hobbs (incl. Hobbs W1) — Noetix Robotics (松延动力)

> Bionic-head service humanoid line from Beijing's Noetix Robotics (maker of the low-cost N2 biped). The line pairs a hyper-realistic 32-active-DoF silicone face with different bodies: the earlier Hobbs generations are stationary bust/upper-body platforms (~$35k), while the fourth-generation Hobbs W1 (launched 16 Dec 2025, ~$73.5k) puts dual 5-DoF arms with 6-DoF dexterous hands on an omnidirectional wheeled base — marketed as "China's first bionic service robot with a high-DoF humanoid head". It competes on affective human-likeness for reception/companionship, not industrial manipulation.

| Field | Value |
|---|---|
| Company | Noetix Robotics (Beijing; brand 松延动力) |
| HQ | Beijing, China |
| Status (2026) | shipping (W1 pre-sales on JD.com; earlier Hobbs "in production") [S2][S3] |
| First shown / launch | Hobbs bust generations 2024–2025; Hobbs W1 wheeled model announced 16 Dec 2025 [S3] |
| Target applications | Hotel/corporate reception, museum & heritage tours, government halls, elder-care companionship, STEM education |
| Price | Hobbs (stationary) ~USD 35,000 [S2]; Hobbs W1 US$73,500 [S3] |
| Availability | China (JD.com pre-sale, reseller export via RobotsAsia); lead time n/a |

## Design & morphology
Two morphologies share the bionic head. (a) Stationary Hobbs: upper-body bust ~120–140 cm, ~40–50 kg, ~20 DoF, aluminium/plastic construction [S2]. (b) Hobbs W1: full-height service robot on an enclosed wheeled skirt base (verified image), 54 active DoF total — head 32 active + 8 passive DoF, 3-axis neck (35° pitch / 25° roll / 90° yaw), two 5-DoF arms, two 6-DoF five-finger hands — plus a chest-mounted display [S3, vendor-claimed via reseller]. W1 height/weight n/a (not disclosed).

## Locomotion
W1: omnidirectional wheeled navigation platform with autonomous navigation; speed n/a (not disclosed) [S3]. Stationary Hobbs: none.

## Upper body & manipulation
W1 arms are light interaction arms (5 DoF each) with 6-DoF dexterous five-finger hands — designed for gesturing, handing over items and light service, not payload work; the stationary Hobbs platform lists ~6 kg manipulation capacity [S2][S3]. Reach, repeatability, tool interfaces n/a (not disclosed).

## Sensing
RGB cameras and microphone arrays in head; facial-recognition and emotion-recognition systems; LiDAR-compatible base sensing on W1 [S2][S3]. The head reproduces 200+ human micro-expressions with <150 ms expression-imitation latency and 98% speech-recognition accuracy claimed [S1][S3, vendor-claimed].

## Actuation & power
Head uses many micro-actuators under platinum-silicone skin (details n/a). Battery capacity/runtime n/a (not disclosed).

## Compute & software
W1: "dual 8 GB GPUs" edge compute for deep-reinforcement-learning-driven facial expression generation and real-time interaction [S3]. Stationary Hobbs: embedded x86/ARM, Linux-based robotics OS, Ethernet/Wi-Fi, LLM integration via external APIs [S2]. Hobbs 3 won China's first domestic robot-debate competition, showcasing real-time conversational reasoning [S3, third-party].

## Safety & compliance
n/a (not disclosed). Marketed for "safe operation in shared spaces"; no ISO 13482/CE claims found.

## Deployment evidence & traction
W1 pre-sale bookings on JD.com reportedly exceeded 500 units within the first days after the 16 Dec 2025 launch [S3, third-party]. Pre-launch deployments claimed in museums, government halls and offices [S3]. Earlier Hobbs used in education/research/demonstration settings [S2].

## Assessment (analyst view)
*Analyst opinion.* Strengths: best-in-class affective realism (32-DoF face, micro-expressions) at aggressive Chinese pricing; proven e-commerce demand; Noetix's N2 biped fame gives brand pull. Weaknesses: manipulation is token (5-DoF arms, light payload), specs are thin and mostly reseller-mediated, and uncanny-valley acceptance in Western markets is uncertain. Threat to a new EU industrial entrant: low on manipulation use-cases — this is a front-of-house interaction product — but it could take reception/companion niches an EU service player might covet.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://noetixrobotics.com/en/hobbs3 | bionic head specs (32 DoF, latency, speech accuracy) | vendor-claimed |
| 2 | https://humanoid.guide/product/hobbs/ | stationary Hobbs specs, $35k price, applications | third-party |
| 3 | https://www.robotsasia.com/Hobbs-W1.htm | W1 launch 2025-12-16, $73.5k, 54 DoF breakdown, omnidirectional base, JD.com pre-sales, deployments | third-party (reseller) |
