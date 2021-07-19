import xml.etree.ElementTree as ET
input='''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
             <user x="7">
                <id>002</id>
                <name>Bob</name>
            </user>
        </users>
    </stuff>
'''
tree= ET.fromstring(input)#we are formatting the string into the tree
lst=tree.findall('users/user')#there are list of trees(tags) inside ->[ ,  ]
print('User count:',len(lst))
for item in lst:
    print('User name:',(item.find('name').text))
    print('User id:',item.find('id').text)
    print('User attr:',item.get('x'))