import xml.etree.ElementTree as ET
import ssl
import urllib.request,urllib.error,urllib.parse

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


address = input('Enter location: ')
fhand = urllib.request.urlopen(address, context=ctx).read()

print('Retrieving',address)
print('Retrieved', len(fhand ),'characters')

fhand.decode()
tree = ET.fromstring(fhand)
counts1 = tree.findall('.//count')
counts2 = tree.findall('comments/comment')
print('Count:',len(counts1))
sum=0
for item in counts2:
    sum+=int((item.find('count').text))     
print("Sum:",sum)

    