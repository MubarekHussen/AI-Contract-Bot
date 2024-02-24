from dotenv import load_dotenv
import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import weaviate
from langchain.vectorstores import Weaviate
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI


def load_env_vars():
    """
    Load environment variables.
    """
    load_dotenv()
    return os.environ["OPENAI_API_KEY"]


def load_data(loader):
    """
    Load data using the provided loader.
    """
    return loader.load()


def split_text(text_splitter, data):
    """
    Split text using the provided text splitter.
    """
    return text_splitter.split_documents(data)


def create_client(OPENAI_KEY):
    """
    Create a Weaviate client.
    """
    return weaviate.Client(
        url="http://localhost:8080",
        additional_headers={"X-OpenAI-Api-Key": OPENAI_KEY},
        startup_period=10
    )


def define_input_structure(client):
    """
    Define input structure for Weaviate client.
    """
    client.schema.delete_all()
    client.schema.get()
    schema = {
        "classes": [
            {
                "class": "Chatbot",
                "description": "Documents for chatbot",
                "vectorizer": "text2vec-openai",
                "moduleConfig": {"text2vec-openai": {"model": "ada", "type": "text"}},
                "properties": [
                    {
                        "dataType": ["text"],
                        "description": "The content of the paragraph",
                        "moduleConfig": {
                            "text2vec-openai": {
                                "skip": False,
                                "vectorizePropertyName": False,
                            }
                        },
                        "name": "content",
                    },
                ],
            },
        ]
    }
    client.schema.create(schema)
    return Weaviate(client, "Chatbot", "content", attributes=["source"])


def load_text_into_vectorstore(vectorstore, docs):
    """
    Load text into the vectorstore.
    """
    text_meta_pair = [(doc.page_content, doc.metadata) for doc in docs]
    texts, meta = list(zip(*text_meta_pair))
    vectorstore.add_texts(texts, meta)


def get_answer(chain, docs, query):
    """
    Get answer for the query.
    """
    return chain.run(input_documents=docs, question=query)


def main():
    OPENAI_KEY = load_env_vars()
    loader = DirectoryLoader('./files', glob="**/*.pdf")
    data = load_data(loader)
    print(f'You have {len(data)} documents in your data')
    print(f'There are {len(data[0].page_content)} characters in your document')
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = split_text(text_splitter, data)
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
    client = create_client(OPENAI_KEY)
    vectorstore = define_input_structure(client)
    load_text_into_vectorstore(vectorstore, docs)
    query = input("Enter your query: ")
    docs = vectorstore.similarity_search(query, k=5)
    chain = load_qa_chain(
        OpenAI(openai_api_key=OPENAI_KEY, temperature=0),
        chain_type="stuff")
    answer = get_answer(chain, docs, query)
    print("Answer:" + answer)


if __name__ == "__main__":
    main()