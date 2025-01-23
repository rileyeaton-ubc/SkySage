// *************************************************************************************
// COSC 310 Project - SkySage

// Description: Functions to allow for backend function acess for frontend

// Author(s): Riley Eaton and Kai Gehry
// Date: 2024-12-03
// *************************************************************************************


import { api_routes } from "./api_routes.js";


//  Function to check if user has an account/verify login information
const verifyUser = async (user_name, user_password) => {
  try {
    const response = await axios.get(api_routes.BASE_DOMAIN+api_routes.VERIFY_USER_ENDPOINT, {
      params: {user_name, user_password},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to verify user:", error);
  }
};

//  Function to create a new user account
const createNewAccount = async (user_name, user_password, user_email) => {
  try {
    const response = await axios.post(api_routes.BASE_DOMAIN+api_routes.CREATE_NEW_USER_ENDPOINT, {
      params: {user_name, user_password, user_email},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to create new account:", error);
  }
};

//  Function to update/change a user's email
const updateUserEmail = async (user_name, new_user_email) => {
  try {
    const response = await axios.post(api_routes.BASE_DOMAIN+api_routes.UPDATE_EMAIL_ENDPOINT, {
      params: {user_name, new_user_email},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to update user email:", error);
  }
};

//  Function to update/change a user's password
const updateUserPassword = async (user_name, new_user_password) => {
  try {
    const response = await axios.post(api_routes.BASE_DOMAIN+api_routes.UPDATE_PASSWORD_ENDPOINT, {
      params: {user_name, new_user_password},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to update user password:", error);
  }
};

//  Function to delete a user account
const deleteUserAccount = async (user_name) => {
  try {
    const response = await axios.post(api_routes.BASE_DOMAIN+api_routes.REMOVE_USER_ENDPOINT, {
      params: {user_name},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to delete user account:", error);
  }
};

//  Function to retrieve a user's id
const getUserId= async (user_name) => {
  try {
    const response = await axios.get(api_routes.BASE_DOMAIN+api_routes.GET_USER_ID_ENDPOINT, {
      params: {user_name},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to retrieve user id:", error);
  }
};

//  Function to retrieve a user's email
const getUserEmail= async (user_name) => {
  try {
    const response = await axios.get(api_routes.BASE_DOMAIN+api_routes.GET_USER_EMAIL_ENDPOINT, {
      params: {user_name},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to retrieve user email:", error);
  }
};

//  Function to share a dashboard with another user
const shareDashboard= async (shared_dashboard_id, shared_to_user_id, shared_from_user_id) => {
  try {
    const response = await axios.post(api_routes.BASE_DOMAIN+api_routes.ADD_SHARED_TO_USER_ENDPOINT, {
      params: {shared_dashboard_id, shared_to_user_id, shared_from_user_id},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to share dashboard:", error);
  }
};

//  Function to unshare a dashboard
const unshareDashboard= async (share_id) => {
  try {
    const response = await axios.post(api_routes.BASE_DOMAIN+api_routes.REMOVE_SHARED_TO_USER_ENDPOINT, {
      params: {share_id},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to unshare dashboard:", error);
  }
};

//  Function to retrieve user ids a dashboard has been shared with
const getSharedToUserIds= async (shared_dashboard_id) => {
  try {
    const response = await axios.get(api_routes.BASE_DOMAIN+api_routes.GET_SHARED_TO_USER_IDS_ENDPOINT, {
      params: {shared_dashboard_id},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to retrieve user ids:", error);
  }
};

//  Function to retrieve user the share id for a particular share instance
const getShareId= async (shared_from_user_id, shared_to_user_id) => {
  try {
    const response = await axios.get(api_routes.BASE_DOMAIN+api_routes.GET_SHARE_ID_ENDPOINT, {
      params: {shared_from_user_id, shared_to_user_id},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to retrieve share id:", error);
  }
};

//  Function to save a location to a dashboard
const saveLocation= async (dashboard_id, location_name) => {
  try {
    const response = await axios.post(api_routes.BASE_DOMAIN+api_routes.SAVE_LOCATION_ENDPOINT, {
      params: {dashboard_id, location_name},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to save location:", error);
  }
};

//  Function to retrieve saved locations
const getSavedLocations= async (dashboard_id) => {
  try {
    const response = await axios.get(api_routes.BASE_DOMAIN+api_routes.GET_SAVED_LOCATIONS_ENDPOINT, {
      params: {dashboard_id},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to retrieve saved locations:", error);
  }
};

//  Function to remove a saved location
const removeSavedLocation= async (dashboard_id, location_name) => {
  try {
    const response = await axios.post(api_routes.BASE_DOMAIN+api_routes.REMOVE_LOCATION_ENDPOINT, {
      params: {dashboard_id, location_name},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to remove saved location:", error);
  }
};

//  Function to retrieve a user's dashboard id
const getDashboardId= async (user_id) => {
  try {
    const response = await axios.get(api_routes.BASE_DOMAIN+api_routes.GET_DASHBOARD_ID_ENDPOINT, {
      params: {user_id},
    });
    return response.data;
  } catch (error) {
    console.error("Failed to retrieve dashboard id:", error);
  }
};

// Function to fetch data from the backend
const fetchLocationCurrentWeather = async (latitude, longitude) => {
  try {
    const response = await axios.get(api_routes.BASE_DOMAIN+api_routes.LOCATION_CURRENT_WEATHER, {
      params: { latitude, longitude },
    });
    return response.data;
  } catch (error) {
    console.error("Failed to fetch current weather:", error);
  }
};

// Function to fetch data from the backend
const fetchLocationForecastWeather = async (latitude, longitude) => {
  try {
    const response = await axios.get(api_routes.BASE_DOMAIN+api_routes.LOCATION_FORECAST_WEATHER, {
      params: { latitude, longitude },
    });
    return response.data;
  } catch (error) {
    console.error("Failed to fetch weather forecast:", error);
  }
};

// Function to fetch an ai generation (summary) from the backend
const fetchForecastAIGeneration = async (forecast) => {
  try {
    const response = await axios.post(api_routes.BASE_DOMAIN+api_routes.AI_FORECAST_GENERATION_ENDPOINT, 
      forecast,
    );
    return response.data;
  } catch (error) {
    console.error("Failed to fetch weather forecast:", error);
  }
};

// Function to send a basic email
const sendBasicEmail = async (to, subject, body) => {
  try {
    const response = await axios.post(api_routes.BASE_DOMAIN+api_routes.SEND_EMAIL_ENDPOINT, 
      { to, subject, body },
    );
    return response.data;
  } catch (error) {
    console.error("Failed to send email:", error);
  }
}

export {fetchLocationCurrentWeather, fetchLocationForecastWeather, fetchForecastAIGeneration, sendBasicEmail, verifyUser, createNewAccount, updateUserEmail, updateUserPassword, deleteUserAccount, getUserId, 
  getUserEmail, shareDashboard, unshareDashboard, getSharedToUserIds, getShareId, saveLocation, getSavedLocations, 
  removeSavedLocation, getDashboardId }