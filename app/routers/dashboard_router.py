# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Router for dashboard
#
# Author: Kai Gehry
# Date: 2024-12-02
# *************************************************************************************

from fastapi import APIRouter, Depends, Query

from app.schemas.dashboard_schema import (
    LocationSearch,
    ViewLocations,
    RemoveLocation,
    GetDashboardId,
)

from app.controllers.dashboard_controller import (
    save_location_controller,
    view_saved_locations_controller,
    remove_saved_location_controller,
    get_dashboard_id_controller,
)


# Initialize APIRouter instance for all /weather routes
router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


# Define a function to get the dashboard id from query parameters
def get_saved_locations(dashboard_id: int = Query(...)) -> ViewLocations:
    return ViewLocations(dashboard_id=dashboard_id)


# Define a function to get the user id from query parameters
def get_dashboard_id(user_id: int = Query(...)) -> GetDashboardId:
    return GetDashboardId(user_id=user_id)


# Route to save a new location
# Expect a LocationSearch object as query parameter
# /save/location
@router.post("/save/location")
def save_new_location(save_location: LocationSearch):
    return {"result": save_location_controller(save_location)}


# Route to get a user's saved locations
# Expect a ViewLocations object as query parameter
# /view/saved/locations
@router.get("/view/saved/locations")
def view_locations(dashboard_id: ViewLocations = Depends(get_saved_locations)):
    return view_saved_locations_controller(dashboard_id)


# Route to remove a saved location
# Expect a RemoveLocation object as query parameter
# /remove/location
@router.post("/remove/location")
def remove_existing_location(remove_location_data: RemoveLocation):
    return {"result": remove_saved_location_controller(remove_location_data)}


# Route to get a user's dashboard id
# Expect a GetDashboardId object as query parameter
# /get/dashboardId
@router.get("/get/dashboardId")
def get_dash_id(user_id: GetDashboardId = Depends(get_dashboard_id)):
    return get_dashboard_id_controller(user_id)
