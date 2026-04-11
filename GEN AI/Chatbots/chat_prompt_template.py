from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([

    # Wrong method in chatprompttemplate case
    # SystemMessage(content="You are a helpful {domain} expert"),
    # HumanMessage(content="Explain in simple terms what is {topic}")

    #right method is 
    ( "system" , "You are a helpful {domain} expert" ),
    ( "user" , "Explain in simple terms what is {topic}")
]
)

prompt = chat_template.invoke({"domain":"cricket" , "topic":"Dusra"})

print(prompt)