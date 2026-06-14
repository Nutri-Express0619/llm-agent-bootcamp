import sys
from llm_client03 import chat_with_history_stream

def main():
    print("===== D3 多轮+流式对话 =====")
    print("输入 exit 结束对话\n")
    chat_history = []

    while True:
        user_text = input("你：")
        if user_text.strip().lower() == "exit":
            print("AI：再见啦！")
            break
        if not user_text.strip():
            print("请输入内容！")
            continue

        chat_history.append({"role": "user", "content": user_text})
        sys.stdout.write("AI：")
        sys.stdout.flush()

        full_reply = ""
        for chunk in chat_with_history_stream(chat_history):
            sys.stdout.write(chunk)
            sys.stdout.flush()
            full_reply += chunk

        sys.stdout.write("\n\n")
        sys.stdout.flush()
        chat_history.append({"role": "assistant", "content": full_reply})

if __name__ == "__main__":
    main()