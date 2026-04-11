# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI(model='gpt-4') # can use hyperparameters like max_completion_tokens=20

# result = model.invoke("Write all the 7 days of a week")

# print(result.content)




# from langchain_openai import ChatOpenAI

# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI(model="gpt-4o")

# x=input("Ask your query:")

# result = model.invoke(x)

# print(result.content)



from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

x= input("Whats your Query:")

result = model.invoke(x)

print(result.content)