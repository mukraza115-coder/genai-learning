from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda,RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text2text-generation",
)
model=ChatHuggingFace(llm=llm)
# model=GoogleGenerativeAI(model="gemini-2.0-flash")
parser1=StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal["positive","negative"]=Field(description="sentiment of the feedback text")


parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="Classify the sentiment of the following feedback text into postive or negative\n {feedback}\n{format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":parser2.get_format_instructions()}
)

classify_chain=prompt1 | model | parser2

prompt2=PromptTemplate(
    template="write a appropriate response of positive feedback {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="positive",prompt2 | model | parser1),
    (lambda x:x.sentiment=="negative",prompt3 | model | parser1),
    RunnableLambda(lambda x: "Invalid sentiment")
    )
chain=classify_chain | branch_chain
result=chain.invoke({"feedback":"I love the product, it works great!"})
print(result)
chain.get_graph().print_ascii()