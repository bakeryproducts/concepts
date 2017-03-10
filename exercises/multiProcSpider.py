from multiprocessing import Pool
from urllib.parse import urljoin
import bs4 as bs
import requests
import random
import string
from requests.adapters import HTTPAdapter

#s = requests.Session()


def url_gen():
    st = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    st = ''.join(['http://', st, '.ru'])
    return st


def exlist(link):  # this is probably bad idea
    list = ['mailto:', 'tel:', 'javascript:', 'skype:',
            '.ppt', '.jpg', '.doc', '#', '.png', '.gif', '.rar', '.zip', 'tg:', '*', '.pdf', 'mp4']
    for el in list:
        if el in link:
            return True
    return False


def get_links(url):
    try:
        print(url)
        #s.mount(url, HTTPAdapter(max_retries=2))
        resp = requests.get(url)
        #resp = s.get(url)

        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body

        links = [link.get('href') for link in body.find_all('a', href=True) if not exlist(link.get('href').lower())]
        links = [urljoin(url, link) for link in links]
        # links = [str(link.encode('utf-8')) for link in links]
        print(' get links',links)
        return links
    except Exception as e:
        print(e)
        return []


def get_dom(url):
    dom = url.split('//')[1].split('/')[0]
    return dom


def main():
    count = 2
    p = Pool(processes=2)
    # parse_us = [url_gen() for _ in range(count)]
    parse_us = ['http://yod.ru', 'http://uzg.ru']

    visited_domain = []
    visited_urls = []
    print(parse_us)
    fd = open('visitedDoms.txt', 'w')
    fu = open('visitedUrls.txt', 'w')

    while 'www.youtube.com' not in visited_domain and len(parse_us) > 0 and count < 10:
        data = p.map(get_links, parse_us)
        data = [url for site in data for url in site]
        data = list(set(data))
        print('1')
        parse_us = [url for url in data if url not in visited_urls and get_dom(url) not in visited_domain]
        visited_urls.extend(parse_us)
        new_dom = ([get_dom(url) for url in parse_us if get_dom(url) not in visited_domain])
        visited_domain.extend(list(set(new_dom)))
        # if len(parse_us)>50:
        #     parse_us=parse_us[:50]

        fd.write('\n'.join(list(set(new_dom))))
        fu.write('\n'.join(parse_us))

        print(len(data), ' urls in data; new ones: ', parse_us)
        count += 1

    p.close()
    fd.close()
    fu.close()


if __name__ == '__main__':
    main()
