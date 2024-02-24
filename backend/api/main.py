from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
import sys
from dotenv import load_dotenv
sys.path.append('/home/mubarek/all_about_programing/10x_projects/AI-Contract-Bot')

# Import necessary functions from file_based_rag module
from rag.file_based_rag import load_data, split_text, create_client, define_input_structure, load_text_into_vectorstore, get_answer
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    text: str


def load_env_vars():
    """
    Load environment variables.
    """
    load_dotenv()
    return os.environ["OPENAI_API"]


@app.post("/query")
async def process_query(query: Query):
    OPENAI_KEY = load_env_vars()
    loader = DirectoryLoader('/home/mubarek/all_about_programing/10x_projects/AI-Contract-Bot/files', glob="**/*.pdf")
    data = load_data(loader)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=256)
    docs = split_text(text_splitter, data)
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
    client = create_client(OPENAI_KEY)
    vectorstore = define_input_structure(client)
    load_text_into_vectorstore(vectorstore, docs)
    docs = vectorstore.similarity_search(query.text, k=5)
    chain = load_qa_chain(
        OpenAI(openai_api_key=OPENAI_KEY, temperature=0),
        chain_type="stuff")
    answer = get_answer(chain, docs, query.text)
    return {"Answer": answer}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"/home/mubarek/all_about_programing/10x_projects/AI-Contract-Bot/files/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())
    return {"info": f"file '{file.filename}' stored at location: '{file_location}'"}