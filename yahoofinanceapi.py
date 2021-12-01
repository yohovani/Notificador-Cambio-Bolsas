import requests

class YahooApi:
    def __init__(self):
        self.__url = "https://yfapi.net/v11/finance/quoteSummary/"
        self.__headers = {
            'X-API-KEY': 'iUre9lD2zm7UBo4bdYoKr6zQdVX5mZjU5BN1uZUa',
            'accept': 'application/json'
        }
        self.__querystring = {"lang": "en", "region": "US", "modules": "price"}
    def _getHeaders(self):
        return self.__headers

    def _getUrl(self):
        return self.__url

    def _getQueryString(self):
        return self.__querystring

    def getquoteSummary(self, code):
        return requests.request("GET", self._getUrl()+code, headers=self._getHeaders(), params=self.__querystring)
