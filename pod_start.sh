#!/bin/bash

# Create a virtual environment
python3 -m venv vllm-env

# Activate virtual environment (venv)
source /workspace/vllm-env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install vLLM
pip install vllm
