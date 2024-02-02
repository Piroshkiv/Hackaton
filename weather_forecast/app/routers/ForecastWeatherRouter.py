import logging
from fastapi import APIRouter

from app.models import WeatherOneDayRequest, WeatherOneDayResponse, WeatherSeveralDaysRequest, \
    WeatherSeveralDaysResponse, WeatherForecastRequest
from app.services import WeatherHistoryService, ForecastService

forecast_router = APIRouter()
forecast_service = ForecastService()

@forecast_router.post("/forecast/several_days/")
async def one_day(request: WeatherForecastRequest) -> WeatherSeveralDaysResponse:
    return await forecast_service.get_forecast(request.lat, request.lon, request.days_count)