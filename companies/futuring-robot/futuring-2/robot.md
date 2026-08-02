# Futuring 2 (未来不远 二代) — Futuring Robot

> Second-generation wheeled dual-arm home humanoid from Shanghai's Futuring
> Robot (未来不远机器人). Torso with two 2-finger-gripper arms on a wheeled
> column base; aimed at household chores (tidying, appliance operation,
> deliveries, serving drinks). Competitively significant as a heavily funded,
> genuinely home-deployed (300+ households claimed) low-cost consumer platform
> rather than a spec-sheet leader. NOTE: listed as Japanese in the discovery
> notes — the company is Chinese.

| Field | Value |
|---|---|
| Company | Futuring Robot (上海未来不远机器人科技有限公司), Shanghai, China |
| HQ | Shanghai, China |
| Status (2026) | prototype / early consumer deployment (guide: "prototype"; vendor claims in-home fleet) [S1][S3] |
| First shown / launch | 2026 (guide listing April 2026; Futuring 1 earlier) [S1] |
| Target applications | household service: tidying, fridge/washing-machine operation, receiving deliveries, serving tea/water; companion, education, healthcare, hospitality [S1][S3] |
| Price | USD 5,000 (guide; inquire via contact form) [S1] |
| Availability | China; direct inquiry; two configuration options reported [S1][S2] |

## Design & morphology
~150-160 cm, ~70 kg; humanoid head (eye display + chest screen) and dual-arm
torso on a slim column over a low wheeled base (image). 26 DoF overall, 12 hand
DoF per guide. Aluminum alloy + composite structure [S1].

## Locomotion
Wheeled base; max 4 km/h (1.1 m/s); 20 mm step-climbing claimed for Gen 2 —
i.e. thresholds/carpet edges, not stairs [S1][S2].

## Upper body & manipulation
Two arms with 2-finger gripping claws (red-padded parallel grippers in image);
total payload 6 kg [S1]. Household manipulation demonstrated in vendor videos
(appliance doors, object pickup). No reach/repeatability disclosed.

## Sensing
HD-4K stereo vision; base sensor arrays visible (front sensor strips); mic/
speaker for interaction [S1]. Details undisclosed.

## Actuation & power
Electric servo motors, harmonic drives / precision reducers [S1]. Runtime: guide
says 3 h; vendor claims for Gen 2 "over 8 h operation, 24+ h standby" —
conflicting, treat 8 h as vendor-optimistic [S1][S2]. Battery capacity n/a.

## Compute & software
AI edge computing unit (likely NVIDIA-based, guide inference); Linux/ROS-likely;
Ethernet + WiFi [S1]. Differentiator is the software: proprietary AVLA
end-to-end model trained on real household data, plus "Self-Evolving WAM" world
action model; claimed 30,000+ in-home service hours feeding training data [S2][S3].

## Safety & compliance
"Safe with humans" (guide attribute); no standards/certifications disclosed [S1].

## Deployment evidence & traction
Claimed deployment in 300+ Chinese households with 30,000+ service hours —
vendor-claimed, echoed by Chinese tech press; "China's first robot deployed in
real family homes" [S2][S3]. Funding traction corroborates momentum (RMB 200M
angel led by ZhenFund Jan 2026; ~RMB 1B follow-on reported) [S2][S3].

## Assessment (analyst view)
*Analyst opinion.* Futuring's edge is not hardware (modest 6 kg payload,
2-finger grippers, harmonic servo arms) but its in-home data flywheel and price
point (~$5k) backed by ~RMB 1.2B of 2026 funding. For a new EU entrant in
industrial/logistics semi-humanoids the direct threat is low today; the medium-
term risk is a China-scale consumer platform maturing into light commercial
service segments (hospitality, care) at unbeatable cost. Spec inconsistencies
(3 h vs 8 h runtime) and "prototype" status warrant caution on claims.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/futuring-2/ | full spec set, $5,000, prototype status, China nationality | third-party |
| 2 | https://html.duckduckgo.com/html/?q=Futuring+Robot+... | Shanghai, founder, funding, 8 h/24 h standby, 20 mm step, 300+ households | third-party |
| 3 | https://html.duckduckgo.com/html/?q=未来不远机器人+... | AVLA/WAM, household task list, 30k hours, funding rounds | third-party |
| 4 | https://futuringrobot.com/ | native name; vendor site (JS-rendered, minimal crawlable content) | vendor-claimed |

*Specs carry confidence per source column; unknown fields marked n/a.*
