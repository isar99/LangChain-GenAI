from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

prompt1 = template1.format(topic="blackhole")

result = model.invoke(prompt1)

prompt2 = template2.invoke({"text":result.text})

result1 = model.invoke(prompt2)

print(result1.content)

