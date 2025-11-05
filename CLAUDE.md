# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a university course project focused on AI agent development using LangChain. The project is a Python-based application that demonstrates simple agent implementations.

## Development Environment

- **Python**: Requires Python >=3.11
- **Package Manager**: Uses `uv` for dependency management
- **Dependencies**: LangChain ecosystem with Ollama and Tavily integrations

## Common Commands

### Environment Setup
```bash
# Install dependencies
uv sync

# Run the main application
uv run python main.py
```

### Working with Notebooks
The project includes Jupyter notebooks in the `notebook/` directory for experimentation and learning:

```bash
# Start Jupyter to work with notebooks
uv run jupyter notebook

# Or if using VS Code, open notebooks directly
```

## Project Structure

- `main.py`: Entry point with a simple "Hello World" application
- `notebook/`: Contains Jupyter notebooks for agent development experiments
- `pyproject.toml`: Project configuration and dependencies
- `uv.lock`: Locked dependency versions

## Technology Stack

- **LangChain**: Primary framework for building AI agents
- **LangChain-Ollama**: Integration with Ollama for local LLM inference
- **LangChain-Tavily**: Integration with Tavily for web search capabilities
- **python-dotenv**: Environment variable management

## Notes

- This appears to be an educational project for learning AI agent development
- The current main.py is minimal - the main work likely happens in the notebook files
- Dependencies suggest focus on agent-based systems with web search capabilities