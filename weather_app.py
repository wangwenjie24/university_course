#!/usr/bin/env python3
"""
Weather Query Interface
A Flask-based web application for querying weather information using LangChain agents.
"""

import os
import json
import requests
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from langchain.chat_models import init_chat_model

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize LangChain components
try:
    llm = init_chat_model(
        model="ollama:qwen3:14b",
        reasoning=False,
    )

    # Create weather-specific search tool
    weather_search = TavilySearch(
        max_results=3,
        topic="general",
    )

    # Create agent with weather search capability
    agent = create_agent(
        model=llm,
        tools=[weather_search]
    )

    AGENT_AVAILABLE = True
except Exception as e:
    print(f"Warning: Agent initialization failed: {e}")
    AGENT_AVAILABLE = False

class WeatherService:
    """Weather service for fetching weather data"""

    @staticmethod
    def get_weather_by_city(city_name):
        """Get weather information using AI agent or fallback method"""
        if AGENT_AVAILABLE:
            try:
                # Use LangChain agent to get weather information
                query = f"今天{city_name}的天气情况怎么样？请提供温度、天气状况、湿度等信息"
                response = agent.invoke({"messages": [{"role": "user", "content": query}]})

                # Extract the assistant's response
                for msg in response["messages"]:
                    if hasattr(msg, 'type') and msg.type == 'ai':
                        return {
                            "success": True,
                            "city": city_name,
                            "data": msg.content,
                            "source": "ai_agent",
                            "timestamp": datetime.now().isoformat()
                        }

                return {
                    "success": False,
                    "error": "无法获取天气信息",
                    "city": city_name
                }
            except Exception as e:
                print(f"Agent error: {e}")
                # Fallback to simple response
                return WeatherService._get_fallback_weather(city_name)
        else:
            return WeatherService._get_fallback_weather(city_name)

    @staticmethod
    def _get_fallback_weather(city_name):
        """Fallback weather information when agent is not available"""
        return {
            "success": True,
            "city": city_name,
            "data": f"由于AI服务暂时不可用，无法获取{city_name}的实时天气信息。请稍后重试或检查其他天气应用。",
            "source": "fallback",
            "timestamp": datetime.now().isoformat()
        }

# Routes
@app.route('/')
def index():
    """Main weather query interface"""
    return render_template('index.html')

@app.route('/api/weather')
def get_weather():
    """API endpoint for weather queries"""
    city = request.args.get('city', '').strip()

    if not city:
        return jsonify({
            "success": False,
            "error": "请输入城市名称"
        }), 400

    try:
        weather_data = WeatherService.get_weather_by_city(city)
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"获取天气信息失败: {str(e)}",
            "city": city
        }), 500

@app.route('/api/status')
def status():
    """API endpoint to check service status"""
    return jsonify({
        "agent_available": AGENT_AVAILABLE,
        "timestamp": datetime.now().isoformat()
    })

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # Create static directory if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')
        os.makedirs('static/css')
        os.makedirs('static/js')

    app.run(debug=True, host='0.0.0.0', port=5000)