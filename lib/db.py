from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

username = "elastic"
password = "aeVIUEp4_aPlkRxxUfA9"
es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=(username, password),
)


def gen_bulk_data(docs):
    for doc in docs:
        doc = doc | {"_index": "lines"}
        yield doc


def bulk_data(docs):
    bulk(es, gen_bulk_data(docs))
