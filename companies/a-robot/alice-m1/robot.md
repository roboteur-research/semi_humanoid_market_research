# ALICE M1 (앨리스 M1) — A Robot / AeiROBOT

> Wheeled "mobile humanoid" for manufacturing floors: a dual-7-DoF-arm upper body from the ALICE 4 biped programme mounted via a distinctive **double parallel-link waist** (working height continuously variable 1.3–1.8 m) on a wheeled AMR base. Launched September 2025 with pre-orders; first industrial deployment at HL Mando's Wonju steering plant (Dec 2025) under Korea's M.AX program. Competitively it is Korea's third wheeled semi-humanoid offering (after Rainbow RB-Y1 and ROBOTIS AI Worker), differentiated by gearless linear actuators for quiet, back-drivable force control.

| Field | Value |
|---|---|
| Company | A Robot / AeiROBOT (에이로봇) |
| HQ | Ansan (Hanyang Univ ERICA campus), South Korea |
| Status (2026) | announced/shipping — pre-orders open, first pilot units in the field |
| First shown / launch | Launched 2025-09-11 [S2]; shown at Int'l robotics conference Oct 2025, CES 2026 [S5] |
| Target applications | Manufacturing (flexible production, repetitive/high-fatigue tasks), flat-floor industrial sites |
| Price | n/a (not disclosed) |
| Availability | Korea; pre-order (사전예약) via official site; pilot deployments 2025-26 |

## Design & morphology
- Base type: **wheeled AMR platform** (verified: official renders show a low black wheeled chassis; Korean press describes the lower body as a wheel-based AMR platform replacing the biped legs) [S1][S3]. Discovery flag "base type unverified" is resolved: wheeled, with parallel-link waist above it.
- Height: **1300–1800 mm variable** via **two parallel-link waist structure** (가변 신장 구조) — the whole torso rides two linkage stages, enabling stable work at heights from 1.3 to 1.8 m [S1] (vendor-claimed).
- Weight: **97 kg** per official spec sheet [S1] (vendor-claimed). Note: one press report said 50 kg [S2] — official 97 kg figure is authoritative; 50 kg likely confuses with the 45 kg ALICE 4 biped.
- DoF: **31 total = waist 3 + arms 7×2 + head 2 + hands 6×2** [S1] (vendor-claimed).

## Locomotion
Wheeled base; drive layout (diff vs omni) not disclosed. SLAM-based navigation with sensor-based obstacle avoidance [S1]. Speed n/a (not disclosed).

## Upper body & manipulation
- Two **7-DoF arms** [S1]. Reach and payload n/a (not disclosed).
- **6-DoF hands** (two), five-fingered per renders; "human-level diverse manipulation" claimed from 7-DoF arm + 6-DoF hand combination [S1] (vendor-claimed).
- 3-DoF waist provides horizontal/vertical torso movement for confined-space work [S2].
- Tool changer / media at flange: n/a.

## Sensing
Stereo camera (head), IMU, **3D lidar**, laser sensor(s) on base [S1][S2]. No tactile/force-torque sensors disclosed, though the actuator design provides current-based force sensitivity.

## Actuation & power
- Self-developed **linear actuators**: no reduction gear, back-drivable, high current sensitivity, low inertia for impedance control, low noise, heatsink-integrated frame, dedicated real-time FOC motor drives [S1] (vendor-claimed; same actuator family as ALICE 4).
- Battery: **~3 h runtime, 1.5 h charge** [S2] (third-party report of launch specs). Capacity kWh n/a.

## Compute & software
- Compute: **NVIDIA AGX Orin + AFE-R360** (official site) [S1]; the launch press release said "Orin NX" [S2] — official AGX Orin taken as current. 
- SLAM autonomy on base; imitation-learning/AI manipulation demonstrated (4th-gen ALICE publicly demoed fetching objects on command [S4]). SDK/ROS support n/a (not disclosed).

## Safety & compliance
n/a (not disclosed). Back-drivable gearless actuators are marketed as inherently safer for physical HRI [S1].

## Deployment evidence & traction
- **HL Mando Wonju plant (Munmak, Korea), Dec 2025**: first unit delivered to steering-component production line under the MOTIE M.AX program; assigned to repetitive high-fatigue processes; billed as first real-world factory application of K-Humanoid Alliance tech (third-party, ZDNet exclusive) [S3].
- Pre-orders open since Sept 2025 launch [S2]; CES 2026 demo in HUMANOID M.AX pavilion [S5]. R&D consortium with POSCO E&C, 7 shipbuilders, Hanyang & Pusan universities (mainly for the biped sibling) [S6]. No unit counts disclosed.

## Assessment (analyst view)
*Analyst opinion.* Strengths: the 1.3–1.8 m parallel-link height range is a real ergonomic differentiator (most wheeled rivals offer smaller lift strokes), and gearless back-drivable linear actuation is attractive for contact-rich, low-noise factory work; strong national-program backing and a marquee tier-1 automotive pilot (HL Mando). Weaknesses: tiny funding (~$7M) versus global rivals, no disclosed price/payload/reach, unclear software/SDK maturity, and a single pilot unit as traction. Threat to a new EU entrant: low-to-moderate — currently Korea-focused with limited export capacity, but the actuator IP and K-Humanoid Alliance scale-up funding could make it a credible mid-decade competitor in force-controlled manufacturing niches.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| S1 | http://www.arobot4all.com/ALICE_M1 | Official specs: 130–180cm/97kg, 31 DoF breakdown, parallel-link waist, sensors, compute, actuators | vendor-claimed |
| S2 | https://www.irobotnews.com/news/articleView.html?idxno=42352 | Launch 2025-09-11, 7-DoF arm, 1.3–1.8m working height, 3h runtime/1.5h charge, pre-orders | third-party |
| S3 | https://zdnet.co.kr/view/?no=20251202162140 | HL Mando Wonju deployment Dec 2025, M.AX program, wheeled platform description | third-party |
| S4 | https://www.smedaily.co.kr/news/articleView.html?idxno=306369 | Public demo of ALICE fetching commanded objects | third-party |
| S5 | https://us.aving.net/news/articleView.html?idxno=53052 | CES 2026 showing of ALICE 4 + M1 | third-party |
| S6 | https://zdnet.co.kr/view/?no=20251001030945 | Wheeled-M1-vs-biped-ALICE-4 deployment split, industrial partners | third-party |
