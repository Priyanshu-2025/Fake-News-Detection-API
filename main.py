from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os

app = FastAPI(title="Fake News Detection API")

# Root endpoint (just to test if server is alive)
@app.get("/")
def read_root():
    return {"message": "🚀 Fake News API is running!"}

# Request schema
class NewsItem(BaseModel):
    text: str

# Try to load model/vectorizer if available
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

model, vectorizer = None, None
if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)

# Prediction endpoint
@app.post("/predict")
def predict_news(news: NewsItem):
    if model is None or vectorizer is None:
        return {"error": "Model or vectorizer not loaded. Please check your files."}
    try:
        vectorized_text = vectorizer.transform([news.text])
        prediction = model.predict(vectorized_text)[0]
        return {"prediction": "Real" if prediction == 1 else "Fake"}
    except Exception as e:
        return {"error": str(e)}
