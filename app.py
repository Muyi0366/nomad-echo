import streamlit as st
import json
from datetime import datetime
import random
from pathlib import Path
import time
import os
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import re

# 加载环境变量
from dotenv import load_dotenv
load_dotenv()

# ==================== 1. 基础配置 ====================
st.set_page_config(
    page_title="NomadEcho - 旅行感悟分享",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== 2. 数据管理函数 ====================

def load_chats():
    """加载所有聊天对话"""
    chat_file = Path("chats.json")
    if chat_file.exists():
        with open(chat_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_chats(chats_data):
    """保存聊天对话到文件"""
    with open("chats.json", "w", encoding="utf-8") as f:
        json.dump(chats_data, f, ensure_ascii=False, indent=2)

def get_or_create_conversation(sender_id, recipient_id):
    """获取或创建对话ID"""
    # 确保对话ID唯一且一致（无论谁发给谁，ID都一样）
    conv_id = "_".join(sorted([sender_id, recipient_id]))
    return conv_id

def add_message(sender_id, recipient_id, text):
    """添加新消息"""
    chats_data = load_chats()
    conv_id = get_or_create_conversation(sender_id, recipient_id)
    
    if conv_id not in chats_data:
        chats_data[conv_id] = {
            "participants": sorted([sender_id, recipient_id]),
            "messages": []
        }
    
    message = {
        "sender": sender_id,
        "text": text,
        "timestamp": datetime.now().strftime("%H:%M") # 简化时间显示
    }
    chats_data[conv_id]["messages"].append(message)
    save_chats(chats_data)

def get_conversation(sender_id, recipient_id):
    """获取指定对话的所有消息"""
    chats_data = load_chats()
    conv_id = get_or_create_conversation(sender_id, recipient_id)
    
    if conv_id in chats_data:
        return chats_data[conv_id]["messages"]
    return []

# ==================== 3. 核心功能函数 ====================

def simulate_traveler_reply(user_message, insight_text):
    """AI 旅人自动回复逻辑"""
    reply_templates = {
        "感动": ["✨ 你的话语触动了我，这正是旅行的意义。", "😊 这种感觉我懂，像是在异乡找到了归属。", "💫 谢谢你的分享，让我也感受到了那份温暖。"],
        "大海": ["🌊 大海总是能包容一切心事。", "💙 我也想去海边吹吹风了。", "🐚 听着海浪声，时间好像都变慢了。"],
        "山": ["⛰️ 站在高处看世界，心胸真的会开阔。", "🌲 山里的空气一定很清新吧。", "🧗‍♂️ 攀登的过程虽然累，但值得。"],
        "孤独": ["🌙 孤独有时候也是一种享受。", "🍷 一个人旅行，是和自己对话的最好时机。", "✨ 虽是独行，但我们的灵魂在此刻相遇。"],
    }
    
    default_replies = [
        "🌸 你的描述好有画面感。",
        "💫 真的吗？快多跟我说说。",
        "✨ 这种体验太难得了，真羡慕你。",
        "🎶 你的文字像一首诗。",
        "🚀 下一站你打算去哪里呢？"
    ]
    
    # 简单关键词匹配
    chosen_reply = random.choice(default_replies)
    for key, replies in reply_templates.items():
        if key in user_message or key in insight_text:
            chosen_reply = random.choice(replies)
            break
            
    return chosen_reply

def extract_keywords(messages):
    """简单提取关键词用于海报生成"""
    if not messages:
        return "travel, soul, connection"
    all_text = " ".join([m["text"] for m in messages])
    # 这里简单处理，实际可接更复杂的NLP
    return "Healing, Travel, Connection, Dreamy" 

# ==================== ✅ 永不崩溃版 (云端 + 本地双保险) ====================
def generate_vibe_poster(messages):
    """
    双模海报生成器：
    1. 优先尝试 Hugging Face 云端 AI 绘图。
    2. 如果网络失败，自动降级为本地 PIL 绘图，确保演示不中断。
    """
    # --- 1. 准备工作 ---
    load_dotenv()
    hf_token = os.getenv("HF_API_KEY") or st.session_state.get("hf_api_key")
    keywords = extract_keywords(messages)
    
    # 定义一个本地画图函数（作为备胎）
    def draw_local_poster(kws):
        # 创建一个渐变色背景
        width, height = 800, 600
        img = Image.new('RGB', (width, height), color='#e0c3fc')
        draw = ImageDraw.Draw(img)
        
        # 画一些随机的几何图形作为装饰
        for _ in range(5):
            x0 = random.randint(0, width)
            y0 = random.randint(0, height)
            draw.ellipse([x0, y0, x0+100, y0+100], fill=(255, 255, 255, 50))
            
        # 写字 (如果没有字体就用默认的)
        try:
            # 尝试加载大字体 (Streamlit Cloud 通常有 Dejavu)
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
        except:
            font = ImageFont.load_default()
            
        text = f"Soul Echo: {kws}"
        # 简单的居中计算
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        draw.text(((width - text_w)/2, height/2), text, fill="white", font=font)
        draw.text(((width - text_w)/2 + 2, height/2 + 2), text, fill="#6c5ce7", font=font) # 阴影
        
        return img

    # --- 2. 尝试云端生成 ---
    if hf_token:
        # 使用目前最稳定的 v1-5 模型路由
        api_url = "https://router.huggingface.co/models/runwayml/stable-diffusion-v1-5"
        headers = {"Authorization": f"Bearer {hf_token}"}
        prompt = f"minimalist travel poster, dreamy pastel colors, healing vibe. Keywords: {keywords}. Vector art, flat design."

        try:
            with st.spinner(f"☁️ 正在云端绘图 (Keywords: {keywords})..."):
                # 请求超时设置为 20 秒，避免让用户等太久
                response = requests.post(api_url, headers=headers, json={"inputs": prompt}, timeout=20)
            
            # 只有当状态码是 200 且内容不是 HTML 时才算成功
            if response.status_code == 200 and "text/html" not in response.headers.get("content-type", ""):
                return Image.open(BytesIO(response.content)), keywords
            else:
                # 打印错误但不要崩溃，转入本地模式
                print(f"云端 API 异常: {response.status_code} - {response.text[:100]}")
                st.toast(f"⚠️ 云端繁忙 ({response.status_code})，已切换至本地艺术模式", icon="🎨")
                
        except Exception as e:
            print(f"云端连接错误: {e}")
            st.toast("⚠️ 网络连接超时，已切换至本地艺术模式", icon="🎨")
    
    # --- 3. 启用本地保底模式 ---
    # 只要上面失败了，或者没有 Token，就走这里
    time.sleep(1) # 假装处理一下，给用户一点仪式感
    return draw_local_poster(keywords), keywords

        
# ==================== 4. CSS 样式 (美化界面) ====================
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #f5f5f7 0%, #e8eef5 100%); }
    .insight-card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #e0e0e0;
        margin-bottom: 20px; transition: transform 0.2s;
    }
    .insight-card:hover { transform: translateY(-2px); }
    
    /* 聊天气泡样式 */
    .chat-container { display: flex; flex-direction: column; gap: 15px; padding: 10px; }
    .bubble { max-width: 70%; padding: 12px 16px; border-radius: 18px; position: relative; font-size: 15px; line-height: 1.5; }
    
    .bubble-sent { 
        align_self: flex-end; 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
        color: white; 
        margin-left: auto;
        border-bottom-right-radius: 4px;
    }
    
    .bubble-received { 
        align_self: flex-start; 
        background: #e9ecef; 
        color: #2c3e50; 
        margin-right: auto;
        border-bottom-left-radius: 4px;
    }
    
    .timestamp { font-size: 11px; opacity: 0.7; margin-top: 5px; text-align: right; }
    .bubble-received .timestamp { text-align: left; color: #666; }
</style>
""", unsafe_allow_html=True)

# ==================== 5. 状态初始化 ====================

if "insights" not in st.session_state:
    # 预置一些感悟数据
    st.session_state.insights = [
        {"text": "山色空蒙，云绕峰峦，溪声入耳，心随风远。", "emotion": "🧘 宁静", "timestamp": "2026-01-27 15:09"},
        {"text": "因为站在高处，风把烦恼都带走了，心也跟着自由飞。", "emotion": "✨ 灵感", "timestamp": "2026-01-27 15:31"},
        {"text": "美丽的田园生活，好多羊。", "emotion": "🌍 冒险", "timestamp": "2026-01-27 15:30"}
    ]

if "current_user_id" not in st.session_state:
    st.session_state.current_user_id = f"user_{random.randint(1000,9999)}"

if "selected_insight_idx" not in st.session_state:
    st.session_state.selected_insight_idx = None

if "chat_recipient" not in st.session_state:
    st.session_state.chat_recipient = None

if "traveler_typing" not in st.session_state:
    st.session_state.traveler_typing = False

# ==================== 6. 页面布局 ====================

st.markdown("<h1 style='text-align: center; color: #2c3e50;'>✨ NomadEcho ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f8c8d;'>在旅程中捕捉每一刻的感悟，在回响中感受他人的故事</p>", unsafe_allow_html=True)
st.divider()

# --- 第一层：广场区 ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("🚀 感悟发射器")
    user_insight = st.text_area("分享你的感悟", height=100, label_visibility="collapsed", placeholder="输入你的旅行心情...")
    if st.button("📤 发送感悟", use_container_width=True):
        if user_insight:
            st.session_state.insights.insert(0, {"text": user_insight, "emotion": "✨ 灵感", "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")})
            st.success("已发送！")
            st.rerun()

with col2:
    st.subheader("🔔 即时回响")
    if st.button("🎲 获取他人的感悟", use_container_width=True):
        st.session_state.selected_insight_idx = random.randint(0, len(st.session_state.insights)-1)
        st.session_state.chat_recipient = f"traveler_{random.randint(100,999)}"
        st.rerun()

    # 展示选中的感悟卡片
    if st.session_state.selected_insight_idx is not None:
        idx = st.session_state.selected_insight_idx
        if idx < len(st.session_state.insights):
            item = st.session_state.insights[idx]
            st.markdown(f"""
            <div class="insight-card">
                <div style="font-size:1.1em; color:#34495e; margin-bottom:10px;">"{item['text']}"</div>
                <div style="font-size:0.9em; color:#7f8c8d; display:flex; justify-content:space-between;">
                    <span>{item['emotion']}</span>
                    <span>{item['timestamp']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- 第二层：对话区 (条件渲染) ---
if st.session_state.selected_insight_idx is not None and st.session_state.chat_recipient:
    st.divider()
    st.markdown("### 💭 与旅人对话")
    
    # 渲染历史消息
    chat_container = st.container()
    with chat_container:
        messages = get_conversation(st.session_state.current_user_id, st.session_state.chat_recipient)
        
        if not messages:
            st.info("👋 试着打个招呼吧，比如 '你好' 或 '我也很喜欢这里'")
        
        for msg in messages:
            is_me = msg['sender'] == st.session_state.current_user_id
            align = "bubble-sent" if is_me else "bubble-received"
            
            st.markdown(f"""
            <div style="display:flex; flex-direction:column; width:100%;">
                <div class="bubble {align}">
                    {msg['text']}
                    <div class="timestamp">{msg['timestamp']}</div>
                </div>
            </div>
            <div style="height: 10px;"></div>
            """, unsafe_allow_html=True)

        # 旅人正在输入的动画
        if st.session_state.traveler_typing:
            with st.spinner("对方正在输入..."):
                time.sleep(1.5) # 模拟思考时间
                
                # 生成并保存回复
                last_input = st.session_state.get("last_user_msg", "")
                insight_ctx = st.session_state.insights[st.session_state.selected_insight_idx]['text']
                reply = simulate_traveler_reply(last_input, insight_ctx)
                
                add_message(st.session_state.chat_recipient, st.session_state.current_user_id, reply)
                st.session_state.traveler_typing = False # 结束输入状态
                st.rerun() # 强制刷新显示新消息

# --- 第三层：回响区 (海报) ---
    st.divider()
    st.markdown("### ✨ 生成灵魂回响海报")
    
    c1, c2 = st.columns([1, 2])
    with c1:
        if st.button("✨ 生成海报", type="primary", use_container_width=True):
            if len(messages) < 2:
                st.warning("再多聊两句吧，AI 需要更多灵感！")
            else:
                with st.spinner("正在编织你们的共同记忆..."):
                    img, kws = generate_vibe_poster(messages)
                    if img:
                        st.session_state.poster_img = img
                    else:
                        st.error("生成失败，请检查 .env 配置或稍后再试")
        
        if st.button("🗑️ 清除海报", use_container_width=True):
            if "poster_img" in st.session_state:
                del st.session_state.poster_img

    with c2:
        if "poster_img" in st.session_state:
            st.image(st.session_state.poster_img, caption="NomadEcho - 灵魂回响", use_column_width=True)
        else:
            st.info("当你们的对话产生共鸣时，点击左侧按钮生成海报。")

# ==================== 7. 聊天输入框 (最底层) ====================
# 关键修复：st.chat_input 必须在所有布局代码之后，且不缩进
if st.session_state.selected_insight_idx is not None and st.session_state.chat_recipient:
    user_text = st.chat_input("输入你的回复...", key="chat_input_main")
    
    if user_text:
        # 1. 保存用户消息
        add_message(st.session_state.current_user_id, st.session_state.chat_recipient, user_text)
        
        # 2. 记录最后输入用于AI生成
        st.session_state.last_user_msg = user_text
        
        # 3. 设置AI输入状态并刷新
        st.session_state.traveler_typing = True
        st.rerun()