# Almond (Almond Robotics / "Almond AI")

| Field | Value |
|---|---|
| HQ | San Francisco, CA, USA (Dogpatch; own small factory in SF) [S1] |
| Founded | 2025 |
| Founders / key people | Saba Khalilnaji (ex-DoorDash logistics engineer, ex-CTO of Conduit) and Shawn Patel (ex-Google hardware engineer; UC Berkeley EECS/Regents) [S2] |
| Employees (approx.) | n/a (very small; YC-stage) |
| Ownership / listing | Private, Y Combinator-backed (Spring 2025 batch per discovery; YC lists company as "almond-2") [S2][S3] |
| Total funding / valuation | YC standard deal; no other rounds disclosed |
| Semi-humanoid products | [axol/](axol/) — Axol dual-arm robot (standalone / Axol Mount / Axol Cart mobile base) |
| Other products | Perception kit (2 wrist + 1 head camera), Axol Cart, data-collection services |
| Website | https://almond.bot |

## Company background
Almond is a small YC-backed San Francisco startup selling Axol, a low-cost dual-7-DoF-arm robot "built for AI" — i.e., a hardware platform for physical-AI teams doing teleoperation, data collection and autonomous policy deployment in factories, warehouses and kitchens [S1][S2]. The playbook is the ALOHA/Trossen dev-platform market, but with beefier arms (860 mm reach, 6.5 kg peak payload per arm, 1 mm repeatability, 500 Hz CAN control) at a disruptive price: from $7,999, or $11,999 for a full kit with base, three ZED X One S cameras and a ZED Box Orin NX 16GB compute unit — shipping from San Francisco in ~1 week [S1][S2][S4].

The stack is deliberately open: open-source Python SDK with bimanual IK solver, low-level CAN motor interface, ZED camera streaming, LeRobot bindings, and WebXR-based VR teleoperation [S1]. Hardware is designed and assembled in California (steel/aluminum/TPU, internal wiring, FAKRA GMSL 2.0 wrist-camera passthrough). Go-to-market is direct e-commerce plus services (customization, data collection, on-site repair in the Bay Area) [S1].

## Relevance to the semi-humanoid market
Almond attacks the research/developer end of the semi-humanoid stack: a torso-class bimanual platform (optionally on the Axol Cart wheeled base) at one-tenth the price of industrial semi-humanoids, US-built — a hedge against Chinese platform dominance (ARX, AgileX, Galaxea) in embodied-AI data collection. It is not an industrial deployment threat, but it shapes price expectations and could grow upward into light automation. For an EU entrant, it is a potential ecosystem partner/supplier as much as a competitor.

## Sources
| # | URL | What it supports | Confidence |
|---|---|---|---|
| 1 | https://almond.bot/ | Specs, pricing, SDK, SF factory, configurations | vendor-claimed |
| 2 | https://www.hackster.io/news/almond-wants-to-put-their-dual-arm-axol-robot-on-your-assembly-line-6c6fb2e99428.amp | Founders, positioning, kit pricing $11,999 | third-party |
| 3 | https://www.ycombinator.com/launches/QlH-axol-a-dual-arm-robot-built-for-ai | YC launch, product framing | vendor-claimed |
| 4 | https://www.techeblog.com/almond-axol-dual-arm-ai-robot/ | Spec confirmation (reach, payload, repeatability) | third-party |
