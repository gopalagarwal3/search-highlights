from datetime import datetime
from elasticsearch import Elasticsearch
from typing import List
import json

document_text = """The easiest way to learn how to use Streamlit is to try things out yourself. As you read through this guide, test each method. As long as your app is running, every time you add a new element to your script and save, Streamlit’s UI will ask if you’d like to rerun the app and view the changes. This allows you to work in a fast interactive loop: you write some code, save it, review the output, write some more, and so on, until you’re happy with the results. The goal is to use Streamlit to create an interactive app for your data or model and along the way to use Streamlit to review, debug, perfect, and share your code."""
es = Elasticsearch()


def search_es(search_query, search_text) -> List[str]:
    doc = {
        'id': '2',
        'content': search_text
    }
    res = es.index(index="test-offset", id=2, body=doc)
    print(res['result'])
    es.indices.refresh(index="test-offset")

    es_query = """{
                  "query": {
                    "query_string": {
                        "query": "%s"
                    }
                  },
                  "highlight": {
                    "fields": {
                      "content": {
                        "type": "offset"
                      }
                    },
                    "fragment_size": 50
                  }
                }""" % (search_query)

    res = es.search(index="test-offset", body=json.loads(es_query))
    print("Got %d Hits:" % res['hits']['total']['value'])

    snippets = []
    for hit in res['hits']['hits']:
        for snippet in hit["highlight"]["content"]:
            snippets.append(snippet)

    return snippets


print(search_es('the', document_text))
