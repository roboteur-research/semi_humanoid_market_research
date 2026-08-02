# QA / gap-fill notes (accumulate during deep-dive phase)

- humanoid-uk (HMND 01): official domain is https://thehumanoid.ai/ (legal name SKL Robotics LTD).
  Site lists partners/clients: NVIDIA, AWS, SAP, Schaeffler, Siemens, Bosch, Ford, Martur Fompak.
  "Landmark deal" with Schaeffler for "thousands of humanoid robots". HMND 01 Alpha Wheeled payload 15 kg [vendor-claimed].
  → verify these landed in companies/humanoid-uk/ dossier; note Schaeffler also backs Hexagon AEON and reportedly Neura — Schaeffler multi-bets angle for the study.

## CN-A completed (agibot, galbot, astribot, pudu-robotics, keenon)
- 20 images verified. Blocked: astribot.com + galbot.com direct images (anti-bot); no deployment photos found (Fulin, Shangri-La, pharmacies) — gap-fill candidate.
- CORRECTIONS: Keenon XMAN-F1 is BIPEDAL (175cm/68kg/43 DoF, 2×6-DoF legs) — out of scope, documented as sibling. Genie G1: concept 11/2023, commercial release 2025-08-18 @ ¥450k; ">1,000 units" was data-collection ops/AgiBot totals, not G1 sales. Genie G2 official DoF = 26. XMAN-R1 height 174cm.
- CONFLICTS flagged in dossiers: Galbot G1 weight 85 vs 92.5kg, DoF 24 vs 47, runtime 8 vs 10h; Astribot S1 payload 10 vs 5 kg/arm, repeat ±0.03 vs ±0.1mm.
- OPEN: A2-W speed/reach/price; G2 price; D7 price + customers (none public!); XMAN-R1 payload/battery; Astribot Thundersoft 1000-unit order unverified; NO safety certifications published for any of the six.

## CN-B completed (ubtech, fourier, galaxea, dexforce, unitree, midea, robot-era)
- RESOLVED: Haier HIVA = customized/rebadged Robot Era Q5 (joint dev; Haier Capital co-led Robot Era Series A). CN-E should write haier/hiva as compact cross-reference dossier, not full research.
- CORRECTIONS: Galaxea R1 Pro payload 3.5kg rated / 5kg max PER ARM (~10kg dual combined), weight 96kg, compute 200 TOPS Jetson AGX Orin 32GB (550 dual-SoC = roadmap). Cruzr S2 hands gen-4 vs gen-5 conflict (flagged). Unitree R1-D: 4 SKUs (A5/A7 × fixed/wheeled), 15/19/18/22 DoF.
- NEW: Cruzr S2 Japan launch 2025-10-15 (GA Robotics), battery 30+3Ah ~8h. Unitree FY2025 GM 60.27%, >5,500 humanoids, 32.4% share, CSRC IPO approval 2026-07-03. DexForce Series B ~RMB 1B 06/2026 @ ~RMB 10B val, HK IPO plans.
- OPEN: Cruzr S2 price/compute; GRW sensing/compute/price; MIRO U hard specs; Q5 price/battery.
- Image notes: Galaxea recovered via Wayback (docs site 503); Midea renders JS-blocked (event photo only).

- Sharpa (sharpa.com, Singapore/MV/Shanghai): North robot is BIPEDAL (67 DoF) — excluded as robot entry; INCLUDE in tech-trends hand-supplier section: Wave hand 22 active DoF, 0.02N tactile, 1:1 proportions, CraftNet VTLA model.

## CN-C remainder completed (jaka, casbot, seer-robotics)
- CORRECTION: CASBOT 02 (灵贰) is a BIPED (163cm/55kg/33-36 DoF); wheeled models are CASBOT W1 (WAIC 2025) + W2 (2026): dual 7-DoF + multi-stage lifting chassis, sub-mm, -20°C validated. Dossier under casbot-02 slug carries correction — consider renaming folder to casbot/w1 during QA.
- CORRECTION: JAKA not SSE-listed — IPO withdrawn 12/2025, new PE round 04/2026. SEER listed HKEX H-shares 06/2026. C1-D chassis: 650×650mm, 150kg payload, 800mm aisles, SRC-4000 (X1 humanoid uses SRC-5000).
- IMAGE GAP: jaka/k1w images show WRONG robots (Lumi single-arm poster + K1 biped render) — replace during QA; no verifiable K1W photo found (JS SPA site).
- OPEN: K1W per-arm DoF/payload/battery; CASBOT W1/W2 payloads/pricing; X1-PRO battery/speed/customers.

