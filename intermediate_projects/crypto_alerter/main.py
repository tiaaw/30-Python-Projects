from crypto_data import get_coins, Coin

def alert(symbol: str, bottom_price: float, top_price: float, coins_list: list[Coin]):
    for coin in coins_list: 
        if coin.symbol == symbol: 
            if bottom_price > coin.current_price > top_price: 
                print(coin, '!!Triggered!!')
            else: 
                print(coin)
                

if __name__ == '__main__':
    coins = get_coins()
        
    alert('eth', 2000, 3000, coins)
    alert('btc', 2000, 3000, coins)
    alert('doge', 0.1, 0.2, coins)