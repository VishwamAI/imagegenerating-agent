import os
import sys
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import save_img

# Ensure the correct directory of VishwamAI is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../imagegenerating_agent')))

from VishwamAI.scripts.vishwamai_prototype import VishwamAI, generate_image

# Configure TensorFlow to use dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

# Initialize the VishwamAI model with a further reduced batch size and lower image resolution
vishwamai = VishwamAI(batch_size=2)

# Generate a random image using the model with 4K resolution
description = "Narendra Modi"
resolution = (3840, 2160)  # 4K resolution
generated_image = generate_image(vishwamai, description, resolution)

# Save the generated image to a file
output_dir = "generated_images"
os.makedirs(output_dir, exist_ok=True)
image_path = os.path.join(output_dir, "random_narendra_modi_image_4k.png")
save_img(image_path, generated_image[0])

print(f"Generated 4K image saved to {image_path}")

# Generate a random image using the model with 2K resolution
resolution = (2560, 1440)  # 2K resolution
generated_image = generate_image(vishwamai, description, resolution)

# Save the generated image to a file
image_path = os.path.join(output_dir, "random_narendra_modi_image_2k.png")
save_img(image_path, generated_image[0])

print(f"Generated 2K image saved to {image_path}")
