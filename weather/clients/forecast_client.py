import requests

def get_current_forecast_from_api(city_name: str):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=2eb93887bcddb22f1d3a59d94af6b1c0&units=metric"
    ).json()
    return response