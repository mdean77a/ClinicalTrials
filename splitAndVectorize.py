import tiktoken
from langchain_community.vectorstores import Qdrant
from langchain.text_splitter import RecursiveCharacterTextSplitter
import defaults

default_embedding_model = defaults.default_embedding_model
default_location = defaults.default_location

def tiktoken_len(text):
    tokens = tiktoken.encoding_for_model("gpt-4o").encode(
        text,
    )
    return len(tokens)

def split_into_chunks(
        document,
        chunk_size,
        chunk_overlap,
        length_function = tiktoken_len):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function = tiktoken_len
    )
    return text_splitter.split_documents(document)

    

# Create vectorstores
def createVectorstore(
        documents,
        collection_name,
        embedding_model = default_embedding_model,
        location = default_location,
        chunk_size = None,
        chunk_overlap = None,
        ):
    if chunk_size == None:
        vectorStore = Qdrant.from_documents(
            documents=documents,
            embedding=embedding_model,
            location=location,
            collection_name=collection_name,
        )
        return vectorStore
    else:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function = tiktoken_len
        )
        vectorStore = Qdrant.from_documents(
            documents=text_splitter.split_documents(documents),
            embedding  = embedding_model,
            location=location,
            collection_name=collection_name
        )
        return vectorStore
    

    