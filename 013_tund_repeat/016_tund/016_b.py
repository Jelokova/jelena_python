import requests
from bs4 import BeautifulSoup as BS

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
r = requests.get('https://xkcd.com/353/', timeout=10, headers=headers)
url='http://gammatest.net/course/python'
full_page=requests.get(url)
#print (full_page.ok)
soup=BS(full_page.content,'html.parser')
print(soup.title.name)
print(soup.title.parent )
print(soup.div['class'])

match=soup.find('div')