# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Model for ai generation to get data from the OpenAI API and pass it back
#
# Author: Riley Eaton
# Date: 2024-12-01
# *************************************************************************************

from app.common.http_services import HttpClient
from app.config.global_config import global_settings

# Initialize the Google API key and HTTP client
http_client = HttpClient(
    base_url="https://api.openai.com/v1",
    headers={"Content-Type": "application/json"},
)


# Get an ai generated response by one of OpenAI's models
# Parameters:
#   => prompt (str): String to pass to the model that will generate a response
def gpt_generation_request(prompt):
    body = {
        "model": global_settings.AI_DEFAULT_MODEL,
        "messages": [
            {
                "role": "system",
                "content": global_settings.AI_FORECAST_WEATHER_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    }
    # Use the HTTP client to make a POST request to the Google API
    return http_client.post(
        endpoint="/chat/completions",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {global_settings.OPENAI_API_KEY}",
        },
    )
