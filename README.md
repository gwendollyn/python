```
mkdir python && cd python
```

1. Selenium 是一個功能強大的工具，廣泛應用於自動化測試與網頁抓取。它允許開發者編寫腳本來模擬 User 與 Web Browser 的互動。
- 這邊用的是 Apple M2 ARM64 架構
```
python3 -m venv .
python3 -m pip install selenium
source /Path/to/bin/activate
python3 -m pip install selenium
```
2. ChromeDriver 是 Selenium WebDriver 用來控制 Chrome 的獨立執行檔。
```
brew install chromedriver
which chromedriver
```
3. 自動化動作：呼叫 Selenium 打開瀏覽器、導至特定網址頁面、找到「線上報名」按鈕
```
vim course_register.py
python3.13 course_register.py
```
