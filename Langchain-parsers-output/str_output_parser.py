from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm1)


template=PromptTemplate(
    template="write a breif story on {topic}",
    input_variables=["topic"]
)

template1=PromptTemplate(
    template="write a summery of 5 lines on {text}",
    output_varibles=["text"]
)
prompt=template.invoke({"topic":"Black Hole"})

result=model.invoke(prompt)

prompt1=template1.invoke({"text":result.content})

result1=model.invoke(prompt1)

print(result1.content)