# VishwamAI

## Overview
VishwamAI is an image-generating chat model designed to create images based on chat interactions. The model is capable of self-improvement and has internet access without relying on APIs and development.

## File Structure
```
VishwamAI/
├── data/               # Directory for datasets
├── models/             # Directory for storing trained models
├── scripts/            # Directory for scripts (e.g., training, preprocessing)
├── notebooks/          # Directory for Jupyter notebooks
├── logs/               # Directory for training logs and metrics
├── docs/               # Directory for documentation
├── config/             # Directory for configuration files
└── README.md           # Project overview and instructions
```

## Components
1. **Generative Model**: The core of VishwamAI is a Generative Adversarial Network (GAN) responsible for generating images.
2. **Natural Language Processing (NLP) Component**: This component handles chat interactions, understanding user inputs, and generating appropriate responses using a transformer-based model like GPT.
3. **Self-Improvement Mechanism**: VishwamAI includes mechanisms for self-tuning and improvement, leveraging internet resources for continuous learning and enhancement.

## High-Level Architecture
1. **Input Handling**: The NLP component processes user inputs and converts them into a format suitable for the generative model.
2. **Image Generation**: The GAN creates images based on the processed inputs.
3. **Output Handling**: The generated images are returned to the user along with any relevant textual responses.
4. **Self-Improvement**: The model periodically accesses internet resources to gather new data and improve its performance.

## Development Steps
1. **Set Up Development Environment**: Install necessary libraries and dependencies, including TensorFlow, transformers, and Flask.
2. **Design Model Architecture**: Define the structure of the GAN and the NLP component.
3. **Collect and Preprocess Data**: Gather datasets for training the model and preprocess them as needed.
4. **Implement Model**: Code the model architecture and training loop.
5. **Train Model**: Train the model on the collected datasets and monitor its performance.
6. **Evaluate and Improve**: Evaluate the model's performance and make necessary adjustments. Implement self-improvement mechanisms.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/VishwamAI/imagegenerating-agent.git
   cd imagegenerating-agent
   ```

2. **Install Dependencies**:
   ```bash
   pip install tensorflow transformers flask
   ```

3. **Set Up Frontend**:
   ```bash
   cd /home/ubuntu/image_generation_frontend
   npm install
   npm start
   ```

4. **Set Up Backend**:
   ```bash
   cd /home/ubuntu/image_generation_backend
   export FLASK_APP=server.py
   flask run --host=0.0.0.0 --port=5000
   ```

## Frontend and Backend Integration
The frontend is developed using React and Chakra UI, and it communicates with the Flask backend server to generate images based on user input. The frontend sends a POST request to the backend's `/generate` endpoint with a description of the desired image. The backend processes the request, generates the image, and returns the image URL to the frontend, which then displays the generated image.

## Changes to `vishwamai_prototype.py`
- Ensured that `image_path` is cast to a string for TensorFlow compatibility.
- Added a step to denormalize generated images to the [0, 255] range.

## Next Steps
1. Confirm the type of images VishwamAI should generate (e.g., realistic photos, cartoons, abstract art).
2. Identify any specific datasets or sources of data for training the model.
3. Begin designing the model architecture based on the confirmed requirements.
