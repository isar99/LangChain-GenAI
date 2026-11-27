from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableBranch
from dotenv import load_dotenv

import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)

prompt1 = PromptTemplate(
    template = "Write detailed report about {topic}",
    input_variables = ["topic"]
)
prompt2 = PromptTemplate(
    template = "Summarise this text in less than 500 words \n {text}",
    input_variables = ["text"]
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 20, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({"topic": "Alien"})

print(f'Result ----->>>> {result}')

final_chain.get_graph().print_ascii()
