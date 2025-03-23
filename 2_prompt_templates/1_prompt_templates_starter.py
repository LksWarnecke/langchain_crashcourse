from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max"

prompt_template = ChatPromptTemplate.from_template(template)

#replacing placeholders
prompt = prompt_template.invoke({
    "tone": "energetic",
    "company": "samsung",
    "position": "AI Engineer",
    "skill": "AI"
})

result = llm.invoke(prompt)

print(result.content)

#Example 2: Prompt with System and Human Message
messages = [
    ("system", "You are a comedian who tells jokes about {topic}.")
    ("human", "Tell me {joke_count} jokes.")
]

prompt_template2 = ChatPromptTemplate.from_messages(messages)
prompt2 = prompt_template2.invoke({
    "topic": "lawyers",
    "joke_count": "3"
})
print("\n---- Prompt with System and Human Message (Tuple) ----\n")
print(prompt2)