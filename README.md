# llm-agent-bootcamp 十大项目 + 对应技术栈清单
## 通用全局技术（所有项目共用）
- 开发环境：PyCharm、Python 独立虚拟环境 venv
- 大模型基座：Qwen2-0.5B / Qwen2-1.8B
- 推理服务：Ollama（开发调试）、vLLM（生产上线，全项目兼容切换）
- 接口规范：OpenAI 兼容接口

---
1. **01-cli-chatbot 命令行对话机器人**
技术：OpenAI SDK、Requests、Python 交互式CLI、JSON本地持久化、异常捕获、环境变量配置

2. **02-web-chatbot 网页流式对话机器人**
技术：FastAPI、Uvicorn、原生HTML/JS、SSE流式输出、Redis（会话缓存）、前后端请求转发

3. **03-simple-rag 基础文本RAG**
技术：LlamaIndex、Chroma向量库、BGE-small词嵌入(Embedding)、文本递归切片、TopK向量检索、Prompt工程

4. **04-pdf-rag PDF文档解析RAG**
技术：pdfplumber（PDF解析）、文本清洗、文件上传接口、复用RAG检索链路、文件异常拦截

5. **05-full-rag 商用完整版RAG系统**
技术：模块化代码拆分、BGE-Rerank（结果重排）、对话记忆管理、Redis历史检索增强、知识库增删改查、FastAPI Swagger接口文档、问答结果缓存

6. **06-simple-agent 单工具智能体**
技术：原生手写ReAct（思考/行动/观测）、LangGraph（状态/节点/边）、工具封装、大模型工具调用、调用异常容错

7. **07-multi-tool-agent 多工具协同智能体**
技术：多工具路由调度、DuckDuckGo联网搜索、本地文件检索、日期查询、防死循环限制、Agent+RAG融合、前端工具调用链路可视化

8. **08-lora-finetune QLoRA轻量化微调**
技术：QLoRA、PEFT、bitsandbytes（4bit量化）、Unsloth、Transformers、Datasets、指令数据集、模型训练/早停回调、LoRA权重导出与推理

9. **09-personal-knowledge-assistant 个人综合私有知识库助手（简历主力项目）**
技术：全栈整合（RAG+Rerank+LangGraph多工具Agent+微调模型）、四层分层架构解耦、批量文件上传、知识库分组、功能开关、一键启动脚本

10. **10-advanced-project 工程化生产改造**
技术：Docker、Docker Compose容器化、环境变量统一配置、公共SDK工具包抽取、Python logging分级日志、接口调用统计、架构文档/简历项目梳理
