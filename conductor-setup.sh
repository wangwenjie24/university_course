#!/bin/bash

# Conductor Setup Script for University Course AI Agent Project
# This script sets up the environment for new workspaces

set -e  # Exit on any error

echo "🚀 开始设置大学课程AI智能体项目..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ 错误: uv 包管理器未安装"
    echo "请先安装 uv: https://docs.astral.sh/uv/"
    exit 1
fi

# Install dependencies
echo "📦 安装项目依赖..."
uv sync

# Set up environment file
if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        echo "📝 创建环境变量文件..."
        cp .env.example .env
        echo "✅ 已创建 .env 文件"
        echo ""
        echo "⚠️  重要提醒：请编辑 .env 文件并配置以下环境变量："
        echo "   - TAVILY_API_KEY: 从 https://tavily.com/ 获取"
        echo "   - OLLAMA_BASE_URL: Ollama服务地址（可选，默认为 http://localhost:11434）"
        echo ""
    else
        echo "❌ 错误: 找不到 .env.example 文件"
        exit 1
    fi
else
    echo "✅ .env 文件已存在"
fi

# Check if Ollama is running (optional service)
echo "🔍 检查 Ollama 服务状态..."
if curl -s http://localhost:11434/api/tags &> /dev/null; then
    echo "✅ Ollama 服务正在运行"
else
    echo "ℹ️  Ollama 服务未运行（这是可选的）"
    echo "   如需使用本地LLM功能，请启动 Ollama: ollama serve"
fi

# Display project information
echo ""
echo "🎉 项目设置完成！"
echo ""
echo "📚 可用命令："
echo "   - /run: 启动天气查询Web应用"
echo "   - /notebook: 启动 Jupyter Notebook"
echo ""
echo "🌐 天气应用启动后访问: http://localhost:5000"
echo "📓 Notebook 启动后访问: http://localhost:8888"
echo ""
echo "📖 更多信息请查看 README.md"