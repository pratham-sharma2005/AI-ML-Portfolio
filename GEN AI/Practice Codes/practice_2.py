from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

template1 = PromptTemplate(
    template="Write a detailed report on the topic {text}",
    input_variables=["text"]
)


template2 = PromptTemplate(
    template="Write a 5 line summary on the following text .\n {text} ",
    input_variables=["text"]
)

prompt1 = template1.invoke({"text": "black hole"})
result1 = model.invoke(prompt1)

print("---- REPORT ----")
print(result1.content)

prompt2 = template2.invoke({"text": result1.content})
result2 = model.invoke(prompt2)

print("\n---- SUMMARY ----")
print(result2.content)

result2 = model.invoke(prompt2)

print(result2.content)
