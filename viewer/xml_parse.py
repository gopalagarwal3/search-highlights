snippet_xml = """<offset start="127" end="294">As long as your <keyword start="143" end="146"/><em>app</em> is running, every time you add a new element to your script and save, Streamlit’s UI will ask if you’d like to rerun the <keyword start="268" end="271"/><em>app</em> and view the changes. </offset>"""

import xml.etree.ElementTree as ET
root = ET.fromstring(snippet_xml)

print(root.get('start'))
print(root.get('end'))

keyword_offset_list = []
for keyword in root.findall('keyword'):
    keyword_offset = {'start': keyword.get('start'), 'end': keyword.get('end')}
    keyword_offset_list.append(keyword_offset)

print(keyword_offset_list)


