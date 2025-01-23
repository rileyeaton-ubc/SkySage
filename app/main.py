# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Root of the FastAPI application to define the main application and
#              include the sub-routers for all API routes
#
# Author: Riley Eaton
# Date: 2024-11-25
# *************************************************************************************

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import (
    weather_router,
    location_router,
    ai_router,
    email_router,
    user_router,
    dashboard_router,
    shared_dashboard_router,
)

# Initialize FastAPI app
app = FastAPI()

# Ensure any origin, method, or header is allowed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(weather_router.router)
app.include_router(location_router.router)
app.include_router(user_router.router)
app.include_router(dashboard_router.router)
app.include_router(shared_dashboard_router.router)
app.include_router(ai_router.router)
app.include_router(email_router.router)


# Base api endpoint to check if the backend is working
@app.get("/api")
def root_message():
    return {"message": "Successful query to the SkySage API"}
