from conf import settings
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch(
    hosts=[settings.ES_HOST],
    basic_auth=(settings.ES_USERNAME, settings.ES_PASSWORD),
)


def gen_bulk_data(docs):
    for doc in docs:
        doc = doc | {"_index": "lines"}
        yield doc


def bulk_data(docs):
    bulk(es, gen_bulk_data(docs))


def register_episode(ep: dict):
    id = ep.pop("id")
    return es.index(index="episodes", id=id, body=ep)


def get_episodes() -> dict:
    return es.search(index="episodes", body={"query": {"match_all": {}}})
