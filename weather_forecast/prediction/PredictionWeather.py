from __future__ import annotations

import pandas as pd
from enum import Enum
from prophet import Prophet
import datetime

class WeatherRegressor(Enum):
    """
    Describes what one can predict
    """

    AVG_TEMPERATURE = "avg_temperature"
    PRECIPITATION = "precipitation"
    RAIN_SUM = "rain_sum"
    SNOWFALL_SUM = "snowfall_sum"
    SHORTWAVE_RADIATION_SUM = "shortwave_radiation_sum"


class WeatherRegressor(Enum):
    """
    Describes what one can predict
    """

    AVG_TEMPERATURE = "avg_temperature"
    PRECIPITATION = "precipitation"
    RAIN_SUM = "rain_sum"
    SNOWFALL_SUM = "snowfall_sum"
    SHORTWAVE_RADIATION_SUM = "shortwave_radiation_sum"


class WeatherPrediction:
    """
    Class for `weather prediction`
    """

    def __init__(self, data: pd.DataFrame) -> None:
        """
        data must have the following keys:

        `date` e.g. 2024-01-08
        `avg_temperature:` float
        `precipitation:` float
        `rain_sum:` float
        `snowfall_sum:` float
        `shortwave_radiation_sum:` float
        """
        self.data = data
        self.model_temp: Prophet | None = None
        self.model_precipitation: Prophet | None = None
        self.model_rain_sum: Prophet | None = None
        self.model_snowfall_sum: Prophet | None = None
        self.model_shortwave_radiation_sum: Prophet | None = None

    def __generate_data_frame(self, regressor: WeatherRegressor) -> pd.DataFrame:
        new_df = self.data.copy(deep=False)
        new_df.rename(columns={regressor.value: "y", "date": "ds"}, inplace=True)
        return new_df[["ds", "y"]]

    def avg_temperature(self, days: int = 7) -> pd.DataFrame:
        """
        `days` for how long to predict

        The method predicts `average temperature`
        """
        df = self.__generate_data_frame(WeatherRegressor.AVG_TEMPERATURE)
        self.model_temp = Prophet(growth="flat", yearly_seasonality=4)
        self.model_temp.fit(df)
        future_dates = pd.date_range(
            start=df.iloc[-1]["ds"], periods=days + 1, freq="D", inclusive="neither"
        )
        future_df = pd.DataFrame({"ds": future_dates})
        forecast = self.model_temp.predict(future_df)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]

    def precipitation(self, days: int = 7) -> pd.DataFrame:
        """
         `days` for how long to predict

        The method predicts `precipitation`
        """
        df = self.__generate_data_frame(WeatherRegressor.PRECIPITATION)
        self.model_temp = Prophet(growth="flat", yearly_seasonality=4)
        self.model_temp.fit(df)
        future_dates = pd.date_range(
            start=df.iloc[-1]["ds"], periods=days + 1, freq="D", inclusive="neither"
        )
        future_df = pd.DataFrame({"ds": future_dates})
        forecast = self.model_temp.predict(future_df)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]

    def rain_sum(self, days: int = 7) -> pd.DataFrame:
        """
         `days` for how long to predict

        The method predicts `rain sum`
        """
        df = self.__generate_data_frame(WeatherRegressor.RAIN_SUM)
        self.model_temp = Prophet(growth="flat", yearly_seasonality=4)
        self.model_temp.fit(df)
        future_dates = pd.date_range(
            start=df.iloc[-1]["ds"], periods=days + 1, freq="D", inclusive="neither"
        )
        future_df = pd.DataFrame({"ds": future_dates})
        forecast = self.model_temp.predict(future_df)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]

    def snowfall_sum(self, days: int = 7) -> pd.DataFrame:
        """
         `days` for how long to predict

        The method predicts `snowfall sum`
        """
        df = self.__generate_data_frame(WeatherRegressor.SNOWFALL_SUM)
        self.model_temp = Prophet(growth="flat", yearly_seasonality=4)
        self.model_temp.fit(df)
        future_dates = pd.date_range(
            start=df.iloc[-1]["ds"], periods=days + 1, freq="D", inclusive="neither"
        )
        future_df = pd.DataFrame({"ds": future_dates})
        forecast = self.model_temp.predict(future_df)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]

    def shortwave_radiation_sum(self, days: int = 7) -> pd.DataFrame:
        """
         `days` for how long to predict

        The method predicts `shortwave radiation sum`
        """
        df = self.__generate_data_frame(WeatherRegressor.SHORTWAVE_RADIATION_SUM)
        self.model_temp = Prophet(growth="flat", yearly_seasonality=4)
        self.model_temp.fit(df)
        future_dates = pd.date_range(
            start=df.iloc[-1]["ds"], periods=days + 1, freq="D", inclusive="neither"
        )
        future_df = pd.DataFrame({"ds": future_dates})
        forecast = self.model_temp.predict(future_df)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]

    def predict_all(
        self, days: int = 7
    ) -> dict[str, list[float] | list[datetime.date]]:
        """
        returns all data, predicting it using other methods of the class.

        {
            `date`: datetime.date(year, month, day),

            `avg_temperature_hat:` float,
            `avg_temperature_lower:` float,
            `avg_temperature_upper:` float,

            `precipitation_hat:` float,
            `precipitation_lower:` float,
            `precipitation_upper:` float,

            `rain_sum_hat:` float,
            `rain_sum_lower:` float,
            `rain_sum_upper:` float,

            `snowfall_sum_hat:` float,
            `snowfall_sum_lower:` float,
            `snowfall_sum_upper:` float,

            `shortwave_radiation_sum_hat:` float,
            `shortwave_radiation_sum_lower:` float,
            `shortwave_radiation_sum_upper:` float
        }
        """
        future_dates = [
            i.date()
            for i in pd.date_range(
                start=self.data.iloc[-1]["date"],
                periods=days + 1,
                freq="D",
                inclusive="neither",
            )
        ]

        def __create_dict(df_: pd.DataFrame, name: str) -> dict:
            temp_ = df_[["yhat", "yhat_lower", "yhat_upper"]]

            temp = temp_.rename(
                columns={
                    "yhat": f"{name}_hat",
                    "yhat_lower": f"{name}_lower",
                    "yhat_upper": f"{name}_upper",
                }
            )
            return {column: temp[column].tolist() for column in temp.columns}

        return {
            "date": future_dates,
            **__create_dict(self.avg_temperature(days=days), "avg_temperature"),
            **__create_dict(self.precipitation(days=days), "precipitation"),
            **__create_dict(self.rain_sum(days=days), "rain_sum"),
            **__create_dict(self.snowfall_sum(days=days), "snowfall_sum"),
            **__create_dict(
                self.shortwave_radiation_sum(days=days), "shortwave_radiation_sum"
            ),
        }


if __name__ == "__main__":
    the_class = WeatherPrediction(pd.read_csv("output49.234,49.234.csv"))
    print(the_class.predict_all())
