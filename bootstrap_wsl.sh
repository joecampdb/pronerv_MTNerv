#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
# Run inside Ubuntu 22.04. Existing installations may already satisfy these.
sudo apt-get update
sudo apt-get install -y gromacs python3-rdkit python3-numpy python3-scipy python3-mdanalysis python3-matplotlib python3-pytest curl
mkdir -p vendor
url='https://mackerell.umaryland.edu/download.php?filename=CHARMM_ff_params_files/charmm36-jul2022.ff.tgz'
if [[ ! -f vendor/charmm36-jul2022.ff/forcefield.itp ]]; then
  curl -fL --retry 2 "$url" -o vendor/charmm36-jul2022.ff.tgz
  tar -xzf vendor/charmm36-jul2022.ff.tgz -C vendor
fi
python3 -m pytest -q
