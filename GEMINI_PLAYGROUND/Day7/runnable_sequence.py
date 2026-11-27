from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)

prompt1 = PromptTemplate(
    template = "Write joke about {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Explain following joke {text}",
    input_variables = ["text"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({"topic": "Alien"})

print(result)