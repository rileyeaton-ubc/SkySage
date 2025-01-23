# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Model for emails to send off using Mailgun and pass back success or fail
#
# Author: Riley Eaton
# Date: 2024-12-02
# *************************************************************************************

from app.common.http_services import HttpClient
from app.config.global_config import global_settings
import base64

# Initialize the Mailgun URL and HTTP client
http_client = HttpClient(
    base_url=f"https://api.mailgun.net/v3/{global_settings.MAILGUN_SANDBOX_ID}",
)


# Send a basic email to one email address
# Parameters:
#   => email_to (str): The address to send the email to
#   => subject (str): String that contains what is required in the email subject line
#   => body (str): String that contains everything required in the email body
def send_single_email(email_to, subject, body):
    # Create the form data for the HTTP request
    form_data = {
        "from": global_settings.MAILGUN_FROM_EMAIL,
        "to": email_to,
        "subject": subject,
        "text": body,
    }
    # Set the correct encoding for basic auth
    credentials = f"api:{global_settings.MAILGUN_API_KEY}"
    encoded_credentials = base64.b64encode(credentials.encode("ascii")).decode("ascii")

    # Use the HTTP client to make a POST request to the Mailgun API
    return http_client.post(
        endpoint="/messages",
        data=form_data,
        headers={
            "Authorization": f"Basic {encoded_credentials}",
        },
        form_data=True,
    )
