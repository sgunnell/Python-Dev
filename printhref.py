import requests as req
from bs4 import BeautifulSoup

while True:
    input_url = input("Enter Starting URL: ")
    try:
        r = req.get(input_url)
        break
    except:
        print('Request failed re-enter email')
print(r.status_code)
print(r.headers['content-type'])
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.contents)
tags = soup('a')
url_list = list()
#print(tags)
for line in soup.find_all('a', href=True):

    
    if(line['href'].startswith('http')):
        print(line['href'])
    else:
        print(input_url+line['href'])
