from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

hf_token = os.getenv("HF_TOKEN")
# print("TOKEN:", hf_token)

client = InferenceClient(
        model="mistralai/Mistral-7B-Instruct-v0.1",
    token=hf_token
)

# 🧠 MEMORY STORAGE
chat_history = []

def get_ai_response(message: str):
    try:
        # Add user message
        chat_history.append({
            "role": "user",
            "content": message
        })

        response = client.chat_completion(
            messages=chat_history,
            max_tokens=300
        )

        reply = response.choices[0].message["content"]

        # Add AI response
        chat_history.append({
            "role": "assistant",
            "content": reply
        })

        return reply

    except Exception as e:
        return str(e)
        