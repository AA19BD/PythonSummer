import xml.etree.ElementTree as ET

data ='''
    <person>
    <name>John</name>
    <phone type="intl">123</phone>
    <email hide="yes"/>
    </person>
'''

tree=ET.fromstring(data)#we are formatting the string into the tree
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))