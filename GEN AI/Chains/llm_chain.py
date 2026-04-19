from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI( model = "gpt-4o")

topic_joke = input("Enter the topic of the joke:")

prompt1 = PromptTemplate(
    template="Frame a joke on the {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the following joke in simple terms:\n{joke}",
    input_variables=["joke"]
)

parser = StrOutputParser()

chain_joke = prompt1 | model | parser 

chain_explanation = prompt2 | model | parser

result_joke = chain_joke.invoke({"topic" : topic_joke}) 

result_explanation = chain_explanation.invoke( {"joke" : result_joke} )

print("Joke:\n", result_joke)
print("\nExplanation:\n", result_explanation)