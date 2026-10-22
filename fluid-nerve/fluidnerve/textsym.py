"""Map category-theoretic Unicode symbols to matplotlib mathtext so they render with any font."""
import re

_MAP = [
    ("𝒰", r"$\mathcal{U}$"), ("↪", r"$\hookrightarrow$"), ("⇒", r"$\Rightarrow$"), ("↦", r"$\mapsto$"),
    ("ℝ≥0", r"$\mathbb{R}_{\geq 0}$"), ("ℝ", r"$\mathbb{R}$"), ("∩", r"$\cap$"), ("⊆", r"$\subseteq$"), ("∈", r"$\in$"),
    ("N_τ", r"$N_\tau$"), ("N_τ′", r"$N_{\tau'}$"), ("W_i^τ", r"$W_i^{\tau}$"), ("U_σ", r"$U_\sigma$"), ("μ_τ", r"$\mu_\tau$"),
    ("τ_ref", r"$\tau_{\mathrm{ref}}$"), ("N₀", r"$N_0$"),
]


def sym(s):
    """Replace known symbols by mathtext; merge adjacent math segments so '$a$$b$' does not break."""
    if s is None:
        return s
    out = str(s)
    for k, v in _MAP:
        out = out.replace(k, v)
    out = out.replace("$$", "")
    return out


def sym_lines(lines):
    return [sym(l) for l in lines]
