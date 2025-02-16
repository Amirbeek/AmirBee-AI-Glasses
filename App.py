import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ai_api")

if not API_KEY:
    raise ValueError("API key is missing! Check your .env file.")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://your-site.com",
    "X-Title": "Your Site Name",
}

payload = {
    "model": "deepseek/deepseek-r1",
    "messages": [
        {
            "role": "user",
            "content": "give one word that can make me happy"
        }
    ],
}

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    data=json.dumps(payload)
)

res_json = response.json()

res_role = res_json["choices"][0]["message"]["role"]
res_content = res_json["choices"][0]["message"]["content"]

print("Response status:", response.status_code)
print("\n💡 Assistant's Role:", res_role)
print("\n💡 Assistant's Response:\n", res_content)