#!/bin/bash

# Setup script for VishwamAI

# Step 1: Update and install system dependencies
sudo apt-get update
sudo apt-get install -y python3.10 python3.10-venv python3.10-dev build-essential wget git

# Step 2: Create and activate virtual environment
python3.10 -m venv vishwamai_env
source vishwamai_env/bin/activate

# Step 3: Upgrade pip and install Python dependencies
pip install --upgrade pip
pip install tensorflow==2.16.1 transformers==4.41.2 torch

# Step 4: Install additional required packages
pip install wikes-toolkit

# Step 5: Clone and install GLIDE package
git clone https://github.com/openai/glide-text2im.git ../glide-text2im
pip install -e ../glide-text2im

# Step 6: Download and extract AirDialogue dataset
mkdir -p data/airdialogue_data_1.3
wget -O data/airdialogue_data_1.3/airdialogue.zip https://example.com/airdialogue.zip
unzip data/airdialogue_data_1.3/airdialogue.zip -d data/airdialogue_data_1.3

# Step 7: Print completion message
echo "Setup complete. The environment is ready for VishwamAI development."
