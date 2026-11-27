from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
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

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "explanation": RunnableSequence(prompt2, model, parser),
    "joke": RunnablePassthrough()
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "Alien"})

print(f'Joke ----->>>> {result["joke"]}')
print(f'Explanation ----->>>> {result["explanation"]}')

final_chain.get_graph().print_ascii()
