"""Assemble the atlas PDF: legend (category theory + fluid extension), catalog of all systems, overview figures,
and one plate per primary system (paired heavy-atom representations two per page).
Writes theory/atlas.tex and compiles it with tectonic to dist/fluid-nerve-atlas.pdf."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
TEX = ROOT / "theory/fluid-nerve-atlas.tex"


def tex(s):
    s = str(s).replace("\\", "/").replace("_", "\\_").replace("%", "\\%").replace("&", "\\&").replace("#", "\\#")
    for k, v in {"α": "$\\alpha$", "β": "$\\beta$", "τ": "$\\tau$", "µ": "$\\mu$", "→": "$\\to$", "≥": "$\\ge$", "·": "$\\cdot$"}.items():
        s = s.replace(k, v)
    return s


def f(x, spec=".3g"):
    return "--" if x is None else format(x, spec)


def time_label(frames, clock):
    if frames is None:
        return "--"
    if clock is None:
        return f"{frames} fr"
    ps = frames * clock
    return f"{ps*1000:.3g} fs" if ps < 1 else (f"{ps:.3g} ps" if ps < 1000 else f"{ps/1000:.3g} ns")


def main():
    systems = []
    for p in sorted((DIST / "systems").iterdir()):
        s = p / "summary.json"
        if s.exists():
            S = json.loads(s.read_text())
            if not S.get("quick"):
                systems.append(S)
    order = {"atom": 0, "backbone": 1, "paired": 2}
    systems.sort(key=lambda S: (order.get(S["group"], 9), S.get("family") or "", S["id"]))
    prim = [S for S in systems if S["group"] in ("atom", "backbone")]
    paired = [S for S in systems if S["group"] == "paired"]
    n_atom = sum(S["group"] == "atom" for S in systems); n_back = sum(S["group"] == "backbone" for S in systems)
    L = []
    L.append(r"""\documentclass[10pt]{article}
