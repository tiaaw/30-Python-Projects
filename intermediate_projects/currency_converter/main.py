import json 
from typing import Final 
import requests

BASE_URL: Final[str] = "http://api.exchangeratesapi.io/v1/latest"
API_KEY: Final[str] = "77f0c20e036e226cf28c5b59b5ab98a6"  


def get_rates(mock: bool = False) -> dict:
    if mock:
        with open('rates.json', 'r') as file:
            data = json.load(file)
            return data
        
    payload = {'access_key': API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data = request.json()
    
    return data

def get_currency(currency:str, rates: dict) -> float:
    currency = currency.upper() # Convert to uppercase
    if currency in rates.keys(): 
        return rates.get(currency)
    else: 
        raise ValueError(f"Currency {currency} not found in rates.")


def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    base_rate = get_currency(base, rates)
    vs_rate = get_currency(vs, rates)
    
    conversion = round((vs_rate / base_rate) * amount, 2)
    print(f'{amount:,.2f} ({base}) is: {conversion:,.2f} ({vs})')
    return conversion

def main():
    data = get_rates(mock=True)
    rates = data.get('rates')
    
    convert_currency(100, 'EUR', 'AUD', rates=rates)
    
    
if __name__ == '__main__':
    main()