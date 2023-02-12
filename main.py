from lib import db
from lib import vtt
from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


class Episode(BaseModel):
    url: str


app = FastAPI()


@app.post("/api/episodes/", status_code=status.HTTP_200_OK)
async def post_episode(ep: Episode, response: Response):
    if db.count_episodes(ep.url) > 0:
        response.status_code = status.HTTP_409_CONFLICT
        return "This url is already exists."

    else:
        text = vtt.fetch(ep.url)
        payload = vtt.extract_payload(text)
        joined_data = vtt.join_multilines(payload)
        db.bulk_data(joined_data)
        db.register_episode(ep.url)

        return "Succeed"


@app.get("/api/episodes/")
async def get_episodes():
    return db.get_episodes()


@app.get("/episodes/register/", response_class=HTMLResponse)
async def register_episode():
    with open("./www/html/register_episode.html", "r") as f:
        return f.read()


@app.get("/episodes/", response_class=HTMLResponse)
async def list_episodes():
    with open("./www/html/list_episodes.html", "r") as f:
        return f.read()


@app.get("/", response_class=HTMLResponse)
async def root():
    with open("./www/html/index.html", "r") as f:
        return f.read()


@app.get("/lines/search", response_class=HTMLResponse)
async def search_lines():
    with open("./www/html/search_lines.html", "r") as f:
        return f.read()
