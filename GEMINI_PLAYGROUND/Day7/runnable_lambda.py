from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)

prompt = PromptTemplate(
    template = "Write joke about {topic}",
    input_variables = ["topic"]
)

def word_count(text):
    return len(text.split())

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    "word_count": RunnableLambda(word_count),
    "joke": RunnablePassthrough()
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "Alien"})

print(f'Joke ----->>>> {result["joke"]}')
print(f'Word count ----->>>> {result["word_count"]}')

final_chain.get_graph().print_ascii()
