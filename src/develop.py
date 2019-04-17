import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse,parse_qs


def pagination(query,year):
    q = str(query)
    a = ['start={0}'.format(x) for x in range(0,20,10)]
    year = 'as_ylo={0}'.format(year)
    for x in a:
        url = "https://scholar.google.com/scholar?{0}&q={1}&hl=en&as_sdt=0,11&{2}".format(x,q,year)
        content = requests.get(url).text
        print (content)
    return a


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
        b = {"title": entry.a.text,"url": entry.a['href']}
        if parsed.netloc == 'www.ncbi.nlm.nih.gov':
            results.append(b)
        else:
            nonfree.append(b)

    return results,nonfree



# print (query('candida%auris',2011))
print (pagination('candida%auris',2011))