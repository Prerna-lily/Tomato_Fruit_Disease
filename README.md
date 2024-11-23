**Project Overview: Tomato Fruit Disease Prediction with CI/CD Deployment**

**Objective**

The goal of this project is to develop and deploy a machine learning model that identifies diseases in tomato fruits from images. The deployment involves creating a RESTful API using FastAPI and setting up a CI/CD pipeline to streamline updates and ensure continuous availability.

**Components**

Model Training (model.py):

Purpose: Train a deep learning model to classify tomato fruit diseases.
Library Used: FastAI for its prebuilt functionalities in computer vision.
Process:
Prepare filtered datasets from the raw image data.
Use a DataBlock pipeline to create DataLoaders.
Train a ResNet18 model with fine-tuning over 10 epochs.
Save the trained model as tomato_fruit_model.pkl for deployment.
API Development (main.py):

Purpose: Serve predictions through an API.
Framework Used: FastAPI for lightweight and efficient API development.
Key Features:
Accepts image uploads.
Processes images and performs predictions using the trained model.
Returns the disease class and prediction confidence.
Containerization (Dockerfile):

Purpose: Package the application and its dependencies into a portable Docker image.
Key Steps:
Use Python slim image for efficiency.
Install dependencies from requirements.txt.
Expose port 8000 for FastAPI to serve requests.
Set uvicorn as the entry point for the application.
Dependency Management (requirements.txt):

Includes essential libraries like FastAI, FastAPI, Pillow, and Uvicorn for API hosting and image processing.

**CI/CD Pipeline:**

Platform: Render is used for automated builds and deployments.
Features:
Automates the deployment process on every Git push.
Builds the application using the Dockerfile or Python commands.
Ensures continuous availability with health monitoring.
