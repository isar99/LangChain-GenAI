from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)


prompt = PromptTemplate(
    input_variables = ["topic"],
    template = "Generate 5 interesting facts about {topic}"
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({"topic": "Fatima payman"})

print(response)

chain.get_graph().print_ascii()
