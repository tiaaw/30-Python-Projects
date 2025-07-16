from datetime import datetime as dt
import json
import requests
from model import Weather

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


def get_weather_details(weather: dict) -> list[Weather]:
    days = weather.get('list')
    
    if not days: 
        raise Exception("Problem with json: {weather}")
    
    list_of_weather = []
    
    for day in days: 
        w = Weather(date=dt.fromtimestamp(day.get('dt')),
                    details=(details := day.get('main')),
                    temp=details.get('temp'),
                    weather=(weather := day.get('weather')),
                    description=weather[0].get('description'))
        list_of_weather.append(w)
        
    return list_of_weather
                    