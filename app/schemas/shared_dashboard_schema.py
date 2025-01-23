# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Schema for all shared dashboard db related data structures to be used, to keep all
#              data consistent for a shared dashboard
#
# Author: Kai Gehry
# Date: 2024-12-02
# *************************************************************************************

from pydantic import BaseModel


# The add shared user schema for sharing to a user
class AddSharedUser(BaseModel):
    shared_dashboard_id: int
    shared_to_user_id: int
    shared_from_user_id: int


# The remove shared to user schema for unsharing
class ShareId(BaseModel):
    share_id: int


# The get ids schema for retrieving shared to user ids and share ids
class GetIds(BaseModel):
    shared_dashboard_id: int


# The get share id schema for retrieving a share id
class GetShareId(BaseModel):
    shared_from_user_id: int
    shared_to_user_id: int


# The shared ids list schema for retrieving shared to user ids
class SharedIdsList(BaseModel):
    shared_user_ids: list
