import os
import numpy as np
import pandas as pd
import tensorflow as tf
from vishwamai_prototype import VishwamAI, generate_image

def generate_demo_images(vishwamai, input_text, num_images=5, output_dir="demo_generated_images"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for i in range(num_images):
        generated_image = generate_image(vishwamai, input_text)
        tf.keras.preprocessing.image.save_img(f"{output_dir}/generated_image_{i}.png", generated_image[0])
        # Clear session to free memory
        tf.keras.backend.clear_session()
    print(f"Generated {num_images} images based on the input text: '{input_text}'")

def read_csv_and_generate_images(csv_file, num_images_per_text=2, output_dir="demo_generated_images"):  # Reduced num_images_per_text to 2
    df = pd.read_csv(csv_file)
    vishwamai = VishwamAI(batch_size=4)  # Further reduced batch size to 4
    for index, row in df.iterrows():
        input_text = f"{row['wikidata_label']}: {row['wikidata_description']}"
        generate_demo_images(vishwamai, input_text, num_images=num_images_per_text, output_dir=output_dir)

if __name__ == "__main__":
    csv_file = "../data/sample_dataset/WikiLitArt-s-entities.csv"
    read_csv_and_generate_images(csv_file)
