import requests
from bs4 import BeautifulSoup
import datetime
import os

# 対象URL
URL = "https://www.etix.com/kketix/e/2009653"

# チェックする日（例：21日は21日）
TARGET_DATE = "21"

# Slack Webhook URL（GitHub Secrets から取得）
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

# Slack通知関数
def notify_slack(message):
    if SLACK_WEBHOOK_URL:
        requests.post(SLACK_WEBHOOK_URL, json={"text": message})
    else
