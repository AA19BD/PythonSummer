import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location=input('Enter location: ')
url=urllib.request.urlopen(location, context=ctx)
print('Retrieving ',location)
data=url.read().decode()
print('Retrieved ',len(data),'characters')

js= json.loads(data)
sum=0
count=0
for item in js['comments']:
    count+=1
    sum+=item['count']
print('Count:',count)
print('Sum:',sum)
