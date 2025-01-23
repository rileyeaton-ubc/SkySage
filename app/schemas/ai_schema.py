# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Schema for all ai-related data structures to be used, to keep all
#              data consistent
#
# Author: Riley Eaton
# Date: 2024-12-01
# *************************************************************************************

from pydantic import BaseModel


# The ai schema to describe a basic generation output
class BasicGeneration(BaseModel):
    generated_text: str
