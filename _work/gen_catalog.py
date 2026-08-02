#!/usr/bin/env python3
"""Generate a 4-robots-per-page illustrated catalog PDF (HTML -> chromium)."""
import json, glob, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_HTML = os.path.join(ROOT, "_work", "catalog.html")
STATUS_ORDER = {"shipping": 0, "announced": 1, "prototype": 2, "research": 3, "discontinued": 4}
REGION_ORDER = ["China", "USA", "Canada", "Europe", "Japan", "Korea", "Other"]
IMG_EXT = (".jpg", ".jpeg", ".png", ".webp")


def esc(x):
    return html.escape(str(x)) if x not in (None, "") else "&mdash;"


def fv(r, k, maxlen=None):
    v = r.get(k)
    val = v.get("value") if isinstance(v, dict) else v
    if val in (None, ""):
        return "&mdash;"
    s = str(val)
    if maxlen and len(s) > maxlen:
        s = s[:maxlen - 1] + "…"
    return html.escape(s)


THUMB_MAP = json.load(open(os.path.join(ROOT, "_work", "thumbs", "mapping.json")))


BAD_WORDS = ("spec", "table", "diagram", "wiring", "chart", "poster", "infographic",
             "logo", "slide", "workspace", "map", "banner", "unit", "crawler-unit",
             "glove", "chassis-only")
GOOD_WORDS = ("hero", "front", "full", "tradeshow", "trade-show", "official", "robot",
              "deployment", "demo", "body", "studio")


def img_score(path):
    name = os.path.basename(path).lower()
    score = 0
    score -= 40 * sum(w in name for w in BAD_WORDS)
    score += 12 * sum(w in name for w in GOOD_WORDS)
    score += min(os.path.getsize(path) / 100_000, 8)  # mild size preference
    return score


def best_image(robot_dir):
    """Best robot photo: filename heuristics + size, thumbnailed."""
    cands = [f for f in glob.glob(os.path.join(robot_dir, "images", "*"))
             if os.path.splitext(f)[1].lower() in IMG_EXT and os.path.getsize(f) > 10000]
    if not cands:
        return None
    full = max(cands, key=img_score)
    return THUMB_MAP.get(os.path.abspath(full), full)


robots = []
for p in sorted(glob.glob(os.path.join(ROOT, "companies", "*", "*", "specs.json"))):
    d = json.load(open(p))
    d["_dir"] = os.path.dirname(p)
    d["_annex"] = "[ANNEX]" in d.get("notes", "")
    robots.append(d)

main = [r for r in robots if not r["_annex"]]
annex = [r for r in robots if r["_annex"]]
key = lambda r: (REGION_ORDER.index(r.get("region")) if r.get("region") in REGION_ORDER else 9,
                 STATUS_ORDER.get(r.get("status"), 9), r.get("company", ""), r.get("robot", ""))
main.sort(key=key)
annex.sort(key=key)


PRESS_DOMAINS = ("therobotreport", "techcrunch", "wikipedia", "prnewswire", "news.",
    "36kr", "sina.c", "qq.com", "ithome", "spectrum.ieee", "reuters", "bloomberg",
    "globenewswire", "youtube", "robotstart", "prtimes", "sohu", "zhihu", "baidu",
    "interestingengineering", "newatlas", "aparobot", "humanoid.guide", "robotsguide",
    "cnbc", "forbes", "sedaily", "yicai", "stcn", "pandaily", "technode", "sacra",
    "crunchbase", "businesswire", "hackaday", "arxiv", "github.io", "medium.com",
    "nate.com", "impress", "monoist", "watch.impress", "eu.36kr", "xinhua", "news.cn")


def official_url(r):
    for u in r.get("sources", []):
        if not isinstance(u, str) or not u.startswith("http"):
            continue
        low = u.lower()
        if not any(d in low for d in PRESS_DOMAINS):
            return u
    return next((u for u in r.get("sources", []) if isinstance(u, str) and u.startswith("http")), None)


def short_url(u, maxlen=58):
    disp = u.replace("https://", "").replace("http://", "").rstrip("/")
    return disp[:maxlen - 1] + "…" if len(disp) > maxlen else disp


