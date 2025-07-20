import requests
from bs4 import BeautifulSoup
import os

# Slack Webhook URL（GitHub Secretsから読み込み）
WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL_NEW"]

# チェック対象URL
TARGET_URL = "https://www.etix.com/kketix/e/2009653?&cobrand=playec&country=JP&language=ja"

def notify_slack(message):
    payload = {"text": message}
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        print(f"Slack通知エラー: {response.text}")

def check_availability():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(TARGET_URL, headers=headers)

    if response.status_code != 200:
        notify_slack(f"ページ取得に失敗しました（{response.status_code}）")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # キーワードに合わせて調整
    if "チケットを選択" in soup.text or "Select Tickets" in soup.text:
        notify_slack(f"チケットが購入可能になった可能性があります。\n{TARGET_URL}")
    else:
        print("現在空席はありません。")

if __name__ == "__main__":
    check_availability()
