# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Schema for all user db related data structures to be used, to keep all
#              data consistent for the user controller
#
# Author: Kai Gehry
# Date: 2024-12-02
# *************************************************************************************

from pydantic import BaseModel


# The user detail schema for verifying user login
class UserDetails(BaseModel):
    user_name: str
    user_password: str


# The create account schema for creating a new account
class CreateAccount(BaseModel):
    user_name: str
    user_password: str
    user_email: str


# The update email schema for updating an email
class UpdateEmail(BaseModel):
    user_name: str
    new_user_email: str


# The update password schema for updating a password
class UpdatePassword(BaseModel):
    user_name: str
    new_user_password: str


# The get or remove schema for retrieving a user email, retrieving a user id, or deleting an account
class GetOrRemove(BaseModel):
    user_name: str


class GetUserId(BaseModel):
    user_id: int


class GetUserEmail(BaseModel):
    user_email: str
