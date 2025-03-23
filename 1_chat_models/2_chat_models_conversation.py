from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Load environment variables from .env
load_dotenv()

#Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4")

chat_history = [] #Use a list to store messages

#Set initial system message (optional)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message) #Add system message to history

#Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    #Get AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")

print("---- Message history -----")
print(chat_history)