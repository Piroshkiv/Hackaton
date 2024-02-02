from datetime import date

from pydantic import BaseModel

from app.models import WeatherData


class WeatherOneDayResponse(BaseModel):
    lat: float
    lon: float
    date: date
    weather_data: WeatherData

