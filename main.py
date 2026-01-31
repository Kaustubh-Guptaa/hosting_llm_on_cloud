from fastapi import FastAPI
from pydantic import BaseModel
import requests
import time
import json

VLLM_ENDPOINT = "http://127.0.0.1:1207/v1/chat/completions"

app = FastAPI()

# Input Schema: The prompt sent by the user
class InferenceRequest(BaseModel):
    prompt: str 
    
# API Endpoint    
@app.post("/inference")
def infer(req: InferenceRequest):

    # Time when inference started
    start_time = time.time()

    response = requests.post(
        VLLM_ENDPOINT,
        json={
            "model": "microsoft/Phi-4-mini-instruct",
            "messages": [
                {
                    "role": "user", 
                    "content": req.prompt
                }
            ],
            "max_tokens": 50,
            "temperature": 0.7
        },
        timeout=300
    )
    
    # Time when inference completed
    end_time = time.time()
    
    # Model response to user's prompt
    output = response.json()["choices"][0]["message"]["content"]
    
    # Record inference log
    record = {
        "latency_sec": end_time - start_time,
        "model": "microsoft/Phi-4-mini-instruct",
    }
    
    with open("logs/model_response.jsonl", "a") as f:
        f.write(json.dumps(record) + "\n")
        
    return {
        "output": output,
        "latency": record["latency_sec"]
    }
    
