import requests as req
from bs4 import BeautifulSoup

Where True:
    input_url = input("Enter Starting URL")
    try:
        r = req.get(input_url)
        break
    except:
        print('Request failed re-enter email')
print(r.status_code)
print(r.headers['content-type'])
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.contents)
tags = soup('span-3 print-span-3 align-left margin-bottom-medium row-end')
url_list = list()
for line in soup.children:
    #print(tag)
    #url = tag.get('href',None)
    print(line)
    if str(line).startswith('strong'):
        print(line)
    '''
    if str(url).startswith('ADet'):
        url_list.append(url)
        print(url)

        print(tag.get('title',None))
'''
