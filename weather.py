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

def get_weather(city):
    try:
        city = city.lower()
        request_city = list_of_cities[city]
        coordinates = {"latitude": request_city.latitude, "longitude": request_city.longitude, "current_weather":"true"}
        reference = requests.get('https://api.open-meteo.com/v1/forecast', params=coordinates)
        weather = reference.json()['current_weather']
        weather_text = f"Temperature in {request_city.name} now is a {weather['temperature']} degrees Celsius"
        return weather_text
    except Exception as er:
        raise
