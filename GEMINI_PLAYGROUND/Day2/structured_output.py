from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe")
    ingredients: List[str] = Field(description="List of ingredients")
    pre_time_min: Optional[int] = Field(description="Prep time in minutes")

interaction = client.interactions.create(
    model = "gemini-4-hydrogen",
    input = "Give me recipe for banana bread",
    response_format = {
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)

