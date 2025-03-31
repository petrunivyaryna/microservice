from fastapi import FastAPI, Depends, HTTPException
import requests
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

app = FastAPI()
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

def verify_token(token: str):
    if token != AUTH_TOKEN:
        raise HTTPException(status_code=403, detail="Unauthorized")

@app.get("/")
def read_root():
    return {"message": "This is the Client Service for Sentiment Analysis"}

class DataItem(BaseModel):
    key: str  # Tweet identifier
    value: str  # The actual tweet text

@app.post("/process-data")
def process_data(item: DataItem, token: str = Depends(verify_token)):
    """
    This endpoint checks if sentiment analysis is available.
    If not, it calls the Business Logic Service for analysis.
    """
    db_response = requests.get(f"http://database_service:8002/get/{item.key}").json()
    
    if db_response.get("sentiment") != "Sentiment Not Found":
        return {"key": item.key, "sentiment": db_response["sentiment"]}
    print(item.value)
    business_logic_response = requests.post(
        "http://business_service:8001/process", json={"text": item.value}
    ).json()
    
    sentiment = business_logic_response.get("sentiment", "UNKNOWN")
    requests.post("http://database_service:8002/save-sentiment", json={"key": item.key, "sentiment": sentiment})

    return {"key": item.key, "sentiment": sentiment}

@app.get("/health")
def health_check():
    return {"status": "ok"}
