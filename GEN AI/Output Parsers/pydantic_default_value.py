from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str ="Pratham" # set a deafult value in the names
    age:Optional[int] = None 
    email:EmailStr # smart enough to also know if @ is present in the gmail id or not if that is used as an attribute
    cgpa:float = Field( gt=0 , lt=10) # to show cg greater than 0 and less than 10

new_student1 = {"name":"Ram" , "age":32} 

new_student2 = {"name":"Shyam" } 
# if u use number of string in name u will get the error # Input should be a valid string [type=string_type, input_value=32, input_type=int]

new_student3 = {"name":"Lakhan" ,"age":"64"} #pydantic is smart enough to typecast the stribg 32 to integer 32 and show it 



student1 = Student(**new_student1)
student2 = Student(**new_student2)
student3 = Student(**new_student3)

print(student1)
print(student1.name)

print(student2)
print(student2.name)

print(student3)
print(student3.name)