from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model=GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

prompt=PromptTemplate(
    template="write 2 lines summery on this {topic}",
    input_variables=["topic"]
)

parser=StrOutputParser()

chain= prompt | model | parser
result=chain.invoke({"topic":"black hole"})
print(result)
