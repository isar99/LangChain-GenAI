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

prompt1 = PromptTemplate(
    input_variables = ["topic"],
    template = "Generate a detailed report on {topic}"
)

prompt2 = PromptTemplate(
    input_variables = ["text"],
    template = "Generate a 5 point summary from the following text \n {text}"
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "What is freon?"})

print(result)

chain.get_graph().print_ascii()
