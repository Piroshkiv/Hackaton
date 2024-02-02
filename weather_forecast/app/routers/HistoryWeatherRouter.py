import logging
from fastapi import APIRouter

from app.models import WeatherOneDayRequest, WeatherOneDayResponse, WeatherSeveralDaysRequest, \
    WeatherSeveralDaysResponse
from app.services import WeatherHistoryService

history_router = APIRouter()
history_service = WeatherHistoryService()


@history_router.post("/one_day/")
async def one_day(request: WeatherOneDayRequest) -> WeatherOneDayResponse:
    return await history_service.get_day_history(request.lon, request.lat, request.date)


@history_router.post("/several_days/")
async def one_day(request: WeatherSeveralDaysRequest) -> WeatherSeveralDaysResponse:
    return await history_service.get_days_history(request.lon, request.lat, request.start_date, request.end_date)
