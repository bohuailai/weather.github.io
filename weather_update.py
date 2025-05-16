import os
import json
import sys
import requests
from datetime import datetime

print("Python 腳本開始執行...")

# 檢查 API 密鑰
api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    print("錯誤：無法獲取 API 密鑰")
    sys.exit(1)

print(f"API 密鑰已設置（長度：{len(api_key)}）")

try:
    print("嘗試獲取台北天氣...")
    
    # 直接使用 OpenWeatherMap API
    params = {
        "q": "Taipei",
        "appid": api_key,
        "units": "metric",
        "lang": "zh_tw"
    }
    response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params)
    data = response.json()
    
    if response.status_code == 200:
        # 添加更新時間
        data["updatedAt"] = datetime.now().isoformat()
        
        print("天氣數據獲取成功：")
        print(json.dumps(data, indent=2, ensure_ascii=False))
        
        print("正在保存數據到文件...")
        with open("weather_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("數據保存成功")
    else:
        print(f"錯誤：API 請求失敗（狀態碼：{response.status_code}）")
        print(f"錯誤訊息：{data.get('message', '未知錯誤')}")
        sys.exit(1)
            
except Exception as e:
    print(f"錯誤詳情：{str(e)}")
    print(f"錯誤類型：{type(e).__name__}")
    import traceback
    print("完整錯誤追蹤：")
    print(traceback.format_exc())
    sys.exit(1) 