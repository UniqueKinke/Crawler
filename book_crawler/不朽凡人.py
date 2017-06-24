import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.booktxt.net/2_2270'

url2 = '/2283859.html'

def getContent(soup):
    print soup.title.string
    for link in soup.find_all('div'):
        text = link.get('id')
        if text == 'content':
            print link.text

def getText(url):
    response = requests.get(url)
    # print requests.utils.get_encodings_from_content(response.text)
    response.encoding = 'gbk'

    # print response.text

    soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')

    # print soup.getText

    # print tag['href']

    # print soup.text

    # for link in soup.find_all('a'):
    #     # if link.get('href').match(re.compile(text)):
    #     print link.string
    #     print link.get('href')
    getContent(soup)


# getText(url)
getText(url + url2)
