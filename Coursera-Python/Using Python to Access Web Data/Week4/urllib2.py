import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter - ')
html=urllib.request.urlopen(url,context=ctx).read()
soap= BeautifulSoup(html,'html.parser')

count=0
sum=0
tags=soap('span')
for tag in tags:
    new_tag=int(tag.contents[0])
    # count+=1
    sum+=new_tag
print(sum)
    
