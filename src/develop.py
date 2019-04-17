import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse,parse_qs


def pagination():
    return


def query(query,year):
    q = str(query)
    year = '?as_ylo={0}'.format(year)
    url = 'https://scholar.google.com/scholar'+ year + '&q={0}'.format(query) + '&ie=UTF-8&oe=UTF-8&hl=en&btnG=Search'

    content = requests.get(url).text
    page = BeautifulSoup(content, 'lxml')
    results = []
    nonfree = []
    for entry in page.find_all("h3", attrs={"class": "gs_rt"}):
        parsed = urlparse(entry.a['href'])
        b = {"title": entry.a.text,
                        "url": entry.a['href']}
        if parsed.netloc == 'www.ncbi.nlm.nih.gov':
            results.append(b)
        else:
            nonfree.append(b)

    return results,nonfree



print (query('candida%auris',2011))