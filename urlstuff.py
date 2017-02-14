# urllib usage

import urllib.request

url = 'https://ya.ru'
x = urllib.request.urlopen(url)
# print(x.read())         #looks like source code

# POST request
import urllib.parse

# url = 'https://pythonprogramming.net/search'
# values = {'q': 'basic'}  # search for keyword basic
#
# data = urllib.parse.urlencode(values)       # convert values to urlstyle
# data = data.encode('utf-8')                 # encode 2 utf8
# req = urllib.request.Request(url, data)     # forming request
# resp = urllib.request.urlopen(req)          # making req
# respdata = resp.read()
# print(respdata)


# BUT what if site dont wanna us to be hacking around?
# google requires API for using their search/ lets see

try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    # fails as HTTP ERROR 403: FORBIDDEN
    # as expected
    print(x.read())

except Exception as e:
    print(e)

try:
    url = 'https://google.com/search?q=test'
    headers = {}
    headers[
        'User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respdata = resp.read()
    with open('testing.txt','w') as f:
        f.write(str(respdata))

except Exception as e:
    print(e)
