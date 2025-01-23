# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Router for email functions that handles incoming requests and return
#              responses from the controller(s)
#
# Author: Riley Eaton
# Date: 2024-12-02
# *************************************************************************************

from fastapi import APIRouter
from app.schemas.email_schema import BasicEmail
from app.schemas.shared_schema import SuccessStatus
from app.controllers.email_controller import send_basic_email

# Initialize APIRouter instance for all /api/email routes
router = APIRouter(prefix="/api/email", tags=["ai"])


# Route to send a basic email to a user
# Expect a basic email object as query parameter
# email/send
@router.post("/send")
def forecast_generation(email_data: BasicEmail):
    # Call and return the send_basic_email function from the email controller
    send_email_result = send_basic_email(email_data)
    return {"success": send_email_result != None}
