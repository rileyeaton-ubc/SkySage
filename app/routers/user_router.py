# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Router for user controller
#
# Author: Kai Gehry
# Date: 2024-12-02
# *************************************************************************************

from fastapi import APIRouter, Depends, Query
from app.schemas.user_schema import (
    UserDetails,
    UpdateEmail,
    UpdatePassword,
    CreateAccount,
    GetOrRemove,
)
from app.controllers.user_controller import (
    verify_user_login_controller,
    create_new_account_controller,
    update_email_controller,
    update_password_controller,
    delete_account_controller,
    get_user_id_controller,
    get_user_email_controller,
)


# Initialize APIRouter instance for all /weather routes
router = APIRouter(prefix="/api/user", tags=["user"])


# Define a function to get user details from query params
def get_user_details(
    user_name: str = Query(...), user_password: str = Query(...)
) -> UserDetails:
    return UserDetails(user_name=user_name, user_password=user_password)


# Define a function to get user name or email from query params
def get_user_data(user_name: str = Query(...)) -> GetOrRemove:
    return GetOrRemove(user_name=user_name)


# Route to vefify login details
# Expect a UserDetails object as query parameter
# /verify/login
@router.get("/verify/login")
def is_verified(user_details: UserDetails = Depends(get_user_details)):
    return verify_user_login_controller(user_details)


# Route to udpate a user's email
# Expect a UserDetails object as query parameter
# /update/email
@router.post("/update/email")
def update_email(user_email_update: UpdateEmail):
    return {"result": update_email_controller(user_email_update)}


# Route to udpate a user's password
# Expect a UpdatePassword object as query parameter
# /update/password
@router.post("/update/password")
def update_password(user_password_update: UpdatePassword):
    return {"result": update_password_controller(user_password_update)}


# Route to create a new user account
# Expect a CreateAccount object as query parameter
# /create/account
@router.post("/create/account")
def create_new_account(create_user_account: CreateAccount):
    return {"result": create_new_account_controller(create_user_account)}


# Route to delete an existing account
# Expect a RemoveUser object as query parameter
# /remove/user
@router.post("/remove/user")
def delete_user_account(user_name: GetOrRemove):
    return {"result": delete_account_controller(user_name)}


# Route to get a user's user id
# Expect a GetUserId object as query parameter
# /get/userid
@router.get("/get/userid")
def get_id_for_user(user_name: GetOrRemove = Depends(get_user_data)):
    return get_user_id_controller(user_name)


# Route to get a user's email
# Expect a GetUserEmail object as query parameter
# /get/userEmail
@router.get("/get/userEmail")
def get_email_for_user(user_name: GetOrRemove = Depends(get_user_data)):
    return get_user_email_controller(user_name)
