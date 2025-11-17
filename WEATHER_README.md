# 天气查询界面

一个基于 LangChain 智能体的天气查询 Web 应用程序。

## 功能特性

- 🌤️ **智能天气查询**: 使用 LangChain 和 Tavily 搜索引擎获取实时天气信息
- 🤖 **AI 驱动**: 集成 Ollama 本地大语言模型提供自然语言交互
- 📱 **响应式设计**: 支持桌面和移动设备访问
- ⚡ **实时状态**: 显示 AI 服务状态和系统可用性
- 🔄 **错误处理**: 优雅的错误处理和用户友好的提示

## 技术栈

- **后端**: Flask (Python Web 框架)
- **AI 框架**: LangChain
- **语言模型**: Ollama (qwen3:14b)
- **搜索引擎**: Tavily Search
- **前端**: HTML5, CSS3, Bootstrap 5, JavaScript
- **依赖管理**: uv

## 快速开始

### 1. 环境准备

确保已安装以下软件：

- Python >= 3.11
- Ollama (并已下载 qwen3:14b 模型)
- Tavily API 密钥

### 2. 安装依赖

```bash
# 安装项目依赖
uv sync

# 或者使用 pip
pip install -r requirements.txt  # 如果存在的话
```

### 3. 环境变量配置

创建 `.env` 文件并配置以下变量：

```env
# Tavily API 密钥
TAVILY_API_KEY=your_tavily_api_key_here

# Ollama 配置（如果需要）
OLLAMA_BASE_URL=http://localhost:11434
```

### 4. 启动 Ollama 服务

```bash
# 确保 Ollama 服务正在运行
ollama serve

# 下载 qwen3 模型（如果还没有）
ollama pull qwen3:14b
```

### 5. 运行天气应用

```bash
# 启动 Flask 应用
uv run python weather_app.py
```

应用将在 `http://localhost:5000` 启动。

## 使用说明

1. 打开浏览器访问 `http://localhost:5000`
2. 在搜索框中输入城市名称（如：北京、上海、广州）
3. 点击"查询"按钮或按回车键
4. 等待 AI 智能体获取并分析天气信息
5. 查看详细的天气报告

## API 接口

### GET `/api/weather?city=<城市名称>`

查询指定城市的天气信息。

**参数:**
- `city`: 城市名称（必需）

**响应示例:**
```json
{
  "success": true,
  "city": "北京",
  "data": "今天北京天气晴朗，温度 25°C，湿度 60%，适合外出活动...",
  "source": "ai_agent",
  "timestamp": "2025-11-17T10:30:00.000Z"
}
```

### GET `/api/status`

检查服务状态。

**响应示例:**
```json
{
  "agent_available": true,
  "timestamp": "2025-11-17T10:30:00.000Z"
}
```

## 项目结构

```
.
├── weather_app.py          # 主应用程序文件
├── templates/              # HTML 模板目录
│   ├── index.html         # 主页面模板
│   ├── 404.html           # 404 错误页面
│   └── 500.html           # 500 错误页面
├── static/                # 静态文件目录（由应用自动创建）
│   ├── css/
│   └── js/
├── pyproject.toml         # 项目配置
└── WEATHER_README.md      # 本说明文件
```

## 故障排除

### 1. AI 服务离线

如果右上角状态显示"AI 服务离线"：

- 检查 Ollama 服务是否运行：`ps aux | grep ollama`
- 确认 qwen3:14b 模型已下载：`ollama list`
- 检查 `.env` 文件中的 API 密钥配置

### 2. Tavily API 错误

确保 `TAVILY_API_KEY` 正确设置且有效：

1. 访问 [Tavily](https://tavily.com/) 注册账户
2. 获取 API 密钥
3. 在 `.env` 文件中设置：`TAVILY_API_KEY=your_api_key`

### 3. 端口冲突

如果 5000 端口被占用：

```bash
# 查找占用端口的进程
lsof -i :5000

# 或者修改 weather_app.py 中的端口号
app.run(debug=True, host='0.0.0.0', port=5001)
```

## 开发说明

### 扩展功能

- **自动补全**: 可以添加城市名称自动补全功能
- **历史记录**: 实现查询历史保存和显示
- **天气预报**: 扩展到多天天气预报
- **多语言**: 支持英文等其他语言界面

### 自定义样式

- 修改 `templates/index.html` 中的 CSS 样式
- 添加自定义主题和动画效果
- 集成更多前端框架和组件库

## 许可证

本项目用于大学课程学习和演示目的。

## 贡献

欢迎提交问题报告和功能建议！