## US-A completed (sunday, 1x, dexterity, weave, reflex, richtech)
- Memo images incl. "naked actuators" internals shot (WIRED ME). Sunday hardware DoF/battery/compute undisclosed.
- REFINEMENTS: Weave Isaac 1 official 21 DoF (2 neck, 2×6 arms, 2×1 hands, 2 torso, 3 base), 8h, 80"/38" reach, "fall 2026". 1X EVE: 6'2"/192lb/9mph/33lb/6h (4h per contrary — conflict noted); EE = Robotiq 3-Finger gripper, NOT in-house. Dexterity Mech arms MANUFACTURED BY KAWASAKI (HiWin components); 29kg/arm (TRR) vs 60kg dual. Reflex: $7-7.3M seed Khosla, target <$50k, Nuevo León plant (announced by Gov. Samuel García 2026-02-02). Richtech Dex: NO customer as of 12/2025.
- Sacra WebFetch hallucination guard: ignore "165M" valuation, use $1.15B (TechCrunch).
- OPEN: ADAM height/DoF (richtech site bot-blocked even via archive); ARCO/ampm unverified; Everon 150-250 units estimate-grade.

## US-B remainder completed (dexmate, aeolus, trossen)
- CORRECTIONS: Dexmate Vega payload 10+ lbs (~4.5kg)/arm vendor-claimed (15kg = unverified 3rd party); MSRP $89,999; battery = 10-30h vendor range. Trossen Stationary AI now $23,995.95 list ($15,995 sale) — $8-17k band belongs to Solo AI; Mobile AI $22,995-33,695. Aeolus: + Wroclaw software office; customer-investor loop (Gakken Cocofump, Saint-Care both operators AND investors); quiet since CES 2023.
- NEW: Dexmate ~$41M funding incl. LG Tech Ventures/LG CNS (2026), Jetson AGX Orin→Thor upgrade, Vega-U university variant.
- IMAGE note: trossen mobile-ai-robot-front.jpg is actually the TOTL workstation tower (honestly captioned); replace or drop at QA.
- WebSearch quota RECOVERED — future agents can use WebSearch again (DDG/Bing HTML now bot-blocked, prefer WebSearch).

## CN-E completed (11 companies)
- CORRECTIONS: Mercury X1 19 DoF, $15,999, 1kg/arm only, 450mm reach, Jetson Orin Nano SUPER; B1 = 17 DoF; weight conflict 55 vs 62.5kg flagged. iSageBot: 100+ LOIs = six-arm MAHAKBOT (not SageMan); 280kg, 3-16kg/arm. Canbot U06 = 38-DoF wheel-leg hybrid from 2019 (early!). Sanbot Max = Sanbot King Kong (1455mm/100kg/mecanum/75kg towing; 5 m/s claim implausible — flagged). KNEWBOTS = ThunderSoft (SZSE 300496) subsidiary, Hangzhou; wheel-arm 35 DoF, 4.5kg/arm, i7+Orin AGX. Zoomlion: 8 embodied prototypes by end-2025; biped Z01 exported.
- OPEN: B1 vendor price (EU reseller €17.6k); GoMate 2026 production; Zoomlion wheeled model names; uurobot.com geo-blocked.

