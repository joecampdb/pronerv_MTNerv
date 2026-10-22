"""Generate the LaTeX fragments (theory/generated/*.tex) and copy figures (theory/figures/) from dist/."""
import json
import shutil
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
GEN = ROOT / "theory/generated"
FIG = ROOT / "theory/figures"
GEN.mkdir(exist_ok=True)
FIG.mkdir(exist_ok=True)


def tex(s):
    return str(s).replace("_", "\\_").replace("%", "\\%").replace("&", "\\&")


def f(x, spec=".3g"):
    return "--" if x is None else format(x, spec)


def time_label(frames, clock):
    if frames is None:
        return "--"
    if clock is None:
        return f"{frames} fr"
    ps = frames * clock
    if ps < 1:
        return f"{ps*1000:.3g} fs"
    if ps < 1000:
        return f"{ps:.3g} ps"
    return f"{ps/1000:.3g} ns"


def main():
    inv = json.loads((DIST / "comparison/invariants.json").read_text())
    tests = json.loads((DIST / "comparison/group_tests.json").read_text())
    dist = json.loads((DIST / "comparison/distances.json").read_text())
    cf = json.loads((DIST / "comparison/comparison_functor.json").read_text())
    tl = json.loads((DIST / "comparison/temperature_ladder.json").read_text())
    corr = json.loads((DIST / "comparison/correlations.json").read_text())
    hom = json.loads((DIST / "homotopy/index.json").read_text()) if (DIST / "homotopy/index.json").exists() else {}
    groups = {g: [r for r in inv if r["group"] == g] for g in ("atom", "backbone", "paired")}
    macros = [
        f"\\newcommand{{\\nSystems}}{{{len(groups['atom']) + len(groups['backbone'])}}}",
        f"\\newcommand{{\\nAtom}}{{{len(groups['atom'])}}}",
        f"\\newcommand{{\\nBackbone}}{{{len(groups['backbone'])}}}",
        f"\\newcommand{{\\nPaired}}{{{len(groups['paired'])}}}",
        f"\\newcommand{{\\nMdcath}}{{{sum(1 for r in groups['backbone'] if r['family'] == 'mdcath')}}}",
        f"\\newcommand{{\\sepRatio}}{{{dist['separation_ratio']:.2f}}}",
        f"\\newcommand{{\\sepP}}{{{dist['permutation_p']:.3f}}}",
    ]
    (GEN / "macros.tex").write_text("\n".join(macros) + "\n", encoding="utf-8")

    # systems table
    rows = ["\\begin{small}\\begin{longtable}{llrrrlrrrl}",
            "\\caption{All primary systems. Objects/inclusions/triangles are the counts of the drawn face-poset nerve; $\\beta$ are GF(2) Betti numbers of the witnessed complex; $h$ is the median supported mobility at the reference lag; $\\alpha$ the mobility exponent; $r_{\\mathrm c}$ the connection radius factor; $\\tau_{\\mathrm c}$ the connection time of the fluid filtration.}\\label{tab:systems}\\\\",
            "\\toprule system & group & frames & sites & objects/incl./tri. & $\\beta_{0,1,2}$ & $r_{\\mathrm c}$ & $h$ (nm) & $\\alpha$ & $\\tau_{\\mathrm c}$\\\\\\midrule\\endfirsthead",
            "\\toprule system & group & frames & sites & objects/incl./tri. & $\\beta_{0,1,2}$ & $r_{\\mathrm c}$ & $h$ (nm) & $\\alpha$ & $\\tau_{\\mathrm c}$\\\\\\midrule\\endhead"]
    for r in sorted(groups["atom"] + groups["backbone"], key=lambda r: (r["group"], r["family"], r["id"])):
        rows.append(f"{tex(r['id'])} & {r['group']} & {r['frames']:,} & {r['sites']} & {r['objects']}/{r['inclusions']}/{r['triangles']} & "
                    f"{r['beta0']},{r['beta1']},{r['beta2']} & {f(r.get('connect_radius_factor'), '.2f')} & {f(r['median_h_ref'])} & {f(r['h_slope'], '.2f')} & {time_label(r['first_connected_frames'], r['clock_ps'])}\\\\")
    rows += ["\\bottomrule\\end{longtable}\\end{small}"]
    (GEN / "systems_table.tex").write_text("\n".join(rows) + "\n", encoding="utf-8")

    # group table
    keys = ["objects", "inclusions", "triangles", "max_dimension", "beta0", "beta1", "median_h_ref", "drift_ratio_ref", "h_slope",
            "first_connected_frames", "beta1_total_lifetime_frames", "flood_basins", "entropy_bits"]
    rows = ["\\begin{table}[H]\\centering\\small\\begin{tabular}{lrrrrr}\\toprule",
            "invariant & median atom & median backbone & Mann--Whitney $p$ & Cliff's $\\delta$ & $n$\\\\\\midrule"]
    for k in keys:
        t = tests[k]
        rows.append(f"{tex(t['label'])} & {f(t['median_atom'])} & {f(t['median_backbone'])} & {f(t.get('p_value'), '.3f')} & "
                    f"{f(t.get('cliffs_delta'), '+.2f')} & {t['n_atom']}/{t['n_backbone']}\\\\")
    rows += ["\\bottomrule\\end{tabular}\\caption{Group medians and descriptive two-sided tests (atom-based vs backbone-based). "
             "Mean within-group distance atom " + f(dist["mean_within"].get("atom")) + ", backbone " + f(dist["mean_within"].get("backbone")) +
             ", between " + f(dist["mean_between"]) + ".}\\label{tab:groups}\\end{table}"]
    (GEN / "group_table.tex").write_text("\n".join(rows) + "\n", encoding="utf-8")

    # functor table
    rows = ["\\begin{table}[H]\\centering\\small\\begin{tabular}{lrrrrrr}\\toprule",
            "domain & faces (heavy/C$\\alpha$) & med.\\ Jaccard & incl.\\ lax & incl.\\ strict & comp.\\ lax & C$\\alpha\\to$heavy incl.\\\\\\midrule"]
    for p in cf["pairs"]:
        a, b = p["heavy_to_ca"], p["ca_to_heavy"]
        rows.append(f"{tex(p['ca'].split('-')[1])} & {a['faces']}/{b['faces']} & {f(a['median_best_jaccard'], '.2f')} & {f(a['inclusion_preserved_lax'], '.2f')} & "
                    f"{f(a['inclusion_preserved_strict'], '.2f')} & {f(a['composition_preserved_lax'], '.2f')} & {f(b['inclusion_preserved_lax'], '.2f')}\\\\")
    s = cf["summary"]
    rows += ["\\midrule", f"median over domains & & {f(s['heavy_to_ca.median_best_jaccard']['median'], '.2f')} & {f(s['heavy_to_ca.inclusion_preserved_lax']['median'], '.2f')} & "
             f"{f(s['heavy_to_ca.inclusion_preserved_strict']['median'], '.2f')} & {f(s['heavy_to_ca.composition_preserved_lax']['median'], '.2f')} & {f(s['ca_to_heavy.inclusion_preserved_lax']['median'], '.2f')}\\\\",
             "\\bottomrule\\end{tabular}\\caption{Comparison of face posets built from heavy atoms and from C$\\alpha$ sites on identical frames (mdCATH).}\\label{tab:functor}\\end{table}"]
    (GEN / "functor_table.tex").write_text("\n".join(rows) + "\n", encoding="utf-8")

    # temperature
    lines = []
    if tl:
        b0 = {T: [] for T in (320, 348, 379, 413, 450)}; hh = {T: [] for T in b0}; tri = {T: [] for T in b0}
        for d in tl:
            for r in d["ladder"]:
                b0[r["T"]].append(r["beta"][0]); tri[r["T"]].append(r["simplices"].get("2", 0))
                if r["median_h"] is not None:
                    hh[r["T"]].append(r["median_h"])
        lines.append("\\begin{table}[H]\\centering\\small\\begin{tabular}{lrrrrr}\\toprule temperature (K) & 320 & 348 & 379 & 413 & 450\\\\\\midrule")
        lines.append("median $\\beta_0$ & " + " & ".join(f(np.median(b0[T]), ".1f") for T in b0) + "\\\\")
        lines.append("median triangles & " + " & ".join(f(np.median(tri[T]), ".0f") for T in b0) + "\\\\")
        lines.append("median $h$ at $\\tau_{\\mathrm{ref}}$ (nm) & " + " & ".join(f(np.median(hh[T]) if hh[T] else None) for T in b0) + "\\\\")
        lines.append("\\bottomrule\\end{tabular}\\caption{mdCATH temperature ladder over " + str(len(tl)) + " domains (same chart and cover per domain).}\\label{tab:temperature}\\end{table}")
    else:
        lines.append("No temperature ladder available.")
    (GEN / "temperature.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # rigidity test: membership flip rate against the early mobility exponent
    prim = groups["atom"] + groups["backbone"]
    flat = []
    for r in prim:
        S = json.loads((DIST / "systems" / r["id"] / "summary.json").read_text())
        rows_ = S["fluid_filtration"]["rows"]
        fr = (S.get("membership_flip_rate") or {}).get("1")
        if len(rows_) > 1 and r.get("h_slope_early") is not None:
            drop = (rows_[0]["betti"][0] - rows_[1]["betti"][0]) / max(rows_[0]["betti"][0], 1)
            flat.append((r["id"], r["family"], r["h_slope_early"], drop, rows_[0]["betti"][0], fr))
    ball = [x for x in flat if x[2] > 0.6]
    sat = [x for x in flat if x[2] < 0.2]

    def mean_flip(xs):
        v = [x[5] for x in xs if x[5] is not None]
        return float(np.mean(v)) if v else None
    rho = corr.get("h_slope_early~flip_rate_1", {})
    txt = ["Theorem~\\ref{thm:rigid} predicts that cover membership is invariant between frames that are first-order close relative to the cover. "
           "We measure the \\emph{membership flip rate}: the fraction of consecutive within-run frame pairs whose 18-ball membership vector differs. "
           f"Classifying by the early mobility exponent $\\alpha_{{\\mathrm{{early}}}}$ (log--log slope over the first half of the lag ladder), {len(ball)} of the {len(flat)} primary systems are ballistic ($\\alpha_{{\\mathrm{{early}}}}>0.6$) "
           f"and {len(sat)} are saturated ($\\alpha_{{\\mathrm{{early}}}}<0.2$). The mean one-frame flip rate is {f(mean_flip(ball), '.3f')} for the ballistic systems and {f(mean_flip(sat), '.3f')} for the saturated ones"
           + (f" (Spearman $\\rho={f(rho.get('spearman_rho'), '.2f')}$, $p={f(rho.get('p'), '.3f')}$, $n={rho.get('n')}$ between the early exponent and the flip rate)." if rho else ".")
           + f" The relative drop of $\\beta_0$ between $\\tau=0$ and the first ladder lag is {f(np.mean([x[3] for x in ball]) if ball else None, '.2f')} (ballistic) against {f(np.mean([x[3] for x in sat]) if sat else None, '.2f')} (saturated); "
           "this statistic is dominated by isolated fringe balls, which a single frame of thickening attaches to the main component, so the flip rate is the cleaner test."]
    txt.append(" Ballistic systems: " + ", ".join(tex(x[0]) for x in ball) + "." if ball else "")
    (GEN / "rigidity.tex").write_text("".join(txt) + "\n", encoding="utf-8")

    # homotopy table
    rows = ["\\begin{table}[H]\\centering\\small\\begin{tabular}{lrrrr}\\toprule system & base generators (0/1/2/3-cells) & status & poset generators & status\\\\\\midrule"]
    for sid, enc in sorted(hom.items()):
        b, p = enc.get("base", {}), enc.get("poset", {})
        rows.append(f"{tex(sid)} & {b.get('vertices')}/{b.get('edges')}/{b.get('triangles')}/{b.get('tetrahedra')} & {tex(str(b.get('status', ''))[:7])} & "
                    f"{p.get('generators')} & {tex(str(p.get('status', ''))[:7])}\\\\")
    rows += ["\\bottomrule\\end{tabular}\\caption{homotopy.io exports (\\texttt{dist/homotopy/<system>/}).}\\label{tab:homotopy}\\end{table}"]
    (GEN / "homotopy_table.tex").write_text("\n".join(rows) + "\n", encoding="utf-8")

    # exemplars: pick one per family if figure exists
    ex = []
    seen = set()
    for r in sorted(prim, key=lambda r: r["id"]):
        if r["family"] in seen:
            continue
        src = DIST / "systems" / r["id"] / "figure.png"
        if src.exists():
            shutil.copy(src, FIG / f"system_{r['id']}.png")
            seen.add(r["family"])
            ex.append(f"\\begin{{figure}}[H]\\centering\\includegraphics[width=\\linewidth]{{figures/system_{r['id']}.png}}"
                      f"\\caption{{{tex(r['label'])}: occupancy and nerve, deformation field, fluid and flooding filtrations.}}\\end{{figure}}")
    (GEN / "exemplars.tex").write_text("\n".join(ex) + "\n", encoding="utf-8")
    for name in ["fig_embedding", "fig_invariants", "fig_betti_curves", "fig_scaling", "fig_functor", "fig_temperature"]:
        src = DIST / "comparison" / f"{name}.png"
        if src.exists():
            shutil.copy(src, FIG / f"{name}.png")
    print("generated", [p.name for p in GEN.iterdir()])


if __name__ == "__main__":
    main()
