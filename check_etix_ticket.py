import os
import sys
import requests

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
if not WEBHOOK_URL:
    print("Error: SLACK_WEBHOOK_URL is not set.")
    sys.exit(1)

def send_slack_message(message):
    payload = {"text": message}
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        print(f"Slack notification failed: {response.text}")
        sys.exit(1)

# 例: 通知テスト
send_slack_message("✅ チェック完了！")
