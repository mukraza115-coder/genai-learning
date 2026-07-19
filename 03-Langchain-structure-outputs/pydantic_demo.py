from pydantic import BaseModel, ValidationError, Field,EmailStr
from typing import Optional


class student(BaseModel):
    name:str="Ali"
    age:int=12
    Email:EmailStr
    cgpa:float=Field(gt=0,lt=10, description="CGPA must be between 0 and 10")



new_student={"Email":"email123@gmai.com","cgpa":9.5}

Student=student(**new_student)

student_dict=dict(Student)

print(student_dict["age"])