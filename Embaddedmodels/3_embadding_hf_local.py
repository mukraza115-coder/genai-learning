from langchain_huggingface import HuggingFaceEmbeddings

embadding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents=[
    "Pakistan is a country in South Asia. It is the world's fifth-most populous country with a population exceeding 225 million.",
    "The capital of Pakistan is Islamabad, which is known for its high standard of living, safety, and abundant greenery.",
    "Pakistan has a rich history and diverse culture, with influences from various civilizations including the Indus Valley Civilization and the Mughal Empire."
]

vector=embadding.embed_documents(documents)
print(str(vector))

#___________________for multiple text_______________________
from langchain_huggingface import HuggingFaceEmbeddings

embadding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text="Pakistan is a country in South Asia. It is the world's fifth-most populous country with a population exceeding 225 million."

vector=embadding.embed_query(text)
print(str(vector))
