from openai import OpenAI
import os
os.environ["OPENAI_BASE_URL"] = "https://api.openai-proxy.org/v1"
os.environ["OPENAI_API_KEY"] = "sk-xwQH3zDFs0rxI7PI5MrDNFep9ELKxTO62QEkt5JQOv98XBiP"
client = OpenAI(base_url=os.getenv("OPENAI_BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))

for i in range(3):
    response = client.chat.completions.create(
        model="gpt-4o",
        # 对于三个请求中的每一个，使用相同的 seed 参数 42，同时将所有其他参数保持相同，我们便能够生成更一致的结果。
        seed=50, #种子
        temperature=0.7,
        max_tokens=50,
        messages=[
            {"role": "system", "content": "你是一个生成故事机器人"},
            {"role": "user", "content": "告诉我一个关于宇宙是如何开始的故事？"}
        ]
    )
    print(f'故事版本{i + 1}：' + response.choices[0].message.content)
    del response
