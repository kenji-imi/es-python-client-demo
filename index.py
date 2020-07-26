# -*- coding: utf-8 -*-
import multiprocessing
import os
import pprint
import elasticsearch
from elasticsearch import helpers

# 接続先のElastisearchを指定
# 今回はElasticsearchのコンテナ名を指定、ローカルで起動しているElasticsearchであればlocalhost:9200
# client = elasticsearch.Elasticsearch("elasticsearch")
client = elasticsearch.Elasticsearch("localhost:9200")
pprint.pprint(client.info(), indent=2, width=1)

print("")
print("---------------------------------------------------")


def index(index_name, doc):
    # indexを指定して登録を行う
    client.index(index=index_name, doc_type='_doc', body=doc)
    print("indexed")


def delete_index(index_name):
    try:
        ret = client.indices.exists(index=index_name)
        if ret == True:
            client.indices.delete(index_name)
            print("deleted")
    except Exception as e:
        print(e)

    print("")
    print("---------------------------------------------------")


def delete_doc(index_name, doc_id):
    client.delete(index=index_name, doc_type='_doc', id=doc_id)


def delete_docs_by_query(index_name, body):
    # ex. body = {'query': {'match': {'title': 'apple'}}}
    client.delete_by_query(index=index_name, body=body)


def delete_all_docs(index_name):
    body = {"query": {"match_all": {}}}
    delete_docs_by_query(index_name, body)


def create_blog_mapping(index_name):
    mapping = {
        "mappings": {
            "_doc": {
                "properties": {
                    "title": {"type": "text"},
                    "content": {"type": "text"},
                    "genre": {"type": "integer"},
                    "publish_date": {"type": "text"},
                }
            }
        }
    }
    client = elasticsearch.Elasticsearch("localhost:9200")
    client.indices.create(index=index_name, body=mapping)


def create_blog_doc():
    blog = {}
    blog['title'] = 'funny blog'
    blog['content'] = 'memo'
    blog['genre'] = 1
    blog['publish_date'] = '2020/07/20'
    return blog


def main():
    index_name = "python-blogs"
    doc = create_blog_doc()

    index(index_name, doc)


if __name__ == "__main__":
    main()
