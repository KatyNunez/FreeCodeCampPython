import xml.etree.ElementTree as ET
data = '''<person> #This most of the time is imported from outside
<name>Katy</name>
<phone type="intl">
1+ 222 222 2222
</phone>
<email hide="yes"/>
</person>'''

tree=ET.fromstring(data)
print('Name',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))