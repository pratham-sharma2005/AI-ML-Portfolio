from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import CSVLoader 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

loader = CSVLoader("/Users/prathamsharma/Desktop/ML_Dataset/UpdatedResumeDataSet.csv")

docs = loader.load()

# print(len(docs))


model = ChatOpenAI(model= "gpt-4o")

prompt = PromptTemplate(
    template="Answer the following question \n {question}, based on the following text \n {text}",
    input_variables=[ "question" , "text"]
)

parser = StrOutputParser()

question = " What is the company name mentioned in the resume? and What is the role and company of the applicant? "

chain = prompt | model | parser

result = chain.invoke( { "question" : question , "text" : docs[0].page_content})

print(result)