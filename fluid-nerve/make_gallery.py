"""Write dist/index.html: a static gallery of every built system with its figure and key invariants."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"


def main():
    cards = []
    rows = []
    for p in sorted((DIST / "systems").iterdir()):
        f = p / "summary.json"
        if not f.exists():
            continue
        S = json.loads(f.read_text())
        if S.get("quick"):
            continue
        rows.append(S)
    groups = {}
    for S in rows:
        groups.setdefault(S["group"], []).append(S)
    for g in ("atom", "backbone", "paired"):
        for S in groups.get(g, []):
            nd = S["nerve_display_counts"]
            fs = next((s for s in S["field"]["summaries"] if s["tau_frames"] == S["tau_ref_frames"]), {})
            fc = S["fluid_filtration"]["first_connected_tau"]
            hom = DIST / "homotopy" / S["id"]
            links = [f'<a href="systems/{S["id"]}/summary.json">summary</a>', f'<a href="systems/{S["id"]}/nerve.json">nerve</a>']
            if (hom / "base.hom").exists():
                links.append(f'<a href="homotopy/{S["id"]}/base.hom">base.hom</a>')
            if (hom / "poset.hom").exists():
                links.append(f'<a href="homotopy/{S["id"]}/poset.hom">poset.hom</a>')
            if (hom / "README.md").exists():
                links.append(f'<a href="homotopy/{S["id"]}/README.md">click script</a>')
            fig = f'<img src="systems/{S["id"]}/figure.png" loading="lazy" alt="">' if (p := DIST / "systems" / S["id"] / "figure.png").exists() else ""
            cards.append(f"""<section class="card {g}"><h3>{S['label']} <code>{S['id']}</code></h3>
<p class="meta">{g} group · {S['representation']} ({S['sites']} sites) · {S['frames']:,} frames / {S['runs']} runs · nerve {nd['objects']}/{nd['inclusions']}/{nd['triangles']} · β {S['nerve']['betti_0_1_2']} · median h {fs.get('median_h') if fs else None} nm · τ_connect {fc} frames</p>
{fig}<p>{' · '.join(links)}</p></section>""")
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Fluid nerve atlas</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{{font-family:system-ui,Segoe UI,sans-serif;margin:0;padding:16px;background:#f9f9f7;color:#0b0b0b}}
h1{{font-size:1.4rem}} .meta{{color:#52514e;font-size:.85rem}} .card{{background:#fcfcfb;border:1px solid #e1e0d9;border-radius:6px;padding:12px;margin:12px 0}}
.card img{{max-width:100%;height:auto}} code{{font-size:.8rem;color:#52514e}} a{{color:#2a78d6}}
.atom h3{{border-left:4px solid #2a78d6;padding-left:8px}} .backbone h3{{border-left:4px solid #eb6834;padding-left:8px}} .paired h3{{border-left:4px solid #1baf7a;padding-left:8px}}</style></head>
<body><h1>Fluid nerve atlas: {len(groups.get('atom', []))} atom-based, {len(groups.get('backbone', []))} backbone-based, {len(groups.get('paired', []))} paired systems</h1>
<p class="meta">Descriptive constructions; see <a href="fluid-nerve-theory.pdf">the theory PDF</a>, <a href="comparison/overview.json">comparison overview</a> and the <a href="../README.md">README</a>. Blue = atom-based, orange = backbone-based, aqua = paired heavy-atom representation.</p>
{''.join(cards)}</body></html>"""
    (DIST / "index.html").write_text(html, encoding="utf-8")
    print("wrote", DIST / "index.html", len(cards), "cards")


if __name__ == "__main__":
    main()
