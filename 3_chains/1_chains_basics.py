from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4")

#Define prompt templates
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}.")
        ("human", "Tell me {fact_count} fatcs.")
    ]
)

#Create the combined chain using LangChain Expression
chain = prompt_template | model | StrOutputParser()