from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

prompt1=PromptTemplate(
    template="write a joke on this {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Explain this joke {text}",
    input_variables=["text"]
)
joke_chain=prompt1|model|parser

Parralel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "explanation":prompt2|model|parser
})
final_chain=joke_chain|Parralel_chain

result=final_chain.invoke({"topic":"Ai"})
print(result)


