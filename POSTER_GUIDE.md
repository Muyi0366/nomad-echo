# 🎨 共鸣海报生成器配置指南

## 功能说明

**共鸣海报生成器**是 NomadEcho 的核心创意功能，它能够：

1. 📝 从聊天对话中自动提取关键词
2. 🎨 利用 AI 生成美观的灵魂回响海报
3. ✨ 配上文案"这是你们灵魂相遇的瞬间"

---

## 两种运行模式

### 模式 1️⃣: 本地美化版（无需 API Key）

**特点**：
- 直接运行，无需任何配置
- 生成高美感的占位海报
- 速度快，无网络依赖

**适用场景**：
- 快速演示
- 本地开发测试
- 网络不稳定环境

### 模式 2️⃣: AI 生成版（需要 Hugging Face API Key）

**特点**：
- 真正的 AI 生成海报
- 基于对话内容的创意设计
- 每次生成都不同

**适用场景**：
- 正式部署
- 想要真实 AI 效果
- 拥有 Hugging Face 账户

---

## 获取 Hugging Face API Key

### 第一步：注册账户

1. 访问 [Hugging Face 官网](https://huggingface.co)
2. 点击 "Sign Up" 注册账户
3. 填写邮箱、用户名、密码
4. 验证邮箱

### 第二步：生成 API Key

1. 登录后，点击右上角 **头像** → **Settings**
2. 在左侧菜单选择 **Access Tokens**
3. 点击 **New token** 创建新令牌
4. **Name**: 输入 `nomad-echo-poster` 或任意名称
5. **Type**: 选择 **Read**（只需读权限）
6. 点击 **Create token**
7. **复制** 生成的 token（一长串字符）

### 第三步：配置环境变量

#### 方式 A: 创建 .env 文件（推荐）

在项目根目录创建 `.env` 文件：

```bash
cat > .env << 'EOF'
HF_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
EOF
```

将 `hf_xxxx...` 替换为你的实际 token。

#### 方式 B: 设置系统环境变量

```bash
# Linux / macOS
export HF_API_KEY="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Windows (PowerShell)
$env:HF_API_KEY = "hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

#### 方式 C: 在应用中直接输入

启动应用后，在侧边栏设置面板中输入 API Key。

---

## 使用流程

### 启动应用

```bash
streamlit run app.py
```

### 使用步骤

1. 在左侧分享感悟
2. 在右侧获取他人感悟
3. 点击 💬 发起对话
4. 进行对话交流
5. 点击 ✨ **生成灵魂回响海报**
6. 等待海报生成并展示
7. 欣赏标题："这是你们灵魂相遇的瞬间"

---

## 海报生成流程

```
对话消息
   ↓
提取关键词（自动）
   ↓
构建 AI Prompt
   ↓
调用 Hugging Face API
   ↓
│
├─ 有效响应 → 显示 AI 生成海报 ✨
│
└─ 无效/无 Key → 显示本地美化版本 📸
   ↓
展示标题
   ↓
用户欣赏和下载
```

---

## 海报风格说明

**风格模板**：
```
Minimalist film photography, cinematic lighting, 
healing vibe, highly aesthetic. Soul connection theme.
Keywords: [从对话提取]. Pastel colors, dreamy, 
peaceful, ethereal poster.
```

**视觉特征**：
- 🎬 极简电影摄影风格
- 💡 专业电影级光影
- 🧘 治愈和谐的氛围
- 🎨 柔和的粉彩色系
- ✨ 梦幻虚幻的意境

---

## 关键词提取规则

系统会自动从对话中提取：

1. ✅ 长度 2+ 的中文词汇
2. ❌ 过滤常用虚词（的、是、在、了等）
3. 📍 选取频率最高的 3-5 个词
4. 🔤 用英文逗号连接

**示例**：

| 对话内容 | 提取关键词 |
|---------|---------|
| "在尼泊尔山顶看日出，感到生命的意义" | 尼泊尔, 山顶, 日出, 生命, 意义 |
| "古镇里迷路了，却找到了一家治愈的茶馆" | 古镇, 迷路, 治愈, 茶馆 |

---

## 常见问题

### Q: 没有 API Key 也能生成海报吗？

**A**: 是的！应用会自动生成高质量的本地美化版本，完全免费且速度更快。

### Q: 本地版本和 API 版本有什么区别？

**A**: 
- **本地版本**：确定的设计，基于固定模板，快速
- **API 版本**：AI 生成，每次不同，需要网络和 Key

### Q: API Key 泄露了怎么办？

**A**: 立即进入 Hugging Face 账户，删除该 token 并创建新的。

### Q: 如何下载生成的海报？

**A**: 在 Streamlit 中，右键点击图片 → "保存图片"，或使用浏览器开发工具。

### Q: 生成超时怎么办？

**A**: 通常是 Hugging Face 模型正在加载。稍等片刻重试，或直接使用本地版本。

### Q: 支持其他 AI 模型吗？

**A**: 目前支持：
- `black-forest-labs/FLUX.1-schnell`（推荐，最快）
- `stabilityai/stable-diffusion-xl-base-1.0`（备选）

可在代码中的 `api_url` 变量修改。

---

## 安全建议

✅ **DO**:
- 使用 `.env` 文件管理敏感信息
- 在 `.gitignore` 中添加 `.env`
- 定期轮换 API Key
- 使用具有最小权限的 token

❌ **DON'T**:
- 将 API Key 硬编码到代码中
- 在 Git 提交中包含 .env
- 与他人分享你的 token
- 在公开场合显示 API Key

---

## 高级配置

### 修改生成参数

编辑 `app.py` 中的 `generate_vibe_poster` 函数：

```python
payload = {
    "inputs": prompt,
    "parameters": {
        "height": 600,        # 修改高度
        "width": 800,         # 修改宽度
        "num_inference_steps": 25,  # 步数（多 = 更好但更慢）
    }
}
```

### 自定义风格提示词

修改 `prompt` 变量：

```python
prompt = f"Your custom style. Keywords: {keywords}. Your description."
```

---

## 故障排查

### 问题：显示"未配置 API Key"

**解决**：
1. 检查 `.env` 文件是否存在并正确
2. 重启 Streamlit 应用
3. 若无 Key，使用本地版本（推荐）

### 问题：API 返回 401 错误

**原因**：Token 无效或已过期  
**解决**：重新生成 Hugging Face token

### 问题：API 返回 503 错误

**原因**：模型正在加载中  
**解决**：等待 1-2 分钟后重试

### 问题：海报一直不显示

**原因**：网络超时或模型繁忙  
**解决**：切换到本地版本或稍后重试

---

## 部署到生产环境

### Streamlit Cloud

1. 在项目根目录创建 `.streamlit/secrets.toml`:

```toml
HF_API_KEY = "hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

2. 推送到 GitHub
3. 在 Streamlit Cloud 中部署
4. 无需提交 secrets.toml 到 Git

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV HF_API_KEY=your_key_here
CMD ["streamlit", "run", "app.py"]
```

---

## 成本估算

| 方案 | 成本 | 优点 | 缺点 |
|------|------|------|------|
| 本地版本 | $0 | 免费、无依赖、快速 | 固定设计 |
| Hugging Face 免费 | $0 | AI 生成、免费配额 | 有请求限制 |
| Pro 订阅 | $9/月 | 无限使用 | 需付费 |

> **提示**：免费配额足以月度小规模使用（几百张海报）

---

## 致谢

- 🤗 Hugging Face 提供的推理 API
- 🎨 Black Forest Labs 的 FLUX 模型
- 🖼️ Stability AI 的 Diffusion 模型

---

**准备好了吗？** 🚀

```bash
streamlit run app.py
```

立即体验灵魂海报生成！✨
