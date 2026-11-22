import base64
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()

image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model = "gemini-4-hydrogen",
    input = [
        {"type": "text", "text": "Describe this image"},
        {"type": "image", "data":image_b64, "mime_type": "image/jpeg"}
    ]
)

print(interaction.output_text)

# interaction = client.interactions.create(
#     model = "gemini-4-hydrogen",
#     input = [
#         {"type": "text", "text": "Describe this audio"},
#         {"type": "audio", "uri":"image_b64", "mime_type": "audio/mp3"}
#     ]
# )
