from datetime import date
from typing import Optional

from pydantic import BaseModel


class WeatherData(BaseModel):
    date: date
    avg_temperature: Optional[float]
    precipitation: Optional[float]
    rain_sum: Optional[float]
    snowfall_sum: Optional[float]
    shortwave_radiation_sum: Optional[float]

