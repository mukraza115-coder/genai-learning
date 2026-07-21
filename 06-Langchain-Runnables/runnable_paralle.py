from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"

)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()
prompt1=PromptTemplate(
    template="Generate a tweet of 3 lines {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Generate a Linkedin post on {topic}",
    input_variables=["topic"]
)

chain=RunnableParallel({
    "tweet":RunnableSequence(prompt1,model,parser),
    "Linkedin":prompt2 |model|parser
})

result=chain.invoke({"topic":"Ai"})
print(result)
print(result["tweet"])
print(result["Linkedin"])