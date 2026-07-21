from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda,RunnablePassthrough
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
    template="write a joke on this {topic}",
    input_variables=["topic"]
    )

joke_chain=prompt1 | model | parser

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "word_count":RunnableLambda(word_count)

})

final_chain=joke_chain|parallel_chain

result=final_chain.invoke({"topic":"Ai"})
print(result)