#!/usr/bin/env python3
"""
NomadEcho 项目信息查询脚本
显示项目的完整统计和快速导航
"""

import json
from pathlib import Path
import os

def main():
    print("\n")
    print("╔════════════════════════════════════════════════════════╗")
    print("║                                                        ║")
    print("║          ✨ NomadEcho - 旅行感悟分享平台 ✨              ║")
    print("║           灵魂海报生成器版本 v2.0                       ║")
    print("║                                                        ║")
    print("╚════════════════════════════════════════════════════════╝")
    print()
    
    # 项目统计
    print("📊 项目统计")
    print("─" * 58)
    
    app_lines = len(open("app.py").readlines())
    print(f"  • 主程序代码行数：{app_lines} 行")
    print(f"  • 主要函数数量：20+")
    print(f"  • 数据库表数：2（感悟 + 聊天）")
    print(f"  • 文档页数：6")
    print()
    
    # 功能检查
    print("✨ 核心功能")
    print("─" * 58)
    features = [
        ("📝", "感悟发射器", "输入文字 + 8 种情绪标签"),
        ("🔔", "即时回响", "随机展示他人感悟"),
        ("💬", "即时聊天", "实时对话 + 自动刷新"),
        ("🎨", "海报生成器", "AI + 本地双模式"),
    ]
    
    for emoji, name, desc in features:
        print(f"  {emoji} {name:12} {desc}")
    print()
    
    # 文件结构
    print("📁 项目文件")
    print("─" * 58)
    
    files_info = {
        "app.py": f"主应用程序 ({app_lines} 行)",
        "requirements.txt": "项目依赖配置",
        ".env.example": "API Key 配置模板",
        "start.sh": "一键启动脚本",
        "README.md": "项目简介",
        "FEATURES.md": "完整功能指南",
        "POSTER_GUIDE.md": "海报配置教程",
        "RUN.md": "快速启动",
        "COMPLETION.md": "开发完成报告",
        "README_CN.md": "中文详细说明",
    }
    
    for file, desc in files_info.items():
        if Path(file).exists():
            print(f"  ✓ {file:20} {desc}")
        else:
            print(f"  ✗ {file:20} {desc}")
    print()
    
    # 可用的数据文件
    print("💾 数据文件（自动生成）")
    print("─" * 58)
    
    data_files = {
        "insights_data.json": "感悟库",
        "chats.json": "聊天库",
    }
    
    for file, desc in data_files.items():
        if Path(file).exists():
            size = Path(file).stat().st_size
            print(f"  ✓ {file:20} {desc} ({size} 字节)")
        else:
            print(f"  ○ {file:20} {desc} (首次运行自动创建)")
    print()
    
    # 依赖检查
    print("🛠️ 依赖检查")
    print("─" * 58)
    
    deps = [
        "streamlit",
        "streamlit-autorefresh",
        "requests",
        "pillow",
        "python-dotenv",
        "pandas",
    ]
    
    for dep in deps:
        try:
            __import__(dep.replace("-", "_"))
            print(f"  ✓ {dep:25} 已安装")
        except ImportError:
            print(f"  ✗ {dep:25} 未安装")
    print()
    
    # 快速命令
    print("🚀 快速命令")
    print("─" * 58)
    
    commands = [
        ("streamlit run app.py", "启动应用"),
        ("bash start.sh", "启动脚本"),
        ("python3 test_complete.py", "运行完整测试"),
        ("python3 info.py", "显示本信息"),
    ]
    
    for cmd, desc in commands:
        print(f"  $ {cmd:30} # {desc}")
    print()
    
    # 推荐文档阅读顺序
    print("📖 推荐阅读顺序")
    print("─" * 58)
    
    reading_order = [
        ("1.", "README.md", "5 分钟", "项目概览"),
        ("2.", "FEATURES.md", "15 分钟", "完整功能"),
        ("3.", "RUN.md", "5 分钟", "快速启动"),
        ("4.", "POSTER_GUIDE.md", "10 分钟", "海报配置"),
        ("5.", "COMPLETION.md", "5 分钟", "开发报告"),
    ]
    
    for num, file, time, desc in reading_order:
        print(f"  {num:2} {file:18} ({time:5}) - {desc}")
    print()
    
    # 技术栈
    print("💻 技术栈")
    print("─" * 58)
    print("  • 框架：Streamlit 1.28.1")
    print("  • 自动刷新：streamlit-autorefresh 0.0.1")
    print("  • 图像处理：Pillow 10.1.0")
    print("  • HTTP 请求：requests 2.31.0")
    print("  • 环境变量：python-dotenv 1.0.0")
    print("  • 数据处理：Pandas 2.1.3")
    print("  • 可选 AI：Hugging Face API")
    print()
    
    # API 支持
    print("🤖 API 支持")
    print("─" * 58)
    print("  • Hugging Face FLUX.1-schnell（推荐）")
    print("  • Stable Diffusion XL（备选）")
    print("  • 本地美化版（默认免费）")
    print()
    
    # 许可证和联系
    print("ℹ️ 信息")
    print("─" * 58)
    print("  • 许可证：MIT License")
    print("  • 完成日期：2025-01-27")
    print("  • 版本：v2.0")
    print()
    
    # 开始指导
    print("🎯 现在就开始")
    print("─" * 58)
    print()
    print("  1️⃣  安装依赖:")
    print("      pip install -r requirements.txt")
    print()
    print("  2️⃣  运行应用:")
    print("      streamlit run app.py")
    print()
    print("  3️⃣  或使用启动脚本:")
    print("      bash start.sh")
    print()
    print("  4️⃣  阅读文档:")
    print("      cat FEATURES.md")
    print()
    print("─" * 58)
    print()
    print("  ✨ 准备好探索灵魂的共鸣了吗？")
    print()
    print("╔════════════════════════════════════════════════════════╗")
    print("║    Let your soul echo across the world. ✨              ║")
    print("╚════════════════════════════════════════════════════════╝")
    print()

if __name__ == "__main__":
    main()
