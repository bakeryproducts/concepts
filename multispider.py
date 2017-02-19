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


def exlist(link):                                       #this is probably bad idea
    list = ['mailto:', 'tel:', 'javascript:']
    for el in list:
        if el in link:
            return True
    return False


def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a', href=True) if not exlist(link.get('href').lower())]
        links = [handle_local(url, link) for link in links]
        # links = [str(link.encode('utf-8')) for link in links]
        return links
    except Exception as e:
        print(e)
        return []


def check_dom(url, visited):
    dom = url.split('//')[-1].split('/')[0]
    if dom not in visited:
        visited.append(dom)
        return True
    else:
        return False


def main():
    count = 1
    p = Pool(processes=count)
    parse_us = [url_gen() for _ in range(count)]
    print(parse_us)
    visited_domain = []
    while 'www.youtube.com' not in visited_domain:
        data = p.map(get_links, parse_us)
        data = [url for site in data for url in site]
        data_out = '\n'.join(data)
        with open('testingurl.txt', 'w') as f:
            f.write(data_out)

        clean_data = []                                         # and this clear_data thing is bad too
        for ind, url in enumerate(data):
            if check_dom(url, visited_domain):
                clean_data.append(url)
        data = clean_data

        parse_us = data

        print(parse_us)
        count += 1
        if count > 10 or len(parse_us) == 0:
            print('quiting, hit top!')
            break

    with open('visited.txt', 'w') as f:
        f.write('\n'.join(visited_domain))
    p.close()


if __name__ == '__main__':
    main()
