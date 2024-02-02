from datetime import date, datetime, timedelta
from pydantic import BaseModel, validator, Field, ValidationError, field_validator


class WeatherOneDayRequest(BaseModel):
    lat: float
    lon: float
    date: date

    @field_validator("lat", "lon")
    @classmethod
    def validate_lat(cls, v):
        if not isinstance(v, float):
            raise ValueError("Latitude must be a float")
        if not 0 <= v <= 180:
            raise ValueError("Latitude must be in the range [0, 180]")
        return v


    @field_validator("date")
    def validate_date(cls, v):
        today = datetime.now().date()
        one_year_ago = today - timedelta(days=365)
        if not (one_year_ago <= v <= today):
            raise ValueError('Date must be between today and one year ago')
        return v
