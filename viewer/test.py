import json
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
            }"""%('dasdass')

print(es_query)
print(json.loads(es_query))