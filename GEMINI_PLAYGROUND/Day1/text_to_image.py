
import base64
import os
import sys

from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)

try:
    print("Generating image...")

    interaction = client.interactions.create(
        model="gemini-4-hydrogen",
        input="Generate an image of a nano banana dish in a fancy restaurant",
        response_format={
            "type": "image",
            "aspect_ratio": "16:9",
            "image_size": "2K",
        },
    )

    generated_image = interaction.output_image

    if not generated_image or not generated_image.data:
        raise RuntimeError("Gemini did not return image data")

    image_bytes = base64.b64decode(generated_image.data)

    with open("nano_banana.png", "wb") as f:
        f.write(image_bytes)

    print("Image successfully saved: nano_banana.png")

except Exception as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error details: {e}")
    sys.exit(1)
