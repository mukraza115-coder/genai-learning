from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class multple_strut(BaseModel):
    a:int=Field(description="First number to multiply")
    b:int=Field(description="Second number to multiply")

class multiply_tool(BaseTool):
    name:str="multiply"
    description:str="Multiply two numbers"
    args_schema:Type[BaseModel]=multple_strut

    def _run(self, a:int,b:int) -> int:
        return a*b
    
muliplt_tool=multiply_tool()

result=muliplt_tool.invoke({"a":3,"b":4})

print(result)