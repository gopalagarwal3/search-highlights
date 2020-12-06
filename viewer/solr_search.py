import pysolr
from typing import List


def search_solr(search_query, search_text) -> List[str]:
    """search solr"""
    solr_con = pysolr.Solr("http://localhost:8983/solr/techproducts/", timeout=10, always_commit=True)

    # Do a health check.
    solr_con.ping()

    solr_con.add([
        {
            "id": "doc_1",
            "content_light_tv": search_text
        }
        # ,{
        #     "id": "doc_2",
        #     "content": "The Banana: Tasty or Dangerous?"
        # },
    ])
    # solr_query = "content_light_tv:" + search_query
    results = solr_con.search(search_query, **{
        'hl': 'on',
        # 'hl.fragsize': 10,
        'hl.snippets': 1000,
        'fq': 'id:doc_1',
        'qf': 'content_light_tv',
        'defType': 'edismax',
        'hl.tag.pre': '<b>',
        'hl.tag.post': '</b>'
    })

    snippets = []
    for result in results:
        snippets.extend(results.highlighting[result['id']]['content_light_tv'])
    # for field_snippet in results.highlighting[result['id']]['content_light_tv']:

    return snippets
