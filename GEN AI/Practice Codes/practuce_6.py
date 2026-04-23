from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from dotenv import load_dotenv
from typing import Annotated,Literal,Optional,TypedDict

load_dotenv()

model = ChatOpenAI( model= "gpt-4o")

class output(TypedDict):
    name_president : Annotated[str ,"name of the president of the country metioned"] 
    name_pm : Annotated[ str , "name of the prime minister of the country metioned" ]
    currency : Annotated[ str , "currency of the country"]

new_model = model.with_structured_output(output)

prompt = PromptTemplate(
    template ="country to study is {country}",
    input_variables=[ "country" ]
)


chain = prompt | new_model

result = chain.invoke( { "country" : "india"})

print("name_president:" , result["name_president"])
print("name_pm:" , result["name_pm"])
print("currency:" , result["currency"])