from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str=Field(description="the name of person")
    age:int=Field(gt=18,description="The age of person")
    city:str=Field(description="the city of person")


parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="write a person information of that{place}\n{format_instructions}",
    input_variables=["place"], 
    partial_variables={"format_instructions":parser.get_format_instructions()}

)

chain=template | model | parser
result=chain.invoke({"place":"Pakistan"})
print(result)