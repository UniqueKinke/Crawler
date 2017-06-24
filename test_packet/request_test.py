# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
import requests
from bs4 import BeautifulSoup

response = requests.get("http://uniqueq.cn/")
# response = requests.get("https://foofish.net")

# print response.status_code  #200
# print response.reason

# for name,value in response.headers.items():
#     print("%s:%s" % (name, value))

# print response.content

# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# r = requests.put('http://httpbin.org/put', data = {'key':'value'})
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')

soup = BeautifulSoup(response.text, 'html.parser')

# print soup.prettify()

print soup.title
print soup.title.name
print soup.title.string
print '-------- -------- --------'
print soup.a
# print soup.a.href
print soup.a.name
print soup.a.string
print '-------- -------- --------'

for link in soup.find_all('a'):
    print link.get('href')
print '-------- -------- --------'

print soup.getText()

tag = soup.a
print type(tag)
print tag.name
print '===-------- -------- --------'
print tag.attrs
print tag['href']
print tag.get('href')
print '-------- -------- --------'
# print tag.get('href')

print tag.string
print soup.name
print soup.head.title.string


for children in soup.children:
    print children
    print '------'

print '-------- -------- --------'




















