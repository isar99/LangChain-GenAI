from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

import os

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)

# model2 = ChatGoogleGenerativeAI(
#     model = "gemini-3.5-flash",
#     api_key = os.getenv("GEMINI_API_KEY")
# )

prompt1 = PromptTemplate(
    template = "Generate a tweet about {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Generate linkedin post about {topic}",
    input_variables = ["topic"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model1, parser),
    "linkedin": RunnableSequence(prompt2, model1, parser)
})

result = parallel_chain.invoke({"topic": "Python Developer Job"})

print(result)
