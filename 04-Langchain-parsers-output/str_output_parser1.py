from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template=PromptTemplate(
    template="write a breif story on {topic}",
    input_variables=["topic"]
)

template1=PromptTemplate(
    template="write a summery of 5 lines on {text}",
    output_varibles=["text"]
)

parser=StrOutputParser()

chain=template |model|parser|template1|model|parser

result=chain.invoke({"topic":"Black Hole"})

print(result)

