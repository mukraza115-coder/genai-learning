from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embadding=OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents=[
    "Pakistan is a country in South Asia. It is the world's fifth-most populous country with a population exceeding 225 million.",
    "The capital of Pakistan is Islamabad, which is known for its high standard of living, safety, and abundant greenery.",
    "Pakistan has a rich history and diverse culture, with influences from various civilizations including the Indus Valley Civilization and the Mughal Empire."
]

result=embadding.embed_documents(documents)
print(str(result))
