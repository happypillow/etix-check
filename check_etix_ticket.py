import os
import requests

webhook_url = os.environ["SLACK_WEBHOOK_URL_NEW"]

def notify_slack(message):
    payload = {"text": message}
    requests.post(webhook_url, json=payload)
