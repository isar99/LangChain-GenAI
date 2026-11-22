from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

interaction1 = client.interactions.create(
    model = "gemini-4-hydrogen",
    input = "One weird cat has 8 legs.",
)

print(f"Response1 -> {interaction1.output_text}")

interaction2 = client.interactions.create(
    model="gemini-4-hydrogen",
    input="Weird cat has how many legs? And how many legs do cat have?",
    previous_interaction_id = interaction1.id,
)

print(f"Response2 -> {interaction2.output_text}")

