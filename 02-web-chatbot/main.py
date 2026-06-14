from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse, RedirectResponse
from pydantic import BaseModel
import redis
import os
from dotenv import load_dotenv
from llm_client import llm_chat_stream

load_dotenv()
app = FastAPI(title="Web ChatBot")

# 静态文件
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Redis
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    db=int(os.getenv("REDIS_DB")),
    decode_responses=True
)

class ChatRequest(BaseModel):
    messages: list

# 根路由直接跳聊天页
@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")


# 流式对话（标准、正规、官方认可写法）
@app.post("/chat/stream")
async def chat_stream(req: ChatRequest, request: Request):
    def sse_generator():
        try:
            for chunk in llm_chat_stream(req.messages):
                # 标准 SSE 格式
                yield f"data: {chunk}\n\n"
        except Exception as e:
            yield f"data: [ERROR] {str(e)}\n\n"

    return StreamingResponse(
        sse_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive"
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)