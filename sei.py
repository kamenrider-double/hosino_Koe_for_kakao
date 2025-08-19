import os
from openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage


token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-5-nano"
loader=TextLoader("/workspaces/hosino_Koe_for_kakao/hosino_koe.txt", encoding="utf-8")
documents=loader.load()

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever("/workspaces/hosino_Koe_for_kakao/DB/*")


response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": retriever.get_relevant_documents(f"당신은 유성아라는 캐릭터입니다. 당신의 성격과 취향은 다음과 같습니다: {documents} 이것을 참조하세요."),
        },
        {
            "role": "user",
            "content": "안녕! 뭐하고 있어?",
        }
    ],
    model=model
)

print(response.choices[0].message.content)

