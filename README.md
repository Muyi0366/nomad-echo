# 🌍 NomadEcho - 旅行感悟分享平台

> 一个由 Python Streamlit 驱动的极简清冷风格旅行感悟分享平台，集成 AI 驱动的灵魂海报生成器

## ✨ 核心功能

### 1. 📝 感悟发射器
在左侧分享你的旅行感悟，选择情绪标签，一键发送。

### 2. 🔔 即时回响
在右侧随机发现他人的感悟，与陌生的旅人产生共鸣。

### 3. 💬 即时聊天
点击感悟下的💬按钮，与虚拟对话伙伴进行实时灵魂对话。
- 自动保存到 `chats.json`
- 每 3 秒自动刷新
- 美观的左右气泡样式

### 4. 🎨 共鸣海报生成器（✨核心亮点）
从对话中提取关键词，自动生成高美感的灵魂回响海报！
- 🤖 AI 驱动（可选）或本地美化版（默认免费）
- 📸 电影级极简美学风格
- 💬 配文："这是你们灵魂相遇的瞬间"

## 🚀 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 启动应用
```bash
streamlit run app.py
```

应用自动打开：`http://localhost:8501`

### 运行测试
```bash
python3 test_complete.py
```

## 📦 项目结构

```
nomad-echo/
├── app.py                    # 主应用程序（700+ 行）
├── requirements.txt          # 依赖配置
├── .env.example             # API Key 配置模板
│
├── insights_data.json       # 感悟数据库
├── chats.json              # 聊天数据库
│
├── test_chat.py            # 聊天测试
├── test_complete.py        # 完整功能测试
│
├── README.md               # 本文件
├── README_CN.md            # 中文详细文档
├── RUN.md                  # 快速启动指南
├── FEATURES.md             # 完整功能说明
├── POSTER_GUIDE.md         # 海报配置指南
└── start.sh               # 启动脚本
```

## 🎨 设计特点

- **极简清冷风格**：淡雅灰蓝色渐变背景
- **毛玻璃效果**：现代感十足的视觉体验
- **紫蓝色主色**：优雅的渐变配色方案
- **响应式布局**：完美适配各种设备

## 🎯 使用流程

```
1. 分享感悟  →  2. 发现回响  →  3. 发起对话  →  4. 生成海报
```

详细文档：

| 文件 | 说明 |
|------|------|
| [FEATURES.md](FEATURES.md) | 📖 **推荐首先阅读** - 完整功能指南 |
| [POSTER_GUIDE.md](POSTER_GUIDE.md) | 🎨 海报生成配置和使用教程 |
| [RUN.md](RUN.md) | 🚀 快速启动和基础功能 |
| [README_CN.md](README_CN.md) | 🇨🇳 中文详细说明 |

## 🛠️ 技术栈

- **框架**：Streamlit 1.28.1
- **自动刷新**：streamlit-autorefresh
- **图像处理**：Pillow
- **HTTP 请求**：requests
- **环境变量**：python-dotenv
- **可选 AI**：Hugging Face API

## 📊 两种海报生成模式

### 模式 1：本地美化版（默认）
✅ 100% 免费  
✅ 无需 API Key  
✅ 无网络延迟  
✅ 即时生成  

### 模式 2：AI 生成版（可选）
需要 Hugging Face API Key  
真实 AI 生成，每次不同  
更高创意性  

配置方法见 [POSTER_GUIDE.md](POSTER_GUIDE.md)

## 📝 8 种情绪标签

| 标签 | 含义 | 适用场景 |
|------|------|--------|
| ✨ 灵感 | inspiration | 突然的想法、创意顿悟 |
| 🌍 冒险 | adventure | 探险经历、新的体验 |
| 🧘 宁静 | peace | 宁静时刻、心境平和 |
| 💭 思考 | reflection | 深思熟虑、人生感悟 |
| 🎨 创意 | creativity | 艺术灵感、创意表现 |
| ❤️ 感动 | touched | 感人时刻、情感触动 |
| 🌅 希望 | hope | 前行的勇气、美好展望 |
| 🚀 兴奋 | excitement | 兴高采烈、激情时刻 |

## 💾 数据存储

- **insights_data.json**：感悟库（自动创建）
- **chats.json**：聊天库（自动创建）
- 无需数据库，开箱即用

## 🔧 自定义配置

### 配置 API Key（可选）

```bash
# 方式 1：创建 .env 文件
cp .env.example .env
# 编辑 .env，填入你的 Hugging Face token

# 方式 2：设置环境变量
export HF_API_KEY="hf_xxxxxxxxxxxxx"
```

### 获取 Hugging Face API Key

1. 注册：https://huggingface.co
2. Settings → Access Tokens
3. Create token → 复制
4. 粘贴到 .env 文件

详见 [POSTER_GUIDE.md](POSTER_GUIDE.md)

## 🚀 部署到云端

### Streamlit Cloud
1. 推送到 GitHub
2. 在 Streamlit Cloud 部署
3. 在 Secrets 中配置 API Key

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV HF_API_KEY=your_key
CMD ["streamlit", "run", "app.py"]
```

## 💡 创意扩展

未来可添加的功能：

- [ ] 海报下载和分享
- [ ] 海报库和排行榜
- [ ] 按主题定制风格
- [ ] 用户头像和昵称
- [ ] 地理位置标签
- [ ] 感悟统计和可视化
- [ ] 多语言支持

## 🐛 故障排查

**Q: 没有 API Key 也能用吗？**  
A: 完全可以！默认使用本地美化版本，完全免费。

**Q: 海报生成很慢？**  
A: 首次调用需要 5-30 秒加载模型，之后会更快。可直接使用本地版本。

**Q: 如何下载海报？**  
A: 右键点击图片 → 保存图片

详见 [POSTER_GUIDE.md](POSTER_GUIDE.md) 的故障排查部分

## 📄 许可证

MIT License - 自由使用和修改

## 🎉 致谢

- 感谢 Streamlit 社区
- 感谢 Hugging Face 提供免费 API
- 感谢所有用户的支持

---

**让每一次旅行都成为永恒的回忆，让每一个感悟都能被听见。** ✨

**在灵魂相遇的瞬间，生成独一无二的视觉记忆。** 🎨

---

## 📞 快速链接

- 🚀 [快速启动](RUN.md)
- 📖 [完整功能](FEATURES.md)
- 🎨 [海报配置](POSTER_GUIDE.md)
- 🇨🇳 [中文文档](README_CN.md)

**准备好了？**

```bash
streamlit run app.py
```