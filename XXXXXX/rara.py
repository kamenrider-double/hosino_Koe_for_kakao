import os
import glob
from openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA 
from langchain.schema import HumanMessage, AIMessage

model = "openai/gpt-5-nano"
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
loader=TextLoader("/workspaces/hosino_Koe_for_kakao/XXXXXX/soudan.txt", encoding="utf-8")
documents=loader.load()
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(documents, embeddings)

retriever = vectorstore.as_retriever()

llm = ChatOpenAI(model=model.join(client), temperature=1.5)

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

A = qa_chain.run(input())

print(A)

