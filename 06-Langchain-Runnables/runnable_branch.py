from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Wite a brief summery on{topic}",
    input_vairables=["topic"]
)
prompt2=PromptTemplate(
    template="Short this summery{text}",
    input_variables=["text"]
)

chain1=prompt1 | model | parser
Chain2=RunnableBranch(
    (lambda x: len(x.split())>100 ,prompt2 | model|parser) ,
    RunnablePassthrough()
)

final_chain=chain1 | Chain2

result=final_chain.invoke({"topic":"Ai"})
print(result)