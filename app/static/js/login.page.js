import { api_routes } from "./api_routes.js";

function validateLoginForm() {

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const errorMessage = document.getElementById("errorMessage");

    if (!username || !password) {
        errorMessage.textContent = "Both username and password are required.";
       // alert(errorMessage.textContent);
        return false;
    }

    errorMessage.textContent = "";
    return true;
}

function sendDataToDataBase() {

    if(validateLoginForm()){
        //create a new request to data base
        // Store the new values for username and password
        // Redirect to the home page

    }
}

module.exports = { validateLoginForm };