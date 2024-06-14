#!/bin/bash

# Fine-Tuning GPT-2 for VishwamAI Chat Component

# This script fine-tunes the GPT-2 model using the preprocessed AirDialogue dataset.

# Activate the virtual environment
source /home/ubuntu/VishwamAI/vishwamai_env/bin/activate

# Define variables
DATA_DIR="/home/ubuntu/VishwamAI/data/airdialogue_data_1.3"
PREPROCESSED_FILE="$DATA_DIR/airdialogue_preprocessed.txt"
OUTPUT_DIR="/home/ubuntu/VishwamAI/models/gpt2_finetuned"
MODEL_NAME="gpt2"

# Install necessary packages
pip install transformers==4.41.2
pip install torch

# Fine-tune GPT-2
python -m transformers.trainer \
  --model_name_or_path $MODEL_NAME \
  --train_file $PREPROCESSED_FILE \
  --do_train \
  --output_dir $OUTPUT_DIR \
  --per_device_train_batch_size 2 \
  --num_train_epochs 3 \
  --save_steps 1000 \
  --logging_dir /home/ubuntu/VishwamAI/logs/gpt2_finetuning

# Deactivate virtual environment
deactivate

# Print completion message
echo "GPT-2 fine-tuning complete. The fine-tuned model is saved in $OUTPUT_DIR."
