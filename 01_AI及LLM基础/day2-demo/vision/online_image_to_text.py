from openai import OpenAI
import os
os.environ["OPENAI_BASE_URL"] = "https://api.openai-proxy.org/v1"
os.environ["OPENAI_API_KEY"] = "sk-xwQH3zDFs0rxI7PI5MrDNFep9ELKxTO62QEkt5JQOv98XBiP"
client = OpenAI(base_url=os.getenv("OPENAI_BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "这张照片里有什么？"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://p7.itc.cn/q_70/images03/20220805/7a369d8407144b11bfd598091095c959.jpeg",
                        #"url": f"data:image/jpeg;base64,{base64_image}"
                    },
                },
            ],
        }
    ],
    max_tokens=50,
)
print(response.choices[0])
