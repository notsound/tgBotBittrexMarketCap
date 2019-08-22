from keys_pocket import ApiKeys
from bittrex.bittrex import *

class getBittrex:
    def __init__(self):
        self.api_key = ApiKeys.BTTRX_API_KEY
        self.api_secret = ApiKeys.BTTRX_API_SECRET
    
    def get_bittrex_coins(self):
        btx = Bittrex(self.api_key, self.api_secret)
        btx = btx.get_balances()['result']
        btx_coins = {}
        
        for i in btx:
            if i['Balance'] !=0:
                btx_coins[i['Currency']] = i['Balance']
        
        return btx_coins