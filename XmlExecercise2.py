import xml.etree.ElementTree as ET
input='''<stuff>
<users>
    <user x="2">
        <id>001</id>
        <name>Yoel</name>
    </user>

    <user x="7">
        <id>009</id>
        <name>Katy</name>
    </user>
</users>
</stuff>'''

stuff=ET.fromstring(input)
lst=stuff.findall('users/user')
print('User count: ' ,len(lst))
for item in lst:
    print('Name: ',item.find('name').text)
    print('ID',item.find('id').text)
    print('attribute:',item.get("x"))