# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Schema for all weather-related data structures to be used, to keep all
#              data consistent
#
# Author: Riley Eaton
# Date: 2024-11-25
# *************************************************************************************

from pydantic import BaseModel


# The current weather schema to define the structure that is returned to the client
class CurrentWeather(BaseModel):
    id: int
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    conditions: str
    wind_speed: float
    wind_direction: int


class ForecastItems(BaseModel):
    date_string: str
    temperature: float
    feels_like: float
    conditions: str
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    cloud_cover_percent: float
    chance_of_precipitation: float
    wind_speed: float
    wind_direction: int


# The forecast weather schema to define the structure that is returned to the client
class ForecastWeather(BaseModel):
    id: int
    forecast_list: list[ForecastItems]
