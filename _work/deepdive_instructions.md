# Deep-dive agent playbook (shared instructions)

You are writing competitor dossiers for a German robotics company's semi-humanoid market study.
ROOT = /home/koepf/work/roboteur/semi_humanoid_market_research

## Deliverables per assigned company
```
ROOT/companies/<company-slug>/company.md
ROOT/companies/<company-slug>/<robot-slug>/robot.md
ROOT/companies/<company-slug>/<robot-slug>/specs.json
ROOT/companies/<company-slug>/<robot-slug>/images/          (downloaded image files)
ROOT/companies/<company-slug>/<robot-slug>/images/images.md (caption + source URL + licence note per image)
```
Templates: ROOT/templates/company.md, ROOT/templates/robot.md, ROOT/templates/specs.schema.md — follow them.
Slugs are given in your assignment. Do NOT create or modify files outside your assigned company folders.

## Tier scope
- T1 flagship: thorough — official site + datasheets + independent press + reviews + forums/Reddit/YouTube + teardowns + funding/deployment digging. 2-4 images. Full robot.md incl. "Assessment (analyst view)".
- T2 standard: official site + 2-3 independent sources. 1-2 images. All template sections, brief where data is thin.
- T3 compact: short company.md + short robot.md (summary table, 3-6 sentences of prose, sources) + specs.json (nulls OK) + 1 image attempt.

## Work order — CRITICAL (sessions can be killed at any time)
Process ONE company at a time: research it → immediately write ALL its files (company.md, robot.md, specs.json, images + images.md) → only then move to the next company. NEVER defer file-writing to the end of your run. Partially finished batches must still leave complete per-company dossiers on disk. Start with the company you can finish fastest.

## Research method — IMPORTANT
- WebSearch quota for this session may be EXHAUSTED. Try WebSearch once; if it errors/denies, switch to:
  - WebFetch on known URLs (start from the discovery file given in your assignment — it has curated URLs per robot).
  - Search via WebFetch on: https://html.duckduckgo.com/html/?q=YOUR+QUERY or https://lite.duckduckgo.com/lite/?q=... or https://www.bing.com/search?q=...
  - Bash curl for pages that block fetchers: curl -sL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36" URL
- Chinese/Japanese/Korean sources: read them, translate all extracted facts to English; keep native names/terms in parentheses.
- Every fact gets confidence: vendor-claimed / third-party / estimated. Unknown = "n/a (not disclosed)".

## specs.json
Follow ROOT/templates/specs.schema.md EXACTLY (same keys). Identity fields plain strings; spec fields = {"value":..., "confidence":"...", "source":"url"}. Numbers as numbers where the key names a unit. Validate mentally: file must be parseable JSON (no trailing commas, no comments).
"region" must be one of: China / Japan / USA / Canada / Europe / Korea / Other.
"status" one of: shipping / announced / prototype / research / discontinued.

## Images
1. Find candidate image URLs: official product pages, press kits, press releases, Wikimedia Commons, news articles (og:image meta tags work well — curl the page and grep -o 'og:image[^>]*').
2. Download: curl -sL -A "Mozilla/5.0 ..." -o ROOT/companies/<c>/<r>/images/<descriptive-name>.jpg "URL"
3. VERIFY: run `file` on it — must be JPEG/PNG/WebP/GIF data, not HTML/text. Also check size >10KB (tiny files are usually icons/errors). Delete failures, try another URL.
4. Name descriptively: <robot>-front.jpg, <robot>-hand-closeup.jpg, <robot>-naked-actuators.jpg etc.
5. Record every kept image in images.md: filename | source page URL | direct image URL | caption | licence/usage note (e.g. "press kit", "vendor marketing image", "CC BY-SA Wikimedia").
6. For T1: try to find at least one NON-marketing image (trade-show photo, deployment photo, teardown/internals) in addition to official renders.

## robot.md quality bar
- Lead paragraph: what it is, who it's for, why it matters competitively.
- Fill ALL template sections; be concrete with numbers + source references [S1], [S2]... mapping to the Sources table.
- "Deployment evidence & traction": real customers, unit counts, pilots — with confidence tags.
- "Assessment (analyst view)" (T1/T2): strengths/weaknesses/threat to a new EU entrant, 3-6 sentences, marked as analyst opinion.

## Final report (your last message)
List: files written per company; images downloaded (count) and any image failures; key facts discovered that CONTRADICT the discovery notes; open questions. Keep it under 40 lines.
