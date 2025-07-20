# etix-check

Etix（エティックス）で指定日時（2025/7/21 10:00）のチケット空き状況をチェックして、IFTTT経由でLINE通知します。

## 使い方

1. `check.py` の `IFTTT_URL` を自分のWebhook URLに書き換える
2. Render でこのリポジトリをデプロイ（start command: `python check.py`）
