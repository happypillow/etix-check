import requests
from bs4 import BeautifulSoup
import datetime
import os
import sys

# 対象URL
URL = "https://www.etix.com/kketix/e/2009653"

# チェックする日（例：21日は"21"）
TARGET_DATE = "21"

# Slack Webhook URL（GitHub Secrets から取得）
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

# Slack通知関数
def notify_slack(message):
    if SLACK_WEBHOOK_URL:
        response = requests.post(SLACK_WEBHOOK_URL, json={"text": message})
        if response.status_code != 200:
            print(f"Slack通知失敗: {response.status_code} - {response.text}")
    else:
        print("Error: SLACK_WEBHOOK_URL is not set.")
        sys.exit(1)

# ページを取得して席の情報をチェック
def check_etix_ticket():
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.RequestException as e:
        notify_slack(f"ページ取得エラー: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # 日付のブロックをすべて取得
    day_blocks = soup.find_all("div", class_="ticket-date-time-wrapper")

    found = False
    for block in day_blocks:
        if TARGET_DATE in block.get_text():
            if "Sold Out" not in block.get_text():
                # 空席がある
                notify_slack(f"🎫 {TARGET_DATE}日に空席があります！\n{URL}")
                found = True
                break

    if not found:
        print(f"{TARGET_DATE}日は空席なしまたは見つかりませんでした。")

# 実行
if __name__ == "__main__":
    check_etix_ticket()
