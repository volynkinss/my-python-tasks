import requests
import json

list_of_cities = {
            "spb":("Saint Petersburg", "59.94", "30.31"),
            "msk":("Moscow", "55.75", "37.62"),
            "muc":("Munich", "48.14", "11.58")
            }

def get_weather(city):
    try:
        city = city.lower()
        class City_characteristics:
            name = list_of_cities[city][0]
            latitude = list_of_cities[city][1]
            longitude = list_of_cities[city][2]
        city = City_characteristics()
        coordinates = {"latitude": city.latitude, "longitude":city.longitude,"current_weather":"true"}
        r = requests.get('https://api.open-meteo.com/v1/forecast', params=coordinates)
        weather = r.json()['current_weather']
        print(f"Temperature in {city.name} now is a {weather['temperature']} degrees Celsius")
    except KeyError:
        print("This city is not on the list ")
    except Exception as er:
        print(er)

if __name__ == '__main__':
    get_weather("spb")
