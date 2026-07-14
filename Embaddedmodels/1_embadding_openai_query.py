from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embadding=OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
result=embadding.embed_query("what is the capital of pakistan")
print(str(result))
