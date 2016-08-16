import requests
import json


class Shortest:
    @staticmethod
    def get(url, token):
        headers = {'public-api-token': token}
        data = {'urlToShorten': url}

        try:
            r = requests.put('https://api.shorte.st/v1/data/url', data=data, headers=headers)
            return r.json()['shortenedUrl']
        except json.decoder.JSONDecodeError:
            raise ValueError('Wrong token or url')
