import json

with open("conf/settings.json", "r") as f:
    settings = json.loads(f.read())

ES_USERNAME = settings["es"]["auth"]["username"]
ES_PASSWORD = settings["es"]["auth"]["password"]
ES_HOST = settings["es"]["host"]
