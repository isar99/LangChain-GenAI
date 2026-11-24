from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-70B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age", gt=18)
    city: str = Field(description="The city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    template=(
        "Generate details for one fictional person related to {place}.\n"
        "Return ONLY a valid JSON object.\n"
        "Do not add markdown.\n"
        "Do not add explanation text.\n"
        "Do not wrap the JSON in any extra object.\n"
        "Do not return a function call or schema.\n"
        "{format_instructions}"
    )
)

chain = template | model | parser

result = chain.invoke({"place": "Japan"})

print(result)
