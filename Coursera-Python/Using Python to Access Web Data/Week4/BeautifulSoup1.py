from bs4 import BeautifulSoup
import urllib.request,urllib.error,urllib.parse

url=input('Enter - ')
html=urllib.request.urlopen(url).read()#that will read() all file into string
soup= BeautifulSoup(html,'html.parser')

tags=soup('a')#retreive all anchor tags from the file into list
for tag in tags:#loop through all the list
    print(tag.get('href',None))#retreive all links in anchor tags or retreive nothiing