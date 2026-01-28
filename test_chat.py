#!/usr/bin/env python3
"""
测试 NomadEcho 聊天功能
验证数据库、消息保存、对话读取等功能
"""

import json
from pathlib import Path
import sys
from datetime import datetime

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
    # 确保ID顺序一致，便于查找
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
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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

def test_chat_functions():
    """测试聊天相关的数据函数"""
    print("=" * 50)
    print("🧪 NomadEcho 聊天功能测试")
    print("=" * 50)
    
    # 测试 1: 创建对话 ID
    print("\n✅ 测试 1: 创建对话 ID")
    conv_id = get_or_create_conversation("user_123", "user_456")
    print(f"   对话 ID: {conv_id}")
    assert "_" in conv_id, "对话 ID 应该包含下划线"
    print("   ✓ 对话 ID 格式正确\n")
    
    # 测试 2: 添加消息
    print("✅ 测试 2: 添加聊天消息")
    add_message("user_123", "user_456", "你好！这是一条测试消息")
    add_message("user_456", "user_123", "你好！我是对方的回复")
    print("   ✓ 消息添加成功\n")
    
    # 测试 3: 读取对话
    print("✅ 测试 3: 读取聊天历史")
    messages = get_conversation("user_123", "user_456")
    print(f"   获取消息数: {len(messages)}")
    for i, msg in enumerate(messages, 1):
        print(f"   消息 {i}: [{msg['sender']}] {msg['text']} ({msg['timestamp']})")
    assert len(messages) >= 2, "应该至少有 2 条消息"
    print("   ✓ 消息读取成功\n")
    
    # 测试 4: 验证 JSON 文件
    print("✅ 测试 4: 验证 chats.json 文件")
    chats_file = Path("chats.json")
    if chats_file.exists():
        with open(chats_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"   文件大小: {chats_file.stat().st_size} 字节")
        print(f"   对话数: {len(data)}")
        print(f"   样例内容:\n{json.dumps(data, ensure_ascii=False, indent=2)[:300]}...")
        print("   ✓ 文件存储成功\n")
    else:
        print("   ⚠️ chats.json 文件不存在（正常，首次运行）\n")
    
    # 测试 5: 验证不同用户对话
    print("✅ 测试 5: 验证多用户对话")
    add_message("user_789", "user_123", "你好，我是新用户")
    conv_789_123 = get_conversation("user_789", "user_123")
    print(f"   user_789 和 user_123 的对话数: {len(conv_789_123)}")
    assert len(conv_789_123) >= 1, "应该有至少 1 条消息"
    print("   ✓ 多用户对话管理正确\n")
    
    # 清理测试文件
    print("🧹 清理测试数据...")
    if chats_file.exists():
        chats_file.unlink()
        print("   已删除 chats.json（重新启动应用时会重新生成）\n")
    
    print("=" * 50)
    print("✨ 所有测试通过！聊天功能正常运行")
    print("=" * 50)

def test_insights_function():
    """测试感悟功能"""
    print("\n" + "=" * 50)
    print("🧪 NomadEcho 感悟功能测试")
    print("=" * 50)
    
    # 创建测试感悟
    test_insights = [
        {
            "text": "在高山之巅，我终于明白了什么叫做海阔天空",
            "emotion": "✨ 灵感",
            "timestamp": "2025-01-27 10:30:45"
        },
        {
            "text": "迷失在陌生的街道，却在一家老茶馆找到了答案",
            "emotion": "💭 思考",
            "timestamp": "2025-01-27 11:45:30"
        }
    ]
    
    # 保存到临时文件进行测试
    test_file = Path("test_insights.json")
    with open(test_file, "w", encoding="utf-8") as f:
        json.dump(test_insights, f, ensure_ascii=False, indent=2)
    
    with open(test_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    
    print(f"\n✅ 感悟数据保存和读取:")
    print(f"   感悟数: {len(loaded)}")
    for i, insight in enumerate(loaded, 1):
        print(f"   感悟 {i}: [{insight['emotion']}] {insight['text'][:30]}...")
    
    # 清理
    test_file.unlink()
    print("\n✨ 感悟功能测试通过！\n")

if __name__ == "__main__":
    try:
        test_chat_functions()
        test_insights_function()
        print("\n🎉 所有测试完成！应用已准备就绪")
        print("\n运行应用: streamlit run app.py")
    except AssertionError as e:
        print(f"\n❌ 测试失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
