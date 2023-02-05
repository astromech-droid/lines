import re
import requests


# インターネットから字幕テキスト(str)を取得する
def fetch(url: str) -> str:
    res = requests.get(url)

    if re.match(r"^WEBVTT", res.text):
        return res.text

    else:
        # WebVTT以外のデータは返さない
        return None


# テキスト(str)をファイルに保存する
def save(text: str, path: str) -> bool:
    try:
        with open(path, "w") as f:
            f.write(text)
        return True

    except Exception:
        return False


# インターネットから字幕テキストをダウンロードする
def download(url: str, path: str) -> bool:
    text = fetch(url)
    return save(text, path)
