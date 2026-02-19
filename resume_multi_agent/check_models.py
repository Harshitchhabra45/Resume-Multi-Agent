from google import genai
import os

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("API key not found in environment")
else:
    client = genai.Client(api_key=api_key)
    print("Available models:\n")
    for m in client.models.list():
        print(m.name)
