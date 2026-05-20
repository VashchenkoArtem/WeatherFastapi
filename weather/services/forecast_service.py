import datetime

from weather.clients.forecast_client import OpenWeatherClient


def get_current_forecast(city_name: str | None, client: OpenWeatherClient):
    data = client.get_current_forecast_from_api(city_name)
    timestamp = data["dt"]
    timezone_offset = data["timezone"]

    tz = datetime.timezone(datetime.timedelta(seconds=timezone_offset))
    local_time = datetime.datetime.fromtimestamp(timestamp, tz=tz)
    response = {
        "forecast": data,
        "date_time": {
            "date": local_time.strftime("%d.%m.%Y"),
            "day_of_week": local_time.strftime("%A"), 
            "time": local_time.strftime("%H:%M")
        }
    }
    return response

def get_daily_forecast(city_name: str | None, client: OpenWeatherClient):
    data = client.get_daily_forecast_from_api(city_name)

    return data