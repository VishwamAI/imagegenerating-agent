#!/bin/bash

# VishwamAI Setup Script
# This script automates the setup process for VishwamAI, ensuring that all necessary dependencies are installed and the environment is configured correctly.

# Update and upgrade the system
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Python 3.7 and pip
sudo apt-get install -y python3.7 python3.7-venv python3.7-dev
sudo apt-get install -y python3-pip

# Create a virtual environment
python3.7 -m venv vishwamai_env
source vishwamai_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required Python packages
pip install tensorflow==2.16.1
pip install transformers==4.41.2
pip install numpy==1.16.4
pip install onnx==1.5.0
pip install requests
pip install beautifulsoup4
pip install gym
pip install tensorflow-datasets
pip install tensorflow-hub

# Set up directory structure
mkdir -p data models scripts notebooks logs documentation config

# Download necessary datasets or pretrained models (if any)
# Example: wget -P data/ http://example.com/dataset.zip

# Print completion message
echo "VishwamAI setup is complete. The environment is ready for use."

# Deactivate virtual environment
deactivate
