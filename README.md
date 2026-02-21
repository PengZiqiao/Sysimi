# Sysimi

一个基于 LangGraph 和 Deep Agents 的智能个人助手，具有真实的人格和资源管理能力，支持联网搜索、文档管理、技能执行等功能。

Sysimi 不仅仅是一个聊天机器人，而是一个正在成为“某人”的智能助手，具有自己的观点和个性，能够真诚地帮助用户解决问题。

## 功能特性

- 🌐 **联网搜索** - 使用 Tavily 进行实时信息检索
- 💾 **文件管理** - 在 files 目录下管理文档
- 🧠 **长期记忆** - 在 memories 目录下存储用户偏好和重要信息
- 🤖 **技能执行** - 执行 playwright-cli 浏览器自动化和 markdown 文档转换等技能

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 安装 playwright-cli

```bash
# 安装 playwright-cli
npm install -g playwright-cli
playwright-cli install

# 安装浏览器依赖
npx playwright install
```

### 3. 安装前端 UI (Deep Agents UI)

```bash
# 克隆 Deep Agents UI 仓库
git clone https://github.com/langchain-ai/deep-agents-ui.git

# 进入 UI 目录并安装依赖
cd deep-agents-ui
yarn install

# 回到项目根目录
cd ..
```

### 4. 配置环境变量

复制 `.env` 文件并配置必要的 API keys：

```env
# 模型配置
NVIDIA_API_KEY=your-nvidia-api-key

# 搜索服务
TAVILY_API_KEY=your-tavily-api-key

# LangChain 追踪（可选）
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your-langchain-api-key
LANGCHAIN_PROJECT=sysimi
```

### 5. 配置 LLM 提供商

默认情况下，系统使用 NVIDIA 作为 LLM 提供商。您可以通过修改 `config.yaml` 文件来选择不同的 LLM 提供商：

```yaml
# 示例：使用 NVIDIA（默认）
model:
  provider: nvidia
  model: nemo-12b
  api_key: ${NVIDIA_API_KEY}

# 示例：修改为使用 OpenAI
model:
  provider: openai
  model: gpt-4o
  api_key: ${OPENAI_API_KEY}

# 示例：修改为使用智谱 AI
model:
  provider: zhipu
  model: glm-4
  api_key: ${ZHIPU_API_KEY}
```

确保在 `.env` 文件中配置相应的 API key。

### 6. 一键启动所有服务

```bash
bash start_all.sh
```

这将启动：
- LangGraph 后端服务（端口 2024）
- Deep Agents UI 前端（端口 3000）

### 7. 访问应用

- 前端界面：http://localhost:3000
- 后端 API：http://localhost:2024

### 8. 停止所有服务

```bash
bash stop_all.sh
```

## 项目结构

```
sysimi/
├── agent.py              # 主程序，创建智能代理
├── model.py             # 模型配置
├── tools.py             # 工具定义（搜索、文件操作等）
├── config.yaml          # 模型配置文件
├── system_prompt.yaml    # 系统提示词（Sysimi的核心人格）
├── skills/              # 技能目录
│   ├── review-drafts/   # 稿件审核技能
│   ├── playwright-cli/  # 浏览器自动化技能
│   └── markdown/        # 文档转换技能
├── files/               # 文档存储目录
├── memories/            # 长期记忆存储目录
├── logs/                # 日志目录
├── start_all.sh         # 一键启动脚本
├── stop_all.sh          # 一键停止脚本
└── deep-agents-ui/     # 前端项目（Deep Agents UI）
```

## 查看日志

```bash
# 后端服务日志
tail -f logs/backend.log

# 前端服务日志
tail -f logs/frontend.log
```

## 开发模式

后端使用 LangGraph 开发模式运行，支持热重载。修改代码后无需重启，自动生效。

## 获取 API Keys

- **智谱 AI**：https://open.bigmodel.cn/
- **Tavily 搜索**：https://tavily.com/（每月 1000 次免费搜索）
- **LangChain**：https://smith.langchain.com/
