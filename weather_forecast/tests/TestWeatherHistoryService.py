import unittest
from datetime import date, timedelta
from app.services import WeatherHistoryService

class TestWeatherHistoryService(unittest.IsolatedAsyncioTestCase):
    async def test_get_days_history(self):
        # Создаем экземпляр сервиса
        weather_service = WeatherHistoryService()

        # Задаем параметры для теста
        lat = 40.7128
        lon = 74.0060
        start_date = date(2024, 1, 1)
        end_date = date(2024, 1, 5)

        # Вызываем метод get_days_history
        result = await weather_service.get_days_history(lat, lon, start_date, end_date)

        # Проверяем, что результат не является пустым
        self.assertIsNotNone(result)

        # Проверяем, что значения lat и lon равны заданным
        self.assertAlmostEqual(result.lat, lat, delta=0.1)
        self.assertAlmostEqual(result.lon, lon, delta=0.5)

        # Проверяем, что даты начала и конца соответствуют заданным датам
        self.assertEqual(result.start_date, start_date)
        self.assertEqual(result.end_date, end_date)

        # Проверяем, что список weather_data не пустой
        self.assertTrue(result.weather_data)

    async def test_get_days_history_with_invalid_dates(self):
        weather_service = WeatherHistoryService()

        lat = 40.7128
        lon = 74.0060
        start_date = date(2024, 2, 5)
        end_date = date(2024, 1, 1)


        with self.assertRaises(ValueError):
            await weather_service.get_days_history(lat, lon, start_date, end_date)

if __name__ == '__main__':
    unittest.main()