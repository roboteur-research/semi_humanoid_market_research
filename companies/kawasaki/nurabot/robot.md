# Nurabot — Foxconn × Kawasaki Heavy Industries (× NVIDIA)

> Nurabot is a nursing-assistant semi-humanoid co-developed by Foxconn (Hon Hai) and Kawasaki on the Nyokkey platform, with NVIDIA supplying the AI stack (FoxBrain LLM, Jetson Orin, Isaac for Healthcare digital-twin training). Piloted at Taichung Veterans General Hospital (Taiwan) since April 2025 with a claimed 20-30% reduction in nursing workload, it targets FY2026 commercial launch — the most credible near-term path to volume deployment of dual-arm service humanoids in Asian hospitals.

| Field | Value |
|---|---|
| Company | Foxconn (Hon Hai Technology Group) + Kawasaki Heavy Industries; AI stack: NVIDIA |
| HQ | Taipei, Taiwan / Tokyo-Kobe, Japan |
| Status (2026) | prototype (hospital field trials; FY2026 launch target) |
| First shown / launch | Announced/shown 2024 (Foxconn Tech Day/GTC); trials from April 2025; co-development formalized publicly 4 July 2025 |
| Target applications | Nursing support: medication/specimen delivery, wound-care kit transport, patient & visitor guidance, night ward patrol, hygiene education |
| Price | n/a (not disclosed) |
| Availability | Taiwan pilots; FY2026 market launch target (Asia healthcare first); TCVGH plans "dozens of units" by end of 2025 |

## Design & morphology
Nyokkey-derived wheeled dual-arm platform, "specially designed" for hospitals: two grasping arms, an enclosed **cargo compartment** for secure medication/specimen transport, self-driving base [S1]. Dimensions/weight n/a (not disclosed; Nyokkey basis ~150cm/75kg). Softer nurse-styling shell than Nyokkey.

## Locomotion
Autonomous indoor navigation in live hospital wards, including night patrol routes; elevator/building integration inherited from Nyokkey [S1][S2]. Speed n/a (not disclosed).

## Upper body & manipulation
Two arms "capable of grasping objects" — handing over wound-care kits, delivering medications and specimens [S1]. Arm DoF/payload n/a (not disclosed; Nyokkey basis 2×6-DoF, 6kg). Future roadmap: patient mobility assistance (transfer support) [S2].

## Sensing
Camera/vision suite processed through **NVIDIA Holoscan** sensor pipeline; speech recognition mics + TTS output for patient interaction [S2]. Individual-recognition (patient identification) planned [S2].

## Actuation & power
n/a (not disclosed); battery-electric (Nyokkey basis).

## Compute & software
Onboard **NVIDIA Jetson Orin** edge computer [S2]. Conversational AI: **FoxBrain**, Foxconn's own LLM (trained on NVIDIA Hopper GPUs), giving Chinese-language (and planned multilingual) patient dialogue [S2]. Training: **NVIDIA Isaac for Healthcare** — Nurabot skills (navigation, manipulation in ward layouts) trained in a **digital twin of TCVGH** built in Omniverse before physical deployment; Foxconn's smart-hospital platform (CoDoctor/CoCare ecosystem) provides the hospital-IT integration [S2, vendor-claimed]. Kawasaki contributes robot control and Successor-derived teleop/skill-transfer tech [S1].

## Safety & compliance
Hospital field-trial under TCVGH clinical governance; formal certifications n/a (not disclosed). Night-patrol and delivery roles keep it out of direct patient-handling risk for now.

## Deployment evidence & traction
- **Taichung Veterans General Hospital (TCVGH), Taiwan**: field trials since **April 2025** — medication/specimen delivery across wards, wound-care kit transport, visitor guidance, night ward patrol [S1][S2].
- Claimed results: **20-30% reduction in daily nursing workload** (manufacturer/hospital-cited, 09/2025) [S3, third-party-reported vendor claim]; nurses report fewer physical trips [S2].
- TCVGH stated intent to deploy **"dozens of units"** by end of 2025 [S2, third-party].
- Market launch target: **FY2026** [S1, vendor-claimed]. First use of Kawasaki's Nyokkey platform in medical settings outside Japan [S1].
- Broader program: Foxconn smart-hospital rollout across Taiwan hospitals (CNN coverage 09/2025) [S3].

## Assessment (analyst view)
*Analyst opinion.* Nurabot pairs the two things hospital robotics usually lacks: a manufacturing giant (Foxconn) that can build thousands of units cheaply, and a robot OEM (Kawasaki) with certified-machine engineering discipline — plus NVIDIA's full healthcare-AI stack as reference design. The TCVGH digital-twin-first methodology materially de-risks deployment and will be the template NVIDIA markets worldwide. Weaknesses: task set today equals what Diligent's Moxi (single-arm) already does at ~50 US hospitals; the dual arms are not yet doing patient-contact work that would justify the humanoid form; and specs/pricing remain opaque. Threat to an EU entrant: high in Asia healthcare and medium in the EU by 2027-28 — if Foxconn hits FY2026 volume pricing, EU healthcare semi-humanoids (Mirokai, MiPA-class) will face a subsidized-scale competitor; EU medical-device regulation is the main moat/delay.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://global.kawasaki.com/en/corp/newsroom/news/detail/?f=20250704_7252 | co-development, functions, cargo compartment, TCVGH trials 04/2025, FY2026 target, Nyokkey basis, quotes | vendor-claimed |
| 2 | https://blogs.nvidia.com/blog/foxconn-smart-hospital-robot/ | Jetson Orin, FoxBrain LLM, Holoscan, Isaac for Healthcare digital twin, task list, "dozens of units", nurse quote | vendor-claimed (NVIDIA) |
| 3 | https://www.cnn.com/2025/09/12/tech/taiwan-nursing-robots-nurabot-foxconn-nvidia-hnk-spc | 20-30% workload-reduction claim, Taiwan rollout context | third-party |
| 4 | https://roboticsandautomationnews.com/2025/07/04/kawasaki-develops-nurse-assistant-robot-with-foxconn/92886/ | independent confirmation of co-development announcement | third-party |
