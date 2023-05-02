import requests
import json


def get_weather(city):
    try:
        coordinates = {"latitude": "", "longitude":"","current_weather":"true"}
        town = ""
        list_of_cities = {
            "spb":("Saint Petersburg", "59.94", "30.31"),
            "msk":("Moscow", "55.75", "37.62"),
            "muc":("Munich", "48.14", "11.58")
            }
        coordinates["latitude"]=list_of_cities[city.lower()][1]
        coordinates["longitude"]=list_of_cities[city.lower()][2]
        town = list_of_cities[city.lower()][0]
        r = requests.get('https://api.open-meteo.com/v1/forecast', params=coordinates)
        weather = r.json()['current_weather']
        print(f"Temperature in {town} now is a {weather['temperature']} degrees Celsius")
    except KeyError:
        print("This city is not on the list ")
    except Exception as er:
        print(er)

if __name__ == '__main__':
    get_weather("mus")
