# 大学课程项目

这是一个基于 LangChain 的 AI 智能体开发大学课程项目。

## 项目简介

本项目专注于 AI 智能体的开发与实验，使用 LangChain 框架构建智能代理系统，集成了本地大语言模型推理和网络搜索功能。

## 技术栈

- **Python**: >=3.11
- **LangChain**: AI 智能体开发框架
- **LangChain-Ollama**: 本地 LLM 推理集成
- **LangChain-Tavily**: 网络搜索功能集成
- **Flask**: Web 框架
- **python-dotenv**: 环境变量管理

## 环境配置

### 1. 安装依赖

```bash
# 使用 uv 安装项目依赖
uv sync
```

### 2. 环境变量配置

复制环境变量示例文件并配置：

```bash
# 复制环境变量示例文件
cp .env.example .env

# 编辑 .env 文件，填入你的 API 密钥和配置
```

需要配置的环境变量：

- **TAVILY_API_KEY**: Tavily API 密钥，用于网络搜索功能
  - 获取地址：https://tavily.com/
- **OLLAMA_BASE_URL**: Ollama 服务地址（可选，默认为 http://localhost:11434）

### 3. 启动 Ollama 服务（可选）

如果使用本地大语言模型，需要先启动 Ollama 服务：

```bash
# 安装并启动 Ollama
# 参考：https://ollama.com/
ollama serve
```

### 4. 运行项目

#### 运行主程序
```bash
# 运行主程序
uv run python main.py
```

#### 运行天气查询界面
```bash
# 启动天气查询 Web 应用
uv run python weather_app.py
```
然后在浏览器中访问 `http://localhost:5000`

### 5. 使用 Jupyter Notebook

项目包含实验性的 Jupyter Notebook 文件，用于智能体开发的实验和学习：

```bash
# 启动 Jupyter Notebook
uv run jupyter notebook

# 或直接在 VS Code 中打开 notebook 文件
```

## 项目结构

```
university_course/
├── main.py              # 主程序入口
├── weather_app.py       # 天气查询 Web 应用
├── templates/           # HTML 模板文件
│   ├── index.html      # 天气查询主页面
│   ├── 404.html        # 404 错误页面
│   └── 500.html        # 500 错误页面
├── notebook/            # Jupyter Notebook 实验文件
│   └── 01-smiple_agent.ipynb
├── pyproject.toml       # 项目配置和依赖
├── uv.lock              # 锁定的依赖版本
├── .env.example         # 环境变量示例文件
├── README.md           # 项目说明文档
└── WEATHER_README.md    # 天气应用详细说明
```

## 功能特性

- 基于 LangChain 的智能体开发
- 集成本地大语言模型支持（Ollama）
- 网络搜索能力（Tavily）
- **天气查询界面**: 基于 AI 智能体的实时天气查询 Web 应用
- 响应式 Web 界面设计
- 教学实验和原型开发

## 开发说明

这是一个教育性质的项目，主要用于学习 AI 智能体开发。主要的开发工作在 `notebook/` 目录中的 Jupyter Notebook 文件中进行。

## 许可证

请查看项目许可证文件了解详情。