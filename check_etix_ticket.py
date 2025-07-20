import os
import requests

WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]

def send_slack_notification(message):
    payload = {"text": message}
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        raise Exception(f"Request to Slack returned error {response.status_code}, response: {response.text}")

send_slack_notification("チェック完了：チケットの更新を確認しました。")
