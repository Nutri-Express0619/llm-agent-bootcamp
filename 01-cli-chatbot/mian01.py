from llm_client01 import simple_chat
import os

if __name__ == "__main__":
    print("=== 基础命令行对话机器人 ===")
    print("✅ 当前使用模型：", os.getenv("LLM_MODEL"))
    user_input = input("请输入问题：")
    res = simple_chat(user_input)
    print(f"AI回复：{res}")