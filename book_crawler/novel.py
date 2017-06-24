import requests
from bs4 import BeautifulSoup
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
response = requests.get("http://www.booktxt.net")
# print (response.text.encode(response.encoding).decode('utf-8'))
print response.encoding
# print response.content
response.encoding = 'GB2312'
soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')

print soup.title

