# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Schema for all location-related data structures to be used, to keep all
#              data consistent
#
# Author: Riley Eaton
# Date: 2024-11-25
# *************************************************************************************

from pydantic import BaseModel
from typing import List


# The location schema to describe its longitude and latitude
class Location(BaseModel):
    latitude: float
    longitude: float


# The location name schema to describe just a location name
class LocationName(BaseModel):
    name: str


# The location list schema to describe a list of locations
class LocationList(BaseModel):
    locations: List[LocationName]


# The location search schema to define the structure that the client must use for search
class LocationSearch(BaseModel):
    search: str
