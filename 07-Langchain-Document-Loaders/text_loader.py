from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

prompt=PromptTemplate(
    template="Summerize this poem in 5 lines \n{poem}",
    input_variables=["poem"]
)

loader=TextLoader("cricket.txt",encoding="utf-8")

docs=loader.load()

print(docs[0])
print(type(docs))
print(len(docs))

chain=prompt | model | parser
print(chain.invoke({"poem":docs[0].page_content}))