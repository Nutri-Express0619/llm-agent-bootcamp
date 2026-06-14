from llm_client02 import chat_with_history
import os
import time

def main():
    print("===== D2 多轮对话机器人 =====")
    print("输入 exit 结束对话\n")

    # 全局列表：存储所有轮次对话（上下文核心）
    chat_history = []

    while True:
        user_text = input("你：")
        # 退出判断
        if user_text.strip().lower() == "exit":
            print("AI：再见啦！")
            break
        # 空输入过滤
        if not user_text.strip():
            print("请输入内容！")
            continue

        # 1. 将用户提问加入历史
        chat_history.append({"role": "user", "content": user_text})
        # 2. 调用模型（把完整历史一起传给模型，实现记忆）
        start_time=time.time()
        ai_reply = chat_with_history(chat_history)
        end_time=time.time()
        # 3. 将AI回复加入历史，供下一轮使用
        chat_history.append({"role": "assistant", "content": ai_reply})

        print(f"AI：{ai_reply}\n")
        print(f"⏱ 本次回答耗时：{end_time - start_time:.2f} 秒")


if __name__ == "__main__":
    print("✅ 当前使用模型：", os.getenv("LLM_MODEL"))
    main()