\usepackage[a4paper,landscape,margin=1.4cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{graphicx,booktabs,longtable,array,float,caption}
\usepackage[hidelinks]{hyperref}
\captionsetup{font=small,labelfont=bf}
\setlength{\parskip}{3pt}
\graphicspath{{../dist/}}
\begin{document}""")
    L.append(f"""\\begin{{center}}{{\\LARGE\\bfseries Fluid nerve atlas}}\\\\[4pt]
{{\\large {len(systems)} systems: {n_atom} atom-based (heavy-atom sites), {n_back} backbone-based (C$\\alpha$ sites), {len(paired)} paired heavy-atom representations}}\\\\[3pt]
Joseph Campagna, PSM --- pronerv fluid-nerve pipeline --- \\today\\end{{center}}

\\section*{{How to read the plates}}
Every plate shows one system in six panels. \\textbf{{(A)}} the biophysical object: the recorded conformation nearest the occupancy
peak of the chart, drawn from its sites (heavy atoms with element colours, or the C$\\alpha$ trace coloured from the N- to the C-terminus),
with the deformation field drawn on the molecule as arrows: the mean rigid-aligned displacement of every site over the reference lag,
conditional on the chart bin of that conformation. \\textbf{{(B)}} the chart (backbone dihedrals on a torus, or the two leading principal
components of the aligned sites) with the occupancy, the 18 cover balls and the drawn nerve; one composable pair is annotated in the
language of the legend below. \\textbf{{(C)}} the deformation field on the chart: mobility $h$ (colour) and drift $v$ (arrows).
\\textbf{{(D)}} the fluid filtration: Betti numbers of the nerve of the cover thickened by $\\pm\\tau$ frames along each run.
\\textbf{{(E)}} the flooding filtration of the occupancy landscape (sublevel sets of $-\\log p$), the geometric analogue of metadynamics.
\\textbf{{(F)}} the categorical reading: the sizes of the category drawn in (B), the Betti numbers of the witnessed complex, the
ambient-time invariants and the field summaries. All constructions are descriptive: no equilibrium free energy, rate constant or
configuration-space nerve theorem is claimed.

\\begin{{figure}}[H]\\centering\\includegraphics[width=\\linewidth]{{comparison/fig_legend.png}}
\\caption{{\\textbf{{Legend in categorical terms.}} (1) A cover $\\mathcal U=\\{{U_i\\}}$ of the chart; the recorded frames are the witnesses.
(2) The witnessed complex $K(\\mathcal U;S)$ and its face poset $N(\\mathcal U)$ seen as a category: \\emph{{objects}} are faces $\\sigma$ (the witnessed intersections $U_\\sigma=\\bigcap_{{i\\in\\sigma}}U_i$),
\\emph{{morphisms}} are inclusions $\\sigma\\hookrightarrow\\tau$ with composition given by transitivity and implicit identities, \\emph{{2-cells}} are composable pairs
$(\\sigma\\hookrightarrow\\tau);(\\tau\\hookrightarrow\\rho)\\Rightarrow\\sigma\\hookrightarrow\\rho$ (Street's orientals; exported to homotopy.io together with the 3-cells of length-three chains and of quadruple overlaps).
(3) The \\emph{{fluid extension}}: thickening every cover set by $\\pm\\tau$ frames along the recorded runs gives $W_i^\\tau$ and the nerve $N_\\tau$;
$\\tau\\mapsto N_\\tau$ is a functor from the poset $(\\mathbb R_{{\\ge0}},\\le)$ to simplicial complexes, whose homology is a persistence module in ambient time.
(4) The \\emph{{deformation field}}: the lag-$\\tau$ pair measure $\\mu_\\tau$ restricted to the objects $U_\\sigma$ is a cosheaf over $N(\\mathcal U)$; the derived
statistics (mobility $h$, drift $v$, spread $\\Sigma$, site displacement $u$) form a presheaf of conditional laws, drawn on the molecule in panel (A) and on the chart in panel (C).
The theory PDF (\\texttt{{fluid-nerve-theory.pdf}}) proves that nerves of formally open covers are rigid under infinitesimal transformations, so the ambient-time behaviour seen in (D) is a finite-time, finite-witness phenomenon.}}
\\end{{figure}}
\\clearpage""")
    # catalog
    L.append(r"""\section*{Catalog}
\begin{small}\begin{longtable}{p{3.9cm}p{5.2cm}llrrrlrlr}
\caption{All systems. Nerve counts are objects/morphisms/2-cells of the drawn face-poset nerve; $\beta$ are GF(2) Betti numbers of the witnessed complex; $h$ the median supported mobility at the reference lag; $\tau_{\mathrm c}$ the ambient-time connection; $r_{\mathrm c}$ the cover-radius factor at which $\beta_0=1$.}\\
\toprule id & system & group & repr. & sites & frames & runs & nerve & $\beta_{0,1,2}$ & $\tau_{\mathrm c}$ & $h$ (nm)\\\midrule\endfirsthead
\toprule id & system & group & repr. & sites & frames & runs & nerve & $\beta_{0,1,2}$ & $\tau_{\mathrm c}$ & $h$ (nm)\\\midrule\endhead""")
    for S in systems:
        nd = S["nerve_display_counts"]
        fs = next((s for s in S["field"]["summaries"] if s["tau_frames"] == S["tau_ref_frames"]), {})
        rep = "heavy" if "heavy" in S["representation"] else "C$\\alpha$"
        L.append(f"{tex(S['id'])} & {tex(S['label'])} & {S['group']} & {rep} & {S['sites']} & {S['frames']:,} & {S['runs']} & "
                 f"{nd['objects']}/{nd['inclusions']}/{nd['triangles']} & {','.join(map(str, S['nerve']['betti_0_1_2']))} & "
                 f"{time_label(S['fluid_filtration']['first_connected_tau'], S['clock_ps_per_frame'])} & {f(fs.get('median_h'))}\\\\")
    L.append(r"\bottomrule\end{longtable}\end{small}\clearpage")
    # overview figures
    L.append(r"\section*{Overview figures}")
    caps = [("fig_embedding", "Systems embedded by nerve and field invariants (classical MDS of z-scored invariants)."),
            ("fig_invariants", "Invariant distributions by group with descriptive tests."),
            ("fig_scaling", "Median mobility against ambient lag; the slope is the mobility exponent."),
            ("fig_betti_curves", "Fluid filtration: Betti numbers of the thickened cover nerve against ambient time."),
            ("fig_functor", "Comparison of face posets from heavy atoms and from C$\\alpha$ sites on identical frames (mdCATH)."),
            ("fig_temperature", "mdCATH temperature ladder.")]
    for name, cap in caps:
        if (DIST / "comparison" / f"{name}.png").exists():
            L.append(f"\\begin{{figure}}[H]\\centering\\includegraphics[width=.8\\linewidth,height=.82\\textheight,keepaspectratio]{{comparison/{name}.png}}\\caption{{{cap}}}\\end{{figure}}\\clearpage")
    # plates
    L.append(r"\section*{Plates}")
    for S in prim:
        if (DIST / "systems" / S["id"] / "plate.png").exists():
            L.append(f"\\begin{{figure}}[H]\\centering\\includegraphics[width=\\linewidth,height=.93\\textheight,keepaspectratio]{{systems/{S['id']}/plate.png}}"
                     f"\\caption{{{tex(S['label'])} (\\texttt{{{tex(S['id'])}}}). Source: {tex(str((S.get('provenance') or {}).get('source', ''))[:110])}.}}\\end{{figure}}\\clearpage")
    if any((DIST / "systems" / S["id"] / "plate.png").exists() for S in paired):
        L.append(r"\section*{Paired heavy-atom representations of the backbone systems}")
        for S in paired:
            if (DIST / "systems" / S["id"] / "plate.png").exists():
                L.append(f"\\begin{{figure}}[H]\\centering\\includegraphics[width=\\linewidth,height=.93\\textheight,keepaspectratio]{{systems/{S['id']}/plate.png}}"
                         f"\\caption{{{tex(S['label'])} (\\texttt{{{tex(S['id'])}}}), paired with \\texttt{{{tex(S.get('paired_with', ''))}}}.}}\\end{{figure}}\\clearpage")
    L.append(r"\end{document}")
    TEX.write_text("\n".join(L), encoding="utf-8")
    r = subprocess.run(["tectonic", str(TEX.name), "--outdir", str(DIST)], cwd=TEX.parent, capture_output=True, text=True)
    print(r.stdout[-600:], r.stderr[-1500:])
    print("pdf:", (DIST / "fluid-nerve-atlas.pdf").exists(), "systems:", len(systems), "plates:", len(prim), "paired:", len(paired))


if __name__ == "__main__":
    main()
