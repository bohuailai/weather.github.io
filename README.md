# 天氣查詢應用

這是一個使用 Python Flask 開發的天氣查詢網頁應用，整合了 OpenWeatherMap API 來獲取即時天氣數據，並使用 GitHub Actions 實現自動更新功能。

## 功能特點

- 全球城市天氣查詢（英文城市名）
- 顯示即時溫度和體感溫度
- 提供天氣狀況描述
- 顯示濕度資訊
- 顯示風速數據
- 自動每 10 分鐘更新台北天氣數據


## 系統要求

- Python 3.11 以上
- OpenWeatherMap API 密鑰
- Git

## 安裝步驟

1. 下載專案：
   ```bash
   git clone https://github.com/bohuailai/weather.github.io.git
   cd weather.github.io
   ```

2. 安裝套件：
   ```bash
   pip install -r requirements.txt
   ```

3. 設置環境變數：
   - 創建 `.env` 文件
   - 設置 API 密鑰：
     ```
     OPENWEATHER_API_KEY=你的OpenWeatherMap_API密鑰
     ```

4. 執行程式：
   ```bash
   python app.py
   ```

5. 開啟瀏覽器：
   ```
   http://localhost:5000
   ```

## GitHub Actions 自動更新

1. 在 GitHub 倉庫中設置 API 密鑰：
   - 進入倉庫的 Settings → Secrets and variables → Actions
   - 點擊 "New repository secret"
   - Name: `OPENWEATHER_API_KEY`
   - Value: 你的 OpenWeatherMap API 密鑰
   - 點擊 "Add secret"

2. 自動更新功能：
   - 系統會每 10 分鐘自動更新台北的天氣數據
   - 更新的數據保存在 `weather_data.json` 文件中

3. 手動觸發更新：
   - 進入 Actions 頁面
   - 選擇 "Update Weather Data" 工作流程
   - 點擊 "Run workflow"

## 使用說明

1. 顯示資訊包括：
   - 城市名稱
   - 當前溫度（°C）
   - 體感溫度（°C）
   - 天氣描述
   - 濕度（%）
   - 風速（m/s）
   - 數據更新時間

2. 自動更新數據：
   - `weather_data.json` 文件會自動更新
   - 可在 GitHub 倉庫中查看更新歷史
   - 每次更新都會創建新的提交記錄


## 注意事項

- 城市名稱必須使用英文
- API 有調用頻率限制
- 自動更新僅追蹤台北天氣

 
