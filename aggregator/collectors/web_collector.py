import requests
from bs4 import BeautifulSoup

class WebPageCollector:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        resp = requests.get(self.url)
        resp.raise_for_status()
        return resp.text
