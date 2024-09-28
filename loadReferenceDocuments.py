import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents.base import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def loadReferenceDocuments(directory):
    separate_pages = []
    # Iterate through all the files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):  # Check if the file is a PDF
            file_path = os.path.join(directory, filename)
            loader = PyMuPDFLoader(file_path)
            page = loader.load()
            separate_pages.extend(page)  # Append the loaded docs to my list
    
    one_document = ""
    for page in separate_pages:
        one_document+= page.page_content

    # text_converter = RecursiveCharacterTextSplitter()
    # new_document = text_converter.create_documents(one_document)
    text_converter = RecursiveCharacterTextSplitter()
    text_chunks = text_converter.split_text(one_document)
    print(text_chunks.count)

    # Convert each chunk into a Document object
    new_document = [Document(page_content=chunk) for chunk in text_chunks]
    return separate_pages, new_document

