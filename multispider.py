from multiprocessing import Pool
from urllib.parse import urljoin
import bs4 as bs
import requests
import random
import string


def url_gen():
    st = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    st = ''.join(['http://', st, '.com'])
    return st


def handle_local(url, link):
    return urljoin(url, link)


def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local(url, link) for link in links]
        links = [str(link.encode('ascii')) for link in links]
        return links
    except Exception as e:
        print(e)
        return []


def main():
    count = 3
    p = Pool(processes=count)
    parse_us = [url_gen() for _ in range(count)]
    data = p.map(get_links, parse_us)
    p.close()

    data = [url for site in data for url in site]
    data = '\n'.join(data)
    with open('testingurl.txt', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    main()
