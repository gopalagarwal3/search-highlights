snippet_xml = """<offset start="0" end="58">Fundamental to <keyword start="15" end="18"/><b>the</b> internals of highlighting are detecting</offset>"""

import xml.etree.ElementTree as ET
root = ET.fromstring(snippet_xml)

print(root.get('start'))
print(root.get('end'))

keyword_offset_list = []
for keyword in root.findall('keyword'):
    keyword_offset = {'start': keyword.get('start'), 'end': keyword.get('end')}
    keyword_offset_list.append(keyword_offset)

print(keyword_offset_list)


