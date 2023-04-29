import requests
import json

def get_weather():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=59.94&longitude=30.31&current_weather=true'
    r = requests.get(url)
    weather = r.json()['current_weather']
    return weather

if __name__ == '__main__':
    current_weather = get_weather()
    print(f"Temperature on St.Petersburg now is a {current_weather['temperature']} degrees Celsius")