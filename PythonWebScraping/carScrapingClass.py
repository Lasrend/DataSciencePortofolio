# Library
from bs4 import BeautifulSoup
import requests

# CONSTANT VAR
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }


class Scrape:
    def __init__(self, link):
        self.link = requests.get(link, headers=HEADERS).text
        self.soup = BeautifulSoup(self.link, "html.parser")

    def scrapeDetail(self):
        price = self.soup.find("span", class_="h4 price_big").getText().split()[1]
        loc = self.soup.find("i", class_="fa fa-map-marker").next_sibling.strip()
        spec = self.soup.find_all("ul", class_="list-unstyled detailpagelist")[0].getText().strip().split("\n")

        dicSpec = {}
        for i in spec:
            word = i
            if "\xa0" in word:
                word = word.replace("\xa0",'')
    
            word = word.strip()
            word = word.split(":")
            dicSpec[word[0]] = word[1].strip()
        dicSpec["Loc"] = loc
        dicSpec["Price"] = price

        return dicSpec