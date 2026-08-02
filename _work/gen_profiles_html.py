#!/usr/bin/env python3
"""Generate HTML fragments for the PDF study: stats + compact per-region robot profiles."""
import json, glob, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, "_work", "fragments")
os.makedirs(OUTDIR, exist_ok=True)

def fv(r, k):
    v = r.get(k)
    if isinstance(v, dict):
        return v.get("value"), v.get("confidence", "")
    return v, ""

def esc(x):
    return html.escape(str(x)) if x not in (None, "") else "n/a"

robots, annex = [], []
for p in sorted(glob.glob(os.path.join(ROOT, "companies", "*", "*", "specs.json"))):
    d = json.load(open(p))
    (annex if "[ANNEX]" in d.get("notes", "") else robots).append(d)

# ---- stats fragment ----
from collections import Counter
reg = Counter(r.get("region", "?") for r in robots)
st = Counter(r.get("status", "?") for r in robots)
with open(os.path.join(OUTDIR, "stats.html"), "w") as f:
    f.write("<table class='stats'><tr><th>Region</th>" +
            "".join(f"<td>{k}</td>" for k, _ in reg.most_common()) + "</tr>")
    f.write("<tr><th>Robots</th>" +
            "".join(f"<td>{v}</td>" for _, v in reg.most_common()) + "</tr></table>\n")
    f.write("<table class='stats'><tr><th>Status</th>" +
            "".join(f"<td>{k}</td>" for k, _ in st.most_common()) + "</tr>")
    f.write("<tr><th>Robots</th>" +
            "".join(f"<td>{v}</td>" for _, v in st.most_common()) + "</tr></table>\n")

# ---- per-region compact profile tables ----
ORDER = ["China", "USA", "Canada", "Europe", "Japan", "Korea", "Other"]
STATUS_ORDER = {"shipping": 0, "announced": 1, "prototype": 2, "research": 3, "discontinued": 4}
for region in ORDER:
    sub = sorted([r for r in robots if r.get("region") == region],
                 key=lambda r: (STATUS_ORDER.get(r.get("status"), 9), r.get("company", "")))
    if not sub:
        continue
    rows = []
    for r in sub:
        base, _ = fv(r, "base_type")
        pay, _ = fv(r, "payload_per_arm_kg")
        price, _ = fv(r, "price")
        dep, _ = fv(r, "deployment_evidence")
        base_short = esc(base)[:60]
        dep_short = esc(dep)[:110]
        price_short = esc(price)[:70]
        native = r.get("robot_native") or ""
        name = esc(r.get("robot"))
        if native:
            name += f" <span class='native'>{esc(native)[:24]}</span>"
        rows.append(
            f"<tr><td><b>{name}</b><br><span class='co'>{esc(r.get('company'))}</span></td>"
            f"<td>{esc(r.get('status'))}</td><td>{base_short}</td>"
            f"<td>{esc(pay)}</td><td>{price_short}</td><td>{dep_short}</td></tr>")
    with open(os.path.join(OUTDIR, f"profiles_{region.lower()}.html"), "w") as f:
        f.write(f"<table class='profiles'><thead><tr><th>Robot / Company</th><th>Status</th>"
                f"<th>Base</th><th>kg/arm</th><th>Price</th><th>Deployment evidence</th>"
                f"</tr></thead><tbody>{''.join(rows)}</tbody></table>\n")

# ---- annex table ----
rows = []
for r in sorted(annex, key=lambda r: r.get("company", "")):
    base, _ = fv(r, "base_type")
    note = r.get("notes", "").replace("[ANNEX]", "").strip()[:130]
    rows.append(f"<tr><td><b>{esc(r.get('robot'))}</b><br><span class='co'>"
                f"{esc(r.get('company'))}</span></td><td>{esc(base)[:60]}</td>"
                f"<td>{esc(note)}</td></tr>")
with open(os.path.join(OUTDIR, "annex.html"), "w") as f:
    f.write("<table class='profiles'><thead><tr><th>Robot / Company</th><th>Base</th>"
            "<th>Classification note</th></tr></thead><tbody>" + "".join(rows) +
            "</tbody></table>\n")

print(f"fragments written: {len(robots)} main, {len(annex)} annex")
