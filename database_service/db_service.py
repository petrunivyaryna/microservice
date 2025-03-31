from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
sentiment_result = {}  # Stores tweet sentiment

class SentimentItem(BaseModel):
    key: str  # Tweet ID or name
    sentiment: str  # Sentiment result

@app.get("/")
def read_root():
    return {"message": "This is the Database Service that returns the sentiment of the text"}

@app.post("/save-sentiment")
def save_sentiment(item: SentimentItem):
    """
    Store the sentiment analysis result of a tweet.
    """
    sentiment_result[item.key] = item.sentiment
    return {"message": f"Sentiment saved for key: {item.key}"}

@app.get("/get/{key}")
def get_data(key: str):
    """
    Retrieve tweet text and sentiment (if available).
    """
    sentiment = sentiment_result.get(key, "Sentiment Not Found")
    return {"key": key, "sentiment": sentiment}

@app.get("/health")
def health_check():
    return {"status": "ok"}
