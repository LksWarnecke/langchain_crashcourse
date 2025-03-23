from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You love facts and you tell facts about {animal}"),
        ("human", "Tell me {count} facts.")
    ]
)

#Create individual runnables (steps in chain)
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

#Create the RunnableSequence, always takes 3 paramets (first, middle, last) middle can have multiple tasks
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

#Run the chain
response = chain.invoke({"animal": "cat", "count": 2})

print(response)