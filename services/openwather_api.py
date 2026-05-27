import requests
from datetime import datetime
from config import Config
from tools.utils import to_celsius
from tools.utils import to_kmh

API_KEY = Config.API_KEY
API_QUERY = Config.API_QUERY

def get_weather():
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={API_QUERY}&appid={API_KEY}"

    try:
        response = requests.get(API_URL, verify=False)
        data = response.json()

        weather = {
           "name": data.get("name"),
           "temp": to_celsius(data.get("main").get("temp")),
            "feels_like": to_celsius(data.get("main").get("feels_like")),
            "wind_speed": to_kmh(data.get("wind").get("speed")),
            "humidity": data.get("main").get("humidity"),
            "pressure": data.get("main").get("pressure"),
            "clouds": data.get("clouds").get("all"),
            "dt": datetime.fromtimestamp(data.get("dt")).strftime("%Y-%m-%d %H:%M:%S"),
            "sunrise" : datetime.fromtimestamp(data.get("sys").get("sunrise")).strftime("%Y-%m-%d %H:%M:%S"),
            "sunset" : datetime.fromtimestamp(data.get("sys").get("sunset")).strftime("%Y-%m-%d %H:%M:%S")







        }

        return weather

    except Exception as e:
        print(e)