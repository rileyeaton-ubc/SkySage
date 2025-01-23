# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Schema for all email-related data structures to be used, to keep all
#              data consistent
#
# Author: Riley Eaton
# Date: 2024-12-02
# *************************************************************************************

from pydantic import BaseModel


# The email schema to describe a basic email format, the bare minimum to send
class BasicEmail(BaseModel):
    to: str
    subject: str
    body: str
