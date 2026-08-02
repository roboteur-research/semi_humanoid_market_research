# TARA GEN1 — iHub Robotics

> Low-cost Indian wheeled service semi-humanoid for customer-facing roles
> (reception, airports, banks, patient support). Marketed as "India's most
> advanced semi-humanoid robot" with 100+ language conversational AI; arms are
> low-DoF and essentially gestural. Competitively it matters as a sub-$15k price
> anchor with early Gulf-region exports, not as a manipulation platform.

| Field | Value |
|---|---|
| Company | iHub Robotics (IHUB Research and Robotics), Kochi, Kerala, India |
| HQ | Kochi, Kerala, India |
| Status (2026) | shipping (small volumes; "in production" per guide, units exported to UAE & Saudi Arabia — third-party, unverified counts) [S1] |
| First shown / launch | 2025 (humanoid.guide listing June 2025) [S1] |
| Target applications | airports, banks, edtech, reception, patient support, logistics/customer-facing interactions [S1][S2] |
| Price | USD 13,998 [S1] |
| Availability | India + exports to UAE, Saudi Arabia; direct purchase [S1] |

## Design & morphology
163 cm tall, 75 kg; humanoid torso with chest-mounted display and skirt-style
cowling over a circular wheeled base (see image). Mild-steel structure. Overall
DoF listed by the guide as only 3 (plus 3 hand DoF, 10 cosmetic fingers) —
i.e. the arms are pose/gesture devices, not manipulators [S1].

## Locomotion
Wheeled circular base, autonomous navigation with obstacle avoidance plus manual
remote-control fallback; max speed 2.52 km/h (0.7 m/s) [S1][S3].

## Upper body & manipulation
Two arms with 5-finger cosmetic hands; payload/strength listed at 2 kg total.
Manipulation score 2/10 on humanoid.guide. No wrist media, no tool interface,
no repeatability data [S1]. Effectively non-manipulating.

## Sensing
4K camera with face, gesture and emotion recognition; microphone/speaker for
multi-language speech (100+ languages claimed); navigation sensors on base (type
not disclosed — depth/lidar visible as sensor cluster on base cowling) [S1][S2][S3].

## Actuation & power
Closed-loop stepper motors with harmonic-drive gears [S1]. Battery capacity not
disclosed; runtime ~8 h per charge [S1]. IP53 ingress protection.

## Compute & software
1024-core NVIDIA Ampere GPU module (i.e. a Jetson Orin-class SoM), Ubuntu 22.04,
Llama 3 LLM integration, WiFi; glass-to-action latency ~1.5 s (guide metric) [S1].
SDK/API openness not disclosed.

## Safety & compliance
n/a (not disclosed). No standards or certifications claimed [S1].

## Deployment evidence & traction
Exports to UAE and Saudi Arabia reported (third-party, no unit counts) [S1][S4].
Target verticals hospitality, healthcare, transportation, customer service. No
named customers found. humanoid.guide marks the listing "Not Verified".

## Assessment (analyst view)
*Analyst opinion.* TARA GEN1 is a conversational kiosk-android — closer to Pepper
than to dual-arm semi-humanoids: 3 arm DoF total, 2 kg payload, 0.7 m/s. Strengths:
aggressive price (~$14k), multilingual AI pitch, and early Gulf sales channels.
Weaknesses: no manipulation, mild-steel build, unverified claims, tiny funding
base for its stated manufacturing ambitions. Threat to a new EU entrant in
industrial/logistics semi-humanoids: negligible; minor relevance only if the EU
entrant also targets reception/hospitality segments on price.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/tara-gen1/ | full spec set, price, status, exports | third-party |
| 2 | https://www.ihubrobotics.com/tara | product positioning (JS site, minimal crawlable text) | vendor-claimed |
| 3 | https://html.duckduckgo.com/html/?q=iHub+Robotics+TARA+GEN1+humanoid+Kerala (roboboom.com, aiwiki.ai, yourstory.com snippets) | semi-humanoid class, navigation, 100+ languages | third-party |
| 4 | https://html.duckduckgo.com/html/?q=%22iHub+Robotics%22+Kerala+funding+humanoid+TARA+news | UAE/Saudi exports, funding context | third-party |

*Specs carry confidence tags per source column; unknown fields marked n/a.*
