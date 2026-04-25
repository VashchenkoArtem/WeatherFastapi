import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_current_forecast_from_api(city_name: str):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    ).json()
    return response

def get_daily_forecast_from_api(city_name: str):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric&cnt=16"
    ).json()
    return response