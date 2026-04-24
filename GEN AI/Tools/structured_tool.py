from langchain_community.tools import StructuredTool
from pydantic import BaseModel , Field


class Multiply_Input(BaseModel):
    a :int = Field( required = True , description= "First number to multiply")
    b :int = Field( required = True , description= "second number to multiply")

def multiply_func( a: int , b : int ) -> int :
    return ( a * b )

multiply_tool = StructuredTool.from_function(
    func= multiply_func,
    description= " multiply two numbers",
    args_schema=Multiply_Input
)

result = multiply_tool.invoke( { "a" : 6 , "b" : 10})

print(result)