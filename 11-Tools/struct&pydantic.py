from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class Multiplyinput(BaseModel):
    a:int=Field(description="First number to multiply")
    b:int=Field(description="Second number to multiply")

def multiply(a:int,b:int) -> int:
    return a*b

multiply_tool=StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description="Multiply two numbers",
    ags_schema=Multiplyinput
    
)

result=multiply_tool.invoke({"a":3,"b":4})
print(result)