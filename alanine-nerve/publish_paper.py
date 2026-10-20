"""Copy the reviewed, compiled paper to its documented distribution paths."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parent
source = root / "output/pdf/paper.pdf"
if not source.is_file():
    raise SystemExit("Compile first: tectonic paper/paper.tex --outdir output/pdf")
for destination in [root/"dist/paper.pdf", root.parent/"paper/molecular-atlas.pdf"]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    print(destination)
