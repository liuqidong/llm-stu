from openai import OpenAI
# pip install openai==1.40.3
import os
# os.environ["OPENAI_BASE_URL"] = "https://api.openai-proxy.org/v1"
# os.environ["OPENAI_API_KEY"] = "sk-xwQH3zDFs0rxI7PI5MrDNFep9ELKxTO62QEkt5JQOv98XBiP"
# # 从环境变量中读取OPENAI_BASE_URL
# print(os.getenv('OPENAI_BASE_URL'))
# 初始化 OpenAI 服务。
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "assistant"},
        {"role": "user", "content": "Hello"}
    ]
)
print(completion.choices[0].message.content)