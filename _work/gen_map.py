#!/usr/bin/env python3
"""World map: distribution of documented semi-humanoid robot models by HQ country.
Choropleth (sequential ramp, direct labels) + ranked bar list. Renders to PNG via chromium."""
import json, glob, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = os.environ.get("SCRATCH", "/tmp/claude-1000/-home-koepf-work-roboteur-semi-humanoid-market-research/b2d1c8a4-6771-46d4-8b08-e4a2495712f3/scratchpad")
SVG_SRC = os.path.join(SP, "worldmap.svg")
OUT_HTML = os.path.join(ROOT, "_work", "map.html")

# ---- data ----
NORM = {
    "United Kingdom": "UK", "Türkiye": "Turkey", "Hong Kong SAR, China": "China",
    "Norway / USA": "USA", "USA (founded Japan; GITAI Japan remains)": "USA",
}
ISO = {"China": "cn", "USA": "us", "Japan": "jp", "South Korea": "kr", "Germany": "de",
       "India": "in", "France": "fr", "UK": "gb", "Spain": "es", "Russia": "ru",
       "Italy": "it", "Canada": "ca", "Luxembourg": "lu", "Switzerland": "ch",
       "Poland": "pl", "Vietnam": "vn", "Nepal": "np", "Netherlands": "nl",
       "Singapore": "sg", "Saudi Arabia": "sa", "Turkey": "tr", "Israel": "il",
       "Australia": "au", "Taiwan": "tw"}

counts = Counter()
for p in glob.glob(os.path.join(ROOT, "companies", "*", "*", "specs.json")):
    d = json.load(open(p))
    if "[ANNEX]" in d.get("notes", ""):
        continue
    c = d.get("hq_country") or "Global (open source)"
    c = NORM.get(c, c)
    counts[c] += 1

globals_n = counts.pop("Global (open source)", 0)

# ---- sequential ramp (magnitude): monotonic lightness, validated ----
BUCKETS = [(1, 2, "#D6E4F5"), (3, 5, "#A8C6E8"), (6, 12, "#6E9CD1"),
           (13, 29, "#3E6CAE"), (30, 999, "#1F3864")]
def bucket_color(n):
    for lo, hi, col in BUCKETS:
        if lo <= n <= hi:
            return col
    return "#EDEFF3"

css_rules = []
for country, n in counts.items():
    iso = ISO.get(country)
    if not iso:
        print(f"WARN no ISO for {country} ({n})")
        continue
    col = bucket_color(n)
    css_rules.append(f".{iso} {{ fill: {col} !important; }} .{iso} * {{ fill: {col} !important; }}")

svg = open(SVG_SRC, encoding="utf-8").read()
svg = re.sub(r'<\?xml[^>]*\?>', '', svg)
# root has fixed width/height but no viewBox: add viewBox, then strip fixed size
m = re.search(r'<svg[^>]*width="([\d.]+)"[^>]*height="([\d.]+)"', svg)
w, h = m.group(1), m.group(2)
svg = re.sub(r'<svg', f'<svg viewBox="0 0 {w} {h}"', svg, count=1)
svg = re.sub(r'(<svg[^>]*?) width="[^"]*"', r'\1', svg, count=1)
svg = re.sub(r'(<svg[^>]*?) height="[^"]*"', r'\1', svg, count=1)

ranked = counts.most_common()
maxn = ranked[0][1]
bars = ""
for country, n in ranked:
    w = max(2.0, 100.0 * n / maxn)
    col = bucket_color(n)
    bars += (f"<div class='brow'><span class='bl'>{country}</span>"
             f"<span class='bar'><span class='fill' style='width:{w}%;background:{col}'></span></span>"
             f"<span class='bn'>{n}</span></div>")

legend = "".join(
    f"<span class='lg'><span class='sw' style='background:{col}'></span>"
    f"{lo}&ndash;{hi if hi<999 else '+'}</span>" if hi < 999 else
    f"<span class='lg'><span class='sw' style='background:{col}'></span>{lo}+</span>"
    for lo, hi, col in BUCKETS)

html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
  body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 0; background: #fff;
         width: 1500px; color: #1a1a2e; }}
  h1 {{ font-size: 26px; color: #1F3864; margin: 18px 24px 2px 24px; }}
  .sub {{ color: #555; font-size: 14px; margin: 0 24px 8px 24px; }}
  .wrap {{ display: flex; gap: 10px; padding: 0 16px; }}
  .mapbox {{ flex: 1; }}
  .mapbox svg {{ width: 100%; height: auto; }}
  .mapbox svg path, .mapbox svg polygon {{ fill: #EDEFF3; stroke: #ffffff; stroke-width: 0.6; }}
  .mapbox svg .oceanxx {{ fill: #ffffff !important; stroke: none; }}
  {' '.join(css_rules)}
  .side {{ width: 330px; padding-top: 8px; }}
  .side h2 {{ font-size: 15px; color: #1F3864; margin: 0 0 6px 0; }}
  .brow {{ display: flex; align-items: center; font-size: 12px; margin: 2.5px 0; }}
  .bl {{ width: 92px; text-align: right; padding-right: 6px; color: #333; }}
  .bar {{ flex: 1; height: 12px; background: #F1F3F7; border-radius: 3px; overflow: hidden; }}
  .fill {{ display: block; height: 100%; border-radius: 3px; }}
  .bn {{ width: 30px; text-align: right; font-weight: 600; color: #1F3864; padding-left: 5px; }}
  .legend {{ margin: 4px 24px 14px 24px; font-size: 12.5px; color: #444; }}
  .lg {{ margin-right: 14px; }}
  .sw {{ display: inline-block; width: 14px; height: 11px; border-radius: 2px;
        margin-right: 4px; vertical-align: -1px; border: 0.5px solid #ccd; }}
  .fnote {{ color: #777; font-size: 11.5px; margin: 0 24px 16px 24px; }}
</style></head><body>
<h1>Semi-humanoid robot models by country of origin</h1>
<p class="sub">{sum(counts.values())} documented models (main matrix, August 2026), by developer headquarters</p>
<div class="wrap">
  <div class="mapbox">{svg}</div>
  <div class="side"><h2>Models per country</h2>{bars}</div>
</div>
<div class="legend"><b>Models:</b>&nbsp; {legend}</div>
<p class="fnote">Hong Kong counted under China; dual-HQ companies (1X, GITAI) counted at
current headquarters (USA). {globals_n} community/open-source project(s) without a single
HQ not shown on map. Nordic note: Norway-founded 1X (EVE) relocated to the USA; Sweden's Hexagon AEON is a wheel-leg hybrid in the borderline annex; Denmark's Odense cluster (Universal Robots, MiR) supplies components, not semi-humanoids. Source: study dossier repository; full per-robot data in
semi_humanoid_market_2026.xlsx.</p>
</body></html>"""
open(OUT_HTML, "w", encoding="utf-8").write(html)
print(f"map html written; countries mapped: {len(css_rules)}; global: {globals_n}")
