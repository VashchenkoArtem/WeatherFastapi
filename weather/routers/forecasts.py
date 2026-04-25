from fastapi import APIRouter
import requests
from datetime import datetime, timezone, timedelta

router = APIRouter()

@router.get("/forecast/now")
async def forecast_now(city_name: str | None = None):
    errors = []
    if not city_name:
        errors.append({
            "status": 400,
            "message": "City name is required. Please enter city name"
            })
        return {
            "errors":errors
            }
    forecast_now = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=2eb93887bcddb22f1d3a59d94af6b1c0&units=metric"
    )

    data = forecast_now.json()

    timestamp = data["dt"]
    timezone_offset = data["timezone"]

    tz = timezone(timedelta(seconds=timezone_offset))
    local_time = datetime.fromtimestamp(timestamp, tz=tz)
    response = {
        "status": 200,
        "forecast": data,
        "date_time": {
            "date": local_time.strftime("%d.%m.%Y"),
            "day_of_week": local_time.strftime("%A"), 
            "time": local_time.strftime("%H:%M:%S")
        }
    }
    return response