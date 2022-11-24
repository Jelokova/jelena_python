import requests
from requests.exceptions import HTTPError

#200-sucsess
#300-redirect
#400-client error
#500-server error

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
r = requests.get('https://xkcd.com/353/', timeout=10, headers=headers)
#print(r.text)
#print(r.content)
import antigravity
# image=requests.get('https://imgs.xkcd.com/comics/python.png')
# with open('python.jpg','wb')as file:
#     file.write(image.content)
print(r.ok)
print(r.headers)
print(r.cookies)
print(r.encoding)
print(r.headers['server'])

for url in ['https://api.github.com','https://api.github.com/invalid']:
    try:
        response=requests.get(url)
        response.raise_for_status()
        x=10/0
    except HTTPError as http_err:
        print(f'HTTP error:{http_err}')
    except Exception as err:
        print(f'Other error:{err}')
    else:
        print('Success')