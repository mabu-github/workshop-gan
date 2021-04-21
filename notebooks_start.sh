#!/usr/bin/env bash

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$script_dir"

eval "$(conda shell.bash hook)"
conda activate workshop_gan
echo $(pwd)/../..
PYTHONPATH=$(pwd) jupyter lab
