import requests
import json

class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

list_of_cities = {
            "spb":City("Saint Petersburg", 59.94, 30.31),
            "msk":City("Moscow", 55.75, 37.62),
            "muc":City("Munich", 48.14, 11.58)
            }

def get_location(location):
    latitude = ""
    longitude = ""
    if type(location) == str:
        location = location.lower()
        request_city = list_of_cities[location]
        latitude = request_city.latitude
        longitude = request_city.longitude
    elif type(location) == tuple:
        latitude = location[0]
        longitude = location[1]
    coordinates = {"latitude": latitude, "longitude": longitude, "current_weather":"true"}
    return coordinates
        
    

def get_weather_from_location(location):
    try:
        reference = requests.get('https://api.open-meteo.com/v1/forecast', params=get_location(location))
        weather = reference.json()['current_weather']
        weather_text = f"Temperature in your location now is a {weather['temperature']} degrees Celsius"
        return weather_text
    except Exception as er:
        raise

# def get_weather(city):
#     city = city.lower()
#     request_city = list_of_cities[city]
#     latitude = request_city.latitude
#     longitude = request_city.longitude
#     get_weather_from_location(latitude , longitude)


