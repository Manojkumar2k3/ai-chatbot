#  GET 

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "API is working"}


#POST-- send i/p from user and respond

'''from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel): # handling client/user functions
    message: str

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/chat") #request hits here, this is the API endpoint
def chat(req: Request): # FastAPI process input, converts json to py object
    return {"response": f"You said: {req.message}"}'''

# @app.post("/chat")
# def chat(req: Request):
#     return {
#         "original": req.message,
#         "length": len(req.message),
#         "uppercase": req.message.upper()
#     }

''' from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class Request(BaseModel):
    message: str

@app.post("/chat")
def chat(req: Request):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": req.message}
        ]
    )

    return {
        "response": response.choices[0].message.content
    } '''


''' from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

HF_API_KEY = "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"

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

class Request(BaseModel):
    message: str

@app.post("/chat")
def chat(req: Request):
    payload = {
        "inputs": req.message
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    print("RAW TEXT:", response.text)  # ADD THIS

    try:
        result = response.json()
    except Exception:
            return {"error": "Invalid JSON response", "raw": response.text}
         

    print("RAW RESPONSE:", result)  # VERY IMPORTANT

    if isinstance(result, list):
        return {"response": result[0].get("generated_text", "No text found")}

    elif isinstance(result, dict):
        if "error" in result:
            return {"error": result["error"]}
        else:
            return {"response": str(result)}
    else:
            return {"response": "Unexpected response format"} '''



''' from fastapi import FastAPI
from pydantic import BaseModel
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

app = FastAPI()

# Get token from environment
hf_token = os.getenv("HF_TOKEN")

client = InferenceClient(
  model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=hf_token
    
)

class Request(BaseModel):
    message: str

@app.post("/chat")
def chat(req: Request):
    try:
        response = client.chat_completion(
            messages=[
                {"role": "user", "content": req.message}
            ],
            max_tokens=300
        )

        return {
            "response": response.choices[0].message["content"]
        }

    except Exception as e:
        return {"error": str(e)}
    
print("TOKEN:", hf_token) '''

from fastapi import FastAPI
from models.request import Request
from services.ai_service import get_ai_response

app = FastAPI()

@app.post("/chat")
def chat(req: Request):
    response = get_ai_response(req.message)

    return {"response": response}

    