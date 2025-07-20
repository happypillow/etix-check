import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# チェック対象URL（22日10時など）
URL = "https://www.etix.com/kketix/online/performanceReserve.jsp?performance_id=6017828&language_cache=ja"
TARGET_TIME = "10:00"

# Slack通知関数
def notify_to_slack(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("SLACK_WEBHOOK_URL が設定されていません")
        return
    payload = {"text": message}
    requests.post(webhook_url, json=payload)

# Chrome設定
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# ドライバ起動
driver = webdriver.Chrome(options=options)
driver.get(URL)
time.sleep(2)  # JS読み込み待ち

try:
    # プルダウン展開
    dropdown = driver.find_element(By.CSS_SELECTOR, "select")
    options = dropdown.find_elements(By.TAG_NAME, "option")

    for option in options:
        text = option.text.strip()
        if TARGET_TIME in text and "現在の残数です" not in text:
            notify_to_slack(f"✅【空きあり】{TARGET_TIME} の予約が可能になりました！\n{URL}")
            print("空きあり！通知しました。")
            break
    else:
        print("まだ空いていません。")

except Exception as e:
    notify_to_slack(f"❌ エラーが発生しました: {str(e)}")
    print(f"エラー: {str(e)}")

driver.quit()
