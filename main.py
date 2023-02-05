from lib import db
from lib import vtt
from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


class Url(BaseModel):
    url: str


app = FastAPI()


@app.post("/api/urls/", status_code=status.HTTP_200_OK)
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


@app.get("/api/urls/")
async def get_urls():
    return db.get_urls()


@app.get("/urls/register/", response_class=HTMLResponse)
async def register_url():
    with open("./www/html/register_url.html", "r") as f:
        return f.read()


@app.get("/urls/", response_class=HTMLResponse)
async def list_urls():
    with open("./www/html/list_urls.html", "r") as f:
        return f.read()
