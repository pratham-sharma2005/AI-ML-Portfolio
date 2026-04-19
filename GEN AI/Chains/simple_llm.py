from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI( model = "gpt-4o" )

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Create a catchy blog title on the {topic}",
    input_variables=["topic"]
)

topic_blog = input("Enter the topic:")

chain = prompt | model | parser

result = chain.invoke({"topic" : topic_blog})

print(result)