def card(r):
    rid = r.get("_rid", "")
    img = best_image(r["_dir"])
    if img:
        img_tag = f"<div class='imgbox'><img src='file://{img}'></div>"
    else:
        img_tag = "<div class='imgbox noimg'>no public imagery</div>"
    native = r.get("robot_native") or ""
    native_tag = f" <span class='native'>{esc(native)}</span>" if native else ""
    annex_tag = "<span class='axtag'>borderline/excluded</span>" if r["_annex"] else ""
    rows = [
        ("Base", fv(r, "base_type", 52)),
        ("Size", f"{fv(r,'height_mm',12)} mm / {fv(r,'weight_kg',10)} kg"),
        ("DoF", f"{fv(r,'dof_total',8)} total / {fv(r,'dof_per_arm',6)} per arm"),
        ("Payload", f"{fv(r,'payload_per_arm_kg',8)} kg/arm"),
        ("Speed/runtime", f"{fv(r,'max_speed_ms',10)} m/s / {fv(r,'runtime_h',10)} h"),
        ("End effector", fv(r, "end_effector", 52)),
        ("Compute", fv(r, "compute", 52)),
        ("Price", fv(r, "price", 52)),
    ]
    url = official_url(r)
    if url:
        rows.append(("Web", f"<a class='weburl' href='{html.escape(url)}'>{html.escape(short_url(url))}</a>"))
    trs = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows)
    return f"""<div class='card' id='{rid}'>
  {img_tag}
  <div class='cardhead'><b>{esc(r.get('robot'))}</b>{native_tag}{annex_tag}
    <div class='co'>{esc(r.get('company'))} &middot; {esc(r.get('region'))} &middot;
      <span class='st st-{esc(r.get('status'))}'>{esc(r.get('status'))}</span></div></div>
  <table class='specs'>{trs}</table>
</div>"""


REGION_LABELS = {
    "China": "China 中国",
    "USA": "USA &amp; Canada",
    "Canada": "USA &amp; Canada",
    "Europe": "Europe",
    "Japan": "Japan 日本",
    "Korea": "South Korea 한국",
    "Other": "Rest of world",
}
SECTIONS = ["China", "USA &amp; Canada", "Europe", "Japan 日本", "South Korea 한국",
            "Rest of world"]
# map each robot to a section label
from collections import Counter, OrderedDict
sections = OrderedDict()
for r in main:
    label = REGION_LABELS.get(r.get("region"), "Rest of world")
    if label == "China 中国": label = "China"
    sections.setdefault(label, []).append(r)
# keep canonical order
ordered_sections = [(lbl, sections[lbl]) for lbl in
                    ["China", "USA &amp; Canada", "Europe", "Japan 日本",
                     "South Korea 한국", "Rest of world"] if lbl in sections]
if annex:
    ordered_sections.append(("Annex: borderline &amp; excluded", annex))

# assign anchor ids
rid = 0
for _, robots_in in ordered_sections:
    for r in robots_in:
        rid += 1
        r["_rid"] = f"rb{rid}"

# page numbering: 1 cover, 2 region TOC, 3 robot index, sections from 4
PAGE_START = 4
section_pages = {}
pageno = PAGE_START
for label, robots_in in ordered_sections:
    section_pages[label] = pageno
    pageno += 1  # divider
    import math
    for i in range(0, len(robots_in), 4):
        for r in robots_in[i:i+4]:
            r["_page"] = pageno
        pageno += 1

# region overview TOC
toc_rows = "".join(
    f"<tr><td><a href='#sec-{i}'>{lbl}</a></td><td>{len(rs)}</td>"
    f"<td>p. {section_pages[lbl]}</td></tr>"
    for i, (lbl, rs) in enumerate(ordered_sections))
toc_page = (f"<div class='page'><h2 class='tochead'>Contents</h2>"
            f"<table class='toct'><thead><tr><th>Section</th><th>Robots</th><th>Page</th></tr></thead>"
            f"<tbody>{toc_rows}</tbody></table>"
            f"<p class='fnote'>Alphabetical robot index overleaf. Entries and section names are "
            f"clickable in PDF viewers that support internal links.</p></div>")

# alphabetical robot index, 3 columns
allr = [r for _, rs in ordered_sections for r in rs]
allr_sorted = sorted(allr, key=lambda r: str(r.get("robot", "")).lower())
items = "".join(
    f"<div class='ixrow'><a href='#{r['_rid']}'>{html.escape(str(r.get('robot'))[:30])}</a>"
    f"<span class='ixco'> {html.escape(str(r.get('company'))[:22])}</span>"
    f"<span class='ixpg'>{r['_page']}</span></div>"
    for r in allr_sorted)
index_page = (f"<div class='page'><h2 class='tochead'>Robot index (A&ndash;Z)</h2>"
              f"<div class='ixcols'>{items}</div></div>")

pages = [toc_page, index_page]
for si, (label, robots_in) in enumerate(ordered_sections):
    st_counts = Counter(r.get("status") for r in robots_in)
    st_line = " &middot; ".join(f"{v} {k}" for k, v in sorted(
        st_counts.items(), key=lambda kv: STATUS_ORDER.get(kv[0], 9)))
    pages.append(
        f"<div class='page divider' id='sec-{si}'><div class='divinner'><h2>{label}</h2>"
        f"<p class='divcount'>{len(robots_in)} robots</p>"
        f"<p class='divstat'>{st_line}</p></div></div>")
    for i in range(0, len(robots_in), 4):
        grid = "".join(card(r) for r in robots_in[i:i + 4])
        pages.append(f"<div class='page'><div class='sechead'>{label}</div>"
                     f"<div class='grid gridh'>{grid}</div></div>")

