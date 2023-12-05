import urllib.request as request
from bs4 import BeautifulSoup
from thefuzz import fuzz

with open('document.txt', 'r') as f:
    document = f.read()

with open('links.txt', 'r') as f:
    links = f.readlines()

    for url in links:
        request_site = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        webUrl = request.urlopen(request_site)
        data = webUrl.read()

        soup = BeautifulSoup(data, 'html.parser')
        plain_text = soup.get_text()

        lines = (line.strip() for line in plain_text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        fuzzy_ratio = fuzz.ratio(document, text)
        fuzzy_partial_ratio = fuzz.partial_ratio(document, text)

        print(f'{fuzzy_partial_ratio}% - {fuzzy_ratio}% => {url}')
