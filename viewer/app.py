import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as st_html
import time
import solr_search
import es_search
from typing import List
import xml.etree.ElementTree as ET

# Text to be searched on
document_text = """The easiest way to learn how to use Streamlit is to try things out yourself. As you read through this guide, test each method. As long as your app is running, every time you add a new element to your script and save, Streamlit’s UI will ask if you’d like to rerun the app and view the changes. This allows you to work in a fast interactive loop: you write some code, save it, review the output, write some more, and so on, until you’re happy with the results. The goal is to use Streamlit to create an interactive app for your data or model and along the way to use Streamlit to review, debug, perfect, and share your code."""
st.write("Search Text:", document_text)

query = st.text_input("Search Query", "app")


def get_snippet_offsets(search_snippets):
    snippet_offset_list = []

    for sp in search_snippets:
        snippet_offset = {}
        root = ET.fromstring(sp)
        snippet_offset['start'] = int(root.get('start'))
        snippet_offset['end'] = int(root.get('end'))

        keyword_offset_list = []
        for keyword in root.findall('keyword'):
            keyword_offset = {'start': int(keyword.get('start')), 'end': int(keyword.get('end'))}
            keyword_offset_list.append(keyword_offset)

        snippet_offset['keywords'] = keyword_offset_list

        snippet_offset_list.append(snippet_offset)

    return snippet_offset_list


def get_highlighted_text(_snippet_offset_list):
    hl_text_snippets = []

    # highlight snippets and keywords
    pos = 0
    for snippet in _snippet_offset_list:
        hl_text_snippets.append(document_text[pos:snippet['start']])
        hl_text_snippets.append("""<span style="background-color: #FFFF00">""")

        # highlight keywords
        pos_keyword = snippet['start']
        for keyword in snippet['keywords']:
            hl_text_snippets.append(document_text[pos_keyword:keyword['start']])
            hl_text_snippets.append("<b>")
            hl_text_snippets.append(document_text[keyword['start']:keyword['end']])
            hl_text_snippets.append("</b>")
            pos_keyword = keyword['end']
        hl_text_snippets.append(document_text[pos_keyword:snippet['end']])

        hl_text_snippets.append("</span>")
        pos = snippet['end']

    hl_text_snippets.append(document_text[pos:])

    hl_text = ''.join(hl_text_snippets)
    return hl_text


result_snippets = []
search_engine = st.radio("Which search engine?", ('SOLR', 'ES'))
if search_engine == "SOLR":
    result_snippets = solr_search.search_solr(query, document_text)
elif search_engine == "ES":
    result_snippets = es_search.search_es(query, document_text)
else:
    print("Not cool!")

snippet_offsets = get_snippet_offsets(result_snippets)
highlighted_text = get_highlighted_text(snippet_offsets)

st_html.html(highlighted_text)
