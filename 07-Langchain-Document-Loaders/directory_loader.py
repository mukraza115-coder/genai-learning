from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path="book",
    glob="*.pdf",
    loader_cls=PyPDFLoader

)
docs=loader.load()
#using lazy_load

docs1=loader.lazy_load()

for documents in docs1:
    print(documents.metadata)