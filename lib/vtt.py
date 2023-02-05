import re
import webvtt
import requests
from io import StringIO


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


# 時刻とセリフだけをテキストから抽出する
def extract_payload(text: str) -> list:
    payload = []
    buffer = StringIO(text)

    for cap in webvtt.read_buffer(buffer):
        payload.append({"start": cap.start, "end": cap.end, "text": cap.text})

    return payload


# 複数行にまたがるセリフを1行にjoinする
def join_multilines(payload: str) -> list:
    queue = []
    joined_data = []

    for cap in payload:
        queue.append(cap)

        # 行末の文字を見てセリフが終わっているか判別
        if re.match(r".*(\.|\!|\?)$", queue[-1]["text"]):
            # セリフが終わった場合 -> queueの中身をjoinして保存
            text_buffer = ""
            for q in queue:
                text_buffer = f'{text_buffer} {q["text"]}'

            joined_data.append(
                {
                    "start": queue[0]["start"],
                    "end": queue[-1]["end"],
                    "text": text_buffer,
                }
            )

            queue.clear()

        else:
            # セリフが終わっていない場合 -> 何もしない
            pass

    return joined_data
