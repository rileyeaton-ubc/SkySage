# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Controller for ai endpoints to get data from the model, run
#              operations on it, and then pass it back to the router for returning
#
# Author: Riley Eaton
# Date: 2024-12-01
# *************************************************************************************
from app.models.ai_model import (
    gpt_generation_request,
)
from app.schemas.weather_schema import ForecastWeather
from fastapi import HTTPException


# Function to get an ai generation for the current weather forecast
# Expects a forecasted weather object, which is returned from /api/weather/forecast
def get_weather_forecast_generation(forecast_object: ForecastWeather):
    try:
        # Set the beginning of the prompt
        full_prompt = "Here is the 5 day forecasted weather, please produce a palatable summary for it: "
        # Loop through each item in the forecast list
        forecast_list = forecast_object.forecast_list
        for i in range(len(forecast_list)):
            curr_json = forecast_list[i].model_dump_json
            full_prompt = full_prompt + f"Forecast [${i}]: ${curr_json}, "

        # Call the ai generation function
        ai_results = gpt_generation_request(full_prompt)

        return ai_results["choices"][0]["message"]["content"]
    except Exception as e:
        print(e)
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500,
            detail=f"Get weather forecast generation failed: Internal Server Error",
        )
