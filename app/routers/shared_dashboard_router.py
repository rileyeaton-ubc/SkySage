# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Router for shared dashboard
#
# Author: Kai Gehry
# Date: 2024-12-02
# *************************************************************************************

from fastapi import APIRouter, Depends, Query

from app.schemas.shared_dashboard_schema import (
    AddSharedUser,
    ShareId,
    GetIds,
    GetShareId,
)

from app.controllers.shared_dashboard_controller import (
    add_shared_to_user_controller,
    remove_shared_to_user_controller,
    get_shared_to_user_ids_controller,
    get_share_id_controller,
)


# Initialize APIRouter instance for all /weather routes
router = APIRouter(prefix="/api/shared-dashboard", tags=["shared-dashboard"])


# Define a function to get a shared dashboard id from query parameters
def get_ids(shared_dashboard_id: int = Query(...)) -> GetIds:
    return GetIds(shared_dashboard_id=shared_dashboard_id)


# Define a function to get shared from user id and shared to user id from query parameters
def get_share_ids(
    shared_from_user_id: int = Query(...), shared_to_user_id: int = Query(...)
) -> GetShareId:
    return GetShareId(
        shared_from_user_id=shared_from_user_id,
        shared_to_user_id=shared_to_user_id,
    )


# Route to share a dashboard with a user
# Expect an AddSharedUser object as query parameter
# /share-with/user
@router.post("/share-with/user")
def share_with_user(share_with_data: AddSharedUser):
    return {"result": add_shared_to_user_controller(share_with_data)}


# Route to unshare a dashboard with a user
# Expect a ShareId object as query parameter
# /remove/share-to/user
@router.post("/remove/share-to/user")
def remove_share_to_user(removal_data: ShareId):
    return {"result": remove_shared_to_user_controller(removal_data)}


# Route to get the ids of shared to users for a dashboard
# Expect a GetIds object as query parameter
# /get/shared-to/ids
@router.get("/get/shared-to/ids")
def get_user_ids(user_id_details: GetIds = Depends(get_ids)):
    return get_shared_to_user_ids_controller(user_id_details)


# Route to get the share id of a particular share instance
# Expect a GetIds object as query parameter
# /get/shareId
@router.get("/get/shareId")
def get_share_id(share_id_details: GetShareId = Depends(get_share_ids)):
    return get_share_id_controller(share_id_details)
