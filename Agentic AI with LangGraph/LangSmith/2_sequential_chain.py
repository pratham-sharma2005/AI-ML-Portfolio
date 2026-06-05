from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["LANGCHAIN_PROJECT"] = "Sequential LLM App" # this over rides the project name mentioned in the .env and u can check this pn the LangSmith site too


load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model1 = ChatOpenAI( model = "gpt-4o-mini" , temperature = 0.7)
model2 = ChatOpenAI( model = "gpt-4o" , temperature = 0.5)

parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model2 | parser


configuration = {
    "run_name" : "sequential chain",
    "tags" : [ "llm app" , "report generation" , "summarization"],
    "metadata" : { "model1" : "4o_mini" , "model1_temp" : "0.7" , "parser used" : "stroutputparser"}
}

result = chain.invoke({'topic': 'Unemployment in India'} , config= configuration)

print(result)
