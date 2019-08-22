from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from keys_pocket import ApiKeys

class getCoins:
    def __init__(self, in_coins):
        self.in_coins = in_coins
        self.CMC_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        self.comma = ','
        self.parameters = {
            'symbol': self.comma.join(in_coins)
        }

        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': ApiKeys.CMC_API_KEY,
        }

    def get_coins(self):
        try:
            session = Session()
            session.headers.update(self.headers)
            response = session.get(self.CMC_URL, params=self.parameters).json()
            response = json.dumps(response['data'])
            data = json.loads(response)
            out_coins = {}
            for coin in self.in_coins:
                price = round(data[coin]['quote']['USD']['price'], 2)
                #change_day = round(data[coin]['quote']['USD']['percent_change_24h'], 2)
                out_coins[coin] = price

            #out_coins = ' '.join("{!s} {!r}".format(key,val) for (key,val) in out_coins.items())
            return out_coins
        
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

