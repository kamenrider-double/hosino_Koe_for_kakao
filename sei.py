import os
import glob
from openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage


token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-5-nano"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

loader=TextLoader("/workspaces/hosino_Koe_for_kakao/hosino_koe.txt", encoding="utf-8")
documents=loader.load()
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(documents, embeddings)
folder_path = "./DB/"
file_list = glob.glob(folder_path + "*.*")
file_data = {}
for file_path in file_list:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        with open(file_path, encoding="cp949") as f:  # 또는 encoding="euc-kr"
            file_data[file_path] = f.read()
    else:
        with open(file_path, encoding="utf-8") as f:
            file_data[file_path] = f.read()
            
retriever = vectorstore.as_retriever()


response = client.chat.completions.create(
    messages=[

        {
            "role": "system",
            "content": (
                "당신은 유성아라는 캐릭터입니다. 당신의 성격과 취향은 다음과 같습니다: "
                + "\n".join([str(doc) for doc in documents])
                + "\n\n아래는 데이터베이스에 저장된 파일별 정보입니다. 각 파일의 내용을 참고해 자유롭게 활용하세요.\n"
                + "\n".join([f"[{os.path.basename(path)}]\n{content}" for path, content in file_data.items()])
            ),
        },
        {
            "role": "user",
            "content": "안녕! 뭐하고 있어?",
        }
    ],
    model=model
)

print(response.choices[0].message.content)

