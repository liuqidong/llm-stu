# pip install requests
import requests
import json
import os


# 设置环境变量（新增或修改）
os.environ["OPENAI_BASE_URL"] = "https://api.openai-proxy.org/v1"
os.environ["OPENAI_API_KEY"] = "sk-xwQH3zDFs0rxI7PI5MrDNFep9ELKxTO62QEkt5JQOv98XBiP"

url = os.getenv('OPENAI_BASE_URL') + "/chat/completions"
#print(os.getenv('OPENAI_BASE_URL'))
payload = json.dumps({
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": "assistant"},
        {"role": "user", "content": "Hello"}
    ]
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY'),
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
