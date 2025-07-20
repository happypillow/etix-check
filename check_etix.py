import requests
from bs4 import BeautifulSoup
import os

# EtixのURL（対象ページ）
URL = "https://www.etix.com/ticket/e/2009653"

# チェックしたいキーワード（出現で空きと判定）
KEYWORDS = ["選択可", "選択可能"]

# LINE Notifyトークン（GitHub Secretsから読み込む）
LINE_TOKEN = os.getenv("LINE_NOTIFY_TOKEN")

def send_line_notify(message):
    if not LINE_TOKEN:
        print("LINE_TOKEN が未設定です。")
        return
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"message": message}
    requests.post(url, headers=headers, data=data)

def check_etix_page():
    res = requests.get(URL)
    if res.status_code != 200:
        print("ページ取得失敗")
        return

    soup = BeautifulSoup(res.text, "html.parser")
    text = soup.get_text()

    if any(keyword in text for keyword in KEYWORDS):
        send_line_notify("🎉 Etixに空きが出たかも！\n👉 " + URL)
    else:
        print("空きなし")

if __name__ == "__main__":
    check_etix_page()
