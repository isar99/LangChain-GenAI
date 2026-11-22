import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

chat = client.chats.create(
    model="gemini-3.8-flash"
)

print("Gemini Chatbot Started!")
print("Type 'exit' to stop.\n")

