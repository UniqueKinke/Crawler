import urllib2

def download(url):
    return urllib2.urlopen(url).read()

# print download('http://uniqueq.cn')
print download('http://baidu.com')

