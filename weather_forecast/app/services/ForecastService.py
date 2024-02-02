import asyncio
import csv
import json
import pandas as pd

from datetime import date, datetime, timedelta
from typing import Dict, Any, Iterable

from app.models import WeatherOneDayResponse, WeatherData, WeatherSeveralDaysResponse, WeatherOneDayRequest
from app.services import WeatherHistoryService
from prediction import WeatherPrediction


class ForecastService:
    def __init__(self):
        self.history_service = WeatherHistoryService()

    async def get_forecast(self, lat: float, lon: float, days_count: int = 7) -> WeatherSeveralDaysResponse:
        #self.weather_prediction  # = WeatherPrediction()
        today = datetime.today().date()

        history = await self.history_service.get_days_history(lat, lon, (today - timedelta(days=10)),
                                                        (today - timedelta(days=1)))

        data_dicts = [obj.model_dump() for obj in history.weather_data]
        df = pd.DataFrame(data_dicts)

        weather_prediction = WeatherPrediction(df)

        prediction_data = weather_prediction.predict_all(days=days_count)

        print(prediction_data)

        weather_data_objects = []
        for i in range(len(prediction_data['date'])):
            weather_data_objects.append(WeatherData(
                date=prediction_data['date'][i],
                avg_temperature=prediction_data.get('avg_temperature_hat', [None])[i],
                precipitation=prediction_data.get('precipitation_hat', [None])[i],
                rain_sum=prediction_data.get('rain_sum_hat', [None])[i],
                snowfall_sum=prediction_data.get('snowfall_sum_hat', [None])[i],
                shortwave_radiation_sum=prediction_data.get('shortwave_radiation_sum_hat', [None])[i]
            ))

        return WeatherSeveralDaysResponse(lat=lat, lon=lon, start_date=weather_data_objects[0].date, end_date=weather_data_objects[-1].date, weather_data = weather_data_objects)

async def main():
    w = ForecastService()

    latitude = 48.530461955161634
    longitude = 32.264886317252774
    start_date = "2020-02-01"
    end_date = "2024-02-01"
    variables = "weather_code,temperature_2m_max,temperature_2m_min,temperature_2m_mean,apparent_temperature_max,apparent_temperature_min,apparent_temperature_mean,sunrise,sunset,daylight_duration,sunshine_duration,precipitation_sum,rain_sum,snowfall_sum,precipitation_hours,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant,shortwave_radiation_sum,et0_fao_evapotranspiration"

    data = await w.get_forecast(latitude, longitude, 7)



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())