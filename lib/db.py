from conf import settings
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch(
    hosts=[settings.ES_HOST],
    basic_auth=(settings.ES_USERNAME, settings.ES_PASSWORD),
)


def gen_bulk_data(ep_id, docs):
    for doc in docs:
        doc = doc | {"_index": "lines", "ep_id": ep_id}
        yield doc


def bulk_lines(ep_id: str, docs: list):
    bulk(es, gen_bulk_data(ep_id, docs))


def register_episode(ep: dict):
    id = ep.pop("id")
    return es.index(index="episodes", id=id, body=ep)


def get_episodes() -> dict:
    return es.search(index="episodes", body={"query": {"match_all": {}}})
