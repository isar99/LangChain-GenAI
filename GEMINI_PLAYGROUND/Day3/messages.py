from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

messages = [
    SystemMessage(content="You are helpful assistant"),
    HumanMessage(content="Tell me about Langchain"),
]

response = llm.invoke(messages)

messages.append(AIMessage(content=response.content))
print(messages)
