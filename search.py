# -*- coding: utf-8 -*-
import os
import pprint
import elasticsearch


def search():
    # Elasticsearchのコンテナ名を指定（Docker Network）
    # client = elasticsearch.Elasticsearch("elasticsearch")
    client = elasticsearch.Elasticsearch("localhost:9200")
    pprint.pprint(client.info(), indent=2, width=1)

    print("")
    print("---------------------------------------------------")

    # index指定で検索
    result = client.search(
        index='python-blogs'
    )
    hits = result['hits']
    print('ヒット数 : %s' % hits['total'])

    for doc in hits['hits']:
        print('- ID : %s' % doc['_id'])
        print('  Title : %s' % doc['_source']['title'])

    print("")
    print("---------------------------------------------------")

    result = client.search(
        index='python-blogs',
        body={'query': {'match': {'genre': 1}}}
    )
    hits = result['hits']
    print('ヒット件数 : %s' % hits['total'])

    num = 1
    for doc in hits['hits']:
        print('%d. ID : %s' % (num, doc['_id']))
        print('   Title : %s' % doc['_source']['title'])
        num += 1


def main():
    search()


if __name__ == "__main__":
    main()
