import requests
from bs4 import BeautifulSoup
import datetime

# 対象URL
URL = "https://www.etix.com/kketix/e/2009653"

# チェックする日（2025年7月21日）
TARGET_DATE = "21"

# Slack Webhook URL（自分のURLに置き換えてください）
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/"

# Slack通知関数
def notify_slack(message):
    requests.post(SLACK_WEBHOOK_URL, json={"text": message})

# 空席チェック
def check_availability():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    target_cells = soup.find_all("td")
    for cell in target_cells:
        if cell.text.strip() == TARGET_DATE:
            if "選択可" in cell.get("class", []) or "available" in cell.g
