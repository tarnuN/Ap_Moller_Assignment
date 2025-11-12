import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_BASE = os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")
MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")

def chat_with_openrouter(prompt: str, temperature: float = 0.3) -> str:
    """Send a message to OpenRouter and return response text."""
    if not API_KEY:
        raise ValueError("❌ OPENROUTER_API_KEY missing in .env")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are an expert data analyst."},
            {"role": "user", "content": prompt},
        ],
        "temperature": temperature,
    }

    response = requests.post(f"{API_BASE}/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"❌ OpenRouter API Error: {response.text}")
