from langchain_community.tools import tool


# step 1 create a function

# def multiply(a,b):
#     """ multiply 2 numbers""" # reccomended to add a doc string though optional
#     return( a * b )
    

#step 2 add type hints

# def multiply( a: int , b : int ) -> int :
#     """multiply two numbers"""
#     return ( a * b )


# step 3 add tool decoratorc

@tool
def multiply( a: int , b : int ) -> int :
    """multiply two numbers"""
    return ( a * b )

result = multiply.invoke( { "a" :4 , "b" : 6})

print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)