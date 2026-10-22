"""System catalog: every example with its group, representation, chart recipe, clock and loader.

Groups
  atom      heavy-atom site representation (small peptides and molecules)          -> 50 % of the primary examples
  backbone  C-alpha site representation (proteins / CLN025)                        -> 50 % of the primary examples
  paired    heavy-atom representation of a backbone system on the same frames (used only for the
            atomistic -> C-alpha comparison functor; not counted in the 50/50 split)
Reference lags (tau_ref, frames) are declared per source family so that the atlas height is comparable
to the earlier alanine (100 ps) and CLN025 (10 frames) constructions.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
AMINO = ["ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE",
         "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"]
ONE = dict(ALA="A", ARG="R", ASN="N", ASP="D", CYS="C", GLN="Q", GLU="E", GLY="G", HIS="H", ILE="I",
           LEU="L", LYS="K", MET="M", PHE="F", PRO="P", SER="S", THR="T", TRP="W", TYR="Y", VAL="V")


def build_catalog():
    systems = []
    systems.append(dict(id="ala2", group="atom", label="Alanine dipeptide (mdshare)", loader="ala2", args={},
                        representation="heavy atoms", chart="phi/psi", tau_ref=100, family="mdshare"))
    for aa in AMINO:
        folder = DATA / "dipeptides" / aa
        runs = [p for p in folder.glob("run-*.npz") if ".partial" not in p.name] if folder.exists() else []
        if runs:
            systems.append(dict(id=f"dipeptide-{aa.lower()}", group="atom", label=f"Ace-{aa}-NMe dipeptide (OpenMM)",
                                loader="dipeptide", args=dict(aa=aa), representation="heavy atoms", chart="phi/psi",
                                tau_ref=100, family="dipeptide", runs_available=len(runs)))
    sg = DATA / "sgdml/manifest.json"
    if sg.exists():
        for name, rec in json.loads(sg.read_text()).items():
            if not (DATA / "sgdml" / rec["file"]).exists():
                continue
            fam = "md17" if name.startswith("md17") else "md22"
            systems.append(dict(id=f"sgdml-{name.lower().replace('_', '-')}", group="atom",
                                label=f"{name.split('_', 1)[1]} ({fam.upper()} ab initio MD)", loader="sgdml",
                                args=dict(name=name), representation="heavy atoms", chart="PCA-2 (aligned heavy atoms)",
                                tau_ref=200 if fam == "md17" else 100, family=fam))
    if (ROOT.parent / "alanine-nerve/data/chignolin/manifest.json").exists():
        systems.append(dict(id="cln025", group="backbone", label="Chignolin CLN025 (128-run subset)", loader="cln025",
                            args={}, representation="C-alpha", chart="PCA-2 (aligned C-alpha)", tau_ref=10, family="cln025"))
    md = DATA / "mdcath/manifest.json"
    if md.exists():
        for dom in json.loads(md.read_text()):
            if not (DATA / "mdcath" / f"mdcath_dataset_{dom}.h5").exists():
                continue
            systems.append(dict(id=f"mdcath-{dom.lower()}-ca", group="backbone", label=f"CATH domain {dom} (mdCATH), C-alpha",
                                loader="mdcath", args=dict(domain=dom, representation="ca"), representation="C-alpha",
                                chart="PCA-2 (aligned C-alpha)", tau_ref=10, family="mdcath"))
            systems.append(dict(id=f"mdcath-{dom.lower()}-heavy", group="paired", label=f"CATH domain {dom} (mdCATH), heavy atoms",
                                loader="mdcath", args=dict(domain=dom, representation="heavy"), representation="heavy atoms",
                                chart="PCA-2 (aligned heavy atoms)", tau_ref=10, family="mdcath", paired_with=f"mdcath-{dom.lower()}-ca"))
    return systems


def write_catalog(path=None):
    systems = build_catalog()
    path = Path(path or ROOT / "catalog/systems.json")
    path.parent.mkdir(exist_ok=True)
    groups = {}
    for s in systems:
        groups[s["group"]] = groups.get(s["group"], 0) + 1
    path.write_text(json.dumps(dict(groups=groups, systems=systems), indent=1))
    return systems, groups


if __name__ == "__main__":
    systems, groups = write_catalog()
    print(json.dumps(groups), len(systems), "systems")
