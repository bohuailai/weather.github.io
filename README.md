# 天氣查詢應用

這是一個使用 Python Flask 開發的天氣查詢網頁應用，整合了 OpenWeatherMap API 來獲取即時天氣數據，並使用 GitHub Actions 實現自動更新功能。

## 功能特點

- 🌍 支持全球城市天氣查詢（使用英文城市名）
- 🌡️ 顯示即時溫度和體感溫度
- 🌤️ 提供天氣狀況描述
- 💧 顯示濕度資訊
- 🌪️ 顯示風速數據
- 🕒 自動每 5 分鐘更新台北天氣數據
- 📱 響應式設計，支援各種設備

## 系統要求

- Python 3.11 或更高版本
- OpenWeatherMap API 密鑰
- Git

## 安裝步驟

1. 下載專案：
   ```bash
   git clone https://github.com/[你的GitHub用戶名]/weather.git
   cd weather
   ```

2. 安裝套件：
   ```bash
   pip install -r requirements.txt
   ```

3. 設置環境變數：
   - 創建 `.env` 文件
   - 添加你的 API 密鑰：
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

## GitHub Actions 自動更新設置

1. 在 GitHub 倉庫中設置 API 密鑰：
   - 進入倉庫的 Settings → Secrets and variables → Actions
   - 點擊 "New repository secret"
   - Name: `OPENWEATHER_API_KEY`
   - Value: 你的 OpenWeatherMap API 密鑰
   - 點擊 "Add secret"

2. 自動更新功能：
   - 系統會每 5 分鐘自動更新台北的天氣數據
   - 更新的數據保存在 `weather_data.json` 文件中
   - 可在 Actions 頁面查看更新記錄

3. 手動觸發更新：
   - 進入 Actions 頁面
   - 選擇 "Update Weather Data" 工作流程
   - 點擊 "Run workflow"

## 使用說明

1. 查詢天氣：
   - 在搜索框輸入城市英文名稱（如：Taipei, Tokyo, London）
   - 點擊查詢按鈕或按 Enter 鍵
   - 系統會顯示該城市的即時天氣資訊

2. 顯示資訊包括：
   - 城市名稱
   - 當前溫度（°C）
   - 體感溫度（°C）
   - 天氣描述
   - 濕度（%）
   - 風速（m/s）
   - 數據更新時間

3. 自動更新數據：
   - `weather_data.json` 文件會自動更新
   - 可在 GitHub 倉庫中查看更新歷史
   - 每次更新都會創建新的提交記錄

## 故障排除

1. API 錯誤：
   - 確認 API 密鑰正確設置
   - 檢查城市名稱拼寫（必須使用英文）
   - 查看 Actions 執行日誌

2. 本地運行問題：
   - 確認 Python 版本正確
   - 檢查是否已安裝所有必要的程式套件
   - 確認 .env 文件設置正確

3. GitHub Actions 問題：
   - 檢查倉庫的 Actions 權限設置
   - 確認 Secrets 正確配置
   - 查看工作流程執行日誌

## 注意事項

- 城市名稱必須使用英文
- API 有調用頻率限制
- 自動更新僅追蹤台北天氣
- 建議定期檢查 API 密鑰有效性

## 技術架構

- 後端：Python Flask
- 前端：HTML5, CSS3（純靜態頁面）
- API：OpenWeatherMap
- 自動化：GitHub Actions
- 數據存儲：JSON

## 授權

本專案採用 MIT 授權條款。詳見 [LICENSE](LICENSE) 文件。

## 貢獻指南

歡迎提交 Issue 和 Pull Request 來改進這個專案。

## 更新記錄

### v1.0.0 (2024-03-21)
- 初始版本發布
- 基本天氣查詢功能
- GitHub Actions 自動更新集成 
