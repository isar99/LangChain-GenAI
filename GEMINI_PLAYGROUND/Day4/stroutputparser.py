from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

import os

load_dotenv()

input_txt = {"topic": "Blackhole"}

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

template1 = PromptTemplate(
    input_variables = ["topic"],
    template = "Write a detailed report on {topic}"
)

template2 = PromptTemplate(
    input_variables = ["text"],
    template = "Write a 5 line summary on following text. /n {text}"
)

parser = StrOutputParser()

chain = template1 | llm | parser | template2 | llm | parser

result = chain.invoke(input_txt)

print(result)
