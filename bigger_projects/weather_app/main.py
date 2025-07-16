from weather_api import get_weather, get_weather_details, Weather

API_KEY = 'a40df88d3825d8b7dc95106c639a4cdb'
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast?'

def main(): 
    user_city = input("Enter a city name: ")
    
    # Get the current weather details 
    current_weather = get_weather(user_city, mock=False)
    weather_details = get_weather_details(current_weather)
    
    # Get the current days
    dfmt = "%d/%m/%y"
    days = sorted(list({f'{date.date:{dfmt}}' for date in weather_details}))
    
    for day in days: 
        print(day)
        print('---')
        
        grouped = [current for current in weather_details if f'{current.date:{dfmt}}' == day]
        for element in grouped:
            print(element)
            
        print()

if __name__ == '__main__':
    main()    