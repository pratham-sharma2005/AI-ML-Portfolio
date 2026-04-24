from langchain_openai import ChatOpenAI
from langchain_community.tools import tool
from langchain_core.messages import HumanMessage

#tool create 

@tool
def multiply( a: int , b: int ) -> int:
    """ given two numbers a and b , this tool returns their product"""
    return( a * b )


# result = multiply.invoke( { "a" : 10 , "b" : 7})

# print(result)

# print(multiply.name)
# print(multiply.description)
# print(multiply.args)


#tool calling

model = ChatOpenAI()

model_with_tools = model.bind_tools( [ multiply ])

# result = model_with_tools.invoke("Hi how are you ")

x = HumanMessage(" can you multiply 3 with 7 ")

messages = [ x ]

print(messages)


result = model_with_tools.invoke(messages).tool_calls[0]


result_args = result["args"]
print(result_args)



output1 = multiply.invoke(result["args"]) # only argumnet of the tool is passed and we only get theaanswer
print(output1)



output2 = multiply.invoke(result) # the complete tool call is sent and we get the tool message
print(output2)