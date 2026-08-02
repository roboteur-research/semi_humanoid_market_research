# Semi-Humanoid Robot Market Research 2026

Global competition landscape analysis of **semi-humanoid robots**: robots with a
human-like upper body (head, torso, two arms) whose legs are replaced by a wheeled,
tracked, lift-column, ball or pedestal base. Textbook examples: SoftBank Pepper,
Sunday Robotics Memo, AgiBot A2-W, 1X EVE.

## Repository layout

```
companies/<company-slug>/
    company.md              # company profile: HQ, founding, funding, strategy, sources
    <robot-slug>/
        robot.md            # full robot dossier (specs, sources, confidence ratings)
        specs.json          # machine-readable spec sheet (fixed schema, feeds the xlsx)
        images/             # downloaded photos / renderings / drawings
        images/images.md    # per-image caption + source URL + licence note
study/
    semi_humanoid_market_2026.xlsx   # comparison matrix, one row per robot
    semi_humanoid_market_2026.pdf    # written market study (English, 34 pp)
    semi_humanoid_catalog_2026.pdf   # illustrated catalog: 4 robots/page, image + key specs (49 pp)
templates/                  # authoring templates + JSON schema
_work/                      # intermediate research artifacts (discovery lists etc.)
```

## Conventions

- All content in **English**; native names (Chinese/Japanese/Korean) given in
  parentheses on first mention. Foreign-language sources are translated.
- Every factual claim carries a source URL and a confidence rating:
  - `vendor-claimed` — from the manufacturer (website, datasheet, press release)
  - `third-party` — verified/reported by independent media, teardowns, papers, filings
  - `estimated` — inferred (from images, comparable products, analyst guesses)
- Status vocabulary: `shipping` / `announced` / `prototype` / `research` / `discontinued`.
- Slugs: lowercase, hyphenated ASCII (e.g. `agibot`, `a2-w`).
