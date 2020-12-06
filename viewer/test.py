document_text = """The <b>easiest</b> way to learn how to use Streamlit is to try things out yourself"""

# display_text = search_text.replace(query, """<span style="background-color: #FFFF00">""" + query + "</span>")
# st.markdown(search_text) # not highlighting well :|

snippet_offsets = [{'start': 0, 'end': 20}, {'start': 30, 'end': 32}]

hl_text_snippets = []

pos = 0
for snippet in snippet_offsets:
    hl_text_snippets.append(document_text[pos:snippet['start']])
    hl_text_snippets.append("""<span style="background-color: #FFFF00">""")
    hl_text_snippets.append(document_text[snippet['start']:snippet['end']])
    hl_text_snippets.append("</span>")
    pos = snippet['end']
hl_text_snippets.append(document_text[pos:])

hl_text = ''.join(hl_text_snippets)

print(hl_text)