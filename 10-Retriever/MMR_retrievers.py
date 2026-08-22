from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
from torch import embedding

load_dotenv()

embadding_model=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

vectore_store=FAISS.from_documents(
    documents=docs,
    embedding=embadding_model,
)
retriever=vectore_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3,"lambda_mult":0.5}  # k = top results, lambda_mult = relevance-diversity balance
)
query="what is langchian"
result=retriever.invoke(query)

for i,doc in enumerate(result):
    print(f"----Result{i+1}---\n")
    print(doc.page_content)