import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url = input('Enter URL: ')
count=int(input("Enter count: "))
link_line = int(input("Enter position: "))
html= urllib.request.urlopen(url, context=ctx).read()
soup= BeautifulSoup(html, 'html.parser')

while count >= 0:
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   tags = soup('a')
   print(url)
   url = tags[link_line-1].get("href", None)
   count = count - 1