from flask import Flask, render_template, jsonify, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import json

# 載入環境變數
load_dotenv()

app = Flask(__name__)

# OpenWeatherMap API 設定
API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
WEATHER_DATA_FILE = "weather_data.json"

def save_weather_data(data):
    """保存天氣數據到 JSON 文件"""
    data['updatedAt'] = datetime.now().isoformat()
    with open(WEATHER_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather/<city>')
def get_weather(city):
    try:
        # 發送請求到 OpenWeatherMap API
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric',  # 使用攝氏溫度
            'lang': 'zh_tw'    # 使用繁體中文
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            # 保存數據到文件
            save_weather_data(data)
            
            # 從 API 響應中獲取數據更新時間（Unix timestamp）並轉換為本地時間
            weather_time = datetime.fromtimestamp(data['dt'])
            weather_time = weather_time.replace(tzinfo=None)  # 移除時區信息
            
            # 格式化數據
            weather_data = {
                'city': data['name'],
                'temperature': round(data['main']['temp'], 1),
                'feels_like': round(data['main']['feels_like'], 1),
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': round(data['wind']['speed'], 1),
                'last_update': weather_time.strftime('%Y-%m-%d %H:%M:%S')
            }
            return jsonify(weather_data)
        else:
            return jsonify({'error': f'無法獲取天氣資料：{data.get("message", "未知錯誤")}'})
            
    except Exception as e:
        return jsonify({'error': f'發生錯誤：{str(e)}'}), 500

@app.route('/api/latest')
def get_latest_weather():
    """獲取最新保存的天氣數據"""
    try:
        if os.path.exists(WEATHER_DATA_FILE):
            with open(WEATHER_DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return jsonify(data)
        else:
            return jsonify({'error': '沒有可用的天氣數據'})
    except Exception as e:
        return jsonify({'error': f'讀取數據時發生錯誤：{str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)