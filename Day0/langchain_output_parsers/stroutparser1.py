from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-70B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# 1st prompt
template1 = PromptTemplate(
    input_variables=["topic"],
    template="Write a detailed report on {topic}"
)

# 2nd prompt
template2 = PromptTemplate(
    input_variables=["text"],
    template="Write a 5 line summary on following text. /n {text}"
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic":"blackhole"})

print(result)
