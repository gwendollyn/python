import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 確保 chromedriver 在 PATH 裡
service = Service("/opt/homebrew/bin/chromedriver")  # 根據 `which chromedriver` 的結果調整

# 正確啟動 webdriver
driver = webdriver.Chrome(service=service)

driver.get("https://ojt.wda.gov.tw/ClassSearch/Detail?PlanType=1&OCID=162676")

# 等待報名開放（可用更準確的時間同步方式）
#while True:
#    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
#    if current_time >= "2025-04-04 12:00:00":
#        break
#    time.sleep(1)

# 找到「線上報名」按鈕
signup_button = driver.find_element(By.LINK_TEXT, "線上報名")  # 確保這是正確的定位方式
signup_button.click()

# 等待一下（視情況而定）
time.sleep(5)

# 這裡可以加上填表單、自動登入的步驟

# 完成後關閉瀏覽器
# driver.quit()

