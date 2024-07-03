# Image Generating Agent Demo Documentation

## Overview
This documentation provides an overview of the image-generating agent, including details on how to generate images using sample datasets, improvements made to the model, and instructions on running the demo.

## Model Improvements
The generator model has been adjusted to produce images with the correct output shape of (1080, 1080, 3). The following changes were made:
- Removed redundant debugging print statements from the `build_generator` method.
- Reduced the number of `Conv2DTranspose` layers to ensure the correct output shape.
- Optimized memory usage by reducing the batch size and adding `tf.keras.backend.clear_session()` to free up memory after each image generation.

## Generating Images Using Sample Datasets
The demo script `demo.py` generates images based on text descriptions from a sample dataset. The dataset used is `WikiLitArt-s-entities.csv`, located in the `VishwamAI/data/sample_dataset` directory.

### Steps to Run the Demo
1. Ensure that the required dependencies are installed. You can install them using the following command:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Navigate to the `scripts` directory:
   ```bash
   cd VishwamAI/scripts
   ```

3. Run the demo script:
   ```bash
   python3 demo.py
   ```

4. The generated images will be saved in the `demo_generated_images` directory.

### Script Details
- `generate_demo_images(input_text, num_images=5, output_dir="demo_generated_images")`: Generates a specified number of images based on the input text and saves them in the output directory.
- `read_csv_and_generate_images(csv_file, num_images_per_text=2, output_dir="demo_generated_images")`: Reads the CSV file, extracts text descriptions, and generates images for each description.

## Conclusion
The image-generating agent has been improved to produce images with the correct dimensions and optimized for memory usage. The demo script provides an easy way to generate images based on text descriptions from a sample dataset. Follow the steps outlined in this documentation to run the demo and generate images.

For any further questions or issues, please refer to the project's README file or contact the project maintainers.
