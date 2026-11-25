from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

import os

load_dotenv()

input_topic = """Over the last two decades, the data industry has been at the forefront of numerous technological transformations. The shift from on-premises infrastructure to cloud-native technologies has enabled organizations to scale rapidly. One thing that has remained the same is that change invariably brings improvement.

Among these advancements, the introduction of Generative Artificial Intelligence (GenAI) is the most significant. By 2025, it is estimated that 10% of all data will originate from GenAI, leading to greater automation, efficiency, and productivity.

One notable advantage of GenAI is its ability to expedite problem-solving, particularly in managing data pipelines. For example, non-technical users can input natural language prompts to generate SQL queries, retrieving specific data points without requiring engineering assistance.

The current enthusiasm for developing GenAI applications is understandable. GenAI can automate complex data analysis, enhance customer service with intelligent chatbots, and drive innovation through predictive analytics and personalized recommendations.

In this article, I will explore how you can utilize unstructured data to build GenAI applications and share how to use them if you are building applications."""

model1 = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)

model2 = ChatGoogleGenerativeAI(
    model = "gemini-3.8-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)

prompt1 = PromptTemplate(
    input_variables = ["text"],
    template = "Generate 5 pointer notes for \n {text}"
)

prompt2 = PromptTemplate(
    input_variables = ["text"],
    template = "Generate 5 quiz for \n {text}"
)

prompt3 = PromptTemplate(
    input_variables = ["notes", "quiz"],
    template = "Merge the provided notes and quiz into a single document \n "
               "notes -> {notes} and quiz -> {quiz}"
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser
})

merge_chain = prompt3 | model2 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({"text": input_topic})

print(result)

chain.get_graph().print_ascii()
