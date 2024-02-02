from datetime import date, datetime, timedelta
from pydantic import BaseModel, validator, Field, ValidationError


class WeatherSeveralDaysRequest(BaseModel):
    lat: float
    lon: float
    start_date: date
    end_date: date

    @validator("lat")
    def validate_lat(cls, v):
        if not isinstance(v, float):
            raise ValueError("Latitude must be a float")
        if not 0 <= v <= 180:
            raise ValueError("Latitude must be in the range [0, 90]")
        return v

    @validator("lon")
    def validate_lon(cls, v):
        if not isinstance(v, float):
            raise ValueError("Longitude must be a float")
        if not 0 <= v <= 180:
            raise ValueError("Longitude must be in the range [0, 90]")
        return v

    @validator('start_date')
    def validate_start_date(cls, value):
        if value > date.today() or value < date.today() - timedelta(days=1000):
            raise ValueError('Start date must be between today and one year ago')
        return value

    @validator('end_date')
    def validate_end_date(cls, value, values):
        start_date = values.get('start_date')
        if start_date and value < start_date:
            raise ValueError('End date must be greater than or equal to start date')
        if value > date.today() or value < date.today() - timedelta(days=1000):
            raise ValueError('End date must be between today and one year ago')
        return value


