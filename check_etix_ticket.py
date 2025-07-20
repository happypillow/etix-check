import os
import requests

WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]  # ←ここを修正！

def send_slack_message(message: str):
    payload = {
        "text": message
    }
    response = requests.post(WEBHOOK_URL, json=payload)
    response.raise_for_status()

send_slack_message("チケットを確認しました。")
