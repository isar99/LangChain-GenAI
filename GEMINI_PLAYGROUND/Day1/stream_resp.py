from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

stream = client.interactions.create(
    model ="gemini-4-hydrogen",
    input = "Why gemini-4-hydrogen is named like this?",
    stream = True
)

for event in stream:
    print(event)
