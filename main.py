import requests
from bs4 import BeautifulSoup
import os

# 対象URL（変更不要）
URL = "https://www.etix.com/kketix/e/2009653"

# チェックする日（例：22日）
target_date_str = "22日"

# Slack Webhook URL（GitHub Actions の Secrets から取得）
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

# Slack通知関数
def notify_slack(message):
    if SLACK_WEBHOOK_URL:
        requests.post(SLACK_WEBHOOK_URL, json={"text": message})

#
