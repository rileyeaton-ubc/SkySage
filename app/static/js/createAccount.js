import { api_routes } from "./api_routes.js";

function validateCreateAccountForm() {
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const errorMessage = document.getElementById("errorMessage");

    // Validate required fields
    if (!username || !email || !password || !confirmPassword) {
        errorMessage.textContent = "All fields are required.";
       // alert(errorMessage.textContent);
        return false;
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        errorMessage.textContent = "Please enter a valid email address.";
      //  alert(errorMessage.textContent);
        return false;
    }

    // Validate password strength (minimum 8 characters, at least one letter and one number)
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!passwordRegex.test(password)) {
        errorMessage.textContent = "Password must be at least 8 characters long and include at least one letter and one number.";
      //  alert(errorMessage.textContent);
        return false;
    }

    // Validate password confirmation
    if (password !== confirmPassword) {
        errorMessage.textContent = "Passwords do not match.";
      //  alert(errorMessage.textContent);
        return false;
    }

    errorMessage.textContent = "";
    return true;
}

function sendDataToDataBase() {
    if (validateCreateAccountForm()) {
        // Create a new request to the database
        // Store the new values for username, email, and password
        // Redirect to the home page
    }
}

module.exports = { validateCreateAccountForm };
