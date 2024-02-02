from datetime import date
from typing import Iterable

from pydantic import BaseModel

from app.models import WeatherData


class WeatherSeveralDaysResponse(BaseModel):
    lat: float
    lon: float
    start_date: date
    end_date: date
    weather_data: list[WeatherData]

