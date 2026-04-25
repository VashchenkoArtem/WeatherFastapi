from fastapi import APIRouter, Depends

from weather.services import get_current_forecast, get_daily_forecast_from_api
from weather.dependencies import validate_city

router = APIRouter(
    prefix="/forecast"
)


@router.get("/now")
async def forecast_now(city_name: str = Depends(validate_city)):
    response = get_current_forecast(city_name= city_name)
    return response

@router.get("/daily")
async def daily_forecast(city_name: str = Depends(validate_city)):
    response = get_daily_forecast_from_api(city_name)
    return response