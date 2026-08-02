# Sean — Zeroth Robotics (ZeroTh)

> Compact wheeled dual-arm research/service prototype from heavily angel-funded Chinese startup Zeroth: 155 cm, 16 DoF, three-finger grippers on a rounded wheeled pedestal base, pitched at "reliable handling and safe human interaction in structured environments" — deliberately simple rather than anthropomorphically maximal. Competitive significance is limited; it matters mainly as evidence of Zeroth's hardware capability behind its ~$351M valuation.

| Field | Value |
|---|---|
| Company | Zeroth Robotics (ZeroTh) |
| HQ | Jiangsu, China |
| Status (2026) | prototype [S1] |
| First shown / launch | listed March 2026 on humanoid.guide; not on current vendor site (likely earlier internal platform) [S1][S2] |
| Target applications | AI development, research, home assistance, retail |
| Price | ~USD 65,000 (third-party listing) [S1] |
| Availability | not commercially available; no ordering channel found |

## Design & morphology
Dual-arm torso on a black central column over a rounded white wheeled pedestal base (verified image); boxy black head with stereo camera bar and eye-like indicators; exposed cabling and joint modules signal prototype maturity. Height 155 cm, weight ~45 kg, 16 DoF overall [S1]. An additional small leader/teleop arm is visible mounted at the right shoulder in the verified image (estimated interpretation). E-stop on torso column.

## Locomotion
Wheeled pedestal base (small wheels visible at corners; drive type n/a). Max speed ~3 km/h [S1]. Indoor structured environments only.

## Upper body & manipulation
Two arms (per-arm DoF n/a; 16 DoF total across platform), payload ~3 kg [S1]. End-effectors: three-finger grippers, ~6 DoF hand total, chosen for "consistency and simplicity over anatomical replication" [S1]. Reach, repeatability n/a.

## Sensing
Head stereo/depth camera bar (HD–4K vision system per listing, estimated) [S1]. Base/wrist sensors, force/tactile n/a (not disclosed).

## Actuation & power
Electric servo motors; aluminium alloy + composite construction [S1, estimated]. Runtime ~2 h per charge [S1]. Battery capacity n/a.

## Compute & software
Jetson-class edge AI compute (listing estimate); Ethernet/Wi-Fi [S1, estimated]. Software stack n/a (not disclosed); company-wide embodied-AI models presumed shared with M1/W1/Jupiter line [S2, estimated].

## Safety & compliance
"Safe with humans: yes" per listing (unverified) [S1]. Visible e-stop. No certifications disclosed.

## Deployment evidence & traction
None found. Sean does not appear on the vendor site's current product line-up (M1, W1, Jupiter), suggesting it is an internal/dev platform or superseded model [S2]. Company-level traction: ~$70M angel funding at ~$351M valuation (Oct 2025, vendor-claimed) [S2].

## Assessment (analyst view)
*Analyst opinion.* Strengths: pragmatic minimal design (three-finger grippers, wheeled base) suited to data collection and structured tasks; extremely well-funded parent. Weaknesses: low DoF and payload, 2 h runtime, prototype build quality, and apparent absence from the vendor's own portfolio — commercial intent unclear. Threat to a new EU entrant: negligible directly; the company's funding velocity is the thing to watch, not this platform.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://humanoid.guide/product/sean/ | specs (155 cm, 45 kg, 16 DoF, 3 kg, 3 km/h, 2 h), price ~$65k, prototype status, image | third-party |
| 2 | https://www.zeroth0.com/ | company products (M1/W1/Jupiter — Sean absent), funding/valuation, Jiangsu ICP | vendor-claimed |
