from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path="/Users/prathamsharma/Desktop/untitled folder", # path of the directory
    glob="*.pdf", # patterns of the file we need
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))