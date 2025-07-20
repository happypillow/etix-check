import requests

# IFTTT Webhook URL（あなたのキーに書き換えてください）
IFTTT_URL = 'https://maker.ifttt.com/trigger/etix_ticket_available/with/key/XXXXXXXXXXXX'

# チェック対象のURL
URL = "https://www.etix.com/kketix/e/2009653?&cobrand=playec&country=JP&language=ja"

def check_ticket():
    response = requests.get(URL)
    html = response.text

    # 7月21日（日）10:00 に「空き」が出たか確認（例：残数ありの表記）
    if "7月21日" in html and "10:00" in html and "残数" in html and "0 現在の残数" not in html:
        print("空きが出ました！通知送信中...")
        requests.post(IFTTT_URL)
    else:
        print("空きなし")

if __name__ == "__main__":
    check_ticket()
