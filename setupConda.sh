#!/bin/bash

# script to setup a demo conda environment from scratch
# This will erase previous env with this name and create a new one
# then it will pip install the requirement.txt

# Activate conda base environment
eval "$(conda shell.bash hook)"
conda activate base

# Remove existing environment if it exists
conda env remove --name llm-demo -y

# Create new environment
conda create -name llm-demo python=3.12 -y

# Activate new environment
conda activate llm-demo

# Install requirements
pip install pip-tools
pip-compile requirements.in 
pip install -r requirements.txt 

pip list | grep chain
pip list | grep pydantic

conda activate llm-demo