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


def register_url(url: str):
    es.index(index="urls", body={"url": url})


def count_url(url: str) -> int:
    result = es.count(index="urls", body={"query": {"match": {"url": url}}})
    return result["count"]
