import os
import requests

def notify_slack(message: str):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("Slack Webhook URLが環境変数に設定されていません")
        return

    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)

    print(f"Slack送信ステータス: {response.status_code}")
    if response.status_code != 200:
        print(f"レスポンス内容: {response.text}")

# テスト送信メッセージ
notify_slack("✅ GitHub Actions からの Slack 通知テストです！")
