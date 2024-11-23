from fastapi import FastAPI, UploadFile, File
from fastai.vision.all import load_learner, PILImage
import uvicorn
import os

# Initialize the FastAPI app
app = FastAPI()

# Load the trained model
MODEL_PATH = r"C:\Users\91820\Downloads\tomatofruit\tomato_fruit_model.pkl"
model = load_learner(MODEL_PATH)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint for predicting tomato fruit classification.
    """
    # Read the image
    contents = await file.read()
    image = PILImage.create(contents)

    # Perform prediction
    pred, pred_idx, probs = model.predict(image)

    # Return the prediction
    return {
        "prediction": pred,
        "confidence": float(probs[pred_idx])
    }


# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
