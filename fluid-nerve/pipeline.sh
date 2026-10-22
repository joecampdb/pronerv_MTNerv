#!/usr/bin/env bash
# Full rebuild of every deliverable from the raw data present under data/.
#   bash pipeline.sh            # rebuild only systems without a summary, then everything downstream
#   bash pipeline.sh --force    # rebuild every system
# Logs go to dist/*.log. Raw data acquisition (acquire_*.py, generate_dipeptides.py) is separate.
set -u
cd "$(dirname "$0")"
FORCE=${1:-}
mkdir -p dist
python build_all.py --workers 2 $FORCE        > dist/build_all.log 2>&1
python render.py                              > dist/render.log 2>&1
python render_plate.py                        > dist/render_plate.log 2>&1
python export_homotopy.py                     > dist/export_homotopy.log 2>&1
python compare_all.py                         > dist/compare.log 2>&1
python make_legend.py                         > dist/legend.log 2>&1
python theory/make_results.py                 > dist/make_results.log 2>&1
( cd theory && tectonic fluid-nerve-theory.tex --outdir ../dist ) > dist/tectonic.log 2>&1
python make_atlas_pdf.py                      > dist/atlas.log 2>&1
python make_gallery.py                        > dist/gallery.log 2>&1
echo "PIPELINE_DONE $(date)" >> dist/gallery.log
