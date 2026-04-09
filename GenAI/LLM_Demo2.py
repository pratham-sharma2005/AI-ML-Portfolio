from langchain_openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

x=input("Enter your query:")

result = llm.invoke(x)

print(result)