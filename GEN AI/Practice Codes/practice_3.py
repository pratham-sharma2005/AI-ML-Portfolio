from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

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


parser = StrOutputParser() # removes garbage data and gives only the required data or the detailed report

chain = template1 | model | parser | template2 | model | parser 

result = chain.invoke({"text":"black hole"})

print(result)