css = """
  @page { size: A4; margin: 10mm; }
  * { box-sizing: border-box; }
  body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; color: #1a1a2e; }
  .page { page-break-after: always; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr;
          gap: 5mm; height: 275mm; }
  .card { border: 0.6pt solid #99a; border-radius: 6px; padding: 4px 6px;
          overflow: hidden; display: flex; flex-direction: column; }
  .imgbox { height: 58mm; display: flex; align-items: center; justify-content: center;
            background: #f4f5f8; border-radius: 4px; overflow: hidden; }
  .imgbox img { max-width: 100%; max-height: 100%; object-fit: contain; }
  .noimg { color: #999; font-size: 8pt; font-style: italic; }
  .cardhead { font-size: 9.5pt; margin: 3pt 0 2pt 0; }
  .native { color: #777; font-size: 8pt; font-weight: normal; }
  .axtag { float: right; font-size: 6.5pt; color: #b06010; border: 0.5pt solid #b06010;
           border-radius: 3px; padding: 0 3px; }
  .co { color: #555; font-size: 7.5pt; margin-top: 1pt; }
  .st { font-weight: bold; }
  .st-shipping { color: #1a7a2e; } .st-announced { color: #b07a10; }
  .st-prototype { color: #8a5a9a; } .st-research { color: #3a5a9f; }
  .st-discontinued { color: #a03030; }
  table.specs { border-collapse: collapse; width: 100%; font-size: 6.8pt; margin-top: 2pt; }
  .specs th { text-align: left; color: #1F3864; padding: 0.5pt 4pt 0.5pt 0; width: 22%;
              font-weight: 600; vertical-align: top; white-space: nowrap; }
  .specs td { padding: 0.5pt 0; vertical-align: top; }
  .specs tr { border-bottom: 0.3pt solid #dde; }
  .cover { text-align: center; padding-top: 130mm; page-break-after: always; position: relative; height: 270mm; }
  h1 { color: #1F3864; }
  .divider { display: flex; align-items: center; justify-content: center; height: 275mm; }
  .divinner { text-align: center; border: 2pt solid #1F3864; border-radius: 10px;
              padding: 30pt 60pt; }
  .divinner h2 { color: #1F3864; font-size: 26pt; margin: 0; }
  .divcount { font-size: 13pt; color: #333; margin: 8pt 0 2pt 0; }
  .divstat { font-size: 9.5pt; color: #666; margin: 0; }
  .sechead { font-size: 8pt; color: #1F3864; border-bottom: 1pt solid #1F3864;
             margin-bottom: 2mm; padding-bottom: 1pt; font-weight: 600;
             text-transform: uppercase; letter-spacing: 1pt; }
  .gridh { height: 268mm; }
  a.weburl { color: #2a5aa0; text-decoration: none; word-break: break-all; }
  .tochead { color: #1F3864; border-bottom: 2px solid #1F3864; padding-bottom: 3pt; }
  table.toct { border-collapse: collapse; width: 60%; font-size: 11pt; margin-top: 6mm; }
  .toct th { background: #1F3864; color: #fff; text-align: left; padding: 4pt 8pt; }
  .toct td { border-bottom: 0.5pt solid #bbc; padding: 5pt 8pt; }
  .toct a { color: #1a1a2e; text-decoration: none; font-weight: 600; }
  .ixcols { column-count: 3; column-gap: 6mm; margin-top: 4mm; }
  .ixrow { font-size: 6.6pt; line-height: 1.55; break-inside: avoid; display: flex; }
  .ixrow a { color: #1a1a2e; text-decoration: none; white-space: nowrap; overflow: hidden;
             text-overflow: ellipsis; max-width: 34mm; }
  .ixco { color: #888; font-size: 5.8pt; white-space: nowrap; overflow: hidden;
          text-overflow: ellipsis; flex: 1; margin-left: 2pt; }
  .ixpg { color: #1F3864; font-weight: 600; margin-left: 3pt; }
  .fnote { font-size: 8pt; color: #666; margin-top: 6mm; }
"""
doc = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Semi-Humanoid Robot Catalog 2026</title><style>{css}</style></head><body>
<div class='cover'><h1>Semi-Humanoid Robot Catalog 2026</h1>
<p>{len(main)} robots (+{len(annex)} borderline/excluded, marked)<br>
Compiled 2 August 2026</p>
<div style="position:absolute; right:12mm; bottom:14mm; text-align:right; font-size:10.5pt; color:#333; line-height:1.6;">
<b>Roboteur Research</b><br>
Andreas K&ouml;pf (<a href="https://x.com/neurosp1ke" style="color:#3a5a9f;text-decoration:none;">x.com/neurosp1ke</a>)<br>
compiled by Claude Fable 5</div></div>
{''.join(pages)}
</body></html>"""
open(OUT_HTML, "w").write(doc)
print(f"catalog html: {sum(len(v) for _, v in ordered_sections)} robots, {len(pages)} pages incl. dividers")
