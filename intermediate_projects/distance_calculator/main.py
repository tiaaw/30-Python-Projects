from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


@dataclass
class Coordinates: 
    latitude: float
    longitude: float
    
    def coordinates(self):
        return self.latitude, self.longitude
    

def get_coordinates(address: str) -> Coordinates | None: 
    geolocator = Nominatim(user_agent='distance_calculator')
    location = geolocator.geocode(address)
    
    if location: 
        return Coordinates(latitude=location.latitude, longitude=location.longitude)
    
    return None


def calculate_distance_km(home: Coordinates, target: Coordinates) -> float | None: 
    if home and target: 
        distance = geodesic(home.coordinates(), target.coordinates()).kilometers
        return distance
    
    return None
    
    
def get_distance_km(home: str, target: str) -> float | None:
    home_coordinates = get_coordinates(home)
    target_coordinates = get_coordinates(target)
    
    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f'Distance from {home} to {target}')
        print(f'{distance:.2f} km')
        return distance
    else:
        print('Could not calculate distance.')
        return None
    

    
    
def main(): 
    home_address = '123 Main St, Sydney, Australia'
    print(f'Home address: {home_address}')
    
    target_address = input('Enter an address: ')
    print('Calculating distance...')
    get_distance_km(home_address, target_address)    
    
if __name__ == '__main__':
    main()