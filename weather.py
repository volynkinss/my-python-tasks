import requests
import json


class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


list_of_cities = {
    "spb": City("Saint Petersburg", 59.94, 30.31),
    "msk": City("Moscow", 55.75, 37.62),
    "muc": City("Munich", 48.14, 11.58),
}


def get_coordinates(city):
    print("started get_coordinates_function")
    city = city.lower()
    request_city = list_of_cities[city]
    location = request_city.latitude, request_city.longitude
    geolocation = request_city.name
    return location, geolocation


def get_weather_from_location(location):
    print("start of get_weather_from_location_function")
    try:
        latitude, longitude = location
        coordinates = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": "true",
        }
        reference = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params=coordinates,
        )
        weather = reference.json()["current_weather"]
        temperature = weather["temperature"]
        return temperature
    except Exception as er:
        raise
