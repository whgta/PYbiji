from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content,'lxml')

#bs自动转码
content = soup.prettify()

print("==" * 12)

print(soup.head)
print("==" * 12)
print(soup.meta)
print("==" * 12)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])
soup.link.attrs['type'] = 'hahaha'
print(soup.link)
print("==" * 12)
print(soup.title.name)
print(soup.title.atrrs)
print(soup.title.string)
print("==" * 12)
print(soup.name)
print(soup.attrs)

print('**'*20)
print(soup.name)
print("==" * 12)
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
print("==" * 12)