## JP-C completed (9 companies)
- CORRECTIONS: MELTIN MMI DISSOLVED 2024-11-28 (MELTz → Sumitomo Pharma/FrontAct 06/2024). Epson W-01 sales ended 2020-12-31 (03/2021 = notice date), support to 2027-12-31. Fujitsu enon: 10kg = torso cargo bay, arms only 0.5kg (5-DoF). ROBEAR lab closed 03/2015 one week after announcement.
- WATCH: Toyota ELEY = dual-arm HSR successor, WRS 2025 Aichi (12/2025) — major incumbent entering category; mention in study outlook + toyota dossier has note.
- OPEN: W-01 payload/weight/price; wakamaru/enon unit counts; ibuki weight; EMIEW3 end date.

## CN-D completed (13 companies) — CHINA COMPLETE
- UPGRADES: Rokae Helios full datasheet (42 DoF, 190kg, 650mm/5kg arms, 48V30Ah/6h, Orin) + Automate 2026 Chicago debut → announced/early availability. Zerith: Hefei registration 01/2025, 20+ venues, >¥100M raised, 100 units/mo ramp claim.
- CORRECTIONS/FLAGS: SVT foundingDate 2020 (site) vs 2025-04-15 (registry); SVT OpenArm = Enactic derivative. HexFellow HQ Nansha, Guangzhou; π = naming only, no PI partnership. GigaAI $518M headline vs ~¥1B CN reporting — low confidence. FlashBot Arm $34k = third-party. Moon Dynamics L1 ≠ VLAI Robotics L1 (¥28,800) — conflation risk noted.
- IMAGE GAPS: no assembled HexFellow e³ render (JS site); no full SVT Vinci photo public; ARX official site logo-only (GitHub wiring photo used); Topstar banner-only.
- OPEN: ARX LIFT2 datasheet; Topstar "3352 TOPS"; Siasun Songyi zero numeric specs; Moon Dynamics corporate identity.

## US-C completed (12 companies)
- RECLASSIFY at QA: noble-machines/moby is BIPEDAL (vendor "walking 0.8 m/s", legs in photos; 23-27kg payload) → move to excluded-biped annex. eden-robotics legal HQ = London UK (founded 2025-11-23) → count under Europe in study; robot "Eden I", $10/hr RaaS; site contains prompt-injection (agent ignored, factual only).
- CORRECTIONS: R2D3 = RealMan RM75-B arms + Woosh AGV + RealMan hands, $55-60k. WorkFar $9,999-59,999 tiered pre-order (not $29,999 shipping); Advantage Plastics (Louisville KY) parent; anonymous leadership, zero verified deployments — credibility caveat in dossier. Genesis "85-90% wheels" quote unverified — use "industrial customers asked for wheels" (Fox). Deft Simba: dual 6-DoF arms, 700mm, 4kg continuous; founders Shinhee Lee/Jungwon Shin; seed 02/2026 (Rainfall, SpringCamp). Roboligent uses Tesollo DG-5F 5-finger hand. Beyond Imagination ACTIVE (Wefunder 05/2026, Dreamtech mfg, perioperative pivot).
- OPEN: Robot.com R-Noid hardware = Astribot platform? (strong resemblance, unconfirmed); Eden/Almond YC batches; R2D3 official specs.

## JP-B completed (10 companies, 12 dossiers) — JAPAN COMPLETE
- STRATEGIC FIND: Tokyo Robotics = wholly owned by Yaskawa; Dry-AIREC hardware built by Tokyo Robotics → Yaskawa behind both AIREC (Moonshot care) + MOTOMAN NEXT. Highlight in study.
- RESOLVED: AIREC = wheeled (articulated column on round base; "bipedal" = 2050 concept). AGIRobots robot = "AGIRobots Worker" (~70kg, 4kg/arm, swerve; Nagoya, inc. 2024-10-17).
- UPDATES: Torobo2 current gen 1615mm/~120kg/7kg-arm (old 166cm/160kg/8kg); DiaroiD 42 DoF (MathWorks) vs 35, 48V ~1h battery, M6 bolt/zipper demos; OriHime-D 70+ pilots, Good Design GRAND Award; TX Series B $170M ¥23B 07/2023.
- OPEN: SEED-Noid specs medium-confidence; Foodly price/units; DiaroiD dims; Torobo pricing.

