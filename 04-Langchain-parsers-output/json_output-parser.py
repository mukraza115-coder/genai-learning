from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
parser=JsonOutputParser()

template=PromptTemplate(
   template="write 5 facts on {topic} \n{format_instructions}",
   input_variables=["topic"],
   partial_variables={"format_instructions":parser.get_format_instructions()}

)

chain=template|model|parser
result=chain.invoke({"topic":"Black Hole"})

print(result)