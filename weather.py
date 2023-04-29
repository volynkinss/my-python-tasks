import requests
import json

def get_weather(latitude,longitude):
    url = 'https://api.open-meteo.com/v1/forecast?latitude=59.94&longitude=30.31&current_weather=true'
    coordinates = {"latitude": "", "longitude":"","current_weather":"true"}
    coordinates["latitude"]=latitude
    coordinates["longitude"]=longitude
    r = requests.get('https://api.open-meteo.com/v1/forecast', params=coordinates)
    weather = r.json()['current_weather']
    return weather

if __name__ == '__main__':
    current_weather = get_weather(59.94,30.31)
    print(f"Temperature on St.Petersburg now is a {current_weather['temperature']} degrees Celsius")
