from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model = "gemini-4-hydrogen",
    store = False,
    input = history
)

print(f"Response 1: {interaction1.steps[-1].content[0].text}")

for step in interaction1.steps:
        history.append(step.model_dump())

history.append(
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "How many paws are in my house?"}]
    }
)

interaction2 = client.interactions.create(
    model="gemini-4-hydrogen",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
