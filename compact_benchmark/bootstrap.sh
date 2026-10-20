#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
# Reuse the scientific Python packages already installed for this workspace.
python3 -m venv --system-site-packages vendor/compact-venv
vendor/compact-venv/bin/pip install -r compact_benchmark/requirements-torch.txt \
  --index-url https://download.pytorch.org/whl/cpu
