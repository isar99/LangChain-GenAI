from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

interaction = client.interactions.create(
    model = "gemini-4-hydrogen",
    input = "Who won Euro 2024",
    tools = [{"type": "google_search"}]
)

print(interaction.output_text)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\ncitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f" [{annotation.title}]({annotation.url})")
