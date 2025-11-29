import requests

class APICollector:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def fetch(self):
        resp = requests.get(self.endpoint)
        resp.raise_for_status()
        return resp.json()
