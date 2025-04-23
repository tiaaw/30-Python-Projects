import requests
from dataclasses import dataclass

BASE_URL = 'https://api.coingecko.com/api/v3/coins/markets'


@dataclass
class Coin: 
    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24hr: float
    price_change_percentage_24hr: float
    
    def __str__(self):
        return f'{self.name} ({self.symbol}) - Current Price: ${self.current_price} AUD'
    

def get_coins() -> list[Coin]: 
    payload = {'vs_currency': 'aud', 'order': 'market_cap_desc'}
    data = requests.get(BASE_URL, params=payload)
    json = data.json()
    
    coin_list = []
    for coin in json: 
        current_coin = Coin(name=coin.get('name'),
                            symbol=coin.get('symbol'),
                            current_price=coin.get('current_price'),
                            high_24h=coin.get('high_24h'),
                            low_24h=coin.get('low_24h'),
                            price_change_24hr=coin.get('price_change_24h'),
                            price_change_percentage_24hr=coin.get('price_change_percentage_24h'))
        coin_list.append(current_coin)
        
    return coin_list

if __name__ == '__main__':
    coins = get_coins()
    for coin in coins: 
        print(coin)