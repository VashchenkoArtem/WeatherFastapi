from fastapi import HTTPException
import datetime

from weather.clients import get_current_forecast_from_api, get_daily_forecast_from_api


def get_current_forecast(city_name: str | None = None):
    data = get_current_forecast_from_api(city_name= city_name)
    if data["cod"] == '404':
        raise HTTPException(
            status_code=404,
            detail="City does not exist"
        )
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

def get_daily_forecast(city_name: str | None = None):
    data = get_daily_forecast_from_api(city_name)
    if data["cod"] == '404':
        raise HTTPException(
            status_code=404,
            detail="City does not exist"
        )
    return data