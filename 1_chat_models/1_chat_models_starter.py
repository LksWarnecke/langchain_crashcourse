from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

messages = [
    SystemMessage("You are an expert in social media content strategyy"),
    HumanMessage("Give a short tip to create engaging posts on Instagram"),
    AIMessage(),
]

#invoke keyword makes api call to OpenAI
result = llm.invoke(messages)

print(result.content)

