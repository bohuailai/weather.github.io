import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
import pytz  # 添加 pytz 模組

# 載入環境變數
load_dotenv()

def fetch_weather():
    """獲取台北市天氣數據"""
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        raise ValueError("未設置 OPENWEATHER_API_KEY 環境變數")

    # 台北市的座標
    lat = "25.0478"
    lon = "121.5319"
    
    # API 請求 URL
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=zh_tw"
    
    try:
        # 發送請求
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        
        # 設定台北時區
        taipei_tz = pytz.timezone('Asia/Taipei')
        current_time = datetime.now(taipei_tz)
        
        # 格式化數據
        formatted_data = {
            'city': weather_data['name'],
            'temperature': round(weather_data['main']['temp'], 1),
            'feels_like': round(weather_data['main']['feels_like'], 1),
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': round(weather_data['wind']['speed'], 1),
            'last_update': current_time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # 保存到文件
        with open('weather_data.json', 'w', encoding='utf-8') as f:
            json.dump(formatted_data, f, ensure_ascii=False, indent=2)
            
        print("天氣數據更新成功！")
        
    except Exception as e:
        print(f"更新天氣數據時發生錯誤：{e}")
        raise

if __name__ == "__main__":
    fetch_weather() 
