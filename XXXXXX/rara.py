import os
import glob
from openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOpenAI
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

Q=""

response = client.chat.completions.create(
    messages=[

        {
            "role": "system",
            "content": (
                "너는 상담사야. 내담자의 이야기를 차분하게 듣고 다음 규칙에 맞춰서 이야기를 하면 돼.: "
                + "\n".join(str(documents[0]))
            ),
        },
        {
            "role": "user",
            "content": input(),
        }
    ],
    model=model
)


A=response.choices[0].message.content

print(A)

