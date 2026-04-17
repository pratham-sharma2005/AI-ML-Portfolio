from pydantic import BaseModel

class Student(BaseModel):
    name:str

new_student = { "name" : "Nitish"} 
# if u use number of string in name u will get the error # Input should be a valid string [type=string_type, input_value=32, input_type=int]

student = Student(**new_student)

print(student)