## Image QA escalation (user catch, 2026-08-02)
- mitsubishi-electric/diaroid: BOTH original images were wrong (telescope-systems slide + corporate logo grabbed from CuboRex article). Replaced with visually verified photos: diaroid-tradeshow-cugo-mega.png (real robot, internals visible) + cugo-mega-crawler-unit.png (base render).
- CONSEQUENCE for QA pass (task #3): file-type/size checks are INSUFFICIENT. The QA agent must VISUALLY inspect every downloaded image (Read tool renders them) and verify each shows the claimed robot. Known suspects already flagged: jaka/k1w (wrong robots), trossen mobile-ai-robot-front.jpg (PC tower), qihan (shows Elf not Max — acceptable, captioned). Batch-check everything else.

## US-D completed (14 companies) — US/CANADA COMPLETE
- REFINEMENTS: Rethink 2nd shutdown 08/2025 (IP fate unresolved). Mobile ALOHA 1.42 m/s, 1.26 kWh/14kg battery, 1.5kg/arm effective. MOVO support ended 2023-07-14, 0/1/2-arm configs, 8-27 DoF. Robonaut 2 weight conflict 140 vs 150kg flagged; leg failure = missing return wire; now at Smithsonian. BEAR = Vecna Technologies (Vecna Robotics = 2018 spinout). uBot-7: first wheeled dynamic balancer w/ SEAs claim.
- IMAGE notes: agent visually caught+fixed wrong Cody image (robotsguide CDN mixes photos — systemic hazard, QA should be suspicious of robotsguide-sourced images); Anybots Monty only 216×144px survives (acceptable, noted).
- OPEN: MOVO price (~$100k est); Baxter units; Punyo arm vendor; Hstar fate.

## EU-B completed (10 companies)
- RESOLVED: Wandercraft Calvin-40 = BIPEDAL ("first two-legged headless robot", Renault Douai; 80kg weight, 40kg payload, 28 DoF; $75M Series D w/ Renault; 350 units ~2027) → EXCLUDED-as-biped, dossier kept as annex context. QA: move out of main matrix. UMA Northstar: wheeled Version 0 first (2026-07-07, tethered); biped roadmap only; ~$40M seed.
- CORRECTIONS: Mojin Robotics → renamed 4am Robotics GmbH (2023-04-13, AMR vendor); Care-O-bot 4 COMMERCIALLY DISCONTINUED. Oversonic certs = CE MD 2006/42/EC + ISO 27001 + EMC + IPX4 — NO ISO 13482/10218/medical (deflate claim in study); STM/ENEA equity mid-2026; revenue €4.5-5M 2025. Engineered Arts $10M Series A = Helium-3 Ventures (Matt Bellamy), NOT Alphabet. Hexagon AEON: BMW Leipzig test 12/2025→pilot summer 2026; Schaeffler = customer AND actuator supplier.
- OPEN: Oversonic units/pricing; Reachy 2 reach/battery; Robody hw specs; AEON price ("$20k" implausible); Prosper activity post-2025; Macco count.

## EU-C completed (12 companies) — EUROPE COMPLETE
- CORRECTIONS: Cybedroid liquidated 07/2019 (raise 2017-05-23; ~10 units, 6 sold). IIT R1: official PDF 1.15-1.35m torso, 1kg/arm (site now claims 1.45m/1.5kg — flagged). Haddadin→MBZUAI 01/2025 verified; NEW GARMI redesign 2026-01-22; NO GARMI spin-off exists (spin-off intent unverified). ARMAR-7: 3 omni-wheels + 2-DoF knee/hip (not lift column); also Hannover Messe 2026. Clone: ~$17M funding, $50M round underway, Mountain View office.
- OPEN: ARMAR-7 h/w/payload; GARMI dims/battery; Alter-Ego weight; Clone Torso price/deliveries.

## ROW-C completed (15 companies)
- NEW FACTS: I.L = KOSDAQ 307180 (ex-IL Science), 2 ILBOTs in mass production (IL Mobility) from 02/2026 — earliest of Korean 03/2026 wave; ILBOT L1 MAX wheel-leg quadruped 06/2026. T-Robotics: KRX-listed 2004 incumbent (vacuum transfer robots); declared wheeled hybrid its FINAL form ("will never build legs") — quotable. Alfa Robotics defunct (domain now unrelated blog). KP-BOT withdrawn from duty by 2025 (INR 21.24 lakh) — reception-robot cautionary datapoint. Nadine → MIRALab Geneva 2022, LLM re-arch arXiv 2405.20189. M-Hubo IROS 2019: 20 DoF, 0.8m reach, 48V 11Ah, VLP-16, PODO/ROS. XLeRobot 5.4k stars, Wowrobo kit $579.
- Paaila vs CloudMinds "Ginger" disambiguation done in dossiers.
- OPEN: Billy prototype (H1 2026 promise) unshown; TR Works/ILBOT zero hard specs; QSS claims unverified.

## ROW-B completed (11 companies) — ALL DEEP-DIVE BATCHES DONE
- VERIFIED: Alice M1 = wheeled AMR + double parallel-link waist, 1300-1800mm, 97kg, 31 DoF, AGX Orin; HL Mando Wonju deployment 12/2025; Series A ~$7.2M. (Press "50kg/Orin NX" wrong.)
- RECLASSIFY at QA: mentee-robotics/menteebot-wheeled — wheeled variant DOES NOT EXIST (confusion w/ Humanoid HMND-01); dossier documents this; move robot to excluded/nonexistent annex, keep company for Mobileye acquisition ($900M, closed 2026-02-03, production 2028). samsung/bot-handy: "Handy 2" dual-arm = single aggregator, likely fabricated — marked unverified.
- UPDATES: Vyommitra G1 flight slipped to Q3 2027 (risk 2028). AMBIDEX arm 2.6kg, ~3kg payload, 5 m/s tip. Invento wound down hardware (~3 staff, AI-training pivot).
- OPEN: Alice price; ADA-7 h/w/price; GenBot arm specs; Perceptyne customers; Svaya funding.

## Gap batch completed (duatic, lg, promobot, hanson, unlimited) — ALL DOSSIERS COMPLETE
- MAJOR MARKET FACT: July 2026 US FCC ban on foreign-made humanoid-robot imports — must feature in study (US market access for CN/RU vendors; boosts US/EU domestic makers). VERIFY primary source during compile.
- CORRECTIONS: Promobot Robo-C DISCONTINUED ("humanoid project is over"). Duatic DynaArm 6kg cont/12kg 10s standalone (not 12.5); founders Dhionis & Dimitris Sako. LG CLOiD pilot production 07/2026; Dexmate investment via LG CNS/LGTV 03/2026. Gary lift column UNCONFIRMED (flagged); Philadelphia ~10 units since 07/2024, hospital unnamed.
- OPEN: Duatic 2026 round/LogiMAT; Sophia price/units unverifiable; Promobot audited numbers.

## Image audit part 1 (CN+JP) completed
- 153 checked, 141 OK, 12 deleted (logos/text-slides/wrong products incl. hospital-exterior, nurses-group, RViz screenshot, Astribot-branded crowd shot), 6 verified replacements. JAKA K1W: still no genuine K1W photo exists publicly (K1 biped render kept, honestly captioned).

## Image audit part 2 completed (Americas+EU+RoW)
- 197 checked, 191 OK, 6 deleted (logos ×3, PC tower, fake PR2 = Barrett WAM rig, AI-art clickbait), 4 verified replacements. Eden I: no public robot imagery exists (folder imageless, documented). AUDIT TOTALS: 350 images inspected, 18 deleted, 10 replaced.

## Inline additions during QA (user tips)
- companies/franka/fr3-duo (T2, prototype, Automatica 2025, full official specs) — German reference platform, Agile Robots group.
- companies/prinlab/panda-dual-arm (T3 research, NII Tokyo, Kobayashi) — component-ecosystem build (Panda + qb SoftHand2 + TriOrb).
- companies/hello-robot/stretch-3 (BORDERLINE single-arm, $24,950) — borderline annex only, NOT main matrix.
- xlsx builder: must exclude borderline/excluded entries from main matrix → add "Borderline & excluded" sheet driven by notes/base_type flags (stretch-3, menteebot-wheeled, moby, calvin-40, hexagon aeon + moon-dynamics l1 flagged wheel-leg, tencent the-five, gac gomate, ultra op1).

## Toyota lineage completed (user-driven)
- toyota/hsr added (borderline single-arm archetype, official Toyota UK specs + press photo).
- toyota/eley PROMOTED from watch-item to full dossier: official Frontier Research article 2026-03-31 — WHEELED dual-arm confirmed by render; QDD in every joint (≤10:1), scapular axis, direct drive (no belts), imitation learning w/ 1h data cycle; Potaro + KumiPro spin-offs; self-declared gaps (reliability/repeatability/data infra). Study outlook: Toyota = highest-credibility JP entrant.

## Freshness sweep completed (2026-08-02)
- FCC BAN VERIFIED: FCC PSHSB Public Notice DA 26-786 (2026-07-28), Covered List addition: "foreign-produced advanced robotic devices" except DoW Conditional Approval. Definition: mobile ground device >4.4 lbs w/ sensor + ≥200kbps connectivity + AI. EXCLUDES fixed industrial robots, vehicles, FDA medical. Wheeled/tracked semi-humanoids IN SCOPE; applies to new device models (not previously authorized units); "foreign-produced" = not domestic end product per 48 CFR 25.101(a). Cite DA 26-786 PDF: https://docs.fcc.gov/public/attachments/DA-26-786A1.pdf — STUDY MUST FEATURE (ch. regulatory + regional outlook).
- NEW DOSSIERS NEEDED: walden-robotics (T1! $300M seed @ $1.1B, Toyota+Deviation co-led, TRI spinout, deployed at Toyota plants, out of stealth 2026-07-15); realman/realbot (T2, WAIC 2026: S2 folding 40cm + L2 lifting torso 9kg/arm 15kg dual, 50k h MTBF modules); haohai-xingkong/juliet (T3, Shanghai retail pods); astribot/t1 (new robot subfolder: $14k, 1.55m, 23 DoF, 5kg/arm, launched 2026-05-28); neuromeka/eir (VERIFY base type first).
- NEWS UPDATES to fold into dossiers: AI2 ~$735M @ ~$2.8-3B (07/2026); Astribot Series B >¥1B unicorn + joint-stock conversion (pre-IPO); AgiBot 15,000th robot (06/2026) + G2 at STK Seoul; Neura Series C CONFIRMED up to $1.4B (CNBC 2026-06-10, Amazon/Nvidia); RB-Y1 Coupang pilot CONFIRMED (nate 2026-01-15); Humanoid UK $152M Series A @ $1.35B post (07-21), Beta Q4 2026, KinetIQ Ascend; Zerith 3 rounds in 6 months; humanoid startups $8.6B YTD 2026 (1.8x all 2025).
- EXCLUSION ANNEX ADDITION: Collaborative Robotics Proxie Gen 2 (dual-arm cart, non-anthropomorphic, 06/2026). Correctly excluded: RoboParty RP1, LimX, AIRBOT, Zhishen NE01, Qiyuan T1 (wheel-foot transformer — watch note).
- AgiRobots: cite robotstart 2026-03-02 primary, drop TBA framing.

## RobCo Alfie added (user catch, 2026-08-02)
- Munich RobCo (modular kits, Sequoia/Lightspeed, $100M Series C 2026-01-29) announced bimanual humanoid-form "Alfie" 2026-04-15, Hannover Messe preview, RaaS, deployments "later this year". Base UNDISCLOSED — official render deliberately ends at waist (waist column visible). In-scope regardless (pedestal torsos qualify). Corpus now 193/181 main. Germany count 12. WATCH: reveal of lower body will determine wheeled vs pedestal classification.
- RobCo Alfie base RESOLVED (user video tip): promo video 0:14 shows full Alfie in simulation with broad mobile-style base platform → classified "probable wheeled" [estimated]; frames archived in dossier. Watch official confirmation.
