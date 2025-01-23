# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Schema for all dashboard db related data structures to be used, to keep all
#              data consistent for the dashboard
#
# Author: Kai Gehry
# Date: 2024-12-02
# *************************************************************************************

from pydantic import BaseModel


# The location search schema for adding a location to a dashboard
class LocationSearch(BaseModel):
    dashboard_id: int
    location_name: str


# likely need to combine this
# The view location schema for viewing all saved locations for a given dashboard
class ViewLocations(BaseModel):
    dashboard_id: int


# added for testing refactor
class ReturnedLocation(BaseModel):
    saved_locations: list


# The remove location schema for reamoving a saved locations from a given dashboard
class RemoveLocation(BaseModel):
    dashboard_id: int
    location_name: str


# The get dashboard id schema for retrieveing a dashboard id for a given user
class GetDashboardId(BaseModel):
    user_id: int
