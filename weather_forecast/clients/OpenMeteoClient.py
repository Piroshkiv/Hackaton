import datetime
from datetime import date
from typing import Dict, Any

import aiohttp
import asyncio


class OpenMeteoClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def get_archive_data(self, lat: float, lon: float, start_date: date, end_date: date) -> Dict[str, Any]:
        variables: str = "temperature_2m_mean,apparent_temperature_mean,daylight_duration,sunshine_duration,precipitation_sum,rain_sum,snowfall_sum,precipitation_hours,shortwave_radiation_sum"
        url = f"{self.base_url}/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "start_date": start_date.strftime('%Y-%m-%d'),
            "end_date": end_date.strftime('%Y-%m-%d'),
            "daily": variables
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                data = await response.json()
                return data


# Пример использования клиента
async def main():
    client = OpenMeteoClient("https://api.open-meteo.com")
    data = await client.get_archive_data(1.23, 4.56, datetime.date(2022, 1, 25), datetime.date(2024,1,28))
    print(data)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())