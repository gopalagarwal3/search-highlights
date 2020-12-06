import streamlit as st
import streamlit.components.v1 as st_html

document_text = """The easiest way to learn how to use Streamlit is to try things out yourself"""

# display_text = search_text.replace(query, """<span style="background-color: #FFFF00">""" + query + "</span>")
# st.markdown(search_text) # not highlighting well :|

snippet_offsets = [{'start': 0, 'end': 25, 'keywords': [{'start': 10, 'end': 15}, {'start': 20, 'end': 23}]}, {'start': 35, 'end': 45, 'keywords': [{'start': 37, 'end': 44}]}]

hl_text_snippets = []

pos = 0
for snippet in snippet_offsets:
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

st_html.html(hl_text)