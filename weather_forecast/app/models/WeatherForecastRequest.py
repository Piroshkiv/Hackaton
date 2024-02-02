from datetime import date, datetime, timedelta
from pydantic import BaseModel, validator, Field, ValidationError, field_validator

class WeatherForecastRequest(BaseModel):
    lat: float
    lon: float
    days_count: int

    @field_validator("lat", "lon")
    @classmethod
    def validate_lat(cls, v):
        if not isinstance(v, float):
            raise ValueError("Latitude must be a float")
        if not 0 <= v <= 180:
            raise ValueError("Latitude must be in the range [0, 180]")
        return v


    @field_validator("days_count")
    def validate_date(cls, v):
        if not (0 < v <= 31):
            raise ValueError('Day count must be between 1 and 31')
        return v