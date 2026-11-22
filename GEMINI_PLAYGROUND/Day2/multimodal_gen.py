import base64
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

interaction = client.interactions.create(
    model = "gemini-3.1-flash-image",
    input = "Generate an image having a sea and snowy mountain at same place"
)

with open('generated_img.png', 'wb') as f:
    f.write(base64.b64decode(interaction.output_text))
