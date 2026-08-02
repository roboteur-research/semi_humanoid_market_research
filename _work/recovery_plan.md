# Recovery plan (2026-08-02) — cap raised to 5 concurrent agents (user OK, mem ~3.2GB)
# RULE: all agents write per-company incrementally (playbook updated) — never batch writes at end.

## Audit result
41 complete / 23 partial / 111 missing robots (see qa_notes.md). JSON all valid.

## Wave R1 (RUNNING)
- CN-B resume → robot-era/q5 only
- CN-C-remainder (fresh) → jaka/k1w, seer-robotics/x1-pro, casbot/casbot-02
- US-A redo (fresh) → sunday memo, weave isaac-1, reflex, richtech adam+dex, 1x eve, dexterity mech (images exist, text missing)

## Wave R2 (next; try resume first, else fresh)
- US-B remainder → dexmate/vega (company.md exists, rest missing), aeolus/aeo (1 img, text missing), trossen/mobile-ai (1 img, text missing). COMPLETE already: sanctuary, dyna, boardwalk, apptronik, roboforce.
- EU-A remainder → duatic/alpha (2 imgs, text missing). COMPLETE: pal×3, neura, enchanted, igus, humanoid-uk.
- ROW-A remainder → lg-electronics/cloid, unlimited-robotics/gary, promobot/v4+robo-c, hanson-robotics/sophia, neubility/billy, t-robotics/tr-works, il-robot/ilbot (all have images, no text). COMPLETE: rainbow, robotis, xyz-corp. NOTE: neubility/t-robotics/il-robot folders prove the agent verified the Korean article robots qualify — write compact T3 dossiers.

## Wave R3
- CN-D (fresh): pudu-robotics/flashbot-arm (NEW — add to EXISTING pudu folder, authorized), hexfellow/e3 (NEW), svt-robot/vinci (NEW — both master_list addendum 2), cloudminds/ginger, siasun/songyi, rokae/helios, topstar/twh020, psibot/psi-v1, arx/lift2, agilex/cobot-magic, zerith/h1, gigaai/maker-h01, moon-dynamics/l1
- CN-E (fresh): isagebot/sageman, elephant-robotics/mercury-x1, bytedance/bytemini, pndbotics/adam-u, zoomlion/wheeled-humanoid, tencent-robotics-x/the-five, gac/gomate, canbot/u05, qihan/sanbot-max, knewbots/wheel-arm, haier/hiva (resolve Q5-rebadge conflict)
- JP-B (fresh): rt-corporation/foodly+sciurus17, thk-seed/seed-noid, telexistence/model-t, mitsubishi-electric/diaroid, tokyo-robotics/torobo, honda/avatar-robot, ory-laboratory/orihime-d, waseda/airec+twendy-one (resolve AIREC base conflict), agirobots/semi-humanoid-tba

## Wave R4
- JP-C (fresh, T3): meltin, epson, riken, mhi, fujitsu, vstone, osaka-university, hitachi, toyota, gitai
- US-C (fresh, T2): eden-robotics/eden (NEW, T3), opendroids/r2d3 (NEW), deft-robotics/simba (NEW — both in master_list addendum 2), genesis-ai/eno, robot-com/r-noid, roboligent/robin, almond-ai/axol, workfar/syntro, noble-machines/moby, beyond-imagination/beomni, palladyne/guardian-xt, ultra-robotics/operator-op1
- US-D (fresh, T2/T3): stanford/mobile-aloha, willow-garage/pr2, rethink-robotics/baxter, kinova/movo, nasa/robonaut-2, tri/punyo, cmu/herb, georgia-tech/cody, mit/domo, meka-robotics/m1, vecna/bear, hstar/rona, anybots/monty, umass/ubot

## Wave R5
- EU-B (fresh, T1/T2): pollen-robotics/reachy-2, oversonic/robee, wandercraft/calvin-40 (RESOLVE wheeled-vs-biped), devanthro/robody, mojin-robotics/care-o-bot-4, prosper-robotics/alfie, engineered-arts/ameca, uma/northstar (verify base), hexagon/aeon (borderline note), macco/kime
- EU-C (fresh, T2/T3): dlr/rollin-justin, kit/armar-7, tum/garmi, fzi/hollie, iit/r1, unipi/alter-ego, cybedroid/leenby, dfki/aila, nimbro-bonn/cosero, tu-eindhoven/amigo, roboy/roboy-3, clone-robotics/clone-torso, luxai/qtrobot
- ROW-B (fresh, T2): genrobotics/genbot (NEW — master_list addendum 2), a-robot/alice-m1, samsung/bot-handy, naver-labs/ambidex, hyundai/dal-e, mentee-robotics/menteebot-wheeled, invento/mitra, isro/vyommitra, akinrobotics/ada-7, perceptyne/pr-34d, svaya-robotics/bimanual

## Wave R6
- ROW-C (fresh, T3): nyro/nyro (NEW — hobbyist, master_list addendum 2), kaist/m-hubo, kist/ciros, asimov-robotics/kp-bot, alfa-robotics/kiki, qss/sara, ntu-singapore/nadine, tosy/topio-dio, paaila/ginger-np, techman/tm-xplore-1, andromeda-robotics/abi, xlerobot/xlerobot, bambot/bambot, inmoov/inmoov

## Then
QA pass (task 3) → xlsx (task 4) → PDF (task 5).
