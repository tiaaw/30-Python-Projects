import json
import requests

API_KEY = 'a40df88d3825d8b7dc95106c639a4cdb'
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast?'

# mock used for testing True is for dummy data
def get_weather(city_name: str, mock: bool = True) -> dict:
    if mock:
        with open('dummy_data.json') as file: 
            return json.load(file)
        
    # request live data    
    payload = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()
    
    return data

if __name__ == '__main__':
    print(get_weather('tokyo', mock=False))