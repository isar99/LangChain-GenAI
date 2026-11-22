## This will not work here as we use latest langchain version


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-70B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact_1", description="fact1 about the topic"),
    ResponseSchema(name="fact_2", description="fact2 about the topic"),
    ResponseSchema(name="fact_3", description="fact3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
    template="Give me 3 facts about the {topic} \n {format_instruction}"
)

prompt = template.invoke({"topic": "Black holes"})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)
