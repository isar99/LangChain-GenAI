from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-70B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
    template="Give me 5 facts about {topic} \n {format_instruction}"
)

chain = template | model | parser

result = chain.invoke({"topic": "Python programming"})

print(result)

# prompt = template.format()

# print("Prompt:", prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)
# print(type(final_result))
