# TWENDY-ONE (トゥエンディワン) — Waseda University Sugano Lab

> TWENDY-ONE (2007) is the Sugano Lab's human-symbiotic care robot — an adult-female-sized dual-arm humanoid on an omnidirectional cart with 47 DoF, 13-DoF four-finger hands and mechanical passive compliance in every joint, able to support a human's body weight in bed-to-wheelchair transfer. It predates the current semi-humanoid wave by ~15 years and remains a canonical reference design for compliant care manipulation; it is a research platform, never commercialized, and the direct ancestor of the AIREC Moonshot program.

| Field | Value |
|---|---|
| Company | Waseda University, Sugano Laboratory (TWENDY team) |
| HQ | Tokyo, Japan |
| Status (2026) | research (historic platform; superseded by AIREC program) |
| First shown / launch | Unveiled 2007 (successor to WENDY, 1999) |
| Target applications | Human-symbiotic daily-life support: care assistance (transfer, fetch), kitchen/housework tasks, safe physical HRI |
| Price | n/a (never sold) |
| Availability | Lab platform only |

## Design & morphology
Adult-female physique so it can use human-scaled tools and environments [S1]. Total 47 DoF + omnidirectional mobility: arms 7×2, hands 13×2, neck 3, trunk 4 [S1]. Weight 111kg [S1]; height ~1.47m (third-party commonly cited). Curved-surface exterior housing harnesses while preserving joint range — designed jointly for approachability and contact safety [S1].

## Locomotion
Omnidirectional mobile cart, chosen so the robot can maneuver stably among people and "deflect" unexpected external forces during contact [S1].

## Upper body & manipulation
Redundant 7-DoF arms for obstacle-avoiding manipulation; 4-DoF trunk with large vertical range (pick objects from floor, wipe floors) [S1]. Hands: 13-DoF anthropomorphic four-finger hands capable of stable grasping/manipulation of complex shapes [S1]. Demonstrated care tasks include supporting a person out of bed and into a wheelchair, breakfast preparation (toast with tongs, fetching ketchup), and object handovers; the platform can bear substantial human load during transfer assist (~34kg-class support demonstrated) [S2] (third-party).

## Sensing
Distributed tactile skin on hands/arms, fingertip 6-axis force sensors (research literature); head with cameras; whole-body force sensing via compliant joints [S2] (third-party). Detailed sensor list n/a on lab page.

## Actuation & power
Signature feature: mechanical PASSIVE COMPLIANCE elements in each joint — absorbing positioning errors and disturbances during human contact while maintaining precision when stiff [S1]. Electric servo actuation; tethered/battery details n/a.

## Compute & software
Proprietary research controllers (pre-ROS era); impedance/compliance control research stack [S2]. n/a beyond publications.

## Safety & compliance
Safety-by-mechanism (passive compliance, rounded shell); no certification (research) [S1].

## Deployment evidence & traction
None commercial. Widely demonstrated 2007-2015 (care transfer, kitchen demos), extensively published; one of the most-cited care-humanoid platforms of its generation [S1][S2]. Lineage continues in AIREC (Moonshot Goal 3).

## Assessment (analyst view)
*Analyst opinion.* TWENDY-ONE established, 15 years early, the exact recipe today's care-oriented semi-humanoids converge on: omni base + compliant dual arms + dexterous hands + soft shell. Its passive-compliance-by-mechanism philosophy remains instructive versus today's software-only compliance. As a 2007 lab artifact it competes with no one; its relevance is as prior art, talent pipeline (Waseda alumni across Japanese robotics) and the intellectual foundation of AIREC. EU entrants studying care-market requirements should mine its literature on contact-safety mechanisms.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | http://www.twendyone.com/tech.html (+concept.html) | 47 DoF breakdown, 111kg, omni cart, passive compliance, trunk design, hands | vendor-claimed (lab) |
| 2 | Sugano Lab publications via http://www.twendyone.com/paper.html | tactile skin, force sensors, transfer-assist demos, ~34kg support | third-party (peer-reviewed) |
