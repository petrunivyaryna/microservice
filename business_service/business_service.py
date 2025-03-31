from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

sentiment_analyzer = pipeline("sentiment-analysis")

# Define the input model using Pydantic
class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "This is the Business Logic Service for Sentiment Analysis"}

@app.post("/process")
def process_text(request: TextRequest):
    """
    This endpoint receives a text input and returns the sentiment analysis result.
    """
    text = request.text
    sentiment_result = sentiment_analyzer(text)
    return {"sentiment": sentiment_result[0]["label"], "confidence": sentiment_result[0]["score"]}

@app.get("/health")
def health_check():
    return {"status": "ok"}
