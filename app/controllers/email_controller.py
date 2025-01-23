# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Controller for email endpoints to get data from the model, run
#              operations on it, and then pass it back to the router for returning
#
# Author: Riley Eaton
# Date: 2024-12-02
# *************************************************************************************
from app.models.email_model import send_single_email
from app.schemas.email_schema import BasicEmail
from fastapi import HTTPException


# Function to send a basic email to a user
# Expects a basic email object
def send_basic_email(email_data: BasicEmail):
    try:
        # Call the email model function to send an email
        email_send_result = send_single_email(
            email_data.to, email_data.subject, email_data.body
        )
        print(email_send_result)
        return email_send_result
    except Exception as e:
        print(e)
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500,
            detail=f"Sending email failed: Internal Server Error",
        )
