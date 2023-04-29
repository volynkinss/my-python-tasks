import requests
import json

def get_weather(city):
    coordinates = {"latitude": "", "longitude":"","current_weather":"true"}
    if city.lower() == "spb":
        coordinates["latitude"]=59.94
        coordinates["longitude"]=30.31
    elif city.lower() == "msk":
        coordinates["latitude"]=55.75
        coordinates["longitude"]=37.62
    else:
        print("You can choose only 'SPB' or 'MSK'")
    r = requests.get('https://api.open-meteo.com/v1/forecast', params=coordinates)
    weather = r.json()['current_weather']
    return weather

if __name__ == '__main__':
    current_weather = get_weather("Msk")
    print(f"Temperature on St.Petersburg now is a {current_weather['temperature']} degrees Celsius")
