from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model = "gpt-4o")

prompt1 = PromptTemplate(
    template="Genrate a detailed report on the {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a 3 line summary on the following text \n {text}",
    input_variables=["text"]
    )

pareser = StrOutputParser()

chain = prompt1 | model | pareser | prompt2 | model | pareser 

result = chain.invoke( {"topic" : "chess"})

# print(result)

chain.get_graph().print_ascii()