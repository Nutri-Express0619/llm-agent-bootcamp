import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

# 初始化客户端
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key="dummy_key",  # Ollama 不需要真实密钥，占位即可
    timeout=int(os.getenv("REQUEST_TIMEOUT"))
)

def simple_chat(prompt: str) -> str:
    """单次问答调用"""
    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content