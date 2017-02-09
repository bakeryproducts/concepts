import requests
from bs4 import BeautifulSoup
import operator


def getter(url):
    news = []
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    for link in soup.findAll('a', {'class': 'item-description-title-link'}):
        headline = link.string.lower().split()
        for word in headline:
            news.append(word)

    return clean_up(news)


def clean_up(data):
    clean_data = []
    list = '!@#$%^&*()_-=+~?><":\'\"/|'
    for word in data:
        for i in range(len(list)):
            word = word.replace(list[i], '')
        if len(word) > 0:
            clean_data.append(word)
    return clean_data


def counter(data):
    dic = {}
    for word in data:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic


url = 'https://www.avito.ru/moskva'
counted = counter(getter(url))
for key, value in sorted(counted.items(), key=operator.itemgetter(1)):
    print(key, value)
