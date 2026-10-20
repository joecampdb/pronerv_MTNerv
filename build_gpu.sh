#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p vendor
curl -fL --retry 2 https://github.com/gromacs/gromacs/archive/refs/tags/v2024.4.tar.gz -o vendor/gromacs-2024.4-source.tar.gz
tar -xzf vendor/gromacs-2024.4-source.tar.gz -C vendor
cmake -S vendor/gromacs-2024.4 -B vendor/gromacs-build-cuda \
  -DGMX_BUILD_OWN_FFTW=ON -DGMX_GPU=CUDA \
  -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda -DCUDA_NVCC_EXECUTABLE=/usr/local/cuda/bin/nvcc \
  -DCUDAToolkit_ROOT=/usr/local/cuda \
  -DGMX_CUDA_TARGET_SM=89 -DGMX_SIMD=AVX2_256 \
  -DCMAKE_INSTALL_PREFIX="$PWD/vendor/gromacs-install" \
  -DGMX_DOWNLOAD_REGRESSIONTESTS=OFF
cmake --build vendor/gromacs-build-cuda -j 8
cmake --install vendor/gromacs-build-cuda
