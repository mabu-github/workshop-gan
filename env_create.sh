#!/usr/bin/env bash

cd $(dirname $0)

if ! type "nvidia-smi" &> /dev/null; then
    cat environment.yml | sed 's/-gpu//g' > environment-nogpu.yml
    PYTHONNOUSERSITE=1 conda env create -f environment-nogpu.yml
    exit 0
fi

PYTHONNOUSERSITE=1 conda env create -f environment.yml
