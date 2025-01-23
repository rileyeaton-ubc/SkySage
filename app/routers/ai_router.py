# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Router for ai generation that handles incoming requests and return
#              responses from the controller(s)
#
# Author: Riley Eaton
# Date: 2024-12-01
# *************************************************************************************

from fastapi import APIRouter
from app.schemas.weather_schema import ForecastWeather
from app.controllers.ai_controller import get_weather_forecast_generation

# Initialize APIRouter instance for all /api/ai routes
router = APIRouter(prefix="/api/ai", tags=["ai"])


# Route to get the ai summary of forecasted weather
# Expect a forecasted weather object as query parameter
# ai/generate/forecast
@router.post("/generate/forecast")
def forecast_generation(forecast: ForecastWeather):
    # Call and return the get_weather_forecast_generation function from the ai controller
    return {
        "ai_generation": get_weather_forecast_generation(forecast),
    }
