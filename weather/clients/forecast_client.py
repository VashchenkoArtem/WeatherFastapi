import requests
import os
from fastapi import HTTPException

API_KEY = os.getenv("API_KEY")


class OpenWeatherClient:
    BASE_URL = "https://api.openweathermap.org/data/2.5"

    def get_forecast_data(self, endpoint: str, params: dict):
        url = f"{self.BASE_URL}/{endpoint}"

        response = requests.get(url, params)
        if response.status_code == 400:
            raise HTTPException(400, "City name did not get")
        
        if response.status_code == 404:
            raise HTTPException(404, "City not found")

        if not response.ok:
            raise HTTPException(502, "Weather service error")

        return response.json()
    
    def get_current_forecast_from_api(self, city_name: str):
        return self.get_forecast_data(
            endpoint= "weather", 
            params= {
                "q": city_name,
                "appid": API_KEY
            }
        )
    
    def get_daily_forecast_from_api(self, city_name: str):
        return self.get_forecast_data(
            endpoint= "forecast",
            params= {
                "q": city_name,
                "appid": API_KEY
            }
        )