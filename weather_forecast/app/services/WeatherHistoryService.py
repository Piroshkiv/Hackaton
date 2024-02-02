import asyncio
import csv
import json
from datetime import date, datetime, timedelta
from typing import Dict, Any, Iterable

from app.models import WeatherOneDayResponse, WeatherData, WeatherSeveralDaysResponse, WeatherOneDayRequest
from clients import OpenArchiveMeteoClient, OpenMeteoClient


class WeatherHistoryService:
    def __init__(self):
        self.ArchiveClient = OpenArchiveMeteoClient(base_url="https://archive-api.open-meteo.com")
        self.OpenClient = OpenMeteoClient(base_url="https://api.open-meteo.com")



    async def get_day_history(self, lat: float, lon: float, date: date) -> WeatherOneDayResponse:

        client = self.ArchiveClient if (datetime.now().date() - date ).days >= 5 else self.OpenClient

        weather: Dict[str, Any] = await client.get_archive_data(lat, lon, date, date)

        print(weather)

        weather_response = WeatherOneDayResponse(
            lat=float(weather['latitude']),
            lon=float(weather['longitude']),
            date=weather['daily']['time'][0],
            weather_data=WeatherData(**{
                "date": weather["daily"]["time"][0],
                "avg_temperature": weather["daily"]["temperature_2m_mean"][0],
                "precipitation":  weather["daily"]["precipitation_sum"][0],
                "rain_sum": weather["daily"]["rain_sum"][0],
                "snowfall_sum": weather["daily"]["snowfall_sum"][0],
                "shortwave_radiation_sum": weather["daily"]["shortwave_radiation_sum"][0]})


        )
        return weather_response

    async def get_days_history(self, lat: float, lon: float, start_date: date, end_date: date) -> WeatherSeveralDaysResponse:

        if start_date > end_date:
            raise ValueError("start_date cannot be greater than end_date")

        archiving_day = datetime.now().date() - timedelta(days=5)

        weather: Dict[str, Any]

        if( start_date >= archiving_day):
            weather = await self.OpenClient.get_archive_data(lat, lon, start_date, end_date)
        elif (end_date < archiving_day):
            weather = await self.ArchiveClient.get_archive_data(lat, lon, start_date, end_date)
        else:
            weather: Dict[str, Any] = await self.ArchiveClient.get_archive_data(lat, lon, start_date, archiving_day)
            new_weather: Dict[str, Any] = await self.ArchiveClient.get_archive_data(lat, lon, archiving_day + timedelta(days=1), end_date)

            weather['daily']["time"].extend(new_weather['daily']["time"])
            weather['daily']["temperature_2m_mean"].extend(new_weather['daily']["temperature_2m_mean"])
            weather['daily']["precipitation_sum"].extend(new_weather['daily']["precipitation_sum"])
            weather['daily']["rain_sum"].extend(new_weather['daily']["rain_sum"])
            weather['daily']["snowfall_sum"].extend(new_weather['daily']["snowfall_sum"])
            weather['daily']["shortwave_radiation_sum"].extend(new_weather['daily']["shortwave_radiation_sum"])


        weather_response = WeatherSeveralDaysResponse(
            lat=float(weather['latitude']),
            lon=float(weather['longitude']),
            start_date=weather['daily']['time'][0],
            end_date=weather['daily']['time'][-1],
            weather_data=[
                    WeatherData(**{
                        "date": x[0],
                        "avg_temperature": x[1],
                        "precipitation": x[2],
                        "rain_sum": x[3],
                        "snowfall_sum": x[4],
                        "shortwave_radiation_sum": x[5]
                    }) for x in
                        zip(weather["daily"]["time"],
                        weather["daily"]["temperature_2m_mean"],
                        weather["daily"]["precipitation_sum"],
                        weather["daily"]["rain_sum"],
                        weather["daily"]["snowfall_sum"],
                        weather["daily"]["shortwave_radiation_sum"])]
        )

        return weather_response

def to_data(date:str)-> date:
    return datetime.strptime(date, "%Y-%m-%d").date()
async def main():
    w = WeatherHistoryService()

    r:WeatherOneDayRequest = WeatherOneDayRequest( lat = 10.1, lon = 10.1, date = date(2024, 1, 1)  )

    latitude = 48.530461955161634
    longitude = 32.264886317252774
    start_date = "2020-02-01"
    end_date = "2024-02-01"
    variables = "weather_code,temperature_2m_max,temperature_2m_min,temperature_2m_mean,apparent_temperature_max,apparent_temperature_min,apparent_temperature_mean,sunrise,sunset,daylight_duration,sunshine_duration,precipitation_sum,rain_sum,snowfall_sum,precipitation_hours,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant,shortwave_radiation_sum,et0_fao_evapotranspiration"

    # Получение архивных данных
    archive_data = await w.get_days_history(latitude, longitude, to_data(start_date), to_data(end_date))

    w = WeatherHistoryService()

    # Запишите данные в CSV-файл
    with open(
            f"output{latitude:.3f},{latitude:.3f}.csv",
            mode="w",
            newline="",
            encoding="UTF-8",
    ) as csvfile:
        fieldnames = [
            "date",
            "avg_temperature",
            "precipitation",
            "rain_sum",
            "snowfall_sum",
            "shortwave_radiation_sum",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for weather in archive_data.weather_data:
            writer.writerow(weather.model_dump())


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())