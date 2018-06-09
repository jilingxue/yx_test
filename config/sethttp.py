import requests


class ConfigRequest:


    def __init__(self,url,data=None,):
        self.url = url
        self.data = data

    def post(self):
        return requests.post(url=self.url,data=self.data)

    def get(self):
        return requests.get(url=self.url,params=self.data).text

print(__name__)