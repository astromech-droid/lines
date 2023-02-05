from lib import db
from lib import vtt
from fastapi import FastAPI
from pydantic import BaseModel


class Url(BaseModel):
    url: str


app = FastAPI()


@app.post("/url/")
async def pass_url(url: Url):
    text = vtt.fetch(url.url)
    payload = vtt.extract_payload(text)
    joined_data = vtt.join_multilines(payload)
    db.bulk_data(joined_data)

    return url
