from fastapi import APIRouter

from weather.services import get_current_forecast

router = APIRouter()


@router.get("/forecast/now")
async def forecast_now(city_name: str | None = None):
    response = get_current_forecast(city_name= city_name)
    return response

