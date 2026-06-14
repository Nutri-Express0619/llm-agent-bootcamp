import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key="dummy_key",  # Ollama/vLLM 无需真实密钥，占位即可
    timeout=int(os.getenv("LLM_TIMEOUT"))
)


def llm_chat_stream(messages: list):
    """SSE 流式对话，返回迭代器"""
    stream = client.chat.completions.create(
        model= os.getenv("LLM_MODEL"),
        messages=messages,
        stream=True
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

