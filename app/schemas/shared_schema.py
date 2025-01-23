# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Schema for shared data structures to be used anywhere accross the app,
#              to keep all data consistent
#
# Author: Riley Eaton
# Date: 2024-12-02
# *************************************************************************************

from pydantic import BaseModel


# The schema that describes a basic success return
class SuccessStatus(BaseModel):
    success: bool
