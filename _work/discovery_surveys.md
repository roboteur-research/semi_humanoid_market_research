# Discovery: Survey-list harvest (awesome-robot-descriptions, robotsguide, Wikipedia, MuJoCo Menagerie, GitHub)
Agent sweep completed 2026-08-02. NEW finds vs regional sweeps marked ★.

## NEW commercial finds (★)
- ★ Wandercraft, France — Calvin-40. Wheeled. SHIPPING/DEPLOYED (2025, Renault plants; 350 units planned by 2027). 170cm, 28 DOF, 40 kg payload industrial semi-humanoid. https://www.wandercraft.eu — MAJOR Europe miss (company known for exoskeletons).
- ★ Elephant Robotics, China — Mercury X1 (+ Mercury B1 torso). Wheeled AGV + two 7-DOF arms + tablet head. SHIPPING 2024 research/edu. https://robotsguide.com/robots/mercuryx1 | https://www.elephantrobotics.com
- ★ ByteDance Seed, China — ByteMini. Wheeled, 22 DOF bimanual. RESEARCH 2025 (embodies GR-3 VLA). https://seed.bytedance.com
- ★ TOSY, Vietnam — TOPIO Dio. 3-wheel, 28 DOF hospitality. Announced 2010, unclear/defunct. Wikipedia.
- ★ Paaila Technology, Nepal — Ginger (+ Pari). Wheeled waiter/bank robot, Kathmandu, shipping regionally 2018–. NOTE: awesome-robot-descriptions misattributes GingerURDF (= CloudMinds Ginger) to Paaila.
- ★ Vecna, US — BEAR. TRACKED dynamically balancing casualty-extraction torso, 227 kg lift. Discontinued prototype ~2005-11. https://robotsguide.com/robots/bear
- ★ Hstar Technologies, US — RoNA. Wheeled nursing dual-arm, 226 kg patient lift. Prototype 2011-15.
- ★ RE2 Robotics (Sarcos), US — HDMS. Dual-arm torso on tracked EOD robots. Delivered to defense.
- ★ Anybots, US — Monty. Two-wheel teleop dual-arm. Prototype 2007, discontinued.
- ★ Hitachi, Japan — EMIEW/2/3. Two-wheel balancing 90cm, gestural arms. Prototype/pilots 2005-16.
- ★ Toyota, Japan — Robina (Partner Robot family). Wheeled guide humanoid, 2007 demo.
- ★ Clone Robotics, Poland/US — Clone Torso. Fixed musculoskeletal water-hydraulic upper body. Prototype.

## NEW research finds (★)
- ★ DFKI Bremen, Germany — AILA. 6-wheel, female-form dual-arm. ~2010. https://robotsguide.com/robots/aila
- ★ KIT ARMAR-III (2006, kitchen). (ARMAR-6/7 already known.)
- ★ TUM — TOMM (two UR5 + full-body skin, 2017); Rosie (mecanum + two KUKA LWR-4, pancakes, ~2009-13 retired).
- ★ Univ. Bonn NimbRo — Dynamaid & Cosero. Omni wheeled RoboCup@Home champions 2009-14.
- ★ TU Eindhoven — AMIGO (+ SERGIO). Omni wheeled dual-arm.
- ★ CMU Ballbot with arms (ball-balancing HRI).
- ★ Georgia Tech — Golem Krang (2-wheel balancing dual-arm), Cody (Segway + two Meka arms, nursing), Simon (pedestal social torso).
- ★ MIT — Cog (1993-2003), Domo (2004-07), Nexi MDS (2-wheel balancing). NRL Octavia (MDS firefighting). USC Bandit (Pioneer base, therapy). UMass uBot-5/6/7 (2-wheel balancing).
- ★ Stanford PR1 (Salisbury, 2006 — PR2 predecessor).
- ★ Meka Robotics M1 (+ Dreamer head) — omni wheeled compliant dual-arm; acquired by Google 2013.
- ★ KIST/Samsung Mahru-M (wheeled Mahru variant, 2008-11). A*STAR Olivia (Singapore, pedestal receptionist ~2010). ECCEROBOT ECCE (UK/EU tendon-driven torso on trolley).
- ★ Waseda WENDY (1999, Twendy-One predecessor). RIKEN RI-MAN (2006).

## NEW open-source/hobbyist (★)
- ★ InMoov (FR, 3D-printed torso, 2012–). Poppy Torso (Pollen/Inria). 
- ★ XLeRobot — 3 omni wheels on IKEA RÅSKOG cart + two SO-100/101 arms, ~$660 kits 2025. https://github.com/Vector-Wangel/XLeRobot
- ★ BamBot — ~$300 dual-SO-arm wheeled. https://bambot.org
- ★ Salvius (wheelchair base). Unverified GitHub: OpenFlex, AlohaX/AlohaMini, finn, VnRobo VNR-WH1.

## Confirmations/enrichments of known entries
- Astribot S1 research editions ~$50k. Pudu D7 ~$70k. Galbot G1 47 DOF total (12-DOF hands). AgiBot A2-W ~$80k. Genie G1 26 DOF, variable height 1.3-1.8m. TIAGo Pro ~$85-95k. Oversonic RoBee 175-190cm, 10 kg bimanual, 40 joints. Keenon XMAN-R1 deployed Shangri-La hotel 10/2025. Sanctuary pivoted to software 2026. UniX AI newer "Panther" model. Menagerie has pal_tiago_dual; halodi-robot-models for EVE; rby1_description; sciurus17_description; baxter_common; nasa r2_description; poppy_torso.
- URDF/description repos exist for: Galaxea R1 (userguide-galaxea/URDF), Spirit Moz1 (issac_moz1), CloudMinds Ginger (Rayckey/GingerURDF).

## Borderline collections (for completeness section)
- Single-arm: HSR, Stretch, Fetch, Moxi, EL-E, Care-O-bot 3, TIAGo single, Everyday Robots, TidyBot, Bot Handy, DLR EDAN, KUKA youBot, Robotnik RB-1/KAIROS/VOGUI, Ridgeback rigs, BD Handle, GITAI S1/S2.
- Dual-arm non-anthropomorphic: Mobile ALOHA, AgileX Cobot Magic, Trossen kits, Kawasaki duAro, Sarcos Guardian GT, HDT Adroit, OriHime-D (gestural).
- Centaurs/wheel-leg: IIT CENTAURO, Bonn Momaro, JPL RoboSimian, Tencent The Five, GAC GoMate, LimX TRON2-WF, GITAI R1 rover. Quadruped+arm noted, excluded.

## Method notes
- robotsguide.com serves full content to browser UA via curl; sitemap enumerates all profiles.
- Wikipedia "List of humanoid robots" 404s; category pages usable.
- Isaac Sim assets: no semi-humanoids beyond arms/bases. Menagerie semi-relevant: TIAGo++, Stretch, TidyBot, Google Robot, ALOHA.
- KIST CIROS could not be independently verified by this agent (RoW agent had 2 sources — OK).
