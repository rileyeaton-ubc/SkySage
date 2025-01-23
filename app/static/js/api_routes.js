// ***********************************************************************************
// COSC 310 Project - SkySage
//
// Description: This config file that contains the API routes for the front-end to
//              communicate with the back-end. 
//
// Author: Riley Eaton
// Date: 11/29/2024
// ***********************************************************************************
export var api_routes = {
  BASE_DOMAIN: "http://localhost:8000",
  LOCATION_CURRENT_WEATHER: "/api/weather/current",
  LOCATION_FORECAST_WEATHER: "/api/weather/forecast",
  LOCATION_COORDINATES_ENDPOINT: "/api/location/coordinates",
  AUTOCOMPLETE_LOCATIONS_ENDPOINT: "/api/location/autocomplete",
  AI_FORECAST_GENERATION_ENDPOINT: "/api/ai/generate/forecast",
  SEND_EMAIL_ENDPOINT: "/api/email/send",
  VERIFY_USER_ENDPOINT: "/api/user/verify/login", 
  CREATE_NEW_USER_ENDPOINT: "/api/user/create/account", 
  UPDATE_EMAIL_ENDPOINT: "/api/user/update/email", 
  UPDATE_PASSWORD_ENDPOINT: "/api/user/update/password", 
  REMOVE_USER_ENDPOINT: "/api/user/remove/user",
  GET_USER_ID_ENDPOINT: "/api/user/get/userid", 
  GET_USER_EMAIL_ENDPOINT: "/api/user/get/userEmail", 
  ADD_SHARED_TO_USER_ENDPOINT: "/api/shared-dashboard/share-with/user", 
  REMOVE_SHARED_TO_USER_ENDPOINT: "/api/shared-dashboard/remove/share-to/user", 
  GET_SHARED_TO_USER_IDS_ENDPOINT: "/api/shared-dashboard/get/shared-to/ids", 
  GET_SHARE_ID_ENDPOINT: "/api/shared-dashboard/get/shareId", 
  SAVE_LOCATION_ENDPOINT: "/api/dashboard/save/location", 
  GET_SAVED_LOCATIONS_ENDPOINT: "/api/dashboard/view/saved/locations", 
  REMOVE_LOCATION_ENDPOINT: "/api/dashboard/remove/location", 
  GET_DASHBOARD_ID_ENDPOINT: "/api/dashboard/get/dashboardId"

}
