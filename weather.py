import requests
import json

def get_weather(city):
    coordinates = {"latitude": "", "longitude":"","current_weather":"true"}
    town = ""
    if city.lower() == "spb":
        coordinates["latitude"]=59.94
        coordinates["longitude"]=30.31
        town = "Saint Petersburg"
    elif city.lower() == "msk":
        coordinates["latitude"]=55.75
        coordinates["longitude"]=37.62
        town = "Moscow"
    else:
        print("You can choose only 'SPB' or 'MSK'")
    r = requests.get('https://api.open-meteo.com/v1/forecast', params=coordinates)
    weather = r.json()['current_weather']
    return weather , town

if __name__ == '__main__':
    current_weather = get_weather("msk")
    print(f"Temperature in {current_weather[-1]} now is a {current_weather[0]['temperature']} degrees Celsius")