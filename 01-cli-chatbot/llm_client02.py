import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

# 初始化客户端
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key="dummy_key",
    timeout=int(os.getenv("REQUEST_TIMEOUT"))
)

def chat_with_history(messages: list) -> str:
    """传入完整对话历史，返回模型回复"""
    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=messages
    )
    return response.choices[0].message.content