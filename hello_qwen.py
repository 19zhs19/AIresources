import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
while True:
    user_input = input("用户：")
    messages.append({'role': 'user', 'content': user_input})
    if user_input.strip() in ["再见", "bye", "结束"]:
        print("助手：感谢您的咨询，再见")
        break
    
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=messages,
        stream=True
    )
    
    for chunk in completion:
        print(chunk.model_dump_json())