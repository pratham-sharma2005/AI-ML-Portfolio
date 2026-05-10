from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="Write a short note on {topic}",
    input_variables=["topic"]
)

parsing = StrOutputParser()

model = ChatOpenAI(model="gpt-4o")

chain = prompt | model | parsing 

result = chain.invoke({ "topic" : "india"})

print(result)