import requests
from API_Key_for_weather import key


class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


CITIES = {
    "/spb": City("Saint Petersburg", 59.94, 30.31),
    "/msk": City("Moscow", 55.75, 37.62),
    "/muc": City("Munich", 48.14, 11.58),
}


def get_coordinates(city):
    city = city.lower()
    return CITIES[city]


def get_weather_from_location(latitude, longitude):
    try:
        coordinates = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
        }
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast", params=coordinates
        )
        data = response.json()
        current_weather = data["current_weather"]
        temperature = current_weather["temperature"]
        return temperature
    except Exception as ex:
        print(f"Error: {ex}")
        raise


def get_data_from_location(latitude, longitude):
    try:
        coordinates = {
            "lat": latitude,
            "lon": longitude,
            "apiKey": key,
        }
        response = requests.get(
            "https://api.geoapify.com/v1/geocode/reverse", params=coordinates
        )
        data = response.json()
        feature = data["features"][0]
        city = feature["properties"]["city"]
        street = feature["properties"]["address_line1"]
        return city, street
    except Exception as ex:
        print(f"Error: {ex}")
        raise
