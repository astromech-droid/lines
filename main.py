from lib import db
from lib import vtt
from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


class Url(BaseModel):
    url: str


app = FastAPI()


@app.post("/urls/", status_code=status.HTTP_200_OK)
async def post_url(url: Url, response: Response):
    if db.count_url(url.url) > 0:
        response.status_code = status.HTTP_409_CONFLICT
        return "This url is already exists."

    else:
        text = vtt.fetch(url.url)
        payload = vtt.extract_payload(text)
        joined_data = vtt.join_multilines(payload)
        db.bulk_data(joined_data)
        db.register_url(url.url)

        return "Succeed"


@app.get("/", response_class=HTMLResponse)
async def root():
    with open("./www/html/index.html", "r") as f:
        return f.read()
