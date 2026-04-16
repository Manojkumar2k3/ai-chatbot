from fastapi import FastAPI
from models.request import Request
from services.ai_service import get_ai_response

app = FastAPI()

# 🔵 Existing: Chat route (keep this)
@app.post("/chat")
def chat(req: Request):
    response = get_ai_response(req.message)
    return {"response": response}

# 🟢 NEW: Home route
@app.get("/")
def home():
    return {"message": "Chatbot is running"}

