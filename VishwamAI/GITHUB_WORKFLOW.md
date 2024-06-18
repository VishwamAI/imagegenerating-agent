# GitHub Workflow Documentation

## Overview
This document outlines the steps and processes involved in the development, testing, and deployment of the image-generating web app with a Narendra Modi animation painting mode. The project is based on the `VishwamAI/imagegenerating-agent` repository.

## Setup Instructions

### Cloning the Repository
1. Clone the repository:
   ```bash
   git clone https://github.com/VishwamAI/imagegenerating-agent.git
   cd imagegenerating-agent
   ```

### Installing Dependencies
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the required Node.js packages for the frontend:
   ```bash
   cd /home/ubuntu/image_generation_frontend
   npm install
   ```

### Setting Up the Development Environment
4. Set up the Python interpreter path in Visual Studio Code for improved linting and diagnostics.

5. Initialize a new React project with a TypeScript template:
   ```bash
   npx create-react-app image_generation_frontend --template typescript
   ```

6. Install Chakra UI and its dependencies:
   ```bash
   npm install @chakra-ui/react @emotion/react @emotion/styled framer-motion
   ```

## Development Steps

### Frontend Development
1. Update the `App.tsx` file with a Chakra UI layout.
2. Implement state management and event handling for the "Generate" button.
3. Ensure the frontend makes a POST request to the backend's `/generate` endpoint and displays the generated image.

### Backend Development
1. Set up a Flask server in the `image_generation_backend` directory.
2. Refactor the `vishwamai_prototype.py` script for Flask integration.
3. Write initial setup code with a placeholder endpoint for image generation.
4. Ensure the Flask backend server is running on port 5000.

### Integration
1. Integrate the backend image generation logic with the frontend.
2. Implement and test the "Generate" button functionality to ensure images are generated based on user input and displayed in the frontend.

## Deployment

### Deploying to Netlify
1. Deploy the frontend to Netlify:
   ```bash
   deploy_netlify /home/ubuntu/image_generation_frontend/build
   ```

2. Provide the deployment details to the user.

## Additional Notes
- Ensure the `sample_dataset` directory within the `VishwamAI/data/` directory is not empty to avoid `InvalidArgumentError`.
- Use the `gh` CLI for making pull requests and managing GitHub workflows.
- Check `git status` before committing or adding files.
- Use `git diff` to see changes before committing.
- Do not push directly to the main branch; use pull requests.
- Create a PR with a description using a markdown file, e.g., `/tmp/PR_DESCRIPTION.md`.
- Retrieve PR comments using the `gh api` command.

## Conclusion
This document provides a comprehensive guide to setting up, developing, and deploying the image-generating web app. Follow the steps outlined to ensure a smooth workflow and successful project completion.
