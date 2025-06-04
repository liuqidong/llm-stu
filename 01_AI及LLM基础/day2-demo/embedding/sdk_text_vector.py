from openai import OpenAI

import os
os.environ["OPENAI_BASE_URL"] = "https://api.openai-proxy.org/v1"
os.environ["OPENAI_API_KEY"] = "sk-xwQH3zDFs0rxI7PI5MrDNFep9ELKxTO62QEkt5JQOv98XBiP"
client = OpenAI(base_url=os.getenv("OPENAI_BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))


# 调用嵌入 API
def get_embedding(text, model="text-embedding-ada-002"):
    response = client.embeddings.create(
        input=text,
        model=model
    )
    return response.data[0].embedding

# 示例文本
text = "Hello, world!"

# 获取嵌入向量
embedding = get_embedding(text)

print("Embedding vector:", embedding)
