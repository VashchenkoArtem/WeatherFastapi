from fastapi import APIRouter, Depends

from weather.dependencies.forecast_dependency import get_weather_client
from weather.services import get_current_forecast, get_daily_forecast

router = APIRouter(
    prefix="/forecast"
)


@router.get("/now")
def forecast_now(city_name: str, client = Depends(get_weather_client)):
    return get_current_forecast(city_name, client)

@router.get("/daily")
async def daily_forecast(city_name: str, client = Depends(get_weather_client)):
    return get_daily_forecast(city_name, client)