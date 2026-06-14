import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key="dummy_key",
    timeout=int(os.getenv("REQUEST_TIMEOUT"))
)

def chat_with_history_stream(messages: list):
    """流式生成器，返回每一个chunk"""
    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=messages,
        stream=True
    )
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            yield content