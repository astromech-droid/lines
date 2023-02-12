import hashlib
import json
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
    # 生のurlだと長すぎてterm検索できないので、hash値も保管しておく
    # hash = hashlib.md5(url.encode()).hexdigest()
    # es.index(index="episodes", body={"url": url, "hash": hash})
    es.index(index="episodes", body=ep)


def count_episodes(url: str) -> int:
    # 生のurlだと長すぎてterm検索できないので、hash値を検索する
    hash = hashlib.md5(url.encode()).hexdigest()
    result = es.count(index="episodes", body={"query": {"term": {"hash": hash}}})
    return result["count"]


def get_episodes() -> dict:
    return es.search(index="episodes", body={"query": {"match_all": {}}})
