from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
parser=StrOutputParser()

prompt1=PromptTemplate(

    template="write a detail summery on this {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="write key points from this {text}",
    input_variables=["text"]
)

chain=prompt1 | model | parser | prompt2 | model |parser
result=chain.invoke({"topic":"black hole"})
print(result)

chain.get_graph().print_ascii()