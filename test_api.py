import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_API_KEY")

if not token:
    print("❌ 错误: .env 里没有 Token")
    exit()

print(f"🔑 Token: {token[:5]}******")
print("🚀 正在启动 Model Hunter，寻找可用模型...\n")

# 备选模型列表 (按成功率排序)
models_to_test = [
    # 1. 最老但最稳的 v1.5 (如果这个都挂了，那免费版可能全挂了)
    "runwayml/stable-diffusion-v1-5",
    
    # 2. 稍微新一点的 v2.1
    "stabilityai/stable-diffusion-2-1",
    
    # 3. 另一个经典的 v1.4
    "CompVis/stable-diffusion-v1-4",
    
    # 4. OpenJourney (风格化模型)
    "prompthero/openjourney",
    
    # 5. 再次尝试 XL (虽然刚才挂了)
    "stabilityai/stable-diffusion-xl-base-1.0"
]

headers = {"Authorization": f"Bearer {token}"}
payload = {"inputs": "cat"} # 画一只猫，简单快捷

for model in models_to_test:
    # 尝试 router 地址
    api_url = f"https://router.huggingface.co/models/{model}"
    
    print(f"📡 测试模型: {model} ...", end=" ")
    
    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=10)
        
        if response.status_code == 200:
            print("✅ 通了！(200 OK)")
            print(f"🎉 结论: 请在 app.py 里使用这个地址: {api_url}")
            break # 找到一个就行，收工
            
        elif response.status_code == 503:
            print("✅ 通了！(503 Loading)")
            print("⚠️ 模型正在启动中，这是可用的！")
            print(f"🎉 结论: 请在 app.py 里使用这个地址: {api_url}")
            break
            
        elif response.status_code == 404:
            print("❌ 没找到 (404)")
            
        else:
            print(f"❌ 失败 ({response.status_code})")
            
    except Exception as e:
        print(f"❌ 异常")

print("\n🏁 测试结束")